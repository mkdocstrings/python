"""Tests for the `rendering` module."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

import pytest

from mkdocstrings_handlers.python import rendering


def test_format_code_and_signature() -> None:
    """Assert code and signatures can be Black-formatted."""
    assert rendering.do_format_code("print('Hello')", 100)
    assert rendering.do_format_code('print("Hello")', 100)
    assert rendering.do_format_signature("(param: str = 'hello') -> 'Class'", 100)
    assert rendering.do_format_signature('(param: str = "hello") -> "Class"', 100)


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
