"""Tests for configuration options."""

from __future__ import annotations

import inspect
from dataclasses import asdict, fields
from typing import TYPE_CHECKING, Any

import pytest
from griffe import Parser, parse_google, parse_numpy, parse_sphinx

from mkdocstrings_handlers.python import AutoStyleOptions, GoogleStyleOptions, NumpyStyleOptions, SphinxStyleOptions
from mkdocstrings_handlers.python._internal.handler import _filter_parser_options

if TYPE_CHECKING:
    from collections.abc import Callable


@pytest.mark.parametrize(
    ("options_class", "parser"),
    [
        (GoogleStyleOptions, parse_google),
        (NumpyStyleOptions, parse_numpy),
        (SphinxStyleOptions, parse_sphinx),
    ],
)
def test_style_options_match_griffe_parser(options_class: type[Any], parser: Callable[..., object]) -> None:
    """Ensure style options stay in sync with Griffe parser options."""
    option_names = {field.name for field in fields(options_class)}
    parser_parameters = inspect.signature(parser).parameters
    parser_option_names = set(parser_parameters) - {"docstring"}

    assert parser_option_names <= option_names


def test_filter_style_options(caplog: pytest.LogCaptureFixture) -> None:
    """Ensure unsupported options are not passed to Griffe and are reported."""
    options = asdict(SphinxStyleOptions())

    filtered_options = _filter_parser_options(Parser.sphinx, options)

    assert filtered_options == {
        name: value for name, value in options.items() if name in inspect.signature(parse_sphinx).parameters
    }
    assert "warn_missing_types" in options
    for name in set(options) - set(filtered_options or {}):
        assert f"Ignoring unsupported sphinx docstring parser option: {name}" in caplog.text


def test_filter_auto_style_options(caplog: pytest.LogCaptureFixture) -> None:
    """Ensure unsupported options nested in auto style options are reported."""
    options = asdict(AutoStyleOptions())

    filtered_options = _filter_parser_options(Parser.auto, options)

    assert filtered_options is not None
    if "warn_missing_types" in inspect.signature(parse_sphinx).parameters:
        assert "warn_missing_types" in filtered_options["per_style_options"]["sphinx"]
    else:
        assert "warn_missing_types" not in filtered_options["per_style_options"]["sphinx"]
        assert "Ignoring unsupported sphinx docstring parser option: warn_missing_types" in caplog.text
