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

/// admonition | Example with colorful labels
    type: example

//// tab | CSS
```css
.doc-label { border-radius: 15px; padding: 0 5px; }
.doc-label-special { background-color: blue; color: white; }
.doc-label-private { background-color: red; color: white; }
.doc-label-property { background-color: green; color: white; }
.doc-label-read-only { background-color: yellow; color: black; }
```
////

//// tab | Result
<style>
  .lbl { border-radius: 15px; padding: 0 5px; }
</style>
<h3 style="margin: 0;"><span>
    <small class="lbl" style="background-color: blue; color: white !important;">special</small>
    <small class="lbl" style="background-color: red; color: white !important;">private</small>
    <small class="lbl" style="background-color: green; color: white !important;">property</small>
    <small class="lbl" style="background-color: yellow; color: black !important;">read-only</small>
</span></h3>
////

///


### Recommended style (Material)

Here are some CSS rules for the
[*Material for MkDocs*](https://squidfunk.github.io/mkdocs-material/) theme:

```css
/* Indentation. */
div.doc-contents:not(.first) {
  padding-left: 25px;
  border-left: .05rem solid var(--md-typeset-table-color);
}

/* Mark external links as such. */
a.autorefs-external::after {
  /* https://primer.style/octicons/arrow-up-right-24 */
  background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="rgb(0, 0, 0)" d="M18.25 15.5a.75.75 0 00.75-.75v-9a.75.75 0 00-.75-.75h-9a.75.75 0 000 1.5h7.19L6.22 16.72a.75.75 0 101.06 1.06L17.5 7.56v7.19c0 .414.336.75.75.75z"></path></svg>');
  content: ' ';

  display: inline-block;
  position: relative;
  top: 0.1em;
  margin-left: 0.2em;
  margin-right: 0.1em;

  height: 1em;
  width: 1em;
  border-radius: 100%;
  background-color: var(--md-typeset-a-color);
}
a.autorefs-external:hover::after {
  background-color: var(--md-accent-fg-color);
}

```

### Recommended style (ReadTheDocs)

Here are some CSS rules for the built-in *ReadTheDocs* theme:

```css
/* Indentation. */
div.doc-contents:not(.first) {
  padding-left: 25px;
  border-left: .05rem solid rgba(200, 200, 200, 0.2);
}
```

## Templates

Templates are organized into the following tree:

```tree result="text"
theme/
    attribute.html
    children.html
    class.html
    docstring/
        admonition.html
        attributes.html
        examples.html
        other_parameters.html
        parameters.html
        raises.html
        receives.html
        returns.html
        warns.html
        yields.html
    docstring.html
    expression.html
    function.html
    labels.html
    module.html
    signature.html
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
