# v2.82.1 — Quick Help word search removal and v2.79 Google AI preservation

## User requirement

Keep every Google AI support action that existed in v2.79.0. Remove all newer v2.80 assistant AI/contextual-transfer additions and explicitly remove the prefix-based word search / masked-letter completion feature from Quick Help. Preserve the TOEIC mock-exam SVG icons and subsequent v2.81/v2.82 learning work.

## Removed

- `assets/js/quick-help.js` vocabulary-prefix matching, masking and completion validation module.
- Quick Help word-search input, suggestions, masked challenge, per-letter entry fields, completion/reveal/details actions.
- Corresponding runtime state, event listeners, handlers and welcome-copy references.
- Word-search styles and generated design-system typography-floor selectors.
- Service Worker REQUIRED/APP_SHELL references to the deleted module.
- The v2.82.0 cache name is retired by bumping the app release to v2.82.1.

## Retained

- All v2.79.0 feature-level Google AI actions: vocabulary detail/unknown-term lookup, practice answer and review analysis, Grammar, Reading and Listening.
- Existing prompt builders, preview panel, privacy disclosure and explicit one-way Google AI Mode user action. No automatic transfer or embedded AI service is added.
- Quick Help greeting, navigation guide and existing Placement Diagnostic entry point. It is not a vocabulary search.
- Mock-exam SVG icons, A2 contextual writing tasks, guided revisions and writing portfolio.
- Existing data and progress storage; no vocabulary/lesson/question changes, no storage schema/key migration, no reset.

## Regression guards

- `tools/tests/legacy-google-ai.mjs` verifies the v2.79 feature-level AI interface and delegated handlers remain.
- `tools/tests/quick-help.mjs` verifies local guide/Placement remains while word-search UI, logic, module, CSS and cache references are absent.
- `tools/tests/learning-assistant.mjs` verifies the v2.80 assistant and Quick Help word-search stay removed.
- `tools/tests/test_ci_coverage.py` verifies every JavaScript suite is invoked by CI.

## Cache compatibility

The Service Worker version changes from v2.82.0 to v2.82.1. This creates a fresh cache namespace so previously cached `quick-help.js` is not retained for updated clients.

## Release boundary

Local source/tests/package checks only. Remote GitHub Actions, public Pages cache behavior and physical-device QA are not claimed until separately observed.
