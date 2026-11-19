# Full Repository Audit — TOEIC Dictionary v2.95.7

## 1. Scope

Audited the v2.95.6 source archive and applied a corrective v2.95.7 privacy patch across Robot Buddy runtime, bundled dialogue metadata, visible privacy statements, Service Worker resources, tests, CI registration, release metadata and Master/Compatibility documentation. Canonical TOEIC learning content and learner storage contracts were preserved.

## 2. Critical finding corrected

The v2.95.6 Robot Buddy was described as not opening learner storage directly, but the application passed already-loaded progress snapshots into a separate insight module. That module aggregated vocabulary, flashcard, grammar, reading, listening, Foundation, objective-recall and Mock history data, and its results were used for a personalized dashboard and idle nudges. This still constituted learner-progress access and conflicted with the established requirement that Robot Buddy must not read or analyze learner progress/profile data.

### Corrected in v2.95.7

- Removed `robot-learning-insights.js`, its import, Service Worker app-shell references and the associated insight/dashboard regression suites.
- Removed Robot Buddy's progress snapshot adapter, progress dashboard, analysis toggle, progress-based idle nudges and command-routing paths.
- Robot Buddy now receives no learner progress, answers, mock history or learner profile data. Its runtime uses the static dialogue library, its own onboarding/reminder preferences, current app interaction context and elapsed idle time only.
- Questions about personal progress receive a static privacy explanation and general navigation links to Trang chủ / Ôn tập. This is not a personalized analysis or recommendation.
- Updated library privacy metadata, visible privacy copy, README, Master Status, Compatibility register and changelog. Added `robot-privacy-isolation.mjs` and registered it in GitHub Actions.
- Preserved the head-only mascot, first-use Placement consent flow, quick prompts, reminder toggle, feature shortcuts and ordinary Robot dialogue.

## 3. Regression and validation results

| Check | Result |
|---|---:|
| JavaScript regression suites | 33/33 PASS |
| JavaScript syntax | PASS — all shipped `assets/js/*.js` modules and `sw.js` |
| Python test modules | 53/54 completed and PASS individually; `test_validator.py` did not complete within the local execution window |
| Python `py_compile` | PASS — all Python files under `tools/` |
| CI coverage guard | PASS — all remaining JavaScript suites and Python modules are declared in workflow |
| Vocabulary validator | 1,141 records; 0 errors / 0 new warnings against legacy baseline |
| Learning-content validator | 0 errors / 0 warnings |
| Part 1 media validator | 9/9 JPG assets valid; 0 missing-photo warnings |
| Repository integrity | 359 inspected references/data files; 0 errors; 0 optional warnings |
| Version synchronization | PASS — manifest, app, Service Worker, index and docs all v2.95.7 |
| Design profile | PASS — 54 tokens / 401 selector groups |
| Objective-resource audit | 339/339 links; 11 objectives |
| Question-evidence audit | 502 TOEIC questions indexed |
| Distractor structural audit | PASS — 240 questions in audit scope |
| Foundation A2 assessment audit | PASS — Reading 13/13, Listening 13/13; 39 questions each |
| Listening readiness | 102 eligible; 137 pending independent review; 239 total |

`test_validator.py` was run as a full module but did not finish within the available local execution window. Its isolated `test_missing_optional_cache_asset_is_not_a_structural_error` case passed; the remaining module is not marked complete. No Python assertion failure was observed in completed modules. The remote GitHub Actions workflow remains the authoritative full CI gate.

## 4. Content inventory and editorial debt carried forward

- Vocabulary: 1,141 records; 213 additive IDs relative to the immutable 928-ID baseline; zero missing baseline IDs.
- Grammar: 50 lessons / 137 exercises.
- TOEIC Listening: 121 units / 239 questions; 102 eligible and 137 reserve-pending independent review.
- TOEIC Reading: 65 resources / 263 questions.
- Separate Part 5 practice: 80 questions, practice-only and pending independent review.
- Objective-resource links: 339/339. Outcome registry: 33 criteria, 6 instrumented evidence paths; the remaining 27 remain a separate integration backlog.
- Editorial information remains: 93 records lack US IPA; 338/809 synonym/antonym terms lack individual glosses; four repeated English definition pairs; one word/sense CEFR discrepancy for `package`. These were not silently auto-filled.

## 5. Preservation and non-changes

- No vocabulary, question, answer key, stable content ID or media asset was changed by the privacy correction.
- No learner progress, IndexedDB schema, existing localStorage key or learner record was reset, migrated, deleted or exported.
- Core vocabulary, flashcard, grammar, Listening, Reading, Foundation, Placement and Mock learning flows remain outside the Robot privacy change.
- Robot Buddy's progress-analysis dashboard and its toggle were removed; this is an intentional small UI change to meet the privacy contract.

## 6. External acceptance still required

- Remote GitHub Actions execution and deployed GitHub Pages version/cache are not verified from this local source archive.
- Windows browser acceptance is the first user test gate; iPhone/iPad and Android layout, offline/reconnect and physical TTS quality remain device acceptance items.
- Follow `USER_ACCEPTANCE_TEST_v2.95.7.md`; record PASS / FAIL / NOT TESTED with browser/device details.
