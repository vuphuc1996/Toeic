# Change Manifest — TOEIC Dictionary v2.95.21

## Baseline and candidate

- Baseline: recovered **v2.95.20 FullSource**.
- Candidate: **v2.95.21**, local source candidate; not pushed or deployed.
- Intent: continue the existing related-term lookup glossary expansion and close a stale progress-test expectation without abandoning the current review backlog.
- UI/CSS/layout/navigation/runtime feature development remains frozen for this content-focused release.

## Data changes

| Area | Change | Guard / boundary |
|---|---|---|
| Related-term glossary Batch 027 | Added 23 Vietnamese lookup glosses: `activity`, `answer`, `carry out`, `combination`, `common`, `continue`, `decrease`, `employee`, `funding`, `goal`, `inaction`, `make`, `minor`, `objective`, `oppose`, `send`, `study`, `support`, `work`, `maximum`, `different`, `determine`, `approach`. | Each term already occurs exactly twice in canonical synonym/antonym relations; each record includes Cambridge Dictionary source URL; additions remain provisional pending independent lexical review. |
| Glossary coverage | Count rises from 400 to 423; exact case-insensitive join rises 389/804 → 412/804 (51.2%); occurrence join rises 598/1,037 → 644/1,037 (62.1%). | 392 distinct terms / 393 relationship occurrences remain unglossed; inventory is not an editorial accuracy score. |
| Patch safety | Added absent-only patch and provenance ledger with the exact baseline file SHA-256. | Patch refuses to overwrite an existing term; dry-run and application were checked against the v2.95.20 baseline. |

## Tooling, tests and documentation

- Added `patches-related-terms/v2.95.21/related-terms-027.json` and `batch-027-glossary-ledger.json`.
- Added `tools/tests/test_related_glossary_batch_027.py` (5 regression tests).
- Updated `.github/workflows/validate-data.yml` to run the new suite and compile the new test module.
- Extended `tools/tests/vocabulary-release-integrity.mjs` to cover the new glossary batches and current 423-entry total.
- Repaired the stale expected coverage in `tools/tests/test_project_progress.py`; regenerated `docs/reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.21.md` from canonical data.
- Restored `docs/archive/PROJECT_HISTORY.md`, a compact retired-document index required by the existing distractor-quality regression; updated the Master Status, current-version pointer, documentation index, and changelog without deleting historical release notes.
- Regenerated the v2.95.21 independent review queue and editorial evidence audit; the 280-question queue remains a handoff only.

## Explicit non-changes

- No canonical vocabulary headword, stable ID, synonym/antonym relation, word-family relation, IPA, learning question, answer key, explanation, learner record, localStorage key or IndexedDB schema changed.
- No UI redesign, CSS/layout/navigation, flashcard, listening playback, TTS, Robot Buddy, PWA service-worker behavior, backend or runtime API change.
- No reserve Listening/Reading/Part 5 item was promoted to Mock eligibility.
- No GitHub push, GitHub Actions remote run or Pages deployment was performed.

## Main files

- `data/related-terms.json`
- `patches-related-terms/v2.95.21/related-terms-027.json`
- `patches-related-terms/v2.95.21/batch-027-glossary-ledger.json`
- `tools/tests/test_related_glossary_batch_027.py`
- `tools/tests/test_project_progress.py`
- `tools/tests/vocabulary-release-integrity.mjs`
- `.github/workflows/validate-data.yml`
- `docs/reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.21.md`
- `docs/reports/VOCABULARY_GLOSSARY_EXPANSION_v2.95.21.md`
- `docs/reports/TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.21.md`
- `docs/reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.21.md`

## Release gate

50 focused Python tests across nine modules and all 38 JavaScript suites pass. Python compile and domain validators pass. Full aggregate Python unittest discovery did not complete within the 240-second execution window and must remain marked incomplete. Remote CI, browser acceptance, physical-device QA, owner manual acceptance and independent lexical/editorial sign-off remain open.
