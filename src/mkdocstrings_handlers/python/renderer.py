"""This module implements a renderer for the Python language."""

from __future__ import annotations

import enum
import re
import sys
from collections import ChainMap
from functools import lru_cache
from typing import Any, Sequence

from griffe.dataclasses import Alias, Object
from griffe.exceptions import AliasResolutionError
from markdown import Markdown
from markupsafe import Markup
from mkdocstrings.extension import PluginError
from mkdocstrings.handlers.base import BaseRenderer, CollectorItem
from mkdocstrings.loggers import get_logger

logger = get_logger(__name__)
# TODO: CSS classes everywhere in templates
# TODO: name normalization (filenames, Jinja2 variables, HTML tags, CSS classes)
# TODO: Jinja2 blocks everywhere in templates


class Order(enum.Enum):
    """Enumeration for the possible members ordering."""

    alphabetical = "alphabetical"
    source = "source"


def _sort_key_alphabetical(item: CollectorItem) -> Any:
    # chr(sys.maxunicode) is a string that contains the final unicode
    # character, so if 'name' isn't found on the object, the item will go to
    # the end of the list.
    return item.name or chr(sys.maxunicode)


def _sort_key_source(item: CollectorItem) -> Any:
    # if 'lineno' is none, the item will go to the start of the list.
    return item.lineno if item.lineno is not None else -1


order_map = {
    Order.alphabetical: _sort_key_alphabetical,
    Order.source: _sort_key_source,
}


