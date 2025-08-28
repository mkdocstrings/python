# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [1.18.1](https://github.com/mkdocstrings/python/releases/tag/1.18.1) - 2025-08-28

<small>[Compare with 1.18.0](https://github.com/mkdocstrings/python/compare/1.18.0...1.18.1)</small>

### Bug Fixes

- Don't show implementation signature of `__init__` method when `overloads_only` is true and it is merged into the class ([9ef620f](https://github.com/mkdocstrings/python/commit/9ef620f2b1ae80b3711a2e84ab12d7d2c4a2dbdd) by Timothée Mazzucotelli). [Issue-308](https://github.com/mkdocstrings/python/issues/308)

## [1.18.0](https://github.com/mkdocstrings/python/releases/tag/1.18.0) - 2025-08-26

<small>[Compare with 1.17.0](https://github.com/mkdocstrings/python/compare/1.17.0...1.18.0)</small>

### Features

- Support PEP 695 generics ([dc8c3ad](https://github.com/mkdocstrings/python/commit/dc8c3adb23b37add6601de9e74085f76e5fc9ee5) by Victor Westerhuis). [PR-221](https://github.com/mkdocstrings/python/pull/221), Co-authored-by: Timothée Mazzucotelli <dev@pawamoy.fr>

### Bug Fixes

- Increase maximum recursion limit in case of deeply nested ASTs (rare occurrence) ([6004ccf](https://github.com/mkdocstrings/python/commit/6004ccf3576c7a20e21c880bb2235b7b426ba382) by Timothée Mazzucotelli). [Issue-griffe-402](https://github.com/mkdocstrings/griffe/issues/402)

## [1.17.0](https://github.com/mkdocstrings/python/releases/tag/1.17.0) - 2025-08-14

<small>[Compare with 1.16.12](https://github.com/mkdocstrings/python/compare/1.16.12...1.17.0)</small>

### Features

- Support new Griffe parsing options `warn_missing_types` and `warnings` ([0e3bdb8](https://github.com/mkdocstrings/python/commit/0e3bdb857b5ede3e15aa7a9b8b87b33f68889c9e) by Timothée Mazzucotelli). [Issue-mkdocstrings-437](https://github.com/mkdocstrings/mkdocstrings/issues/437)
- Add `skip_local_inventory` option to prevent objects from being registered in the local objects inventory ([e82c24f](https://github.com/mkdocstrings/python/commit/e82c24f17513fba4cff22e90f0a82c00a01a077d) by Bartosz Sławecki). [Issue-296](https://github.com/mkdocstrings/python/issues/296), [Issue-mkdocstrings-671](https://github.com/mkdocstrings/mkdocstrings/issues/671), [PR-297](https://github.com/mkdocstrings/python/pull/297)
- Support hiding attribute values ([6cf34b9](https://github.com/mkdocstrings/python/commit/6cf34b9882e20d9147a6481e672ae09989a27796) by Bartosz Sławecki). Issue-292: #292, PR-293: #293
- Support hiding implementation signature (showing overload only) ([d3b35e1](https://github.com/mkdocstrings/python/commit/d3b35e17384901e7280b8b6926f10fb033480358) by Bartosz Sławecki). [Issue-213](https://github.com/mkdocstrings/python/issues/213), [PR-286](https://github.com/mkdocstrings/python/pull/286)

### Code Refactoring

- Deprecate `locale` option in favor of mkdocstrings' ([17f71ba](https://github.com/mkdocstrings/python/commit/17f71babf11081869478b21b2bde1a33fc97be41) by Timothée Mazzucotelli). [PR-288](https://github.com/mkdocstrings/python/pull/288)

## [1.16.12](https://github.com/mkdocstrings/python/releases/tag/1.16.12) - 2025-06-03

<small>[Compare with 1.16.11](https://github.com/mkdocstrings/python/compare/1.16.11...1.16.12)</small>

### Bug Fixes

- Only replace CSS class in first *highlighting* span ([d57740f](https://github.com/mkdocstrings/python/commit/d57740f874f056fb3ba1c6013ad04227df0f0af8) by Timothée Mazzucotelli). [Issue-281](https://github.com/mkdocstrings/python/issues/281)

## [1.16.11](https://github.com/mkdocstrings/python/releases/tag/1.16.11) - 2025-05-24

<small>[Compare with 1.16.10](https://github.com/mkdocstrings/python/compare/1.16.10...1.16.11)</small>

### Bug Fixes

- Fix highlighting for signature with known special names like `__init__` ([7f95686](https://github.com/mkdocstrings/python/commit/7f956868f93a766346455fedb296c26787894d5c) by Timothée Mazzucotelli). [Issue-mkdocstrings-757](https://github.com/mkdocstrings/mkdocstrings/issues/757)
- Use default font-size for parameter headings ([0a35b20](https://github.com/mkdocstrings/python/commit/0a35b20a6050a28ba8492d93e5f9940a69462ce3) by Timothée Mazzucotelli). [Issue-mkdocstrings-697](https://github.com/mkdocstrings/mkdocstrings/issues/697)
- Prevent uppercasing H5 titles (by Material for MkDocs) ([ba66969](https://github.com/mkdocstrings/python/commit/ba669697daad5067ea5db3fdf8a2d5ba2f966b25) by Timothée Mazzucotelli). [Issue-mkdocstrings-697](https://github.com/mkdocstrings/mkdocstrings/issues/697), [Issue-276](https://github.com/mkdocstrings/python/issues/276)
- Use configured heading even when signature is not separated ([096960a](https://github.com/mkdocstrings/python/commit/096960abd79831d6fd45e2a7962dfd2bd49e4edd) by Timothée Mazzucotelli). [Issue-mkdocstrings-767](https://github.com/mkdocstrings/mkdocstrings/issues/767), [PR-278](https://github.com/mkdocstrings/python/pull/278)
- Render attribute names without full path in ToC ([d4e618a](https://github.com/mkdocstrings/python/commit/d4e618ab794747b84dced848b1be824639fea2b8) by David Lee). [Issue-271](https://github.com/mkdocstrings/python/issues/271), [PR-272](https://github.com/mkdocstrings/python/pull/272)

## [1.16.10](https://github.com/mkdocstrings/python/releases/tag/1.16.10) - 2025-04-03

<small>[Compare with 1.16.9](https://github.com/mkdocstrings/python/compare/1.16.9...1.16.10)</small>

### Bug Fixes

- Fix inventory `base_url` being ignored ([8870eb9](https://github.com/mkdocstrings/python/commit/8870eb9af837666f59f96149c67c849e02f7ee25) by Stefan Mejlgaard). [Issue-268](https://github.com/mkdocstrings/python/issues/268), [PR-269](https://github.com/mkdocstrings/python/pull/269)

## [1.16.9](https://github.com/mkdocstrings/python/releases/tag/1.16.9) - 2025-04-03

<small>[Compare with 1.16.8](https://github.com/mkdocstrings/python/compare/1.16.8...1.16.9)</small>

### Bug Fixes

- Use `toc_label` option in a few missing places ([337b46b](https://github.com/mkdocstrings/python/commit/337b46be912ff69e70b398bb252c8217c917db0a) by Timothée Mazzucotelli). [Issue-267](https://github.com/mkdocstrings/python/discussions/267)

## [1.16.8](https://github.com/mkdocstrings/python/releases/tag/1.16.8) - 2025-03-24

<small>[Compare with 1.16.7](https://github.com/mkdocstrings/python/compare/1.16.7...1.16.8)</small>

### Bug Fixes

- Prevent infinite recursion by detecting parent-member cycles ([f3917e9](https://github.com/mkdocstrings/python/commit/f3917e9dd50ca7f94d0dd22b6e4e11885b4617e7) by Timothée Mazzucotelli). [Issue-griffe-368](https://github.com/mkdocstrings/griffe/issues/368)

### Code Refactoring

- Prepare feature for ordering by `__all__` value ([bfb5b30](https://github.com/mkdocstrings/python/commit/bfb5b303f4ea2187c15bccc688f7eba25e7edfcc) by Timothée Mazzucotelli). [Issue-219](https://github.com/mkdocstrings/python/issues/219)
- Sort objects without line numbers last instead of first ([681afb1](https://github.com/mkdocstrings/python/commit/681afb146225d98350a8eb2178aab07aec95fe6b) by Timothée Mazzucotelli).

## [1.16.7](https://github.com/mkdocstrings/python/releases/tag/1.16.7) - 2025-03-20

<small>[Compare with 1.16.6](https://github.com/mkdocstrings/python/compare/1.16.6...1.16.7)</small>

### Code Refactoring

- Prepare `public` filtering method feature ([fde2019](https://github.com/mkdocstrings/python/commit/fde20191cab20f39d9e5e729a95cdfa3390b8f1f) by Timothée Mazzucotelli). [Issue-78](https://github.com/mkdocstrings/python/issues/78)

## [1.16.6](https://github.com/mkdocstrings/python/releases/tag/1.16.6) - 2025-03-18

<small>[Compare with 1.16.5](https://github.com/mkdocstrings/python/compare/1.16.5...1.16.6)</small>

### Deprecations

Importing from submodules is now deprecated: the public API is fully exposed under the top-level `mkdocstrings_handler.python` module.

### Bug Fixes

- Add back default compiled filters (regression) ([2d83900](https://github.com/mkdocstrings/python/commit/2d83900c9e258399c90ecbac350ad03ff5d8f311) by Timothée Mazzucotelli). [Issue-264](https://github.com/mkdocstrings/python/issues/264)

### Code Refactoring

- Start logging warnings instead of info messages about deprecated use of templates ([7606f33](https://github.com/mkdocstrings/python/commit/7606f33559ced6962ecf9a1bc9aa76f24d87f515) by Timothée Mazzucotelli).
- Move modules into internal folder, expose API in top-level module ([93a68d0](https://github.com/mkdocstrings/python/commit/93a68d0d7afce38c78a8264189cfa812d737666c) by Timothée Mazzucotelli).

## [1.16.5](https://github.com/mkdocstrings/python/releases/tag/1.16.5) - 2025-03-10

<small>[Compare with 1.16.4](https://github.com/mkdocstrings/python/compare/1.16.4...1.16.5)</small>

### Code Refactoring

- Prepare backlinks support ([56bf627](https://github.com/mkdocstrings/python/commit/56bf627b9483a12228b769ae4690b84733061ea5) by Timothée Mazzucotelli). [Issue-153](https://github.com/mkdocstrings/python/issues/153), [PR-252](https://github.com/mkdocstrings/python/pull/252)

## [1.16.4](https://github.com/mkdocstrings/python/releases/tag/1.16.4) - 2025-03-10

<small>[Compare with 1.16.3](https://github.com/mkdocstrings/python/compare/1.16.3...1.16.4)</small>

### Bug Fixes

- Fix de-duplication of summary sections ([dc46ac9](https://github.com/mkdocstrings/python/commit/dc46ac9b4cfc642decd153dceb62e9f45c5c750e) by Timothée Mazzucotelli).

## [1.16.3](https://github.com/mkdocstrings/python/releases/tag/1.16.3) - 2025-03-08

<small>[Compare with 1.16.2](https://github.com/mkdocstrings/python/compare/1.16.2...1.16.3)</small>

### Build

- Depend on mkdocstrings 0.28.3 ([9fa4f16](https://github.com/mkdocstrings/python/commit/9fa4f1636af240bb695661b7172f052cb11e0ec9) by Timothée Mazzucotelli).

### Bug Fixes

- De-duplicate summary sections ([a657d07](https://github.com/mkdocstrings/python/commit/a657d07499eb82d22337c169aa86b1cdd85543fa) by Timothée Mazzucotelli). [Issue-134](https://github.com/mkdocstrings/python/issues/134)

### Code Refactoring

- Import from top-level `mkdocstrings` module ([da2ba13](https://github.com/mkdocstrings/python/commit/da2ba13b1367ce107416d08f382fb9f2384c015c) by Timothée Mazzucotelli).

## [1.16.2](https://github.com/mkdocstrings/python/releases/tag/1.16.2) - 2025-02-24

<small>[Compare with 1.16.1](https://github.com/mkdocstrings/python/compare/1.16.1...1.16.2)</small>

### Build

- Depend on mkdocs-autorefs >= 1.4 and mkdocstrings >= 0.28.2 ([ea1ab49](https://github.com/mkdocstrings/python/commit/ea1ab498be836c94eb695ace05c41357b12f2c95) by Timothée Mazzucotelli).

## [1.16.1](https://github.com/mkdocstrings/python/releases/tag/1.16.1) - 2025-02-18

<small>[Compare with 1.16.0](https://github.com/mkdocstrings/python/compare/1.16.0...1.16.1)</small>

### Bug Fixes

- Give precedence to user-provided paths when they are already listed in `sys.path` ([0f497d1](https://github.com/mkdocstrings/python/commit/0f497d185ba1860c61555803bfc4b311a410bd39) by Timothée Mazzucotelli). [Issue-248](https://github.com/mkdocstrings/python/discussions/248)

## [1.16.0](https://github.com/mkdocstrings/python/releases/tag/1.16.0) - 2025-02-17

<small>[Compare with 1.15.1](https://github.com/mkdocstrings/python/compare/1.15.1...1.16.0)</small>

### Features

- Add option to show/hide overloads ([4a5ee10](https://github.com/mkdocstrings/python/commit/4a5ee10c65de28b7921a56ef2c222d2f3417edaa) by Pete Stenger). [PR-250](https://github.com/mkdocstrings/python/pull/250)

## [1.15.1](https://github.com/mkdocstrings/python/releases/tag/1.15.1) - 2025-02-17

<small>[Compare with 1.15.0](https://github.com/mkdocstrings/python/compare/1.15.0...1.15.1)</small>

### Bug Fixes

- Unwrap `Annotated` regardless of `signature_crossrefs` ([d809f1a](https://github.com/mkdocstrings/python/commit/d809f1a9e6a6f4eaf6fe4a18c2ec0e69e5716a12) by Timothée Mazzucotelli). [Issue-249](https://github.com/mkdocstrings/python/issues/249)

## [1.15.0](https://github.com/mkdocstrings/python/releases/tag/1.15.0) - 2025-02-11

<small>[Compare with 1.14.6](https://github.com/mkdocstrings/python/compare/1.14.6...1.15.0)</small>

### Features

- Support cross-referencing constructor parameters in instance attribute values ([f07bf58](https://github.com/mkdocstrings/python/commit/f07bf58a7358dea106032c7da27098e7617eefa0) by Timothée Mazzucotelli).

## [1.14.6](https://github.com/mkdocstrings/python/releases/tag/1.14.6) - 2025-02-07

<small>[Compare with 1.14.5](https://github.com/mkdocstrings/python/compare/1.14.5...1.14.6)</small>

### Bug Fixes

- Catch alias resolution errors when getting aliases for an identifier ([0aaa260](https://github.com/mkdocstrings/python/commit/0aaa260139afe2e3ab85d62224c90a389df64978) by Timothée Mazzucotelli). [Issue-358](https://github.com/mkdocstrings/griffe/discussions/358)

### Code Refactoring

- Improve translations for Simplified Chinese and Japanese ([753a0df](https://github.com/mkdocstrings/python/commit/753a0df8f91f1cf42fb7e56b7fdd312b2bd652ab) by Zhikang Yan). [PR-244](https://github.com/mkdocstrings/python/pull/244)

## [1.14.5](https://github.com/mkdocstrings/python/releases/tag/1.14.5) - 2025-02-05

<small>[Compare with 1.14.4](https://github.com/mkdocstrings/python/compare/1.14.4...1.14.5)</small>

### Bug Fixes

- Remove type from property docstring summary in summary sections ([15f2cd4](https://github.com/mkdocstrings/python/commit/15f2cd48b79a1f062086a47ea0c6bc52d89786d8) by Uchechukwu Orji). [PR-242](https://github.com/mkdocstrings/python/pull/242)

## [1.14.4](https://github.com/mkdocstrings/python/releases/tag/1.14.4) - 2025-02-04

<small>[Compare with 1.14.3](https://github.com/mkdocstrings/python/compare/1.14.3...1.14.4)</small>

### Bug Fixes

- Deactivate Pydantic validation on Python 3.9 is `eval-type-backport` is not available (for modern typing syntax support) ([0de0e5e](https://github.com/mkdocstrings/python/commit/0de0e5e57f8f22e039b0d19aad6341ce7ab3da9f) by Timothée Mazzucotelli). [Issue-241](https://github.com/mkdocstrings/python/issues/241)

## [1.14.3](https://github.com/mkdocstrings/python/releases/tag/1.14.3) - 2025-02-04

<small>[Compare with 1.14.2](https://github.com/mkdocstrings/python/compare/1.14.2...1.14.3)</small>

### Bug Fixes

- Let dataclass implement `__init__` method, set extra fields in `get_options` ([477b9e4](https://github.com/mkdocstrings/python/commit/477b9e447ef9717c6edcb14bd4c53f9cacc555b8) by Timothée Mazzucotelli).

## [1.14.2](https://github.com/mkdocstrings/python/releases/tag/1.14.2) - 2025-02-03

<small>[Compare with 1.14.1](https://github.com/mkdocstrings/python/compare/1.14.1...1.14.2)</small>

### Bug Fixes

- Deactivate Pydantic logic if v1 is installed instead of v2 ([c5ecd70](https://github.com/mkdocstrings/python/commit/c5ecd702b04417fa3d862806d608ea627b2e8ed9) by Timothée Mazzucotelli). [Issue-240](https://github.com/mkdocstrings/python/issues/240)

## [1.14.1](https://github.com/mkdocstrings/python/releases/tag/1.14.1) - 2025-02-03

<small>[Compare with 1.14.0](https://github.com/mkdocstrings/python/compare/1.14.0...1.14.1)</small>

### Bug Fixes

- Fix type errors with options during collection and docstring parsing ([15ca6d8](https://github.com/mkdocstrings/python/commit/15ca6d8cbe8187ae2938b3cc3a6134d10c94a3aa) by Timothée Mazzucotelli).

## [1.14.0](https://github.com/mkdocstrings/python/releases/tag/1.14.0) - 2025-02-03

<small>[Compare with 1.13.0](https://github.com/mkdocstrings/python/compare/1.13.0...1.14.0)</small>

### Features

- Add `heading` and `toc_label` options ([7cabacf](https://github.com/mkdocstrings/python/commit/7cabacf13735dbc5066793baf5820d61cd342dc8) by Yann Van Crombrugge). [Issue-mkdocstrings-725](https://github.com/mkdocstrings/mkdocstrings/issues/725), [PR-236](https://github.com/mkdocstrings/python/pull/236)
- Add `force_inspection` option to force dynamic analysis ([83823be](https://github.com/mkdocstrings/python/commit/83823be2146d6a2ecedc5fe9c0cfd84098d780ca) by Uchechukwu Orji). [Issue-94](https://github.com/mkdocstrings/python/issues/94), [PR-231](https://github.com/mkdocstrings/python/pull/231)

### Code Refactoring

- Use dataclasses for configuration/options and automate schema generation ([5ebeda6](https://github.com/mkdocstrings/python/commit/5ebeda6fce1b1bc7cb3f5e27a5a90ac394a3de0c) by Timothée Mazzucotelli).

## [1.13.0](https://github.com/mkdocstrings/python/releases/tag/1.13.0) - 2024-12-26

<small>[Compare with 1.12.2](https://github.com/mkdocstrings/python/compare/1.12.2...1.13.0)</small>

### Features

- Allow using Ruff to format signatures and attribute values ([d67215c](https://github.com/mkdocstrings/python/commit/d67215c976938ef1e169f16dd0b6166067ebd7bc) by dm). [PR-216](https://github.com/mkdocstrings/python/pull/216)

### Bug Fixes

- Respect `show_signature_annotations` option for attribute signatures in headings ([e93d166](https://github.com/mkdocstrings/python/commit/e93d166a14d0944d30ff2f28f21f2262ac396bff) by Timothée Mazzucotelli). [Issue-griffe-pydantic#9](https://github.com/mkdocstrings/griffe-pydantic/issues/9)
- Handle `__init__` overloads when merging into class ([af6fab3](https://github.com/mkdocstrings/python/commit/af6fab31142204872ace716392dcb314b2cb5d0f) by Timothée Mazzucotelli). [Issue-212](https://github.com/mkdocstrings/python/issues/212)
- Actually check if a module is public when rendering auto-generated summary table for modules ([3bf55b2](https://github.com/mkdocstrings/python/commit/3bf55b22ce9a841242c55b2efcedbd8f3a99ccc9) by Timothée Mazzucotelli). [Issue-203](https://github.com/mkdocstrings/python/issues/203)
- Never render line numbers for signatures and attribute values ([a669f1c](https://github.com/mkdocstrings/python/commit/a669f1caefbd54305cc4610bdd57a529aa1208cf) by Timothée Mazzucotelli). [Issue-192](https://github.com/mkdocstrings/python/issues/192)
- Respect highlight's `linenums` config for `pycon` examples in docstrings ([53eb82a](https://github.com/mkdocstrings/python/commit/53eb82a21bbcaa959306e909bf0d4ac468f87580) by Timothée Mazzucotelli). [Related-to-#192](https://github.com/mkdocstrings/python/issues/192)
- Fix normalization of extension paths on the annoying operating system and Python 3.13 ([101a6dc](https://github.com/mkdocstrings/python/commit/101a6dc428da59a512da617a0a2453f2b6ef4387) by Timothée Mazzucotelli).
- Don't merge parent `__init__` docstring into class docstring if such inherited method wasn't selected through the `inherited_members` configuration option ([6c5b5c3](https://github.com/mkdocstrings/python/commit/6c5b5c341940af9425b3de0672ac400794b3f6e5) by Timothée Mazzucotelli). [Issue-189](https://github.com/mkdocstrings/python/issues/189)

### Code Refactoring

- Render `*` and `**` outside of cross-references in signatures ([c4506f0](https://github.com/mkdocstrings/python/commit/c4506f080e0c75cd32d6512c80f5016e82fc12bc) by Timothée Mazzucotelli). [Needed-for-PR-216](https://github.com/mkdocstrings/python/pull/216)

## [1.12.2](https://github.com/mkdocstrings/python/releases/tag/1.12.2) - 2024-10-19

<small>[Compare with 1.12.1](https://github.com/mkdocstrings/python/compare/1.12.1...1.12.2)</small>

### Bug Fixes

- Always render cross-references outside of signatures ([73f11dc](https://github.com/mkdocstrings/python/commit/73f11dcc584a672af7e17738cba08a50f119176a) by Timothée Mazzucotelli). [Issue-mkdocstrings#700](https://github.com/mkdocstrings/mkdocstrings/issues/700)

## [1.12.1](https://github.com/mkdocstrings/python/releases/tag/1.12.1) - 2024-10-14

<small>[Compare with 1.12.0](https://github.com/mkdocstrings/python/compare/1.12.0...1.12.1)</small>

### Bug Fixes

- Don't escape parameter default values ([9dee4d4](https://github.com/mkdocstrings/python/commit/9dee4d4f8e1258e99c19dc7b2b18d3e9090de79b) by Timothée Mazzucotelli). [Issue-191](https://github.com/mkdocstrings/python/issues/191)

## [1.12.0](https://github.com/mkdocstrings/python/releases/tag/1.12.0) - 2024-10-12

<small>[Compare with 1.11.1](https://github.com/mkdocstrings/python/compare/1.11.1...1.12.0)</small>

### Build

- Drop support for Python 3.8 ([6615c91](https://github.com/mkdocstrings/python/commit/6615c91cdc035bc0c2fdd12f3952ff84f5e1c04e) by Timothée Mazzucotelli).

### Features

- Auto-summary of members ([7f9757d](https://github.com/mkdocstrings/python/commit/7f9757d1584555edebc56f1aefe6cc8242e6c8bb) by Timothée Mazzucotelli).
- Render function overloads ([0f2c25c](https://github.com/mkdocstrings/python/commit/0f2c25c9ed7f6c5c93ff13df214f02edfd3a4cb1) by Timothée Mazzucotelli).
- Parameter headings, more automatic cross-references ([0176b83](https://github.com/mkdocstrings/python/commit/0176b83f21ae02d345489c93cca3baf51f8bc58c) by Timothée Mazzucotelli).

### Code Refactoring

- Declare default CSS symbol colors under :host as well ([3b9dba2](https://github.com/mkdocstrings/python/commit/3b9dba2709a8668e379c6ce1536cb1714971b3f4) by James McDonnell). [PR-186](https://github.com/mkdocstrings/python/pull/186)

## [1.11.1](https://github.com/mkdocstrings/python/releases/tag/1.11.1) - 2024-09-03

<small>[Compare with 1.11.0](https://github.com/mkdocstrings/python/compare/1.11.0...1.11.1)</small>

### Code Refactoring

- Prepare `relative_crossrefs` and `scoped_crossrefs` insiders features ([dd8b014](https://github.com/mkdocstrings/python/commit/dd8b014a8ab3decc31d4b08bc22fe68577e1a02c) by Timothée Mazzucotelli).

## [1.11.0](https://github.com/mkdocstrings/python/releases/tag/1.11.0) - 2024-09-03

<small>[Compare with 1.10.9](https://github.com/mkdocstrings/python/compare/1.10.9...1.11.0)</small>

### Features

- Hook into autorefs to provide context around cross-ref errors ([bb4be5b](https://github.com/mkdocstrings/python/commit/bb4be5be1b85be50f46c7889231a2d4a3bd05165) by Timothée Mazzucotelli).

## [1.10.9](https://github.com/mkdocstrings/python/releases/tag/1.10.9) - 2024-08-30

<small>[Compare with 1.10.8](https://github.com/mkdocstrings/python/compare/1.10.8...1.10.9)</small>

### Build

- Explicitly depend on mkdocs-autorefs to be able to specify lower bound ([2299ab5](https://github.com/mkdocstrings/python/commit/2299ab55641585d65babe0e116a6465b4736dcd9) by Timothée Mazzucotelli).

### Code Refactoring

- Use new autorefs syntax ([68cb72f](https://github.com/mkdocstrings/python/commit/68cb72f62253f54146ece621345b36c90d712913) by Timothée Mazzucotelli).

## [1.10.8](https://github.com/mkdocstrings/python/releases/tag/1.10.8) - 2024-08-14

<small>[Compare with 1.10.7](https://github.com/mkdocstrings/python/compare/1.10.7...1.10.8)</small>

### Build

- Depend on Griffe 0.49 ([a87dcad](https://github.com/mkdocstrings/python/commit/a87dcad36065dc3171512e166ec632ee3e5b0a64) by Timothée Mazzucotelli).

## [1.10.7](https://github.com/mkdocstrings/python/releases/tag/1.10.7) - 2024-07-25

<small>[Compare with 1.10.6](https://github.com/mkdocstrings/python/compare/1.10.6...1.10.7)</small>

### Packaging

- Include tests and all relevant files for downstream packaging in source distribution

## [1.10.6](https://github.com/mkdocstrings/python/releases/tag/1.10.6) - 2024-07-25

<small>[Compare with 1.10.5](https://github.com/mkdocstrings/python/compare/1.10.5...1.10.6)</small>

### Bug Fixes

- Fix condition to display members (check all members, not just non-inherited ones) ([3d838a9](https://github.com/mkdocstrings/python/commit/3d838a96f77fa128cd6f2afa5ed0cb151ab225fd) by Timothée Mazzucotelli).

### Code Refactoring

- Update code for Griffe 0.48 (removing deprecation warnings) ([eff10cc](https://github.com/mkdocstrings/python/commit/eff10ccf0fa1b2e73df912048a15c2d6406a2c8b) by Timothée Mazzucotelli). [Issue-173](https://github.com/mkdocstrings/python/issues/173)

## [1.10.5](https://github.com/mkdocstrings/python/releases/tag/1.10.5) - 2024-06-19

<small>[Compare with 1.10.4](https://github.com/mkdocstrings/python/compare/1.10.4...1.10.5)</small>

### Bug Fixes

- Mix both previous checks for displaying objects: not imported or public ([587963b](https://github.com/mkdocstrings/python/commit/587963ba53f765c9d7eefbc2fb80bdbb11164850) by Timothée Mazzucotelli). [Issue-294](https://github.com/mkdocstrings/griffe/issues/294)

## [1.10.4](https://github.com/mkdocstrings/python/releases/tag/1.10.4) - 2024-06-18

<small>[Compare with 1.10.3](https://github.com/mkdocstrings/python/compare/1.10.3...1.10.4)</small>

### Code Refactoring

- Only filter out imported objects instead of non-public ones after applying filters ([e2f4b35](https://github.com/mkdocstrings/python/commit/e2f4b35d29eca6f68afbd2e728ef7542a2abc992) by Timothée Mazzucotelli). [Issue-mkdocstrings/griffe-294](https://github.com/mkdocstrings/griffe/issues/294)
- Update code for Griffe 0.46 to avoid deprecation warnings ([321b407](https://github.com/mkdocstrings/python/commit/321b407eb95195c44f3cf34d780784e0d6751998) by Timothée Mazzucotelli).
- Change `load_external_modules` default value to `None` to support new default mode in Griffe ([ae5896c](https://github.com/mkdocstrings/python/commit/ae5896c1604e9089162d0d63ec97a510a6bcef89) by Timothée Mazzucotelli).

## [1.10.3](https://github.com/mkdocstrings/python/releases/tag/1.10.3) - 2024-05-22

<small>[Compare with 1.10.2](https://github.com/mkdocstrings/python/compare/1.10.2...1.10.3)</small>

### Bug Fixes

- Don't crash when rendering the source of an object whose lineno is none ([64df00b](https://github.com/mkdocstrings/python/commit/64df00b9b757e9642d65cf425d32f5a2e0d75f38) by Timothée Mazzucotelli). [Issue-163](https://github.com/mkdocstrings/python/issues/163)

## [1.10.2](https://github.com/mkdocstrings/python/releases/tag/1.10.2) - 2024-05-16

<small>[Compare with 1.10.1](https://github.com/mkdocstrings/python/compare/1.10.1...1.10.2)</small>

### Bug Fixes

- Actually make use of custom .html.jinja templates ([5668abb](https://github.com/mkdocstrings/python/commit/5668abba15b13b86fe67f70f6b4004b7b1feeb4f) by Timothée Mazzucotelli).

## [1.10.1](https://github.com/mkdocstrings/python/releases/tag/1.10.1) - 2024-05-14

<small>[Compare with 1.10.0](https://github.com/mkdocstrings/python/compare/1.10.0...1.10.1)</small>

### Build

- Depend on mkdocstrings 0.25 which adds support for parameter `once` when logging messages ([2bc156b](https://github.com/mkdocstrings/python/commit/2bc156bd6f231ae13066651f4490d1e9c2ce3ca2) by Timothée Mazzucotelli).

### Code Refactoring

- Set handler's name ([a71ab12](https://github.com/mkdocstrings/python/commit/a71ab12c8e52efe76e5c0a5e54065926a47cc0d2) by Timothée Mazzucotelli).
- Update `*.html` top-level templates to extend the `*.html.jinja` base templates ([a8c540e](https://github.com/mkdocstrings/python/commit/a8c540e95693e8500da884c32ad159b3bbaaa7ba) by Timothée Mazzucotelli). [Issue-151](https://github.com/mkdocstrings/python/issues/151)
- Update `*.html` base templates to extend their `*.html.jinja` counterpart, while overriding the `logs` block to issue a logging message (info) stating that extending `*.html` templates is deprecated ([e6f1b9c](https://github.com/mkdocstrings/python/commit/e6f1b9caf13754eca9dbb2f112727bef50876ed7) by Timothée Mazzucotelli). [Issue-151](https://github.com/mkdocstrings/python/issues/151)
- Add `*.html.jinja` top-level (overridable) templates, extending their base counterpart ([7c14924](https://github.com/mkdocstrings/python/commit/7c14924c406d7b5f4f1c22d03019d4c566018d2d) by Timothée Mazzucotelli). [Issue-151](https://github.com/mkdocstrings/python/issues/151)
- Add `*.html.jinja` base templates, which are copies of `*.html` templates, with an additional `logs` block, and using the updated `get_template` filter ([eced9a5](https://github.com/mkdocstrings/python/commit/eced9a54fc8a559b686cb1b1180a0d2e04ba452d) by Timothée Mazzucotelli). [Issue-151](https://github.com/mkdocstrings/python/issues/151)
- Update `get_template` filter to support both `*.html` and `*.html.jinja` templates, logging a message (info) when `*.html` templates are overridden by users ([3546fd7](https://github.com/mkdocstrings/python/commit/3546fd70b2d4e45f77b166b2e67c333acc8af0d2) by Timothée Mazzucotelli). [Issue-151](https://github.com/mkdocstrings/python/issues/151)
- Log a warning when base templates are overridden ([26e3d66](https://github.com/mkdocstrings/python/commit/26e3d66f5334a5aaff75bda030afe6dfa1cc94d7) by Timothée Mazzucotelli). [Issue-151](https://github.com/mkdocstrings/python/issues/151)

## [1.10.0](https://github.com/mkdocstrings/python/releases/tag/1.10.0) - 2024-04-19

<small>[Compare with 1.9.2](https://github.com/mkdocstrings/python/compare/1.9.2...1.10.0)</small>

### Features

- Add CSS classes `doc-section-title` and `doc-section-item` in docstring sections ([d6e1d68](https://github.com/mkdocstrings/python/commit/d6e1d68c099e61c3bd6d93e583708335d84158f5) by Timothée Mazzucotelli). [Issue-17](https://github.com/mkdocstrings/python/issues/17)

### Bug Fixes

- Render enumeration instance name instead of just "value", allowing proper cross-reference ([11d81d8](https://github.com/mkdocstrings/python/commit/11d81d8e056b7c074eb3a1c47606867156a338fa) by Timothée Mazzucotelli). [Issue-124](https://github.com/mkdocstrings/python/issues/124)

## [1.9.2](https://github.com/mkdocstrings/python/releases/tag/1.9.2) - 2024-04-02

<small>[Compare with 1.9.1](https://github.com/mkdocstrings/python/compare/1.9.1...1.9.2)</small>

### Dependencies

- Remove cap on Python-Markdown 3.6 now that ToC labels are fixed by mkdocstrings ([0c1e2c1](https://github.com/mkdocstrings/python/commit/0c1e2c15b2497d99974cbb9bd68f25056bb8451b) by Timothée Mazzucotelli).

## [1.9.1](https://github.com/mkdocstrings/python/releases/tag/1.9.1) - 2024-04-02

<small>[Compare with 1.9.0](https://github.com/mkdocstrings/python/compare/1.9.0...1.9.1)</small>

### Bug Fixes

- Don't try loading packages from relative paths ([bd73497](https://github.com/mkdocstrings/python/commit/bd7349714059afb1295e743dbc82380fa797a032) by Timothée Mazzucotelli). [Issue-145](https://github.com/mkdocstrings/python/issues/145)

### Code Refactoring

- Allow first name in a separate signature to be highlighted as a function name ([f798a1e](https://github.com/mkdocstrings/python/commit/f798a1e19dbac548420dcbe1172e9a49232b615b) by Timothée Mazzucotelli).
- Maintain original Pygments color for cross-refs in signatures ([7c8b885](https://github.com/mkdocstrings/python/commit/7c8b885fa2b704e719016acb35791723ea3a496a) by Timothée Mazzucotelli).

## [1.9.0](https://github.com/mkdocstrings/python/releases/tag/1.9.0) - 2024-03-13

<small>[Compare with 1.8.0](https://github.com/mkdocstrings/python/compare/1.8.0...1.9.0)</small>

### Dependencies

- Add upper bound on Python-Markdown 3.6 to temporarily prevent breaking changes ([cd93ee3](https://github.com/mkdocstrings/python/commit/cd93ee31418a2752667d43bb5a05d22284522c24) by Timothée Mazzucotelli).

### Features

- Add `show_labels` option to show/hide labels ([eaf9b82](https://github.com/mkdocstrings/python/commit/eaf9b8240069f7369f401fe048892043c8b173d3) by Viicos). [Issue #120](https://github.com/mkdocstrings/python/issues/120), [PR #130](https://github.com/mkdocstrings/python/pull/130)
- Add option to search for stubs packages ([0c6aa32](https://github.com/mkdocstrings/python/commit/0c6aa323c9e57b8348765a5daa11c79d0c5edb07) by Romain). [PR #128](https://github.com/mkdocstrings/python/pull/128), PR griffe#221: : https://github.com/mkdocstrings/griffe/pull/221

### Code Refactoring

- Mark all Jinja blocks as scoped ([548bdad](https://github.com/mkdocstrings/python/commit/548bdaddd66ffc99b3b9a5a62228a2ff4ff0dd00) by Timothée Mazzucotelli).

## [1.8.0](https://github.com/mkdocstrings/python/releases/tag/1.8.0) - 2024-01-08

<small>[Compare with 1.7.5](https://github.com/mkdocstrings/python/compare/1.7.5...1.8.0)</small>

### Features

- Release Insiders features of the $500/month funding goal ([bd30106](https://github.com/mkdocstrings/python/commit/bd301061fe9c647f9b91c2c9b4baa784c304eca7) by Timothée Mazzucotelli).
    The features and projects related to *mkdocstrings-python* are:

    - [Cross-references for type annotations in signatures](https://mkdocstrings.github.io/python/usage/configuration/signatures/#signature_crossrefs)
    - [Symbol types in headings and table of contents](https://mkdocstrings.github.io/python/usage/configuration/headings/#show_symbol_type_toc)
    - [`griffe-inherited-docstrings`](https://mkdocstrings.github.io/griffe-inherited-docstrings/), a Griffe extension for inheriting docstrings
    - [`griffe2md`](https://mkdocstrings.github.io/griffe2md/), a tool to output API docs to Markdown using Griffe

    See the complete list of features and projects here:
    https://pawamoy.github.io/insiders/#500-plasmavac-user-guide.

## [1.7.5](https://github.com/mkdocstrings/python/releases/tag/1.7.5) - 2023-11-21

<small>[Compare with 1.7.4](https://github.com/mkdocstrings/python/compare/1.7.4...1.7.5)</small>

### Bug Fixes

- Add missing translations (fallback theme) for ReadTheDocs ([2fb6513](https://github.com/mkdocstrings/python/commit/2fb651304d0a80fa9d6a8c77c16b3004bda22972) by Timothée Mazzucotelli). [Issue #115](https://github.com/mkdocstrings/python/issues/115)

## [1.7.4](https://github.com/mkdocstrings/python/releases/tag/1.7.4) - 2023-11-12

<small>[Compare with 1.7.3](https://github.com/mkdocstrings/python/compare/1.7.3...1.7.4)</small>

### Bug Fixes

- Make extension paths relative to config file ([5035e92](https://github.com/mkdocstrings/python/commit/5035e9269fe11664fd25e438ac8f746721b3de0a) by Waylan Limberg). [PR #112](https://github.com/mkdocstrings/python/pull/112), Co-authored-by: Timothée Mazzucotelli <pawamoy@pm.me>

### Code Refactoring

- Prepare for Griffe 0.37 ([b5bb8a9](https://github.com/mkdocstrings/python/commit/b5bb8a982e7a2ec97c73335e453d0033bf4987b6) by Timothée Mazzucotelli).

## [1.7.3](https://github.com/mkdocstrings/python/releases/tag/1.7.3) - 2023-10-09

<small>[Compare with 1.7.2](https://github.com/mkdocstrings/python/compare/1.7.2...1.7.3)</small>

### Bug Fixes

- Don't deepcopy the local config ([1300d2c](https://github.com/mkdocstrings/python/commit/1300d2c77dd49f5dea459ad844d72edcc856c4cd) by Timothée Mazzucotelli).

## [1.7.2](https://github.com/mkdocstrings/python/releases/tag/1.7.2) - 2023-10-05

<small>[Compare with 1.7.1](https://github.com/mkdocstrings/python/compare/1.7.1...1.7.2)</small>

### Bug Fixes

- Prevent alias resolution error when source-ordering members ([67df10c](https://github.com/mkdocstrings/python/commit/67df10cbb86225e1e3efc251325cbff883a1ef3c) by Timothée Mazzucotelli). [Issue griffe#213](https://github.com/mkdocstrings/griffe/issues/213)

### Code Refactoring

- Use package relative filepath if filepath is not relative ([aa5a3f7](https://github.com/mkdocstrings/python/commit/aa5a3f7b0928498ba9da10ed1211d1e55b7f6c4b) by Timothée Mazzucotelli). [Discussion mkdocstrings#622](https://github.com/mkdocstrings/mkdocstrings/discussions/622)

## [1.7.1](https://github.com/mkdocstrings/python/releases/tag/1.7.1) - 2023-09-28

<small>[Compare with 1.7.0](https://github.com/mkdocstrings/python/compare/1.7.0...1.7.1)</small>

### Bug Fixes

- Stop propagation of annotation to next parameter in signature template ([3a760ac](https://github.com/mkdocstrings/python/commit/3a760acacfabaef5abc658ee579e1c205e674994) by Timothée Mazzucotelli). [Issue #110](https://github.com/mkdocstrings/python/issues/110)

### Code Refactoring

- Look into inherited members for `__init__` methods when merging docstrings ([b97d51f](https://github.com/mkdocstrings/python/commit/b97d51f67c2ee3d1edfe6975274ead50fcb3fa8f) by Timothée Mazzucotelli). [Issue #106](https://github.com/mkdocstrings/python/issues/106)

## [1.7.0](https://github.com/mkdocstrings/python/releases/tag/1.7.0) - 2023-09-14

<small>[Compare with 1.6.3](https://github.com/mkdocstrings/python/compare/1.6.3...1.7.0)</small>

### Features

- Add option to unwrap `Annotated` types ([53db04b](https://github.com/mkdocstrings/python/commit/53db04b6256db960aebc2a9f91129b82ca222e41) by Timothée Mazzucotelli).

## [1.6.3](https://github.com/mkdocstrings/python/releases/tag/1.6.3) - 2023-09-11

<small>[Compare with 1.6.2](https://github.com/mkdocstrings/python/compare/1.6.2...1.6.3)</small>

### Bug Fixes

- Make `load_external_modules` a global-only option ([266f41f](https://github.com/mkdocstrings/python/commit/266f41f2033e034060001bc2bed376b4f3a8d7b8) by Timothée Mazzucotelli). [Issue #87](https://github.com/mkdocstrings/python/issues/87)
- Never fail when trying to format code with Black ([df24bbc](https://github.com/mkdocstrings/python/commit/df24bbc640886e1da2d00a3b58c1aa7736cb1eeb) by Timothée Mazzucotelli).

### Code Refactoring

- Wrap docstring section elements (list style) in code tags to prevent spell checker errors ([1ae8dd8](https://github.com/mkdocstrings/python/commit/1ae8dd89cddd67c09d7d30c59b9013516cea2924) by Timothée Mazzucotelli).

## [1.6.2](https://github.com/mkdocstrings/python/releases/tag/1.6.2) - 2023-09-05

<small>[Compare with 1.6.1](https://github.com/mkdocstrings/python/compare/1.6.1...1.6.2)</small>

### Bug Fixes

- Don't render cross-ref spans when they're not enabled ([eed51ee](https://github.com/mkdocstrings/python/commit/eed51ee14bd973a08395f95377f9bd4cd38febfc) by Timothée Mazzucotelli).

## [1.6.1](https://github.com/mkdocstrings/python/releases/tag/1.6.1) - 2023-09-04

<small>[Compare with 1.6.0](https://github.com/mkdocstrings/python/compare/1.6.0...1.6.1)</small>

### Bug Fixes

- Fix spacing for rendered named items in Yields, Receives and Returns sections (list style) ([e12688e](https://github.com/mkdocstrings/python/commit/e12688ecb7d868047f794300eb2638d052563e68) by Timothée Mazzucotelli).
- Fix rendering Receives sections as lists ([9ff7e68](https://github.com/mkdocstrings/python/commit/9ff7e68b58e2ab0829c73e4e62254325a4f766ac) by Timothée Mazzucotelli).

## [1.6.0](https://github.com/mkdocstrings/python/releases/tag/1.6.0) - 2023-08-27

<small>[Compare with 1.5.2](https://github.com/mkdocstrings/python/compare/1.5.2...1.6.0)</small>

### Features

- Add `doc-signature` CSS class to separate signature code blocks ([b6c648f](https://github.com/mkdocstrings/python/commit/b6c648f554f2e0dce609afc2a2c1a3b27a4fbeba) by Timothée Mazzucotelli).

### Code Refactoring

- Add a `format_attribute` filter, preparing for cross-refs in attribute signatures ([8f0ade2](https://github.com/mkdocstrings/python/commit/8f0ade249638ee2f2d446f083c70b6c30799875a) by Timothée Mazzucotelli).

## [1.5.2](https://github.com/mkdocstrings/python/releases/tag/1.5.2) - 2023-08-25

<small>[Compare with 1.5.1](https://github.com/mkdocstrings/python/compare/1.5.1...1.5.2)</small>

### Bug Fixes

- Regression in children template: fix condition for when members are specified ([beeebff](https://github.com/mkdocstrings/python/commit/beeebffa36288d1f71d122f78ecd9064b41a75d0) by Timothée Mazzucotelli). [Issue #100](https://github.com/mkdocstrings/python/issues/100)
- Prevent whitespace removal before highlight filter ([c6f36c0](https://github.com/mkdocstrings/python/commit/c6f36c0c9e5141800f8c5c988c9b67720fccccb8) by Timothée Mazzucotelli).

### Code Refactoring

- Never show full object path in ToC entry ([9aa758b](https://github.com/mkdocstrings/python/commit/9aa758bcc42dfcf7c416d87b8f7cd407b7fdf148) by Timothée Mazzucotelli).
- Sync templates with insiders, remove useless lines ([38b317f](https://github.com/mkdocstrings/python/commit/38b317f4fc74b583a4788721a5559c51a5a47d86) by Timothée Mazzucotelli).

## [1.5.1](https://github.com/mkdocstrings/python/releases/tag/1.5.1) - 2023-08-24

<small>[Compare with 1.5.0](https://github.com/mkdocstrings/python/compare/1.5.0...1.5.1)</small>

### Code Refactoring

- Never show full path in separate signature since it would appear in the heading already ([9e02049](https://github.com/mkdocstrings/python/commit/9e0204930cf4dc973ba8eb41c471fc0132e1631f) by Timothée Mazzucotelli).
- Improve guessing whether an object is public ([35eb811](https://github.com/mkdocstrings/python/commit/35eb81162582d794f170cd7e8c68f10ecfd8ff9d) by Timothée Mazzucotelli).
- Always sort modules alphabetically as source order wouldn't make sense ([70c81ce](https://github.com/mkdocstrings/python/commit/70c81cebb62366cbfc6124bc84d1563db176afb6) by Timothée Mazzucotelli).
- Return anchors as a tuple, not a set, to preserve order ([736a2b5](https://github.com/mkdocstrings/python/commit/736a2b5e729d25bb184db8d42f2ad01025a5bc58) by Timothée Mazzucotelli). [Related-to #mkdocstrings/crystal#6](https://github.com/mkdocstrings/crystal/pull/6)

## [1.5.0](https://github.com/mkdocstrings/python/releases/tag/1.5.0) - 2023-08-20

<small>[Compare with 1.4.0](https://github.com/mkdocstrings/python/compare/1.4.0...1.5.0)</small>

### Features

- Add support for new Griffe docstring sections: modules, classes, and functions (methods) ([d5337af](https://github.com/mkdocstrings/python/commit/d5337afdf68fc492b34f749aa69d1da33b49f9c2) by Timothée Mazzucotelli).

## [1.4.0](https://github.com/mkdocstrings/python/releases/tag/1.4.0) - 2023-08-18

<small>[Compare with 1.3.0](https://github.com/mkdocstrings/python/compare/1.3.0...1.4.0)</small>

### Features

- Support new Griffe expressions (in v0.33) ([9b8e1b1](https://github.com/mkdocstrings/python/commit/9b8e1b1604b978cf2d89b7abf826cf4407f92394) by Timothée Mazzucotelli).

### Code Refactoring

- Deprecate `crossref` and `multi_crossref` filters ([4fe3d20](https://github.com/mkdocstrings/python/commit/4fe3d2051047061780e20683da6513a7c8d91829) by Timothée Mazzucotelli).

## [1.3.0](https://github.com/mkdocstrings/python/releases/tag/1.3.0) - 2023-08-06

<small>[Compare with 1.2.1](https://github.com/mkdocstrings/python/compare/1.2.1...1.3.0)</small>

### Dependencies

- Set upper bound on Griffe (0.33) ([ad8c2a3](https://github.com/mkdocstrings/python/commit/ad8c2a3ac8daf0b0c06579b6ba667e05feffa247) by Timothée Mazzucotelli). See https://github.com/mkdocstrings/griffe/discussions/195.

### Features

- Show parameter default values within the "list" section style too ([55f08f3](https://github.com/mkdocstrings/python/commit/55f08f3e2cece815dd79d35c82515ba8003ec64c) by Antoine Dechaume). [PR #92](https://github.com/mkdocstrings/python/pull/92), Co-authored-by: Timothée Mazzucotelli <pawamoy@pm.me>

## [1.2.1](https://github.com/mkdocstrings/python/releases/tag/1.2.1) - 2023-07-20

<small>[Compare with 1.2.0](https://github.com/mkdocstrings/python/compare/1.2.0...1.2.1)</small>

### Bug Fixes

- Fix members ordering when members are specified with a boolean ([c69f9c3](https://github.com/mkdocstrings/python/commit/c69f9c3b3ddde915619eded6620f7ddada977b00) by Timothée Mazzucotelli). [Issue #89](https://github.com/mkdocstrings/python/issues/89)

## [1.2.0](https://github.com/mkdocstrings/python/releases/tag/1.2.0) - 2023-07-14

<small>[Compare with 1.1.2](https://github.com/mkdocstrings/python/compare/1.1.2...1.2.0)</small>

### Features

- Add Jinja blocks to module, class, function and attribute templates ([299fe48](https://github.com/mkdocstrings/python/commit/299fe483cc03ba76df29b843f88467f89db6dc72) by Timothée Mazzucotelli).
- Setup infrastructure for I18N, add translations for simplified chinese and japanese ([b053b29](https://github.com/mkdocstrings/python/commit/b053b2900ef5c0069b68ad19bda9aaa98141a525) by Nyuan Zhang). [PR #77](https://github.com/mkdocstrings/python/pull/77)
- Support inheritance ([ae42356](https://github.com/mkdocstrings/python/commit/ae4235689155a4b4f0c1e74b0014a466c6b1181f) by Timothée Mazzucotelli). [Issue mkdocstrings#157](https://github.com/mkdocstrings/mkdocstrings/issues/157), [Discussion mkdocstrings#536](https://github.com/mkdocstrings/mkdocstrings/discussions/536)

### Bug Fixes

- Don't show `None` as return annotation of class signatures ([3d8724e](https://github.com/mkdocstrings/python/commit/3d8724ed1f4d040d7a3d9d02784cf0d1f80445b2) by Timothée Mazzucotelli). [Issue #85](https://github.com/mkdocstrings/python/issues/85)
- Show labels in deterministic order ([02619a8](https://github.com/mkdocstrings/python/commit/02619a85ee4aab25f3241d983bdfff0534dd3f81) by Oleh Prypin).

## [1.1.2](https://github.com/mkdocstrings/python/releases/tag/1.1.2) - 2023-06-04

<small>[Compare with 1.1.1](https://github.com/mkdocstrings/python/compare/1.1.1...1.1.2)</small>

### Code Refactoring

- Keep headings style consistent (CSS) ([92032e5](https://github.com/mkdocstrings/python/commit/92032e561861c3fc4e3fb0c6882bb076d0e6614d) by Timothée Mazzucotelli).

## [1.1.1](https://github.com/mkdocstrings/python/releases/tag/1.1.1) - 2023-06-04

<small>[Compare with 1.1.0](https://github.com/mkdocstrings/python/compare/1.1.0...1.1.1)</small>

### Bug Fixes

- Fix mkdocs and readthedocs themes support ([14f18b2](https://github.com/mkdocstrings/python/commit/14f18b219f67f9b6d154d4a52051d8d7d7c49348) by Timothée Mazzucotelli).

### Code Refactoring

- Improve display of paragraphs in docstring sections ([439f5e6](https://github.com/mkdocstrings/python/commit/439f5e6984fe94c28324ca57fbd1a52ef8f55b62) by Timothée Mazzucotelli).

## [1.1.0](https://github.com/mkdocstrings/python/releases/tag/1.1.0) - 2023-05-25

<small>[Compare with 1.0.0](https://github.com/mkdocstrings/python/compare/1.0.0...1.1.0)</small>

### Features

- Support custom templates through objects' extra data ([8ff2b06](https://github.com/mkdocstrings/python/commit/8ff2b06295e848b9c84867802eb845adf061dc10) by Timothée Mazzucotelli). [PR #70](https://github.com/mkdocstrings/python/pull/70)

## [1.0.0](https://github.com/mkdocstrings/python/releases/tag/1.0.0) - 2023-05-11

<small>[Compare with 0.10.1](https://github.com/mkdocstrings/python/compare/0.10.1...1.0.0)</small>

### Breaking changes

- The signature of the [`format_signature` filter][mkdocstrings_handlers.python.do_format_signature] has changed.
    If you override templates in your project to customize the output,
    make sure to update the following templates so that they use
    the new filter signature:

    - `class.html`
    - `expression.html`
    - `function.html`
    - `signature.html`

    You can see how to use the filter in this commit's changes:
    [f686f4e4](https://github.com/mkdocstrings/python/commit/f686f4e4599cea64686d4ef4863b507dd096a513).

**We take this as an opportunity to go out of beta and bump the version to 1.0.0.
This will allow users to rely on semantic versioning.**

### Bug Fixes

- Bring compatibility with insiders signature crossrefs feature ([f686f4e](https://github.com/mkdocstrings/python/commit/f686f4e4599cea64686d4ef4863b507dd096a513) by Timothée Mazzucotelli).

## [0.10.1](https://github.com/mkdocstrings/python/releases/tag/0.10.1) - 2023-05-07

<small>[Compare with 0.10.0](https://github.com/mkdocstrings/python/compare/0.10.0...0.10.1)</small>

### Bug Fixes

- Format signatures with full-path names ([685512d](https://github.com/mkdocstrings/python/commit/685512decf1a14c53fa6ca82048e65619aa6a463) by Timothée Mazzucotelli).

## [0.10.0](https://github.com/mkdocstrings/python/releases/tag/0.10.0) - 2023-05-07

<small>[Compare with 0.9.0](https://github.com/mkdocstrings/python/compare/0.9.0...0.10.0)</small>

### Features

- Add option to disallow inspection ([40f2f26](https://github.com/mkdocstrings/python/commit/40f2f268876358941cf8221d01d219a0deb9de38) by Nyuan Zhang). [Issue #68](https://github.com/mkdocstrings/python/issues/68), [PR #69](https://github.com/mkdocstrings/python/pull/69)

### Bug Fixes

- Make admonitions open by default ([79cd153](https://github.com/mkdocstrings/python/commit/79cd153cfceec860f6ce08d30817c21031983238) by Timothée Mazzucotelli). [Issue #22](https://github.com/mkdocstrings/python/issues/22)

### Code Refactoring

- Match documented behavior for filtering (all members, list, none) ([c7f70c3](https://github.com/mkdocstrings/python/commit/c7f70c353c3dd2b82e1f34c70cd433e0bab4f6e6) by Timothée Mazzucotelli).
- Switch to an info level log for when black's not installed ([f593bb0](https://github.com/mkdocstrings/python/commit/f593bb06c63860be14d2025c4bd795e0c8976ce0) by Faster Speeding).
- Return anchors as a set ([e2b820c](https://github.com/mkdocstrings/python/commit/e2b820c5af3787518656d5f7f799ecb6b55aa033) by Timothée Mazzucotelli).

## [0.9.0](https://github.com/mkdocstrings/python/releases/tag/0.9.0) - 2023-04-03

<small>[Compare with 0.8.3](https://github.com/mkdocstrings/python/compare/0.8.3...0.9.0)</small>

### Features

- Allow resolving alias to external modules ([02052e2](https://github.com/mkdocstrings/python/commit/02052e248b125a113ab788faa9a075adbdc92ca6) by Gilad). [PR #61](https://github.com/mkdocstrings/python/pull/61), [Follow-up of PR #60](https://github.com/mkdocstrings/python/pull/60)
- Allow pre-loading modules ([36002cb](https://github.com/mkdocstrings/python/commit/36002cb9c89fba35d23afb07a866dd8c6877f742) by Gilad). [Issue mkdocstrings/mkdocstrings#503](https://github.com/mkdocstrings/mkdocstrings/issues/503), [PR #60](https://github.com/mkdocstrings/python/pull/60)
- Add show options for docstrings ([a6c55fb](https://github.com/mkdocstrings/python/commit/a6c55fb52f362dd49b1a7e334a631f6ea3b1b963) by Jeremy Goh). [Issue mkdocstrings/mkdocstrings#466](https://github.com/mkdocstrings/mkdocstrings/issues/466), [PR #56](https://github.com/mkdocstrings/python/pull/56)
- Allow custom list of domains for inventories ([f5ea6fd](https://github.com/mkdocstrings/python/commit/f5ea6fd81f7a531e8a97bb0e48267188d72936c1) by Sorin Sbarnea). [Issue mkdocstrings/mkdocstrings#510](https://github.com/mkdocstrings/mkdocstrings/issues/510), [PR #49](https://github.com/mkdocstrings/python/pull/49)

### Bug Fixes

- Prevent alias resolution error when searching for anchors ([a190e2c](https://github.com/mkdocstrings/python/commit/a190e2c4a752e74a05ad03702837a0914c198742) by Timothée Mazzucotelli). [Issue #64](https://github.com/mkdocstrings/python/issues/64)

### Code Refactoring

- Support Griffe 0.26 ([075735c](https://github.com/mkdocstrings/python/commit/075735ce8d86921fbf092d7ad1d009bbb3a2e0bb) by Timothée Mazzucotelli).
- Log (debug) unresolved aliases ([9164742](https://github.com/mkdocstrings/python/commit/9164742f87362e8241dea11bec0fd96f6b9d9dda) by Timothée Mazzucotelli).

## [0.8.3](https://github.com/mkdocstrings/python/releases/tag/0.8.3) - 2023-01-04

<small>[Compare with 0.8.2](https://github.com/mkdocstrings/python/compare/0.8.2...0.8.3)</small>

### Code Refactoring
- Change "unresolved aliases" log level to DEBUG ([dccb818](https://github.com/mkdocstrings/python/commit/dccb818f51278cc8799e2187a615d999a3ab86fb) by Timothée Mazzucotelli).


## [0.8.2](https://github.com/mkdocstrings/python/releases/tag/0.8.2) - 2022-11-19

<small>[Compare with 0.8.1](https://github.com/mkdocstrings/python/compare/0.8.1...0.8.2)</small>

### Bug Fixes
- Fix base directory used to expand globs ([34cfa4b](https://github.com/mkdocstrings/python/commit/34cfa4b41f264437a338e66f6060ceeee134ba15) by Florian Hofer). [PR #45](https://github.com/mkdocstrings/python/pull/45)


## [0.8.1](https://github.com/mkdocstrings/python/releases/tag/0.8.1) - 2022-11-19

<small>[Compare with 0.8.0](https://github.com/mkdocstrings/python/compare/0.8.0...0.8.1)</small>

### Bug Fixes
- Expand globs relative to configuration file path ([0dc45ae](https://github.com/mkdocstrings/python/commit/0dc45aeb7c7f9b2f15118ebf1584baa06d365c9b) by David Vegh). [Issue #42](https://github.com/mkdocstrings/python/issues/42), [PR #43](https://github.com/mkdocstrings/python/pull/43)


## [0.8.0](https://github.com/mkdocstrings/python/releases/tag/0.8.0) - 2022-11-13

<small>[Compare with 0.7.1](https://github.com/mkdocstrings/python/compare/0.7.1...0.8.0)</small>

### Features
- Add support for globs in paths configuration ([29edd02](https://github.com/mkdocstrings/python/commit/29edd02e7a4d83f6b7e8555d4d5b03a79882eb07) by Andrew Guenther). [Issue #33](https://github.com/mkdocstrings/python/issues/33), [PR #34](https://github.com/mkdocstrings/python/pull/34)

### Code Refactoring
- Support Griffe 0.24 ([3b9f701](https://github.com/mkdocstrings/python/commit/3b9f7013a7367f18e4354c37f029f9caf3ad0a4e) by Timothée Mazzucotelli).


## [0.7.1](https://github.com/mkdocstrings/python/releases/tag/0.7.1) - 2022-06-12

<small>[Compare with 0.7.0](https://github.com/mkdocstrings/python/compare/0.7.0...0.7.1)</small>

### Bug Fixes
- Fix rendering of `/` in signatures ([3e927e4](https://github.com/mkdocstrings/python/commit/3e927e43192710218fe69f67ff832936c856a678) by Timothée Mazzucotelli). [Issue #25](https://github.com/mkdocstrings/python/issues/25)


## [0.7.0](https://github.com/mkdocstrings/python/releases/tag/0.7.0) - 2022-05-28

<small>[Compare with 0.6.6](https://github.com/mkdocstrings/python/compare/0.6.6...0.7.0)</small>

### Packaging / Dependencies
- Depend on mkdocstrings 0.19 ([b6a9a47](https://github.com/mkdocstrings/python/commit/b6a9a4799980c4590a7ce2838e12653f40e43be3) by Timothée Mazzucotelli).

### Features
- Add config option for annotations paths verbosity ([b6c9893](https://github.com/mkdocstrings/python/commit/b6c989315fb028813a919319ad1818b0b1f597ac) by Timothée Mazzucotelli).
- Use sections titles in SpaCy-styled docstrings ([fe16b54](https://github.com/mkdocstrings/python/commit/fe16b54aea60473575343e3a3c428567b701bd7d) by Timothée Mazzucotelli).
- Wrap objects names in spans to allow custom styling ([0822ff9](https://github.com/mkdocstrings/python/commit/0822ff9d3ffd3fb71fb619a8b557160661eff9c3) by Timothée Mazzucotelli). [Issue mkdocstrings/mkdocstrings#240](https://github.com/mkdocstrings/mkdocstrings/issues/240)
- Add Jinja blocks around docstring section styles ([aaa79ee](https://github.com/mkdocstrings/python/commit/aaa79eea40d49a64a69badbe732bf5211fbf055a) by Timothée Mazzucotelli).
- Add members and filters options ([24a6136](https://github.com/mkdocstrings/python/commit/24a6136ee6c04a6a49ee74b20e65177868a10ea7) by Timothée Mazzucotelli).
- Add paths option ([dd41182](https://github.com/mkdocstrings/python/commit/dd41182c210f0bb2675ead162adaa01dbbb1949f) by Timothée Mazzucotelli). [Issue mkdocstrings/mkdocstrings#311](https://github.com/mkdocstrings/mkdocstrings/issues/311), [PR #20](https://github.com/mkdocstrings/python/issues/20)

### Bug Fixes
- Fix CSS class on labels ([312a709](https://github.com/mkdocstrings/python/commit/312a7092394aab968032cf08195af7445a85052f) by Timothée Mazzucotelli).
- Fix categories rendering ([6407cf4](https://github.com/mkdocstrings/python/commit/6407cf4f2375c894e0c528e932e9b76774a6455e) by Timothée Mazzucotelli). [Issue #14](https://github.com/mkdocstrings/python/issues/14)

### Code Refactoring
- Disable `show_submodules` by default ([480d0c3](https://github.com/mkdocstrings/python/commit/480d0c373904713313ec76b6e2570dbc35eb527b) by Timothée Mazzucotelli).
- Merge default configuration options in handler ([347ce76](https://github.com/mkdocstrings/python/commit/347ce76d074c0e3841df2d5162b54d3938d00453) by Timothée Mazzucotelli).
- Reduce number of template debug logs ([8fed314](https://github.com/mkdocstrings/python/commit/8fed314243e3981fc7b527c69cee628e87b10220) by Timothée Mazzucotelli).
- Respect `show_root_full_path` for ToC entries (hidden headings) ([8f4c853](https://github.com/mkdocstrings/python/commit/8f4c85328e8b4a45db77f9fc3e536a5008686f37) by Timothée Mazzucotelli).
- Bring consistency on headings style ([59104c4](https://github.com/mkdocstrings/python/commit/59104c4c51c86c774eed76d8508f9f4d3db5463f) by Timothée Mazzucotelli).
- Stop using deprecated base classes ([d5ea1c5](https://github.com/mkdocstrings/python/commit/d5ea1c5cf7884d8c019145f73685a84218e69840) by Timothée Mazzucotelli).


## [0.6.6](https://github.com/mkdocstrings/python/releases/tag/0.6.6) - 2022-03-06

<small>[Compare with 0.6.5](https://github.com/mkdocstrings/python/compare/0.6.5...0.6.6)</small>

### Code Refactoring
- Always hide `self` and `cls` parameters ([7f579d1](https://github.com/mkdocstrings/python/commit/7f579d162e184adcfe25b2215bce4d38677f75b7) by Timothée Mazzucotelli). [Issue #7](https://github.com/mkdocstrings/python/issues/7)
- Use `pycon` for examples code blocks ([6545900](https://github.com/mkdocstrings/python/commit/6545900eecc67c8a6ddd343c497ac22fdd6a26e2) by Timothée Mazzucotelli).


## [0.6.5](https://github.com/mkdocstrings/python/releases/tag/0.6.5) - 2022-02-24

<small>[Compare with 0.6.4](https://github.com/mkdocstrings/python/compare/0.6.4...0.6.5)</small>

### Bug Fixes
- Don't escape signatures return annotations ([ac54bfc](https://github.com/mkdocstrings/python/commit/ac54bfc5761337aa606fb1aa6575745062ce26f8) by Timothée Mazzucotelli). [Issue #6](https://github.com/mkdocstrings/python/issues/6)


## [0.6.4](https://github.com/mkdocstrings/python/releases/tag/0.6.4) - 2022-02-22

<small>[Compare with 0.6.3](https://github.com/mkdocstrings/python/compare/0.6.3...0.6.4)</small>

### Bug Fixes
- Fix rendering of signature return annotation ([b92ba3b](https://github.com/mkdocstrings/python/commit/b92ba3b370388aa6c956bcc70ba87b7aebb91a4c) by Timothée Mazzucotelli). [Issue #4](https://github.com/mkdocstrings/python/issues/4)


## [0.6.3](https://github.com/mkdocstrings/python/releases/tag/0.6.3) - 2022-02-20

<small>[Compare with 0.6.2](https://github.com/mkdocstrings/python/compare/0.6.2...0.6.3)</small>

### Bug Fixes
- Fix examples rendering ([a06a7e3](https://github.com/mkdocstrings/python/commit/a06a7e34c7017374c5bed41f4757ed86ae64cb2e) by Timothée Mazzucotelli). [Issue mkdocstrings/griffe#46](https://github.com/mkdocstrings/griffe/issues/46)


## [0.6.2](https://github.com/mkdocstrings/python/releases/tag/0.6.2) - 2022-02-17

<small>[Compare with 0.6.1](https://github.com/mkdocstrings/python/compare/0.6.1...0.6.2)</small>

### Bug Fixes
- Catch alias resolution errors ([b734dd0](https://github.com/mkdocstrings/python/commit/b734dd0dcd72f5b985b3afce01e852c9c74e451a) by Timothée Mazzucotelli).


## [0.6.1](https://github.com/mkdocstrings/python/releases/tag/0.6.1) - 2022-02-17

<small>[Compare with 0.6.0](https://github.com/mkdocstrings/python/compare/0.6.0...0.6.1)</small>

### Bug Fixes
- Don't pop from fallback config ([bde32af](https://github.com/mkdocstrings/python/commit/bde32afb5d99539813b1884a4c735de5845f62ae) by Timothée Mazzucotelli).
- Fix rendering init method source when merged into class ([4a20aea](https://github.com/mkdocstrings/python/commit/4a20aeaa60f3efbcb4781a369feef3b4826ff1df) by Timothée Mazzucotelli).


## [0.6.0](https://github.com/mkdocstrings/python/releases/tag/0.6.0) - 2022-02-13

<small>[Compare with 0.5.4](https://github.com/mkdocstrings/python/compare/0.5.4...0.6.0)</small>

### Features
- Add option to merge `__init__` methods' docstrings into their classes' docstrings ([1b4d1c0](https://github.com/mkdocstrings/python/commit/1b4d1c0e9254fc51756caed3875fbc8c1da079a6) by Timothée Mazzucotelli).
- Support separate attribute signature ([e962b88](https://github.com/mkdocstrings/python/commit/e962b885f48570762c5bfcefc9b61e5fc1df1c70) by Timothée Mazzucotelli).

### Bug Fixes
- Restore full cross-refs paths on hover ([ac11970](https://github.com/mkdocstrings/python/commit/ac1197062f2e23e819f144fe74a774d504d0ac49) by Timothée Mazzucotelli).
- Fix rendering of labels ([52919c5](https://github.com/mkdocstrings/python/commit/52919c559378a6006bbe931423c5f03eb5883eaf) by Timothée Mazzucotelli).

### Code Refactoring
- Don't add trailing parentheses in functions heading when separate signature ([885696e](https://github.com/mkdocstrings/python/commit/885696e05606d07334e0428128ed688d54098da1) by Timothée Mazzucotelli).
- Use more explicit template debug messages ([f2122d7](https://github.com/mkdocstrings/python/commit/f2122d7fa119ed055ffe2b2bac72d2c643daca1c) by Timothée Mazzucotelli).


## [0.5.4](https://github.com/mkdocstrings/python/releases/tag/0.5.4) - 2022-02-13

<small>[Compare with 0.5.3](https://github.com/mkdocstrings/python/compare/0.5.3...0.5.4)</small>

### Bug Fixes
- Don't load additional modules during fallback ([69b8e25](https://github.com/mkdocstrings/python/commit/69b8e25cddc9e256c5edb8843592a466023aa124) by Timothée Mazzucotelli).


## [0.5.3](https://github.com/mkdocstrings/python/releases/tag/0.5.3) - 2022-02-08

<small>[Compare with 0.5.2](https://github.com/mkdocstrings/python/compare/0.5.2...0.5.3)</small>

### Bug Fixes
- Allow passing `null` as docstring style ([f526816](https://github.com/mkdocstrings/python/commit/f526816ef1d499795c647e6fe184ba91c1d41b1b) by Timothée Mazzucotelli). [Issue #2](https://github.com/mkdocstrings/python/issues/2)


## [0.5.2](https://github.com/mkdocstrings/python/releases/tag/0.5.2) - 2022-02-05

<small>[Compare with 0.5.1](https://github.com/mkdocstrings/python/compare/0.5.1...0.5.2)</small>

### Dependencies
- Require at least mkdocstrings 0.18 ([7abdda4](https://github.com/mkdocstrings/python/commit/7abdda416e25128eec06f3b15aae5058fbc7320c) by Timothée Mazzucotelli).


## [0.5.1](https://github.com/mkdocstrings/python/releases/tag/0.5.1) - 2022-02-03

<small>[Compare with 0.5.0](https://github.com/mkdocstrings/python/compare/0.5.0...0.5.1)</small>

### Dependencies
- Depend on Griffe >= 0.11.1 ([1303557](https://github.com/mkdocstrings/python/commit/1303557928a27a3d9b063baee9d698458f471357) by Timothée Mazzucotelli).

### Code Refactoring
- Move handler into its own module ([b787e78](https://github.com/mkdocstrings/python/commit/b787e78e31652438039775850e55ea956c22e8d0) by Timothée Mazzucotelli).


## [0.5.0](https://github.com/mkdocstrings/python/releases/tag/0.5.0) - 2022-02-03

<small>[Compare with 0.4.1](https://github.com/mkdocstrings/python/compare/0.4.1...0.5.0)</small>

### Features
- Allow changing docstring style of an object ([39240c1](https://github.com/mkdocstrings/python/commit/39240c1497dced15c03f9046138f2829fc10e139) by Timothée Mazzucotelli).

### Bug Fixes
- Warn if Black is not installed when formatting signature ([b848277](https://github.com/mkdocstrings/python/commit/b84827789b2bf66a4b76ff63a514ec6ba98cae68) by Timothée Mazzucotelli).
- Fix missing default for `docstring_section_style` option ([774988e](https://github.com/mkdocstrings/python/commit/774988ef06a9bf3446949da63611ad7bc5a712fc) by Timothée Mazzucotelli).

### Code Refactoring
- Change to new way of stripping paragraphs ([33d4594](https://github.com/mkdocstrings/python/commit/33d45945bf8ffce2435a6b3749795397fa7c3fc8) by Timothée Mazzucotelli).


## [0.4.1](https://github.com/mkdocstrings/python/releases/tag/0.4.1) - 2022-02-01

<small>[Compare with 0.4.0](https://github.com/mkdocstrings/python/compare/0.4.0...0.4.1)</small>

### Bug Fixes
- Fix docstring admonitions rendering ([a24ae2e](https://github.com/mkdocstrings/python/commit/a24ae2e95f4c0451a44037120451cf06c973ba65) by Timothée Mazzucotelli).


## [0.4.0](https://github.com/mkdocstrings/python/releases/tag/0.4.0) - 2022-02-01

<small>[Compare with 0.3.0](https://github.com/mkdocstrings/python/compare/0.3.0...0.4.0)</small>

### Code Refactoring
- Use the new `mkdocstrings_handlers` namespace ([23c9023](https://github.com/mkdocstrings/python/commit/23c9023780535251778077cd7d957c0067ecb0dc) by Timothée Mazzucotelli).


## [0.3.0](https://github.com/mkdocstrings/python/releases/tag/0.3.0) - 2022-01-14

<small>[Compare with 0.2.0](https://github.com/mkdocstrings/python/compare/0.2.0...0.3.0)</small>

### Features
- Support griffe 0.10 ([28061de](https://github.com/mkdocstrings/python/commit/28061de20094c510f27bb375b2e1dc44a699809d) by Timothée Mazzucotelli).

### Dependencies
- Require griffe 0.10 ([cfbd7bb](https://github.com/mkdocstrings/python/commit/cfbd7bb4761691ef36100962c775ed1d0a247514) by Timothée Mazzucotelli).

### Code Refactoring
- Use new logger patching utility ([4cdb292](https://github.com/mkdocstrings/python/commit/4cdb2921b3a9292db3ef0663c63f148a4eec3966) by Timothée Mazzucotelli).


## [0.2.0](https://github.com/mkdocstrings/python/releases/tag/0.2.0) - 2021-12-28

<small>[Compare with 0.1.0](https://github.com/mkdocstrings/python/compare/0.1.0...0.2.0)</small>

### Dependencies
- Depend on griffe >= 0.7.1 ([34f7ebd](https://github.com/mkdocstrings/python/commit/34f7ebd41f3ebda025ad87e3b52a7226fcb93720) by Timothée Mazzucotelli).
- Upgrade griffe, no upper bound ([8f0aa42](https://github.com/mkdocstrings/python/commit/8f0aa42eed07424a1377708897d92f9894f4abdb) by Timothée Mazzucotelli).

### Features
- Add `show_signature` rendering option ([0f07c2e](https://github.com/mkdocstrings/python/commit/0f07c2e51a51a56eeb5d32fdf05dbed7243f0bc5) by Will Da Silva).

### Bug Fixes
- Fix templates for named docstring elements ([47868a1](https://github.com/mkdocstrings/python/commit/47868a143bf2c462abd5ad85bd0ab8dca7bc5f82) by Timothée Mazzucotelli).


## [0.1.0](https://github.com/mkdocstrings/python/releases/tag/0.1.0) - 2021-12-19

<small>[Compare with first commit](https://github.com/mkdocstrings/python/compare/0032f18c9f902c3e75e0e00114ca8fa6a810c8f5...0.1.0)</small>

### Features
- Implement handler and add templates ([dbb580a](https://github.com/mkdocstrings/python/commit/dbb580aa79f6b2f8a089c80bdc67d0f7457c2d30) by Timothée Mazzucotelli).

### Bug Fixes
- Fix separate signature feature ([da6e81c](https://github.com/mkdocstrings/python/commit/da6e81c897899f09e1dae7bb8930ce6782aeb306) by Timothée Mazzucotelli).
- Fix signature template (parameters annotations) ([b34ead0](https://github.com/mkdocstrings/python/commit/b34ead008773880fd8d1d7a2a41768ec27820520) by Timothée Mazzucotelli).
- Only show source when present ([c270d68](https://github.com/mkdocstrings/python/commit/c270d68c9e17204606ae12a2159c04563a18ec2b) by Timothée Mazzucotelli).

### Code Refactoring
- Return all known anchors ([9bbfe14](https://github.com/mkdocstrings/python/commit/9bbfe1442e2aab28bd6fb2618c943d3f698750ab) by Timothée Mazzucotelli).
- Update for griffe 0.4.0 ([831aabb](https://github.com/mkdocstrings/python/commit/831aabb135db7e75729954adc675af6379f58e24) by Timothée Mazzucotelli).
