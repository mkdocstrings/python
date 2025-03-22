# Changelog

## mkdocstrings-python Insiders

### 1.12.0 <small>March 22, 2025</small> { id="1.12.0" }

- [Ordering method: `__all__`][option-members_order]

### 1.11.0 <small>March 20, 2025</small> { id="1.11.0" }

- [Filtering method: `public`][option-filters-public]

### 1.10.0 <small>March 10, 2025</small> { id="1.10.0" }

- [Backlinks][backlinks]

### 1.9.0 <small>September 03, 2024</small> { id="1.9.0" }

- [Relative cross-references][relative_crossrefs]
- [Scoped cross-references][scoped_crossrefs]

### 1.8.3 <small>June 19, 2024</small> { id="1.8.3" }

- Update code for Griffe 0.46+ to avoid deprecation warnings

### 1.8.2 <small>May 09, 2024</small> { id="1.8.2" }

- Don't render cross-refs for default values when signatures aren't separated

### 1.8.1 <small>April 19, 2024</small> { id="1.8.1" }

- Render enumeration instance name instead of just "value", allowing proper cross-reference

### 1.8.0 <small>March 24, 2024</small> { id="1.8.0" }

- [Annotations modernization][modernize_annotations]

### 1.7.0 <small>March 24, 2024</small> { id="1.7.0" }

- [Class inheritance diagrams with Mermaid][show_inheritance_diagram]

### 1.6.0 <small>January 30, 2024</small> { id="1.6.0" }

- Render cross-references to parameters documentation in signatures and attribute values.
- Add [`parameter_headings`][parameter_headings] option to render headings for parameters (enabling permalinks and ToC/inventory entries).
- Render cross-references for default parameter values in signatures.

### 1.5.1 <small>September 12, 2023</small> { id="1.5.1" }

- Prevent empty auto-summarized Methods section.

### 1.5.0 <small>September 05, 2023</small> { id="1.5.0" }

- Render function signature overloads.

### 1.4.0 <small>August 27, 2023</small> { id="1.4.0" }

- Render cross-references in attribute signatures.

### 1.3.0 <small>August 24, 2023</small> { id="1.3.0" }

- Add "method" symbol type.

### 1.2.0 <small>August 20, 2023</small> { id="1.2.0" }

- Add [member auto-summaries](../usage/configuration/members.md#summary).

### 1.1.4 <small>July 17, 2023</small> { id="1.1.4" }

- Fix heading level increment for class members.

### 1.1.3 <small>July 17, 2023</small> { id="1.1.3" }

- Fix heading level (avoid with clause preventing to decrease it).

### 1.1.2 <small>July 15, 2023</small> { id="1.1.2" }

- Use non-breaking spaces after symbol types.

### 1.1.1 <small>June 27, 2023</small> { id="1.1.1" }

- Correctly escape expressions in signatures and other rendered types.

### 1.1.0 <small>June 4, 2023</small> { id="1.1.0" }

- Add [Symbol types in headings and table of contents](../usage/configuration/headings.md#show_symbol_type_toc).

### 1.0.0 <small>May 10, 2023</small> { id="1.0.0" }

- Add [cross-references for type annotations in signatures](../usage/configuration/signatures.md#signature_crossrefs).
    Make sure to update your local templates as the signature of the
    [`format_signature` filter][mkdocstrings_handlers.python.do_format_signature]
    has changed. The templates that must be updated:
    `class.html`, `expression.html`, `function.html` and `signature.html`.
