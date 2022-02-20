"""Tests for the `collector` module."""

import pytest

from mkdocstrings_handlers.python.collector import CollectionError, PythonCollector


def test_collect_missing_module():
    """Assert error is raised for missing modules."""
    collector = PythonCollector()
    with pytest.raises(CollectionError):
        collector.collect("aaaaaaaa", {})


def test_collect_missing_module_item():
    """Assert error is raised for missing items within existing modules."""
    collector = PythonCollector()
    with pytest.raises(CollectionError):
        collector.collect("mkdocstrings.aaaaaaaa", {})


def test_collect_module():
    """Assert existing module can be collected."""
    collector = PythonCollector()
    assert collector.collect("mkdocstrings", {})


def test_collect_with_null_parser():
    """Assert we can pass `None` as parser when collecting."""
    collector = PythonCollector()
    assert collector.collect("mkdocstrings", {"docstring_style": None})
