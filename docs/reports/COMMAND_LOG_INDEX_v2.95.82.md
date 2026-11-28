# Command Log Index — TOEIC Dictionary v2.95.82

**Branch:** `candidate`
**Predecessor baseline:** `4d1eead800e3378cf91b5b83ddb14bc3c8fb8737`
**Release scope:** Part 2 question-to-criterion evidence; no learner-facing UI or bank changes.

| Order | Command / workflow step | Purpose | Evidence status |
|---:|---|---|---|
| 1 | `python -m unittest discover -s tools/tests -p 'test_objective_criterion_map.py' -v` | Validate all 16 Part 2 evidence rows and negative cases | **PENDING CI** |
| 2 | `python tools/audit-objective-criterion-map.py` | Reconcile 1,119 links, 638 stable IDs, Part 2 evidence and reserve exclusions | **PENDING CI** |
| 3 | `python -m unittest discover -s tools/tests -p 'test_learning_outcomes.py' -v` | Reconcile 23/27 TOEIC and 29/33 total criteria | **PENDING CI** |
| 4 | `python tools/audit-learning-outcome-evidence.py` | Regenerate the 33-criterion evidence matrix | **PENDING CI** |
| 5 | `python tools/sync-version.py --check` | Validate 19 markers and app/SW/mock cache groups | **PENDING CI** |
| 6 | `python -m unittest discover -s tools/tests -v` | Full Python discovery on exact candidate SHA | **PENDING CI** |
| 7 | GitHub Validate | Exact candidate source/test acceptance | **PENDING** |
| 8 | GitHub Pages build/deploy | Candidate Pages build and deployment | **PENDING** |

Hosted workflow results, not source edits or local reasoning, determine acceptance.
