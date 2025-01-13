"""Generate a JSON schema of the Python handler configuration."""

import json
from os.path import join
from typing import Any

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import get_plugin_logger

from mkdocstrings_handlers.python.config import PythonInputConfig

# TODO: Update when Pydantic supports Python 3.14 (sources and duties as well).
try:
    from pydantic import TypeAdapter
except ImportError:
    TypeAdapter = None  # type: ignore[assignment,misc]


logger = get_plugin_logger(__name__)


def on_post_build(config: MkDocsConfig, **kwargs: Any) -> None:  # noqa: ARG001
    """Write `schema.json` to the site directory."""
    if TypeAdapter is None:
        logger.info("Pydantic is not installed, skipping JSON schema generation")
        return
    adapter = TypeAdapter(PythonInputConfig)
    schema = adapter.json_schema()
    schema["$schema"] = "https://json-schema.org/draft-07/schema"
    with open(join(config.site_dir, "schema.json"), "w") as file:
        json.dump(schema, file, indent=2)
        logger.debug("Generated JSON schema")
