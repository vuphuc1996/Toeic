# Change Manifest — TOEIC Dictionary v2.95.42

## Summary

- Base Full Source: **v2.95.41**
- Release Full Source: **v2.95.42**
- Related Glossary Batch 035: 8 sourced relation-target entries
- Release tree comparison (excluding package artifacts, audit logs and cache files): **17 modified / 22 added / 0 deleted** before this manifest was added; this manifest itself is one additional added file.
- Final patch overlay therefore contains **17 modified / 23 added / 0 deleted = 40 source files**.
- Full Source: 620 source files. Patch ZIP: 40 overlay files + 2 metadata files.
- Patch replay: v2.95.41 baseline + overlay/deletions exactly matches v2.95.42 release tree byte-for-byte.

## Modified files

- `.github/workflows/validate-data.yml`
- `assets/js/app.js`
- `data/manifest.json`
- `data/related-terms.json`
- `docs/CHANGELOG.md`
- `docs/MASTER_STATUS.md`
- `docs/README.md`
- `docs/reports/RELATED_GLOSSARY_BACKLOG.md`
- `docs/reports/RELATED_GLOSSARY_CANDIDATE_AUDIT_CURRENT.md`
- `docs/reports/related-glossary-backlog.json`
- `docs/versions/CURRENT_VERSION.md`
- `docs/versions/PREVIOUS_VERSION.md`
- `index.html`
- `sw.js`
- `tools/tests/test_major_release_quality_audit_025.py`
- `tools/tests/test_related_glossary_batch_034.py`
- `tools/tests/test_related_glossary_candidate_audit.py`

## Added files (excluding this manifest)

- `V2.95.42_UPDATE_NOTES.txt`
- `docs/reports/COMMAND_LOG_INDEX_v2.95.42.md`
- `docs/reports/FOUNDATION_A2_ASSESSMENT_QUALITY_v2.95.42.md`
- `docs/reports/LEARNING_OUTCOME_EVIDENCE_MATRIX_v2.95.42.md`
- `docs/reports/MAJOR_RELEASE_QUALITY_AUDIT_v2.95.42.md`
- `docs/reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.42.md`
- `docs/reports/RELATED_GLOSSARY_CANDIDATE_AUDIT_v2.95.42.md`
- `docs/reports/RELATED_GLOSSARY_QUALITY_FLAGS_v2.95.42.json`
- `docs/reports/RELATED_GLOSSARY_QUALITY_FLAGS_v2.95.42.md`
- `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.42.md`
- `docs/reports/TOEIC_CONTENT_COVERAGE_v2.95.42.md`
- `docs/reports/TOEIC_DISTRACTOR_AUDIT_v2.95.42.md`
- `docs/reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.42.md`
- `docs/reports/TOEIC_GLOSSARY_BATCH_035_v2.95.42.md`
- `docs/reports/TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.42.md`
- `docs/reports/TOEIC_LISTENING_READINESS_v2.95.42.md`
- `docs/reports/VOCABULARY_RELATIONSHIP_GRAPH_AUDIT_v2.95.42.json`
- `docs/reports/VOCABULARY_RELATIONSHIP_GRAPH_AUDIT_v2.95.42.md`
- `docs/reports/major-release-quality-audit-v2.95.42.json`
- `patches-related-terms/v2.95.42/batch-035-glossary-ledger.json`
- `patches-related-terms/v2.95.42/related-terms-035.json`
- `tools/tests/test_related_glossary_batch_035.py`

## Added by this manifest

- `docs/reports/CHANGE_MANIFEST_v2.95.42.md`

## Deleted files

- None

## Release boundary

- No canonical vocabulary IDs/headwords, relation arrays, learning question/answer keys, Mock eligibility, learner data/IndexedDB, UI or backend configuration changed.
- Cambridge indexed excerpts were used; direct entry opens returned HTTP 403. Independent editorial review remains pending.
