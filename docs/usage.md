## Handler options

!!! warning "This the documentation for the NEW, EXPERIMENTAL Python handler."
    To read the documentation for the LEGACY handler,
    go to the [legacy handler documentation](https://mkdocstrings.github.io/python-legacy).

Like every handler, the Python handler accepts the common
[`selection`](#selection) and [`rendering`](#rendering) options,
both as **global** and **local** options.
The `selection` options gives you control over the selection of Python objects,
while the `rendering` options lets you change how the documentation is rendered.

### Selection

The following options are directly passed to the handler's collector.
See [Collector: Griffe](#collector-griffe) to learn more about Griffe.

Option | Description
------ | -----------
**`docstring_style`** | Type: `str`. Docstring style to parse: `google` (default), `numpy` or `sphinx`.
**`docstring_options`** | Type: `dict`. Options to pass to the docstring parser. See [Collector: Griffe](#collector-griffe).

!!! example "Configuration example"
    === "Global"
        ```yaml
        # mkdocs.yml
        plugins:
          - mkdocstrings:
              handlers:
                python:
                  selection:
                    docstring_style: google
        ```
        
    === "Local"
        ```yaml
        ::: my_package
            selection:
              docstring_style: sphinx
        ```
    
### Rendering

::: mkdocstrings_handlers.python.renderer.PythonRenderer.default_config
    rendering:
      show_root_toc_entry: false

These options affect how the documentation is rendered.

!!! example "Configuration example"
    === "Global"
        ```yaml
        # mkdocs.yml
        plugins:
          - mkdocstrings:
              handlers:
                python:
                  rendering:
                    show_root_heading: yes
        ```
        
    === "Local"
        ```md
        ## `ClassA`

        ::: my_package.my_module.ClassA
            rendering:
              show_root_heading: no
              heading_level: 3
        ```

## Collector: Griffe

The tool used by the Python handler to collect documentation from Python source code
is [Griffe](https://mkdocstrings.github.io/griffe). Griffe can mean "signature" in french.

### Supported docstrings styles

Griffe supports the Google-style, Numpy-style and Sphinx-style docstring formats.
The style used by default is the Google-style.
You can configure what style you want to use with
the `docstring_style` and `docstring_options` [selection options](#selection),
both globally or per autodoc instruction.

- Google: see [Napoleon's documentation](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
- Numpy: see [Numpydoc's documentation](https://numpydoc.readthedocs.io/en/latest/format.html).
- Sphinx: see [Sphinx's documentation](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html).

See the supported docstring sections on [Griffe's documentation](https://mkdocstrings.github.io/griffe/docstrings/).

#### Google-style admonitions

With Google-style docstrings, any section that is not recognized will be transformed into its admonition equivalent.
For example:

=== "Docstring"
    ```python
    """
    Important:
        It looks like a section, but it will be rendered as an admonition.

    Tip: You can even chose a title.
        This admonition has a custom title!
    """
    ```
    
=== "Result"
    !!! important
        It looks like a section, but it will be rendered as an admonition.

    !!! tip "You can even chose a title."
        This admonition has a custom title!

## Finding modules

In order for Griffe to find your packages and modules,
you can take advantage of the usual Python loading mechanisms:

- install your package in the current virtualenv:
    ```bash
    . venv/bin/activate
    pip install -e .
    ```
  
    ```bash
    poetry install
    ```
  
    ...etc.
    
- or add your package(s) parent directory in the `PYTHONPATH`.
  
(*The following instructions assume your Python package is in the `src` directory.*)

In Bash and other shells, you can run your command like this
(note the prepended `PYTHONPATH=...`):

```console
$ PYTHONPATH=src mkdocs serve
```

You can also export that variable,
but this is **not recommended** as it could affect other Python processes:

```bash
export PYTHONPATH=src  # Linux/Bash and similar
setx PYTHONPATH src  # Windows, USE AT YOUR OWN RISKS
```

## Recommended style (Material)

Here are some CSS rules for the
[*Material for MkDocs*](https://squidfunk.github.io/mkdocs-material/) theme:

```css
/* Indentation. */
div.doc-contents:not(.first) {
  padding-left: 25px;
  border-left: .05rem solid var(--md-default-fg-color--lightest);
  margin-bottom: 80px;
}
```

## Recommended style (ReadTheDocs)

Here are some CSS rules for the built-in *ReadTheDocs* theme:

```css
/* Indentation. */
div.doc-contents:not(.first) {
  padding-left: 25px;
  border-left: .05rem solid rgba(200, 200, 200, 0.2);
  margin-bottom: 60px;
}
```
