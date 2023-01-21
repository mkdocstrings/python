<h1 align="center">mkdocstrings-python</h1>

<p align="center">A Python handler for <a href="https://github.com/mkdocstrings/mkdocstrings"><i>mkdocstrings</i></a>.</p>

<p align="center">
  <a href="https://github.com/mkdocstrings/python/actions?query=workflow%3Aci">
    <img alt="ci" src="https://github.com/mkdocstrings/python/workflows/ci/badge.svg" />
  </a>
  <a href="https://mkdocstrings.github.io/python/">
    <img alt="documentation" src="https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat" />
  </a>
  <a href="https://pypi.org/project/mkdocstrings-python/">
    <img alt="pypi version" src="https://img.shields.io/pypi/v/mkdocstrings-python.svg" />
  </a>
  <a href="https://gitpod.io/#https://github.com/mkdocstrings/python">
    <img alt="gitpod" src="https://img.shields.io/badge/gitpod-workspace-blue.svg?style=flat" />
  </a>
  <a href="https://gitter.im/mkdocstrings/python">
    <img alt="gitter" src="https://badges.gitter.im/join%20chat.svg" />
  </a>
</p>

---

<p align="center"><img src="logo.png"></p>

## Installation

You can install this handler as a *mkdocstrings* extra:

```toml title="pyproject.toml"
# PEP 621 dependencies declaration
# adapt to your dependencies manager
[project]
dependencies = [
    "mkdocstrings[python]>=0.18",
]
```

You can also explicitly depend on the handler:

```toml title="pyproject.toml"
# PEP 621 dependencies declaration
# adapt to your dependencies manager
[project]
dependencies = [
    "mkdocstrings-python",
]
```

## Preview

<!-- TODO: update the GIF with a more recent screen capture. Maybe use mp4 instead -->
![mkdocstrings_python_gif](https://user-images.githubusercontent.com/3999221/77157838-7184db80-6aa2-11ea-9f9a-fe77405202de.gif)

## Features

- **Data collection from source code**: collection of the object-tree and the docstrings is done thanks to
  [Griffe](https://github.com/mkdocstrings/griffe).

- **Support for type annotations:** Griffe collects your type annotations and *mkdocstrings* uses them
  to display parameter types or return types. It is even able to automatically add cross-references
  to other objects from your API, from the standard library or third-party libraries!
  See [how to load inventories](https://mkdocstrings.github.io/usage/#cross-references-to-other-projects-inventories) to enable it.

- **Recursive documentation of Python objects:** just use the module dotted-path as an identifier, and you get the full
  module docs. You don't need to inject documentation for each class, function, etc.

- **Support for documented attributes:** attributes (variables) followed by a docstring (triple-quoted string) will
  be recognized by Griffe in modules, classes and even in `__init__` methods.

- **Multiple docstring-styles support:** common support for Google-style, Numpydoc-style,
  and Sphinx-style docstrings. See [Griffe's documentation](https://mkdocstrings.github.io/griffe/docstrings/) on docstrings support.

- **Admonition support in Google docstrings:** blocks like `Note:` or `Warning:` will be transformed
  to their [admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) equivalent.
  *We do not support nested admonitions in docstrings!*

- **Every object has a TOC entry:** we render a heading for each object, meaning *MkDocs* picks them into the Table
  of Contents, which is nicely displayed by the Material theme. Thanks to *mkdocstrings* cross-reference ability,
  you can reference other objects within your docstrings, with the classic Markdown syntax:
  `[this object][package.module.object]` or directly with `[package.module.object][]`

- **Source code display:** *mkdocstrings* can add a collapsible div containing the highlighted source code
  of the Python object.
