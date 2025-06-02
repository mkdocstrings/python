# This module implements rendering utilities.

from __future__ import annotations

import random
import re
import string
import subprocess
import sys
import warnings
from collections import defaultdict
from contextlib import suppress
from dataclasses import replace
from functools import lru_cache
from pathlib import Path
from re import Match, Pattern
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Literal, TypeVar

from griffe import (
    Alias,
    AliasResolutionError,
    CyclicAliasError,
    DocstringAttribute,
    DocstringClass,
    DocstringFunction,
    DocstringModule,
    DocstringSectionAttributes,
    DocstringSectionClasses,
    DocstringSectionFunctions,
    DocstringSectionModules,
    Object,
)
from jinja2 import TemplateNotFound, pass_context, pass_environment
from markupsafe import Markup
from mkdocs_autorefs import AutorefsHookInterface, Backlink, BacklinkCrumb
from mkdocstrings import get_logger

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator, Sequence

    from griffe import Attribute, Class, Function, Module
    from jinja2 import Environment
    from jinja2.runtime import Context
    from mkdocstrings import CollectorItem

_logger = get_logger(__name__)


def _sort_key_alphabetical(item: CollectorItem) -> str:
    # `chr(sys.maxunicode)` is a string that contains the final unicode character,
    # so if `name` isn't found on the object, the item will go to the end of the list.
    return item.name or chr(sys.maxunicode)


def _sort_key_source(item: CollectorItem) -> float:
    # If `lineno` is none, the item will go to the end of the list.
    if item.is_alias:
        return item.alias_lineno if item.alias_lineno is not None else float("inf")
    return item.lineno if item.lineno is not None else float("inf")


def _sort__all__(item: CollectorItem) -> float:  # noqa: ARG001
    raise ValueError("Not implemented in public version of mkdocstrings-python")


Order = Literal["__all__", "alphabetical", "source"]
"""Ordering methods.

- `__all__`: order members according to `__all__` module attributes, if declared;
- `alphabetical`: order members alphabetically;
- `source`: order members as they appear in the source file.
"""

_order_map: dict[str, Callable[[Object | Alias], str | float]] = {
    "alphabetical": _sort_key_alphabetical,
    "source": _sort_key_source,
    "__all__": _sort__all__,
}


def do_format_code(code: str, line_length: int) -> str:
    """Format code.

    Parameters:
        code: The code to format.
        line_length: The line length.

    Returns:
        The same code, formatted.
    """
    code = code.strip()
    if len(code) < line_length:
        return code
    formatter = _get_formatter()
    return formatter(code, line_length)


class _StashCrossRefFilter:
    stash: ClassVar[dict[str, str]] = {}

    @staticmethod
    def _gen_key(length: int) -> str:
        return "_" + "".join(random.choice(string.ascii_letters + string.digits) for _ in range(max(1, length - 1)))  # noqa: S311

    def _gen_stash_key(self, length: int) -> str:
        key = self._gen_key(length)
        while key in self.stash:
            key = self._gen_key(length)
        return key

    def __call__(self, crossref: str, *, length: int) -> str:
        key = self._gen_stash_key(length)
        self.stash[key] = crossref
        return key


do_stash_crossref = _StashCrossRefFilter()
"""Filter to stash cross-references (and restore them after formatting and highlighting)."""


def _format_signature(name: Markup, signature: str, line_length: int) -> str:
    name = str(name).strip()  # type: ignore[assignment]
    signature = signature.strip()
    if len(name + signature) < line_length:
        return name + signature

    # Black cannot format names with dots, so we replace
    # the whole name with a string of equal length
    name_length = len(name)
    formatter = _get_formatter()
    formatable = f"def {'x' * name_length}{signature}: pass"
    formatted = formatter(formatable, line_length)

    # We put back the original name
    # and remove starting `def ` and trailing `: pass`
    return name + formatted[4:-5].strip()[name_length:-1]


