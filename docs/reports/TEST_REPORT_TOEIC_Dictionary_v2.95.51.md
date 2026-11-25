# Test Report — TOEIC Dictionary v2.95.51

## Python dynamic suite

- Approved roots: `tools/tests`; baseline inventory: v2.95.45 (88 modules).
- Discovered / completed: **90 / 90 modules**.
- Collected cases: **701**.
- Passed / failed / skipped / errored: **700 / 0 / 1 / 0**.
- Timed out / not run / deselected: **0 / 0 / 0**.
- Module outcomes: **89 PASS + 1 PASS WITH SKIPS**.
- Overall: **PASS WITH SKIPS**; all modules reached terminal execution.
- Accepted skip: `test_patch_data.PatchDataTests.test_repository_gitignore_excludes_audit_logs`; reason: `source archive has no Git metadata; gitignore assertion requires a clone`. The exact reason is allowlisted in `tools/test-inventory-policy.json`. The skipped case is not counted as passed.
- Environment: Python 3.13.5 / Node v22.16.0 / Linux x86_64. GitHub Actions workflow targets Python 3.12 / Node 24; remote hosted execution is still required to confirm that environment.
- Machine-readable evidence: `/mnt/data/toeic_v29551_python_suite_final4/PYTHON_TEST_SHARDS_v2.95.51.json` and `.md`.

## Focused glossary tests

- `test_related_glossary_quality_audit.py`: **15/15 PASS** (quality audit, deterministic frequency queue, read-only guarantees, Batch 040 patch reconstruction).
- `test_related_glossary_backfill_025.py`: **6/6 PASS**.
- `test_related_glossary_batch_034.py`: **6/6 PASS**.
- `test_related_glossary_batch_035.py`: **5/5 PASS**.
- `test_related_glossary_batch_036.py`: **6/6 PASS**.
- `test_related_glossary_batch_037.py`: **7/7 PASS**.
- `test_related_glossary_batch_038.py`: **8/8 PASS**.
- `test_related_glossary_batch_039.py`: **4/4 PASS**.
- Candidate audit: **4/4 PASS**; backlog: **3/3 PASS**.
- Batch 040 guarded patch dry-run: PASS; exact base hash is reconstructed by regression test.

## Data and project audits

- `tools/validate-data.py`: **PASS**, 1,141 vocabulary records; zero ID additions/removals; 0 ERROR / 0 WARNING. ID-set SHA-256 prefix `adccbdb4c9887220`.
- `tools/audit-learning-outcomes.py`: **PASS**, 11 objectives / 33 criteria; 6/33 have evidence-collection paths; Foundation 6/6. Wiring does not certify mastery.
- `tools/audit-objective-resources.py`: **PASS**, 379/379 resource links.
- `tools/sync-version.py --check`: **PASS**, all 13 version markers and changelog heading aligned to 2.95.51.
- Python syntax checks for new queue tool and modified tests: **PASS**.

## CI and production boundary

- Complete local shell replay of `.github/workflows/validate-data.yml`: **112/112 run steps PASS**, 0 fail / timeout / error / pending. This is a local command replay, not a hosted GitHub Actions run.
- GitHub-hosted Actions, GitHub Pages deployment, installed-PWA cache update, offline behavior and physical iOS/Android/tablet/desktop acceptance: **UNVERIFIED** until performed on the hosted product.
- Independent editorial review of six Batch 040 Cambridge paraphrases remains pending; multi-sense entries require extra review.

## Overall result

**Source/package candidate: local validation PASS WITH SKIPS. Production acceptance is not granted.**
