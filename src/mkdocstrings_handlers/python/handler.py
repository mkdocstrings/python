"""This module implements a handler for the Python language."""

from __future__ import annotations

import posixpath
from collections import ChainMap
from contextlib import suppress
from typing import Any, BinaryIO, Iterator, Optional, Tuple

from griffe.agents.extensions import load_extensions
from griffe.collections import LinesCollection, ModulesCollection
from griffe.docstrings.parsers import Parser
from griffe.exceptions import AliasResolutionError
from griffe.loader import GriffeLoader
from griffe.logger import patch_loggers
from markdown import Markdown
from mkdocstrings.extension import PluginError
from mkdocstrings.handlers.base import BaseHandler, CollectionError, CollectorItem
from mkdocstrings.inventory import Inventory
from mkdocstrings.loggers import get_logger

from mkdocstrings_handlers.python import rendering

logger = get_logger(__name__)

patch_loggers(get_logger)


class PythonHandler(BaseHandler):
    """The Python handler class.

    Attributes:
        domain: The cross-documentation domain/language for this handler.
        enable_inventory: Whether this handler is interested in enabling the creation
            of the `objects.inv` Sphinx inventory file.
        fallback_theme: The fallback theme.
        fallback_config: The configuration used to collect item during autorefs fallback.
        default_collection_config: The default rendering options,
            see [`default_collection_config`][mkdocstrings_handlers.python.handler.PythonHandler.default_collection_config].
        default_rendering_config: The default rendering options,
            see [`default_rendering_config`][mkdocstrings_handlers.python.handler.PythonHandler.default_rendering_config].
    """

    domain: str = "py"  # to match Sphinx's default domain
    enable_inventory: bool = True
    fallback_theme = "material"
    fallback_config: dict = {"fallback": True}
    default_collection_config: dict = {"docstring_style": "google", "docstring_options": {}}
    """The default collection options.

    Option | Type | Description | Default
    ------ | ---- | ----------- | -------
    **`docstring_style`** | `"google" | "numpy" | "sphinx" | None` | The docstring style to use. | `"google"`
    **`docstring_options`** | `dict[str, Any]` | The options for the docstring parser. | `{}`
    """
    default_rendering_config: dict = {
        "show_root_heading": False,
        "show_root_toc_entry": True,
        "show_root_full_path": True,
        "show_root_members_full_path": False,
        "show_object_full_path": False,
        "show_category_heading": False,
        "show_if_no_docstring": False,
        "show_signature": True,
        "show_signature_annotations": False,
        "separate_signature": False,
        "line_length": 60,
        "merge_init_into_class": False,
        "show_source": True,
        "show_bases": True,
        "show_submodules": True,
        "group_by_category": True,
        "heading_level": 2,
        "members_order": rendering.Order.alphabetical.value,
        "docstring_section_style": "table",
    }
    """
    Attributes: Default rendering options:
        show_root_heading (bool): Show the heading of the object at the root of the documentation tree. Default: `False`.
        show_root_toc_entry (bool): If the root heading is not shown, at least add a ToC entry for it. Default: `True`.
        show_root_full_path (bool): Show the full Python path for the root object heading. Default: `True`.
        show_root_members_full_path (bool): Show the full Python path of every object. Default: `False`.
        show_object_full_path (bool): Show the full Python path of objects that are children of the root object (for example, classes in a module). When False, `show_object_full_path` overrides. Default: `False`.
        show_category_heading (bool): When grouped by categories, show a heading for each category. Default: `False`.
        show_if_no_docstring (bool): Show the object heading even if it has no docstring or children with docstrings. Default: `False`.
        show_signature (bool): Show method and function signatures. Default: `True`.
        show_signature_annotations (bool): Show the type annotations in method and function signatures. Default: `False`.
        separate_signature (bool): Whether to put the whole signature in a code block below the heading. Default: `False`.
        line_length (int): Maximum line length when formatting code. Default: `60`.
        merge_init_into_class (bool): Whether to merge the `__init__` method into the class' signature and docstring. Default: `False`.
        show_source (bool): Show the source code of this object. Default: `True`.
        show_bases (bool): Show the base classes of a class. Default: `True`.
        show_submodules (bool): When rendering a module, show its submodules recursively. Default: `True`.
        group_by_category (bool): Group the object's children by categories: attributes, classes, functions, methods, and modules. Default: `True`.
        heading_level (int): The initial heading level to use. Default: `2`.
        members_order (str): The members ordering to use. Options: `alphabetical` - order by the members names, `source` - order members as they appear in the source file. Default: `alphabetical`.
        docstring_section_style (str): The style used to render docstring sections. Options: `table`, `list`, `spacy`. Default: `table`.
    """  # noqa: E501

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the handler.

        Parameters:
            *args: Handler name, theme and custom templates.
            **kwargs: Same thing, but with keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._modules_collection: ModulesCollection = ModulesCollection()
        self._lines_collection: LinesCollection = LinesCollection()

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

        final_config = ChainMap(config, self.default_collection_config)
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

    def render(self, data: CollectorItem, config: dict) -> str:  # noqa: D102 (ignore missing docstring)
        final_config = ChainMap(config, self.default_rendering_config)

        template = self.env.get_template(f"{data.kind.value}.html")

        # Heading level is a "state" variable, that will change at each step
        # of the rendering recursion. Therefore, it's easier to use it as a plain value
        # than as an item in a dictionary.
        heading_level = final_config["heading_level"]
        try:
            final_config["members_order"] = rendering.Order(final_config["members_order"])
        except ValueError:
            choices = "', '".join(item.value for item in rendering.Order)
            raise PluginError(f"Unknown members_order '{final_config['members_order']}', choose between '{choices}'.")

        return template.render(
            **{"config": final_config, data.kind.value: data, "heading_level": heading_level, "root": True},
        )

    def update_env(self, md: Markdown, config: dict) -> None:  # noqa: D102 (ignore missing docstring)
        super().update_env(md, config)
        self.env.trim_blocks = True
        self.env.lstrip_blocks = True
        self.env.keep_trailing_newline = False
        self.env.filters["crossref"] = rendering.do_crossref
        self.env.filters["multi_crossref"] = rendering.do_multi_crossref
        self.env.filters["order_members"] = rendering.do_order_members
        self.env.filters["format_code"] = rendering.do_format_code
        self.env.filters["format_signature"] = rendering.do_format_signature
        self.env.filters["filter_docstrings"] = rendering.do_filter_docstrings

    def get_anchors(self, data: CollectorItem) -> list[str]:  # noqa: D102 (ignore missing docstring)
        try:
            return list({data.path, data.canonical_path, *data.aliases})
        except AliasResolutionError:
            return [data.path]


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
    return PythonHandler("python", theme, custom_templates)
