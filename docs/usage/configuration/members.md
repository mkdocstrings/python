# Members options

[](){#option-members}
## `members`

- **:octicons-package-24: Type <code><autoref identifier="list" optional>list</autoref>[<autoref identifier="str" optional>str</autoref>] |
    <autoref identifier="bool" optional>bool</autoref> | None</code>  :material-equal: `None`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

An explicit list of members to render.

Only members declared in this list will be rendered.
A member without a docstring will still be rendered,
even if [`show_if_no_docstring`][] is set to false.

The members will be rendered in the specified order,
regardless of the value of [`members_order`][].
**Note that members will still be grouped by category,
according to the [`group_by_category`][] option.**

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

[](){#option-inherited_members}
## `inherited_members`

- **:octicons-package-24: Type <code><autoref identifier="list" optional>list</autoref>[<autoref identifier="str" optional>str</autoref>] |
    <autoref identifier="bool" optional>bool</autoref></code>  :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

An explicit list of inherited members (for classes) to render.

Inherited members are always fetched from classes that are in the same package
as the currently rendered class. To fetch members inherited from base classes,
themselves coming from external packages, use the [`preload_modules`][preload_modules] option.
For example, if your class inherits from Pydantic's `BaseModel`, and you want to render
`BaseModel`'s methods in your class, use `preload_modules: [pydantic]`.
The `pydantic` package must be available in the current environment.

Passing a falsy value (`no`, `false` in YAML) or an empty list (`[]`)
will tell the Python handler not to render any inherited member.
Passing a truthy value (`yes`, `true` in YAML)
will tell the Python handler to render every inherited member.

When all inherited members are selected with `inherited_members: true`,
it is possible to specify both members and inherited members in the `members` list:

```yaml
inherited_members: true
members:
- inherited_member_a
- inherited_member_b
- member_x
- member_y
```

The alternative is not supported:

```yaml
inherited_members:
- inherited_member_a
- inherited_member_b
members:
- member_x
- member_y
```

...because it would make members ordering ambiguous/unspecified.

You can render inherited members *only* by setting `inherited_members: true`
(or a list of inherited members) and setting `members: false`:

```yaml
inherited_members: true
members: false
```

```yaml
inherited_members:
- inherited_member_a
- inherited_member_b
members: false
```

You can render *all declared members* and all or specific inherited members
by leaving `members` as null (default):

```yaml
inherited_members:
- inherited_member_a
- inherited_member_b
# members: null  # (1)
```

1. In this case, only declared members will be subject
to further filtering with [`filters`][filters] and [`docstrings`][show_if_no_docstring].

```yaml
inherited_members: true  # (1)
# members: null
```

1. In this case, both declared and inherited members will be subject
to further filtering with [`filters`][filters] and [`docstrings`][show_if_no_docstring].

You can render *all declared members* and all or specific inherited members,
avoiding further filtering with [`filters`][filters] and [`docstrings`][show_if_no_docstring]
by setting `members: true`:

```yaml
inherited_members: true
members: true
```

```yaml
inherited_members:
- inherited_member_a
- inherited_member_b
members: true
```

The general rule is that declared or inherited members specified in lists
are never filtered out.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          inherited_members: false
```

```md title="or in docs/some_page.md (local configuration)"
::: package.module
    options:
      inherited_members: true
```

```python title="package/module.py"
"""Module docstring."""


class Base:
    """Base class."""

    def base(self):
        """Base method."""


class Main(Base):
    """Main class."""

    def main(self):
        """Main method."""
```

/// admonition | Preview
    type: preview

//// tab | With inherited members
<p>Module docstring.</p>
<h2><code>Base</code></h2>
<p>Base class.</p>
<h3><code>base</code></h3>
<p>Base method.</p>
<h2><code>Main</code></h2>
<p>Main class.</p>
<h3><code>base</code></h3>
<p>Base method.</p>
<h3><code>main</code></h3>
<p>Main method.</p>
////

//// tab | Without inherited members
<p>Module docstring.</p>
<h2><code>Base</code></h2>
<p>Base class.</p>
<h3><code>base</code></h3>
<p>Base method.</p>
<h2><code>Main</code></h2>
<p>Main class.</p>
<h3><code>main</code></h3>
<p>Main method.</p>
////

///

[](){#option-members_order}
## `members_order`

- **:octicons-package-24: Type `str | list[str]` :material-equal: `"alphabetical"`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

The members ordering to use. Possible values:

- `__all__` ([:octicons-heart-fill-24:{ .pulse } Sponsors only](../../insiders/index.md){ .insiders } &mdash; [:octicons-tag-24: Insiders 1.12.0](../../insiders/changelog.md#1.12.0)): Order according to `__all__` attributes. Since classes do not define `__all__` attributes, you can specify a second ordering method by using a list.
- `alphabetical`: Order by the members names.
- `source`: Order members as they appear in the source file.

The order applies for all members, recursively.
The order will be ignored for members that are explicitely sorted using the [`members`][] option.
**Note that members will still be grouped by category,
according to the [`group_by_category`][] option.**

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

```md title="or in docs/some_page.md (local configuration)"
::: package.module
    options:
      members_order: [__all__, source]
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

[](){#option-filters}
## `filters`

- **:octicons-package-24: Type <code><autoref identifier="list" optional>list</autoref>[<autoref identifier="str" optional>str</autoref>] | <autoref identifier="typing.Literal" optional>Literal</autoref>["public"] | None</code>  :material-equal: `["!^_[^_]"]`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

A list of filters, or `"public"`.

**Filtering methods**

[](){#option-filters-public}

[:octicons-heart-fill-24:{ .pulse } Sponsors only](../../insiders/index.md){ .insiders } &mdash;
[:octicons-tag-24: Insiders 1.11.0](../../insiders/changelog.md#1.11.0)

The `public` filtering method will include only public objects: those added to the `__all__` attribute of modules, or not starting with a single underscore. Special methods and attributes ("dunder" methods/attributes, starting and ending with two underscores), like `__init__`, `__call__`, `__mult__`, etc., are always considered public.

**List of filters**

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
          - "!^_[^_]"
```

```md title="or in docs/some_page.md (local configuration)"
::: package.module
    options:
      filters: public
```

```python title="package/module.py"
def hello():
    ...


def _world():
    ...
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

[](){#option-group_by_category}
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
def function_a():
    ...


class ClassB:
    ...


attribute_C = 0


def function_d():
    ...
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

[](){#option-show_submodules}
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

[](){#option-summary}
## `summary`

[:octicons-tag-24: Insiders 1.2.0](../../insiders/changelog.md#1.2.0)

- **:octicons-package-24: Type <code><autoref identifier="bool" optional>bool</autoref> | <autoref identifier="dict" optional>dict</autoref>[<autoref identifier="str" optional>str</autoref>, <autoref identifier="bool" optional>bool</autoref>]</code>  :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to render summaries of modules, classes, functions (methods) and attributes.

This option accepts a boolean (`yes`, `true`, `no`, `false` in YAML)
or a dictionary with one or more of the following keys: `attributes`, `functions`, `classes`, `modules`, `type_aliases`,
with booleans as values. Class methods summary is (de)activated with the `functions` key.
By default, `summary` is false, and by extension all values are false.

Examples:

```yaml
summary: true
```

```yaml
summary: false
```

```yaml
summary:
  attributes: false
  functions: true
  modules: false
```

Summaries will be rendered as the corresponding docstring sections.
For example, the summary for attributes will be rendered as an Attributes docstring section.
The section will be rendered in accordance with the [`docstring_section_style`][] option.
If the objects appearing in the summary are also rendered on the page
(or somewhere else on the site), their name will automatically link to their rendered documentation.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          summary: true
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      summary: false
```

/// admonition | Preview
    type: preview

//// tab | With all summaries
```
::: path.to.module.MyClass
    options:
      summary: true
```
<h2>MyClass</h2>
<p>Class docstring.</p>
<p>Methods:</p>
<ul>
  <li><a href="#my_method1">my_method1</a>: Summary of the method (first docstring line).</li>
  <li><a href="#my_method2">my_method2</a>: Summary of the method (first docstring line).</li>
</ul>
<p>Attributes:</p>
<ul>
  <li><a href="#attr1">attr1</a>: Summary of the attribute (first docstring line).</li>
  <li><a href="#attr2">attr2</a>: Summary of the attribute (first docstring line).</li>
</ul>
////

//// tab | With methods summary only
```
::: path.to.module.MyClass
    options:
      summary:
        functions: true
```

<h2>MyClass</h2>
<p>Class docstring.</p>
<p>Methods:</p>
<ul>
  <li><a href="#my_method1">my_method1</a>: Summary of the method (first docstring line).</li>
  <li><a href="#my_method2">my_method2</a>: Summary of the method (first docstring line).</li>
</ul>
////
///

[](){#option-show_labels}
## `show_labels`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Whether to show labels of the members.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_labels: true
```

```md title="or in docs/some_page.md (local configuration)"
::: package.module
    options:
      show_labels: false
```

```python title="package/module.py"
class SomeClass:
    some_attr: int
```

/// admonition | Preview
    type: preview

//// tab | With labels
<code class="highlight language-python">
  <span class="n">some_attr</span><span class="p">:</span>
  <span class="nb">int</span>
</code>
<small><code>instance-attribute</code></small>
////

//// tab | Without labels
<code class="highlight language-python">
  <span class="n">some_attr</span><span class="p">:</span>
  <span class="nb">int</span>
</code>
////
///
