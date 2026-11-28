# Command Log Index — TOEIC Dictionary v2.95.78

This index records the reproducible checks associated with the v2.95.78 candidate. Results are intentionally left pending until GitHub Actions runs on the exact commit.

| Order | Command | Purpose | Evidence status |
|---:|---|---|---|
| 1 | `python tools/audit-objective-criterion-map.py` | Resolve every stable question link against canonical banks; verify 22/27 criteria and no Listening reserve mappings | Pending CI |
| 2 | `python -m unittest discover -s tools/tests -p 'test_objective_criterion_map.py' -v` | Mapping-audit regression | Pending CI |
| 3 | `python -m unittest discover -s tools/tests -p 'test_learning_outcomes.py' -v` | Outcome registry and generated evidence report | Pending CI |
| 4 | `python -m unittest discover -s tools/tests -p 'test_learning_outcome_progress.py' -v` | Existing and new criterion runtime behavior | Pending CI |
| 5 | `node tools/tests/learning-outcome-criterion-progress.mjs` | Criterion summary, timed accuracy, self-report rubric, delayed recall and editorial gates | Pending CI |
| 6 | `python -m unittest discover -s tools/tests -p 'test_project_progress_index.py' -v` | 73.73% provisional weighted build index | Pending CI |
| 7 | `python -m unittest discover -s tools/tests -p 'test_project_progress.py' -v` | Target-based project progress output | Pending CI |
| 8 | `python tools/sync-version.py --check` | Version marker and cache-key coherence | Pending CI |
| 9 | `python tools/validate-data.py` | Vocabulary IDs, manifest, Service Worker shell and data constraints | Pending CI |
| 10 | GitHub Actions Validate + Pages deployment | Exact-commit hosted acceptance | Pending |

No check in this document is represented as passed before its execution result exists.
