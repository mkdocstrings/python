"""End-to-end tests for every combination of options."""

from __future__ import annotations

import json
import re
from typing import TYPE_CHECKING, Any

import bs4
import pytest
from griffe import LinesCollection, ModulesCollection, TmpPackage, temporary_pypackage
from inline_snapshot import outsource

from tests.snapshots import snapshots_members, snapshots_signatures

if TYPE_CHECKING:
    from collections.abc import Iterator

    from mkdocstrings_handlers.python.handler import PythonHandler


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

    handler._paths = [str(package.tmpdir)]
    try:
        data = handler.collect(package.name, handler_options)
    finally:
        # We're using a session handler, so we need to reset its state after each call.
        # This is not thread-safe, but pytest-xdist uses subprocesses, so it's fine.
        handler._modules_collection = ModulesCollection()
        handler._lines_collection = LinesCollection()
        handler._paths = []

    html = handler.render(data, handler_options)
    return _normalize_html(html)


def _render_options(options: dict[str, Any]) -> str:
    return f"<!--\n{json.dumps(options, indent=2, sort_keys=True)}\n-->\n\n"


# Signature options
@pytest.fixture(name="signature_package", scope="session")
def _signature_package() -> Iterator[TmpPackage]:
    code = """
        def module_function(a: int, b: str) -> None:
            '''Docstring for `module_function`.'''

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
    final_options = {
        "show_signature_annotations": show_signature_annotations,
        "signature_crossrefs": signature_crossrefs,
        "separate_signature": separate_signature,
    }
    html = _render_options(final_options) + _render(session_handler, signature_package, final_options)
    snapshot_key = tuple(sorted(final_options.items()))
    assert outsource(html, suffix=".html") == snapshots_signatures[snapshot_key]


# Members options.
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
@pytest.mark.parametrize("filters", [(), ("!module_attribute",), ("module_attribute",), None])
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
    final_options = {
        "inherited_members": inherited_members,
        "members": members,
        "filters": filters,
    }
    html = _render_options(final_options) + _render(session_handler, members_package, final_options)
    snapshot_key = tuple(sorted(final_options.items()))
    assert outsource(html, suffix=".html") == snapshots_members[snapshot_key]
