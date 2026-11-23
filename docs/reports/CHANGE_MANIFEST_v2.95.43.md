# Change Manifest — TOEIC Dictionary v2.95.43

## Release scope

Related Glossary Batch 036 (11 sourced relation-target additions), regression/historical test updates, CI registration, version synchronization and generated audit reports. UI layout and learner data are out of scope.

- Modified files: **18**
- Added files: **21** (includes this manifest)
- Deleted files: **0**
- Canonical vocabulary A–Z files: **0 changed**
- Protected learning banks: **0 changed**

## Modified files

- `.github/workflows/validate-data.yml`
- `assets/js/app.js`
- `data/manifest.json`
- `data/related-terms.json`
- `docs/CHANGELOG.md`
- `docs/MASTER_STATUS.md`
- `docs/README.md`
- `docs/reports/RELATED_GLOSSARY_BACKLOG.md`
- `docs/reports/related-glossary-backlog.json`
- `docs/versions/CURRENT_VERSION.md`
- `docs/versions/PREVIOUS_VERSION.md`
- `index.html`
- `sw.js`
- `tools/tests/test_major_release_quality_audit_025.py`
- `tools/tests/test_related_glossary_batch_027.py`
- `tools/tests/test_related_glossary_batch_034.py`
- `tools/tests/test_related_glossary_batch_035.py`
- `tools/tests/test_related_glossary_candidate_audit.py`

## Added files

- `V2.95.43_UPDATE_NOTES.txt`
- `docs/reports/COMMAND_LOG_INDEX_v2.95.43.md`
- `docs/reports/FOUNDATION_A2_ASSESSMENT_QUALITY_v2.95.43.md`
- `docs/reports/LEARNING_OUTCOME_EVIDENCE_MATRIX_v2.95.43.md`
- `docs/reports/MAJOR_RELEASE_QUALITY_AUDIT_v2.95.43.md`
- `docs/reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.43.md`
- `docs/reports/RELATED_GLOSSARY_CANDIDATE_AUDIT_v2.95.43.md`
- `docs/reports/RELATED_GLOSSARY_QUALITY_FLAGS_v2.95.43.json`
- `docs/reports/RELATED_GLOSSARY_QUALITY_FLAGS_v2.95.43.md`
- `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.43.md`
- `docs/reports/TOEIC_CONTENT_COVERAGE_v2.95.43.md`
- `docs/reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.43.md`
- `docs/reports/TOEIC_GLOSSARY_BATCH_036_v2.95.43.md`
- `docs/reports/TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.43.md`
- `docs/reports/VOCABULARY_RELATIONSHIP_GRAPH_AUDIT_v2.95.43.json`
- `docs/reports/VOCABULARY_RELATIONSHIP_GRAPH_AUDIT_v2.95.43.md`
- `docs/reports/major-release-quality-audit-v2.95.43.json`
- `docs/reports/CHANGE_MANIFEST_v2.95.43.md` (this manifest)
- `patches-related-terms/v2.95.43/batch-036-glossary-ledger.json`
- `patches-related-terms/v2.95.43/related-terms-036.json`
- `tools/tests/test_related_glossary_batch_036.py`

## Release boundaries

- Related-term glossary only: 11 records added; no existing term overwritten.
- Six Batch 036 regression tests; CI test and syntax-check registration.
- Historical Batch 027, 034 and 035 tests reconciled to additive batches/current coverage.
- Version markers, changelog, Master, current/previous version and release reports updated.
- No learner IndexedDB data, UI redesign, backend or Cloudflare integration.
