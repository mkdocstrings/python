"""This module implements a handler for the Python language."""

import posixpath
from typing import Any, BinaryIO, Iterator, Optional, Tuple

from griffe.logger import patch_loggers
from mkdocstrings.handlers.base import BaseHandler
from mkdocstrings.inventory import Inventory
from mkdocstrings.loggers import get_logger

from mkdocstrings_handlers.python.collector import PythonCollector
from mkdocstrings_handlers.python.renderer import PythonRenderer

patch_loggers(get_logger)


class PythonHandler(BaseHandler):
    """The Python handler class.

    Attributes:
        domain: The cross-documentation domain/language for this handler.
        enable_inventory: Whether this handler is interested in enabling the creation
            of the `objects.inv` Sphinx inventory file.
    """

    domain: str = "py"  # to match Sphinx's default domain
    enable_inventory: bool = True

    @classmethod
    def load_inventory(
        cls,
        in_file: BinaryIO,
        url: str,
        base_url: Optional[str] = None,
        **kwargs: Any,
    ) -> Iterator[Tuple[str, str]]:
        """Yield items and their URLs from an inventory file streamed from `in_file`.

        This implements mkdocstrings' `load_inventory` "protocol" (see plugin.py).

        Arguments:
            in_file: The binary file-like object to read the inventory from.
            url: The URL that this file is being streamed from (used to guess `base_url`).
            base_url: The URL that this inventory's sub-paths are relative to.
            **kwargs: Ignore additional arguments passed from the config.

        Yields:
            Tuples of (item identifier, item URL).
        """
        if base_url is None:
            base_url = posixpath.dirname(url)

        for item in Inventory.parse_sphinx(in_file, domain_filter=("py",)).values():  # noqa: WPS526
            yield item.name, posixpath.join(base_url, item.uri)


def get_handler(
    theme: str,  # noqa: W0613 (unused argument config)
    custom_templates: Optional[str] = None,
    **config: Any,
) -> PythonHandler:
    """Simply return an instance of `PythonHandler`.

    Arguments:
        theme: The theme to use when rendering contents.
        custom_templates: Directory containing custom templates.
        **config: Configuration passed to the handler.

    Returns:
        An instance of `PythonHandler`.
    """
    return PythonHandler(
        collector=PythonCollector(),
        renderer=PythonRenderer("python", theme, custom_templates),
    )
