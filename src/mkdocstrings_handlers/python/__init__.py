"""This package implements a handler for the Python language."""

from mkdocstrings_handlers.python.handler import get_handler

__all__ = ["get_handler"]  # noqa: WPS410

# TODO: CSS classes everywhere in templates
# TODO: name normalization (filenames, Jinja2 variables, HTML tags, CSS classes)
# TODO: Jinja2 blocks everywhere in templates
