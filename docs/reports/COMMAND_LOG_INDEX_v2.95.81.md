# Command Log Index — TOEIC Dictionary v2.95.81

**Branch:** `candidate`
**Predecessor baseline:** `a16a3e4a51917e687b92e404ab1c785a393dfb0f`
**Release scope:** validator hardening and regression tests; UI and learning-bank data frozen.

| Order | Command | Purpose | Evidence status |
|---:|---|---|---|
| 1 | `python -m unittest discover -s tools/tests -p 'test_objective_criterion_map.py' -v` | Mapping and Part 7 evidence regressions | **PENDING CI** |
| 2 | `python tools/audit-objective-criterion-map.py` | Reconcile canonical mapping IDs, source quotes and reserve gates | **PENDING CI** |
| 3 | `python tools/sync-version.py --check` | Verify all single-instance markers and release-keyed app/SW/mock imports | **PENDING CI** |
| 4 | `python -m unittest discover -s tools/tests -v` | Full discovered Python test inventory | **PENDING CI** |
| 5 | GitHub Validate | Exact candidate source/test acceptance | **PENDING** |
| 6 | GitHub Pages build/deploy | Exact candidate Pages acceptance | **PENDING** |

No local test execution is represented as completed in this index. Hosted CI is the source of acceptance evidence for this candidate commit.
