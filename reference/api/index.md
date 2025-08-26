# python

Python handler for mkdocstrings.

Modules:

- **`config`** – Deprecated. Import from mkdocstrings_handlers.python directly.
- **`handler`** – Deprecated. Import from mkdocstrings_handlers.python directly.
- **`rendering`** – Deprecated. Import from mkdocstrings_handlers.python directly.

Classes:

- **`AutoStyleOptions`** – Auto style docstring options.
- **`AutorefsHook`** – Autorefs hook.
- **`GoogleStyleOptions`** – Google style docstring options.
- **`Inventory`** – An inventory.
- **`NumpyStyleOptions`** – Numpy style docstring options.
- **`PerStyleOptions`** – Per style options.
- **`PythonConfig`** – Python handler configuration.
- **`PythonHandler`** – The Python handler class.
- **`PythonInputConfig`** – Python handler configuration.
- **`PythonInputOptions`** – Accepted input options.
- **`PythonOptions`** – Final options passed as template context.
- **`SphinxStyleOptions`** – Sphinx style docstring options.
- **`SummaryOption`** – Summary option.

Functions:

- **`do_as_attributes_section`** – Build an attributes section from a list of attributes.
- **`do_as_classes_section`** – Build a classes section from a list of classes.
- **`do_as_functions_section`** – Build a functions section from a list of functions.
- **`do_as_modules_section`** – Build a modules section from a list of modules.
- **`do_as_type_aliases_section`** – Build a type aliases section from a list of type aliases.
- **`do_backlink_tree`** – Build a tree of backlinks.
- **`do_crossref`** – Deprecated. Filter to create cross-references.
- **`do_filter_objects`** – Filter a dictionary of objects based on their docstrings.
- **`do_format_attribute`** – Format an attribute.
- **`do_format_code`** – Format code.
- **`do_format_signature`** – Format a signature.
- **`do_format_type_alias`** – Format a type alias.
- **`do_get_template`** – Get the template name used to render an object.
- **`do_multi_crossref`** – Deprecated. Filter to create cross-references.
- **`do_order_members`** – Order members given an ordering method.
- **`do_split_path`** – Split object paths for building cross-references.
- **`get_handler`** – Return an instance of PythonHandler.

Attributes:

- **`Order`** – Ordering methods.
- **`Tree`** – A tree type. Each node holds a tuple of items.
- **`do_stash_crossref`** – Filter to stash cross-references (and restore them after formatting and highlighting).

## Order

```python
Order = Literal['__all__', 'alphabetical', 'source']
```

Ordering methods.

- `__all__`: order members according to `__all__` module attributes, if declared;
- `alphabetical`: order members alphabetically;
- `source`: order members as they appear in the source file.

## Tree

```python
Tree = dict[tuple[_T, ...], 'Tree']
```

A tree type. Each node holds a tuple of items.

## do_stash_crossref

```python
do_stash_crossref = _StashCrossRefFilter()
```

Filter to stash cross-references (and restore them after formatting and highlighting).

## AutoStyleOptions

```python
AutoStyleOptions(
    method: Literal["heuristics", "max_sections"] = "heuristics",
    style_order: list[str] = (lambda: ["sphinx", "google", "numpy"])(),
    default: str | None = None,
    per_style_options: PerStyleOptions = PerStyleOptions(),
)
```

Auto style docstring options.

Methods:

- **`from_data`** – Create an instance from a dictionary.

Attributes:

- **`default`** (`str | None`) – The default docstring style to use if no other style is detected.
- **`method`** (`Literal['heuristics', 'max_sections']`) – The method to use to determine the docstring style.
- **`per_style_options`** (`PerStyleOptions`) – Per-style options.
- **`style_order`** (`list[str]`) – The order of the docstring styles to try.

### default

```python
default: str | None = None
```

The default docstring style to use if no other style is detected.

### method

```python
method: Literal['heuristics', 'max_sections'] = 'heuristics'
```

The method to use to determine the docstring style.

### per_style_options

```python
per_style_options: PerStyleOptions = field(default_factory=PerStyleOptions)
```

Per-style options.

### style_order

```python
style_order: list[str] = field(default_factory=lambda: ['sphinx', 'google', 'numpy'])
```

The order of the docstring styles to try.

### from_data

```python
from_data(**data: Any) -> Self
```

Create an instance from a dictionary.

## AutorefsHook

```python
AutorefsHook(current_object: Object | Alias, config: dict[str, Any])
```

```
              flowchart TD
              mkdocstrings_handlers.python.AutorefsHook[AutorefsHook]

              

              click mkdocstrings_handlers.python.AutorefsHook href "" "mkdocstrings_handlers.python.AutorefsHook"
```

Autorefs hook.

With this hook, we're able to add context to autorefs (cross-references), such as originating file path and line number, to improve error reporting.

Parameters:

- ### **`current_object`**

  (`Object | Alias`) – The object being rendered.

- ### **`config`**

  (`dict[str, Any]`) – The configuration dictionary.

Methods:

- **`expand_identifier`** – Expand an identifier.
- **`get_context`** – Get the context for the current object.

Attributes:

- **`config`** – The configuration options.
- **`current_object`** – The current object being rendered.

### config

```python
config = config
```

The configuration options.

### current_object

```python
current_object = current_object
```

The current object being rendered.

### expand_identifier

```python
expand_identifier(identifier: str) -> str
```

Expand an identifier.

Parameters:

- #### **`identifier`**

  (`str`) – The identifier to expand.

Returns:

- `str` – The expanded identifier.

### get_context

```python
get_context() -> Context
```

Get the context for the current object.

Returns:

- `Context` – The context.

## GoogleStyleOptions

```python
GoogleStyleOptions(
    ignore_init_summary: bool = False,
    returns_multiple_items: bool = True,
    returns_named_value: bool = True,
    returns_type_in_property_summary: bool = False,
    receives_multiple_items: bool = True,
    receives_named_value: bool = True,
    trim_doctest_flags: bool = True,
    warn_unknown_params: bool = True,
    warn_missing_types: bool = True,
    warnings: bool = True,
)
```

Google style docstring options.

Attributes:

- **`ignore_init_summary`** (`bool`) – Whether to ignore the summary in __init__ methods' docstrings.
- **`receives_multiple_items`** (`bool`) – Whether to parse multiple items in Receives sections.
- **`receives_named_value`** (`bool`) – Whether to parse Receives section items as name and description, rather than type and description.
- **`returns_multiple_items`** (`bool`) – Whether to parse multiple items in Yields and Returns sections.
- **`returns_named_value`** (`bool`) – Whether to parse Yields and Returns section items as name and description, rather than type and description.
- **`returns_type_in_property_summary`** (`bool`) – Whether to parse the return type of properties at the beginning of their summary: str: Summary of the property.
- **`trim_doctest_flags`** (`bool`) – Whether to remove doctest flags from Python example blocks.
- **`warn_missing_types`** (`bool`) – Warn about missing type/annotation for parameters, return values, etc.
- **`warn_unknown_params`** (`bool`) – Warn about documented parameters not appearing in the signature.
- **`warnings`** (`bool`) – Generally enable/disable warnings when parsing docstrings.

### ignore_init_summary

```python
ignore_init_summary: bool = False
```

Whether to ignore the summary in `__init__` methods' docstrings.

### receives_multiple_items

```python
receives_multiple_items: bool = True
```

Whether to parse multiple items in `Receives` sections.

When true, each item's continuation lines must be indented. When false (single item), no further indentation is required.

### receives_named_value

```python
receives_named_value: bool = True
```

Whether to parse `Receives` section items as name and description, rather than type and description.

When true, type must be wrapped in parentheses: `(int): Description.`. Names are optional: `name (int): Description.`. When false, parentheses are optional but the items cannot be named: `int: Description`.

### returns_multiple_items

```python
returns_multiple_items: bool = True
```

Whether to parse multiple items in `Yields` and `Returns` sections.

When true, each item's continuation lines must be indented. When false (single item), no further indentation is required.

### returns_named_value

```python
returns_named_value: bool = True
```

Whether to parse `Yields` and `Returns` section items as name and description, rather than type and description.

When true, type must be wrapped in parentheses: `(int): Description.`. Names are optional: `name (int): Description.`. When false, parentheses are optional but the items cannot be named: `int: Description`.

### returns_type_in_property_summary

```python
returns_type_in_property_summary: bool = False
```

Whether to parse the return type of properties at the beginning of their summary: `str: Summary of the property`.

### trim_doctest_flags

```python
trim_doctest_flags: bool = True
```

Whether to remove doctest flags from Python example blocks.

### warn_missing_types

```python
warn_missing_types: bool = True
```

Warn about missing type/annotation for parameters, return values, etc.

### warn_unknown_params

```python
warn_unknown_params: bool = True
```

Warn about documented parameters not appearing in the signature.

### warnings

```python
warnings: bool = True
```

Generally enable/disable warnings when parsing docstrings.

## Inventory

```python
Inventory(
    url: str, base_url: str | None = None, domains: list[str] = (lambda: ["py"])()
)
```

An inventory.

Attributes:

- **`base_url`** (`str | None`) – The base URL of the inventory.
- **`domains`** (`list[str]`) – The domains to load from the inventory.
- **`url`** (`str`) – The URL of the inventory.

### base_url

```python
base_url: str | None = None
```

The base URL of the inventory.

### domains

```python
domains: list[str] = field(default_factory=lambda: ['py'])
```

The domains to load from the inventory.

### url

```python
url: str
```

The URL of the inventory.

## NumpyStyleOptions

```python
NumpyStyleOptions(
    ignore_init_summary: bool = False,
    trim_doctest_flags: bool = True,
    warn_unknown_params: bool = True,
    warn_missing_types: bool = True,
    warnings: bool = True,
)
```

Numpy style docstring options.

Attributes:

