"""End-to-end tests for every combination of options."""

from __future__ import annotations

import json
import re
from typing import TYPE_CHECKING, Any

import bs4
import pytest
from griffe import LinesCollection, ModulesCollection, TmpPackage, temporary_pypackage
from inline_snapshot import external_file, register_format_alias

if TYPE_CHECKING:
    from collections.abc import Iterator

    from mkdocstrings_handlers.python import PythonHandler


register_format_alias(".html", ".txt")


def _normalize_html(html: str) -> str:
    soup = bs4.BeautifulSoup(html, features="html.parser")
    html = soup.prettify()
    html = re.sub(r"\b(0x)[a-f0-9]+\b", r"\1...", html)
    html = re.sub(r"^(Build Date UTC ?:).+", r"\1...", html, flags=re.MULTILINE)
    html = re.sub(r"\b[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\b", r"...", html)
    html = re.sub(r'(?<=id="cell-id=)\w+(?=")', r"...", html)
    return html  # noqa: RET504


def _render(handler: PythonHandler, package: TmpPackage, final_options: dict[str, Any]) -> str:
    final_options.pop("handler", None)
    final_options.pop("session_handler", None)
    handler_options = final_options.copy()

    # Some default options to make snapshots easier to review.
    handler_options.setdefault("heading_level", 1)
    handler_options.setdefault("show_root_heading", True)
    handler_options.setdefault("show_source", False)

    options = handler.get_options(handler_options)

    handler._paths = [str(package.tmpdir)]
    try:
        data = handler.collect(package.name, options)
    finally:
        # We're using a session handler, so we need to reset its state after each call.
        # This is not thread-safe, but pytest-xdist uses subprocesses, so it's fine.
        handler._modules_collection = ModulesCollection()
        handler._lines_collection = LinesCollection()
        handler._paths = []

    html = handler.render(data, options)
    return _normalize_html(html)


def _render_options(options: dict[str, Any]) -> str:
    return f"<!--\n{json.dumps(options, indent=2, sort_keys=True)}\n-->\n\n"


def _snapshot_file(group: str, options: dict[str, Any]) -> str:
    return f"snapshots/{group}/" + ",".join(f"{k}={v}" for k, v in sorted(options.items())) + ".html"


# Signature tests.
@pytest.fixture(name="signature_package", scope="session")
def _signature_package() -> Iterator[TmpPackage]:
    code = """
        def module_function(a: int, b: str) -> None:
            '''Docstring for `module_function`.'''

        def _private_function(a: int, b: str) -> None:
            '''Docstring for `_private_function`.'''

        class Class:
            '''Docstring for `Class`.'''

            def __init__(self, a: int, b: str) -> None:
                '''Docstring for `Class.__init__.'''

            def method1(self, a: int, b: str) -> None:
                '''Docstring for `Class.method1`.'''
    """
    with temporary_pypackage("signature_package", {"__init__.py": code}) as tmppkg:
        yield tmppkg


@pytest.mark.parametrize("show_signature_annotations", [True, False])
@pytest.mark.parametrize("signature_crossrefs", [True, False])
@pytest.mark.parametrize("separate_signature", [True, False])
def test_end_to_end_for_signatures(
    session_handler: PythonHandler,
    signature_package: TmpPackage,
    show_signature_annotations: bool,
    signature_crossrefs: bool,
    separate_signature: bool,
) -> None:
    """Test rendering of a given theme's templates.

    Parameters:
        identifier: Parametrized identifier.
        session_handler: Python handler (fixture).
    """
    options = {
        "show_signature_annotations": show_signature_annotations,
        "signature_crossrefs": signature_crossrefs,
        "separate_signature": separate_signature,
    }
    html = _render_options(options) + _render(session_handler, signature_package, options)
    assert html == external_file(_snapshot_file("signatures", options), format=".txt")


# Signature overloads tests.
@pytest.fixture(name="overloads_package", scope="session")
def _overloads_package() -> Iterator[TmpPackage]:
    code = """
        from typing_extensions import overload

        @overload
        def foo(a: int, b: str) -> float: ...

        @overload
        def foo(a: str, b: int) -> None: ...

        def foo(a: str | int, b: int | str) -> float | None:
            '''Docstring for `foo`.'''

        def bar(a: str, b: int | str) -> float | None:
            '''Docstring for `bar`.'''

        class Class:
            '''Docstring for `Class`.'''

            @overload
            def foo(self, a: int, b: str) -> float: ...

            @overload
            def foo(self, a: str, b: int) -> None: ...

            def foo(self, a: str | int, b: int | str) -> float | None:
                '''Docstring for `Class.foo`.'''

            def bar(self, a: str, b: int | str) -> float | None:
                '''Docstring for `Class.bar`.'''
    """
    with temporary_pypackage("overloads_package", {"__init__.py": code}) as tmppkg:
        yield tmppkg


