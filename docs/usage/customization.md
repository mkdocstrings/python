# Customization

It is possible to customize the output of the generated documentation with CSS
and/or by overriding templates.

## CSS classes

Our templates add [CSS](https://www.w3schools.com/Css/) classes to many HTML elements
to make it possible for users to customize the resulting look and feel.

To add CSS rules and style mkdocstrings' output,
put them in a CSS file in your docs folder, for example in `docs/css/mkdocstrings.css`,
and reference this file in [MkDocs' `extra_css` configuration option](https://www.mkdocs.org/user-guide/configuration/#extra_css):

```yaml title="mkdocs.yml"
extra_css:
- css/mkdocstrings.css
```

Example:

```css title="docs/css/mkdocstrings.css"
.doc-section-title {
  font-weight: bold;
}
```

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
- `doc-section-title`: on section titles (depend on the [selected style for section rendering][docstring_style])
- `doc-section-item`: on section items (depend on the [selected style for section rendering][docstring_style])
- `doc-md-description`: on `div`s containing HTML descriptions converted from Markdown docstrings
- `doc-symbol`: on `code` tags of symbol types
    - `doc-symbol-heading`: on symbol types in headings
    - `doc-symbol-toc`: on symbol types in the ToC
    - `doc-symbol-KIND`: specific to the kind of object (`module`, `class`, `function`, `method`, `attribute`)

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

## Symbol types

### Colors

You can customize the colors of the symbol types
(see [`show_symbol_type_heading`][show_symbol_type_heading] and [`show_symbol_type_toc`][show_symbol_type_toc])
by overriding the values of our CSS variables, for example:

```css title="docs/css/mkdocstrings.css"
[data-md-color-scheme="default"] {
  --doc-symbol-parameter-fg-color: #df50af;
  --doc-symbol-attribute-fg-color: #0079ff;
  --doc-symbol-function-fg-color: #00dfa2;
  --doc-symbol-method-fg-color: #00dfa2;
  --doc-symbol-class-fg-color: #d1b619;
  --doc-symbol-module-fg-color: #ff0060;

  --doc-symbol-parameter-bg-color: #df50af1a;
  --doc-symbol-attribute-bg-color: #0079ff1a;
  --doc-symbol-function-bg-color: #00dfa21a;
  --doc-symbol-method-bg-color: #00dfa21a;
  --doc-symbol-class-bg-color: #d1b6191a;
  --doc-symbol-module-bg-color: #ff00601a;
}

[data-md-color-scheme="slate"] {
  --doc-symbol-parameter-fg-color: #ffa8cc;
  --doc-symbol-attribute-fg-color: #963fb8;
  --doc-symbol-function-fg-color: #6d67e4;
  --doc-symbol-method-fg-color: #6d67e4;
  --doc-symbol-class-fg-color: #46c2cb;
  --doc-symbol-module-fg-color: #f2f7a1;

  --doc-symbol-parameter-bg-color: #ffa8cc1a;
  --doc-symbol-attribute-bg-color: #963fb81a;
  --doc-symbol-function-bg-color: #6d67e41a;
  --doc-symbol-method-bg-color: #6d67e41a;
  --doc-symbol-class-bg-color: #46c2cb1a;
  --doc-symbol-module-bg-color: #f2f7a11a;
}
```

The `[data-md-color-scheme="*"]` selectors work with the [Material for MkDocs] theme.
If you are using another theme, adapt the selectors to this theme
if it supports light and dark themes,
otherwise just override the variables at root level:

```css title="docs/css/mkdocstrings.css"
:root {
  --doc-symbol-parameter-fg-color: #df50af;
  --doc-symbol-attribute-fg-color: #0079ff;
  --doc-symbol-function-fg-color: #00dfa2;
  --doc-symbol-method-fg-color: #00dfa2;
  --doc-symbol-class-fg-color: #d1b619;
  --doc-symbol-module-fg-color: #ff0060;

  --doc-symbol-parameter-bg-color: #df50af1a;
  --doc-symbol-attribute-bg-color: #0079ff1a;
  --doc-symbol-function-bg-color: #00dfa21a;
  --doc-symbol-method-bg-color: #00dfa21a;
  --doc-symbol-class-bg-color: #d1b6191a;
  --doc-symbol-module-bg-color: #ff00601a;
}
```

/// admonition | Preview
    type: preview

<div id="preview-symbol-colors">
  <style>
    [data-md-color-scheme="default"] #preview-symbol-colors {
      --doc-symbol-parameter-fg-color: #df50af;
      --doc-symbol-attribute-fg-color: #0079ff;
      --doc-symbol-function-fg-color: #00dfa2;
      --doc-symbol-method-fg-color: #00dfa2;
      --doc-symbol-class-fg-color: #d1b619;
      --doc-symbol-module-fg-color: #ff0060;

      --doc-symbol-parameter-bg-color: #df50af1a;
      --doc-symbol-attribute-bg-color: #0079ff1a;
      --doc-symbol-function-bg-color: #00dfa21a;
      --doc-symbol-method-bg-color: #00dfa21a;
      --doc-symbol-class-bg-color: #d1b6191a;
      --doc-symbol-module-bg-color: #ff00601a;
    }

    [data-md-color-scheme="slate"] #preview-symbol-colors {
      --doc-symbol-parameter-fg-color: #ffa8cc;
      --doc-symbol-attribute-fg-color: #963fb8;
      --doc-symbol-function-fg-color: #6d67e4;
      --doc-symbol-method-fg-color: #6d67e4;
      --doc-symbol-class-fg-color: #46c2cb;
      --doc-symbol-module-fg-color: #f2f7a1;

      --doc-symbol-parameter-bg-color: #ffa8cc1a;
      --doc-symbol-attribute-bg-color: #963fb81a;
      --doc-symbol-function-bg-color: #6d67e41a;
      --doc-symbol-method-bg-color: #6d67e41a;
      --doc-symbol-class-bg-color: #46c2cb1a;
      --doc-symbol-module-bg-color: #f2f7a11a;
    }
  </style>
  <p>
    Try cycling through the themes to see the colors for each theme:
    <code class="doc-symbol doc-symbol-parameter"></code>
    <code class="doc-symbol doc-symbol-attribute"></code>
    <code class="doc-symbol doc-symbol-function"></code>
    <code class="doc-symbol doc-symbol-method"></code>
    <code class="doc-symbol doc-symbol-class"></code>
    <code class="doc-symbol doc-symbol-module"></code>
  </p>
