"""Support for translating compact relative crossreferences in docstrings."""
# author: Christopher Barber, Analog Devices | Analog Garage

from __future__ import annotations

import re
from typing import List, Optional

from griffe.dataclasses import Docstring, Object
from mkdocstrings.loggers import get_logger

__all__ = ["substitute_relative_crossrefs"]  # noqa: WPS410

logger = get_logger(__name__)


def _re_or(*exps: str) -> str:
    """Construct an "or" regular expression from a sequence of regular expressions.

    Arguments:
        *exps: two or more regular expressions

    Returns:
        regular expression string
    """
    return "(?:" + "|".join(f"(?:{exp})" for exp in exps) + ")"


def _re_named(name: str, exp: str, optional: bool = False) -> str:
    """Construct a named regular expression.

    Arguments:
        name: the name for the regular expression group to create
        exp: the regular expression to be named
        optional: if true, then the entire expression group will be made optional

    Returns:
        regular expression string
    """
    optchar = "?" if optional else ""
    return f"(?P<{name}>{exp}){optchar}"


_RE_REL_CROSSREF = re.compile(r"\[(.+?)\]\[([\.^\(][^\]]*?|[^\]]*?\.)\]")
"""Regular expression that matches relative cross-reference expressions in doc-string.

This will match a cross reference where the path expression either ends in '.'
or begins with '.', '^' or '('.
"""

_RE_REL = re.compile(
    _re_named(
        "parent",
        _re_or(
            _re_named("up", r"\^+") + r"\.?",
            _re_named("class", r"\([cC]\)\.?"),
            _re_named("module", r"\([mM]\)\.?"),
            _re_named("current", r"\."),
        ),
        optional=True,
    )
    + _re_named("relname", r"(?:[a-zA-Z_][a-zA-Z0-9_\.]*)?")
)
"""Regular expression that matches a relative path reference.

This has two main parts a 'parent' group that matches the parent prefix expression,
if present, and a 'relname' group that matches the relative path text and any
final '.' character.

If the 'parent' group is matched, then exactly one of its subgroups will be present:

- 'up': an expression of the form '^'+ '.'?
- 'class': an expression of the form '(c)' '.'?
- 'module': an expression of the form '(m)' '.'?
- 'current': an expression of the form '.'
"""

_RE_ID = re.compile("[a-zA-Z_][a-zA-Z0-9_.]*")
"""Regular expression that matches a qualified python identifier."""


