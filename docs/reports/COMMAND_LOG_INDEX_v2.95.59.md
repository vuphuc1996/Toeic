# Command Log Index — v2.95.59

All commands below were run against the v2.95.59 working tree derived only from the verified v2.95.58 FullSource.

| Command / scope | Exit | Evidence |
|---|---:|---|
| `python tools/audit-item-complexity.py` | 0 | 582 questions; 280 reserve; 106 signalled; 0 structural errors |
| `python -m unittest discover -s tools/tests -p 'test_item_complexity_review.py' -v` | 0 | 5/5 PASS |
| `python -m unittest discover -s tools/tests -p 'test_answer_position_balance.py' -v` | 0 | 4/4 PASS |
| `python -m unittest discover -s tools/tests -p 'test_learning_outcome_progress.py' -v` | 0 | 3/3 PASS |
| `python -m unittest discover -s tools/tests -p 'test_learning_outcomes.py' -v` | 0 | 3/3 PASS |
| `python -m unittest discover -s tools/tests -p 'test_question_evidence.py' -v` | 0 | 7/7 PASS |
| `python -m unittest discover -s tools/tests -p 'test_answer_leakage_audit.py' -v` | 0 | 7/7 PASS |
| `python -m unittest discover -s tools/tests -p 'test_distractor_quality.py' -v` | 0 | 6/6 PASS |
| `node tools/tests/*.mjs` | 0 each | 42 scripts; 42 PASS, 0 FAIL |
| `python tools/audit-question-evidence.py` | 0 | 582 indexed; 193 Listening reserve pending |
| `python tools/audit-answer-leakage.py` | 0 | 177 questions; 6 diagnostic flags |
| `python tools/audit-distractors.py` | 0 | 264 questions; 156 reserve structural checks |
| `python tools/validate-data.py` | 0 | 1,141 records; 0 ERROR / 0 WARNING |
| `python tools/validate-learning-content.py` | 0 | Listening/Reading/Grammar inventory valid; 0 errors / 0 warnings |
| `python tools/sync-version.py --check` | 0 | 13/13 markers synchronized |
| `python -m py_compile tools/audit-item-complexity.py tools/tests/test_item_complexity_review.py` | 0 | Python syntax PASS |
| `node --check sw.js` and all `assets/js/*.js` | 0 | JS syntax PASS |

Full Python discovery, remote Actions/Pages and physical-device acceptance were not run or verified.
