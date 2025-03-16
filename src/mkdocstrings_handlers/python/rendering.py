"""Deprecated. Import from `mkdocstrings_handlers.python` directly."""

# YORE: Bump 2: Remove file.

import warnings
from typing import Any

from mkdocstrings_handlers.python._internal import rendering


def __getattr__(name: str) -> Any:
    warnings.warn(
        "Importing from `mkdocstrings_handlers.python.rendering` is deprecated. Import from `mkdocstrings_handlers.python` directly.",
        DeprecationWarning,
        stacklevel=2,
    )
    return getattr(rendering, name)
