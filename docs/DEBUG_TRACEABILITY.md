# Debug & Traceability Map

**Purpose:** isolate reported defects to the smallest relevant code, data, style, asset and test set. This is a source-navigation map, not runtime telemetry. Update it whenever a module boundary, schema, dependency or test owner changes.

## 1. Bug report contract

When reporting a defect, capture only what is available:

- Version/commit and page or feature.
- Exact action immediately before the issue.
- Expected result vs actual result.
- Exact visible error text / console stack / failed CI test name.
- Device, browser, viewport and zoom only when layout/audio/input behavior is involved.
- Whether it reproduces after a hard reload and whether existing learner data is affected.
- Screenshot or short recording when visual; do not export or share learner data/passwords/tokens.

Do not ask the learner to repeat a full-system audit. Start from the failing test, stack frame, DOM selector, data ID or asset path and expand only along the dependency chain below.

## 2. Runtime dependency map

| User-visible area | Entry / primary code | Canonical data | Shared dependencies | Focused tests / validators |
|---|---|---|---|---|
| App shell, navigation, dashboard | `index.html`, `assets/js/app.js` | `data/manifest.json`, `data/categories.json` | `assets/css/app.css`, `assets/css/design-system.css`, `sw.js` | `test_dashboard_layout.py`, `mock-ui-integrity.mjs`, `runtime-render-smoke.mjs` |
| Vocabulary list/detail/search | `assets/js/app.js` | `data/vocabulary/*.json`, `data/related-terms.json` | storage/progress, shared card/modal styles | `test_validator.py`, `test_vocabulary_detail_examples.py`, `test_vocabulary_family_links.py`, `validate-data.py` |
| Grammar lessons/exercises | `assets/js/app.js` | `data/grammar/lessons.json` | question UI, progress/review | `test_grammar_expansion.py`, `test_learning_detail_scope.py`, `test_learning_content.py` |
| Part 5 sentence completion | `assets/js/sentence-completion.js`, `assets/js/app.js` | `data/practice/part5-sentence-completion.json` | question renderer, answer/explanation UI | `test_sentence_completion.py`, `sentence-completion.mjs`, `test_choice_identity.py`, `test_choice_history.py` |
| Listening library and player | `assets/js/app.js` | `data/listening/listening-library.json` | audio/TTS handling, image renderer, `assets/listening/*`, `ATTRIBUTION.csv` | `test_listening_expansion.py`, `test_part1_photo_assets.py`, `listening-tts-regression.mjs`, `audit-listening-readiness.py` |
| Reading library and passages | `assets/js/app.js` | `data/readings/reading-library.json` | question renderer, passage/document layout | `test_reading_expansion.py`, `test_learning_content.py` |
| Mock exams | `assets/js/mock-engine.js`, `assets/js/app.js` | Listening, Reading and Part 5 canonical banks | blueprint, passage/conversation grouping, progress | `mock-exam-engine.mjs`, `test_answer_position_balance.py`, `test_ci_coverage.py` |
| Learning progress / review | `assets/js/practice-progress.js`, `assets/js/app.js` | IndexedDB profile + existing content IDs | storage adapter, review scheduling, shared focus workspace | `practice-progress.mjs`, `learning-focus-workspace.mjs`, `test_baseline_ids.py` |
| PWA install/offline/cache | `sw.js`, `manifest.webmanifest`, `index.html` | app-shell asset lists | all runtime assets and cache version | `test_pwa_readiness.py`, `test_design_system.py` |
| Shared visual system / responsive layout | `assets/css/design-system.css`, `assets/css/app.css`, `index.html` | design tokens in CSS | all screens/components | `test_design_system.py`, `test_dashboard_layout.py`, `flashcard-image-policy.mjs` |
| Release/version metadata | `data/manifest.json`, `sw.js`, `index.html` | docs version markers | `tools/sync-version.py`, release notes | `test_sync_version.py`, `test_release_rotation.py` |

## 3. Data and identity rules

