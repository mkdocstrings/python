# Usage

TIP: **This is the documentation for the NEW Python handler.**  
To read the documentation for the LEGACY handler,
go to the [legacy handler documentation](https://mkdocstrings.github.io/python-legacy).

The tool used by the Python handler to collect documentation from Python source code
is [Griffe](https://mkdocstrings.github.io/griffe). The word "griffe" can sometimes be used instead of "signature" in french.
Griffe is able to visit the Abstract Syntax Tree (AST) of the source code to extract useful information.
It is also able to execute the code (by importing it) and introspect objects in memory
when source code is not available. Finally, it can parse docstrings following different styles,
see [Supported docstrings styles](#supported-docstrings-styles).

Like every handler, the Python handler accepts both **global** and **local** options.

## Global-only options

Some options are **global only**, and go directly under the handler's name.

- `import`: this option is used to import Sphinx-compatible objects inventories from other
    documentation sites. For example, you can import the standard library
    objects inventory like this:

    ```yaml title="mkdocs.yml"
    plugins:
    - mkdocstrings:
        handlers:
          python:
            import:
            - https://docs.python-requests.org/en/master/objects.inv
    ```

    When importing an inventory, you enable automatic cross-references
    to other documentation sites like the standard library docs
    or any third-party package docs. Typically, you want to import
    the inventories of your project's dependencies, at least those
    that are used in the public API. 

    NOTE: This global option is common to *all* handlers, however
    they might implement it differently (or not even implement it).

- `paths`: this option is used to provide filesystem paths in which to search for Python modules.
    Non-absolute paths are computed as relative to MkDocs configuration file. Example:

    ```yaml title="mkdocs.yml"
    plugins:
    - mkdocstrings:
        handlers:
          python:
            paths: [src]  # search packages in the src folder
    ```

    More details at [Finding modules](#finding-modules).

- `load_external_modules`:
  this option allows resolving aliases to any external module.  
  Enabling this option will tell handler that when it encounters an import that is made public  
  through the `__all__` variable, it will resolve it recursively to *any* module.  
  **Use with caution:** this can load a *lot* of modules, slowing down your build  
  or triggering errors that we do not yet handle.  
  **We recommend using the `preload_modules` option instead**,  
  which acts as an include-list rather than as include-all.  

## Global/local options

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

These options affect how the documentation is collected from sources and rendered:
headings, members, docstrings, etc.

::: mkdocstrings_handlers.python.handler.PythonHandler.default_config
    options:
      show_root_toc_entry: false

## Supported docstrings styles

Griffe supports the Google-style, Numpy-style and Sphinx-style docstring formats.
The style used by default is the Google-style.
You can configure what style you want to use with
the `docstring_style` and `docstring_options` options,
both globally or locally, i.e. per autodoc instruction.

- Google: see [Napoleon's documentation](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
- Numpy: see [Numpydoc's documentation](https://numpydoc.readthedocs.io/en/latest/format.html).
- Sphinx: see [Sphinx's documentation](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html).

See the supported docstring sections on [Griffe's documentation](https://mkdocstrings.github.io/griffe/docstrings/).

NOTE: As Numpy-style is partially supported by the underlying parser,
you may experience problems in the building process if your docstring
has a `Methods` section in the class docstring
(see [#366](https://github.com/mkdocstrings/mkdocstrings/issues/366)).

### Google-style admonitions

With Google-style docstrings, any section that is not recognized will be transformed into its admonition equivalent.
For example:

=== "Docstring"
    ```python
    """
    Note:
        It looks like a section, but it will be rendered as an admonition.

    Tip: You can even choose a title.
        This admonition has a custom title!
    """
    ```
    
=== "Result"
    NOTE: It looks like a section, but it will be rendered as an admonition.

    TIP: **You can even choose a title.**  
    This admonition has a custom title!

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

=== "pip"
    ```bash
    . venv/bin/activate
    pip install -e .
    mkdocs build
    ```

=== "PDM"
    ```bash
    pdm install
    pdm run mkdocs build
    ```

=== "Poetry"
    ```bash
    poetry install
    poetry run mkdocs build
    ```
