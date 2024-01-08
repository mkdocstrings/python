# Headings options

## `heading_level`

- **:octicons-package-24: Type [`int`][] :material-equal: `2`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

The initial heading level to use.

When injecting documentation for an object,
the object itself and its members are rendered.
For each layer of objects, we increase the heading level by 1.

The initial heading level will be used for the first layer.
If you set it to 3, then headings will start with `<h3>`.

If the [heading for the root object][show_root_heading] is not shown,
then the initial heading level is used for its members.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          heading_level: 2
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    options:
      heading_level: 3
```

/// admonition | Preview
    type: preview

//// tab | With level 3 and root heading
<h3><code>module</code> (3)</h3>
<p>Docstring of the module.</p>
<h4><code>ClassA</code> (4)</h4>
<p>Docstring of class A.</p>
<h4><code>ClassB</code> (4)</h4>
<p>Docstring of class B.</p>
<h5><code>method_1</code> (5)</h5>
<p>Docstring of the method.</p>
////

//// tab | With level 3, without root heading
<p>Docstring of the module.</p>
<h3><code>ClassA</code> (3)</h3>
<p>Docstring of class A.</p>
<h3><code>ClassB</code> (3)</h3>
<p>Docstring of class B.</p>
<h4><code>method_1</code> (4)</h4>
<p>Docstring of the method.</p>
////
///

## `show_root_heading`

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Show the heading of the object at the root of the documentation tree
(i.e. the object referenced by the identifier after `:::`).

It is pretty common to inject documentation for one module per page,
especially when following our [automatic reference pages recipe][autopages recipe].
Since each page already has a title, usually being the module's name,
we can spare one heading level by not showing the heading for the module itself
(heading levels are limited to 6 by the HTML specification).

Sparing that extra level can be helpful when your objects tree is deeply nested
(e.g. method in a class in a class in a module).
If your objects tree is not deeply nested, and you are injecting documentation
for many different objects on a single page, it might be preferable to render
the heading of each object.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_root_heading: false
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.ClassA
    options:
      show_root_heading: true

::: path.to.ClassB
    options:
      show_root_heading: true
```

/// admonition | Preview
    type: preview

//// tab | With root heading
<h2><code>ClassA</code> (2)</h2>
<p>Docstring of class A.</p>
<h3><code>method_a1</code> (3)</h3>
<p>Docstring of the method.</p>
<h2><code>ClassB</code> (2)</h2>
<p>Docstring of class B.</p>
<h3><code>method_b1</code> (3)</h3>
<p>Docstring of the method.</p>
////

//// tab | Without root heading
<p>Docstring of class A.</p>
<h2><code>method_a1</code> (2)</h2>
<p>Docstring of the method.</p>
<p>Docstring of class B.</p>
<h2><code>method_b1</code> (2)</h2>
<p>Docstring of the method.</p>
////
///

## `show_root_toc_entry`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

If the root heading is not shown, at least add a ToC entry for it.

If you inject documentation for an object in the middle of a page,
after long paragraphs, and without showing the [root heading][show_root_heading],
then you will not be able to link to this particular object
as it won't have a permalink and will be "lost" in the middle of text.
In that case, it is useful to add a hidden anchor to the document,
which will also appear in the table of contents.

In other cases, you might want to disable the entry to avoid polluting the ToC.
It is not possible to show the root heading *and* hide the ToC entry.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_root_toc_entry: true
```

```md title="or in docs/some_page.md (local configuration)"
## Some heading

Lots of text.

::: path.to.object
    options:
      show_root_toc_entry: false

## Other heading.

More text.
```

/// admonition | Preview
    type: preview

//// tab | With ToC entry
**Table of contents**  
[Some heading](#permalink-to-some-heading){ title="#permalink-to-some-heading" }  
[`object`](#permalink-to-object){ title="#permalink-to-object" }   
[Other heading](#permalink-to-other-heading){ title="#permalink-to-other-heading" } 
////

//// tab | Without ToC entry
**Table of contents**  
[Some heading](#permalink-to-some-heading){ title="#permalink-to-some-heading" }  
[Other heading](#permalink-to-other-heading){ title="#permalink-to-other-heading" }
////
///

## `show_root_full_path`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Show the full Python path for the root object heading.

The path of a Python object is the dot-separated list of names
under which it is accessible, for example `package.module.Class.method`.

With this option you can choose to show the full path of the object
you inject documentation for, or just its name. This option impacts
only the object you specify, not its members. For members, see the two
other options [`show_root_members_full_path`][]
and [`show_object_full_path`][].

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_root_full_path: true
```