- **`ignore_init_summary`** (`bool`) – Whether to ignore the summary in __init__ methods' docstrings.
- **`trim_doctest_flags`** (`bool`) – Whether to remove doctest flags from Python example blocks.
- **`warn_missing_types`** (`bool`) – Warn about missing type/annotation for parameters, return values, etc.
- **`warn_unknown_params`** (`bool`) – Warn about documented parameters not appearing in the signature.
- **`warnings`** (`bool`) – Generally enable/disable warnings when parsing docstrings.

### ignore_init_summary

```python
ignore_init_summary: bool = False
```

Whether to ignore the summary in `__init__` methods' docstrings.

### trim_doctest_flags

```python
trim_doctest_flags: bool = True
```

Whether to remove doctest flags from Python example blocks.

### warn_missing_types

```python
warn_missing_types: bool = True
```

Warn about missing type/annotation for parameters, return values, etc.

### warn_unknown_params

```python
warn_unknown_params: bool = True
```

Warn about documented parameters not appearing in the signature.

### warnings

```python
warnings: bool = True
```

Generally enable/disable warnings when parsing docstrings.

## PerStyleOptions

```python
PerStyleOptions(
    google: GoogleStyleOptions = GoogleStyleOptions(),
    numpy: NumpyStyleOptions = NumpyStyleOptions(),
    sphinx: SphinxStyleOptions = SphinxStyleOptions(),
)
```

Per style options.

Methods:

- **`from_data`** – Create an instance from a dictionary.

Attributes:

- **`google`** (`GoogleStyleOptions`) – Google-style options.
- **`numpy`** (`NumpyStyleOptions`) – Numpydoc-style options.
- **`sphinx`** (`SphinxStyleOptions`) – Sphinx-style options.

### google

```python
google: GoogleStyleOptions = field(default_factory=GoogleStyleOptions)
```

Google-style options.

### numpy

```python
numpy: NumpyStyleOptions = field(default_factory=NumpyStyleOptions)
```

Numpydoc-style options.

### sphinx

```python
sphinx: SphinxStyleOptions = field(default_factory=SphinxStyleOptions)
```

Sphinx-style options.

### from_data

```python
from_data(**data: Any) -> Self
```

Create an instance from a dictionary.

## PythonConfig

```python
PythonConfig(
    inventories: list[Inventory] = list(),
    paths: list[str] = (lambda: ["."])(),
    load_external_modules: bool | None = None,
    options: dict[str, Any] = dict(),
    locale: str | None = None,
)
```

```
              flowchart TD
              mkdocstrings_handlers.python.PythonConfig[PythonConfig]
              mkdocstrings_handlers.python._internal.config.PythonInputConfig[PythonInputConfig]

                              mkdocstrings_handlers.python._internal.config.PythonInputConfig --> mkdocstrings_handlers.python.PythonConfig
                


              click mkdocstrings_handlers.python.PythonConfig href "" "mkdocstrings_handlers.python.PythonConfig"
              click mkdocstrings_handlers.python._internal.config.PythonInputConfig href "" "mkdocstrings_handlers.python._internal.config.PythonInputConfig"
```

Python handler configuration.

Methods:

- **`coerce`** – Coerce data.
- **`from_data`** – Create an instance from a dictionary.

Attributes:

- **`inventories`** (`list[Inventory]`) – The object inventories to load.
- **`load_external_modules`** (`bool | None`) – Whether to always load external modules/packages.
- **`locale`** (`str | None`) – Deprecated. Use mkdocstrings' own locale setting instead. The locale to use when translating template strings.
- **`options`** (`dict[str, Any]`) – Configuration options for collecting and rendering objects.
- **`paths`** (`list[str]`) – The paths in which to search for Python packages.

### inventories

```python
inventories: list[Inventory] = field(default_factory=list)
```

The object inventories to load.

### load_external_modules

```python
load_external_modules: bool | None = None
```

Whether to always load external modules/packages.

### locale

```python
locale: str | None = None
```

Deprecated. Use mkdocstrings' own `locale` setting instead. The locale to use when translating template strings.

### options

```python
options: dict[str, Any] = field(default_factory=dict)
```

Configuration options for collecting and rendering objects.

### paths

```python
paths: list[str] = field(default_factory=lambda: ['.'])
```

The paths in which to search for Python packages.

### coerce

```python
coerce(**data: Any) -> MutableMapping[str, Any]
```

Coerce data.

### from_data

```python
from_data(**data: Any) -> Self
```

Create an instance from a dictionary.

## PythonHandler

```python
PythonHandler(config: PythonConfig, base_dir: Path, **kwargs: Any)
```

```
              flowchart TD
              mkdocstrings_handlers.python.PythonHandler[PythonHandler]
              mkdocstrings._internal.handlers.base.BaseHandler[BaseHandler]

                              mkdocstrings._internal.handlers.base.BaseHandler --> mkdocstrings_handlers.python.PythonHandler
                


              click mkdocstrings_handlers.python.PythonHandler href "" "mkdocstrings_handlers.python.PythonHandler"
              click mkdocstrings._internal.handlers.base.BaseHandler href "" "mkdocstrings._internal.handlers.base.BaseHandler"
```

The Python handler class.

Parameters:

- ### **`config`**

  (`PythonConfig`) – The handler configuration.

- ### **`base_dir`**

  (`Path`) – The base directory of the project.

- ### **`**kwargs`**

  (`Any`, default: `{}` ) – Arguments passed to the parent constructor.

Methods:

- **`collect`** – Collect the documentation for the given identifier.
- **`do_convert_markdown`** – Render Markdown text; for use inside templates.
- **`do_heading`** – Render an HTML heading and register it for the table of contents. For use inside templates.
- **`get_aliases`** – Get the aliases for the given identifier.
- **`get_extended_templates_dirs`** – Load template extensions for the given handler, return their templates directories.
- **`get_headings`** – Return and clear the headings gathered so far.
- **`get_inventory_urls`** – Return the URLs of the inventory files to download.
- **`get_options`** – Get combined default, global and local options.
- **`get_templates_dir`** – Return the path to the handler's templates directory.
- **`load_inventory`** – Yield items and their URLs from an inventory file streamed from in_file.
- **`normalize_extension_paths`** – Resolve extension paths relative to config file.
- **`render`** – Render the collected data.
- **`render_backlinks`** – Render the backlinks.
- **`teardown`** – Teardown the handler.
- **`update_env`** – Update the Jinja environment with custom filters and tests.

Attributes:

- **`base_dir`** – The base directory of the project.
- **`config`** – The handler configuration.
- **`custom_templates`** – The path to custom templates.
- **`domain`** (`str`) – The cross-documentation domain/language for this handler.
- **`enable_inventory`** (`bool`) – Whether this handler is interested in enabling the creation of the objects.inv Sphinx inventory file.
- **`env`** – The Jinja environment.
- **`extra_css`** (`str`) – Extra CSS.
- **`fallback_config`** (`dict`) – Fallback configuration when searching anchors for identifiers.
- **`fallback_theme`** (`str`) – The fallback theme.
- **`global_options`** – The global configuration options (in mkdocs.yml).
- **`md`** (`Markdown`) – The Markdown instance.
- **`mdx`** – The Markdown extensions to use.
- **`mdx_config`** – The configuration for the Markdown extensions.
- **`name`** (`str`) – The handler's name.
- **`outer_layer`** (`bool`) – Whether we're in the outer Markdown conversion layer.
- **`theme`** – The selected theme.

### base_dir

```python
base_dir = base_dir
```

The base directory of the project.

### config

```python
config = config
```

The handler configuration.

### custom_templates

```python
custom_templates = custom_templates
```

The path to custom templates.

### domain

```python
domain: str = 'py'
```

The cross-documentation domain/language for this handler.

### enable_inventory

```python
enable_inventory: bool = True
```

Whether this handler is interested in enabling the creation of the `objects.inv` Sphinx inventory file.

### env

```python
env = Environment(autoescape=True, loader=FileSystemLoader(paths), auto_reload=False)
```

The Jinja environment.

### extra_css

```python
extra_css: str = ''
```

Extra CSS.

### fallback_config

```python
fallback_config: dict = {}
```

Fallback configuration when searching anchors for identifiers.

### fallback_theme

```python
fallback_theme: str = 'material'
```

The fallback theme.

### global_options

```python
global_options = global_options
```

The global configuration options (in `mkdocs.yml`).

### md

```python
md: Markdown
```

The Markdown instance.

Raises:

- `RuntimeError` – When the Markdown instance is not set yet.

### mdx

```python
mdx = mdx
```

The Markdown extensions to use.

### mdx_config

```python
mdx_config = mdx_config
```

The configuration for the Markdown extensions.

### name

```python
name: str = 'python'
```

The handler's name.

### outer_layer

```python
outer_layer: bool
```

Whether we're in the outer Markdown conversion layer.

### theme

```python
theme = theme
```

The selected theme.

### collect

```python
collect(identifier: str, options: PythonOptions) -> CollectorItem
```

Collect the documentation for the given identifier.

Parameters:

- #### **`identifier`**

  (`str`) – The identifier of the object to collect.

- #### **`options`**

  (`PythonOptions`) – The options to use for the collection.

Returns:

- `CollectorItem` – The collected item.

### do_convert_markdown

```python
do_convert_markdown(
    text: str,
    heading_level: int,
    html_id: str = "",
    *,
    strip_paragraph: bool = False,
    autoref_hook: AutorefsHookInterface | None = None
) -> Markup
```

Render Markdown text; for use inside templates.

Parameters:

- #### **`text`**

  (`str`) – The text to convert.

- #### **`heading_level`**

  (`int`) – The base heading level to start all Markdown headings from.

- #### **`html_id`**

  (`str`, default: `''` ) – The HTML id of the element that's considered the parent of this element.

- #### **`strip_paragraph`**

  (`bool`, default: `False` ) – Whether to exclude the <p> tag from around the whole output.

