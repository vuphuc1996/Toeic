# Command Log Index — TOEIC Dictionary v2.95.66

All commands were executed locally against the v2.95.65 exact-baseline working tree. Paths are repository-relative unless noted.

| Area | Command / procedure | Result |
|---|---|---|
| Baseline | Verify v2.95.65 FullSource SHA-256 and ZIP CRC | PASS; exact sole predecessor |
| Batch 022 | `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_022.py' -v` | 9/9 PASS |
| Batch 023 | `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_023.py' -v` | 9/9 PASS |
| Batch 035 | `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_035*.py' -v` | 10/10 PASS |
| Release shell coherence | `python -m unittest discover -s tools/tests -p 'test_release_shell_coherence.py' -v` | 6/6 PASS |
| BindEvents DOM | `python -m unittest discover -s tools/tests -p 'test_bind_events_dom_contract.py' -v` | 4/4 PASS |
| CI coverage | `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v` | 8/8 PASS |
| PWA readiness | `python -m unittest discover -s tools/tests -p 'test_pwa_readiness.py' -v` | 3/3 PASS |
| Design system | `python -m unittest discover -s tools/tests -p 'test_design_system.py' -v` | 19/19 PASS |
| Validator release-query regressions | `python -m unittest discover -s tools/tests -p 'test_validator.py' -k release_keyed -v` | 2/2 PASS |
| Python sharded tests | `python tools/run-python-tests-sharded.py --root <repo> --timeout-per-module 60 --report-dir <report-dir> --version 2.95.66 --only <each test_*.py except test_validator.py>` | 100/100 modules; 727/727 cases PASS; 0 fail/skip/error |
| Full validator unittest module | `python -m unittest discover -s tools/tests -p 'test_validator.py' -v` | INCOMPLETE: execution window ended after 21 successful cases; no final module summary. Do not count as PASS. |
| Node regression scripts | `for f in tools/tests/*.mjs; do node "$f"; done` | 43/43 PASS |
| JavaScript syntax | `node --check sw.js`; loop over `assets/js/*.js` copied as `.mjs` | PASS |
| Python syntax | `python -m compileall -q tools` | PASS |
| Version synchronization | `python tools/sync-version.py --check` | 18/18 markers PASS |
| Data validation | `python tools/validate-data.py` | 1,141 records; 0 errors/warnings; IDs +0/-0 |
| Learning content | `python tools/validate-learning-content.py` | 0 errors / 0 warnings |
| Part 1 assets | `python tools/validate-part1-photo-assets.py` | 9/9 PASS |
| Repository integrity | `python tools/audit-repository-integrity.py` | 405 references; 0 errors / 0 warnings |
| Design token audit | `python tools/audit-design-tokens.py` | 0 new violations; 2,773 historical warnings |

The full Python inventory contains 101 modules / 771 unittest cases. The one incomplete module is `test_validator.py`; the separate 2/2 targeted URL-key regression methods passed, as did the production data validator command. Do not report 101/101 full Python suite PASS.
