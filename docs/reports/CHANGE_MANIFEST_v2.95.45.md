# Change Manifest — TOEIC Dictionary v2.95.45

Base: released v2.95.44 FullSource (664 files).

## Implemented source changes

### Imported QA infrastructure from the alternate upload

- `tools/run-python-tests-sharded.py`
- `tools/run-release-acceptance.py`
- `tools/tests/test_python_test_shard_runner.py`
- `tools/tests/test_release_acceptance_runner.py`

The Release Acceptance runner was hardened after import: it derives version from the manifest; JSON and Markdown reports use the same resolved version; timed-out commands terminate their process group through the shared sharder helper. Tests cover these contracts.

### Related Glossary Batch 038

- 5 new relationship-target lookup terms: `ask for`, `change`, `comments`, `communicate with`, `connection`.
- 3 exact-guarded sense corrections: `caller`, `article`, `assume`.
- Patch and ledger files under `patches-related-terms/v2.95.45/`.
- 8 dedicated regression tests; historical Batch 035–037 base reconstruction is corrected for later guarded changes.

### Documentation / audits / CI

- Updated Master, changelog, README, current/previous version, update notes, and current version markers.
- Added source comparison, Batch 038, test report, command log and acceptance reports.
- Regenerated glossary candidate/backlog/quality, relationship graph, major-release, project progress, TOEIC coverage, listening, question evidence, distractor, learning outcome and Foundation A2 reports.
- CI compiles the two runners and registers their tests and the Batch 038 suite.

## File preservation

- No deletions.
- No changes to canonical A–Z vocabulary data, stable IDs, synonym/antonym arrays, Grammar/Listening/Reading/Part 5 question banks, question/choice IDs, answer keys, IndexedDB schema or learner progress implementation, Mock eligibility or CSS/layout.
- Only version/cache markers changed in `assets/js/app.js`, `index.html` and `sw.js`.

## Alternate branch decisions

See `COMPARE_MERGE_REVIEW_v2.95.45.md`. The uploaded v2.95.44 tree was not used as a replacement. `consideration` and the uploaded `run-validator-test-batches.py` were intentionally not merged.

## Validation limits

Focused local regression and validators are listed in `TEST_REPORT_TOEIC_Dictionary_v2.95.45.md`. Full Python discovery and aggregate Release Acceptance are INCOMPLETE due the outer execution limit. Remote CI, Pages and physical-device QA remain unverified.

## Package delta

- Base FullSource: 664 files.
- v2.95.45 packageable tree: 698 files.
- 34 added / 21 modified / 0 deleted; 643 common paths are byte-identical.
- Patch overlay: 55 entries; exact replay must reproduce all 698 files byte-for-byte.