Returns:

- `Markup` – An HTML string.

### do_heading

```python
do_heading(
    content: Markup,
    heading_level: int,
    *,
    role: str | None = None,
    hidden: bool = False,
    toc_label: str | None = None,
    skip_inventory: bool = False,
    **attributes: str
) -> Markup
```

Render an HTML heading and register it for the table of contents. For use inside templates.

Parameters:

- #### **`content`**

  (`Markup`) – The HTML within the heading.

- #### **`heading_level`**

  (`int`) – The level of heading (e.g. 3 -> h3).

- #### **`role`**

  (`str | None`, default: `None` ) – An optional role for the object bound to this heading.

- #### **`hidden`**

  (`bool`, default: `False` ) – If True, only register it for the table of contents, don't render anything.

- #### **`toc_label`**

  (`str | None`, default: `None` ) – The title to use in the table of contents ('data-toc-label' attribute).

- #### **`skip_inventory`**

  (`bool`, default: `False` ) – Flag element to not be registered in the inventory (by setting a data-skip-inventory attribute).

- #### **`**attributes`**

  (`str`, default: `{}` ) – Any extra HTML attributes of the heading.

Returns:

- `Markup` – An HTML string.

### get_aliases

```python
get_aliases(identifier: str) -> tuple[str, ...]
```

Get the aliases for the given identifier.

Parameters:

- #### **`identifier`**

  (`str`) – The identifier to get the aliases for.

Returns:

- `tuple[str, ...]` – The aliases.

### get_extended_templates_dirs

```python
get_extended_templates_dirs(handler: str) -> list[Path]
```

Load template extensions for the given handler, return their templates directories.

Parameters:

- #### **`handler`**

  (`str`) – The name of the handler to get the extended templates directory of.

Returns:

- `list[Path]` – The extensions templates directories.

### get_headings

```python
get_headings() -> Sequence[Element]
```

Return and clear the headings gathered so far.

Returns:

- `Sequence[Element]` – A list of HTML elements.

### get_inventory_urls

```python
get_inventory_urls() -> list[tuple[str, dict[str, Any]]]
```

Return the URLs of the inventory files to download.

### get_options

```python
get_options(local_options: Mapping[str, Any]) -> HandlerOptions
```

Get combined default, global and local options.

Parameters:

- #### **`local_options`**

  (`Mapping[str, Any]`) – The local options.

Returns:

- `HandlerOptions` – The combined options.

### get_templates_dir

```python
get_templates_dir(handler: str | None = None) -> Path
```

Return the path to the handler's templates directory.

Override to customize how the templates directory is found.

Parameters:

- #### **`handler`**

  (`str | None`, default: `None` ) – The name of the handler to get the templates directory of.

Raises:

- `ModuleNotFoundError` – When no such handler is installed.
- `FileNotFoundError` – When the templates directory cannot be found.

Returns:

- `Path` – The templates directory path.

### load_inventory

```python
load_inventory(
    in_file: BinaryIO,
    url: str,
    base_url: str | None = None,
    domains: list[str] | None = None,
    **kwargs: Any
) -> Iterator[tuple[str, str]]
```

Yield items and their URLs from an inventory file streamed from `in_file`.

This implements mkdocstrings' `load_inventory` "protocol" (see mkdocstrings.plugin).

Parameters:

- #### **`in_file`**

  (`BinaryIO`) – The binary file-like object to read the inventory from.

- #### **`url`**

  (`str`) – The URL that this file is being streamed from (used to guess base_url).

- #### **`base_url`**

  (`str | None`, default: `None` ) – The URL that this inventory's sub-paths are relative to.

- #### **`domains`**

  (`list[str] | None`, default: `None` ) – A list of domain strings to filter the inventory by, when not passed, "py" will be used.

- #### **`**kwargs`**

  (`Any`, default: `{}` ) – Ignore additional arguments passed from the config.

Yields:

- `tuple[str, str]` – Tuples of (item identifier, item URL).

### normalize_extension_paths

```python
normalize_extension_paths(extensions: Sequence) -> list[str | dict[str, Any]]
```

Resolve extension paths relative to config file.

Parameters:

- #### **`extensions`**

  (`Sequence`) – The extensions (configuration) to normalize.

Returns:

- `list[str | dict[str, Any]]` – The normalized extensions.

### render

```python
render(data: CollectorItem, options: PythonOptions, locale: str | None = None) -> str
```

Render the collected data.

Parameters:

- #### **`data`**

  (`CollectorItem`) – The collected data.

- #### **`options`**

  (`PythonOptions`) – The options to use for rendering.

- #### **`locale`**

  (`str | None`, default: `None` ) – The locale to use for rendering (default is "en").

Returns:

- `str` – The rendered data (HTML).

### render_backlinks

```python
render_backlinks(
    backlinks: Mapping[str, Iterable[Backlink]], *, locale: str | None = None
) -> str
```

Render the backlinks.

Parameters:

- #### **`backlinks`**

  (`Mapping[str, Iterable[Backlink]]`) – The backlinks to render.

Returns:

- `str` – The rendered backlinks (HTML).

### teardown

```python
teardown() -> None
```

Teardown the handler.

This method should be implemented to, for example, terminate a subprocess that was started when creating the handler instance.

### update_env

```python
update_env(config: Any) -> None
```

Update the Jinja environment with custom filters and tests.

Parameters:

- #### **`config`**

  (`Any`) – The SSG configuration.

## PythonInputConfig

```python
PythonInputConfig(
    inventories: list[str | Inventory] = list(),
    paths: list[str] = (lambda: ["."])(),
    load_external_modules: bool | None = None,
    options: PythonInputOptions = PythonInputOptions(),
    locale: str | None = None,
)
```

Python handler configuration.

Methods:

- **`coerce`** – Coerce data.
- **`from_data`** – Create an instance from a dictionary.

Attributes:

- **`inventories`** (`list[str | Inventory]`) – The inventories to load.
- **`load_external_modules`** (`bool | None`) – Whether to always load external modules/packages.
- **`locale`** (`str | None`) – Deprecated. Use mkdocstrings' own locale setting instead. The locale to use when translating template strings.
- **`options`** (`PythonInputOptions`) – Configuration options for collecting and rendering objects.
- **`paths`** (`list[str]`) – The paths in which to search for Python packages.

### inventories

```python
inventories: list[str | Inventory] = field(default_factory=list)
```

The inventories to load.

### load_external_modules

```python
load_external_modules: bool | None = None
```

Whether to always load external modules/packages.

### locale

```python
locale: str | None = None
```

Deprecated. Use mkdocstrings' own `locale` setting instead. The locale to use when translating template strings.

### options

```python
options: PythonInputOptions = field(default_factory=PythonInputOptions)
```

Configuration options for collecting and rendering objects.

### paths

```python
paths: list[str] = field(default_factory=lambda: ['.'])
```

The paths in which to search for Python packages.

### coerce

```python
coerce(**data: Any) -> MutableMapping[str, Any]
```

Coerce data.

### from_data

```python
from_data(**data: Any) -> Self
```

Create an instance from a dictionary.

## PythonInputOptions

```python
PythonInputOptions(
    allow_inspection: bool = True,
    force_inspection: bool = False,
    annotations_path: Literal["brief", "source", "full"] = "brief",
    backlinks: Literal["flat", "tree", False] = False,
    docstring_options: (
        GoogleStyleOptions
        | NumpyStyleOptions
        | SphinxStyleOptions
        | AutoStyleOptions
        | None
    ) = None,
    docstring_section_style: Literal["table", "list", "spacy"] = "table",
    docstring_style: Literal["auto", "google", "numpy", "sphinx"] | None = "google",
    extensions: list[str | dict[str, Any]] = list(),
    filters: list[str] | Literal["public"] = (lambda: copy())(),
    find_stubs_package: bool = False,
    group_by_category: bool = True,
    heading: str = "",
    heading_level: int = 2,
    inheritance_diagram_direction: Literal["TB", "TD", "BT", "RL", "LR"] = "TD",
    inherited_members: bool | list[str] = False,
    line_length: int = 60,
    members: list[str] | bool | None = None,
    members_order: Order | list[Order] = "alphabetical",
    merge_init_into_class: bool = False,
    modernize_annotations: bool = False,
    overloads_only: bool = False,
    parameter_headings: bool = False,
    preload_modules: list[str] = list(),
    relative_crossrefs: bool = False,
    scoped_crossrefs: bool = False,
    show_overloads: bool = True,
    separate_signature: bool = False,
    show_attribute_values: bool = True,
    show_bases: bool = True,
    show_category_heading: bool = False,
    show_docstring_attributes: bool = True,
    show_docstring_classes: bool = True,
    show_docstring_description: bool = True,
    show_docstring_examples: bool = True,
    show_docstring_functions: bool = True,
    show_docstring_modules: bool = True,
    show_docstring_other_parameters: bool = True,
    show_docstring_parameters: bool = True,
    show_docstring_raises: bool = True,
    show_docstring_receives: bool = True,
    show_docstring_returns: bool = True,
    show_docstring_type_aliases: bool = True,
    show_docstring_type_parameters: bool = True,
    show_docstring_warns: bool = True,
    show_docstring_yields: bool = True,
    show_if_no_docstring: bool = False,
    show_inheritance_diagram: bool = False,
    show_labels: bool = True,
    show_object_full_path: bool = False,
    show_root_full_path: bool = True,
    show_root_heading: bool = False,
    show_root_members_full_path: bool = False,
    show_root_toc_entry: bool = True,
    show_signature_annotations: bool = False,
    show_signature_type_parameters: bool = False,
    show_signature: bool = True,
    show_source: bool = True,
    show_submodules: bool = False,
    show_symbol_type_heading: bool = False,
    show_symbol_type_toc: bool = False,
    skip_local_inventory: bool = False,
    signature_crossrefs: bool = False,
    summary: bool | SummaryOption = SummaryOption(),
    toc_label: str = "",
    type_parameter_headings: bool = False,
    unwrap_annotated: bool = False,
    extra: dict[str, Any] = dict(),
)
```

