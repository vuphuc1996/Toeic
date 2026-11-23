# Release Delta — v2.95.42 → v2.95.43

- Baseline: clean extraction of `TOEIC_Dictionary_v2.95.42_FullSource.zip` (612 files; ZIP CRC PASS).
- Candidate: v2.95.43 source (637 files before ZIP packaging).
- Exact content delta: **25 added / 23 modified / 0 removed**; all common files were compared by SHA-256.
- The uploaded .42 ZIP and the previous assistant-built .42 ZIP were byte-identical: 5,254,175 bytes, 612 entries, CRC PASS, SHA-256 `c4e9ad7aba00987a41f122d7a8230ad1f7e71ddc5fd72abf1fdeb820a503823c`.

## Added files

- `docs/reports/COMMAND_LOG_INDEX_v2.95.43.md`
- `docs/reports/FOUNDATION_A2_ASSESSMENT_QUALITY_v2.95.43.md`
- `docs/reports/LEARNING_OUTCOME_EVIDENCE_MATRIX_v2.95.43.md`
- `docs/reports/MAJOR_RELEASE_QUALITY_AUDIT_v2.95.43.md`
- `docs/reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.43.md`
- `docs/reports/PYTHON_TEST_SHARDS_v2.95.43.json`
- `docs/reports/PYTHON_TEST_SHARDS_v2.95.43.md`
- `docs/reports/RELATED_GLOSSARY_BATCH_035_v2.95.43.md`
- `docs/reports/RELATED_GLOSSARY_CANDIDATE_AUDIT_v2.95.43.md`
- `docs/reports/RELATED_GLOSSARY_QUALITY_FLAGS_v2.95.43.json`
- `docs/reports/RELATED_GLOSSARY_QUALITY_FLAGS_v2.95.43.md`
- `docs/reports/RELEASE_DELTA_v2.95.43.md`
- `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.43.md`
- `docs/reports/TEST_VALIDATOR_CASE_BATCHES_v2.95.43.json`
- `docs/reports/TEST_VALIDATOR_CASE_BATCHES_v2.95.43.md`
- `docs/reports/TOEIC_DISTRACTOR_AUDIT_v2.95.43.md`
- `docs/reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.43.md`
- `docs/reports/TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.43.md`
- `docs/reports/TOEIC_LISTENING_READINESS_v2.95.43.md`
- `docs/reports/major-release-quality-audit-v2.95.43.json`
- `patches-related-terms/v2.95.43/batch-035-glossary-ledger.json`
- `patches-related-terms/v2.95.43/related-terms-035.json`
- `tools/run-python-tests-sharded.py`
- `tools/tests/test_python_test_shard_runner.py`
- `tools/tests/test_related_glossary_batch_035_cambridge.py`

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
- `tools/build-editorial-review-queue.py`
- `tools/run-release-acceptance.py`
- `tools/tests/test_editorial_review_queue.py`
- `tools/tests/test_major_release_quality_audit_025.py`
- `tools/tests/test_project_progress.py`
- `tools/tests/test_related_glossary_batch_027.py`
- `tools/tests/test_related_glossary_batch_034.py`
- `tools/tests/test_related_glossary_candidate_audit.py`
- `tools/tests/test_release_acceptance_runner.py`
- `tools/tests/test_vocabulary_detail_examples.py`

## Removed files

None.

## Scope summary

- 26 related-glossary terms added to existing source-headword synonym references, with a SHA-guarded patch and traceability ledger.
- Added resumable Python test runner and grouped execution support for large unittest modules.
- Corrected Editorial Review Queue counts to derive from current Listening reserve data.
- Refreshed historical regression checks to protect immutable source fields while allowing additive metadata and later batches.
- Updated audits, quality metrics, release reports, documentation, CI registration and version markers.
- No canonical vocabulary headwords/IDs, existing synonym/antonym arrays, question/choice/resource IDs, answer keys, learner records, IndexedDB schema, UI layout or Mock eligibility were altered. Batch 035 terms remain subject to independent lexical/pedagogical review.