</div>

///

### Names

You can also change the actual symbol names.
For example, to use single letters instead of truncated types:

```css title="docs/css/mkdocstrings.css"
.doc-symbol-parameter::after {
  content: "P";
}

.doc-symbol-attribute::after {
  content: "A";
}

.doc-symbol-function::after {
  content: "F";
}

.doc-symbol-method::after {
  content: "M";
}

.doc-symbol-class::after {
  content: "C";
}

.doc-symbol-module::after {
  content: "M";
}
```

/// admonition | Preview
    type: preview

<div id="preview-symbol-names">
  <style>
    #preview-symbol-names .doc-symbol-parameter::after {
      content: "P";
    }

    #preview-symbol-names .doc-symbol-attribute::after {
      content: "A";
    }

    #preview-symbol-names .doc-symbol-function::after {
      content: "F";
    }

    #preview-symbol-names .doc-symbol-method::after {
      content: "M";
    }

    #preview-symbol-names .doc-symbol-class::after {
      content: "C";
    }

    #preview-symbol-names .doc-symbol-module::after {
      content: "M";
    }
  </style>
  <ul>
    <li>Parameter: <code class="doc-symbol doc-symbol-parameter"></code></li>
    <li>Attribute: <code class="doc-symbol doc-symbol-attribute"></code></li>
    <li>Function: <code class="doc-symbol doc-symbol-function"></code></li>
    <li>Method: <code class="doc-symbol doc-symbol-method"></code></li>
    <li>Class: <code class="doc-symbol doc-symbol-class"></code></li>
    <li>Module: <code class="doc-symbol doc-symbol-module"></code></li>
  </ul>
</div>

///

## Templates

Templates are organized into the following tree:

```python exec="1" result="tree"
from pathlib import Path

basedir = "src/mkdocstrings_handlers/python/templates/material"
print("theme/")
for filepath in sorted(path for path in Path(basedir).rglob("*") if "_base" not in str(path) and path.suffix != ".css"):
    print(
        "    " * (len(filepath.relative_to(basedir).parent.parts) + 1)
        + filepath.name
        + ("/" if filepath.is_dir() else "")
    )
```

