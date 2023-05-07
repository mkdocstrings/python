"""Tests for the `rendering` module."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

import pytest

from mkdocstrings_handlers.python import rendering


@pytest.mark.parametrize(
    "code",
    [
        "print('Hello')",
        "aaaaa(bbbbb, ccccc=1) + ddddd.eeeee[ffff] or {ggggg: hhhhh, iiiii: jjjjj}",
    ],
)
def test_format_code(code: str) -> None:
    """Assert code can be Black-formatted.

    Parameters:
        code: Code to format.
    """
    for length in (5, 100):
        assert rendering.do_format_code(code, length)


@pytest.mark.parametrize(
    "signature",
    ["Class.method(param: str = 'hello') -> 'OtherClass'"],
)
def test_format_signature(signature: str) -> None:
    """Assert signatures can be Black-formatted.

    Parameters:
        signature: Signature to format.
    """
    for length in (5, 100):
        assert rendering.do_format_signature(signature, length)


@dataclass
class _FakeObject:
    name: str


@pytest.mark.parametrize(
    ("names", "filter_params", "expected_names"),
    [
        (["aa", "ab", "ac", "da"], {"filters": [(re.compile("^a[^b]"), True)]}, {"ab", "da"}),
        (["aa", "ab", "ac", "da"], {"members_list": ["aa", "ab"]}, {"aa", "ab"}),
    ],
)
def test_filter_objects(names: list[str], filter_params: dict[str, Any], expected_names: set[str]) -> None:
    """Assert the objects filter works correctly.

    Parameters:
        names: Names of the objects.
        filter_params: Parameters passed to the filter function.
        expected_names: Names expected to be kept.
    """
    objects = {name: _FakeObject(name) for name in names}
    filtered = rendering.do_filter_objects(objects, **filter_params)  # type: ignore[arg-type]
    filtered_names = {obj.name for obj in filtered}
    assert set(filtered_names) == set(expected_names)
