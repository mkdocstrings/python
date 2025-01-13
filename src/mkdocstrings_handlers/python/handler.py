"""This module implements a handler for the Python language."""

from __future__ import annotations

import glob
import os
import posixpath
import sys
from contextlib import suppress
from dataclasses import asdict
from pathlib import Path
from typing import TYPE_CHECKING, Any, BinaryIO, ClassVar
from warnings import warn

from griffe import (
    AliasResolutionError,
    GriffeLoader,
    LinesCollection,
    ModulesCollection,
    Parser,
    load_extensions,
    patch_loggers,
)
from mkdocs.exceptions import PluginError
from mkdocstrings.handlers.base import BaseHandler, CollectionError, CollectorItem, HandlerOptions
from mkdocstrings.inventory import Inventory
from mkdocstrings.loggers import get_logger

from mkdocstrings_handlers.python import rendering
from mkdocstrings_handlers.python.config import PythonConfig, PythonOptions

if TYPE_CHECKING:
    from collections.abc import Iterator, Mapping, MutableMapping, Sequence

    from mkdocs.config.defaults import MkDocsConfig


if sys.version_info >= (3, 11):
    from contextlib import chdir
else:
    # TODO: remove once support for Python 3.10 is dropped
    from contextlib import contextmanager

    @contextmanager
    def chdir(path: str) -> Iterator[None]:  # noqa: D103
        old_wd = os.getcwd()
        os.chdir(path)
        try:
            yield
        finally:
            os.chdir(old_wd)


logger = get_logger(__name__)

patch_loggers(get_logger)


def _warn_extra_options(names: Sequence[str]) -> None:
    warn(
        "Passing extra options directly under `options` is deprecated. "
        "Instead, pass them under `options.extra`, and update your templates. "
        f"Current extra (unrecognized) options: {', '.join(sorted(names))}",
        DeprecationWarning,
        stacklevel=3,
    )


