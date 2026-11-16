# TOEIC Dictionary v2.82.0 — Test & Verification Report

**Date:** 2026-11-16  
**Base:** v2.81.0 Full Source, with the exact legacy Google AI feature contract restored from v2.79.0  
**Release:** Restore pre-v2.80 Google AI actions; keep v2.80 assistant AI handoff removed; preserve local Quick Help and A2 writing portfolio.

## 1. Python regression tests

**151/151 PASS across 21 selected modules.** These selected modules were each run to completion; this is not a claim that every `test_*.py` file in the repository was executed.

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

**26/26 PASS.** Every `tools/tests/*.mjs` suite was executed, including:

- `legacy-google-ai.mjs`: verifies v2.79 feature-level Google AI actions are restored for vocabulary, unknown-term lookup, practice answer/review, Grammar, Reading and Listening; checks modal controls, explicit URL construction, user-triggered outbound action, and style presence.
- `quick-help.mjs`: verifies local navigation, Placement Diagnostic entry, canonical vocabulary prefix search, masked completion, exact answer validation, offline Service Worker wiring and responsive behavior. It also ensures Quick Help contains no Google AI action.
- The two suites separately assert that v2.80 assistant-specific contextual AI, copy/transfer and Google follow-up actions remain absent.
- Runtime render/migration, TTS, Mock exam engine/UI, A2 writing production/revision, Foundation evidence, practice progression and other existing regression suites all PASS.

## 3. Syntax and design-system checks

| Check | Result |
|---|---|
| Python compile | 66/66 source files PASS |
| JavaScript syntax | 13/13 `assets/js/*.js` plus `sw.js` PASS |
| HTML parser | `index.html` parsed without parser exception |
| CSS parser | `assets/css/app.css` and `design-system.css`: 0 parse errors |
| Design profile | 54 tokens and 393 legacy font-floor selector groups PASS |
| Version sync | All registered release markers v2.82.0 PASS |
| CI coverage | Every `.mjs` suite is declared in `.github/workflows/validate-data.yml`; 2/2 Python coverage checks PASS |

Two malformed `quick-helpRoot` identifiers inherited from v2.81.0 were corrected to the valid `quickHelpRoot` identifier; the current app source now passes JavaScript syntax checking.

## 4. Data and content validators

| Check | Result |
|---|---|
| Canonical vocabulary | 1,137 records; 0 errors; 0 warnings |
| Learning Content | Listening 107 units / 201 questions; Reading 51 / 200; Grammar 33 / 86; 0 errors / 0 warnings |
| Separate Part 5 practice | 80 questions; practice-only / independent review pending |
| Part 1 photos | 9/9 valid; attribution checked |
| Objective-resource links | 294/294; 11 objectives |
| Learning outcomes | 11/11 objectives; 33 criteria; 6/33 with an evidence-collection path; Foundation 6/6 instrumented |
| CMUdict IPA | 333 source-linked records PASS |
| A2 assessment audit | Reading 13/13 / 39 questions; Listening 13/13 / 39 questions; 5/5 source-evidence links; answer positions [15,15,15,14] |

Inventory and instrumentation counts do not represent learner completion, editorial approval, CEFR/ETS equivalence or mastery.

## 5. Google AI scope verification

- Restored the feature-level Google AI prompt builders and action controls from v2.79.0: vocabulary detail/unknown lookup, practice answer/review, Grammar, Reading and Listening.
- Restored the one-way preview modal and explicit Google Search AI Mode launch (`udm=50`, `hl=vi`). The query is created locally and the browser is opened only after the learner clicks the run button.
- No embedded model, API key, backend, proxy, hidden prompt submission or background network call is added.
- The new v2.80 floating-assistant contextual Google AI prompt/follow-up/copy/transfer path remains absent. Quick Help itself is local-only.
- `ai-generated` in the image attribution ledger remains source metadata, not an AI runtime integration.

See `RESTORE_LEGACY_GOOGLE_AI_v2.82.0.md` for the exact restored/removed boundary.

## 6. Storage and compatibility

- A2 portfolio/revision history continues to use `toeic:foundation-progress:v1`.
- Existing `::apply1` and `::produce1` IDs remain isolated.
- IndexedDB remains v1; no new store, migration, localStorage key or progress reset.
- Canonical vocabulary, Foundation lesson/question IDs, Reading/Listening bank IDs and TOEIC Mock pools are unchanged by this corrective release.

## 7. Release package verification

- Full Source ZIP and TAR.GZ each contain **253 files**.
- Both archives were extracted independently into separate verification directories.
- Relative file paths and SHA-256 digests were compared against the canonical release source: **253/253 files match** for ZIP and **253/253 files match** for TAR.GZ.
- Archive-level SHA-256 sidecars were generated and verified against the final ZIP/TAR.GZ bytes. The sidecars are distributed beside the archives, not embedded inside them.
- The final archives exclude Python bytecode/cache artifacts (`__pycache__`, `*.pyc`).
- The extracted ZIP was used for the full selected regression run: **26/26 JavaScript suites and 151/151 Python tests across 21 modules**. The extracted TAR.GZ passed the Quick Help, legacy Google AI and runtime smoke tests, plus the data, learning-content, Part 1 image, objective-resource, learning-outcome, CMUdict, version-sync and design-profile validators.

The externally distributed SHA-256 sidecars are the authoritative whole-archive checksums. Individual file hashes were compared separately during the independent extraction check.

## 8. Limits

- Local tests do not prove that remote GitHub Actions passed.
- GitHub Pages deployment/cache behavior has not been checked in this session.
- No physical-device QA on iOS/Android/tablets/laptops is claimed.
- Google AI is an external third-party product; availability, query parameter handling and response quality are outside app control.
- Self-ratings are not automated language grading, TOEIC scoring, CEFR certification or proof of mastery.
