# Test Report — TOEIC Dictionary v2.95.17

## Scope

Nine Cambridge-sourced related-term lookup entries, patch safety, version synchronization, project progress reporting, package-tool regression and release-integrity wiring.

## Focused Python tests

| Test module | Result |
|---|---:|
| `test_related_glossary_batch_021.py` | 7/7 PASS |
| `test_related_glossary_batch_022.py` | 9/9 PASS |
| `test_related_glossary_batch_023.py` | 9/9 PASS |
| `test_patch_related_terms.py` | 11/11 PASS |
| `test_package_source.py` | 3/3 PASS |
| `test_ci_coverage.py` | 3/3 PASS |
| `test_project_progress.py` | 4/4 PASS |
| **Total focused Python cases** | **46/46 PASS** |

Python syntax compilation for the changed helper/test modules: PASS.

## JavaScript and project validators

- `node tools/tests/vocabulary-release-integrity.mjs`: **PASS**; includes Batch 023, 396 glossary entries and release version 2.95.17.
- `python tools/validate-data.py`: **PASS** — 1,141 records; ID additions 0 / missing 0; 0 errors / 0 warnings. Stable ID-set SHA-256 remains `adccbdb4c98872207d2bede7bdc530e1c079bbd8b3679e7e4f6288054c7e404b`.
- `python tools/validate-learning-content.py`: **PASS** — Listening 121/239; Reading 65/263; Grammar 50/137; zero errors / zero warnings.
- `python tools/audit-repository-integrity.py`: **PASS** — 388 local references/data files inspected; 0 errors / 0 optional warnings.
- `python tools/sync-version.py --check`: **PASS** — all registered app, Service Worker, HTML and documentation version markers match 2.95.17.
- `python tools/report-project-progress.py`: **PASS** — target-based snapshot generated; exact related-term coverage reports 385/804 (47.9%).

The glossary patch was dry-run tested and then applied with `expect.absent=true`, exact baseline SHA-256 guard and Cambridge host/path validation. Patcher unit tests also cover rollback, refusal to overwrite existing terms, file mode preservation and byte restoration when audit logging fails.

## Release ZIP

- Generated from the clean committed source using `tools/package_source.py`. The archive contains 369 files under exactly one root folder, `Toeic_Dictionary_v2.95.17/`, with zero excluded-path violations (no `.git`, logs, cache, nested archives or release folders).

## Not claimed

- Full Python test inventory or all JavaScript regression suites were not run in this release pass.
- Remote GitHub Actions, GitHub Pages deployment/cache, browser layout, PWA install/offline/reconnect, two-tab update behavior and physical iOS/Android speech output remain unverified.
- All 22 owner-run manual acceptance checks remain **Chưa kiểm**.
- Independent editorial approval for the nine new glosses remains pending.
- No GitHub push or deployment was performed.
