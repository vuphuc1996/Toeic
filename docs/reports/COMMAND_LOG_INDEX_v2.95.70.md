# Command Log Index — v2.95.70

All commands below were executed against the extracted `Toeic_Dictionary_v2.95.69` working folder whose `data/manifest.json` had been synchronized to `2.95.70`. Outputs were kept outside the source tree until final report copies were added.

| Command / check | Outcome | Evidence |
|---|---|---|
| `python tools/run-python-tests-sharded.py --root <root> --timeout-per-module 120 --report-dir /mnt/data/v2970_python_test_run --version 2.95.70` with compatible resume | 105/105 modules terminal; 788 PASS, 0 FAIL, 1 accepted SKIP | `PYTHON_TEST_SHARDS_v2.95.70.md/.json` |
| CI Node workflow script block, all 45 scripts | 45/45 PASS | `NODE_TEST_REPORT_v2.95.70.md` |
| JavaScript syntax checks for `assets/js/*.js` and `sw.js` | PASS | Run log `/mnt/data/v2970_node_tests/NODE_TESTS_v2.95.70.log` and validation outputs |
| `python tools/validate-data.py --root <root> --json <outside>/validate-data.json` | 0 errors, 0 warnings; 1,141 IDs; +0/-0 | validation output recorded in test report |
| `python tools/validate-learning-content.py` | 0 errors, 0 warnings | Test report |
| `python tools/audit-repository-integrity.py` | 409 inspected; 0 errors/warnings | Test report |
| `python tools/audit-design-tokens.py --root <root>` | 0 new violations; 2,773 legacy warnings | Test report |
| `python tools/validate-part1-photo-assets.py` | 9/9 valid | Test report |
| `python tools/sync-version.py --root <root> --check` | 18 markers + 17 app imports + 42 SW URLs PASS | Test report |
| `python tools/sync-design-profile.py --check` from source root | 54 tokens + 406 selector groups PASS | Test report |
| Clean baseline ZIP extraction and recursive `data/` byte comparison | 68/68 same paths; manifest version only | `DATA_DIFF_v2.95.70.md` |

A preliminary `sync-design-profile.py --check --root <root>` invocation was invalid because that script does not accept `--root`; it made no source changes. The supported invocation was rerun from the source root and passed. No failed test result was suppressed.
