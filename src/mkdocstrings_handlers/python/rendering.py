"""This module implements rendering utilities."""

from __future__ import annotations

import enum
import re
import sys
from functools import lru_cache
from typing import Any, Sequence

from griffe.dataclasses import Alias, Object
from markupsafe import Markup
from mkdocstrings.handlers.base import CollectorItem
from mkdocstrings.loggers import get_logger

logger = get_logger(__name__)


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


def do_format_code(code: str, line_length: int) -> str:
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


def do_format_signature(signature: str, line_length: int) -> str:
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


def do_order_members(members: Sequence[Object | Alias], order: Order) -> Sequence[Object | Alias]:
    """Order members given an ordering method.

    Parameters:
        members: The members to order.
        order: The ordering method.

    Returns:
        The same members, ordered.
    """
    return sorted(members, key=order_map[order])


def do_crossref(path: str, brief: bool = True) -> Markup:
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
    return Markup("<span data-autorefs-optional-hover={full_path}>{path}</span>").format(full_path=full_path, path=path)


def do_multi_crossref(text: str, code: bool = True) -> Markup:
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
