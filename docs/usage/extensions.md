# Extensions

## :warning: Work in Progress!

The Python handler supports extensions through
[*mkdocstrings*' handler extensions](https://mkdocstrings.github.io/usage/handlers/#handler-extensions).

Specifically, additional templates can be added to the handler,
and Griffe extensions can instruct the handler to use a particular template
for a particular object by setting a value in the Griffe object's `extra` dictionary:

```python title="griffe_extension.py"
obj = ...  # get a reference to a Griffe object
if "mkdocstrings" not in obj.extra:
    obj.extra["mkdocstrings"] = {}
obj.extra["mkdocstrings"]["template"] = "template_name.html"
```
