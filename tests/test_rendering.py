"""Tests for the `rendering` module."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

import pytest
from griffe import ModulesCollection, temporary_visited_module

from mkdocstrings_handlers.python import rendering

if TYPE_CHECKING:
    from markupsafe import Markup


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
    ("name", "signature"),
    [("Class.method", "(param: str = 'hello') -> 'OtherClass'")],
)
def test_format_signature(name: Markup, signature: str) -> None:
    """Assert signatures can be Black-formatted.

    Parameters:
        signature: Signature to format.
    """
    for length in (5, 100):
        assert rendering._format_signature(name, signature, length)


@dataclass
class _FakeObject:
    name: str
    inherited: bool = False


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


@pytest.mark.parametrize(
    ("members", "inherited_members", "expected_names"),
    [
        (True, True, {"base", "main"}),
        (True, False, {"main"}),
        (True, ["base"], {"base", "main"}),
        (True, [], {"main"}),
        (False, True, {"base"}),
        (False, False, set()),
        (False, ["base"], {"base"}),
        (False, [], set()),
        ([], True, {"base"}),
        ([], False, set()),
        ([], ["base"], {"base"}),
        ([], [], set()),
        (None, True, {"base", "main"}),
        (None, False, {"main"}),
        (None, ["base"], {"base", "main"}),
        (None, [], {"main"}),
        (["base"], True, {"base"}),
        (["base"], False, set()),
        (["base"], ["base"], {"base"}),
        (["base"], [], set()),
        (["main"], True, {"main"}),
        (["main"], False, {"main"}),
        (["main"], ["base"], {"base", "main"}),
        (["main"], [], {"main"}),
    ],
)
def test_filter_inherited_members(
    members: bool | list[str] | None,
    inherited_members: bool | list[str],
    expected_names: list[str],
) -> None:
    """Test inherited members filtering.

    Parameters:
        members: Members option (parametrized).
        inherited_members: Inherited members option (parametrized).
        expected_names: The expected result as a list of member names.
    """
    collection = ModulesCollection()
    with temporary_visited_module(
        """
        class Base:
            def base(self): ...

        class Main(Base):
            def main(self): ...
        """,
        modules_collection=collection,
    ) as module:
        collection["module"] = module
        objects = module["Main"].all_members
        filtered = rendering.do_filter_objects(objects, members_list=members, inherited_members=inherited_members)
        names = {obj.name for obj in filtered}
        assert names == expected_names


@pytest.mark.parametrize(
    ("order", "members_list", "expected_names"),
    [
        (rendering.Order.alphabetical, None, ["a", "b", "c"]),
        (rendering.Order.source, None, ["c", "b", "a"]),
        (rendering.Order.alphabetical, ["c", "b"], ["c", "b"]),
        (rendering.Order.source, ["a", "c"], ["a", "c"]),
        (rendering.Order.alphabetical, [], ["a", "b", "c"]),
        (rendering.Order.source, [], ["c", "b", "a"]),
        (rendering.Order.alphabetical, True, ["a", "b", "c"]),
        (rendering.Order.source, False, ["c", "b", "a"]),
    ],
)
def test_ordering_members(order: rendering.Order, members_list: list[str | None], expected_names: list[str]) -> None:
    """Assert the objects are correctly ordered.

    Parameters:
        order: The order to use (alphabetical or source).
        members_list: The user specified members list.
        expected_names: The expected ordered list of object names.
    """

    class Obj:
        def __init__(self, name: str, lineno: int | None = None, *, is_alias: bool = False) -> None:
            self.name = name
            self.lineno = lineno
            self.alias_lineno = lineno
            self.is_alias = is_alias

    members = [Obj("a", 10, is_alias=True), Obj("b", 9, is_alias=False), Obj("c", 8, is_alias=True)]
    ordered = rendering.do_order_members(members, order, members_list)  # type: ignore[arg-type]
    assert [obj.name for obj in ordered] == expected_names


@pytest.mark.parametrize(
    ("strategy", "docstrings_list", "expected_docstrings_list"),
    [
        (rendering.DocstringInheritStrategy.default, ['"""base"""', "", ""], ["base", None, None]),
        (
            rendering.DocstringInheritStrategy.if_not_present,
            ['"""base"""', '"""main"""', ""],
            ["base", "main", "main"],
        ),  # main: stays the same (no merge); sub: main is taken (not base)
        (
            rendering.DocstringInheritStrategy.merge,
            ['"""base"""', '"""main"""', ""],
            ["base", "base+main", "base+main"],
        ),  # main: is merged with base; sub: empty is merged with base+main (not base+main+)
        (
            rendering.DocstringInheritStrategy.merge,
            ["", '"""main"""', ""],
            [None, "main", "main"],
        ),  # Base class has no docstring after merging (as opposed to an empty one)
    ],
)
def test_do_optionally_inherit_docstrings(
    strategy: rendering.DocstringInheritStrategy, docstrings_list: list[str], expected_docstrings_list: list[str],
) -> None:
    """Test the inheritance strategies of docstrings for members.

    Parameters:
        strategy: The docstring inheritance strategy to use.
        docstrings_list: The list of docstrings for the base, main, and sub classes. Needs triple quotes.
        expected_docstrings_list: The expected list of docstrings for the base, main, and sub classes. Just the content, i.e. without triple quotes. None for no docstring at all.
    """
    docstring_base, docstring_main, docstring_sub = docstrings_list

    collection = ModulesCollection()
    with temporary_visited_module(
        f"""
        class Obj:
            # No base method to verify that this doesn't break anything.
            ...

        class Base(Obj):
            def base(self):
                {docstring_base} # Without triple quotes so we can control between empty docstring and no docstring.
                ...

        class Main(Base):
            def base(self):
                {docstring_main}
                ...

        class Sub(Main):
            def base(self):
                {docstring_sub}
                ...
        """,
        modules_collection=collection,
    ) as module:
        collection["module"] = module

    classes = ["Base", "Main", "Sub"]
    result = rendering.do_optionally_inherit_docstrings(
        objects={class_: collection["module"][class_] for class_ in classes},
        docstring_inherit_strategy=strategy,
        docstring_merge_delimiter="+",
    )
    docstrings = [result[class_].members["base"].docstring for class_ in classes]
    docstring_values = [docstring.value if docstring else None for docstring in docstrings]

    assert docstring_values == expected_docstrings_list
