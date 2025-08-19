"""Configuration for the pytest test suite."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING

import pytest

from tests import helpers

if TYPE_CHECKING:
    from collections.abc import Iterator
    from pathlib import Path

    from markdown.core import Markdown
    from mkdocs.config.defaults import MkDocsConfig
    from mkdocstrings import MkdocstringsPlugin

    from mkdocstrings_handlers.python import PythonHandler


# --------------------------------------------
# Function-scoped fixtures.
# --------------------------------------------
@pytest.fixture(name="mkdocs_conf")
def fixture_mkdocs_conf(request: pytest.FixtureRequest, tmp_path: Path) -> Iterator[MkDocsConfig]:
    """Yield a MkDocs configuration object.

    Parameters:
        request: Pytest fixture.
        tmp_path: Pytest fixture.

    Yields:
        MkDocs config.
    """
    with helpers.mkdocs_conf(request, tmp_path) as mkdocs_conf:
        yield mkdocs_conf


@pytest.fixture(name="plugin")
def fixture_plugin(mkdocs_conf: MkDocsConfig) -> MkdocstringsPlugin:
    """Return a plugin instance.

    Parameters:
        mkdocs_conf: Pytest fixture (see conftest.py).

    Returns:
        mkdocstrings plugin instance.
    """
    return helpers.plugin(mkdocs_conf)


@pytest.fixture(name="ext_markdown")
def fixture_ext_markdown(mkdocs_conf: MkDocsConfig) -> Markdown:
    """Return a Markdown instance with MkdocstringsExtension.

    Parameters:
        mkdocs_conf: Pytest fixture (see conftest.py).

    Returns:
        A Markdown instance.
    """
    return helpers.ext_markdown(mkdocs_conf)


@pytest.fixture(name="handler")
def fixture_handler(plugin: MkdocstringsPlugin, ext_markdown: Markdown) -> PythonHandler:
    """Return a handler instance.

    Parameters:
        plugin: Pytest fixture (see conftest.py).

    Returns:
        A handler instance.
    """
    return helpers.handler(plugin, ext_markdown)


# --------------------------------------------
# Session-scoped fixtures.
# --------------------------------------------
@pytest.fixture(name="session_mkdocs_conf", scope="session")
def fixture_session_mkdocs_conf(
    request: pytest.FixtureRequest,
    tmp_path_factory: pytest.TempPathFactory,
) -> Iterator[MkDocsConfig]:
    """Yield a MkDocs configuration object.

    Parameters:
        request: Pytest fixture.
        tmp_path: Pytest fixture.

    Yields:
        MkDocs config.
    """
    with helpers.mkdocs_conf(request, tmp_path_factory.mktemp("project")) as mkdocs_conf:
        yield mkdocs_conf


@pytest.fixture(name="session_plugin", scope="session")
def fixture_session_plugin(session_mkdocs_conf: MkDocsConfig) -> MkdocstringsPlugin:
    """Return a plugin instance.

    Parameters:
        mkdocs_conf: Pytest fixture (see conftest.py).

    Returns:
        mkdocstrings plugin instance.
    """
    return helpers.plugin(session_mkdocs_conf)


@pytest.fixture(name="session_ext_markdown", scope="session")
def fixture_session_ext_markdown(session_mkdocs_conf: MkDocsConfig) -> Markdown:
    """Return a Markdown instance with MkdocstringsExtension.

    Parameters:
        mkdocs_conf: Pytest fixture (see conftest.py).

    Returns:
        A Markdown instance.
    """
    return helpers.ext_markdown(session_mkdocs_conf)


@pytest.fixture(name="session_handler", scope="session")
def fixture_session_handler(session_plugin: MkdocstringsPlugin, session_ext_markdown: Markdown) -> PythonHandler:
    """Return a handler instance.

    Parameters:
        plugin: Pytest fixture (see conftest.py).

    Returns:
        A handler instance.
    """
    return helpers.handler(session_plugin, session_ext_markdown)
