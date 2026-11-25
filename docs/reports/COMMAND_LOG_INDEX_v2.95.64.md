# Command Log Index — v2.95.64

| Command / scope | Result |
|---|---|
| `sha256sum TOEIC_Dictionary_v2.95.63_FullSource.zip` and sidecar comparison | PASS — exact predecessor verified |
| `unzip -t TOEIC_Dictionary_v2.95.63_FullSource.zip` | PASS |
| `python -m compileall -q tools` | PASS |
| `python tools/sync-version.py --check` | PASS — 13 markers |
| `python tools/audit-repository-integrity.py` | PASS — 363 checks, 0 errors/warnings |
| `python tools/validate-data.py` | PASS — 1,141 records, no errors/new debt |
| `python tools/validate-learning-content.py` | PASS — 0 errors/warnings |
| `python tools/validate-part1-photo-assets.py` | PASS — 9/9 |
| `python tools/audit-answer-leakage.py` | PASS — read-only report |
| `python tools/audit-distractors.py` | PASS — structural audit |
| `python tools/audit-question-evidence.py` | PASS — evidence report |
| `python tools/audit-listening-readiness.py` | PASS — readiness report |
| `python tools/audit-learning-outcomes.py` | PASS — 11/11 objective wiring |
| `node --check sw.js` and all `assets/js/*.js` as ES modules | PASS |
| `node tools/tests/*.mjs` (43 separate scripts) | 43/43 PASS |
| Python focused modules (Git preflight / CI coverage / repository integrity / package source / shard runner / acceptance runner / sync version) | 64 test cases PASS |
| `python tools/run-python-tests-sharded.py --timeout-per-module 180` | INCOMPLETE — 19/97 modules, 144 cases passed; 78 pending at outer execution-window timeout |
| Isolated Foundation A2 assessment quality and production tests | 8/8 + 8/8 PASS |
| YAML BaseLoader parse + workflow structure checks | PASS — 124 steps, unique names, all action references pinned |
| Git commit-readiness staging simulation | Covered by 10/10 integration tests; final staged check is recorded in package verification |

The incomplete full Python-suite result is not promoted to PASS. Remote GitHub Actions and deployed/device tests were not run.
