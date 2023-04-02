"""Tests for the different themes we claim to support."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from markdown import Markdown
    from mkdocstrings.plugin import MkdocstringsPlugin


@pytest.mark.parametrize(
    "plugin",
    [
        {"theme": "mkdocs"},
        {"theme": "readthedocs"},
        {"theme": {"name": "material"}},
    ],
    indirect=["plugin"],
)
@pytest.mark.parametrize(
    "module",
    [
        "mkdocstrings.extension",
        "mkdocstrings.inventory",
        "mkdocstrings.loggers",
        "mkdocstrings.plugin",
        "mkdocstrings.handlers.base",
        "mkdocstrings.handlers.rendering",
        "mkdocstrings_handlers.python",
    ],
)
@pytest.mark.skipif(sys.version_info < (3, 7), reason="material is not installed on Python 3.6")
def test_render_themes_templates_python(module: str, plugin: MkdocstringsPlugin, ext_markdown: Markdown) -> None:
    """Test rendering of a given theme's templates.

    Parameters:
        module: Parametrized argument.
        plugin: Pytest fixture: [tests.conftest.fixture_plugin][].
    """
    handler = plugin.handlers.get_handler("python")
    handler._update_env(ext_markdown, plugin.handlers._config)
    data = handler.collect(module, {})
    handler.render(data, {})