```md title="or in docs/some_page.md (local configuration)"
::: package.module.Class.method
    options:
      show_root_full_path: false
```

/// admonition | Preview
    type: preview

//// tab | With root full path
<h2><code>package.module.Class.method</code></h2>
<p>Docstring of the method.</p>
////

//// tab | Without root full path
<h2><code>method</code></h2>
<p>Docstring of the method.</p>
////
///

## `show_root_members_full_path`

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Show the full Python path of the root members.

This option does the same thing as [`show_root_full_path`][],
but for direct members  of the root object instead of the root object itself.

To show the full path for every member recursively,
see [`show_object_full_path`][].

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_root_members_full_path: true
```

```md title="or in docs/some_page.md (local configuration)"
::: package.module
    options:
      show_root_members_full_path: false
```

/// admonition | Preview
    type: preview

//// tab | With members full path
<p>Docstring of the module.</p>
<h2><code>package.module.Class</code></h2>
<p>Docstring of the class.</p>
<h3><code>method</code></h3>
<p>Docstring of the method.</p>
////

//// tab | Without members full path
<p>Docstring of the module.</p>
<h2><code>Class</code></h2>
<p>Docstring of the class.</p>
<h3><code>method</code></h3>
<p>Docstring of the method.</p>
////
///

## `show_object_full_path`

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Show the full Python path of every object.

Same as for [`show_root_members_full_path`][],
but for every member, recursively. This option takes precedence over 
[`show_root_members_full_path`][]:

`show_root_members_full_path` | `show_object_full_path` | Direct root members path
----------------------------- | ----------------------- | ------------------------
False                         | False                   | Name only
False                         | True                    | Full
True                          | False                   | Full
True                          | True                    | Full

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_object_full_path: true
```

```md title="or in docs/some_page.md (local configuration)"
::: package.module
    options:
      show_object_full_path: false
```

/// admonition | Preview
    type: preview

//// tab | With objects full path
<p>Docstring of the module.</p>
<h2><code>package.module.Class</code></h2>
<p>Docstring of the class.</p>
<h3><code>package.module.Class.method</code></h3>
<p>Docstring of the method.</p>
////

//// tab | Without objects full path
<p>Docstring of the module.</p>
<h2><code>Class</code></h2>
<p>Docstring of the class.</p>
<h3><code>method</code></h3>
<p>Docstring of the method.</p>
////
///

## `show_category_heading`

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

When [grouped by categories][group_by_category], show a heading for each category.
These category headings will appear in the table of contents,
allowing you to link to them using their permalinks.

WARNING: **Not recommended with deeply nested object**  
When injecting documentation for deeply nested objects,
you'll quickly run out of heading levels, and the objects
at the bottom of the tree risk all getting documented
using H6 headings, which might decrease the readability
of your API docs.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          group_by_category: true
          show_category_heading: true
```

```md title="or in docs/some_page.md (local configuration)"
::: package.module
    options:
      group_by_category: true
      show_category_heading: false
