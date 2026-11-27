# Change Manifest — TOEIC Dictionary v2.95.72

Baseline: exact verified `TOEIC_Dictionary_v2.95.71_FullSource.zip` (`vuphuc1996/Toeic` `main` commit `256ca21461e78a7685bed773ddd622a64050e33a`).

- Added: **25** (including Batch 026 vocabulary files, Batch 046 related terms ledger/patch, and v2.95.72 release audit reports).
- Modified: **22**.
- Deleted: **0**.
- Final source inventory: **919** files.

## Added paths

- `data/vocabulary/batch-026.json`
- `tools/vocabulary-batch-026-cmudict-v2.95.72.json`
- `patches/v2.95.72/batch-001-word-family-expansion.json`
- `patches-related-terms/v2.95.72/related-terms-046.json`
- `patches-related-terms/v2.95.72/batch-046-glossary-ledger.json`
- `tools/tests/test_vocabulary_batch_026.py`
- `tools/tests/test_related_glossary_batch_046.py`
- `docs/reports/PROJECT_PROGRESS_v2.95.72.md`
- `docs/reports/WORD_FAMILY_GRAPH_AUDIT_v2.95.72.md`
- `docs/reports/WORD_FAMILY_GRAPH_AUDIT_v2.95.72.json`
- `docs/reports/MAJOR_RELEASE_QUALITY_AUDIT_v2.95.72.md`
- `docs/reports/major-release-quality-audit-v2.95.72.json`
- `docs/reports/LEARNING_OUTCOME_EVIDENCE_MATRIX_v2.95.72.md`
- `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.72.md`
- `docs/reports/DATA_DIFF_v2.95.72.md`
- `docs/reports/CHANGE_MANIFEST_v2.95.72.md`
- `docs/reports/COMMAND_LOG_INDEX_v2.95.72.md`

## Modified paths

- `.github/workflows/validate-data.yml`
- `CHANGELOG.md`
- `package.json`
- `index.html`
- `sw.js`
- `assets/js/app.js`
- `data/manifest.json`
- `data/related-terms.json`
- `data/vocabulary/A.json`, `B.json`, `C.json`, `D.json`, `E.json`, `F.json`, `H.json`, `K.json`, `N.json`, `O.json`, `P.json`, `R.json`, `S.json`, `T.json`, `U.json`, `V.json`
- `docs/CHANGELOG.md`
- `docs/MASTER_STATUS.md`
- `docs/README.md`
- `docs/versions/CURRENT_VERSION.md`
- `tools/audit-item-complexity.py`
- `tools/backfill-related-glossary-from-vocabulary.py`
- `tools/tests/glossary_test_helpers.py`
- `tools/tests/test_patch_data.py`
- `tools/tests/test_related_glossary_backfill_025.py`

## Change boundaries

- Vocabulary expansion adds 40 canonical headwords resolving missing Word Family graph targets.
- Related Glossary remediation enriches 65 existing rows with Cambridge/Wiktionary provenance and definitions.
- No learner IndexedDB schema, learner records, question IDs, choice IDs, answer keys or Mock eligibility are changed.
- UI layout is frozen; GitHub Pages/static architecture remains unchanged. No Cloudflare/backend was introduced.
