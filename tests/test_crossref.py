"""Unit tests for relative crossref expansion."""

from __future__ import annotations

import inspect
import logging
import re
from pathlib import Path

from griffe.dataclasses import Class, Docstring, Function, Module, Object

from mkdocstrings_handlers.python.crossref import (  # noqa: WPS450
    _RE_REL_CROSSREF,
    _RelativeCrossrefProcessor,
    substitute_relative_crossrefs,
)


def test_substitute_relative_crossref(caplog):
    """Unit test for internal _substitute_relative_crossref method.

    Arguments:
        caplog: fixture
    """
    mod1 = Module(name="mod1", filepath=Path("mod1.py"))
    mod2 = Module(name="mod2", parent=mod1, filepath=Path("mod2.py"))
    cls1 = Class(name="Class1", parent=mod2)
    meth1 = Function(name="meth1", parent=cls1)

    def assert_sub(parent: Object, text: str, ref: str, expected: str = "", warning: str = ""):  # noqa: WPS218,WPS430
        if not expected:
            expected = ref
        crossref = f"[{text}][{ref}]"
        doc = Docstring(parent=parent, value=crossref, lineno=42)  # noqa: WPS432
        match = _RE_REL_CROSSREF.fullmatch(crossref)
        assert match is not None
        caplog.clear()
        actual = _RelativeCrossrefProcessor(doc)(match)
        if warning:
            assert len(caplog.records) == 1
            _, level, msg = caplog.record_tuples[0]
            assert level == logging.WARNING
            assert re.search(warning, msg)
            assert f"{parent.filepath}" in msg
        else:
            assert not caplog.records
        assert actual == f"[{text}][{expected}]"

    assert_sub(meth1, "foo", ".", "mod1.mod2.Class1.foo")
    assert_sub(cls1, "foo", ".", "mod1.mod2.Class1.foo")
    assert_sub(meth1, "foo", "^", "mod1.mod2.Class1")
    assert_sub(meth1, "foo", "^.", "mod1.mod2.Class1.foo")
    assert_sub(meth1, "foo", ".bar", "mod1.mod2.Class1.bar")
    assert_sub(meth1, "foo", "(c)", "mod1.mod2.Class1")
    assert_sub(meth1, "foo", "(c).", "mod1.mod2.Class1.foo")
    assert_sub(meth1, "foo", "(C).baz", "mod1.mod2.Class1.baz")
    assert_sub(meth1, "foo", "(c).baz.", "mod1.mod2.Class1.baz.foo")
    assert_sub(meth1, "foo", "(m).", "mod1.mod2.foo")
    assert_sub(meth1, "foo", "mod3.", "mod3.foo")
    assert_sub(meth1, "foo", "^^.", "mod1.mod2.foo")

    # Error cases

    assert_sub(meth1, "foo", ".bad+syntax", warning="Bad syntax")
    assert_sub(meth1, "bad id", ".", warning="not a qualified identifier")
    assert_sub(mod2, "foo", "(c)", warning="not in a class")
    assert_sub(meth1, "foo", "^^^^", warning="too many levels")


def test_substitute_relative_crossrefs(caplog):
    """Unit test for substitute_relative_crossrefs.

    Arguments:
        caplog: fixture
    """
    mod1 = Module(name="mod1", filepath=Path("mod1.py"))
    mod2 = Module(name="mod2", parent=mod1, filepath=Path("mod2.py"))
    mod1.members["mod2"] = mod2
    cls1 = Class(name="Class1", parent=mod2)
    mod2.members["Class1"] = cls1
    meth1 = Function(name="meth1", parent=cls1)
    cls1.members["meth1"] = meth1

    meth1.docstring = Docstring(
        """
    [foo][.]
    [bar][(m).]
    """,
        parent=meth1,
        lineno=42,  # noqa: WPS432
    )

    mod1.docstring = Docstring(
        """
    [mod2.Class1][.]
    """,
        parent=mod1,
        lineno=23,  # noqa: WPS432
    )

    substitute_relative_crossrefs(mod1)

    assert meth1.docstring.value == inspect.cleandoc(
        """
    [foo][mod1.mod2.Class1.foo]
    [bar][mod1.mod2.bar]
    """
    )  # noqa: WPS355

    assert not caplog.records