```

/// admonition | Preview
    type: preview

//// tab | With category headings
<p>Docstring of the module.</p>
<h2>Attributes (2)</h2>
<h3><code>module_attribute</code> (3)</h3>
<p>Docstring of the module attribute.</p>
<h2>Classes (2)</h2>
<h3><code>Class</code> (3)</h3>
<p>Docstring of the class.</p>
<h4>Attributes (4)</h4>
<h5><code>class_attribute</code> (5)</h5>
<p>Docstring of the class attribute.</p>
<h4>Methods (4)</h4>
<h5><code>method</code> (5)</h5>
<p>Docstring of the method.</p>
////

//// tab | Without category headings
<p>Docstring of the module.</p>
<h2><code>module_attribute</code> (2)</h2>
<p>Docstring of the module attribute.</p>
<h2><code>Class</code> (2)</h2>
<p>Docstring of the class.</p>
<h3><code>class_attribute</code> (3)</h3>
<p>Docstring of the class attribute.</p>
<h3><code>method</code> (3)</h3>
<p>Docstring of the method.</p>
////
///

## `show_symbol_type_heading`

[:octicons-tag-24: Insiders 1.1.0](../../insiders/changelog.md#1.1.0)

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Show the symbol type in headings.

This option will prefix headings with
<code class="doc-symbol doc-symbol-attribute"></code>,
<code class="doc-symbol doc-symbol-function"></code>,
<code class="doc-symbol doc-symbol-method"></code>,
<code class="doc-symbol doc-symbol-class"></code> or
<code class="doc-symbol doc-symbol-module"></code> types.
See also [`show_symbol_type_toc`][show_symbol_type_toc].

To customize symbols, see [Customizing symbol types](../customization.md/#symbol-types).

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_symbol_type_heading: true
```

```md title="or in docs/some_page.md (local configuration)"
::: package.module
    options:
      show_symbol_type_heading: false
```

/// admonition | Preview
    type: preview

//// tab | With symbol type in headings
<h1><code class="doc-symbol doc-symbol-module"></code> <code>module</code></h1>
<p>Docstring of the module.</p>
<h2><code class="doc-symbol doc-symbol-attribute"></code> <code>attribute</code></h2>
<p>Docstring of the module attribute.</p>
<h2><code class="doc-symbol doc-symbol-function"></code> <code>function</code></h2>
<p>Docstring of the function.</p>
<h2><code class="doc-symbol doc-symbol-class"></code> <code>Class</code></h2>
<p>Docstring of the class.</p>
<h3><code class="doc-symbol doc-symbol-method"></code> <code>method</code></h3>
<p>Docstring of the method.</p>
////

//// tab | Without symbol type in headings
<h1><code>module</code></h1>
<p>Docstring of the module.</p>
<h2><code>attribute</code></h2>
<p>Docstring of the module attribute.</p>
<h2><code>function</code></h2>
<p>Docstring of the function.</p>
<h2><code>Class</code></h2>
<p>Docstring of the class.</p>
<h3><code>method</code></h3>
<p>Docstring of the method.</p>
////
///

## `show_symbol_type_toc`

[:octicons-tag-24: Insiders 1.1.0](../../insiders/changelog.md#1.1.0)

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

Show the symbol type in the Table of Contents.

This option will prefix items in the ToC with
<code class="doc-symbol doc-symbol-attribute"></code>,
<code class="doc-symbol doc-symbol-function"></code>,
<code class="doc-symbol doc-symbol-method"></code>,
<code class="doc-symbol doc-symbol-class"></code> or
<code class="doc-symbol doc-symbol-module"></code> types.
See also [`show_symbol_type_heading`][show_symbol_type_heading].

To customize symbols, see [Customizing symbol types](../customization.md/#symbol-types).

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          show_symbol_type_toc: true
```

```md title="or in docs/some_page.md (local configuration)"
::: package.module
    options:
      show_symbol_type_toc: false
```

/// admonition | Preview
    type: preview

//// tab | With symbol type in ToC
<ul style="list-style: none;">
  <li><code class="doc-symbol doc-symbol-module"></code> module</li>
  <li><code class="doc-symbol doc-symbol-attribute"></code> attribute</li>
  <li><code class="doc-symbol doc-symbol-function"></code> function</li>
  <li><code class="doc-symbol doc-symbol-class"></code> Class
    <ul style="list-style: none;">
      <li><code class="doc-symbol doc-symbol-method"></code> method</li>
    </ul>
  </li>
</ul>
////

//// tab | Without symbol type in ToC
<ul style="list-style: none;">
  <li>module</li>
  <li>attribute</li>
  <li>function</li>
  <li>Class
    <ul style="list-style: none;">
      <li>method</li>
    </ul>
  </li>
</ul>
////
///