Accepted input options.

Methods:

- **`coerce`** – Coerce data.
- **`from_data`** – Create an instance from a dictionary.

Attributes:

- **`allow_inspection`** (`bool`) – Whether to allow inspecting modules when visiting them is not possible.
- **`annotations_path`** (`Literal['brief', 'source', 'full']`) – The verbosity for annotations path: brief (recommended), source (as written in the source), or full.
- **`backlinks`** (`Literal['flat', 'tree', False]`) – Whether to render backlinks, and how.
- **`docstring_options`** (`GoogleStyleOptions | NumpyStyleOptions | SphinxStyleOptions | AutoStyleOptions | None`) – The options for the docstring parser.
- **`docstring_section_style`** (`Literal['table', 'list', 'spacy']`) – The style used to render docstring sections.
- **`docstring_style`** (`Literal['auto', 'google', 'numpy', 'sphinx'] | None`) – The docstring style to use: auto, google, numpy, sphinx, or None.
- **`extensions`** (`list[str | dict[str, Any]]`) – A list of Griffe extensions to load.
- **`extra`** (`dict[str, Any]`) – Extra options.
- **`filters`** (`list[str] | Literal['public']`) – A list of filters, or "public".
- **`find_stubs_package`** (`bool`) – Whether to load stubs package (package-stubs) when extracting docstrings.
- **`force_inspection`** (`bool`) – Whether to force using dynamic analysis when loading data.
- **`group_by_category`** (`bool`) – Group the object's children by categories: attributes, classes, functions, and modules.
- **`heading`** (`str`) – A custom string to override the autogenerated heading of the root object.
- **`heading_level`** (`int`) – The initial heading level to use.
- **`inheritance_diagram_direction`** (`Literal['TB', 'TD', 'BT', 'RL', 'LR']`) – The direction of the Mermaid chart presenting the inheritance diagram of a class.
- **`inherited_members`** (`bool | list[str]`) – A boolean, or an explicit list of inherited members to render.
- **`line_length`** (`int`) – Maximum line length when formatting code/signatures.
- **`members`** (`list[str] | bool | None`) – A boolean, or an explicit list of members to render.
- **`members_order`** (`Order | list[Order]`) – The members ordering to use.
- **`merge_init_into_class`** (`bool`) – Whether to merge the __init__ method into the class' signature and docstring.
- **`modernize_annotations`** (`bool`) – Whether to modernize annotations, for example Optional[str] into str | None.
- **`overloads_only`** (`bool`) – Whether to hide the implementation signature if the overloads are shown.
- **`parameter_headings`** (`bool`) – Whether to render headings for parameters (therefore showing parameters in the ToC).
- **`preload_modules`** (`list[str]`) – Pre-load modules that are not specified directly in autodoc instructions (::: identifier).
- **`relative_crossrefs`** (`bool`) – Whether to enable the relative crossref syntax.
- **`scoped_crossrefs`** (`bool`) – Whether to enable the scoped crossref ability.
- **`separate_signature`** (`bool`) – Whether to put the whole signature in a code block below the heading.
- **`show_attribute_values`** (`bool`) – Show initial values of attributes in classes.
- **`show_bases`** (`bool`) – Show the base classes of a class.
- **`show_category_heading`** (`bool`) – When grouped by categories, show a heading for each category.
- **`show_docstring_attributes`** (`bool`) – Whether to display the 'Attributes' section in the object's docstring.
- **`show_docstring_classes`** (`bool`) – Whether to display the 'Classes' section in the object's docstring.
- **`show_docstring_description`** (`bool`) – Whether to display the textual block (including admonitions) in the object's docstring.
- **`show_docstring_examples`** (`bool`) – Whether to display the 'Examples' section in the object's docstring.
- **`show_docstring_functions`** (`bool`) – Whether to display the 'Functions' or 'Methods' sections in the object's docstring.
- **`show_docstring_modules`** (`bool`) – Whether to display the 'Modules' section in the object's docstring.
- **`show_docstring_other_parameters`** (`bool`) – Whether to display the 'Other Parameters' section in the object's docstring.
- **`show_docstring_parameters`** (`bool`) – Whether to display the 'Parameters' section in the object's docstring.
- **`show_docstring_raises`** (`bool`) – Whether to display the 'Raises' section in the object's docstring.
- **`show_docstring_receives`** (`bool`) – Whether to display the 'Receives' section in the object's docstring.
- **`show_docstring_returns`** (`bool`) – Whether to display the 'Returns' section in the object's docstring.
- **`show_docstring_type_aliases`** (`bool`) – Whether to display the 'Type Aliases' section in the object's docstring.
- **`show_docstring_type_parameters`** (`bool`) – Whether to display the 'Type Parameters' section in the object's docstring.
- **`show_docstring_warns`** (`bool`) – Whether to display the 'Warns' section in the object's docstring.
- **`show_docstring_yields`** (`bool`) – Whether to display the 'Yields' section in the object's docstring.
- **`show_if_no_docstring`** (`bool`) – Show the object heading even if it has no docstring or children with docstrings.
- **`show_inheritance_diagram`** (`bool`) – Show the inheritance diagram of a class using Mermaid.
- **`show_labels`** (`bool`) – Whether to show labels of the members.
- **`show_object_full_path`** (`bool`) – Show the full Python path of every object.
- **`show_overloads`** (`bool`) – Show the overloads of a function or method.
- **`show_root_full_path`** (`bool`) – Show the full Python path for the root object heading.
- **`show_root_heading`** (`bool`) – Show the heading of the object at the root of the documentation tree.
- **`show_root_members_full_path`** (`bool`) – Show the full Python path of the root members.
- **`show_root_toc_entry`** (`bool`) – If the root heading is not shown, at least add a ToC entry for it.
- **`show_signature`** (`bool`) – Show methods and functions signatures.
- **`show_signature_annotations`** (`bool`) – Show the type annotations in methods and functions signatures.
- **`show_signature_type_parameters`** (`bool`) – Show the type parameters in generic classes, methods, functions and type aliases signatures.
- **`show_source`** (`bool`) – Show the source code of this object.
- **`show_submodules`** (`bool`) – When rendering a module, show its submodules recursively.
- **`show_symbol_type_heading`** (`bool`) – Show the symbol type in headings (e.g. mod, class, meth, func and attr).
- **`show_symbol_type_toc`** (`bool`) – Show the symbol type in the Table of Contents (e.g. mod, class, methd, func and attr).
- **`signature_crossrefs`** (`bool`) – Whether to render cross-references for type annotations in signatures.
- **`skip_local_inventory`** (`bool`) – Whether to prevent objects from being registered in the local objects inventory.
- **`summary`** (`bool | SummaryOption`) – Whether to render summaries of modules, classes, functions (methods) and attributes.
- **`toc_label`** (`str`) – A custom string to override the autogenerated toc label of the root object.
- **`type_parameter_headings`** (`bool`) – Whether to render headings for type parameters (therefore showing type parameters in the ToC).
- **`unwrap_annotated`** (`bool`) – Whether to unwrap Annotated types to show only the type without the annotations.

### allow_inspection

```python
allow_inspection: bool = True
```

Whether to allow inspecting modules when visiting them is not possible.

### annotations_path

```python
annotations_path: Literal['brief', 'source', 'full'] = 'brief'
```

The verbosity for annotations path: `brief` (recommended), `source` (as written in the source), or `full`.

### backlinks

```python
backlinks: Literal['flat', 'tree', False] = False
```

Whether to render backlinks, and how.

### docstring_options

```python
docstring_options: (
    GoogleStyleOptions
    | NumpyStyleOptions
    | SphinxStyleOptions
    | AutoStyleOptions
    | None
) = None
```

The options for the docstring parser.

