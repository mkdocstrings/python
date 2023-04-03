# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
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
