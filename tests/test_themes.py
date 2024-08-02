"""Tests for the different themes we claim to support."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from mkdocstrings.handlers.python import PythonHandler


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
def test_render_themes_templates_python(identifier: str, handler: PythonHandler) -> None:
    """Test rendering of a given theme's templates.

    Parameters:
        identifier: Parametrized identifier.
        handler: Python handler (fixture).
    """
    data = handler.collect(identifier, {})
    handler.render(data, {})
