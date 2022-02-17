"""This module implements a collector for the Python language.

It collects data with [Griffe](https://github.com/pawamoy/griffe).
"""

from __future__ import annotations

from collections import ChainMap
from contextlib import suppress

from griffe.agents.extensions import load_extensions
from griffe.collections import LinesCollection, ModulesCollection
from griffe.docstrings.parsers import Parser
from griffe.exceptions import AliasResolutionError
from griffe.loader import GriffeLoader
from mkdocstrings.handlers.base import BaseCollector, CollectionError, CollectorItem
from mkdocstrings.loggers import get_logger

logger = get_logger(__name__)


class PythonCollector(BaseCollector):
    """The class responsible for loading Jinja templates and rendering them.

    It defines some configuration options, implements the `render` method,
    and overrides the `update_env` method of the [`BaseRenderer` class][mkdocstrings.handlers.base.BaseRenderer].
    """

    default_config: dict = {"docstring_style": "google", "docstring_options": {}}
    """The default selection options.

    Option | Type | Description | Default
    ------ | ---- | ----------- | -------
    **`docstring_style`** | `"google" | "numpy" | "sphinx" | None` | The docstring style to use. | `"google"`
    **`docstring_options`** | `dict[str, Any]` | The options for the docstring parser. | `{}`
    """

    fallback_config: dict = {"fallback": True}

    def __init__(self) -> None:
        """Initialize the collector."""
        self._modules_collection: ModulesCollection = ModulesCollection()
        self._lines_collection: LinesCollection = LinesCollection()

    def collect(self, identifier: str, config: dict) -> CollectorItem:  # noqa: WPS231
        """Collect the documentation tree given an identifier and selection options.

        Arguments:
            identifier: The dotted-path of a Python object available in the Python path.
            config: Selection options, used to alter the data collection done by `pytkdocs`.

        Raises:
            CollectionError: When there was a problem collecting the object documentation.

        Returns:
            The collected object-tree.
        """
        module_name = identifier.split(".", 1)[0]
        unknown_module = module_name not in self._modules_collection
        if config.get("fallback", False) and unknown_module:
            raise CollectionError("Not loading additional modules during fallback")

        final_config = ChainMap(config, self.default_config)
        parser_name = final_config["docstring_style"]
        parser_options = final_config["docstring_options"]
        parser = parser_name and Parser(parser_name)

        if unknown_module:
            loader = GriffeLoader(
                extensions=load_extensions(final_config.get("extensions", [])),
                docstring_parser=parser,
                docstring_options=parser_options,
                modules_collection=self._modules_collection,
                lines_collection=self._lines_collection,
            )
            try:
                loader.load_module(module_name)
            except ImportError as error:
                raise CollectionError(str(error)) from error

            unresolved, iterations = loader.resolve_aliases(only_exported=True, only_known_modules=True)
            if unresolved:
                logger.warning(f"{len(unresolved)} aliases were still unresolved after {iterations} iterations")

        try:
            doc_object = self._modules_collection[identifier]
        except KeyError as error:  # noqa: WPS440
            raise CollectionError(f"{identifier} could not be found") from error

        if not unknown_module:
            with suppress(AliasResolutionError):
                if doc_object.docstring is not None:
                    doc_object.docstring.parser = parser
                    doc_object.docstring.parser_options = parser_options

        return doc_object
