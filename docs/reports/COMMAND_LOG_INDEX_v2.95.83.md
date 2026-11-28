# Command Log Index — TOEIC Dictionary v2.95.83

**Branch:** `candidate`
**Sole predecessor:** `5eb3b736c3252a38702438efbbbc75e74864189a`
**Scope:** Part 4 inference/action, Part 6 discourse-purpose, question-level Mock exclusion and review handoff.

| Order | Command / workflow | Purpose | Status |
|---:|---|---|---|
| 1 | `python -m unittest discover -s tools/tests -p 'test_objective_criterion_map.py' -v` | Part 2/4/6 evidence mapping, answer-key and source-review guards | **PENDING CI** |
| 2 | `python tools/audit-objective-criterion-map.py` | Reconcile 1,139 links / 648 IDs / 25 mapped TOEIC criteria | **PENDING CI** |
| 3 | `node tools/tests/mock-exam-engine.mjs` | Verify Quick/Half/Full quotas, Part 4 three-question blocks and practice-only exclusion | **PENDING CI** |
| 4 | `python -m unittest discover -s tools/tests -p 'test_mock_readiness_audit.py' -v` | Verify Part 4 approved pool 30 and Listening approved pool 102 | **PENDING CI** |
| 5 | `python -m unittest discover -s tools/tests -p 'test_listening_expansion.py' -v` | Reconcile eligible and reserve Listening using question-level eligibility | **PENDING CI** |
| 6 | `python -m unittest discover -s tools/tests -p 'test_learning_outcomes.py' -v` | Reconcile 31/33 overall and 25/27 TOEIC evidence paths | **PENDING CI** |
| 7 | `python tools/audit-learning-outcome-evidence.py` | Generate 33-criterion outcome matrix | **PENDING CI** |
| 8 | `python tools/sync-version.py --check` | Verify canonical version and release cache groups | **PENDING CI** |
| 9 | `python -m unittest discover -s tools/tests -v` | Full Python discovery on exact candidate SHA | **PENDING CI** |
| 10 | GitHub Validate + GitHub Pages | Exact-commit validation and candidate deployment | **PENDING** |

FullSource ZIP, installed-PWA/offline and physical-device QA remain separate acceptance gates.