See [docstring parsers](https://mkdocstrings.github.io/griffe/reference/docstrings/) and their options in Griffe docs.

### docstring_section_style

```python
docstring_section_style: Literal['table', 'list', 'spacy'] = 'table'
```

The style used to render docstring sections.

### docstring_style

```python
docstring_style: Literal['auto', 'google', 'numpy', 'sphinx'] | None = 'google'
```

The docstring style to use: `auto`, `google`, `numpy`, `sphinx`, or `None`.

### extensions

```python
extensions: list[str | dict[str, Any]] = field(default_factory=list)
```

A list of Griffe extensions to load.

### extra

```python
extra: dict[str, Any] = field(default_factory=dict)
```

Extra options.

### filters

```python
filters: list[str] | Literal['public'] = field(default_factory=lambda: copy())
```

A list of filters, or `"public"`.

**List of filters**

A filter starting with `!` will exclude matching objects instead of including them. The `members` option takes precedence over `filters` (filters will still be applied recursively to lower members in the hierarchy).

**Filtering methods**

[Sponsors only](../../insiders/) — [Insiders 1.11.0](../../insiders/changelog/#1.11.0)

The `public` method will include only public objects: those added to `__all__` or not starting with an underscore (except for special methods/attributes).

### find_stubs_package

```python
find_stubs_package: bool = False
```

Whether to load stubs package (package-stubs) when extracting docstrings.

### force_inspection

```python
force_inspection: bool = False
```

Whether to force using dynamic analysis when loading data.

### group_by_category

```python
group_by_category: bool = True
```

Group the object's children by categories: attributes, classes, functions, and modules.

### heading

```python
heading: str = ''
```

A custom string to override the autogenerated heading of the root object.

### heading_level

```python
heading_level: int = 2
```

The initial heading level to use.

### inheritance_diagram_direction

```python
inheritance_diagram_direction: Literal['TB', 'TD', 'BT', 'RL', 'LR'] = 'TD'
```

The direction of the Mermaid chart presenting the inheritance diagram of a class.

### inherited_members

```python
inherited_members: bool | list[str] = False
```

A boolean, or an explicit list of inherited members to render.

If true, select all inherited members, which can then be filtered with `members`. If false or empty list, do not select any inherited member.

### line_length

```python
line_length: int = 60
```

Maximum line length when formatting code/signatures.

### members

```python
members: list[str] | bool | None = None
```

A boolean, or an explicit list of members to render.

If true, select all members without further filtering. If false or empty list, do not render members. If none, select all members and apply further filtering with filters and docstrings.

### members_order

```python
members_order: Order | list[Order] = 'alphabetical'
```

The members ordering to use.

- `__all__`: order members according to `__all__` module attributes, if declared;
- `alphabetical`: order members alphabetically;
- `source`: order members as they appear in the source file.

Since `__all__` is a module-only attribute, it can't be used to sort class members, therefore the `members_order` option accepts a list of ordering methods, indicating ordering preferences.

### merge_init_into_class

```python
merge_init_into_class: bool = False
```

Whether to merge the `__init__` method into the class' signature and docstring.

### modernize_annotations

```python
modernize_annotations: bool = False
```

Whether to modernize annotations, for example `Optional[str]` into `str | None`.

### overloads_only

```python
overloads_only: bool = False
```

Whether to hide the implementation signature if the overloads are shown.

### parameter_headings

```python
parameter_headings: bool = False
```

Whether to render headings for parameters (therefore showing parameters in the ToC).

### preload_modules

```python
preload_modules: list[str] = field(default_factory=list)
```

Pre-load modules that are not specified directly in autodoc instructions (`::: identifier`).

It is useful when you want to render documentation for a particular member of an object, and this member is imported from another package than its parent.

For an imported member to be rendered, you need to add it to the `__all__` attribute of the importing module.

The modules must be listed as an array of strings.

### relative_crossrefs

```python
relative_crossrefs: bool = False
```

Whether to enable the relative crossref syntax.

### scoped_crossrefs

```python
scoped_crossrefs: bool = False
```

Whether to enable the scoped crossref ability.

### separate_signature

```python
separate_signature: bool = False
```

Whether to put the whole signature in a code block below the heading.

If Black or Ruff are installed, the signature is also formatted using them.

### show_attribute_values

```python
show_attribute_values: bool = True
```

Show initial values of attributes in classes.

### show_bases

```python
show_bases: bool = True
```

Show the base classes of a class.

### show_category_heading

```python
show_category_heading: bool = False
```

When grouped by categories, show a heading for each category.

### show_docstring_attributes

```python
show_docstring_attributes: bool = True
```

Whether to display the 'Attributes' section in the object's docstring.

### show_docstring_classes

```python
show_docstring_classes: bool = True
```

Whether to display the 'Classes' section in the object's docstring.

### show_docstring_description

```python
show_docstring_description: bool = True
```

Whether to display the textual block (including admonitions) in the object's docstring.

### show_docstring_examples

```python
show_docstring_examples: bool = True
```

Whether to display the 'Examples' section in the object's docstring.

### show_docstring_functions

```python
show_docstring_functions: bool = True
```

Whether to display the 'Functions' or 'Methods' sections in the object's docstring.

### show_docstring_modules

```python
show_docstring_modules: bool = True
```

Whether to display the 'Modules' section in the object's docstring.

### show_docstring_other_parameters

```python
show_docstring_other_parameters: bool = True
```

Whether to display the 'Other Parameters' section in the object's docstring.

### show_docstring_parameters

```python
show_docstring_parameters: bool = True
```

Whether to display the 'Parameters' section in the object's docstring.

### show_docstring_raises

```python
show_docstring_raises: bool = True
```

Whether to display the 'Raises' section in the object's docstring.

### show_docstring_receives

```python
show_docstring_receives: bool = True
```

Whether to display the 'Receives' section in the object's docstring.

### show_docstring_returns

```python
show_docstring_returns: bool = True
```

Whether to display the 'Returns' section in the object's docstring.

### show_docstring_type_aliases

```python
show_docstring_type_aliases: bool = True
```

Whether to display the 'Type Aliases' section in the object's docstring.

### show_docstring_type_parameters

```python
show_docstring_type_parameters: bool = True
```

Whether to display the 'Type Parameters' section in the object's docstring.

### show_docstring_warns

```python
show_docstring_warns: bool = True
```

Whether to display the 'Warns' section in the object's docstring.

### show_docstring_yields

```python
show_docstring_yields: bool = True
```

Whether to display the 'Yields' section in the object's docstring.

### show_if_no_docstring

```python
show_if_no_docstring: bool = False
```

Show the object heading even if it has no docstring or children with docstrings.

### show_inheritance_diagram

```python
show_inheritance_diagram: bool = False
```

Show the inheritance diagram of a class using Mermaid.

### show_labels

```python
show_labels: bool = True
```

Whether to show labels of the members.

### show_object_full_path

```python
show_object_full_path: bool = False
```

Show the full Python path of every object.

### show_overloads

```python
show_overloads: bool = True
```

Show the overloads of a function or method.

### show_root_full_path

```python
show_root_full_path: bool = True
```

Show the full Python path for the root object heading.

### show_root_heading

```python
show_root_heading: bool = False
```

Show the heading of the object at the root of the documentation tree.

The root object is the object referenced by the identifier after `:::`.

### show_root_members_full_path

```python
show_root_members_full_path: bool = False
```

Show the full Python path of the root members.

### show_root_toc_entry

```python
show_root_toc_entry: bool = True
```

If the root heading is not shown, at least add a ToC entry for it.

### show_signature

```python
show_signature: bool = True
```

Show methods and functions signatures.

### show_signature_annotations

```python
show_signature_annotations: bool = False
```

Show the type annotations in methods and functions signatures.

### show_signature_type_parameters

```python
show_signature_type_parameters: bool = False
```

Show the type parameters in generic classes, methods, functions and type aliases signatures.

### show_source

```python
show_source: bool = True
```

Show the source code of this object.

### show_submodules

```python
show_submodules: bool = False
```

When rendering a module, show its submodules recursively.

### show_symbol_type_heading

```python
show_symbol_type_heading: bool = False
```

Show the symbol type in headings (e.g. mod, class, meth, func and attr).

### show_symbol_type_toc

```python
show_symbol_type_toc: bool = False
```

Show the symbol type in the Table of Contents (e.g. mod, class, methd, func and attr).

### signature_crossrefs

```python
signature_crossrefs: bool = False
```

Whether to render cross-references for type annotations in signatures.

### skip_local_inventory

```python
skip_local_inventory: bool = False
```

Whether to prevent objects from being registered in the local objects inventory.

### summary

```python
summary: bool | SummaryOption = field(default_factory=SummaryOption)
```

Whether to render summaries of modules, classes, functions (methods) and attributes.

### toc_label

```python
toc_label: str = ''
```

A custom string to override the autogenerated toc label of the root object.

### type_parameter_headings

```python
type_parameter_headings: bool = False
```

Whether to render headings for type parameters (therefore showing type parameters in the ToC).

### unwrap_annotated

```python
unwrap_annotated: bool = False
```

Whether to unwrap `Annotated` types to show only the type without the annotations.

### coerce

```python
coerce(**data: Any) -> MutableMapping[str, Any]
```

Coerce data.

### from_data

```python
from_data(**data: Any) -> Self
```

Create an instance from a dictionary.

## PythonOptions

```python
PythonOptions(
    allow_inspection: bool = True,
    force_inspection: bool = False,
    annotations_path: Literal["brief", "source", "full"] = "brief",
    backlinks: Literal["flat", "tree", False] = False,
    docstring_options: (
        GoogleStyleOptions
        | NumpyStyleOptions
        | SphinxStyleOptions
        | AutoStyleOptions
        | None
    ) = None,
    docstring_section_style: Literal["table", "list", "spacy"] = "table",
    docstring_style: Literal["auto", "google", "numpy", "sphinx"] | None = "google",
    extensions: list[str | dict[str, Any]] = list(),
    filters: list[tuple[Pattern, bool]] | Literal["public"] = (
        lambda: [
            (compile(removeprefix("!")), startswith("!")) for filtr in _DEFAULT_FILTERS
        ]
    )(),
    find_stubs_package: bool = False,
    group_by_category: bool = True,
    heading: str = "",
    heading_level: int = 2,
    inheritance_diagram_direction: Literal["TB", "TD", "BT", "RL", "LR"] = "TD",
    inherited_members: bool | list[str] = False,
    line_length: int = 60,
    members: list[str] | bool | None = None,
    members_order: Order | list[Order] = "alphabetical",
    merge_init_into_class: bool = False,
    modernize_annotations: bool = False,
    overloads_only: bool = False,
    parameter_headings: bool = False,
    preload_modules: list[str] = list(),
    relative_crossrefs: bool = False,
    scoped_crossrefs: bool = False,
    show_overloads: bool = True,
    separate_signature: bool = False,
    show_attribute_values: bool = True,
    show_bases: bool = True,
    show_category_heading: bool = False,
    show_docstring_attributes: bool = True,
    show_docstring_classes: bool = True,
    show_docstring_description: bool = True,
    show_docstring_examples: bool = True,
    show_docstring_functions: bool = True,
    show_docstring_modules: bool = True,
    show_docstring_other_parameters: bool = True,
    show_docstring_parameters: bool = True,
    show_docstring_raises: bool = True,
    show_docstring_receives: bool = True,
    show_docstring_returns: bool = True,
    show_docstring_type_aliases: bool = True,
    show_docstring_type_parameters: bool = True,
    show_docstring_warns: bool = True,
    show_docstring_yields: bool = True,
    show_if_no_docstring: bool = False,
    show_inheritance_diagram: bool = False,
    show_labels: bool = True,
    show_object_full_path: bool = False,
    show_root_full_path: bool = True,
    show_root_heading: bool = False,
    show_root_members_full_path: bool = False,
    show_root_toc_entry: bool = True,
    show_signature_annotations: bool = False,
    show_signature_type_parameters: bool = False,
    show_signature: bool = True,
    show_source: bool = True,
    show_submodules: bool = False,
    show_symbol_type_heading: bool = False,
    show_symbol_type_toc: bool = False,
    skip_local_inventory: bool = False,
    signature_crossrefs: bool = False,
    summary: SummaryOption = SummaryOption(),
    toc_label: str = "",
    type_parameter_headings: bool = False,
    unwrap_annotated: bool = False,
    extra: dict[str, Any] = dict(),
)
```

```
              flowchart TD
              mkdocstrings_handlers.python.PythonOptions[PythonOptions]
              mkdocstrings_handlers.python._internal.config.PythonInputOptions[PythonInputOptions]

                              mkdocstrings_handlers.python._internal.config.PythonInputOptions --> mkdocstrings_handlers.python.PythonOptions
                


              click mkdocstrings_handlers.python.PythonOptions href "" "mkdocstrings_handlers.python.PythonOptions"
              click mkdocstrings_handlers.python._internal.config.PythonInputOptions href "" "mkdocstrings_handlers.python._internal.config.PythonInputOptions"
```

Final options passed as template context.

Methods:

- **`coerce`** – Create an instance from a dictionary.
- **`from_data`** – Create an instance from a dictionary.

Attributes:

- **`allow_inspection`** (`bool`) – Whether to allow inspecting modules when visiting them is not possible.
- **`annotations_path`** (`Literal['brief', 'source', 'full']`) – The verbosity for annotations path: brief (recommended), source (as written in the source), or full.
- **`backlinks`** (`Literal['flat', 'tree', False]`) – Whether to render backlinks, and how.
- **`docstring_options`** (`GoogleStyleOptions | NumpyStyleOptions | SphinxStyleOptions | AutoStyleOptions | None`) – The options for the docstring parser.
- **`docstring_section_style`** (`Literal['table', 'list', 'spacy']`) – The style used to render docstring sections.
- **`docstring_style`** (`Literal['auto', 'google', 'numpy', 'sphinx'] | None`) – The docstring style to use: auto, google, numpy, sphinx, or None.
- **`extensions`** (`list[str | dict[str, Any]]`) – A list of Griffe extensions to load.
- **`extra`** (`dict[str, Any]`) – Extra options.
- **`filters`** (`list[tuple[Pattern, bool]] | Literal['public']`) – A list of filters, or "public".
- **`find_stubs_package`** (`bool`) – Whether to load stubs package (package-stubs) when extracting docstrings.
- **`force_inspection`** (`bool`) – Whether to force using dynamic analysis when loading data.
- **`group_by_category`** (`bool`) – Group the object's children by categories: attributes, classes, functions, and modules.
- **`heading`** (`str`) – A custom string to override the autogenerated heading of the root object.
- **`heading_level`** (`int`) – The initial heading level to use.
- **`inheritance_diagram_direction`** (`Literal['TB', 'TD', 'BT', 'RL', 'LR']`) – The direction of the Mermaid chart presenting the inheritance diagram of a class.
- **`inherited_members`** (`bool | list[str]`) – A boolean, or an explicit list of inherited members to render.
- **`line_length`** (`int`) – Maximum line length when formatting code/signatures.
- **`members`** (`list[str] | bool | None`) – A boolean, or an explicit list of members to render.
- **`members_order`** (`Order | list[Order]`) – The members ordering to use.
- **`merge_init_into_class`** (`bool`) – Whether to merge the __init__ method into the class' signature and docstring.
- **`modernize_annotations`** (`bool`) – Whether to modernize annotations, for example Optional[str] into str | None.
- **`overloads_only`** (`bool`) – Whether to hide the implementation signature if the overloads are shown.
- **`parameter_headings`** (`bool`) – Whether to render headings for parameters (therefore showing parameters in the ToC).
- **`preload_modules`** (`list[str]`) – Pre-load modules that are not specified directly in autodoc instructions (::: identifier).
- **`relative_crossrefs`** (`bool`) – Whether to enable the relative crossref syntax.
- **`scoped_crossrefs`** (`bool`) – Whether to enable the scoped crossref ability.
- **`separate_signature`** (`bool`) – Whether to put the whole signature in a code block below the heading.
- **`show_attribute_values`** (`bool`) – Show initial values of attributes in classes.
- **`show_bases`** (`bool`) – Show the base classes of a class.
- **`show_category_heading`** (`bool`) – When grouped by categories, show a heading for each category.
- **`show_docstring_attributes`** (`bool`) – Whether to display the 'Attributes' section in the object's docstring.
- **`show_docstring_classes`** (`bool`) – Whether to display the 'Classes' section in the object's docstring.
- **`show_docstring_description`** (`bool`) – Whether to display the textual block (including admonitions) in the object's docstring.
- **`show_docstring_examples`** (`bool`) – Whether to display the 'Examples' section in the object's docstring.
- **`show_docstring_functions`** (`bool`) – Whether to display the 'Functions' or 'Methods' sections in the object's docstring.
- **`show_docstring_modules`** (`bool`) – Whether to display the 'Modules' section in the object's docstring.
- **`show_docstring_other_parameters`** (`bool`) – Whether to display the 'Other Parameters' section in the object's docstring.
- **`show_docstring_parameters`** (`bool`) – Whether to display the 'Parameters' section in the object's docstring.
- **`show_docstring_raises`** (`bool`) – Whether to display the 'Raises' section in the object's docstring.
- **`show_docstring_receives`** (`bool`) – Whether to display the 'Receives' section in the object's docstring.
- **`show_docstring_returns`** (`bool`) – Whether to display the 'Returns' section in the object's docstring.
- **`show_docstring_type_aliases`** (`bool`) – Whether to display the 'Type Aliases' section in the object's docstring.
- **`show_docstring_type_parameters`** (`bool`) – Whether to display the 'Type Parameters' section in the object's docstring.
- **`show_docstring_warns`** (`bool`) – Whether to display the 'Warns' section in the object's docstring.
- **`show_docstring_yields`** (`bool`) – Whether to display the 'Yields' section in the object's docstring.
- **`show_if_no_docstring`** (`bool`) – Show the object heading even if it has no docstring or children with docstrings.
- **`show_inheritance_diagram`** (`bool`) – Show the inheritance diagram of a class using Mermaid.
- **`show_labels`** (`bool`) – Whether to show labels of the members.
- **`show_object_full_path`** (`bool`) – Show the full Python path of every object.
- **`show_overloads`** (`bool`) – Show the overloads of a function or method.
- **`show_root_full_path`** (`bool`) – Show the full Python path for the root object heading.
- **`show_root_heading`** (`bool`) – Show the heading of the object at the root of the documentation tree.
- **`show_root_members_full_path`** (`bool`) – Show the full Python path of the root members.
- **`show_root_toc_entry`** (`bool`) – If the root heading is not shown, at least add a ToC entry for it.
- **`show_signature`** (`bool`) – Show methods and functions signatures.
- **`show_signature_annotations`** (`bool`) – Show the type annotations in methods and functions signatures.
- **`show_signature_type_parameters`** (`bool`) – Show the type parameters in generic classes, methods, functions and type aliases signatures.
- **`show_source`** (`bool`) – Show the source code of this object.
- **`show_submodules`** (`bool`) – When rendering a module, show its submodules recursively.
- **`show_symbol_type_heading`** (`bool`) – Show the symbol type in headings (e.g. mod, class, meth, func and attr).
- **`show_symbol_type_toc`** (`bool`) – Show the symbol type in the Table of Contents (e.g. mod, class, methd, func and attr).
- **`signature_crossrefs`** (`bool`) – Whether to render cross-references for type annotations in signatures.
- **`skip_local_inventory`** (`bool`) – Whether to prevent objects from being registered in the local objects inventory.
- **`summary`** (`SummaryOption`) – Whether to render summaries of modules, classes, functions (methods), attributes and type aliases.
- **`toc_label`** (`str`) – A custom string to override the autogenerated toc label of the root object.
- **`type_parameter_headings`** (`bool`) – Whether to render headings for type parameters (therefore showing type parameters in the ToC).
- **`unwrap_annotated`** (`bool`) – Whether to unwrap Annotated types to show only the type without the annotations.

### allow_inspection

```python
allow_inspection: bool = True
```

Whether to allow inspecting modules when visiting them is not possible.

### annotations_path

```python
annotations_path: Literal['brief', 'source', 'full'] = 'brief'
```

The verbosity for annotations path: `brief` (recommended), `source` (as written in the source), or `full`.

### backlinks

```python
backlinks: Literal['flat', 'tree', False] = False
```

Whether to render backlinks, and how.

### docstring_options

```python
docstring_options: (
    GoogleStyleOptions
    | NumpyStyleOptions
    | SphinxStyleOptions
    | AutoStyleOptions
    | None
) = None
```

The options for the docstring parser.

See [docstring parsers](https://mkdocstrings.github.io/griffe/reference/docstrings/) and their options in Griffe docs.

### docstring_section_style

```python
docstring_section_style: Literal['table', 'list', 'spacy'] = 'table'
```

The style used to render docstring sections.

### docstring_style

```python
docstring_style: Literal['auto', 'google', 'numpy', 'sphinx'] | None = 'google'
```

The docstring style to use: `auto`, `google`, `numpy`, `sphinx`, or `None`.

### extensions

```python
extensions: list[str | dict[str, Any]] = field(default_factory=list)
```

A list of Griffe extensions to load.

### extra

```python
extra: dict[str, Any] = field(default_factory=dict)
```

Extra options.

### filters

```python
filters: list[tuple[Pattern, bool]] | Literal["public"] = field(
    default_factory=lambda: [
        (compile(removeprefix("!")), startswith("!")) for filtr in _DEFAULT_FILTERS
    ]
)
```

A list of filters, or `"public"`.

### find_stubs_package

```python
find_stubs_package: bool = False
```

Whether to load stubs package (package-stubs) when extracting docstrings.

### force_inspection

```python
force_inspection: bool = False
```

Whether to force using dynamic analysis when loading data.

### group_by_category

```python
group_by_category: bool = True
```

Group the object's children by categories: attributes, classes, functions, and modules.

### heading

```python
heading: str = ''
```

A custom string to override the autogenerated heading of the root object.

### heading_level

```python
heading_level: int = 2
```

The initial heading level to use.

### inheritance_diagram_direction

```python
inheritance_diagram_direction: Literal['TB', 'TD', 'BT', 'RL', 'LR'] = 'TD'
```

The direction of the Mermaid chart presenting the inheritance diagram of a class.

### inherited_members

```python
inherited_members: bool | list[str] = False
```

A boolean, or an explicit list of inherited members to render.

If true, select all inherited members, which can then be filtered with `members`. If false or empty list, do not select any inherited member.

### line_length

```python
line_length: int = 60
```

Maximum line length when formatting code/signatures.

### members

```python
members: list[str] | bool | None = None
```

A boolean, or an explicit list of members to render.

If true, select all members without further filtering. If false or empty list, do not render members. If none, select all members and apply further filtering with filters and docstrings.

### members_order

```python
members_order: Order | list[Order] = 'alphabetical'
```

The members ordering to use.

- `__all__`: order members according to `__all__` module attributes, if declared;
- `alphabetical`: order members alphabetically;
- `source`: order members as they appear in the source file.

Since `__all__` is a module-only attribute, it can't be used to sort class members, therefore the `members_order` option accepts a list of ordering methods, indicating ordering preferences.

### merge_init_into_class

```python
merge_init_into_class: bool = False
```

Whether to merge the `__init__` method into the class' signature and docstring.

### modernize_annotations

```python
modernize_annotations: bool = False
```

Whether to modernize annotations, for example `Optional[str]` into `str | None`.

### overloads_only

```python
overloads_only: bool = False
```

Whether to hide the implementation signature if the overloads are shown.

### parameter_headings

```python
parameter_headings: bool = False
```

Whether to render headings for parameters (therefore showing parameters in the ToC).

### preload_modules

```python
preload_modules: list[str] = field(default_factory=list)
```

Pre-load modules that are not specified directly in autodoc instructions (`::: identifier`).

It is useful when you want to render documentation for a particular member of an object, and this member is imported from another package than its parent.

For an imported member to be rendered, you need to add it to the `__all__` attribute of the importing module.

The modules must be listed as an array of strings.

### relative_crossrefs

```python
relative_crossrefs: bool = False
```

Whether to enable the relative crossref syntax.

### scoped_crossrefs

```python
scoped_crossrefs: bool = False
```

Whether to enable the scoped crossref ability.

### separate_signature

```python
separate_signature: bool = False
```

Whether to put the whole signature in a code block below the heading.

If Black or Ruff are installed, the signature is also formatted using them.

### show_attribute_values

```python
show_attribute_values: bool = True
```

Show initial values of attributes in classes.

### show_bases

```python
show_bases: bool = True
```

Show the base classes of a class.

### show_category_heading

```python
show_category_heading: bool = False
```

When grouped by categories, show a heading for each category.

### show_docstring_attributes

```python
show_docstring_attributes: bool = True
```

Whether to display the 'Attributes' section in the object's docstring.

### show_docstring_classes

```python
show_docstring_classes: bool = True
```

Whether to display the 'Classes' section in the object's docstring.

### show_docstring_description

```python
show_docstring_description: bool = True
```

Whether to display the textual block (including admonitions) in the object's docstring.

### show_docstring_examples

```python
show_docstring_examples: bool = True
```

Whether to display the 'Examples' section in the object's docstring.

### show_docstring_functions

```python
show_docstring_functions: bool = True
```

Whether to display the 'Functions' or 'Methods' sections in the object's docstring.

### show_docstring_modules

```python
show_docstring_modules: bool = True
```

Whether to display the 'Modules' section in the object's docstring.

### show_docstring_other_parameters

```python
show_docstring_other_parameters: bool = True
```

Whether to display the 'Other Parameters' section in the object's docstring.

### show_docstring_parameters

```python
show_docstring_parameters: bool = True
```

Whether to display the 'Parameters' section in the object's docstring.

### show_docstring_raises

```python
show_docstring_raises: bool = True
```

Whether to display the 'Raises' section in the object's docstring.

### show_docstring_receives

```python
show_docstring_receives: bool = True
```

Whether to display the 'Receives' section in the object's docstring.

### show_docstring_returns

```python
show_docstring_returns: bool = True
```

Whether to display the 'Returns' section in the object's docstring.

### show_docstring_type_aliases

```python
show_docstring_type_aliases: bool = True
```

Whether to display the 'Type Aliases' section in the object's docstring.

### show_docstring_type_parameters

```python
show_docstring_type_parameters: bool = True
```

Whether to display the 'Type Parameters' section in the object's docstring.

### show_docstring_warns

```python
show_docstring_warns: bool = True
```

Whether to display the 'Warns' section in the object's docstring.

### show_docstring_yields

```python
show_docstring_yields: bool = True
```

Whether to display the 'Yields' section in the object's docstring.

### show_if_no_docstring

```python
show_if_no_docstring: bool = False
```

Show the object heading even if it has no docstring or children with docstrings.

### show_inheritance_diagram

```python
show_inheritance_diagram: bool = False
```

Show the inheritance diagram of a class using Mermaid.

### show_labels

```python
show_labels: bool = True
```

Whether to show labels of the members.

### show_object_full_path

```python
show_object_full_path: bool = False
```

Show the full Python path of every object.

### show_overloads

```python
show_overloads: bool = True
```

Show the overloads of a function or method.

### show_root_full_path

```python
show_root_full_path: bool = True
```

Show the full Python path for the root object heading.

### show_root_heading

```python
show_root_heading: bool = False
```

Show the heading of the object at the root of the documentation tree.

The root object is the object referenced by the identifier after `:::`.

### show_root_members_full_path

```python
show_root_members_full_path: bool = False
```

Show the full Python path of the root members.

### show_root_toc_entry

```python
show_root_toc_entry: bool = True
```

If the root heading is not shown, at least add a ToC entry for it.

### show_signature

```python
show_signature: bool = True
```

Show methods and functions signatures.

### show_signature_annotations

```python
show_signature_annotations: bool = False
```

Show the type annotations in methods and functions signatures.

### show_signature_type_parameters

```python
show_signature_type_parameters: bool = False
```

Show the type parameters in generic classes, methods, functions and type aliases signatures.

### show_source

```python
show_source: bool = True
```

Show the source code of this object.

### show_submodules

```python
show_submodules: bool = False
```

When rendering a module, show its submodules recursively.

### show_symbol_type_heading

```python
show_symbol_type_heading: bool = False
```

Show the symbol type in headings (e.g. mod, class, meth, func and attr).

### show_symbol_type_toc

```python
show_symbol_type_toc: bool = False
```

Show the symbol type in the Table of Contents (e.g. mod, class, methd, func and attr).

### signature_crossrefs

```python
signature_crossrefs: bool = False
```

Whether to render cross-references for type annotations in signatures.

### skip_local_inventory

```python
skip_local_inventory: bool = False
```

Whether to prevent objects from being registered in the local objects inventory.

### summary

```python
summary: SummaryOption = field(default_factory=SummaryOption)
```

Whether to render summaries of modules, classes, functions (methods), attributes and type aliases.

### toc_label

```python
toc_label: str = ''
```

A custom string to override the autogenerated toc label of the root object.

### type_parameter_headings

```python
type_parameter_headings: bool = False
```

Whether to render headings for type parameters (therefore showing type parameters in the ToC).

### unwrap_annotated

```python
unwrap_annotated: bool = False
```

Whether to unwrap `Annotated` types to show only the type without the annotations.

### coerce

```python
coerce(**data: Any) -> MutableMapping[str, Any]
```

Create an instance from a dictionary.

### from_data

```python
from_data(**data: Any) -> Self
```

Create an instance from a dictionary.

## SphinxStyleOptions

```python
SphinxStyleOptions(
    warn_unknown_params: bool = True,
    warn_missing_types: bool = True,
    warnings: bool = True,
)
```

Sphinx style docstring options.

Attributes:

- **`warn_missing_types`** (`bool`) – Warn about missing type/annotation for return values.
- **`warn_unknown_params`** (`bool`) – Warn about documented parameters not appearing in the signature.
- **`warnings`** (`bool`) – Generally enable/disable warnings when parsing docstrings.

### warn_missing_types

```python
warn_missing_types: bool = True
```

Warn about missing type/annotation for return values.

### warn_unknown_params

```python
warn_unknown_params: bool = True
```

Warn about documented parameters not appearing in the signature.

### warnings

```python
warnings: bool = True
```

Generally enable/disable warnings when parsing docstrings.

## SummaryOption

```python
SummaryOption(
    attributes: bool = False,
    functions: bool = False,
    classes: bool = False,
    modules: bool = False,
    type_aliases: bool = False,
)
```

Summary option.

Attributes:

- **`attributes`** (`bool`) – Whether to render summaries of attributes.
- **`classes`** (`bool`) – Whether to render summaries of classes.
- **`functions`** (`bool`) – Whether to render summaries of functions (methods).
- **`modules`** (`bool`) – Whether to render summaries of modules.
- **`type_aliases`** (`bool`) – Whether to render summaries of type aliases.

### attributes

```python
attributes: bool = False
```

Whether to render summaries of attributes.

### classes

```python
classes: bool = False
```

Whether to render summaries of classes.

### functions

```python
functions: bool = False
```

Whether to render summaries of functions (methods).

### modules

```python
modules: bool = False
```

Whether to render summaries of modules.

### type_aliases

```python
type_aliases: bool = False
```

Whether to render summaries of type aliases.

## do_as_attributes_section

```python
do_as_attributes_section(
    context: Context, attributes: Sequence[Attribute], *, check_public: bool = True
) -> DocstringSectionAttributes
```

Build an attributes section from a list of attributes.

Parameters:

- ### **`attributes`**

  (`Sequence[Attribute]`) – The attributes to build the section from.

- ### **`check_public`**

  (`bool`, default: `True` ) – Whether to check if the attribute is public.

Returns:

- `DocstringSectionAttributes` – An attributes docstring section.

## do_as_classes_section

```python
do_as_classes_section(
    context: Context, classes: Sequence[Class], *, check_public: bool = True
) -> DocstringSectionClasses
```

Build a classes section from a list of classes.

Parameters:

- ### **`classes`**

  (`Sequence[Class]`) – The classes to build the section from.

- ### **`check_public`**

  (`bool`, default: `True` ) – Whether to check if the class is public.

Returns:

- `DocstringSectionClasses` – A classes docstring section.

## do_as_functions_section

```python
do_as_functions_section(
    context: Context, functions: Sequence[Function], *, check_public: bool = True
) -> DocstringSectionFunctions
```

Build a functions section from a list of functions.

Parameters:

- ### **`functions`**

  (`Sequence[Function]`) – The functions to build the section from.

- ### **`check_public`**

  (`bool`, default: `True` ) – Whether to check if the function is public.

Returns:

- `DocstringSectionFunctions` – A functions docstring section.

## do_as_modules_section

```python
do_as_modules_section(
    context: Context, modules: Sequence[Module], *, check_public: bool = True
) -> DocstringSectionModules
```

Build a modules section from a list of modules.

Parameters:

- ### **`modules`**

  (`Sequence[Module]`) – The modules to build the section from.

- ### **`check_public`**

  (`bool`, default: `True` ) – Whether to check if the module is public.

Returns:

- `DocstringSectionModules` – A modules docstring section.

## do_as_type_aliases_section

```python
do_as_type_aliases_section(
    context: Context, type_aliases: Sequence[TypeAlias], *, check_public: bool = True
) -> DocstringSectionTypeAliases
```

Build a type aliases section from a list of type aliases.

Parameters:

- ### **`type_aliases`**

  (`Sequence[TypeAlias]`) – The type aliases to build the section from.

- ### **`check_public`**

  (`bool`, default: `True` ) – Whether to check if the type_alias is public.

Returns:

- `DocstringSectionTypeAliases` – A type aliases docstring section.

## do_backlink_tree

```python
do_backlink_tree(backlinks: list[Backlink]) -> Tree[BacklinkCrumb]
```

Build a tree of backlinks.

Parameters:

- ### **`backlinks`**

  (`list[Backlink]`) – The list of backlinks.

Returns:

- `Tree[BacklinkCrumb]` – A tree of backlinks.

## do_crossref

```python
do_crossref(path: str, *, brief: bool = True) -> Markup
```

Deprecated. Filter to create cross-references.

Parameters:

- ### **`path`**

  (`str`) – The path to link to.

- ### **`brief`**

  (`bool`, default: `True` ) – Show only the last part of the path, add full path as hover.

Returns:

- `Markup` – Markup text.

## do_filter_objects

```python
do_filter_objects(
    objects_dictionary: dict[str, Object | Alias],
    *,
    filters: Sequence[tuple[Pattern, bool]] | Literal["public"] | None = None,
    members_list: bool | list[str] | None = None,
    inherited_members: bool | list[str] = False,
    keep_no_docstrings: bool = True
) -> list[Object | Alias]
```

Filter a dictionary of objects based on their docstrings.

Parameters:

- ### **`objects_dictionary`**

  (`dict[str, Object | Alias]`) – The dictionary of objects.

- ### **`filters`**

  (`Sequence[tuple[Pattern, bool]] | Literal['public'] | None`, default: `None` ) – Filters to apply, based on members' names, or "public". Each element is a tuple: a pattern, and a boolean indicating whether to reject the object if the pattern matches.

- ### **`members_list`**

  (`bool | list[str] | None`, default: `None` ) – An optional, explicit list of members to keep. When given and empty, return an empty list. When given and not empty, ignore filters and docstrings presence/absence.

- ### **`inherited_members`**

  (`bool | list[str]`, default: `False` ) – Whether to keep inherited members or exclude them.

- ### **`keep_no_docstrings`**

  (`bool`, default: `True` ) – Whether to keep objects with no/empty docstrings (recursive check).

Returns:

- `list[Object | Alias]` – A list of objects.

## do_format_attribute

```python
do_format_attribute(
    context: Context,
    attribute_path: Markup,
    attribute: Attribute,
    line_length: int,
    *,
    crossrefs: bool = False,
    show_value: bool = True
) -> str
```

Format an attribute.

Parameters:

- ### **`context`**

  (`Context`) – Jinja context, passed automatically.

- ### **`attribute_path`**

  (`Markup`) – The path of the callable we render the signature of.

- ### **`attribute`**

  (`Attribute`) – The attribute we render the signature of.

- ### **`line_length`**

  (`int`) – The line length.

- ### **`crossrefs`**

  (`bool`, default: `False` ) – Whether to cross-reference types in the signature.

Returns:

- `str` – The same code, formatted.

## do_format_code

```python
do_format_code(code: str, line_length: int) -> str
```

Format code.

Parameters:

- ### **`code`**

  (`str`) – The code to format.

- ### **`line_length`**

  (`int`) – The line length.

Returns:

- `str` – The same code, formatted.

## do_format_signature

```python
do_format_signature(
    context: Context,
    callable_path: Markup,
    function: Function,
    line_length: int,
    *,
    annotations: bool | None = None,
    crossrefs: bool = False
) -> str
```

Format a signature.

Parameters:

- ### **`context`**

  (`Context`) – Jinja context, passed automatically.

- ### **`callable_path`**

  (`Markup`) – The path of the callable we render the signature of.

- ### **`function`**

  (`Function`) – The function we render the signature of.

- ### **`line_length`**

  (`int`) – The line length.

- ### **`annotations`**

  (`bool | None`, default: `None` ) – Whether to show type annotations.

- ### **`crossrefs`**

  (`bool`, default: `False` ) – Whether to cross-reference types in the signature.

Returns:

- `str` – The same code, formatted.

## do_format_type_alias

```python
do_format_type_alias(
    context: Context,
    type_alias_path: Markup,
    type_alias: TypeAlias,
    line_length: int,
    *,
    crossrefs: bool = False
) -> str
```

Format a type alias.

Parameters:

- ### **`context`**

  (`Context`) – Jinja context, passed automatically.

- ### **`type_alias_path`**

  (`Markup`) – The path of the type alias we render the signature of.

- ### **`type_alias`**

  (`TypeAlias`) – The type alias we render the signature of.

- ### **`line_length`**

  (`int`) – The line length.

- ### **`crossrefs`**

  (`bool`, default: `False` ) – Whether to cross-reference types in the signature.

Returns:

- `str` – The same code, formatted.

## do_get_template

```python
do_get_template(env: Environment, obj: str | Object) -> str
```

Get the template name used to render an object.

Parameters:

- ### **`env`**

  (`Environment`) – The Jinja environment, passed automatically.

- ### **`obj`**

  (`str | Object`) – A Griffe object, or a template name.

Returns:

- `str` – A template name.

## do_multi_crossref

```python
do_multi_crossref(text: str, *, code: bool = True) -> Markup
```

Deprecated. Filter to create cross-references.

Parameters:

- ### **`text`**

  (`str`) – The text to scan.

- ### **`code`**

  (`bool`, default: `True` ) – Whether to wrap the result in a code tag.

Returns:

- `Markup` – Markup text.

## do_order_members

```python
do_order_members(
    members: Sequence[Object | Alias],
    order: Order | list[Order],
    members_list: bool | list[str] | None,
) -> Sequence[Object | Alias]
```

Order members given an ordering method.

Parameters:

- ### **`members`**

  (`Sequence[Object | Alias]`) – The members to order.

- ### **`order`**

  (`Order | list[Order]`) – The ordering method.

- ### **`members_list`**

  (`bool | list[str] | None`) – An optional member list (manual ordering).

Returns:

- `Sequence[Object | Alias]` – The same members, ordered.

## do_split_path

```python
do_split_path(path: str, full_path: str) -> Iterator[tuple[str, str, str, str]]
```

Split object paths for building cross-references.

Parameters:

- ### **`path`**

  (`str`) – The path to split.

- ### **`full_path`**

  (`str`) – The full path, used to compute correct paths for each part of the path.

Yields:

- `tuple[str, str, str, str]` – 4-tuples: prefix, word, full path, suffix.

## get_handler

```python
get_handler(
    handler_config: MutableMapping[str, Any], tool_config: MkDocsConfig, **kwargs: Any
) -> PythonHandler
```

Return an instance of `PythonHandler`.

Parameters:

- ### **`handler_config`**

  (`MutableMapping[str, Any]`) – The handler configuration.

- ### **`tool_config`**

  (`MkDocsConfig`) – The tool (SSG) configuration.

- ### **`**kwargs`**

  (`Any`, default: `{}` ) – Additional arguments to pass to the handler.

Returns:

- `PythonHandler` – An instance of PythonHandler.

## config

Deprecated. Import from `mkdocstrings_handlers.python` directly.

## handler

Deprecated. Import from `mkdocstrings_handlers.python` directly.

## rendering

Deprecated. Import from `mkdocstrings_handlers.python` directly.
