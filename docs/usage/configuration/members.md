# Members options

## `members`

- **:octicons-package-24: Type <code><span data-autorefs-optional="list">list</span>[<span data-autorefs-optional="str">str</span>] |
    <span data-autorefs-optional="bool">bool</span> | None</code>  :material-equal: `None`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

An explicit list of members to render.

Only members declared in this list will be rendered.
A member without a docstring will still be rendered,
even if [`show_if_no_docstring`][] is set to false.

The members will be rendered in the specified order,
regardless of the value of [`members_order`][].

Passing a falsy value (`no`, `false` in YAML) or an empty list (`[]`)
will tell the Python handler not to render any member.
Passing a truthy value (`yes`, `true` in YAML)
will tell the Python handler to render every member.

Any given value, except for an explicit `None` (`null` in YAML)
will tell the handler to ignore [`filters`][] for the object's members.
Filters will still be applied to the next layers of members (grand-children).

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          members:
          - hello  # (1)
```

1. :warning: Most of the time it won't make sense to use this option at the global level.

```md title="or in docs/some_page.md (local configuration)"
::: package.module
    options:
      members:
      - ThisClass
      - this_function
```

```python title="package/module.py"
"""Module docstring."""

def this_function():
    """Function docstring."""

class ThisClass:
    """Class docstring."""
    def method(self):
        """Method docstring."""

this_attribute = 0
"""Attribute docstring."""
```

/// admonition | Preview
    type: preview

//// tab | With `members: true`
<p>Module docstring.</p>
<h2><code>this_function</code></h2>
<p>Function docstring.</p>
<h2><code>ThisClass</code></h2>
<p>Class docstring.</p>
<h3><code>method</code></h3>
<p>Method docstring.</p>
<h2><code>this_attribute</code></h2>
<p>Attribute docstring.</p>
////

//// tab | With `members: false` or `members: []`
<p>Module docstring.</p>
////

//// tab | With `members: [ThisClass]`
<p>Module docstring.</p>
<h2><code>ThisClass</code></h2>
<p>Class docstring.</p>
<h3><code>method</code></h3>
<p>Method docstring.</p>
////
///

INFO: **The default behavior (with unspecified `members` or `members: null`) is to use [`filters`][].**

## `members_order`

- **:octicons-package-24: Type [`str`][] :material-equal: `"alphabetical"`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

The members ordering to use. Possible values:

- `alphabetical`: order by the members names.
- `source`: order members as they appear in the source file.

The order applies for all members, recursively.
The order will be ignored for members that are explicitely sorted using the [`members`][] option.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          members_order: alphabetical
```

```md title="or in docs/some_page.md (local configuration)"
::: package.module
    options:
      members_order: source
```

```python title="package/module.py"
"""Module docstring."""

def function_b():
    """Function a."""

def function_a():
    """Function b."""

def function_c():
    """Function c."""
```

/// admonition | Preview
    type: preview

//// tab | With alphabetical order
<p>Module docstring.</p>
<h2><code>function_a</code></h2>
<p>Function a.</p>
<h2><code>function_b</code></h2>
<p>Function b.</p>
<h2><code>function_c</code></h2>
<p>Function c.</p>
////

//// tab | With source order
<p>Module docstring.</p>
<h2><code>function_b</code></h2>
<p>Function b.</p>
<h2><code>function_a</code></h2>
<p>Function a.</p>
<h2><code>function_c</code></h2>
<p>Function c.</p>
////
///

## `filters`

- **:octicons-package-24: Type <code><span data-autorefs-optional="list">list</span>[<span data-autorefs-optional="str">str</span>] | None</code>  :material-equal: `["!^_[^_]"]`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

A list of filters applied to filter objects based on their name.

Filters are regular expressions. These regular expressions are evaluated by Python
and so must match the syntax supported by the [`re`][] module.
A filter starting with `!` (negative filter) will exclude matching objects instead of including them.

The default value (`["!^_[^_]"]`) means: *render every object, except those
starting with one underscore, unless they start with two underscores*.
It means that an object whose name is `hello`, `__hello`, or `__hello__`
will be rendered, but not one whose name is `_hello`.

