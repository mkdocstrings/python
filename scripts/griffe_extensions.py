# Custom extensions for Griffe.

from __future__ import annotations

import ast
from typing import Any

import griffe

_logger = griffe.get_logger("griffe_extensions")


class CustomFields(griffe.Extension):
    """Support our custom dataclass fields."""

    def on_attribute_instance(
        self,
        *,
        attr: griffe.Attribute,
        agent: griffe.Visitor | griffe.Inspector,
        **kwargs: Any,  # noqa: ARG002
    ) -> None:
        """Fetch descriptions from `Field` annotations."""
        if attr.docstring:
            return
        try:
            field: griffe.ExprCall = attr.annotation.slice.elements[1]  # type: ignore[union-attr]
        except AttributeError:
            return

        if field.canonical_path == "mkdocstrings_handlers.python._internal.config._Field":
            description = next(
                attr.value
                for attr in field.arguments
                if isinstance(attr, griffe.ExprKeyword) and attr.name == "description"
            )
            if not isinstance(description, str):
                _logger.warning(f"Field description of {attr.path} is not a static string")
                description = str(description)

            attr.docstring = griffe.Docstring(
                ast.literal_eval(description),
                parent=attr,
                parser=agent.docstring_parser,
                parser_options=agent.docstring_options,
            )
