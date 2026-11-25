# Command Log Index — TOEIC Dictionary v2.95.51

| Sequence | Command / operation | Result |
|---:|---|---|
| 1 | `python tools/update-related-terms.py --patch patches-related-terms/v2.95.51/related-terms-040.json --dry-run` | PASS — 6 exact-guarded updates; no writes |
| 2 | `python tools/update-related-terms.py --patch patches-related-terms/v2.95.51/related-terms-040.json --apply` | PASS — atomic update of 6 existing rows |
| 3 | `python tools/audit-related-glossary-quality.py` | PASS — 567 rows / 209 flagged |
| 4 | `python tools/build-related-glossary-enrichment-queue.py` | PASS — deterministic read-only queue |
| 5 | `python tools/audit-related-glossary-candidates.py` | PASS — 248 unique uncovered relation terms / 249 occurrences |
| 6 | `python tools/validate-data.py` | PASS — 1,141 records; 0 ID additions/removals; 0 errors / warnings |
| 7 | `python tools/audit-learning-outcomes.py` | PASS — 11 objectives / 33 criteria / 6 evidence paths |
| 8 | `python tools/audit-objective-resources.py` | PASS — 379/379 links |
| 9 | `python tools/sync-version.py --check` | PASS — all 13 markers |
| 10 | Focused Related Glossary regression modules | PASS — all focused modules rerun after historical reconstruction fixes |
| 11 | `python tools/run-python-tests-sharded.py --root . --version 2.95.51 --timeout-per-module 120 ...` | PASS WITH SKIPS — 90 modules / 701 cases; 700 passed / 1 accepted skip |
| 12 | Local replay of all `run:` steps in `.github/workflows/validate-data.yml` | PASS — 112/112 steps |
| 13 | `node tools/tests/related-glossary-quality.mjs` | PASS — 69 placeholders suppressed; valid definitions retained |
| 14 | FullSource and Patch packaging / exact replay | See `PACKAGE_VERIFICATION_v2.95.51.md` |

Full command output and machine-readable summaries are retained in the associated reports and CI replay logs. Hosted GitHub Actions, Pages and device acceptance remain unverified.
