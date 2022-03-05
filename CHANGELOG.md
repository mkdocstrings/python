# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
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