Each filter takes precedence over the previous one. This allows for fine-grain
selection of objects by adding more specific filters. For example, you can
start by unselecting objects that start with `_`, and add a second filter
that re-select objects that start with `__`. The default filters can
therefore be rewritten like this:

```yaml
filters:
- "!^_"
- "^__"
```

If there are no negative filters, the handler considers that everything
is **unselected** first, and then selects things based on your positive filters.
If there is at least one negative filter, the handler considers that everything
is **selected** first, and then re-selects/unselects things based on your other filters.
In short, `filters: ["a"]` means *"keep ***nothing*** except names containing `a`"*, while
`filters: ["!a"]` means *"keep ***everything*** except names containing `a`"*.

An empty list of filters tells the Python handler to render every object.
The [`members`][] option takes precedence over filters
(filters will still be applied recursively to lower members in the hierarchy).

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          filters:
          - "!^_"
```

```md title="or in docs/some_page.md (local configuration)"
::: package.module
    options:
      filters: []
```

```python title="package/module.py"
def hello(): ...
def _world(): ...
```

/// admonition | Preview
    type: preview

//// tab | With `filters: []`
<p>Module docstring.</p>
<h2><code>hello</code></h2>
<p>Function docstring.</p>
<h2><code>_world</code></h2>
<p>Function docstring.</p>
////

//// tab | With `filters: ["hello"]`
<p>Module docstring.</p>
<h2><code>hello</code></h2>
<p>Function docstring.</p>
////

//// tab | With `filters: ["!hello"]`
<p>Module docstring.</p>
<h2><code>_world</code></h2>
<p>Function docstring.</p>
////
///

/// admonition | Common filters
    type: tip

Here are some common filters that you might to want to use.

- `["!^_"]`: exclude all private/protected/special objects
- `["!^_", "^__init__$"]`: same as above, but keep `__init__` methods
- `["!^_[^_]"]`: exclude all private/protected objects, keep special ones (default filters)
///

## `group_by_category`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Group the object members by categories: attributes, classes, functions, and modules.

Members within a same category will be ordered according to the [`members_order`][] option.
You can use the [`show_category_heading`][] option to also render a heading for each category.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          group_by_category: true
```

```md title="or in docs/some_page.md (local configuration)"
::: package.module
    options:
      group_by_category: false
```

```python title="package/module.py"
def function_a(): ...
class ClassB: ...
attribute_C = 0
def function_d(): ...
```

/// admonition | Preview
    type: preview

//// tab | With category grouping
<p>Module docstring.</p>
<h2><code>attribute_c</code></h2>
<p>Attribute docstring.</p>
<h2><code>ClassB</code></h2>
<p>Class docstring.</p>
<h2><code>function_a</code></h2>
<p>Function docstring.</p>
<h2><code>function_d</code></h2>
<p>Function docstring.</p>
////

//// tab | Without category grouping
<p>Module docstring.</p>
<h2><code>function_a</code></h2>
<p>Function docstring.</p>
<h2><code>ClassB</code></h2>
<p>Class docstring.</p>
<h2><code>attribute_c</code></h2>
<p>Attribute docstring.</p>
<h2><code>function_d</code></h2>
<p>Function docstring.</p>
////
///

## `show_submodules`

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

When rendering a module, show its submodules recursively.

This is false by default, because most of the time we render only one module per page,
and when rendering a package (a tree of modules and their members) on a single page,
we quickly run out of [heading levels][heading_level].

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_submodules: true
```

```md title="or in docs/some_page.md (local configuration)"
::: package.subpackage
    options:
      show_submodules: false
```

```tree title="package"
package
    __init__.py
    subpackage
        __init__.py
        submodule.py
```

/// admonition | Preview
    type: preview

//// tab | With submodules
<p>Subpackage docstring.</p>
<h2><code>subpackage_member</code></h2>
<p>Member docstring.</p>
<h2><code>submodule</code></h2>
<p>Submodule docstring.</p>
<h3><code>submodule_member</code></h3>
<p>Member docstring.</p>
////

//// tab | Without submodules
<p>Subpackage docstring.</p>
<h2><code>subpackage_member</code></h2>
<p>Member docstring.</p>
////
///