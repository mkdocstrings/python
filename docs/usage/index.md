# Usage

TIP: **This is the documentation for the NEW Python handler.**
To read the documentation for the LEGACY handler,
go to the [legacy handler documentation](https://mkdocstrings.github.io/python-legacy).

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

The Python handler is the default *mkdocstrings* handler.
You can change the default handler,
or explicitely set the Python handler as default by defining the `default_handler`
configuration option of `mkdocstrings` in `mkdocs.yml`:

```yaml title="mkdocs.yml"
plugins:
- mkdocstrings:
    default_handler: python
```

## Injecting documentation

With the Python handler installed and configured as default handler,
you can inject documentation for a module, class, function, or any other Python object
with *mkdocstrings*' [autodoc syntax], in your Markdown pages:

```md
::: path.to.object
```

If another handler was defined as default handler,
you can explicitely ask for the Python handler to be used when injecting documentation
with the `handler` option:

```md
::: path.to.object
    handler: python
```

## Configuration

When installed, the Python handler becomes the default *mkdocstrings* handler.
You can configure it in `mkdocs.yml`:

```yaml title="mkdocs.yml"
plugins:
- mkdocstrings:
    handlers:
      python:
        ...  # the Python handler configuration
```

### Global-only options

Some options are **global only**, and go directly under the handler's name.

[](){#setting-inventories}
#### `inventories`

This option is used to load Sphinx-compatible objects inventories from other
documentation sites. For example, you can load the standard library
objects inventory like this:

```yaml title="mkdocs.yml"
plugins:
- mkdocstrings:
    handlers:
      python:
        inventories:
        - https://docs.python.org/3/objects.inv
```

When loading an inventory, you enable automatic cross-references
to other documentation sites like the standard library docs
or any third-party package docs. Typically, you want to load
the inventories of your project's dependencies, at least those
that are used in the public API.

See [*mkdocstrings*' documentation on inventories][inventories]
for more details.

  [inventories]: https://mkdocstrings.github.io/usage/#cross-references-to-other-projects-inventories

Additionally, the Python handler accepts a `domains` option in the inventory options,
which allows to select the inventory domains to load.
By default the Python handler only selects the `py` domain (for Python objects).
You might find useful to also enable the [`std` domain][std domain]:

  [std domain]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-standard-domain

```yaml title="mkdocs.yml"
plugins:
- mkdocstrings:
    handlers:
      python:
        inventories:
        - url: https://docs.python-requests.org/en/master/objects.inv
          domains: [std, py]
```

[](){#setting-load_external_modules}
#### `load_external_modules`

This option allows resolving aliases (imports) to any external module.
Modules are considered external when they are not part
of the package your are injecting documentation for.
Setting this option to `True` will tell the handler to resolve aliases recursively
when they are made public through the [`__all__`][__all__] variable.
By default, the handler will only resolve aliases when they point at a private sibling
of the source package, for example aliases going from `ast` to `_ast`.
Set `load_external_modules` to `False` to prevent even that.

WARNING: **Use with caution**
This can load a *lot* of modules through [Griffe],
slowing down your build or triggering errors that Griffe does not yet handle.
**We recommend using the [`preload_modules`][] option instead**,
which acts as an include-list rather than as include-all.

Example:

```yaml title="mkdocs.yml"
plugins:
- mkdocstrings:
    handlers:
      python:
        load_external_modules: true
```

  [__all__]: https://docs.python.org/3/tutorial/modules.html#importing-from-a-package

[](){#setting-locale}
#### `locale`

The locale to use when translating template strings. The translation system is not fully ready yet, so we don't recommend setting the option for now.

[](){#setting-paths}
#### `paths`

This option is used to provide filesystem paths in which to search for Python modules.
Non-absolute paths are computed as relative to MkDocs configuration file. Example:

```yaml title="mkdocs.yml"
plugins:
- mkdocstrings:
    handlers:
      python:
        paths: [src]  # search packages in the src folder
```

More details at [Finding modules](#finding-modules).

[](){#setting-options}
### Global/local options

The other options can be used both globally *and* locally, under the `options` key.
For example, globally:

```yaml title="mkdocs.yml"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          do_something: true
```

...and locally, overriding the global configuration:

```md title="docs/some_page.md"
::: package.module.class
    options:
      do_something: false
```

These options affect how the documentation is collected from sources and rendered.
See the following tables summarizing the options, and get more details for each option
in the following pages:

- [General options](configuration/general.md): various options that do not fit in the other categories
- [Headings options](configuration/headings.md): options related to headings and the table of contents
    (or sidebar, depending on the theme used)
- [Members options](configuration/members.md): options related to filtering or ordering members
    in the generated documentation
- [Docstrings options](configuration/docstrings.md): options related to docstrings (parsing and rendering)
- [Signature options](configuration/signatures.md): options related to signatures and type annotations

## Finding modules

There are multiple ways to tell the handler where to find your packages/modules.

**The recommended method is to use the `paths` option, as it's the only one
that works with the `-f` option of MkDocs, allowing to build the documentation
from any location on the file system.** Indeed, the paths provided with the
`paths` option are computed as relative to the configuration file (mkdocs.yml),
so that the current working directory has no impact on the build process:
*you can build the docs from any location on your filesystem*.

### Using the `paths` option

TIP: **This is the recommended method.**

1. mkdocs.yml in root, package in root
    ```tree
    root/
        mkdocs.yml
        package/
    ```

    ```yaml title="mkdocs.yml"
    plugins:
    - mkdocstrings:
        handlers:
          python:
            paths: [.]  # actually not needed, default
    ```

1. mkdocs.yml in root, package in subfolder
    ```tree
    root/
        mkdocs.yml
        src/
            package/
    ```

    ```yaml title="mkdocs.yml"
    plugins:
    - mkdocstrings:
        handlers:
          python:
            paths: [src]
    ```

1. mkdocs.yml in subfolder, package in root
    ```tree
    root/
        docs/
            mkdocs.yml
        package/
    ```

    ```yaml title="mkdocs.yml"
    plugins:
    - mkdocstrings:
        handlers:
          python:
            paths: [..]
    ```

1. mkdocs.yml in subfolder, package in subfolder
    ```tree
    root/
        docs/
            mkdocs.yml
        src/
            package/
    ```

    ```yaml title="mkdocs.yml"
    plugins:
    - mkdocstrings:
        handlers:
          python:
            paths: [../src]
    ```

Except for case 1, which is supported by default, **we strongly recommend
setting the path to your packages using this option, even if it works without it**
(for example because your project manager automatically adds `src` to PYTHONPATH),
to make sure anyone can build your docs from any location on their filesystem.

### Using the PYTHONPATH environment variable

WARNING: **This method has limitations.**
This method might work for you, with your current setup,
but not for others trying your build your docs with their own setup/environment.
We recommend using the [`paths` method](#using-the-paths-option) instead.

You can take advantage of the usual Python loading mechanisms.
In Bash and other shells, you can run your command like this
(note the prepended `PYTHONPATH=...`):

1. mkdocs.yml in root, package in root
    ```tree
    root/
        mkdocs.yml
        package/
    ```

    ```bash
    PYTHONPATH=. mkdocs build  # actually not needed, default
    ```

1. mkdocs.yml in root, package in subfolder
    ```tree
    root/
        mkdocs.yml
        src/
            package/
    ```

    ```bash
    PYTHONPATH=src mkdocs build
    ```

1. mkdocs.yml in subfolder, package in root
    ```tree
    root/
        docs/
            mkdocs.yml
        package/
    ```

    ```bash
    PYTHONPATH=. mkdocs build -f docs/mkdocs.yml
    ```

1. mkdocs.yml in subfolder, package in subfolder
    ```tree
    root/
        docs/
            mkdocs.yml
        src/
            package/
    ```

    ```bash
    PYTHONPATH=src mkdocs build -f docs/mkdocs.yml
    ```

### Installing your package in the current Python environment

WARNING: **This method has limitations.**
This method might work for you, with your current setup,
but not for others trying your build your docs with their own setup/environment.
We recommend using the [`paths` method](#using-the-paths-option) instead.

Install your package in the current environment, and run MkDocs:

/// tab | pip
```bash
. venv/bin/activate
pip install -e .
mkdocs build
```
///

/// tab | PDM
```bash
pdm install
pdm run mkdocs build
```
///

/// tab | Poetry
```bash
poetry install
poetry run mkdocs build
```
///
