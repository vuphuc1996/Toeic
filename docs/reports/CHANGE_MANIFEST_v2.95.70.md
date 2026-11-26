# Change Manifest — TOEIC Dictionary v2.95.70

Baseline: verified `TOEIC_Dictionary_v2.95.69_FullSource.zip` (SHA-256 `4ec559a2117a1b1b38ef95d4a0d6955431b46e701cf208bd939bd38db232e853`; 847 files).

- Added: **17** (includes this manifest).
- Modified: **15**.
- Deleted: **0**.
- Final target inventory: **864** files (including this manifest).

## Added paths

- `docs/reports/COMMAND_LOG_INDEX_v2.95.70.md`
- `docs/reports/DATA_DIFF_v2.95.70.md`
- `docs/reports/FOUNDATION_A2_ASSESSMENT_QUALITY_v2.95.70.md`
- `docs/reports/LEARNING_OUTCOME_EVIDENCE_MATRIX_v2.95.70.md`
- `docs/reports/MAJOR_RELEASE_QUALITY_AUDIT_v2.95.70.md`
- `docs/reports/NODE_TEST_REPORT_v2.95.70.md`
- `docs/reports/PACKAGE_VERIFICATION_v2.95.70.md`
- `docs/reports/PYTHON_TEST_SHARDS_v2.95.70.json`
- `docs/reports/PYTHON_TEST_SHARDS_v2.95.70.md`
- `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.70.md`
- `docs/reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.70.md`
- `docs/reports/TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.70.md`
- `docs/reports/TOEIC_ITEM_COMPLEXITY_REVIEW_v2.95.70.md`
- `docs/reports/major-release-quality-audit-v2.95.70.json`
- `tools/tests/assessment-one-way-confirmation.mjs`
- `tools/tests/test_assessment_one_way_confirmation.py`
- `docs/reports/CHANGE_MANIFEST_v2.95.70.md`

## Modified paths

- `.github/workflows/validate-data.yml`
- `CHANGELOG.md`
- `assets/js/app.js`
- `data/manifest.json`
- `docs/ASSESSMENT_FLOW.md`
- `docs/CHANGELOG.md`
- `docs/MASTER_STATUS.md`
- `docs/README.md`
- `docs/versions/CURRENT_VERSION.md`
- `index.html`
- `sw.js`
- `tools/tests/assessment-result-focus-workflow.mjs`
- `tools/tests/foundation-evidence.mjs`
- `tools/tests/test_choice_history.py`
- `tools/tests/test_distractor_quality.py`

## Deleted paths

- None.

## Scope summary

- Runtime changes are limited to the assessment result completion surface and Foundation confirmation persistence ordering.
- Tests cover the one-action result CTA, removed return routes, storage-failure retention and successful persist-before-reveal.
- CI registers the new Node behavioral regression; Python and historical test boundaries are updated.
- Release version markers, changelogs, Master/Current Version documentation and release evidence are updated.
- `data/` contains no content changes: only `data/manifest.json` release version changes `.69`→`.70`.
- No new learner data migration, IndexedDB schema change, vocabulary/question/choice/answer-key modification, or UI layout redesign.