@pass_context
def do_format_signature(
    context: Context,
    callable_path: Markup,
    function: Function,
    line_length: int,
    *,
    annotations: bool | None = None,
    crossrefs: bool = False,  # noqa: ARG001
) -> str:
    """Format a signature.

    Parameters:
        context: Jinja context, passed automatically.
        callable_path: The path of the callable we render the signature of.
        function: The function we render the signature of.
        line_length: The line length.
        annotations: Whether to show type annotations.
        crossrefs: Whether to cross-reference types in the signature.

    Returns:
        The same code, formatted.
    """
    env = context.environment
    # YORE: Bump 2: Replace `do_get_template(env, "signature")` with `"signature.html.jinja"` within line.
    template = env.get_template(do_get_template(env, "signature"))

    if annotations is None:
        new_context = context.parent
    else:
        new_context = dict(context.parent)
        new_context["config"] = replace(new_context["config"], show_signature_annotations=annotations)

    signature = template.render(new_context, function=function, signature=True)
    signature = _format_signature(callable_path, signature, line_length)
    signature = str(
        env.filters["highlight"](
            Markup.escape(signature),
            language="python",
            inline=False,
            classes=["doc-signature"],
            linenums=False,
        ),
    )

    # Since we highlight the signature without `def`,
    # Pygments sees it as a function call and not a function definition.
    # The result is that the function name is not parsed as such,
    # but instead as a regular name: `n` CSS class instead of `nf`.
    # When the function name is a known special name like `__exit__`,
    # Pygments will set an `fm` (function -> magic) CSS class.
    # To fix this, we replace the CSS class in the first span with `nf`,
    # unless we already found an `nf` span.
    if not re.search(r'<span class="nf">', signature):
        signature = re.sub(r'<span class="[a-z]{1,2}">', '<span class="nf">', signature, count=1)

    if stash := env.filters["stash_crossref"].stash:
        for key, value in stash.items():
            signature = re.sub(rf"\b{key}\b", value, signature)
        stash.clear()

    return signature


@pass_context
def do_format_attribute(
    context: Context,
    attribute_path: Markup,
    attribute: Attribute,
    line_length: int,
    *,
    crossrefs: bool = False,  # noqa: ARG001
) -> str:
    """Format an attribute.

    Parameters:
        context: Jinja context, passed automatically.
        attribute_path: The path of the callable we render the signature of.
        attribute: The attribute we render the signature of.
        line_length: The line length.
        crossrefs: Whether to cross-reference types in the signature.

    Returns:
        The same code, formatted.
    """
    env = context.environment
    # YORE: Bump 2: Replace `do_get_template(env, "expression")` with `"expression.html.jinja"` within line.
    template = env.get_template(do_get_template(env, "expression"))
    annotations = context.parent["config"].show_signature_annotations

    signature = str(attribute_path).strip()
    if annotations and attribute.annotation:
        annotation = template.render(
            context.parent,
            expression=attribute.annotation,
            signature=True,
            backlink_type="returned-by",
        )
        signature += f": {annotation}"
    if attribute.value:
        value = template.render(context.parent, expression=attribute.value, signature=True, backlink_type="used-by")
        signature += f" = {value}"

    signature = do_format_code(signature, line_length)
    signature = str(
        env.filters["highlight"](
            Markup.escape(signature),
            language="python",
            inline=False,
            classes=["doc-signature"],
            linenums=False,
        ),
    )

    if stash := env.filters["stash_crossref"].stash:
        for key, value in stash.items():
            signature = re.sub(rf"\b{key}\b", value, signature)
        stash.clear()

    return signature


def do_order_members(
    members: Sequence[Object | Alias],
    order: Order | list[Order],
    members_list: bool | list[str] | None,
) -> Sequence[Object | Alias]:
    """Order members given an ordering method.

    Parameters:
        members: The members to order.
        order: The ordering method.
        members_list: An optional member list (manual ordering).

    Returns:
        The same members, ordered.
    """
    if isinstance(members_list, list) and members_list:
        sorted_members = []
        members_dict = {member.name: member for member in members}
        for name in members_list:
            if name in members_dict:
                sorted_members.append(members_dict[name])
        return sorted_members
    if isinstance(order, str):
        order = [order]
    for method in order:
        with suppress(ValueError):
            return sorted(members, key=_order_map[method])
    return members


