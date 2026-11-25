# Development Batch — Deterministic Delayed-Recall Evidence

Date: 2026-11-24
Base: user-optimized v2.95.46 FullSource (candidate-derived release package).

## Implementation

`assets/js/learning-outcome-progress.js` now accepts an optional `now` timestamp in `summarizeObjectiveProgress` and `summarizeAllObjectives`. Existing callers remain compatible through the default `Date.now()`. All due-recall counts within a summary use the supplied evaluation instant. Invalid timestamps safely fall back to the wall clock.

## Why

The due-recall metric previously read `Date.now()` internally, which made exact boundary tests and reproducible evidence snapshots dependent on execution time. Injecting the clock makes reporting deterministic without changing the scheduling policy or learner records.

## Tests actually run

- `node tools/tests/learning-outcome-progress.mjs`: PASS (including new deterministic boundary tests).
- `python -m unittest tools.tests.test_learning_outcome_progress tools.tests.test_learning_outcomes tools.tests.test_objective_resource_map -v`: 8/8 PASS.
- `python tools/audit-learning-outcomes.py`: PASS, 11 objectives / 33 criteria / 6 instrumented.
- `python tools/audit-objective-resources.py`: PASS, 379/379 resource links.
- `node --check assets/js/learning-outcome-progress.js`: PASS.
- `node --check tools/tests/learning-outcome-progress.mjs`: PASS.

## Incomplete checks

- Full `python -m unittest discover -s tools/tests -p 'test_*.py' -v` exceeded the outer 300-second tool limit after 334 test cases had reported. The process was terminated by the tool timeout. The remaining suite was not completed; this is not recorded as PASS or FAIL.
- Remote GitHub Actions, GitHub Pages deployment, cache propagation and physical device testing were not run.

## Protected invariants

No vocabulary records, IDs, headwords, relations, question IDs, choices, answer keys, learner IndexedDB data/schema, UI layout, backend or deployment target were changed.
