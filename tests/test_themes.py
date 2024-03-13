"""Tests for the different themes we claim to support."""

from __future__ import annotations

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
    "identifier",
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
def test_render_themes_templates_python(identifier: str, plugin: MkdocstringsPlugin, ext_markdown: Markdown) -> None:
    """Test rendering of a given theme's templates.

    Parameters:
        identifier: Parametrized identifier.
        plugin: Pytest fixture (see conftest.py).
        ext_markdown: Pytest fixture (see conftest.py).
    """
    handler = plugin.handlers.get_handler("python")
    handler._update_env(ext_markdown, plugin.handlers._config)
    data = handler.collect(identifier, {})
    handler.render(data, {})
