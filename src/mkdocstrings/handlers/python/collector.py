"""This module implements a collector for the Python language.

It collects data with [Griffe](https://github.com/pawamoy/griffe).
"""

from collections import ChainMap

from griffe import logger as griffe_logger

from mkdocstrings.handlers.base import BaseCollector, CollectionError, CollectorItem
from mkdocstrings.loggers import get_logger

griffe_logger.get_logger = get_logger  # patch logger to blend in MkDocs logs
from griffe.agents.extensions import load_extensions  # noqa: E402
from griffe.collections import LinesCollection, ModulesCollection  # noqa: E402
from griffe.docstrings.parsers import Parser  # noqa: E402
from griffe.loader import GriffeLoader  # noqa: E402

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
    **`docstring_style`** | `"google" | "numpy" | "rst" | None` | The docstring style to use. | `"google"`
    **`docstring_options`** | dict[str, Any] | The options for the docstring parser. | `{}`
    """

    def __init__(self) -> None:
        """Initialize the object."""
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
        final_config = ChainMap(config, self.default_config)

        module_name = identifier.split(".", 1)[0]
        if module_name not in self._modules_collection:
            loader = GriffeLoader(
                extensions=load_extensions(final_config.get("extensions", [])),
                docstring_parser=Parser(final_config["docstring_style"]),
                docstring_options=final_config["docstring_options"],
                modules_collection=self._modules_collection,
                lines_collection=self._lines_collection,
            )
            try:
                module = loader.load_module(module_name)
            except ModuleNotFoundError as error:
                raise CollectionError from error

            for _ in range(5):
                if loader.follow_aliases(module):
                    break
            else:
                logger.warning("some aliases could not be resolved")

        try:
            return self._modules_collection[identifier]
        except KeyError as error:  # noqa: WPS440
            raise CollectionError from error