See them [in the repository](https://github.com/mkdocstrings/python/tree/main/src/mkdocstrings_handlers/python/templates/).
See the general *mkdocstrings* documentation to learn how to override them: https://mkdocstrings.github.io/theming/#templates.

Each one of these templates extends a base version in `theme/_base`. Example:

```html+jinja title="theme/class.html"
{% extends "_base/class.html" %}
```

Some of these templates define [Jinja blocks](https://jinja.palletsprojects.com/en/3.0.x/templates/#template-inheritance).
allowing to customize only *parts* of a template
without having to fully copy-paste it into your project:

```jinja title="templates/theme/class.html"
{% extends "_base/class.html" %}
{% block contents %}
  {{ block.super }}
  Additional contents
{% endblock contents %}
```

### Available blocks

Only the templates for the **Material for MkDocs** provide Jinja blocks.
The following tables show the block names, description,
and the Jinja context available in their scope.

#### `module.html`

- `heading`: The module heading.
- `labels`: The module labels.
- `contents`: The module contents: docstring and children blocks.
- `docstring`: The module docstring.
- `summary`: The automatic summaries of members.
- `children`: The module children.

Available context:

- `config`: The handler configuration (dictionary).
- `module`: The [Module][griffe.Module] instance.

#### `class.html`

- `heading`: The class heading.
- `labels`: The class labels.
- `signature`: The class signature.
- `contents`: The class contents: bases, docstring, source and children blocks.
- `bases`: The class bases.
- `docstring`: The class docstring.
- `summary`: The automatic summaries of members.
- `source`: The class source code.
- `children`: The class children.

Available context:

- `config`: The handler configuration (dictionary).
- `class`: The [Class][griffe.Class] instance.

#### `function.html`

- `heading`: The function heading.
- `labels`: The function labels.
- `signature`: The function signature.
- `contents`: The function contents: docstring and source blocks.
- `docstring`: The function docstring.
- `source`: The function source code.

Available context:

- `config`: The handler configuration (dictionary).
- `function`: The [Function][griffe.Function] instance.

#### `attribute.html`

- `heading`: The attribute heading.
- `labels`: The attribute labels.
- `signature`: The attribute signature.
- `contents`: The attribute contents: docstring block.
- `docstring`: The attribute docstring.

Available context:

- `config`: The handler configuration (dictionary).
- `attribute`: The [Attribute][griffe.Attribute] instance.

#### Docstring sections

In `docstring/attributes.html`,
`docstring/functions.html`,
`docstring/classes.html`,
`docstring/modules.html`,
`docstring/other_parameters.html`,
`docstring/parameters.html`,
`docstring/raises.html`,
`docstring/receives.html`,
`docstring/returns.html`,
`docstring/warns.html`,
and `docstring/yields.html`:

- `table_style`: The section as a table.
- `list_style`: The section as a list.
- `spacy_style`: The section as a Spacy table.

Available context:

- `section`: The [DocstringSection][griffe.DocstringSection] instance (see `DocstringSection*` subclasses).

### Syntax highlight in signatures

You can customize the colors in syntax highlighted signatures.
If you are using the [Material for MkDocs] theme,
here are some customization examples:

```css
/* Fancier color for operators such as * and |. */
.doc-signature .o {
  color: var(--md-code-hl-special-color);
}

/* Fancier color for constants such as None, True, and False. */
.doc-signature .kc {
  color: var(--md-code-hl-constant-color);
}

/* Fancier color for built-in types (only useful when cross-references are used). */
.doc-signature .n > a[href^="https://docs.python.org/"][href*="/functions.html#"],
.doc-signature .n > a[href^="https://docs.python.org/"][href*="/stdtypes.html#"] {
  color: var(--md-code-hl-constant-color);
}
```

For other themes, use their own CSS variables,
or use plain colors such as `violet` or `#2987f2`.

## Style recommendations

[](){#recommended-style-material}
### Material

Here are some CSS rules for the [Material for MkDocs] theme:

```css
--8<-- "docs/css/mkdocstrings.css"
```

[](){#recommended-style-readthedocs}
### ReadTheDocs

Here are some CSS rules for the built-in ReadTheDocs theme:

```css
/* Indentation. */
div.doc-contents:not(.first) {
  padding-left: 25px;
  border-left: .05rem solid rgba(200, 200, 200, 0.2);
}
```
