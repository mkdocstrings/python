"""End-to-end tests for every combination of options."""

from __future__ import annotations

import json
import re
from typing import TYPE_CHECKING, Any

import bs4
import pytest
from griffe import temporary_pypackage
from inline_snapshot import outsource

from tests.snapshots import snapshots_members, snapshots_signatures

if TYPE_CHECKING:
    from mkdocstrings.handlers.python import PythonHandler


options: dict[str, Any] = {
    # General options.
    "find_stubs_package": (True, False),
    "allow_inspection": (True, False),
    "show_bases": (True, False),
    "show_source": (True, False),
    "preload_modules": ((), ("mod1",), None),
    # Heading options.
    "heading_level": (1, 2, 3, 4, 5, 6),
    "show_root_heading": (True, False),
    "show_root_toc_entry": (True, False),
    "show_root_full_path": (True, False),
    "show_root_members_full_path": (True, False),
    "show_object_full_path": (True, False),
    "show_category_heading": (True, False),
    "show_symbol_type_heading": (True, False),
    "show_symbol_type_toc": (True, False),
    # Members options.
    "inherited_members": ((), ("method1",), True, False),
    "members": ((), ("module_attribute",), True, False, None),
    "members_order": ("source", "alphabetical"),
    "filters": ((), ("!module_attribute",), ("module_attribute",), None),
    "group_by_category": (True, False),
    "show_submodules": (True, False),
    "summary": (True, False),  # TODO: Test dict.
    "show_labels": (True, False),
    # Docstrings options.
    "docstring_style": ("numpy", "google", "sphinx", None),
    "docstring_options": ({},),  # TODO: Add more examples.
    "docstring_section_style": ("table", "list", "spacy"),
    "merge_init_into_class": (True, False),
    "show_if_no_docstring": (True, False),
    "show_docstring_attributes": (True, False),
    "show_docstring_functions": (True, False),
    "show_docstring_classes": (True, False),
    "show_docstring_modules": (True, False),
    "show_docstring_description": (True, False),
    "show_docstring_examples": (True, False),
    "show_docstring_other_parameters": (True, False),
    "show_docstring_parameters": (True, False),
    "show_docstring_raises": (True, False),
    "show_docstring_receives": (True, False),
    "show_docstring_returns": (True, False),
    "show_docstring_warns": (True, False),
    "show_docstring_yields": (True, False),
    # Signature options.
    "annotations_path": ("brief", "source", "full"),
    "line_length": (0, 1, 10, 60, 120, 1000),
    "show_signature": (True, False),
    "show_signature_annotations": (True, False),
    "signature_crossrefs": (True, False),
    "separate_signature": (True, False),
    "unwrap_annotated": (True, False),
}

code = """
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


def _normalize_html(html: str) -> str:
    soup = bs4.BeautifulSoup(html, features="html.parser")
    html = soup.prettify()
    html = re.sub(r"\b(0x)[a-f0-9]+\b", r"\1...", html)
    html = re.sub(r"^(Build Date UTC ?:).+", r"\1...", html, flags=re.MULTILINE)
    html = re.sub(r"\b[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\b", r"...", html)
    html = re.sub(r'(?<=id="cell-id=)\w+(?=")', r"...", html)
    return html  # noqa: RET504


def _render(handler: PythonHandler, final_options: dict[str, Any]) -> str:
    final_options.pop("handler", None)
    final_options.pop("session_handler", None)
    handler_options = final_options.copy()
    with temporary_pypackage("pkg", {"__init__.py": code}) as tmppkg:
        handler._paths.insert(0, tmppkg.tmpdir)
        data = handler.collect("pkg", handler_options)
        html = handler.render(data, handler_options)
        return _normalize_html(html)


def _render_options(options: dict[str, Any]) -> str:
    return f"<!--\n{json.dumps(options, indent=2, sort_keys=True)}\n-->\n\n"


# Signature options
@pytest.mark.parametrize("show_signature_annotations", options["show_signature_annotations"])
@pytest.mark.parametrize("signature_crossrefs", options["signature_crossrefs"])
@pytest.mark.parametrize("separate_signature", options["separate_signature"])
def test_end_to_end_for_signatures(
    session_handler: PythonHandler,
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
    html = _render_options(final_options) + _render(session_handler, final_options)
    snapshot_key = tuple(sorted(final_options.items()))
    assert outsource(html, suffix=".html") == snapshots_signatures[snapshot_key]


# Members options.
@pytest.mark.parametrize("inherited_members", options["inherited_members"])
@pytest.mark.parametrize("members", options["members"])
@pytest.mark.parametrize("filters", options["filters"])
def test_end_to_end_for_members(
    session_handler: PythonHandler,
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
    html = _render_options(final_options) + _render(session_handler, final_options)
    snapshot_key = tuple(sorted(final_options.items()))
    assert outsource(html, suffix=".html") == snapshots_members[snapshot_key]
