# Change Manifest — v2.95.48

## Purpose

Harden Learning Outcome Evidence reads and writes against malformed local progress data without changing learner records or educational content.

## Source changes

- `assets/js/learning-outcome-progress.js`
  - Defensively build resource index from validated objective/resource arrays; ignore invalid/empty IDs and deduplicate links.
  - Defensively list due recall items and summarize objectives when nested ledger branches are malformed.
  - Reject negative/non-finite timestamps in attempt and explanation-rubric writes; deduplicate objective IDs.
  - Report latest-attempt / current-summary mismatch as a warning; tighten recall-check and rubric timestamp checks.
- `tools/tests/learning-outcome-progress.mjs`: add malformed branch, invalid timestamp, duplicate objective ID and latest-attempt mismatch regression assertions.
- `docs/OBJECTIVE_PROGRESS_INTEGRITY.md`: document defensive semantics and warning behavior.
- Version metadata synchronized to `2.95.48`.
- `docs/MASTER_STATUS.md`, `docs/versions/CURRENT_VERSION.md`, `CHANGELOG.md`, `docs/CHANGELOG.md` and release evidence updated. The package also retains the current source-derived `FOUNDATION_A2_ASSESSMENT_QUALITY_v2.95.48.md` and `TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.48.md` evidence reports.

## Protected content / data

No vocabulary records, headwords, sense identities, synonyms, antonyms, question IDs, choices, answer keys, mock eligibility, learner progress values, IndexedDB schema, UI layout or hosting architecture were intentionally changed. `data/manifest.json` changed only its version string.

## Validation

See `TEST_REPORT_TOEIC_Dictionary_v2.95.48.md`. Full dynamic test suite and remote deployment remain unverified.