# YORE: Bump 2: Remove block.
@lru_cache
def _warn_crossref() -> None:
    warnings.warn(
        "The `crossref` filter is deprecated and will be removed in a future version",
        DeprecationWarning,
        stacklevel=1,
    )


# YORE: Bump 2: Remove block.
def do_crossref(path: str, *, brief: bool = True) -> Markup:
    """Deprecated. Filter to create cross-references.

    Parameters:
        path: The path to link to.
        brief: Show only the last part of the path, add full path as hover.

    Returns:
        Markup text.
    """
    _warn_crossref()
    full_path = path
    if brief:
        path = full_path.split(".")[-1]
    return Markup("<autoref identifier={full_path} optional hover>{path}</autoref>").format(
        full_path=full_path,
        path=path,
    )


# YORE: Bump 2: Remove block.
@lru_cache
def _warn_multi_crossref() -> None:
    warnings.warn(
        "The `multi_crossref` filter is deprecated and will be removed in a future version",
        DeprecationWarning,
        stacklevel=1,
    )


# YORE: Bump 2: Remove block.
def do_multi_crossref(text: str, *, code: bool = True) -> Markup:
    """Deprecated. Filter to create cross-references.

    Parameters:
        text: The text to scan.
        code: Whether to wrap the result in a code tag.

    Returns:
        Markup text.
    """
    _warn_multi_crossref()
    group_number = 0
    variables = {}

    def repl(match: Match) -> str:
        nonlocal group_number
        group_number += 1
        path = match.group()
        path_var = f"path{group_number}"
        variables[path_var] = path
        return f"<autoref identifier={{{path_var}}} optional hover>{{{path_var}}}</autoref>"

    text = re.sub(r"([\w.]+)", repl, text)
    if code:
        text = f"<code>{text}</code>"
    return Markup(text).format(**variables)  # noqa: S704


_split_path_re = re.compile(r"([.(]?)([\w]+)(\))?")
_splitable_re = re.compile(r"[().]")


def do_split_path(path: str, full_path: str) -> Iterator[tuple[str, str, str, str]]:
    """Split object paths for building cross-references.

    Parameters:
        path: The path to split.
        full_path: The full path, used to compute correct paths for each part of the path.

    Yields:
        4-tuples: prefix, word, full path, suffix.
    """
    # Path is a single word, yield full path directly.
    if not _splitable_re.search(path):
        yield ("", path, full_path, "")
        return

    current_path = ""
    if path == full_path:
        # Split full path and yield directly without storing data in a dict.
        for match in _split_path_re.finditer(full_path):
            prefix, word, suffix = match.groups()
            current_path = f"{current_path}{prefix}{word}{suffix or ''}" if current_path else word
            yield prefix or "", word, current_path, suffix or ""
        return

    # Split full path first to store tuples in a dict.
    elements = {}
    for match in _split_path_re.finditer(full_path):
        prefix, word, suffix = match.groups()
        current_path = f"{current_path}{prefix}{word}{suffix or ''}" if current_path else word
        elements[word] = (prefix or "", word, current_path, suffix or "")

    # Then split path and pick tuples from the dict.
    first = True
    for match in _split_path_re.finditer(path):
        prefix, word, current_path, suffix = elements[match.group(2)]
        yield "" if first else prefix, word, current_path, suffix
        first = False


def _keep_object(name: str, filters: Sequence[tuple[Pattern, bool]]) -> bool:
    keep = None
    rules = set()
    for regex, exclude in filters:
        rules.add(exclude)
        if regex.search(name):
            keep = not exclude
    if keep is None:
        # When we only include stuff, no match = reject.
        # When we only exclude stuff, or include and exclude stuff, no match = keep.
        return rules != {False}
    return keep