class PythonRenderer(BaseRenderer):
    """The class responsible for loading Jinja templates and rendering them.

    It defines some configuration options, implements the `render` method,
    and overrides the `update_env` method of the [`BaseRenderer` class][mkdocstrings.handlers.base.BaseRenderer].

    Attributes:
        fallback_theme: The theme to fallback to.
        default_config: The default rendering options,
            see [`default_config`][mkdocstrings_handlers.python.renderer.PythonRenderer.default_config].
    """

    fallback_theme = "material"

    default_config: dict = {
        "show_root_heading": False,
        "show_root_toc_entry": True,
        "show_root_full_path": True,
        "show_root_members_full_path": False,
        "show_object_full_path": False,
        "show_category_heading": False,
        "show_if_no_docstring": False,
        "show_signature": True,
        "show_signature_annotations": False,
        "separate_signature": False,
        "line_length": 60,
        "merge_init_into_class": False,
        "show_source": True,
        "show_bases": True,
        "show_submodules": True,
        "group_by_category": True,
        "heading_level": 2,
        "members_order": Order.alphabetical.value,
        "docstring_section_style": "table",
    }
    """The default rendering options.

    Option | Type | Description | Default
    ------ | ---- | ----------- | -------
    **`show_root_heading`** | `bool` | Show the heading of the object at the root of the documentation tree. | `False`
    **`show_root_toc_entry`** | `bool` | If the root heading is not shown, at least add a ToC entry for it. | `True`
    **`show_root_full_path`** | `bool` | Show the full Python path for the root object heading. | `True`
    **`show_object_full_path`** | `bool` | Show the full Python path of every object. | `False`
    **`show_root_members_full_path`** | `bool` | Show the full Python path of objects that are children of the root object (for example, classes in a module). When False, `show_object_full_path` overrides. | `False`
    **`show_category_heading`** | `bool` | When grouped by categories, show a heading for each category. | `False`
    **`show_if_no_docstring`** | `bool` | Show the object heading even if it has no docstring or children with docstrings. | `False`
    **`show_signature`** | `bool` | Show method and function signatures. | `True`
    **`show_signature_annotations`** | `bool` | Show the type annotations in method and function signatures. | `False`
    **`separate_signature`** | `bool` | Whether to put the whole signature in a code block below the heading. | `False`
    **`line_length`** | `int` | Maximum line length when formatting code. | `60`
    **`merge_init_into_class`** | `bool` | Whether to merge the `__init__` method into the class' signature and docstring. | `False`
    **`show_source`** | `bool` | Show the source code of this object. | `True`
    **`show_bases`** | `bool` | Show the base classes of a class. | `True`
    **`show_submodules`** | `bool` | When rendering a module, show its submodules recursively. | `True`
    **`group_by_category`** | `bool` | Group the object's children by categories: attributes, classes, functions, methods, and modules. | `True`
    **`heading_level`** | `int` | The initial heading level to use. | `2`
    **`members_order`** | `str` | The members ordering to use. Options: `alphabetical` - order by the members names, `source` - order members as they appear in the source file. | `alphabetical`
    **`docstring_section_style`** | `str` | The style used to render docstring sections. Options: `table`, `list`, `spacy`. | `table`
    """  # noqa: E501

    def render(self, data: CollectorItem, config: dict) -> str:  # noqa: D102 (ignore missing docstring)
        final_config = ChainMap(config, self.default_config)

        template = self.env.get_template(f"{data.kind.value}.html")

        # Heading level is a "state" variable, that will change at each step
        # of the rendering recursion. Therefore, it's easier to use it as a plain value
        # than as an item in a dictionary.
        heading_level = final_config["heading_level"]
        try:
            final_config["members_order"] = Order(final_config["members_order"])
        except ValueError:
            choices = "', '".join(item.value for item in Order)
            raise PluginError(f"Unknown members_order '{final_config['members_order']}', choose between '{choices}'.")

        return template.render(
            **{"config": final_config, data.kind.value: data, "heading_level": heading_level, "root": True},
        )

    def get_anchors(self, data: CollectorItem) -> list[str]:  # noqa: D102 (ignore missing docstring)
        try:
            return list({data.path, data.canonical_path, *data.aliases})
        except AliasResolutionError:
            return [data.path]

    def update_env(self, md: Markdown, config: dict) -> None:  # noqa: D102 (ignore missing docstring)
        super().update_env(md, config)
        self.env.trim_blocks = True
        self.env.lstrip_blocks = True
        self.env.keep_trailing_newline = False
        self.env.filters["crossref"] = self.do_crossref
        self.env.filters["multi_crossref"] = self.do_multi_crossref
        self.env.filters["order_members"] = self.do_order_members
        self.env.filters["format_code"] = self.do_format_code
        self.env.filters["format_signature"] = self.do_format_signature

    def do_format_code(self, code: str, line_length: int) -> str:
        """Format code using Black.

        Parameters:
            code: The code to format.
            line_length: The line length to give to Black.

        Returns:
            The same code, formatted.
        """
        code = code.strip()
        if len(code) < line_length:
            return code
        formatter = _get_black_formatter()
        return formatter(code, line_length)

    def do_format_signature(self, signature: str, line_length: int) -> str:
        """Format a signature using Black.

        Parameters:
            signature: The signature to format.
            line_length: The line length to give to Black.

        Returns:
            The same code, formatted.
        """
        code = signature.strip()
        if len(code) < line_length:
            return code
        formatter = _get_black_formatter()
        formatted = formatter(f"def {code}: pass", line_length)
        # remove starting `def ` and trailing `: pass`
        return formatted[4:-5].strip()[:-1]

    def do_order_members(self, members: Sequence[Object | Alias], order: Order) -> Sequence[Object | Alias]:
        """Order members given an ordering method.

        Parameters:
            members: The members to order.
            order: The ordering method.

        Returns:
            The same members, ordered.
        """
        return sorted(members, key=order_map[order])

    def do_crossref(self, path: str, brief: bool = True) -> Markup:
        """Filter to create cross-references.

        Parameters:
            path: The path to link to.
            brief: Show only the last part of the path, add full path as hover.

        Returns:
            Markup text.
        """
        full_path = path
        if brief:
            path = full_path.split(".")[-1]
        return Markup("<span data-autorefs-optional-hover={full_path}>{path}</span>").format(
            full_path=full_path, path=path
        )

    def do_multi_crossref(self, text: str, code: bool = True) -> Markup:
        """Filter to create cross-references.

        Parameters:
            text: The text to scan.
            code: Whether to wrap the result in a code tag.

        Returns:
            Markup text.
        """
        group_number = 0
        variables = {}

        def repl(match):  # noqa: WPS430
            nonlocal group_number  # noqa: WPS420
            group_number += 1
            path = match.group()
            path_var = f"path{group_number}"
            variables[path_var] = path
            return f"<span data-autorefs-optional-hover={{{path_var}}}>{{{path_var}}}</span>"

        text = re.sub(r"([\w.]+)", repl, text)
        if code:
            text = f"<code>{text}</code>"
        return Markup(text).format(**variables)


@lru_cache(maxsize=1)
def _get_black_formatter():
    try:
        from black import Mode, format_str
    except ModuleNotFoundError:
        logger.warning("Formatting signatures requires Black to be installed.")
        return lambda text, _: text

    def formatter(code, line_length):  # noqa: WPS430
        mode = Mode(line_length=line_length)
        return format_str(code, mode=mode)

    return formatter
