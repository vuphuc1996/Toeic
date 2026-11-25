# Command Log Index — v2.95.58

- `node tools/tests/*.mjs`: 42 scripts, all exit code 0. Captured in the release execution log.
- `PYTHONPATH=tools/tests python -m unittest tools.tests.test_answer_position_balance tools.tests.test_learning_outcome_progress tools.tests.test_learning_outcomes tools.tests.test_question_evidence -v`: 17/17 PASS.
- `python tools/audit-question-evidence.py`: exit 0; generated 582-question evidence report.
- `python tools/audit-learning-outcomes.py`: exit 0; 11/11 objectives, 33 criteria, 6/33 with collection paths.
- `python tools/validate-data.py`: exit 0; 1,141 records, 0 ERROR / 0 WARNING.
- `python tools/sync-version.py --check`: exit 0; all 13 registered markers and changelog synchronized.
- `node --check sw.js` and `node --check` on every `assets/js/*.js`: exit 0.
- `python -m unittest discover -s tools/tests -p 'test_*.py' -v`: INCOMPLETE; exceeded 300 seconds after 337 test result lines, without terminal summary. No aggregate suite status is claimed.
- Initial focused Node test invocation: failed due to an incorrect expected value in the newly added assertion; corrected and rerun PASS.
- Initial unittest invocation: import error due to missing `PYTHONPATH`; corrected invocation PASS.

- FullSource ZIP CRC: PASS; 693 files under one versioned root.
- Patch ZIP CRC: PASS.
- Exact patch replay against v2.95.57: 693/693 target files byte-identical; 0 extra/missing/changed files.
- SHA-256 sidecars: both final archives verified with `sha256sum -c`.