def _parents(obj: Alias) -> set[str]:
    parent: Object | Alias = obj.parent  # type: ignore[assignment]
    parents = {obj.path, parent.path}
    if parent.is_alias:
        parents.add(parent.final_target.path)  # type: ignore[union-attr]
    while parent.parent:
        parent = parent.parent
        parents.add(parent.path)
        if parent.is_alias:
            parents.add(parent.final_target.path)  # type: ignore[union-attr]
    return parents


def _remove_cycles(objects: list[Object | Alias]) -> Iterator[Object | Alias]:
    suppress_errors = suppress(AliasResolutionError, CyclicAliasError)
    for obj in objects:
        if obj.is_alias:
            with suppress_errors:
                if obj.final_target.path in _parents(obj):  # type: ignore[arg-type,union-attr]
                    continue
        yield obj


def do_filter_objects(
    objects_dictionary: dict[str, Object | Alias],
    *,
    filters: Sequence[tuple[Pattern, bool]] | Literal["public"] | None = None,
    members_list: bool | list[str] | None = None,
    inherited_members: bool | list[str] = False,
    keep_no_docstrings: bool = True,
) -> list[Object | Alias]:
    """Filter a dictionary of objects based on their docstrings.

    Parameters:
        objects_dictionary: The dictionary of objects.
        filters: Filters to apply, based on members' names, or `"public"`.
            Each element is a tuple: a pattern, and a boolean indicating whether
            to reject the object if the pattern matches.
        members_list: An optional, explicit list of members to keep.
            When given and empty, return an empty list.
            When given and not empty, ignore filters and docstrings presence/absence.
        inherited_members: Whether to keep inherited members or exclude them.
        keep_no_docstrings: Whether to keep objects with no/empty docstrings (recursive check).

    Returns:
        A list of objects.
    """
    inherited_members_specified = False
    if inherited_members is True:
        # Include all inherited members.
        objects = list(objects_dictionary.values())
    elif inherited_members is False:
        # Include no inherited members.
        objects = [obj for obj in objects_dictionary.values() if not obj.inherited]
    else:
        # Include specific inherited members.
        inherited_members_specified = True
        objects = [
            obj for obj in objects_dictionary.values() if not obj.inherited or obj.name in set(inherited_members)
        ]

    if members_list is True:
        # Return all pre-selected members.
        return objects

    if members_list is False or members_list == []:
        # Return selected inherited members, if any.
        return [obj for obj in objects if obj.inherited]

    if members_list is not None:
        # Return selected members (keeping any pre-selected inherited members).
        return [
            obj for obj in objects if obj.name in set(members_list) or (inherited_members_specified and obj.inherited)
        ]

    # Use filters and docstrings.
    if filters == "public":
        objects = [obj for obj in objects if obj.is_public]
    elif filters:
        objects = [
            obj for obj in objects if _keep_object(obj.name, filters) or (inherited_members_specified and obj.inherited)
        ]
    if not keep_no_docstrings:
        objects = [obj for obj in objects if obj.has_docstrings or (inherited_members_specified and obj.inherited)]

    # Prevent infinite recursion.
    if objects:
        objects = list(_remove_cycles(objects))

    return objects


@lru_cache(maxsize=1)
def _get_formatter() -> Callable[[str, int], str]:
    for formatter_function in [
        _get_black_formatter,
        _get_ruff_formatter,
    ]:
        if (formatter := formatter_function()) is not None:
            return formatter

    _logger.info("Formatting signatures requires either Black or Ruff to be installed.")
    return lambda text, _: text