@pytest.mark.parametrize("separate_signature", [True, False])
@pytest.mark.parametrize("show_overloads", [True, False])
@pytest.mark.parametrize("overloads_only", [True, False])
def test_end_to_end_for_overloads(
    session_handler: PythonHandler,
    overloads_package: TmpPackage,
    separate_signature: bool,
    show_overloads: bool,
    overloads_only: bool,
) -> None:
    """Test rendering of a given theme's templates.

    Parameters:
        identifier: Parametrized identifier.
        session_handler: Python handler (fixture).
    """
    options = {
        "separate_signature": separate_signature,
        "show_overloads": show_overloads,
        "overloads_only": overloads_only,
    }
    html = _render_options(options) + _render(session_handler, overloads_package, options)
    assert html == external_file(_snapshot_file("overloads", options), format=".txt")


# Member tests.
@pytest.fixture(name="members_package", scope="session")
def _members_package() -> Iterator[TmpPackage]:
    code = """
        '''Docstring for the package.'''

        def module_function(a: int, b: str) -> None:
            '''Docstring for `module_function`.'''

        class Class:
            '''Docstring for `Class`.'''

            class NestedClass:
                '''Docstring for `NestedClass`.'''

            class_attribute: int = 42
            '''Docstring for `Class.class_attribute`.'''

            def __init__(self, a: int, b: str) -> None:
                '''Docstring for `Class.__init__`.'''
                self.instance_attribute = a + b
                '''Docstring for `Class.instance_attribute`.'''

            def method1(self, a: int, b: str) -> None:
                '''Docstring for `Class.method1`.'''

            def method2(self, a: int, b: str) -> None:
                '''Docstring for `Class.method2`.'''

        module_attribute: int = 42
        '''Docstring for `module_attribute`.'''

        class Subclass(Class):
            '''Docstring for `Subclass`.'''
    """
    with temporary_pypackage("members_package", {"__init__.py": code}) as tmppkg:
        yield tmppkg


@pytest.mark.parametrize("inherited_members", [(), ("method1",), True, False])
@pytest.mark.parametrize("members", [(), ("module_attribute",), True, False, None])
@pytest.mark.parametrize("filters", [(), ("!module_attribute",), ("module_attribute",), "public", None])
def test_end_to_end_for_members(
    session_handler: PythonHandler,
    members_package: TmpPackage,
    inherited_members: list[str] | bool | None,
    members: list[str] | bool | None,
    filters: list[str] | None,
) -> None:
    """Test rendering of a given theme's templates.

    Parameters:
        identifier: Parametrized identifier.
        session_handler: Python handler (fixture).
    """
    options = {
        "inherited_members": inherited_members,
        "members": members,
        "filters": filters,
    }
    html = _render_options(options) + _render(session_handler, members_package, options)
    assert html == external_file(_snapshot_file("members", options), format=".txt")


# Heading tests.
@pytest.fixture(name="headings_package", scope="session")
def _headings_package() -> Iterator[TmpPackage]:
    code = """
        def module_function(a: int, b: str) -> None:
            pass

        class Class:
            class_attribute: int = 42

            def __init__(self, a: int, b: str) -> None:
                self.instance_attribute = a + b

            def method1(self, a: int, b: str) -> None:
                pass

        module_attribute: int = 42
    """
    with temporary_pypackage("headings_package", {"__init__.py": code}) as tmppkg:
        yield tmppkg


@pytest.mark.parametrize("separate_signature", [True, False])
@pytest.mark.parametrize("heading", ["", "Some heading"])
def test_end_to_end_for_headings(
    session_handler: PythonHandler,
    headings_package: TmpPackage,
    separate_signature: bool,
    heading: str,
) -> None:
    """Test rendering of a given theme's templates.

    Parameters:
        identifier: Parametrized identifier.
        session_handler: Python handler (fixture).
    """
    options = {
        "separate_signature": separate_signature,
        "heading": heading,
    }
    extra = {"show_if_no_docstring": True, "members": False}
    html = _render_options(options) + _render(session_handler, headings_package, {**options, **extra})
    assert html == external_file(_snapshot_file("headings", options), format=".txt")
