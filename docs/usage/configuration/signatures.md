# Signatures options

[](){#option-annotations_path}
## `annotations_path`

- **:octicons-package-24: Type [`str`][] :material-equal: `"brief"`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

The verbosity for annotations path.

Possible values:

- `brief` (recommended): render only the last component of each type path, not their full paths.
    For example, it will render `Sequence[Path]` and not `typing.Sequence[pathlib.Path]`.
    Brief annotations will cross-reference the right object anyway,
    and show the full path in a tooltip when hovering them.
- `source`: render annotations as written in the source. For example if you imported `typing` as `t`,
    it will render `typing.Sequence` as `t.Sequence`. Each part will cross-reference the relevant object:
    `t` will link to the `typing` module and `Sequence` will link to the `Sequence` type.
- `full`: render annotations with their full path (the opposite of brief).
    For example if you import `Sequence` and `Pattern` from `typing` and annoate something using
    `Sequence[Pattern]`, it will render as `typing.Sequence[typing.Pattern]`, with each part
    cross-referencing the corresponding object.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          annotations_path: brief
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      annotations_path: source
```


/// admonition | Preview
    type: preview

//// tab | Brief annotations
```python
import markdown
import markupsafe


def convert(text: str, md: markdown.Markdown) -> markupsafe.Markup:
    """Convert text to Markdown.

    Parameters:
        text: The text to convert.
        md: A Markdown instance.

    Returns:
        Converted markup.
    """
    return markupsafe.Markup(md.convert(text))
```

<h2><code>convert(text, md)</code></h2>
<p>Convert text to Markdown.</p>
<p><b>Parameters:</b></p>

**Type**   | **Description**          | **Default**
---------- | ------------------------ | -----------
[`str`][]  | The text to convert.     | *required*
[`Markdown`](#ref-to-markdown){ .external title="markdown.Markdown" } | A Markdown instance. | *required*

<p><b>Returns:</b></p>

**Type**   | **Name**    | **Description**
---------- | ----------- | ---------------
[`Markup`](#ref-to-markup){ .external title="markupsafe.Markup" } | `text` | Converted markup.
////

//// tab | Source annotations
```python
import markdown
from markupsafe import Markup


def convert(text: str, md: markdown.Markdown) -> Markup:
    """Convert text to Markdown.

    Parameters:
        text: The text to convert.
        md: A Markdown instance.

    Returns:
        Converted markup.
    """
    return Markup(md.convert(text))
```

<h2><code>convert(text, md)</code></h2>
<p>Convert text to Markdown.</p>
<p><b>Parameters:</b></p>

**Type**   | **Description**          | **Default**
---------- | ------------------------ | -----------
[`str`][]  | The text to convert.     | *required*
<code><a class="external" href="#ref-to-markdown">markdown</a>.<a class="external" href="#ref-to-Markdown" title="markdown.Markdown">Markdown</a></code> | A Markdown instance. | *required*

<p><b>Returns:</b></p>

**Type**   | **Name**    | **Description**
---------- | ----------- | ---------------
[`Markup`](#ref-to-markup){ .external title="markupsafe.Markup" } | `text` | Converted markup.
////

//// tab | Full annotations
```python
from markdown import Markdown
from markupsafe import Markup


def convert(text: str, md: Markdown) -> Markup:
    """Convert text to Markdown.

    Parameters:
        text: The text to convert.
        md: A Markdown instance.

    Returns:
        Converted markup.
    """
    return Markup(md.convert(text))
```

<h2><code>convert(text, md)</code></h2>
<p>Convert text to Markdown.</p>
<p><b>Parameters:</b></p>

**Type**   | **Description**          | **Default**
---------- | ------------------------ | -----------
[`str`][]  | The text to convert.     | *required*
<code><a class="external" href="#ref-to-markdown">markdown</a>.<a class="external" href="#ref-to-Markdown" title="markdown.Markdown">Markdown</a></code> | A Markdown instance. | *required*

<p><b>Returns:</b></p>

**Type**   | **Name**    | **Description**
---------- | ----------- | ---------------
<code><a class="external" href="#ref-to-markupsafe">markupsafe</a>.<a class="external" href="#ref-to-Markup" title="markupsafe.Markup">Markup</a></code> | `text` | Converted markup.
////
///

[](){#option-line_length}
## `line_length`

- **:octicons-package-24: Type [`int`][] :material-equal: `60`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Maximum line length when formatting code/signatures.

When separating signatures from headings with the [`separate_signature`][] option,
the Python handler will try to format the signatures using a formatter and
the specified line length.

The handler will automatically try to format using :

1. [Black]
2. [Ruff]

If a formatter is not found, the handler issues an INFO log once.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          separate_signature: true
          line_length: 60
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      separate_signature: true
      line_length: 80
```

/// admonition | Preview
    type: preview

//// tab | Line length 60
<h2>long_function_name</h2>
<pre><code>long_function_name(
    long_parameter_1="hello",
    long_parameter_2="world",
)</code></pre>
////

//// tab | Line length 80
<h2>long_function_name</h2>
<pre><code>long_function_name(long_parameter_1="hello", long_parameter_2="world")</code></pre>
////
///

[](){#option-modernize_annotations}
## `modernize_annotations`

[:octicons-heart-fill-24:{ .pulse } Sponsors only](../../insiders/index.md){ .insiders } &mdash;
[:octicons-tag-24: Insiders 1.8.0](../../insiders/changelog.md#1.8.0) &mdash;
**This feature also requires
[Griffe Insiders](https://mkdocstrings.github.io/griffe/insiders/)
to be installed.**

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (contained in [`class.html`][class template]) -->

Modernize annotations with latest features and PEPs of the Python language.

The Python language keeps evolving, and often library developers
must continue to support a few minor versions of Python.
Therefore they cannot use some features that were introduced
in the latest versions.

Yet this doesn't mean they can't enjoy latest features in their docs:
Griffe allows to "modernize" expressions, for example
by replacing `typing.Union` with [PEP 604][pep-604] type unions `|`.
Thanks to this, mkdocstrings' Python handler
can automatically transform type annotations into their modern equivalent.
This improves consistency in your docs, and shows users
how to use your code with the latest features of the language.

[pep-604]: https://peps.python.org/pep-0604/

Modernizations applied:

- `typing.Dict[A, B]` becomes `dict[A, B]`
- `typing.List[A]` becomes `list[A]`
- `typing.Set[A]` becomes `set[A]`
- `typing.Tuple[A]` becomes `tuple[A]`
- `typing.Union[A, B]` becomes `A | B`
- `typing.Optional[A]` becomes `A | None`

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          modernize_annotations: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.object
    options:
      modernize_annotations: false
```

/// admonition | Preview
    type: preview

```python
--8<-- "docs/snippets/package/modern.py"
```

//// tab | Unchanged annotations

```md exec="on"
::: package.modern.example
    options:
      modernize_annotations: false
      show_symbol_type_heading: false
      show_labels: false
```

////

//// tab | Modernized annotations

```md exec="on"
::: package.modern.example
    options:
      modernize_annotations: true
      show_symbol_type_heading: false
      show_labels: false
```

////

///

[](){#option-show_signature}
## `show_signature`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Show methods and functions signatures.

Without it, just the function/method name is rendered.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_signature: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_signature: false
```

/// admonition | Preview
    type: preview

//// tab | With signature
<h2><code>function(param1, param2=None)</code></h2>
<p>Function docstring.</p>
////

//// tab | Without signature
<h2><code>function</code></h2>
<p>Function docstring.</p>
////
///

[](){#option-show_signature_annotations}
## `show_signature_annotations`

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Show the type annotations in methods and functions signatures.

Since the heading can become quite long when annotations are rendered,
it is usually best to [separate the signature][separate_signature] from the heading.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          separate_signature: true
          show_signature_annotations: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      separate_signature: true
      show_signature_annotations: false
```

/// admonition | Preview
    type: preview

//// tab | With signature annotations
<h2>function</h2>

```python
function(
    param1: list[int | float],
    param2: bool | None = None,
) -> float
```

<p>Function docstring.</p>
////

//// tab | Without signature annotations
<h2>function</h2>

```python
function(param1, param2=None)
```

<p>Function docstring.</p>
////
///

[](){#option-separate_signature}
## `separate_signature`

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to put the whole signature in a code block below the heading.

When separating signatures from headings,
the Python handler will try to format the signatures using a formatter and
the specified [line length][line_length].

The handler will automatically try to format using :

1. [Black]
2. [Ruff]

If a formatter is not found, the handler issues an INFO log once.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          separate_signature: false
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      separate_signature: true
```

/// admonition | Preview
    type: preview

//// tab | With separate signature
<h2>function</h2>

```python
function(param1, param2=None)
```

<p>Function docstring.</p>
////

//// tab | Without separate signature
<h2><code>function(param1, param2=None)</code></h2>
<p>Function docstring.</p>
////
///

[](){#option-show_overloads}
## `show_overloads`

Whether to render function / method overloads.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_overloads: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_overloads: false
```

/// admonition | Preview
    type: preview
//// tab | With overloads
<h2>function</h2>


```python
@overload
function(param1: int): ...

@overload
function(param1: str): ...

function(param1: str | int)
```
Function docstring.

////
//// tab | Without overloads
<h2>function</h2>

```python
function(param1: str | int)
```
Function docstring.

////
///

[](){#option-signature_crossrefs}
## `signature_crossrefs`

[:octicons-tag-24: Insiders 1.0.0](../../insiders/changelog.md#1.0.0)

Whether to render cross-references for type annotations in signatures.

When signatures are separated from headings with the [`separate_signature`][] option
and type annotations are shown with the [`show_signature_annotations`][] option,
this option will render a cross-reference (link) for each type annotation in the signature.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          separate_signature: true
          show_signature_annotations: true
          signature_crossrefs: false
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      separate_signature: true
      show_signature_annotations: true
      signature_crossrefs: true
```

/// admonition | Preview
    type: preview

//// tab | With signature cross-references
<h2>do_format_code</h2>
<div class="highlight"><pre><code><span class="n">do_format_code</span><span class="p">(</span><span class="n">code</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n">line_length</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>
<p>Function docstring.</p>
////

//// tab | Without signature cross-references
<h2>do_format_code</h2>
<div class="highlight"><pre><code><span class="n">do_format_code</span><span class="p">(</span><span class="n">code</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">line_length</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span>
</code></pre></div>
<p>Function docstring.</p>
////
///

[](){#option-unwrap_annotated}
## `unwrap_annotated`

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to unwrap [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated){ .external }
types to show only the type without the annotations.

For example, unwrapping `Annotated[int, Gt(10)]` will render `int`.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          unwrap_annotated: false
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      unwrap_annotated: true
```
