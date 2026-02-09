# mkdocstrings-python

A Python handler for [*mkdocstrings*](https://github.com/mkdocstrings/mkdocstrings).

______________________________________________________________________

The Python handler uses [Griffe](https://mkdocstrings.github.io/griffe) to collect documentation from Python source code. The word "griffe" can sometimes be used instead of "signature" in French. Griffe is able to visit the Abstract Syntax Tree (AST) of the source code to extract useful information. It is also able to execute the code (by importing it) and introspect objects in memory when source code is not available. Finally, it can parse docstrings following different styles.

## Installation

You can install this handler as a *mkdocstrings* extra:

pyproject.toml

```toml
# PEP 621 dependencies declaration
# adapt to your dependencies manager
[project]
dependencies = [
    "mkdocstrings[python]>=0.18",
]
```

You can also explicitly depend on the handler:

pyproject.toml

```toml
# PEP 621 dependencies declaration
# adapt to your dependencies manager
[project]
dependencies = [
    "mkdocstrings-python",
]
```

## Preview

## Features

- **Data collection from source code**: collection of the object-tree and the docstrings is done thanks to [Griffe](https://github.com/mkdocstrings/griffe).
- **Support for type annotations:** Griffe collects your type annotations and *mkdocstrings* uses them to display parameter types or return types. It is even able to automatically add cross-references to other objects from your API, from the standard library or third-party libraries! See [how to load inventories](https://mkdocstrings.github.io/usage/#cross-references-to-other-projects-inventories) to enable it.
- **Recursive documentation of Python objects:** just use the module dotted-path as an identifier, and you get the full module docs. You don't need to inject documentation for each class, function, etc.
- **Support for documented attributes:** attributes (variables) followed by a docstring (triple-quoted string) will be recognized by Griffe in modules, classes and even in `__init__` methods.
- **Multiple docstring-styles support:** common support for Google-style, Numpydoc-style, and Sphinx-style docstrings. See [Griffe's documentation](https://mkdocstrings.github.io/griffe/docstrings/) on docstrings support.
- **Admonition support in Google docstrings:** blocks like `Note:` or `Warning:` will be transformed to their [admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) equivalent. *We do not support nested admonitions in docstrings!*
- **Every object has a TOC entry:** we render a heading for each object, meaning *MkDocs* picks them into the Table of Contents, which is nicely displayed by the Material theme. Thanks to *mkdocstrings* cross-reference ability, you can reference other objects within your docstrings, with the classic Markdown syntax: `[this object][package.module.object]` or directly with `[package.module.object][]`
- **Source code display:** *mkdocstrings* can add a collapsible div containing the highlighted source code of the Python object.

## Sponsors

**Silver sponsors**

**Bronze sponsors**

______________________________________________________________________

*And 7 more private sponsor(s).*
