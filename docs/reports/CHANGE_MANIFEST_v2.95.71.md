# Change Manifest — TOEIC Dictionary v2.95.71

Baseline: exact verified `TOEIC_Dictionary_v2.95.70_FullSource.zip` (SHA-256 `1a0df44d309d127df3d3fb5012e7a6654c93a450c591f1f67575f4d15822e672`; 864 files).

- Added: **30** (includes this manifest and package verification).
- Modified: **18**.
- Deleted: **0**.
- Final source inventory: **894** files.

## Added paths

- `docs/reports/COMMAND_LOG_INDEX_v2.95.71.md`
- `docs/reports/DATA_DIFF_v2.95.71.md`
- `docs/reports/FOUNDATION_A2_ASSESSMENT_QUALITY_v2.95.71.md`
- `docs/reports/LEARNING_OUTCOME_EVIDENCE_MATRIX_v2.95.71.md`
- `docs/reports/MAJOR_RELEASE_QUALITY_AUDIT_v2.95.71.md`
- `docs/reports/NODE_TEST_REPORT_v2.95.71.md`
- `docs/reports/PROJECT_PROGRESS_v2.95.71.json`
- `docs/reports/PROJECT_PROGRESS_v2.95.71.md`
- `docs/reports/PYTHON_TEST_SHARDS_v2.95.71.json`
- `docs/reports/PYTHON_TEST_SHARDS_v2.95.71.md`
- `docs/reports/RELATED_GLOSSARY_BATCH_045_v2.95.71.md`
- `docs/reports/RELATED_GLOSSARY_ENRICHMENT_QUEUE_v2.95.71.json`
- `docs/reports/RELATED_GLOSSARY_ENRICHMENT_QUEUE_v2.95.71.md`
- `docs/reports/RELATED_GLOSSARY_QUALITY_v2.95.71.json`
- `docs/reports/RELATED_GLOSSARY_QUALITY_v2.95.71.md`
- `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.71.md`
- `docs/reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.71.md`
- `docs/reports/TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.71.md`
- `docs/reports/TOEIC_ITEM_COMPLEXITY_REVIEW_v2.95.71.md`
- `docs/reports/WORD_FAMILY_GRAPH_AUDIT_v2.95.71.json`
- `docs/reports/WORD_FAMILY_GRAPH_AUDIT_v2.95.71.md`
- `docs/reports/major-release-quality-audit-v2.95.71.json`
- `patches-related-terms/v2.95.71/batch-045-glossary-ledger.json`
- `patches-related-terms/v2.95.71/related-terms-045.json`
- `tools/project-progress-index.py`
- `tools/project-progress-plan-v2.95.71.json`
- `tools/tests/test_project_progress_index.py`
- `tools/tests/test_related_glossary_batch_045.py`
- `docs/reports/CHANGE_MANIFEST_v2.95.71.md`
- `docs/reports/PACKAGE_VERIFICATION_v2.95.71.md`

## Modified paths

- `.github/workflows/validate-data.yml`
- `CHANGELOG.md`
- `assets/js/app.js`
- `data/manifest.json`
- `data/related-terms.json`
- `docs/CHANGELOG.md`
- `docs/MASTER_STATUS.md`
- `docs/README.md`
- `docs/versions/CURRENT_VERSION.md`
- `docs/versions/PREVIOUS_VERSION.md`
- `index.html`
- `sw.js`
- `tools/tests/glossary_test_helpers.py`
- `tools/tests/related-glossary-quality.mjs`
- `tools/tests/test_ci_coverage.py`
- `tools/tests/test_related_glossary_backfill_025.py`
- `tools/tests/test_related_glossary_batch_044.py`
- `tools/tests/test_related_glossary_candidate_audit.py`

## Deleted paths

- None.

## Change boundaries

- Data changes are limited to `data/manifest.json` and `data/related-terms.json`.
- Related Glossary Batch 045 changes metadata on 23 existing rows only; no term identities, Vietnamese meanings or relation arrays change.
- No learner IndexedDB schema, learner records, question IDs, choice IDs, answer keys or Mock eligibility are changed.
- UI layout is frozen; GitHub Pages/static architecture remains unchanged. No Cloudflare/backend was introduced.
