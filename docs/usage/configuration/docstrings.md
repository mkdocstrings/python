# Docstrings options

[](){#option-docstring_style}
## `docstring_style`

- **:octicons-package-24: Type [`str`][] :material-equal: `"google"`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

The docstring style to expect when parsing docstrings.

Possible values:

- `"google"`: see [Google style](../docstrings/google.md).
- `"numpy"`: see [Numpy style](../docstrings/numpy.md).
- `"sphinx"`: see [Sphinx style](../docstrings/sphinx.md).
- `None` (`null` or `~` in YAML): no style at all, parse as regular text.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          docstring_style: google
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      docstring_style: numpy
```

WARNING: **The style is applied to the specified object only, not its members.** Local `docstring_style` options (in `:::` instructions) will only be applied to the specified object, and not its members. Instead of changing the style when rendering, we strongly recommend to *set the right style as early as possible*, for example by using the [auto-style](https://mkdocstrings.github.io/griffe/reference/docstrings/#auto-style) (sponsors only), or with a custom Griffe extension


/// admonition | Preview
    type: preview

Every style gets rendered the same way.
Here are some docstring examples.

//// tab | Google
```python
def greet(name: str) -> str:
    """Greet someone.

    Parameters:
        name: The name of the person to greet.

    Returns:
        A greeting message.
    """
    return f"Hello {name}!"
```
////

//// tab | Numpy
```python
def greet(name: str) -> str:
    """Greet someone.

    Parameters
    ----------
    name
        The name of the person to greet.

    Returns
    -------
    A greeting message.
    """
    return f"Hello {name}!"
```
////

//// tab | Sphinx
```python
def greet(name: str) -> str:
    """Greet someone.

    :param name: The name of the person to greet.
    :return: A greeting message.
    """
    return f"Hello {name}!"
```
////
///

[](){#option-docstring_options}
## `docstring_options`

- **:octicons-package-24: Type [`dict`][] :material-equal: `{}`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

The options for the docstring parser.

- [Google-style options](https://mkdocstrings.github.io/griffe/docstrings/#parser-options){ .external }
- [Numpydoc-style options](https://mkdocstrings.github.io/griffe/docstrings/#parser-options_1){ .external }

The Sphinx style does not offer any option.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          docstring_options:
            ignore_init_summary: false
            trim_doctest_flags: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      docstring_options:
        ignore_init_summary: true
        trim_doctest_flags: false
```

```python
class PrintOK:
    """Class docstring."""

    def __init__(self):
        """Initialize the instance.

        Examples:
            >>> PrintOK()  # doctest: +NORMALIZE_WHITESPACE
            ok
        """
        print("ok")
```

/// admonition | Preview
    type: preview

//// tab | Ignore init summary, trim doctest flags
<h2><code>PrintOK</code></h2>
<p>Class docstring.</p>
<h3><code>__init__</code></h3>
<p>Examples:</p>

```pycon
>>> PrintOK()
ok
```
////

//// tab | Keep init summary and doctest flags
<h2><code>PrintOK</code></h2>
<p>Class docstring.</p>
<h3><code>__init__</code></h3>
<p>Initialize the instance.</p>
<p>Examples:</p>

```pycon
>>> PrintOK()  # doctest: +NORMALIZE_WHITESPACE
ok
```
////
///

[](){#option-docstring_section_style}
## `docstring_section_style`

- **:octicons-package-24: Type [`str`][] :material-equal: `"table"`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

The style used to render docstring sections.

A section is a block of text that has a special meaning in a docstring.
There are sections for documenting attributes of an object,
parameters of a function, exceptions raised by a function,
the return value of a function, etc.

Sections are parsed as structured data and can therefore be rendered
in different ways. Possible values:

- `"table"`: a simple table, usually with type, name and description columns
- `"list"`: a simple list, akin to what you get with the [ReadTheDocs Sphinx theme]{ .external }
- `"spacy"`: a poor implementation of the amazing tables in [Spacy's documentation]{ .external }

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          docstring_section_style: table
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      docstring_section_style: list
```

/// admonition | Preview
    type: preview

//// tab | Table
Tables work well when you have lots of items with short names, type annotations, descriptions, etc..
With longer strings, the columns risk getting squished horizontally.
In that case, the Spacy tables can help.

**Parameters:**

**Type**   | **Name**    | **Description**          | **Default**
---------- | ----------- | ------------------------ | -----------
[`int`][]  | `threshold` | Threshold for something. | *required*
[`bool`][] | `flag`      | Enable something.        | `False`

**Other Parameters:**

**Type**   | **Name**    | **Description**          | **Default**
---------- | ----------- | ------------------------ | -----------
<code><autoref identifier="list" optional>list</autoref>[<autoref identifier="int" optional>int</autoref> \| <autoref identifier="float" optional>float</autoref>]</code> | `gravity_forces` | Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. | *required*
<code><autoref identifier="VacuumType" optional>VacuumType</autoref> \| <autoref identifier="typing.Literal" optional>Literal</autoref>["regular"]</code> | `vacuum_type` | Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. | `VacuumType.PLASMA`
////

//// tab | List
Lists work well whatever the length of names, type annotations, descriptions, etc.

**Parameters:**

- `threshold` ([`int`][]) &mdash; Threshold for something.
- `flag` ([`bool`][]) &mdash; Enable something.

**Other Parameters:**

- `gravity_forces` (<code><autoref identifier="list" optional>list</autoref>[<autoref identifier="int" optional>int</autoref> \| <autoref identifier="float" optional>float</autoref>]</code>) &mdash; Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
- `vacuum_type` (<code><autoref identifier="VacuumType" optional>VacuumType</autoref> \| <autoref identifier="typing.Literal" optional>Literal</autoref>["regular"]</code>) &mdash; Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
////

//// tab | Spacy
Spacy tables work better than regular tables with longer names, type annotations, descriptions, etc.,
by reserving more horizontal space on the second column.

**Parameters:**

**Name**    | **Description**
----------- | ---------------
`threshold` | <span style="display: inline-block; min-width: 400px;">Threshold for something.</span><br>**TYPE:** [`int`][] <span style="float: right;"><b>DEFAULT:</b> <i>required</i></span>
`flag`      | <span style="display: inline-block; min-width: 400px;">Enable something.</span><br>**TYPE:** [`bool`][] <span style="float: right;"><b>DEFAULT:</b> <code>False</code></span>

**Other Parameters:**

**Name**    | **Description**
----------- | ---------------
`gravity_forces` | Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.<br>**TYPE:** <code><autoref identifier="list" optional>list</autoref>[<autoref identifier="int" optional>int</autoref> \| <autoref identifier="float" optional>float</autoref>]</code> <span style="float: right;"><b>DEFAULT:</b> <i>required</i></span>
`vacuum_type` | Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.<br>**TYPE:**<code><autoref identifier="VacuumType" optional>VacuumType</autoref> \| <autoref identifier="typing.Literal" optional>Literal</autoref>["regular"]</code> <span style="float: right;"><b>DEFAULT:</b> <code>VacuumType.PLASMA</code></span>
////
///

[](){#option-merge_init_into_class}
## `merge_init_into_class`

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to merge the `__init__` method into the class' signature and docstring.

By default, only the class name is rendered in headings.
When merging, the `__init__` method parameters are added after the class name,
like a signature, and the `__init__` method docstring is appended to the class' docstring.
This option is well used in combination with the `ignore_init_summary` [docstring option][docstring_options],
to discard the first line of the `__init__` docstring which is not often useful.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          docstring_options:
            ignore_init_summary: false
          merge_init_into_class: false
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      docstring_options:
        ignore_init_summary: true
      merge_init_into_class: true
```

```python
class Thing:
    """A class for things."""

    def __init__(self, value: int = 0):
        """Initialize a thing.

        Parameters:
            value: The thing's value.
        """
        self.value = value
```

/// admonition | Preview
    type: preview

//// tab | Merged, summary discarded
<h2><code>Thing(value=0)</code></h2>
<p>Class docstring.</p>
<p><b>Parameters:</b></p>

**Type**  | **Name** | **Description**    | **Default**
--------- | -------- | ------------------ | -----------
[`int`][] | `value`  | The thing's value. | `0`
////

//// tab | Unmerged, summary kept
<h2><code>Thing</code></h2>
<p>Class docstring.</p>
<h3><code>__init__(value=0)</code></h3>
<p>Initialize a thing.</p>
<p><b>Parameters:</b></p>

**Type**  | **Name** | **Description**    | **Default**
--------- | -------- | ------------------ | -----------
[`int`][] | `value`  | The thing's value. | `0`
////
///

[](){#option-relative_crossrefs}
## `relative_crossrefs`

[:octicons-heart-fill-24:{ .pulse } Sponsors only](../../insiders/index.md){ .insiders } &mdash;
[:octicons-tag-24: Insiders 1.9.0](../../insiders/changelog.md#1.9.0)

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to enable the relative-crossref syntax.

The relative-crossref syntax lets you reference the current object or its parent by prefixing a crossref identifier with dots. For example, to cross-reference the current object's `name` member, you can write `[link to name attribute][.name]`. The "current object" is the object containing the docstring being rendered.


```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          relative_crossrefs: false
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      relative_crossrefs: true
```

/// admonition | Examples
    type: preview

```python title="pkg/module.py"
"""Summary.

- Link to [`module`][.].
- Link to [`module_attribute`][.module_attribute].
- Link to [`Class`][.Class].
- Link to [`class_attribute`][.Class.class_attribute].
- Link to [`instance_attribute`][.Class.instance_attribute].
- Link to [`method`][.Class.method].
"""

module_attribute = 0
"""Summary.

- Link to [`module`][..].
- Link to [`module_attribute`][.].
- Link to [`Class`][..Class].
- Link to [`class_attribute`][..Class.class_attribute].
- Link to [`instance_attribute`][..Class.instance_attribute].
- Link to [`method`][..Class.method].
"""

class Class:
    """Summary.

    - Link to [`module`][..].
    - Link to [`module_attribute`][..module_attribute].
    - Link to [`Class`][.].
    - Link to [`class_attribute`][.class_attribute].
    - Link to [`instance_attribute`][.instance_attribute].
    - Link to [`method`][.method].
    """

    class_attribute = 0
    """Summary.

    - Link to [`module`][...].
    - Link to [`module_attribute`][...module_attribute].
    - Link to [`Class`][..].
    - Link to [`class_attribute`][.].
    - Link to [`instance_attribute`][..instance_attribute].
    - Link to [`method`][..method].
    """

    def __init__(self):
        """Summary.

        - Link to [`module`][...].
        - Link to [`module_attribute`][...module_attribute].
        - Link to [`Class`][..].
        - Link to [`class_attribute`][..class_attribute].
        - Link to [`instance_attribute`][..instance_attribute].
        - Link to [`method`][..method].
        """
        self.instance_attribute = 0
        """Summary.

        - Link to [`module`][...].
        - Link to [`module_attribute`][...module_attribute].
        - Link to [`Class`][..].
        - Link to [`class_attribute`][..class_attribute].
        - Link to [`instance_attribute`][.].
        - Link to [`method`][..method].
        """

    def method(self):
        """Summary.

        - Link to [`module`][...].
        - Link to [`module_attribute`][...module_attribute].
        - Link to [`Class`][..].
        - Link to [`class_attribute`][..class_attribute].
        - Link to [`instance_attribute`][..instance_attribute].
        - Link to [`method`][.].
        """
```

///

INFO: **There is an alternative, third-party Python handler that handles relative references: [mkdocstrings-python-xref](https://github.com/analog-garage/mkdocstrings-python-xref).**

[](){#option-scoped_crossrefs}
## `scoped_crossrefs`

[:octicons-heart-fill-24:{ .pulse } Sponsors only](../../insiders/index.md){ .insiders } &mdash;
[:octicons-tag-24: Insiders 1.9.0](../../insiders/changelog.md#1.9.0)

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to enable scoped cross-references.

With scoped cross-references, you can write identifiers as if you wanted to access them from the current object's scope. The scoping rules do not exactly match Python's: you can reference members and siblings too, without prefixing with `self.` or `cls.`.

The following order is applied when resolving a name in a given scope:

1. member of the current object
2. parent class
3. repeat 1-2 within parent's scope

In practice, it means that the name is first looked up in members, then it is compared against the parent name (only if it's a class), then it is looked up in siblings. It continues climbing up the object tree until there's no parent, in which case it raises a name resolution error.

Cross-referencing an imported object will directly link to this object if the objects inventory of the project it comes from was [loaded][inventories]. You won't be able to cross-reference it within your own documentation with scoped references, if you happen to be rendering this external object too. In that case, you can use an absolute reference or a [relative][relative_crossrefs] one instead.

Another limitation is that you won't be able to reference an external package if its name can be resolved in the current object's scope.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          scoped_crossrefs: false
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      scoped_crossrefs: true
```

/// admonition | Examples
    type: preview

```python title="pkg/module.py"
"""Summary.

- Link to [`module_attribute`][module_attribute].
- Link to [`Class`][Class].
- Link to [`class_attribute`][Class.class_attribute].
- Link to [`instance_attribute`][Class.instance_attribute].
- Link to [`method`][Class.method].
"""

module_attribute = 0
"""Summary.

- Link to [`Class`][Class].
- Link to [`class_attribute`][Class.class_attribute].
- Link to [`instance_attribute`][Class.instance_attribute].
- Link to [`method`][Class.method].
"""

class Class:
    """Summary.

    - Link to [`module_attribute`][module_attribute].
    - Link to [`class_attribute`][class_attribute].
    - Link to [`instance_attribute`][instance_attribute].
    - Link to [`method`][method].
    """

    class_attribute = 0
    """Summary.

    - Link to [`module_attribute`][module_attribute].
    - Link to [`Class`][Class].
    - Link to [`instance_attribute`][instance_attribute].
    - Link to [`method`][method].
    """

    def __init__(self):
        """Summary.

        - Link to [`module_attribute`][module_attribute].
        - Link to [`Class`][Class].
        - Link to [`class_attribute`][class_attribute].
        - Link to [`instance_attribute`][instance_attribute].
        - Link to [`method`][method].
        """
        self.instance_attribute = 0
        """Summary.

        - Link to [`module_attribute`][module_attribute].
        - Link to [`Class`][Class].
        - Link to [`class_attribute`][class_attribute].
        - Link to [`method`][method].
        """

    def method(self):
        """Summary.

        - Link to [`module_attribute`][module_attribute].
        - Link to [`Class`][Class].
        - Link to [`class_attribute`][class_attribute].
        - Link to [`instance_attribute`][instance_attribute].
        """
```

///

[](){#option-show_if_no_docstring}
## `show_if_no_docstring`

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Show the object heading even if it has no docstring or children with docstrings.

Without an explicit list of [`members`][], members are selected based on [`filters`][],
and then filtered again to keep only those with docstrings. Checking if a member has a docstring
is done recursively: if at least one of its direct or indirect members (lower in the tree)
has a docstring, the member is rendered. If the member does not have a docstring,
and none of its members have a docstring, it is excluded.

With this option you can tell the Python handler to skip the docstring check.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_if_no_docstring: false
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_if_no_docstring: true
```

```python
def function_without_docstring():
    ...


def function_with_docstring():
    """Hello."""


class ClassWithoutDocstring:
    def method_without_docstring(self):
        ...

    def method_with_docstring(self):
        """Hello."""
```

/// admonition | Preview
    type: preview

//// tab | Show
<h2><code>function_without_docstring</code></h2>
<h2><code>function_with_docstring</code></h2>
<p>Hello.</p>
<h2><code>ClassWithoutDocstring</code></h2>
<h3><code>method_without_docstring</code></h3>
<h3><code>method_with_docstring</code></h3>
<p>Hello.</p>
////

//// tab | Don't show
<h2><code>function_with_docstring</code></h2>
<p>Hello.</p>
<h2><code>ClassWithoutDocstring</code></h2>
<h3><code>method_with_docstring</code></h3>
<p>Hello.</p>
////
///

[](){#option-show_docstring_attributes}
## `show_docstring_attributes`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to render the "Attributes" sections of docstrings.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_docstring_attributes: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_docstring_attributes: false
```

```python
class Class:
    """Summary.

    Attributes:
        attr: Some attribute.
    """

    attr: int = 1
```

/// admonition | Preview
    type: preview

//// tab | With attributes
<h2><code>Class</code></h2>
<p>Summary.</p>
<p><b>Attributes:</b></p>

**Type**  | **Name** | **Description**
--------- | -------- | ---------------
[`int`][] | `attr`   | Some attribute.
////

//// tab | Without attributes
<h2><code>Class</code></h2>
<p>Summary.</p>
////
///

[](){#option-show_docstring_functions}
## `show_docstring_functions`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to render the "Functions" or "Methods" sections of docstrings.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_docstring_functions: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_docstring_functions: false
```

```python
"""Summary.

Functions:
    foo: Some function.
"""


def foo():
    ...


class Class:
    """Summary.

    Methods:
        bar: Some method.
    """

    def bar(self):
        ...
```

/// admonition | Preview
    type: preview

//// tab | With functions
<h2>module</h2>
<p>Summary.</p>
<p><b>Functions:</b></p>

**Name** | **Description**
-------- | ---------------
`foo`    | Some function.

<h3><code>Class</code></h3>
<p>Summary.</p>
<p><b>Methods:</b></p>

**Name** | **Description**
-------- | ---------------
`bar`    | Some method.
////

//// tab | Without functions
<h2>module</h2>
<p>Summary.</p>
<h3><code>Class</code></h3>
<p>Summary.</p>
////
///

[](){#option-show_docstring_classes}
## `show_docstring_classes`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to render the "Classes" sections of docstrings.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_docstring_classes: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_docstring_classes: false
```

```python
"""Summary.

Classes:
    Class: Some class.
"""


class Class:
    """Summary."""
```

/// admonition | Preview
    type: preview

//// tab | With classes
<h2>module</h2>
<p>Summary.</p>
<p><b>Classes:</b></p>

**Name** | **Description**
-------- | ---------------
`Class`  | Some class.

<h3><code>Class</code></h3>
<p>Summary.</p>
////

//// tab | Without classes
<h2>module</h2>
<p>Summary.</p>
<h3><code>Class</code></h3>
<p>Summary.</p>
////
///

[](){#option-show_docstring_modules}
## `show_docstring_modules`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to render the "Modules" sections of docstrings.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_docstring_modules: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_docstring_modules: false
```

```tree
module/
    __init__.py
    submodule.py
```

```python title="module/__init__.py"
"""Summary.

Modules:
    submodule: Some module.
"""
```

/// admonition | Preview
    type: preview

//// tab | With modules
<h2>module</h2>
<p>Summary.</p>
<p><b>Modules:</b></p>

**Name**    | **Description**
----------- | ---------------
`submodule` | Some module.

////

//// tab | Without modules
<h2>module</h2>
<p>Summary.</p>
////
///

[](){#option-show_docstring_description}
## `show_docstring_description`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to render the textual blocks (including admonitions) of docstrings.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_docstring_description: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_docstring_description: false
```

```python
class Class:
    """Summary.

    Long description.

    Warning: Deprecated
        Stop using this class.

    Attributes:
        attr: Some attribute.
    """

    attr: int = 1
```

/// admonition | Preview
    type: preview

//// tab | With description blocks
<h2><code>Class</code></h2>
<p>Summary.</p>
<p>Long description.</p>
<details class="warning" open><summary>Deprecated</summary><p>Stop using this class.</p></details>
<p><b>Attributes:</b></p>

**Type**  | **Name** | **Description**
--------- | -------- | ---------------
[`int`][] | `attr`   | Some attribute.
////

//// tab | Without description blocks
<h2><code>Class</code></h2>
<p><b>Attributes:</b></p>

**Type**  | **Name** | **Description**
--------- | -------- | ---------------
[`int`][] | `attr`   | Some attribute.
////
///

[](){#option-show_docstring_examples}
## `show_docstring_examples`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to render the "Examples" section of docstrings.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_docstring_examples: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_docstring_examples: false
```

```python
def print_hello():
    """Print hello.

    Examples:
        >>> print("hello")
        hello
    """
    print("hello")
```

/// admonition | Preview
    type: preview

//// tab | With examples
<h2><code>print_hello</code></h2>
<p>Print hello.</p>
<p><b>Examples:</b></p>

```pycon
>>> print("hello")
hello
```
////

//// tab | Without examples
<h2><code>print_hello</code></h2>
<p>Print hello.</p>
////
///

[](){#option-show_docstring_other_parameters}
## `show_docstring_other_parameters`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to render the "Other Parameters" section of docstrings.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_docstring_other_parameters: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_docstring_other_parameters: false
```

```python
def do_something(**kwargs):
    """Do something.

    Other parameters:
        whatever (int): Some integer.
    """
```

/// admonition | Preview
    type: preview

//// tab | With other parameters
<h2><code>do_something</code></h2>
<p>Do something.</p>
<p><b>Other parameters:</b></p>

**Type**  | **Name**   | **Description**
--------- | ---------- | ---------------
[`int`][] | `whatever` | Some integer.
////

//// tab | Without other parameters
<h2><code>do_something</code></h2>
<p>Do something.</p>
////
///

[](){#option-show_docstring_parameters}
## `show_docstring_parameters`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to render the "Parameters" section of docstrings.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_docstring_parameters: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_docstring_parameters: false
```

```python
def do_something(whatever: int = 0):
    """Do something.

    Parameters:
        whatever: Some integer.
    """
```

/// admonition | Preview
    type: preview

//// tab | With parameters
<h2><code>do_something</code></h2>
<p>Do something.</p>
<p><b>Parameters:</b></p>

**Type**  | **Name**   | **Description** | **Default**
--------- | ---------- | --------------- | -----------
[`int`][] | `whatever` | Some integer.   | `0`
////

//// tab | Without parameters
<h2><code>do_something</code></h2>
<p>Do something.</p>
////
///

[](){#option-show_docstring_raises}
## `show_docstring_raises`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to render the "Raises" section of docstrings.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_docstring_raises: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_docstring_raises: false
```

```python
def raise_runtime_error():
    """Raise a runtime error.

    Raises:
        RuntimeError: Not good.
    """
    raise RuntimeError
```

/// admonition | Preview
    type: preview

//// tab | With exceptions
<h2><code>raise_runtime_error</code></h2>
<p>Raise a runtime error.</p>
<p><b>Raises:</b></p>

**Type**           | **Description**
------------------ | ---------------
[`RuntimeError`][] | Not good.
////

//// tab | Without exceptions
<h2><code>raise_runtime_error</code></h2>
<p>Raise a runtime error.</p>
////
///

[](){#option-show_docstring_receives}
## `show_docstring_receives`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to render the "Receives" section of docstrings.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_docstring_receives: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_docstring_receives: false
```

```python
def iter_skip(
    iterable: Iterable[T],
    initial_skip: int = 0,
) -> Generator[T, int, None]:
    """Iterate and skip elements.

    Receives:
        skip: Number of elements to skip.
    """
    skip = initial_skip
    for element in iterable:
        if skip or 0 > 0:
            skip -= 1
        else:
            skip = yield element
```

/// admonition | Preview
    type: preview

//// tab | With received values
<h2><code>iter_skip</code></h2>
<p>Iterate and skip elements.</p>
<p><b>Receives:</b></p>

**Type**  | **Description**
--------- | ---------------
[`int`][] | Number of elements to skip.
////

//// tab | Without received values
<h2><code>iter_skip</code></h2>
<p>Iterate and skip elements.</p>
////
///

[](){#option-show_docstring_returns}
## `show_docstring_returns`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to render the "Returns" section of docstrings.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_docstring_returns: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_docstring_returns: false
```

```python
def rand() -> int:
    """Return a random number.

    Returns:
        A random number.
    """
    return random.randint(0, 1000)
```

/// admonition | Preview
    type: preview

//// tab | With return value
<h2><code>rand</code></h2>
<p>Return a random number.</p>
<p><b>Returns:</b></p>

**Type**  | **Description**
--------- | ---------------
[`int`][] | A random number.
////

//// tab | Without return value
<h2><code>rand</code></h2>
<p>Return a random number.</p>
////
///

[](){#option-show_docstring_warns}
## `show_docstring_warns`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to render the "Warns" section of docstrings.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_docstring_warns: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_docstring_warns: false
```

```python
def warn():
    """Warn user.

    Warns:
        UserWarning: When this is inappropriate.
    """
    warnings.warn(UserWarning("This is inappropriate"))
```

/// admonition | Preview
    type: preview

//// tab | With warnings
<h2><code>warn</code></h2>
<p>Warn user.</p>
<p><b>Warns:</b></p>

**Type**          | **Description**
----------------- | ---------------
[`UserWarning`][] | When this is inappropriate.
////

//// tab | Without warnings
<h2><code>warn</code></h2>
<p>Warn user.</p>
////
///

[](){#option-show_docstring_yields}
## `show_docstring_yields`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to render the "Yields" section of docstrings.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_docstring_yields: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      show_docstring_yields: false
```

```python
def iter_skip(
    iterable: Iterable[T],
    initial_skip: int = 0,
) -> Generator[T, int, None]:
    """Iterate and skip elements.

    Yields:
        Elements of the iterable.
    """
    skip = initial_skip
    for element in iterable:
        if skip or 0 > 0:
            skip -= 1
        else:
            skip = yield element
```

/// admonition | Preview
    type: preview

//// tab | With yielded values
<h2><code>iter_skip</code></h2>
<p>Iterate and skip elements.</p>
<p><b>Yields:</b></p>

**Type**  | **Description**
--------- | ---------------
`T`       | Elements of the iterable.
////

//// tab | Without yielded values
<h2><code>iter_skip</code></h2>
<p>Iterate and skip elements.</p>
////
///
