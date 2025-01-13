"""Tests for the `handler` module."""

from __future__ import annotations

import os
from glob import glob
from textwrap import dedent
from typing import TYPE_CHECKING

import pytest
from griffe import DocstringSectionExamples, DocstringSectionKind, temporary_visited_module

from mkdocstrings_handlers.python.config import PythonOptions
from mkdocstrings_handlers.python.handler import CollectionError, PythonHandler

if TYPE_CHECKING:
    from pathlib import Path

    from mkdocstrings.plugin import MkdocstringsPlugin


def test_collect_missing_module(handler: PythonHandler) -> None:
    """Assert error is raised for missing modules."""
    with pytest.raises(CollectionError):
        handler.collect("aaaaaaaa", PythonOptions())


def test_collect_missing_module_item(handler: PythonHandler) -> None:
    """Assert error is raised for missing items within existing modules."""
    with pytest.raises(CollectionError):
        handler.collect("mkdocstrings.aaaaaaaa", PythonOptions())


def test_collect_module(handler: PythonHandler) -> None:
    """Assert existing module can be collected."""
    assert handler.collect("mkdocstrings", PythonOptions())


def test_collect_with_null_parser(handler: PythonHandler) -> None:
    """Assert we can pass `None` as parser when collecting."""
    assert handler.collect("mkdocstrings", PythonOptions(docstring_style=None))


@pytest.mark.parametrize(
    "handler",
    [
        {"theme": "mkdocs"},
        {"theme": "readthedocs"},
        {"theme": {"name": "material"}},
    ],
    indirect=["handler"],
)
def test_render_docstring_examples_section(handler: PythonHandler) -> None:
    """Assert docstrings' examples section can be rendered.

    Parameters:
        handler: A handler instance (parametrized).
    """
    section = DocstringSectionExamples(
        value=[
            (DocstringSectionKind.text, "This is an example."),
            (DocstringSectionKind.examples, ">>> print('Hello')\nHello"),
        ],
    )
    template = handler.env.get_template("docstring/examples.html.jinja")
    rendered = template.render(section=section, locale="en")
    template.render(section=section, locale="not_existing")
    assert "<p>This is an example.</p>" in rendered
    assert "print" in rendered
    assert "Hello" in rendered


def test_expand_globs(tmp_path: Path, plugin: MkdocstringsPlugin) -> None:
    """Assert globs are correctly expanded.

    Parameters:
        tmp_path: Pytext fixture that creates a temporary directory.
    """
    globbed_names = (
        "expanded_a",
        "expanded_b",
        "other_expanded_c",
        "other_expanded_d",
    )
    globbed_paths = [tmp_path.joinpath(globbed_name) for globbed_name in globbed_names]
    for path in globbed_paths:
        path.touch()
    plugin.handlers._tool_config.config_file_path = str(tmp_path.joinpath("mkdocs.yml"))
    handler: PythonHandler = plugin.handlers.get_handler("python", {"paths": ["*exp*"]})  # type: ignore[assignment]
    for path in globbed_paths:
        assert str(path) in handler._paths


def test_expand_globs_without_changing_directory(plugin: MkdocstringsPlugin) -> None:
    """Assert globs are correctly expanded when we are already in the right directory."""
    plugin.handlers._tool_config.config_file_path = "mkdocs.yml"
    handler: PythonHandler = plugin.handlers.get_handler("python", {"paths": ["*.md"]})  # type: ignore[assignment]
    for path in list(glob(os.path.abspath(".") + "/*.md")):
        assert path in handler._paths


@pytest.mark.parametrize(
    ("expect_change", "extension"),
    [
        (True, "extension.py"),
        (True, "extension.py:SomeExtension"),
        (True, "path/to/extension.py"),
        (True, "path/to/extension.py:SomeExtension"),
        (True, {"extension.py": {"option": "value"}}),
        (True, {"extension.py:SomeExtension": {"option": "value"}}),
        (True, {"path/to/extension.py": {"option": "value"}}),
        (True, {"path/to/extension.py:SomeExtension": {"option": "value"}}),
        # True because OS path normalization.
        (True, "/absolute/path/to/extension.py"),
        (True, "/absolute/path/to/extension.py:SomeExtension"),
        (True, {"/absolute/path/to/extension.py": {"option": "value"}}),
        (True, {"/absolute/path/to/extension.py:SomeExtension": {"option": "value"}}),
        (False, "dot.notation.path.to.extension"),
        (False, "dot.notation.path.to.pyextension"),
        (False, {"dot.notation.path.to.extension": {"option": "value"}}),
        (False, {"dot.notation.path.to.pyextension": {"option": "value"}}),
    ],
)
def test_extension_paths(
    tmp_path: Path,
    expect_change: bool,
    extension: str | dict,
    plugin: MkdocstringsPlugin,
) -> None:
    """Assert extension paths are resolved relative to config file."""
    plugin.handlers._tool_config.config_file_path = str(tmp_path.joinpath("mkdocs.yml"))
    handler: PythonHandler = plugin.handlers.get_handler("python")  # type: ignore[assignment]
    normalized = handler.normalize_extension_paths([extension])[0]
    if expect_change:
        if isinstance(normalized, str) and isinstance(extension, str):
            assert normalized == str(tmp_path.joinpath(extension))
        elif isinstance(normalized, dict) and isinstance(extension, dict):
            pth, options = next(iter(extension.items()))
            assert normalized == {str(tmp_path.joinpath(pth)): options}
        else:
            raise ValueError("Normalization must not change extension items type")
    else:
        assert normalized == extension


def test_rendering_object_source_without_lineno(handler: PythonHandler) -> None:
    """Test rendering objects without a line number."""
    code = dedent(
        """
        '''Module docstring.'''

        class Class:
            '''Class docstring.'''

            def function(self):
                '''Function docstring.'''

        attribute = 0
        '''Attribute docstring.'''
        """,
    )
    with temporary_visited_module(code) as module:
        # TODO: Remove once Griffe does that automatically.
        module.lines_collection[module.filepath] = code.splitlines()  # type: ignore[index]

        module["Class"].lineno = None
        module["Class.function"].lineno = None
        module["attribute"].lineno = None
        assert handler.render(module, PythonOptions(show_source=True))
