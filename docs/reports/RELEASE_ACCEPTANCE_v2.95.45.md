# Release Acceptance — v2.95.45

## Aggregate status

**INCOMPLETE — full Python discovery did not finish within the available execution window.** No aggregate PASS is claimed.

A combined `python tools/run-release-acceptance.py --timeout 1800` invocation was interrupted by the outer execution limit before the runner could persist a final acceptance report. The new Python shard runner separately recorded an interrupted broad run with 17/88 modules PASS and 71 not yet executed. A subsequent broad sharded chunk also exceeded the outer execution window while entering larger editorial-review modules. These outcomes are incomplete, not failed assertions and not a full-suite pass.

## Individually verified local gates

| Gate | Exact command / method | Result |
|---|---|---|
| Repository integrity | `python tools/audit-repository-integrity.py` | PASS — 419 local references/data files, 0 errors, 0 optional warnings |
| Data validation | `python tools/validate-data.py` | PASS — 1,141 records, 0 errors, 0 warnings; 0 IDs added/lost |
| Learning-content validation | `python tools/validate-learning-content.py` | PASS — 0 errors / 0 warnings |
| Version markers | `python tools/sync-version.py --check` | PASS — 13/13 locations |
| Python compilation | `python -m compileall -q tools` | PASS |
| JavaScript syntax | `node --check` on 18 `assets` JS/MJS files plus `sw.js` | PASS — 19 files |
| JavaScript regression | all `tools/tests/*.mjs` executed individually with Node | PASS — 39/39 |
| Focused Python regression | 35 distinct test modules across 284 test methods | 283 PASS, 1 environment-dependent SKIP; see the test report for module grouping |
| Batch 038 | `test_related_glossary_merge_038.py` | PASS — 8/8 |
| Python test-shard runner | `test_python_test_shard_runner.py` | PASS — 12/12 |
| Release Acceptance runner | `test_release_acceptance_runner.py` | PASS — 10/10 |

The Python focused total includes one skip in `test_patch_data.py`: a Git-metadata-dependent `.gitignore` assertion is skipped because the source is an archive without `.git`. No learning-content or data test was skipped.

## Not complete / not externally verified

- All 88 Python test modules as one aggregate: **INCOMPLETE**; 17/88 modules were observed PASS in the interrupted broad shard run, and a larger set of focused modules passed separately. Do not infer the remaining modules passed.
- The full ordered Release Acceptance sequence: **INCOMPLETE**; no final runner-generated aggregate report was written.
- Remote GitHub Actions: not run/verified.
- GitHub Pages deployment, cache propagation and actual update behavior: not verified.
- Browser acceptance and physical Android/iOS/tablet/desktop tests: not verified.
- Independent editorial/lexical review of newly added or corrected glossary senses: pending.

## Protected-data verification

- Canonical vocabulary A–Z JSON files: byte-identical to released v2.95.44.
- Listening, Reading, Grammar, Part 5, placement/foundation and learning-path protected data sets: byte-identical.
- Baseline ID regression: PASS (13 tests).
- Choice history/identity and answer-position modules: PASS in the broad shard run.
- UI runtime changes are release/cache version strings only; no CSS/layout change.
