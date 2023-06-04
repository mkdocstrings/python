# Customization

It is possible to customize the output of the generated documentation with CSS
and/or by overriding templates.

## CSS classes

The following CSS classes are used in the generated HTML:

- `doc`: on all the following elements
- `doc-children`: on `div`s containing the children of an object
- `doc-object`: on `div`s containing an object
    - `doc-attribute`: on `div`s containing an attribute
    - `doc-class`: on `div`s containing a class
    - `doc-function`: on `div`s containing a function
    - `doc-module`: on `div`s containing a module
- `doc-heading`: on objects headings
    - `doc-object-name`: on `span`s wrapping objects names/paths in the heading
        - `doc-KIND-name`: as above, specific to the kind of object (module, class, function, attribute)
- `doc-contents`: on `div`s wrapping the docstring then the children (if any)
    - `first`: same, but only on the root object's contents `div`
- `doc-labels`: on `span`s wrapping the object's labels
    - `doc-label`: on `small` elements containing a label
        - `doc-label-LABEL`: same, where `LABEL` is replaced by the actual label
- `doc-md-description`: on `div`s containing HTML descriptions converted from Markdown docstrings

/// admonition | Example with colorful labels
    type: example

//// tab | CSS
```css
.doc-label { border-radius: 15px; padding: 2px 8px; font-weight: bold; }
.doc-label-special { background-color: #3330E4; color: white; }
.doc-label-private { background-color: #F637EC; color: white; }
.doc-label-property { background-color: #FBB454; color: black; }
.doc-label-read-only { background-color: #FAEA48; color: black; }
```
////

//// tab | Result
<style>
  .lbl { border-radius: 15px; padding: 2px 8px; font-weight: bold; }
</style>
<h3 style="margin: 0;">
  <p>
  <small class="lbl" style="background-color: #3330E4; color: white !important;">special</small>
  <small class="lbl" style="background-color: #F637EC; color: white !important;">private</small>
  <small class="lbl" style="background-color: #FBB454; color: black !important;">property</small>
  <small class="lbl" style="background-color: #FAEA48; color: black !important;">read-only</small>
  </p>
</h3>
////

///

## Templates

Templates are organized into the following tree:

```python exec="1" result="tree"
from pathlib import Path

basedir = "src/mkdocstrings_handlers/python/templates/material"
print("theme/")
for filepath in sorted(path for path in Path(basedir).rglob("*") if "_base" not in str(path) and path.suffix != ".css"):
    print("    " * (len(filepath.relative_to(basedir).parent.parts) + 1) + filepath.name + ("/" if filepath.is_dir() else ""))
```

See them [in the repository](https://github.com/mkdocstrings/python/tree/master/src/mkdocstrings_handlers/python/templates/).
See the general *mkdocstrings* documentation to learn how to override them: https://mkdocstrings.github.io/theming/#templates.

In preparation for Jinja2 blocks, which will improve customization,
each one of these templates extends a base version in `theme/_base`. Example:

```html+jinja title="theme/docstring/admonition.html"
{% extends "_base/docstring/admonition.html" %}
```

```html+jinja title="theme/_base/docstring/admonition.html"
{{ log.debug() }}
<details class="{{ section.value.kind }}">
  <summary>{{ section.title|convert_markdown(heading_level, html_id, strip_paragraph=True) }}</summary>
  {{ section.value.contents|convert_markdown(heading_level, html_id) }}
</details>
```

It means you will be able to customize only *parts* of a template
without having to fully copy-paste it into your project:

```jinja title="templates/theme/docstring.html"
{% extends "_base/docstring.html" %}
{% block contents %}
  {{ block.super }}
  Additional contents
{% endblock contents %}
```

WARNING: **Block-level customization is not ready yet. We welcome [suggestions](https://github.com/mkdocstrings/python/issues/new).**

## Style recommendations

<a id="recommended-style-material"></a>

### Material

Here are some CSS rules for the [Material for MkDocs] theme:

```css
--8<-- "docs/css/mkdocstrings.css"
```

<a id="recommended-style-readthedocs"></a>

### ReadTheDocs

Here are some CSS rules for the built-in ReadTheDocs theme:

```css
/* Indentation. */
div.doc-contents:not(.first) {
  padding-left: 25px;
  border-left: .05rem solid rgba(200, 200, 200, 0.2);
}
```