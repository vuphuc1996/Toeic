# Command Log Index — TOEIC Dictionary v2.95.81

**Branch:** `candidate`
**Predecessor baseline:** `a16a3e4a51917e687b92e404ab1c785a393dfb0f`
**Release scope:** validator hardening and regression tests; UI and learning-bank data frozen.

| Order | Command | Purpose | Evidence status |
|---:|---|---|---|
| 1 | `python -m unittest discover -s tools/tests -p 'test_objective_criterion_map.py' -v` | Mapping and Part 7 evidence regressions | **PASS** |
| 2 | `python tools/audit-objective-criterion-map.py` | Reconcile canonical mapping IDs, source quotes and reserve gates | **PASS** |
| 3 | `python tools/sync-version.py --check` | Verify all single-instance markers and release-keyed app/SW/mock imports | **PASS** |
| 4 | `python -m unittest discover -s tools/tests -v` | Full discovered Python test inventory | **PASS** |
| 5 | GitHub Validate | Exact candidate source/test acceptance | **PASS** |
| 6 | GitHub Pages build/deploy | Exact candidate Pages acceptance | **PASS** |

Exact candidate source/test HEAD `047781760d0c34788e9153cc402efdec605c3d5f`: GitHub Validate [run 46118675768](https://github.com/vuphuc1996/Toeic/actions/runs/46118675768) PASS (151/151 steps; 853 Python tests); GitHub Pages [run 46118675714](https://github.com/vuphuc1996/Toeic/actions/runs/46118675714) PASS (build, deploy and status-report). The specific Part 7 test module, mapping audit and version synchronization also passed. No local test execution is claimed.
