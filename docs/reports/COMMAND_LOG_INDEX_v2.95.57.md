# Command Log Index — v2.95.57

All command output logs are packaged separately in the release handoff/log bundle. Exit status is reported only for commands that completed.

| Log | Commands / scope | Result |
|---|---|---|
| `Node_Regression.log` | `node tools/tests/*.mjs` | 42 scripts, 0 failures |
| `Python_Focused.log` | `unittest` modules: answer leakage, distractor quality, CI coverage, answer-position balance, question evidence, choice identity | 36 tests, PASS |
| `Source_Preflight.log` | repository integrity, data validator, distractor structural audit, answer leakage audit, version sync, `node --check assets/js/app.js` | All commands PASS |

## Reproduction

```bash
python -m py_compile tools/audit-answer-leakage.py tools/tests/test_answer_leakage_audit.py
python -m unittest discover -s tools/tests -p 'test_answer_leakage_audit.py' -v
python -m unittest discover -s tools/tests -p 'test_distractor_quality.py' -v
python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v
python -m unittest discover -s tools/tests -p 'test_answer_position_balance.py' -v
python -m unittest discover -s tools/tests -p 'test_question_evidence.py' -v
python -m unittest discover -s tools/tests -p 'test_choice_identity.py' -v
python tools/audit-answer-leakage.py
python tools/audit-distractors.py
python tools/validate-data.py
python tools/audit-repository-integrity.py
python tools/sync-version.py --check
node --check assets/js/app.js
```

Full Python discovery was not run for this release and is not implied by the focused test results.
