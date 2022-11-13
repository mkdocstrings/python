"""Configuration for the pytest test suite."""

from __future__ import annotations

from collections import ChainMap

import pytest
from markdown.core import Markdown
from mkdocs import config
from mkdocs.config.defaults import get_schema


@pytest.fixture(name="mkdocs_conf")
def fixture_mkdocs_conf(request, tmp_path):
    """Yield a MkDocs configuration object.

    Parameters:
        request: Pytest fixture.
        tmp_path: Pytest fixture.

    Yields:
        MkDocs config.
    """
    conf = config.Config(schema=get_schema())
    while hasattr(request, "_parent_request") and hasattr(request._parent_request, "_parent_request"):  # noqa: WPS437
        request = request._parent_request  # noqa: WPS437

    conf_dict = {
        "site_name": "foo",
        "site_url": "https://example.org/",
        "site_dir": str(tmp_path),
        "plugins": [{"mkdocstrings": {"default_handler": "python"}}],
        **getattr(request, "param", {}),
    }
    # Re-create it manually as a workaround for https://github.com/mkdocs/mkdocs/issues/2289
    mdx_configs = dict(ChainMap(*conf_dict.get("markdown_extensions", [])))

    conf.load_dict(conf_dict)
    assert conf.validate() == ([], [])

    conf["mdx_configs"] = mdx_configs
    conf["markdown_extensions"].insert(0, "toc")  # Guaranteed to be added by MkDocs.

    conf = conf["plugins"]["mkdocstrings"].on_config(conf)
    conf = conf["plugins"]["autorefs"].on_config(conf)
    yield conf
    conf["plugins"]["mkdocstrings"].on_post_build(conf)


@pytest.fixture(name="plugin")
def fixture_plugin(mkdocs_conf):
    """Return a plugin instance.

    Parameters:
        mkdocs_conf: Pytest fixture: [tests.conftest.fixture_mkdocs_conf][].

    Returns:
        mkdocstrings plugin instance.
    """
    plugin = mkdocs_conf["plugins"]["mkdocstrings"]
    plugin.md = Markdown(extensions=mkdocs_conf["markdown_extensions"], extension_configs=mkdocs_conf["mdx_configs"])
    return plugin


@pytest.fixture(name="ext_markdown")
def fixture_ext_markdown(plugin):
    """Return a Markdown instance with MkdocstringsExtension.

    Parameters:
        plugin: Pytest fixture: [tests.conftest.fixture_plugin][].

    Returns:
        A Markdown instance.
    """
    return plugin.md


@pytest.fixture(name="handler")
def fixture_handler(plugin):
    """Return a handler instance.

    Parameters:
        plugin: Pytest fixture: [tests.conftest.fixture_plugin][].

    Returns:
        A handler instance.
    """
    handler = plugin.handlers.get_handler("python")
    handler._update_env(plugin.md, plugin.handlers._config)  # noqa: WPS437
    return handler