- Canonical content remains in `data/`; do not create a second copy of a word/question to represent another topic. Use tags/relationships where supported.
- Preserve stable vocabulary, lesson, question, choice, passage, unit and resource IDs. A defect fix must not silently regenerate IDs.
- Vocabulary files are alphabet shards plus historical batch files. Before editing, inspect `data/manifest.json` and the loader in `assets/js/app.js` to establish which files are canonical inputs; never assume every batch file is loaded at runtime.
- Listening question media references must resolve to real files. Part 1 photo provenance is centralized in `assets/listening/ATTRIBUTION.csv`; JSON IDs and attribution rows must remain aligned.
- Reading passage/document blocks and Listening conversation/talk groups may be indivisible in mock assembly. Do not split blocks to satisfy a question count.
- IndexedDB contract at v2.41 baseline: database `toeic-vocabulary-phase1`, version 1, object store `workspace`. Do not change schema, clear, migrate or import/export learner data without an explicit migration plan and user authorization.
- Service Worker asset changes must update the relevant cache lists and PWA tests together. Avoid adding optional media to the required app shell without a clear offline requirement.

## 4. Fast diagnosis workflow

1. **Name the failing surface:** route/screen, feature, content ID or asset filename.
2. **Find the first failing boundary:** CI test → validator → console stack → DOM/style selector → canonical JSON reference.
3. **Read only the mapped files:** primary code + canonical data + shared dependency + focused test. Expand only if evidence crosses another boundary.
4. **Reproduce with a focused test** before editing; add a regression test for the reported case.
5. **Patch the smallest layer:** data defect in canonical data; rendering defect in shared renderer; styling defect in shared tokens/component; cache defect in SW + PWA test.
6. **Run targeted tests first**, then adjacent integration checks. Run full suite only when the change crosses shared infrastructure or when targeted results indicate wider risk.
7. **Record exact outcome:** commands, pass/fail counts, warnings, unverified remote/device behavior, affected IDs/files.
8. **Update this map only if dependency ownership changed.** Record release-specific defect/fix in `CURRENT_VERSION.md`, not in a new standalone note for every small bug.

## 5. Focused command index

```bash
# Data and content
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/audit-toeic-coverage.py
python tools/audit-question-evidence.py

# Focused Python tests (replace pattern with the failing module)
python -m unittest discover -s tools/tests -p 'test_learning_content.py' -v
python -m unittest discover -s tools/tests -p 'test_vocabulary*.py' -v
python -m unittest discover -s tools/tests -p 'test_*listening*.py' -v
python -m unittest discover -s tools/tests -p 'test_*reading*.py' -v

# Runtime syntax / PWA / version
node --check assets/js/app.js
node --check assets/js/mock-engine.js
node --check assets/js/practice-progress.js
node --check assets/js/sentence-completion.js
node --check sw.js
python -m unittest discover -s tools/tests -p 'test_pwa_readiness.py' -v
python tools/sync-version.py --check
```

## 6. Do not do this

- Do not scan or rewrite every file for a localized defect before inspecting its stack/test/ID.
- Do not replace a whole module to fix a single content record or CSS selector.
- Do not patch generated/build output when the canonical source is elsewhere.
- Do not update a validator baseline/fingerprint just to make CI green; verify the underlying editorial/data change first.
- Do not mark external GitHub Actions, Pages deployment, mobile device behavior or audio quality as verified unless actually observed.
- Do not include secrets, access tokens, passwords or personal learner records in diagnostics.

## 7. Maintenance ownership

`docs/MASTER_CURRICULUM.md` owns intended learning coverage. `docs/MASTER_STATUS.md` owns current project state and backlog. This file owns code/data/test traceability. `docs/COMPATIBILITY.md` owns schema/runtime compatibility. `docs/versions/CURRENT_VERSION.md` and `PREVIOUS_VERSION.md` own only the latest two release generations. Older release details are summarized in `docs/archive/PROJECT_HISTORY.md`.


## Responsive layout v2.47.0
- Runtime styles: `assets/css/app.css` (final section `v2.47.0 · viewport-first responsive layout system`).
- Main structure: `index.html` (`.sidebar`, `.main-area`, `.topbar`, `.page`, `.mobile-bottom-nav`).
- Data dependencies: none; no IndexedDB/localStorage schema changes.
- Focused checks: `tools/tests/test_responsive_layout.py`; visual QA still requires browser/device verification at the widths listed in `docs/versions/CURRENT_VERSION.md` and `docs/MASTER_STATUS.md`.
