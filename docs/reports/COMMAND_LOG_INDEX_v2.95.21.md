# Command Log Index — TOEIC Dictionary v2.95.21

> Commands were executed against the local candidate source. This index records outcomes; it does not imply remote CI or deployment.

| Command / check | Result |
|---|---|
| `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_027.py' -v` | PASS — 5 tests |
| `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_026.py' -v` | PASS — 5 tests |
| `python -m unittest discover -s tools/tests -p 'test_patch_related_terms.py' -v` | PASS — 11 tests |
| `python -m unittest discover -s tools/tests -p 'test_project_progress.py' -v` | PASS — 4 tests |
| `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v` | PASS — 3 tests |
| `python -m unittest discover -s tools/tests -p 'test_sync_version.py' -v` | PASS — 12 tests |
| `python -m unittest discover -s tools/tests -p 'test_distractor_quality.py' -v` | PASS — 6 tests |
| `python -m unittest discover -s tools/tests -p 'test_repository_integrity.py' -v` | PASS — 1 test |
| `python -m unittest discover -s tools/tests -p 'test_package_source.py' -v` | PASS — 3 tests |
| `python -m compileall -q tools` | PASS |
| Run every `tools/tests/*.mjs` file with `node` | PASS — 38/38 suites |
| `node --check sw.js` and Node syntax-check of each `assets/js/*.js` file | PASS |
| `node tools/tests/vocabulary-release-integrity.mjs` | PASS |
| `python tools/validate-data.py` | PASS — 1,141 records, 0 errors / 0 warnings; 0 ID additions / 0 missing |
| `python tools/validate-learning-content.py` | PASS — 0 errors / 0 warnings |
| `python tools/audit-repository-integrity.py` | PASS — 393 references, 0 errors / 0 optional warnings |
| `python tools/audit-question-evidence.py` | PASS — 502 indexed questions; wrote v2.95.21 evidence audit |
| `python tools/sync-version.py --check` | PASS — all markers synchronized to 2.95.21 |
| `python -m unittest discover -s tools/tests -p 'test_*.py' -v` | INCOMPLETE — execution limit reached at 240 seconds while running aggregate Python discovery; no overall result claimed |

## Patch execution record

- Patch: `patches-related-terms/v2.95.21/related-terms-027.json`.
- Ledger: `patches-related-terms/v2.95.21/batch-027-glossary-ledger.json`.
- Preconditions: exact baseline SHA-256 and `expect.absent=true` for each addition.
- Dry-run and apply were completed in the local candidate workspace; the dedicated patch-safety regression suite passed 11/11.
- The patch changes explanatory lookup glossary records only; canonical synonym/antonym relationships are not rewritten.

## Clean baseline replay and packaging

- Replayed Batch 027 from a pristine v2.95.20 glossary file using the recorded SHA-256 precondition. Output matched the candidate `data/related-terms.json` byte-for-byte.
- FullSource ZIP: one root, 412 project files. Update patch: 13 modified + 12 new files, no deletions. ZIP layout and per-file hashes were verified.

## External / manual gates

- Remote GitHub Actions: not run / not verified.
- GitHub Pages push and deployment: not performed.
- Browser, PWA/offline, multi-tab and physical-device checks: not performed in this environment.
- Owner acceptance and independent content review: pending.