class PythonHandler(BaseHandler):
    """The Python handler class."""

    name: ClassVar[str] = "python"
    """The handler's name."""

    domain: ClassVar[str] = "py"
    """The cross-documentation domain/language for this handler."""

    enable_inventory: ClassVar[bool] = True
    """Whether this handler is interested in enabling the creation of the `objects.inv` Sphinx inventory file."""

    fallback_theme: ClassVar[str] = "material"
    """The fallback theme."""

    def __init__(self, config: PythonConfig, base_dir: Path, **kwargs: Any) -> None:
        """Initialize the handler.

        Parameters:
            config: The handler configuration.
            base_dir: The base directory of the project.
            **kwargs: Arguments passed to the parent constructor.
        """
        super().__init__(**kwargs)

        self.config = config
        self.base_dir = base_dir

        # YORE: Bump 2: Replace block with `self.global_options = config.options`.
        global_extra, global_options = PythonOptions._extract_extra(config.options)
        if global_extra:
            _warn_extra_options(global_extra.keys())  # type: ignore[arg-type]
        self._global_extra = global_extra
        self.global_options = global_options

        # Warn if user overrides base templates.
        if self.custom_templates:
            for theme_dir in base_dir.joinpath(self.custom_templates, "python").iterdir():
                if theme_dir.joinpath("_base").is_dir():
                    logger.warning(
                        f"Overriding base template '{theme_dir.name}/_base/<template>.html.jinja' is not supported, "
                        f"override '{theme_dir.name}/<template>.html.jinja' instead",
                    )

        paths = config.paths or []

        # Expand paths with glob patterns.
        with chdir(str(base_dir)):
            resolved_globs = [glob.glob(path) for path in paths]
        paths = [path for glob_list in resolved_globs for path in glob_list]

        # By default, add the base directory to the search paths.
        if not paths:
            paths.append(str(base_dir))

        # Initialize search paths from `sys.path`, eliminating empty paths.
        search_paths = [path for path in sys.path if path]

        for path in reversed(paths):
            # If it's not absolute, make path relative to the config file path, then make it absolute.
            if not os.path.isabs(path):
                path = os.path.abspath(base_dir / path)  # noqa: PLW2901
            # Don't add duplicates.
            if path not in search_paths:
                search_paths.insert(0, path)

        self._paths = search_paths
        self._modules_collection: ModulesCollection = ModulesCollection()
        self._lines_collection: LinesCollection = LinesCollection()

    def get_inventory_urls(self) -> list[tuple[str, dict[str, Any]]]:
        """Return the URLs of the inventory files to download."""
        return [(inv.url, inv._config) for inv in self.config.inventories]

    @staticmethod
    def load_inventory(
        in_file: BinaryIO,
        url: str,
        base_url: str | None = None,
        domains: list[str] | None = None,
        **kwargs: Any,  # noqa: ARG004
    ) -> Iterator[tuple[str, str]]:
        """Yield items and their URLs from an inventory file streamed from `in_file`.

        This implements mkdocstrings' `load_inventory` "protocol" (see [`mkdocstrings.plugin`][]).

        Arguments:
            in_file: The binary file-like object to read the inventory from.
            url: The URL that this file is being streamed from (used to guess `base_url`).
            base_url: The URL that this inventory's sub-paths are relative to.
            domains: A list of domain strings to filter the inventory by, when not passed, "py" will be used.
            **kwargs: Ignore additional arguments passed from the config.

        Yields:
            Tuples of (item identifier, item URL).
        """
        domains = domains or ["py"]
        if base_url is None:
            base_url = posixpath.dirname(url)

        for item in Inventory.parse_sphinx(in_file, domain_filter=domains).values():
            yield item.name, posixpath.join(base_url, item.uri)

    def get_options(self, local_options: Mapping[str, Any]) -> HandlerOptions:
        """Get combined default, global and local options.

        Arguments:
            local_options: The local options.

        Returns:
            The combined options.
        """
        # YORE: Bump 2: Remove block.
        local_extra, local_options = PythonOptions._extract_extra(local_options)  # type: ignore[arg-type]
        if local_extra:
            _warn_extra_options(local_extra.keys())  # type: ignore[arg-type]
        unknown_extra = self._global_extra | local_extra

        extra = {**self.global_options.get("extra", {}), **local_options.get("extra", {})}
        options = {**self.global_options, **local_options, "extra": extra}
        # YORE: Bump 2: Replace `, **unknown_extra` with `` within line.
        try:
            return PythonOptions.from_data(**options, **unknown_extra)
        except Exception as error:
            raise PluginError(f"Invalid options: {error}") from error

    def collect(self, identifier: str, options: PythonOptions) -> CollectorItem:  # noqa: D102
        module_name = identifier.split(".", 1)[0]
        unknown_module = module_name not in self._modules_collection
        if options == {} and unknown_module:
            raise CollectionError("Not loading additional modules during fallback")

        parser_name = options.docstring_style
        parser = parser_name and Parser(parser_name)
        parser_options = options.docstring_options and asdict(options.docstring_options)

        if unknown_module:
            extensions = self.normalize_extension_paths(options.extensions)
            loader = GriffeLoader(
                extensions=load_extensions(*extensions),
                search_paths=self._paths,
                docstring_parser=parser,
                docstring_options=parser_options,  # type: ignore[arg-type]
                modules_collection=self._modules_collection,
                lines_collection=self._lines_collection,
                allow_inspection=options.allow_inspection,
                force_inspection=options.force_inspection,
            )
            try:
                for pre_loaded_module in options.preload_modules:
                    if pre_loaded_module not in self._modules_collection:
                        loader.load(
                            pre_loaded_module,
                            try_relative_path=False,
                            find_stubs_package=options.find_stubs_package,
                        )
                loader.load(
                    module_name,
                    try_relative_path=False,
                    find_stubs_package=options.find_stubs_package,
                )
            except ImportError as error:
                raise CollectionError(str(error)) from error
            unresolved, iterations = loader.resolve_aliases(
                implicit=False,
                external=self.config.load_external_modules,
            )
            if unresolved:
                logger.debug(f"{len(unresolved)} aliases were still unresolved after {iterations} iterations")
                logger.debug(f"Unresolved aliases: {', '.join(sorted(unresolved))}")

        try:
            doc_object = self._modules_collection[identifier]
        except KeyError as error:
            raise CollectionError(f"{identifier} could not be found") from error
        except AliasResolutionError as error:
            raise CollectionError(str(error)) from error

        if not unknown_module:
            with suppress(AliasResolutionError):
                if doc_object.docstring is not None:
                    doc_object.docstring.parser = parser
                    doc_object.docstring.parser_options = parser_options

        return doc_object

    def render(self, data: CollectorItem, options: PythonOptions) -> str:  # noqa: D102 (ignore missing docstring)
        template_name = rendering.do_get_template(self.env, data)
        template = self.env.get_template(template_name)

        return template.render(
            **{
                "config": options,
                data.kind.value: data,
                # Heading level is a "state" variable, that will change at each step
                # of the rendering recursion. Therefore, it's easier to use it as a plain value
                # than as an item in a dictionary.
                "heading_level": options.heading_level,
                "root": True,
                "locale": self.config.locale,
            },
        )

    def update_env(self, config: Any) -> None:  # noqa: ARG002
        """Update the Jinja environment with custom filters and tests.

        Parameters:
            config: The SSG configuration.
        """
        self.env.trim_blocks = True
        self.env.lstrip_blocks = True
        self.env.keep_trailing_newline = False
        self.env.filters["split_path"] = rendering.do_split_path
        self.env.filters["crossref"] = rendering.do_crossref
        self.env.filters["multi_crossref"] = rendering.do_multi_crossref
        self.env.filters["order_members"] = rendering.do_order_members
        self.env.filters["format_code"] = rendering.do_format_code
        self.env.filters["format_signature"] = rendering.do_format_signature
        self.env.filters["format_attribute"] = rendering.do_format_attribute
        self.env.filters["filter_objects"] = rendering.do_filter_objects
        self.env.filters["stash_crossref"] = rendering.do_stash_crossref
        self.env.filters["get_template"] = rendering.do_get_template
        self.env.filters["as_attributes_section"] = rendering.do_as_attributes_section
        self.env.filters["as_functions_section"] = rendering.do_as_functions_section
        self.env.filters["as_classes_section"] = rendering.do_as_classes_section
        self.env.filters["as_modules_section"] = rendering.do_as_modules_section
        self.env.globals["AutorefsHook"] = rendering.AutorefsHook
        self.env.tests["existing_template"] = lambda template_name: template_name in self.env.list_templates()

    def get_aliases(self, identifier: str) -> tuple[str, ...]:  # noqa: D102 (ignore missing docstring)
        try:
            data = self._modules_collection[identifier]
        except KeyError:
            return ()
        aliases = [data.path]
        try:
            for alias in [data.canonical_path, *data.aliases]:
                if alias not in aliases:
                    aliases.append(alias)
        except AliasResolutionError:
            return tuple(aliases)
        return tuple(aliases)

    def normalize_extension_paths(self, extensions: Sequence) -> Sequence:
        """Resolve extension paths relative to config file."""
        normalized = []

        for ext in extensions:
            if isinstance(ext, dict):
                pth, options = next(iter(ext.items()))
                pth = str(pth)
            else:
                pth = str(ext)
                options = None

            if pth.endswith(".py") or ".py:" in pth or "/" in pth or "\\" in pth:
                # This is a system path. Normalize it, make it absolute relative to config file path.
                pth = os.path.abspath(self.base_dir / pth)

            if options is not None:
                normalized.append({pth: options})
            else:
                normalized.append(pth)

        return normalized


def get_handler(
    handler_config: MutableMapping[str, Any],
    tool_config: MkDocsConfig,
    **kwargs: Any,
) -> PythonHandler:
    """Simply return an instance of `PythonHandler`.

    Arguments:
        handler_config: The handler configuration.
        tool_config: The tool (SSG) configuration.

    Returns:
        An instance of `PythonHandler`.
    """
    base_dir = Path(tool_config.config_file_path or "./mkdocs.yml").parent
    if "inventories" not in handler_config and "import" in handler_config:
        warn("The 'import' key is renamed 'inventories' for the Python handler", FutureWarning, stacklevel=1)
        handler_config["inventories"] = handler_config.pop("import", [])
    return PythonHandler(
        config=PythonConfig.from_data(**handler_config),
        base_dir=base_dir,
        **kwargs,
    )
