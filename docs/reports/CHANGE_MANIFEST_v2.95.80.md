# Change Manifest — TOEIC Dictionary v2.95.80

**Predecessor:** candidate HEAD `5bbdc5e05e396380d17d5a65f108d73aa8ee172a` (v2.95.79).
**Target:** v2.95.80 — Criterion Mapping Coverage & Source Evidence Hardening.
**Target branch:** `candidate`; `main` is not modified.

## Source changes

- `data/learning-path/objective-criterion-map.json`: add 21 links using existing stable question keys; total 1,103 links / 638 unique keys.
- `data/learning-path/objective-outcomes.json`: reconcile the four updated mapping counts and the scope warning; the same 22/27 TOEIC criteria remain instrumented.
- `tools/audit-objective-criterion-map.py`: require Part 7 cross-document mappings to cite two distinct declared sources from an internally reviewed unit, with one matching quote per source; require the mapping basis to name those labels.
- `tools/tests/test_objective_criterion_map.py`: add mapping-count, below-minimum and fail-closed source-evidence regression tests.
- `tools/tests/test_learning_outcomes.py`: update the report expectation to 1,103 links.
- `data/manifest.json`, `package.json`, `assets/js/app.js`, `sw.js`, `assets/js/mock-engine.js`, and `index.html`: synchronize the release version and cache keys to v2.95.80.
- Release ledgers, criterion evidence report, project progress snapshot and release reports move to v2.95.80.

## Scope decisions

The 21 new links cover Grammar form recognition (+9), Listening Part 3 conversation purpose (+2), Listening Part 3 speaker/action linking (+9), and Listening Part 4 talk purpose (+1). All selected questions already exist and retain their stable IDs. No new unique question key is introduced.

Part 7 cross-document remains at two eligible questions: only those two current questions carry two-source evidence with quotes matching two declared documents on internally reviewed material. Part 1 remains at eight non-reserve photo questions; the reserve item stays excluded. Five unsupported TOEIC criteria remain uninstrumented.

## Verification strategy

Run the stable mapping audit, outcome report tests, full Python discovery, version synchronization and Pages build/deploy on the exact new candidate commit. Hosted acceptance is pending until those runs complete.

## Protected boundaries

No bank question, passage, choice, answer key, stable question/choice ID, canonical vocabulary ID, Mock eligibility, Listening reserve state, IndexedDB schema/data, UI/UX, navigation or Robot Buddy behavior is intentionally changed. Hosting architecture/settings are unchanged.
