"""Tests for the `handler` module."""

from __future__ import annotations

import os
from glob import glob
from typing import TYPE_CHECKING

import pytest
from griffe.docstrings.dataclasses import DocstringSectionExamples, DocstringSectionKind

from mkdocstrings_handlers.python.handler import CollectionError, PythonHandler, get_handler

if TYPE_CHECKING:
    from pathlib import Path


def test_collect_missing_module() -> None:
    """Assert error is raised for missing modules."""
    handler = get_handler(theme="material")
    with pytest.raises(CollectionError):
        handler.collect("aaaaaaaa", {})


def test_collect_missing_module_item() -> None:
    """Assert error is raised for missing items within existing modules."""
    handler = get_handler(theme="material")
    with pytest.raises(CollectionError):
        handler.collect("mkdocstrings.aaaaaaaa", {})


def test_collect_module() -> None:
    """Assert existing module can be collected."""
    handler = get_handler(theme="material")
    assert handler.collect("mkdocstrings", {})


def test_collect_with_null_parser() -> None:
    """Assert we can pass `None` as parser when collecting."""
    handler = get_handler(theme="material")
    assert handler.collect("mkdocstrings", {"docstring_style": None})


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
    template = handler.env.get_template("docstring/examples.html")
    rendered = template.render(section=section)
    assert "<p>This is an example.</p>" in rendered
    assert "print" in rendered
    assert "Hello" in rendered


def test_expand_globs(tmp_path: Path) -> None:
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
    handler = PythonHandler(
        handler="python",
        theme="material",
        config_file_path=str(tmp_path.joinpath("mkdocs.yml")),
        paths=["*exp*"],
    )
    for path in globbed_paths:
        assert str(path) in handler._paths


def test_expand_globs_without_changing_directory() -> None:
    """Assert globs are correctly expanded when we are already in the right directory."""
    handler = PythonHandler(
        handler="python",
        theme="material",
        config_file_path="mkdocs.yml",
        paths=["*.md"],
    )
    for path in list(glob(os.path.abspath(".") + "/*.md")):
        assert path in handler._paths
