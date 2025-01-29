# Google style

## :warning: Work in Progress!

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

See [Napoleon's documentation](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
See the supported docstring sections on [Griffe's documentation](https://mkdocstrings.github.io/griffe/docstrings/).
