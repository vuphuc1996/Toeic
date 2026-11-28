# Command Log Index — TOEIC Dictionary v2.95.78

**Verified candidate:** `0187b446123fca1a8708b496e971e18b19a46c57`

Hosted execution evidence: GitHub Validate [run 46100106836](https://github.com/vuphuc1996/Toeic/actions/runs/46100106836) and GitHub Pages build/deploy [run 46100106757](https://github.com/vuphuc1996/Toeic/actions/runs/46100106757), both on the exact candidate SHA.

| Order | Command / CI action | Purpose | Evidence status |
|---:|---|---|---|
| 1 | `python tools/audit-objective-criterion-map.py` | Validate 1,082 stable question links, question IDs/indices, objective ownership, review gates and Listening reserve exclusion | **PASS** |
| 2 | `python -m unittest discover -s tools/tests -p 'test_objective_criterion_map.py' -v` | Mapping-audit regression | **PASS** |
| 3 | `python -m unittest discover -s tools/tests -p 'test_learning_outcomes.py' -v` | Outcome registry and evidence report | **PASS** |
| 4 | `python -m unittest discover -s tools/tests -p 'test_learning_outcome_progress.py' -v` | Group and criterion runtime behavior | **PASS** |
| 5 | `node tools/tests/learning-outcome-criterion-progress.mjs` | Accuracy, timed accuracy, self-report rubric, recall and editorial gates | **PASS** |
| 6 | `python -m unittest discover -s tools/tests -p 'test_project_progress_index.py' -v` | 73.73% provisional weighted build index and criterion counts | **PASS** |
| 7 | `python -m unittest discover -s tools/tests -p 'test_project_progress.py' -v` | Target-based project progress output | **PASS** |
| 8 | `python tools/sync-version.py --check` | Release markers, module imports and Service Worker cache keys | **PASS** |
| 9 | `python tools/validate-data.py` | Vocabulary IDs, manifest, Service Worker shell and data constraints | **PASS** |
| 10 | Full Python test discovery | All discovered Python modules | **846 tests PASS; 0 failure; 0 skip** |
| 11 | GitHub Validate | Exact-commit hosted source acceptance | **PASS** |
| 12 | GitHub Pages build and deployment | Exact same-commit deployment acceptance | **PASS** |

Installed-PWA/offline propagation and physical-device QA are not implied by the hosted CI and Pages checks.
