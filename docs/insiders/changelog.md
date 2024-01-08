# Changelog

## mkdocstrings-python Insiders

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
    [`format_signature` filter][mkdocstrings_handlers.python.rendering.do_format_signature]
    has changed. The templates that must be updated:
    `class.html`, `expression.html`, `function.html` and `signature.html`.
