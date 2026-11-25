# Test Report — TOEIC Dictionary v2.95.48

Date: 2026-11-24

## Scope

Defensive handling for the learner-local Learning Outcome Evidence ledger. No vocabulary or question data migration was performed.

## Results actually observed

| Check | Cases / scope | Result |
|---|---:|---|
| Node runtime `tools/tests/learning-outcome-progress.mjs` | 5 assertion groups | PASS |
| Python `test_learning_outcome_progress.py` | 3 | PASS |
| Python `test_learning_outcomes.py` | 3 | PASS |
| Python `test_foundation_outcome_evidence.py` | 2 | PASS |
| Python `test_objective_resource_map.py` | 2 | PASS |
| Python `test_question_evidence.py` | 7 | PASS |
| Python `test_python_test_shard_runner.py` | 19 | PASS |
| Python `test_test_fingerprints.py` | 9 | PASS |
| Python `test_validator.py` (direct unittest discovery) | 38 | PASS |
| `node --check assets/js/learning-outcome-progress.js` | syntax | PASS |
| `python tools/sync-version.py --check` | 13 markers + changelog | PASS |
| `python tools/validate-data.py --root .` | 1,141 records | PASS; 0 errors, 0 warnings |
| `python tools/audit-learning-outcomes.py` | 11 objectives / 33 criteria | PASS; 6/33 criteria have an evidence-collection path |
| `python tools/audit-objective-resources.py` | 379 resources | PASS; 379/379 linked |

Python focused total: **83/83 PASS** across eight modules. The 38-case validator module is included in this total. The Node runtime suite also now verifies a valid explanation-rubric-only ledger, including a successful read-only audit and summary.

## Incomplete / unverified

- The full dynamic 89-module sharded suite did not complete. The latest full-run checkpoint records **18/89 modules PASS and 133/133 cases PASS**, with 71 modules NOT RUN and 0 failures/timeouts/errors among the completed modules. This is INCOMPLETE, not PASS. A separate sharded run of `test_foundation_a2_assessment_quality.py` also passed 8/8; a separate sharded run of `test_validator.py` passed 38/38.
- A complete local replay of every GitHub Actions workflow step was not run for v2.95.48.
- Hosted GitHub Actions, GitHub Pages deployment, cache propagation, offline behavior, and physical iOS/Android/tablet/desktop acceptance remain UNVERIFIED.

## Data integrity

The data validator reported 1,141 vocabulary records, 0 IDs added, 0 IDs missing, and the same ID-set SHA-256 prefix `adccbdb4c9887220`. Only `data/manifest.json` version metadata changed among the data files. Vocabulary content, question content, choices, answer keys, and learner IndexedDB schema were not edited.
