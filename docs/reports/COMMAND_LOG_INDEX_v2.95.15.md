# Command Log Index — TOEIC Dictionary v2.95.15

All commands below were run against the local v2.95.15 candidate. Exit code 0 unless an initial test-maintenance issue is explicitly noted.

| # | Command | Result |
|---:|---|---|
| 1 | `python tools/patch-related-terms.py --root . --patch patches-related-terms/v2.95.15/related-terms-001.json --dry-run` | PASS; four operations, no target mutation |
| 2 | `python tools/patch-related-terms.py --root . --patch patches-related-terms/v2.95.15/related-terms-001.json --apply` | PASS; four glosses added |
| 3 | `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_022.py' -v` | PASS; 9/9 |
| 4 | `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_021.py' -v` | PASS; 7/7 |
| 5 | `python -m unittest discover -s tools/tests -p 'test_patch_related_terms.py' -v` | PASS; 11/11 |
| 6 | `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v` | PASS; 3/3 |
| 7 | `python -m unittest discover -s tools/tests -p 'test_release_rotation.py' -v` | PASS; 6/6 |
| 8 | `python tools/validate-data.py` | PASS; 1,141 records, 0 errors / 0 warnings |
| 9 | `python tools/validate-learning-content.py` | PASS; 0 errors / 0 warnings |
| 10 | `python tools/audit-repository-integrity.py` | PASS; 384 files, 0 errors / 0 optional warnings |
| 11 | `python tools/sync-version.py --check` | PASS; all markers 2.95.15 |
| 12 | `node tools/tests/vocabulary-release-integrity.mjs` | PASS; 1,141 canonical records, batch 022 and release version verified |
| 13 | `for f in tools/tests/*.mjs; do node "$f"; done` | PASS; 38/38 suites |
| 14 | `node --check sw.js` and `node --check` for each `assets/js/*.js` | PASS |
| 15 | `python -m compileall -q tools` | PASS |
| 16 | Rollback in disposable workspace + SHA-256 comparison with patch baseline | PASS; exact baseline restored |

## Test-maintenance note

The first JS release-integrity invocation after version bump failed because its expected version literal was still `2.95.14`. The assertion was updated to `2.95.15`; the release-integrity test and the complete 38-suite run then passed. Preserve both the initial failure and successful rerun in the test log archive.

## Scope limitation

Full Python discovery, remote GitHub Actions/Pages, PWA/browser/device acceptance and owner manual checklist were not completed. No push or deployment was performed.
