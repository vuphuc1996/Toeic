# Change Manifest — TOEIC Dictionary v2.95.19

## Baseline and candidate

- Baseline source: v2.95.18 FullSource.
- Candidate: v2.95.19.
- Scope: close Listening evidence-pointer gaps; make pending review states explicit; consolidate independent-review handoff; improve progress reporting and CI coverage.

## Data changes

| Area | Change | Guard / boundary |
|---|---|---|
| Listening Part 1–4 reserve records | Added matching `evidenceText` to 29 older questions whose evidence field was missing. | Transcript spans must match exact source text; all reserve statuses stay pending. |
| Listening Part 1 image item | Added `visualEvidenceNote` describing the visible broom/sweeping action. | Explicitly internal visual note; not a second reviewer approval. |
| Listening unit review metadata | Added explicit pending-review notes to 16 legacy units. | No change to `editorialStatus`; all 137 questions remain reserve-pending. |
| Reviewer handoff | Generated a single 280-question queue: 137 Listening, 63 Reading Part 7 and 80 Part 5. | Handoff only; no Mock eligibility or content status changed. |

## Tooling and tests

- Updated `tools/audit-question-evidence.py` to distinguish source-pointer traceability from correctness or editorial approval.
- Added `tools/build-editorial-review-queue.py` and `tools/tests/test_editorial_review_queue.py`.
- Added regression checks for all Listening reserve evidence pointers and review-queue ID coverage.
- Registered review queue compile/test steps in `.github/workflows/validate-data.yml`.
- Updated `tools/report-project-progress.py` to dynamically report pending review counts and the 280-item total; updated its tests and generated `PROJECT_PROGRESS_SNAPSHOT_v2.95.19.md`.
- Updated the release-integrity test to assert the current manifest version rather than the previous fixed release string.
- Restored the historical `docs/archive/PROJECT_HISTORY.md` reference required by the existing distractor-quality test.

## Explicit non-changes

- No visual redesign, CSS/layout refactor, navigation change or new UI module.
- No vocabulary headword, stable ID, IPA, definition, synonym/antonym relation or word-family content change.
- No Listening/Reading/Part 5 prompt, choices, answer key or explanation changed as part of this release.
- No learner progress, localStorage key, IndexedDB schema, backend or runtime API change.
- No pending reserve item promoted to Mock.
- No GitHub push or deployment.

## Files of interest

- `data/listening/listening-library.json`
- `tools/audit-question-evidence.py`
- `tools/build-editorial-review-queue.py`
- `tools/report-project-progress.py`
- `tools/tests/test_listening_expansion.py`
- `tools/tests/test_question_evidence.py`
- `tools/tests/test_editorial_review_queue.py`
- `tools/tests/test_project_progress.py`
- `.github/workflows/validate-data.yml`
- `docs/reports/TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.19.md`
- `docs/reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.19.md`

## Final gate

The source candidate is locally validated and ready for reviewer handoff, not yet accepted for deployment. Independent review, the full Python validator module, remote CI, manual browser/device acceptance and owner approval remain open.
