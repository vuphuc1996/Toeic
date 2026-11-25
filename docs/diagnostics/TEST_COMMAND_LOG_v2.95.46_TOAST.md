# Test Command Log — v2.95.46 Toast Candidate

All commands below were run against the extracted v2.95.46 source, after the Toast candidate patch unless otherwise noted.


| Command | Result |
|---|---|
| `python tools/audit-repository-integrity.py` | PASS: 420 inspected, 0 errors, 0 optional warnings |
| `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v` | PASS: 3/3 |
| `python -m unittest discover -s tools/tests -p 'test_visual_composition.py' -v` | PASS: 9/9 |
| `python -m unittest discover -s tools/tests -p 'test_patch_data.py' -v` | PASS: 20 tests, 1 skipped (Git metadata unavailable) |
| `python tools/validate-data.py` | PASS: 1,141 vocabulary records, 0 errors/warnings, stable ID set |
| `python tools/validate-learning-content.py` | PASS: 0 errors/warnings |
| `python tools/validate-part1-photo-assets.py` | PASS: 9/9 valid |
| `python tools/sync-version.py --check` | PASS: v2.95.46 synchronized |
| `node --check assets/js/app.js` | PASS |
| Workflow py_compile target existence check | PASS: 86/86 present |
| Workflow unittest pattern/module existence check | PASS: 91/91 matched |
| Full unittest discovery | TIMEOUT/INCOMPLETE; partial log `FULL_UNIT_TESTS.log` outside source archive |

