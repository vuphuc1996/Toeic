# Command Log Index — TOEIC Dictionary v2.95.18

## Data update

- `python tools/patch-data.py --patch patches/v2.95.18/batch-001-ipa.json --dry-run` — PASS.
- `python tools/patch-data.py --patch patches/v2.95.18/batch-001-ipa.json --apply` — PASS.
- `python tools/sync-version.py --set 2.95.18 --apply` — version markers written; changelog heading was added manually.
- `python tools/sync-version.py --check` — PASS.

## Focused regressions

- `python -m unittest discover -s tools/tests -p 'test_ipa_backfill_batch_024.py' -v` — 6/6 PASS.
- `python -m unittest discover -s tools/tests -p 'test_project_progress.py' -v` — 4/4 PASS.
- `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v` — 3/3 PASS.
- `python -m unittest discover -s tools/tests -p 'test_package_source.py' -v` — 3/3 PASS.
- `python -m unittest discover -s tools/tests -p 'test_baseline_ids.py' -v` — 13/13 PASS.
- `python -m unittest discover -s tools/tests -p 'test_patch_data.py' -v` — 20/20 PASS (rerun after local Git initialization).
- `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_021.py' -v` — 7/7 PASS.
- `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_022.py' -v` — 9/9 PASS.
- `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_023.py' -v` — 9/9 PASS.
- `python -m unittest discover -s tools/tests -p 'test_vocabulary_detail_examples.py' -v` — 19/19 PASS.
- `python -m unittest discover -s tools/tests -p 'test_vocabulary_family_links.py' -v` — 6/6 PASS.
- `python -m unittest discover -s tools/tests -p 'test_sync_version.py' -v` — 12/12 PASS.
- `python -m py_compile $(find tools -type f -name '*.py' -print)` — PASS.
- All `tools/tests/*.mjs` executed individually — 38/38 PASS.
- All `assets/js/*.js` Node syntax checks — PASS.

## Project validation and audits

- `python tools/validate-data.py` — PASS.
- `python tools/validate-learning-content.py` — PASS.
- `python tools/audit-repository-integrity.py` — PASS.
- `python tools/audit-question-evidence.py` — completed; evidence report generated.
- `python tools/audit-distractors.py` — PASS.
- `python tools/audit-listening-readiness.py` — PASS.
- `python tools/audit-learning-outcomes.py` — PASS.
- `python tools/audit-objective-resources.py` — PASS.
- `python tools/validate-part1-photo-assets.py` — PASS.
- `python tools/audit-toeic-coverage.py` — PASS.
- `python tools/sync-design-profile.py --check` — PASS.
- `python tools/audit-design-tokens.py` — PASS; no new violations, inherited warnings retained.
- `python tools/report-project-progress.py` — snapshot generated.

## Known incomplete commands

- Full `unittest discover -p 'test_*.py'` exceeded the local execution time limit; not a full-suite pass.
- Isolated `test_validator.py` also exceeded the local execution time limit after emitting passing cases; module result remains incomplete.
- These limits are recorded in the release test report; validator CLI results are reported separately.

## Release packaging

- `python tools/package_source.py 2.95.18 /mnt/data/toeic_continue/release_v2.95.18/TOEIC_Dictionary_v2.95.18_FullSource.zip` — PASS.
- ZIP membership validation — PASS: 382 files, exactly one root `Toeic_Dictionary_v2.95.18/`, no excluded paths.
- Size — 3,806,760 bytes. SHA-256 is recorded with the delivered artifact in the release handoff, rather than inside the ZIP itself.
