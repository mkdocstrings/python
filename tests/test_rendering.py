"""Tests for the `rendering` module."""

from mkdocstrings_handlers.python import rendering


def test_format_code_and_signature():
    """Assert code and signatures can be Black-formatted."""
    assert rendering.do_format_code("print('Hello')", 100)
    assert rendering.do_format_code('print("Hello")', 100)
    assert rendering.do_format_signature("(param: str = 'hello') -> 'Class'", 100)
    assert rendering.do_format_signature('(param: str = "hello") -> "Class"', 100)