def _get_ruff_formatter() -> Callable[[str, int], str] | None:
    try:
        from ruff.__main__ import find_ruff_bin
    except ImportError:
        return None

    try:
        ruff_bin = find_ruff_bin()
    except FileNotFoundError:
        ruff_bin = "ruff"

    def formatter(code: str, line_length: int) -> str:
        try:
            completed_process = subprocess.run(  # noqa: S603
                [
                    ruff_bin,
                    "format",
                    "--config",
                    f"line-length={line_length}",
                    "--stdin-filename",
                    "file.py",
                    "-",
                ],
                check=True,
                capture_output=True,
                text=True,
                input=code,
            )
        except subprocess.CalledProcessError:
            return code
        else:
            return completed_process.stdout

    return formatter


def _get_black_formatter() -> Callable[[str, int], str] | None:
    try:
        from black import InvalidInput, Mode, format_str
    except ModuleNotFoundError:
        return None

    def formatter(code: str, line_length: int) -> str:
        mode = Mode(line_length=line_length)
        try:
            return format_str(code, mode=mode)
        except InvalidInput:
            return code

    return formatter


# YORE: Bump 2: Remove line.
@pass_environment
# YORE: Bump 2: Replace `env: Environment, ` with `` within line.
# YORE: Bump 2: Replace `str | ` with `` within line.
def do_get_template(env: Environment, obj: str | Object) -> str:
    """Get the template name used to render an object.

    Parameters:
        env: The Jinja environment, passed automatically.
        obj: A Griffe object, or a template name.

    Returns:
        A template name.
    """
    name = obj
    if isinstance(obj, (Alias, Object)):
        extra_data = getattr(obj, "extra", {}).get("mkdocstrings", {})
        if name := extra_data.get("template", ""):
            return name
        name = obj.kind.value
    # YORE: Bump 2: Replace block with `return f"{name}.html.jinja"`.
    try:
        template = env.get_template(f"{name}.html")
    except TemplateNotFound:
        return f"{name}.html.jinja"
    our_template = Path(template.filename).is_relative_to(Path(__file__).parent.parent)  # type: ignore[arg-type]
    if our_template:
        return f"{name}.html.jinja"
    _logger.warning(
        f"DeprecationWarning: Overriding '{name}.html' is deprecated, override '{name}.html.jinja' instead. ",
        once=True,
    )
    return f"{name}.html"


@pass_context
def do_as_attributes_section(
    context: Context,  # noqa: ARG001
    attributes: Sequence[Attribute],
    *,
    check_public: bool = True,
) -> DocstringSectionAttributes:
    """Build an attributes section from a list of attributes.

    Parameters:
        attributes: The attributes to build the section from.
        check_public: Whether to check if the attribute is public.

    Returns:
        An attributes docstring section.
    """

    def _parse_docstring_summary(attribute: Attribute) -> str:
        if attribute.docstring is None:
            return ""
        line = attribute.docstring.value.split("\n", 1)[0]
        if ":" in line and attribute.docstring.parser_options.get("returns_type_in_property_summary", False):
            _, line = line.split(":", 1)
        return line

    return DocstringSectionAttributes(
        [
            DocstringAttribute(
                name=attribute.name,
                description=_parse_docstring_summary(attribute),
                annotation=attribute.annotation,
                value=attribute.value,  # type: ignore[arg-type]
            )
            for attribute in attributes
            if not check_public or attribute.is_public
        ],
    )


@pass_context
def do_as_functions_section(
    context: Context,
    functions: Sequence[Function],
    *,
    check_public: bool = True,
) -> DocstringSectionFunctions:
    """Build a functions section from a list of functions.

    Parameters:
        functions: The functions to build the section from.
        check_public: Whether to check if the function is public.

    Returns:
        A functions docstring section.
    """
    keep_init_method = not context.parent["config"].merge_init_into_class
    return DocstringSectionFunctions(
        [
            DocstringFunction(
                name=function.name,
                description=function.docstring.value.split("\n", 1)[0] if function.docstring else "",
            )
            for function in functions
            if (not check_public or function.is_public) and (function.name != "__init__" or keep_init_method)
        ],
    )