class _RelativeCrossrefProcessor:
    """
    A callable object that substitutes relative cross-reference expressions.

    This is intended to be used as a substitution function by `re.sub`
    to process relative cross-references in a doc-string.
    """

    _doc: Docstring
    _cur_match: re.Match | None
    _cur_input: str
    _cur_offset: int
    _cur_ref_parts: List[str]
    _ok: bool

    def __init__(self, doc: Docstring):
        self._doc = doc
        self._cur_match = None
        self._cur_input = ""
        self._cur_offset = 0
        self._cur_ref_parts = []
        self._ok = True

    def __call__(self, match: re.Match) -> str:
        self._start_match(match)

        title = match[1]
        ref = match[2]

        ref_match = _RE_REL.fullmatch(ref)
        if ref_match is None:
            self._error(f"Bad syntax in relative cross reference: '{ref}'")
        else:
            self._process_parent_specifier(ref_match)
            self._process_relname(ref_match)
            self._process_append_from_title(ref_match, title)

        if self._ok:
            result = f"[{title}][{'.'.join(self._cur_ref_parts)}]"
        else:
            result = match.group(0)

        return result

    def _start_match(self, match: re.Match):
        self._cur_match = match
        self._cur_offset = match.start(0)
        self._cur_input = match[0]
        self._ok = True
        self._cur_ref_parts.clear()

    def _process_relname(self, ref_match: re.Match) -> None:
        relname = ref_match.group("relname").strip(".")
        if relname:
            self._cur_ref_parts.append(relname)

    def _process_append_from_title(self, ref_match: re.Match, title_text: str) -> None:
        if ref_match.group(0).endswith("."):
            id_from_title = title_text.strip("`*")
            if not _RE_ID.fullmatch(id_from_title):
                self._error(f"Relative cross reference text is not a qualified identifier: '{id_from_title}'")
                return
            self._cur_ref_parts.append(id_from_title)

    def _process_parent_specifier(self, ref_match: re.Match):
        if not ref_match.group("parent"):
            return

        obj = self._doc.parent
        if obj is None:  # pragma: no cover
            self._error("INTERNAL ERROR: docstring lacks a parent!")
            return

        rel_obj = (
            self._process_current_specifier(obj, ref_match)
            or self._process_class_specifier(obj, ref_match)
            or self._process_module_specifier(obj, ref_match)
            or self._process_up_specifier(obj, ref_match)
        )

        if rel_obj is not None and self._ok:
            self._cur_ref_parts.append(rel_obj.canonical_path)

    def _process_current_specifier(self, obj: Object, ref_match: re.Match) -> Optional[Object]:
        rel_obj: Object | None = None
        if ref_match.group("current"):
            rel_obj = obj.parent if obj.is_function else obj
        return rel_obj

    def _process_class_specifier(self, obj: Object, ref_match: re.Match) -> Optional[Object]:
        rel_obj: Object | None = None
        if ref_match.group("class"):
            rel_obj = obj
            while not rel_obj.is_class:
                rel_obj = rel_obj.parent
                if rel_obj is None:
                    self._error(f"{obj.canonical_path} not in a class")
                    break
        return rel_obj

    def _process_module_specifier(self, obj: Object, ref_match: re.Match) -> Optional[Object]:
        rel_obj: Object | None = None
        if ref_match.group("module"):
            rel_obj = obj
            while not rel_obj.is_module:
                rel_obj = rel_obj.parent
                if rel_obj is None:  # pragma: no cover
                    self._error(f"{obj.canonical_path} not in a module!")
                    break
        return rel_obj

    def _process_up_specifier(self, obj: Object, ref_match: re.Match) -> Optional[Object]:
        rel_obj: Object | None = None
        if ref_match.group("up"):
            level = len(ref_match.group("up"))
            rel_obj = obj
            for _ in range(level):
                if rel_obj.parent is None:
                    self._error(f"'{ref_match.group('up')}' has too many levels for {obj.canonical_path}")
                    break
                else:
                    rel_obj = rel_obj.parent
        return rel_obj

    def _error(self, msg: str) -> None:
        """Logs a warning for a specific crossref in a docstring.

        This will include the filepath and line number if available.

        Arguments:
            msg: the warning message to report
        """
        doc = self._doc
        parent = doc.parent
        prefix = ""
        if parent is not None:  # pragma: no branch
            # We include the file:// prefix because it helps IDEs such as PyCharm
            # recognize that this is a navigable location it can highlight.
            prefix = f"file://{parent.filepath}:"
            line = doc.lineno
            if line is not None:
                # Add line offset to match in docstring
                line += doc.value.count("\n", 0, self._cur_offset)
                prefix += f"{line}:"
                # It would be nice to add the column as well, but we cannot determine
                # that without knowing how much the doc string was unindented.
            prefix += " \n"

        logger.warning(prefix + msg)

        self._ok = False


def substitute_relative_crossrefs(obj: Object):
    """Recursively expand relative cross-references in all docstrings in tree.

    Arguments:
        obj: root object. The object's docstring will be be processed as well
            as all of its children recursively.
    """
    doc = obj.docstring
    if doc:
        doc.value = _RE_REL_CROSSREF.sub(_RelativeCrossrefProcessor(doc), doc.value)

    for member in obj.members.values():
        if isinstance(member, Object):
            substitute_relative_crossrefs(member)
