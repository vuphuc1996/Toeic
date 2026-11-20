# Command Log Index — TOEIC Dictionary v2.95.14

All commands below were run against the local v2.95.14 candidate source. Exit code 0 unless stated otherwise. Full terminal output is retained in `TOEIC_v2.95.14_Test_Logs.zip`.

| # | Command / activity | Result |
|---:|---|---|
| 1 | `python tools/patch-related-terms.py --root . --patch patches-related-terms/v2.95.14/related-terms-001.json --rollback` | PASS; restored baseline bytes |
| 2 | `sha256sum data/related-terms.json` | Matched base hash `cd9d3c2d948d9d1bb53ed9edd8085818f05289c52e424a7b843bbfdd92e8c9cf` |
| 3 | `python tools/patch-related-terms.py --root . --patch patches-related-terms/v2.95.14/related-terms-001.json --dry-run` | PASS; no data mutation |
| 4 | `python tools/patch-related-terms.py --root . --patch patches-related-terms/v2.95.14/related-terms-001.json --apply` | PASS; 10 glossary rows added |
| 5 | `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_021.py' -v` | 6/6 PASS |
| 6 | `python -m unittest discover -s tools/tests -p 'test_patch_related_terms.py' -v` | 11/11 PASS |
| 7 | `python -m unittest discover -s tools/tests -p 'test_vocabulary_detail_examples.py' -v` | 19/19 PASS |
| 8 | `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v` | 3/3 PASS |
| 9 | `python -m unittest discover -s tools/tests -p 'test_project_progress.py' -v` | 4/4 PASS |
| 10 | `for f in tools/tests/*.mjs; do node "$f"; done` | 38/38 PASS |
| 11 | `python tools/validate-data.py` | PASS; 1,141 records; IDs +0 / missing 0; 0 errors/warnings |
| 12 | `python tools/validate-learning-content.py` | PASS; 0 errors/warnings |
| 13 | `python tools/audit-repository-integrity.py` | PASS; 382 references/data files, 0 errors/warnings |
| 14 | `python tools/sync-version.py --check` | PASS; all version markers 2.95.14 |
| 15 | `python -m py_compile tools/tests/test_related_glossary_batch_021.py` | PASS |
| 16 | `node --check assets/js/app.js`; `node --check sw.js` | PASS |
| 17 | `node tools/tests/vocabulary-release-integrity.mjs` | PASS; v2.95.14/batch 021 included |

## Data hashes

- `data/related-terms.json`: `57c97c32c8d681ebbbb0129e9b21dc0ba3d4c7f8e12731a9d0f54d6a42b83fbc`
- `data/vocabulary/batch-021.json`: `68f616174d85e71cfd4a226ff5902a6d46d3f731caae4836c9f43708e0dd06aa`
- `patches-related-terms/v2.95.14/related-terms-001.json`: `886a6b0111038fc098c0193f9f2f2ebe4715353d7ed6306d6fb6ad7837a1e071`

## Boundaries

- These are local results, not remote GitHub Actions results.
- The full Python test inventory and aggregate discovery were not run to completion.
- Manual owner checks, device testing, Claude review and deployment remain pending.