@pass_context
def do_as_classes_section(
    context: Context,  # noqa: ARG001
    classes: Sequence[Class],
    *,
    check_public: bool = True,
) -> DocstringSectionClasses:
    """Build a classes section from a list of classes.

    Parameters:
        classes: The classes to build the section from.
        check_public: Whether to check if the class is public.

    Returns:
        A classes docstring section.
    """
    return DocstringSectionClasses(
        [
            DocstringClass(
                name=cls.name,
                description=cls.docstring.value.split("\n", 1)[0] if cls.docstring else "",
            )
            for cls in classes
            if not check_public or cls.is_public
        ],
    )


@pass_context
def do_as_modules_section(
    context: Context,  # noqa: ARG001
    modules: Sequence[Module],
    *,
    check_public: bool = True,
) -> DocstringSectionModules:
    """Build a modules section from a list of modules.

    Parameters:
        modules: The modules to build the section from.
        check_public: Whether to check if the module is public.

    Returns:
        A modules docstring section.
    """
    return DocstringSectionModules(
        [
            DocstringModule(
                name=module.name,
                description=module.docstring.value.split("\n", 1)[0] if module.docstring else "",
            )
            for module in modules
            if not check_public or module.is_public
        ],
    )


class AutorefsHook(AutorefsHookInterface):
    """Autorefs hook.

    With this hook, we're able to add context to autorefs (cross-references),
    such as originating file path and line number, to improve error reporting.
    """

    def __init__(self, current_object: Object | Alias, config: dict[str, Any]) -> None:
        """Initialize the hook.

        Parameters:
            current_object: The object being rendered.
            config: The configuration dictionary.
        """
        self.current_object = current_object
        """The current object being rendered."""
        self.config = config
        """The configuration options."""

    def expand_identifier(self, identifier: str) -> str:
        """Expand an identifier.

        Parameters:
            identifier: The identifier to expand.

        Returns:
            The expanded identifier.
        """
        return identifier

    def get_context(self) -> AutorefsHookInterface.Context:
        """Get the context for the current object.

        Returns:
            The context.
        """
        role = {
            "attribute": "data" if self.current_object.parent and self.current_object.parent.is_module else "attr",
            "class": "class",
            "function": "meth" if self.current_object.parent and self.current_object.parent.is_class else "func",
            "module": "mod",
        }.get(self.current_object.kind.value.lower(), "obj")
        origin = self.current_object.path
        try:
            filepath = self.current_object.docstring.parent.filepath  # type: ignore[union-attr]
            lineno = self.current_object.docstring.lineno or 0  # type: ignore[union-attr]
        except AttributeError:
            filepath = self.current_object.filepath
            lineno = 0

        return AutorefsHookInterface.Context(
            domain="py",
            role=role,
            origin=origin,
            filepath=str(filepath),
            lineno=lineno,
        )


_T = TypeVar("_T")
_Tree = dict[_T, "_Tree"]
_rtree = lambda: defaultdict(_rtree)  # type: ignore[has-type,var-annotated]  # noqa: E731

Tree = dict[tuple[_T, ...], "Tree"]
"""A tree type. Each node holds a tuple of items."""


def _tree(data: Iterable[tuple[_T, ...]]) -> _Tree:
    new_tree = _rtree()
    for nav in data:
        *path, leaf = nav
        node = new_tree
        for key in path:
            node = node[key]
        node[leaf] = _rtree()
    return new_tree


def _compact_tree(tree: _Tree) -> Tree:
    new_tree = _rtree()
    for key, value in tree.items():
        child = _compact_tree(value)
        if len(child) == 1:
            child_key, child_value = next(iter(child.items()))
            new_key = (key, *child_key)
            new_tree[new_key] = child_value
        else:
            new_tree[(key,)] = child
    return new_tree


def do_backlink_tree(backlinks: list[Backlink]) -> Tree[BacklinkCrumb]:
    """Build a tree of backlinks.

    Parameters:
        backlinks: The list of backlinks.

    Returns:
        A tree of backlinks.
    """
    return _compact_tree(_tree(backlink.crumbs for backlink in backlinks))
