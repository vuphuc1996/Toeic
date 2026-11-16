# TOEIC Dictionary v2.83.0 — Test & Verification Report

**Date:** 2026-11-16  
**Base:** v2.82.1 Full Source  
**Release:** Robot Buddy first-run onboarding, progress-aware companion behavior, removal of guide/prefix search, and SW002 repair.

## 1. Python regression tests

**160/160 PASS across 22 selected modules.** Each selected module ran to completion. This is not a claim that every Python test module in the repository was executed.

| Module | Tests | Status |
|---|---:|---|
| `test_foundation_production_revision.py` | 6 | PASS |
| `test_foundation_a2_production.py` | 7 | PASS |
| `test_foundation_a2_assessment_quality.py` | 8 | PASS |
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
| `test_release_rotation.py` | 4 | PASS |

The exact GitHub Actions coverage command also passed separately:

```text
python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v
Ran 2 tests
OK
```

## 2. JavaScript regression suites

**27/27 PASS.** Every `tools/tests/*.mjs` suite was executed.

- `learning-assistant.mjs`: verifies first-run footprint detection, latest-attempt per-question summaries, Grammar, Flashcard, Foundation Reading/Listening, A2 writing and Mock summaries, thresholds and no network/Google/API calls from the Robot module.
- `quick-help.mjs`: verifies robot icon/panel, first-run Start/Skip actions, no usage guide, no prefix/masked-letter search, animation/accessibility, mobile layout, offline-cache registration and retained Mock Exam icons.
- `legacy-google-ai.mjs`: verifies all original v2.79 feature-level Google AI actions remain and the withdrawn v2.80 contextual assistant handoff does not return.
- Remaining suites cover runtime render/migration, TTS, Mock Exam, Foundation evidence, A2 writing/revision, objective progress and vocabulary integrity.

## 3. Syntax, design and version checks

| Check | Result |
|---|---|
| Python compile | 66/66 files PASS |
| JavaScript syntax | 14/14 asset files + `sw.js` PASS |
| HTML IDs | 286 IDs; no duplicates |
| CSS parse | `app.css` and `design-system.css`: 0 parse errors |
| Design profile | 54 tokens; 390 legacy font-floor selector groups PASS |
| Version sync | all registered markers v2.83.0 PASS |
| CI coverage | Python/JavaScript coverage guard 2/2 PASS |

## 4. Data and learning validators

| Check | Result |
|---|---|
| `python tools/validate-data.py` | 1,137 records; 0 errors; 0 warnings; SW002 resolved |
| `python tools/validate-learning-content.py` | 0 errors / 0 warnings; Listening 107/201, Reading 51/200, Grammar 33/86, Part 5 practice 80 |
| `python tools/validate-part1-photo-assets.py` | 9/9 valid JPGs |
| `python tools/audit-objective-resources.py` | 294/294 links; 11 objectives |
| `python tools/audit-learning-outcomes.py` | 11/11 objectives; 33 criteria; 6/33 with evidence path |
| `python tools/audit-foundation-a2-assessment.py` | Reading 13/13 resources / 39 questions; Listening 13/13 / 39; source evidence 5/5; answer positions [15,15,15,14] |

Vocabulary field coverage against the 1,137-headword base: US IPA 1,044 (91.8%), word family 276 (24.3%), verb forms 325 (28.6%), collocations 967 (85.0%), synonyms 404 (35.5%), antonyms 213 (18.7%). The 93 records with missing IPA remain unchanged where no source-linked IPA is available.

Counts represent inventory/structure or evidence-collection wiring, not editorial approval, learner mastery, CEFR certification or ETS-equated scores.

## 5. AI / Robot scope verification

**Preserved:** v2.79 feature-level user-triggered Google AI actions at Vocabulary, practice answer/review, Grammar, Reading and Listening, using existing prompt builders, preview and explicit external handoff.

**Withdrawn:** v2.80 shared floating assistant, current-page contextual prompt, follow-up/copy/transfer flow and Quick Help prefix/masked-letter word search.

**New v2.83 Robot Buddy:** deterministic local progress summary and milestone messaging only; no generative model, Google request, API, backend or external transfer. First-run asks whether to start Placement or skip. No usage guide remains.

Mock Exam icons (`icon-clipboard-check`, `icon-bolt`, `icon-stopwatch`, `icon-trophy`) remain.

## 6. Documentation / release rotation

- Release rotation now reads the exact previous release from `docs/versions/PREVIOUS_VERSION.md`, rather than assuming that the previous release is the preceding patch number. This keeps v2.82.1 as the previous release to v2.83.0 and prevents accidental retirement of the wrong version.
- The release-rotation tests cover explicit previous-version selection, dry-run, apply, and archive heading consolidation (4/4). The standalone A2 assessment audit now writes its report using the current manifest version instead of recreating a stale v2.77.0 report on every run.
- Experimental v2.80–v2.82 shared-assistant claims are marked withdrawn in current docs/history; the retained Google AI scope is limited to the original v2.79 feature-level actions.

## 7. Storage and compatibility

- New key: `toeic:robot-companion-onboarding:v1` for the local first-run decision.
- Existing vocabulary, Grammar/Reading/Listening, Foundation, A2 writing portfolio/revision, Mock Exam and Placement progress remain unchanged.
- IndexedDB remains v1; no schema/store migration, no profile reset and no change to `toeic:foundation-progress:v1`.
- `assets/js/learning-assistant.js` and no-op `assets/js/quick-help.js` are registered in both Service Worker `REQUIRED` and `APP_SHELL`. Cache version is 2.83.0.
- Data validator's SW002 error for those two assets is resolved.

## 8. Limits

- Tests and validators were run locally. Remote GitHub-hosted Actions, public Pages deployment/cache behavior and physical-device UX have not been verified in this session.
- The Robot is not a generative AI chatbot. It only summarizes and responds using deterministic local rules and existing data.
- Legacy Google AI remains a third-party external service; its interface and response quality are outside app control.
- Robot suggestions use limited local evidence thresholds and are not diagnostic/CEFR mastery results.
