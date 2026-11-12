# TOEIC Dictionary v2.15.0 — Release Test Report

- **Release:** v2.15.0 — Distractor Quality Audit & Answer-Key Safety
- **Test date:** 10/11/2026
- **Baseline:** exact v2.14.0 release ZIP
- **Scope:** 211-question evidence map; 132-question distractor review; backwards-compatible saved-choice history protection; no vocabulary expansion or database object-store/schema migration.

## 1. Unit-test accounting

**126/126 test methods PASS.** The slow `test_sync_version.py` (12 methods) and `test_validator.py` (33 methods) suites were run one method at a time in the Python 3.13 sandbox because grouped subprocess tests intermittently exceeded the sandbox execution limit. Other suites were run as independent test modules using the same discovery form as the GitHub Actions workflow. This report does not claim that a single monolithic `unittest discover` run passed.

| Suite | Test methods | Result | Execution method |
|---|---:|---|---|
| Baseline ID integrity | 13 | PASS | Module |
| Guarded patch engine | 11 | PASS | Module |
| Version synchronization | 12 | PASS | Each test method independently |
| Vocabulary validator | 33 | PASS | Each test method independently |
| Learning content | 24 | PASS | Module |
| Dashboard layout | 6 | PASS | Module |
| Shared design system | 13 | PASS | Module |
| Answer-to-source evidence audit | 4 | PASS | Module; report regenerated |
| Distractor quality / answer-index safety | 5 | PASS | Module |
| Saved-choice history compatibility | 5 | PASS | Module |
| **Total** | **126** | **PASS** | **All methods accounted for** |

## 2. Data and content validators

### Vocabulary

- 928 records; **0 ERROR**; 12 known legacy warnings (DF005=3, EX006=1, FD001=8 violations across 7 records).
- Added IDs: 0; removed IDs: 0; stable ID-set hash prefix `dd1705e64c8df4ad`.
- IPA 580; word family 131; verb forms 291; collocations 758; synonyms 361; antonyms 213.

### TOEIC learning content

- Listening: 56 units / 102 questions — P1=8, P2=25, P3=39, P4=30.
- Reading: 35 resources / 109 questions — P5=30, P6=16, P7=63.
- Part 7: 38 single-passage / 25 multiple-passage question pool.
- Grammar: 25 lessons / 54 exercises.
- **0 errors, 0 warnings.**

### Editorial evidence and distractors

- All 211 Listening/Reading question keys are mapped to source evidence or an explicitly identified editorial review category.
- 132 Part 3/4/7 questions were reviewed against full transcript/passage, keyed answer and three distractors. Twelve option groups were improved.
- Question IDs, set/question order, correct answer text and `answerIndex` remained unchanged. Only the choice text in the 12 reviewed groups changed.
- Part 3/4/7 answer-position imbalance was documented, not shuffled, because saved `choiceIndex` values rely on option order. A stable `choiceId` and safe legacy progress migration are required before any rebalancing.
- Programmatic checks confirm 4 distinct choice texts and valid answer indices; they do not constitute psychometric validation or independent second-review approval.

## 3. Baseline-preservation checks

Compared against the extracted v2.14.0 ZIP:

- All 31 JSON files under `data/vocabulary/` are byte-identical.
- Listening and Reading set IDs, question IDs and order are unchanged.
- No question `answerIndex` changed; no non-choice question fields changed.
- Exactly 3 Listening and 9 Reading question option groups changed, matching the 12 documented editorial revisions.
- No IndexedDB object-store/schema migration or progress reset was made. The Reading/Listening renderer uses `legacyChoices` for pre-release records; new attempts store `choiceText` alongside the existing `choiceIndex` and `correct` fields.

## 4. Static checks

- Python `py_compile`: PASS for validators, audits, sync-version and patch tooling.
- `node --check sw.js` and all `assets/js/*.js`: PASS.
- GitHub Actions workflow YAML parse: PASS.
- `python tools/sync-version.py --check`: PASS for manifest, Service Worker, HTML and docs markers.
- 206 HTML IDs: unique; APP_SHELL: 74 unique resources, none missing.
- No Markdown files at repository root; Markdown documentation remains under `docs/`.

## 5. Final ZIP integrity

- Archive: `TOEIC_Dictionary_v2.15.0_Distractor_Quality_Audit.zip`
- Files: 164. Archive size and SHA-256 are supplied in an external sidecar so the ZIP does not contain a self-referential digest.
- CRC: PASS; fresh extraction comparison: 164/164 files byte-identical to the release working tree.
- Extracted-package rerun: vocabulary validator, learning-content validator, coverage/evidence/distractor audits, version sync, Python/JavaScript syntax, workflow YAML, 206 unique HTML IDs and 74/74 APP_SHELL resources all PASS.

## 6. Release boundary / known limitations

- Local automated release checks pass. Final ZIP CRC and exact clean-extraction comparison are recorded in `MASTER_STATUS.md` after package construction.
- A local Chromium preview was blocked by the sandbox (`ERR_BLOCKED_BY_ADMINISTRATOR`); no browser visual/interaction QA or physical iPhone, Android, iPad, laptop or PC verification is claimed.
- GitHub Actions remote CI, GitHub commit/push and GitHub Pages deployment have not been run/confirmed.
- No independent second editor, expert psychometric validation, ETS source content, official ETS audio or ETS-equated score is claimed.
- Part 1 remains original SVG illustrations; Listening audio remains browser SpeechSynthesis.
- Next critical data-safety step: add stable `choiceId` values and migrate legacy `choiceIndex` records to those identities before rebalancing answer positions. `choiceText` is now recorded for new Reading/Listening attempts, but index-based history still prevents safe shuffling.
