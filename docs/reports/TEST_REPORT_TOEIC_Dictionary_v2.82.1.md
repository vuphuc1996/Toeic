# TOEIC Dictionary v2.82.1 — Test & Verification Report

**Date:** 2026-11-16  
**Base:** v2.82.0 Full Source  
**Release:** remove Quick Help prefix search/masked-letter completion, preserve v2.79 feature-level Google AI, keep mock-exam icons and A2 portfolio.

## 1. Python regression tests

**151/151 PASS across 21 selected modules.** Each selected module ran to completion. This is not a claim that every Python test module in the repository was executed.

| Module | Tests | Status |
|---|---:|---|
| `test_foundation_production_revision.py` | 6 | PASS |
| `test_foundation_a2_production.py` | 7 | PASS |
| `test_ci_coverage.py` | 2 | PASS |
| `test_sync_version.py` | 12 | PASS |
| `test_design_profile.py` | 6 | PASS |
| `test_learning_content.py` | 34 | PASS |
| `test_foundation_pathway.py` | 10 | PASS |
| `test_foundation_reading.py` | 9 | PASS |
| `test_foundation_listening.py` | 13 | PASS |
| `test_foundation_outcome_evidence.py` | 2 | PASS |
| `test_learning_outcomes.py` | 3 | PASS |
| `test_learning_outcome_progress.py` | 3 | PASS |
| `test_project_progress.py` | 4 | PASS |
| `test_objective_resource_map.py` | 2 | PASS |
| `test_pwa_readiness.py` | 3 | PASS |
| `test_responsive_layout.py` | 5 | PASS |
| `test_learning_surface_consistency.py` | 5 | PASS |
| `test_part1_photo_assets.py` | 6 | PASS |
| `test_sentence_completion.py` | 12 | PASS |
| `test_vocabulary_batch_012.py` | 4 | PASS |
| `test_release_rotation.py` | 3 | PASS |

## 2. JavaScript regression suites

**27/27 PASS.** Every `tools/tests/*.mjs` suite was run.

- `legacy-google-ai.mjs`: protects all pre-v2.80 Google AI controls/functions from v2.79: vocabulary detail/unknown-term lookup, practice answer/review, Grammar, Reading, Listening, shared preview modal and explicit Google Search AI Mode launch (`udm=50`, `hl=vi`).
- `quick-help.mjs`: verifies the offline greeting/navigation guide and Placement Diagnostic remain; the word-prefix search UI, suggestions, masked challenge, letter inputs, completion functions, dedicated module, CSS and Service Worker references are absent.
- `learning-assistant.mjs`: under its historical CI filename, verifies that the v2.80 floating assistant, contextual AI handoff and Quick Help word-completion feature stay removed while Placement/help navigation and mock icons remain.
- Other suites cover runtime render/migration, TTS, mock-exam engine/UI, deferred assessment, Foundation evidence, A2 production/revision and practice progress.

## 3. Syntax, design system and release checks

| Check | Result |
|---|---|
| Python compile | 66/66 source files PASS |
| JavaScript syntax | 12/12 `assets/js/*.js` and `sw.js` PASS |
| HTML parser | PASS; 282 IDs, no duplicate IDs |
| CSS parser | `app.css` and `design-system.css`: 0 parse errors |
| Design profile | 54 tokens; 384 generated legacy font-floor selector groups PASS |
| Version sync | all registered markers v2.82.1 PASS |
| CI coverage | all JavaScript regression suites invoked by workflow; `test_ci_coverage.py` 2/2 PASS |

## 4. Content/data validators

| Check | Result |
|---|---|
| Canonical vocabulary | 1,137 records; 0 errors; 0 warnings |
| Learning Content | Listening 107 units / 201 questions; Reading 51 / 200; Grammar 33 / 86; 0 errors / 0 warnings |
| Separate Part 5 practice | 80 practice-only questions; independent editorial review remains separate |
| Part 1 photos | 9/9 valid |
| Objective-resource links | 294/294; 11 objectives |
| Learning outcomes | 11/11 objectives; 33 criteria; 6/33 with evidence-collection path; Foundation 6/6 instrumented |
| A2 assessment | Reading 13/13 / 39 questions; Listening 13/13 / 39 questions; 5/5 source evidence links |

Counts describe inventory or instrumentation, not learner mastery, CEFR certification, ETS equivalence or editorial approval.

## 5. Retained and removed feature scope

**Retained from v2.79.0:** feature-level Google AI actions at vocabulary detail/unknown-term lookup, practice answer and review, Grammar, Reading and Listening. They use the original prompt builders, preview modal, privacy disclosure and explicit one-way Google Search handoff. The browser leaves the app only after the learner presses the original action. No model/API/backend or hidden call is added.

**Removed from v2.80.0:** shared floating Learning Assistant, contextual prompt/follow-up/copy/transfer, Google AI action inside that assistant, plus prefix-based Quick Help search, suggestion list, masked headwords, character-entry challenge, validation/reveal and detail-open shortcuts.

**Quick Help remaining:** greeting, in-app guide/navigation, existing Placement Diagnostic entry. It does not search vocabulary or contact external services.

**Preserved from v2.80+:** mock exam SVG icons (`icon-clipboard-check`, `icon-bolt`, `icon-stopwatch`, `icon-trophy`), A2 guided writing, revision history and writing portfolio.

## 6. Storage and compatibility

- No vocabulary, lesson, question, choice or mock pool data was changed.
- A2 writing data remains under `toeic:foundation-progress:v1`; existing `::apply1` and `::produce1` IDs remain isolated.
- IndexedDB remains v1. No new localStorage key, store, schema migration or progress reset.
- Service Worker version changes from 2.82.0 to 2.82.1 to create a fresh cache namespace and retire the deleted `quick-help.js` module from the old offline cache.

## 7. Release package verification

- Full Source ZIP and TAR.GZ each contain **253 files**; no `__pycache__`, `*.pyc` or deleted Quick Help module is included.
- Both archives were extracted independently. Relative paths and per-file SHA-256 digests match the source **253/253** for ZIP and **253/253** for TAR.GZ.
- Archive-level SHA-256 sidecars were generated and verified against the final ZIP/TAR.GZ bytes.
- The extracted ZIP was used to re-run the **27/27 JavaScript suites**, **151/151 selected Python tests across 21 modules**, version/design checks and the core data/content/objective/outcome validators.
- The extracted TAR.GZ passed smoke tests for the Quick Help removal guard, v2.79 legacy Google AI, mock-exam icons, runtime rendering and the main validators.

## 8. Limits

- Local tests do not prove remote GitHub Actions passed.
- GitHub Pages deployment/cache behavior and physical-device QA have not been checked in this session.
- Google AI remains an external third-party service; URL parameter handling and response quality are outside app control.
- A2 self-ratings are learner self-reports, not automated writing grading or mastery certification.
