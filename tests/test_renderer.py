"""Tests for the `renderer` module."""

import pytest
from griffe.docstrings.dataclasses import DocstringSection, DocstringSectionKind


@pytest.mark.parametrize(
    "renderer",
    [
        {"theme": "mkdocs"},
        {"theme": "readthedocs"},
        {"theme": {"name": "material"}},
    ],
    indirect=["renderer"],
)
def test_render_docstring_examples_section(renderer):
    """Assert docstrings' examples section can be rendered.

    Parameters:
        renderer: A renderer instance (parametrized).
    """
    section = DocstringSection(
        DocstringSectionKind.examples,
        value=[
            (DocstringSectionKind.text, "This is an example."),
            (DocstringSectionKind.examples, ">>> print('Hello')\nHello"),
        ],
    )
    template = renderer.env.get_template("docstring/examples.html")
    rendered = template.render(section=section)
    assert "<p>This is an example.</p>" in rendered
    assert "print" in rendered
    assert "Hello" in rendered
