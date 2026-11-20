# Command Log Index — v2.95.13 candidate

Baseline: v2.95.12 (`85be68a`)
Candidate: v2.95.13
All commands below were run locally. Exit code 0 means the individual command completed; it does not establish remote CI or browser acceptance.

## Python focused test modules

Invocation pattern: `python -m unittest discover -s tools/tests -p '<module>.py' -v`.

| Module | Tests | Elapsed (s) | Exit code |
|---|---:|---:|---:|
| `test_vocabulary_detail_examples.py` | 19 | 1s | 0 |
| `test_vocabulary_family_links.py` | 6 | 1s | 0 |
| `test_patch_data.py` | 20 | 17s | 0 |
| `test_patch_related_terms.py` | 11 | 10s | 0 |
| `test_ci_coverage.py` | 3 | 1s | 0 |
| `test_audit_design_tokens.py` | 8 | 1s | 0 |
| `test_learning_content.py` | 34 | 0s | 0 |
| `test_repository_integrity.py` | 1 | 2s | 0 |
| `test_design_system.py` | 19 | 1s | 0 |
| `test_responsive_layout.py` | 7 | 1s | 0 |
| `test_design_profile.py` | 6 | 2s | 0 |
| `test_sync_version.py` | 12 | 12s | 0 |
| `test_part1_photo_assets.py` | 6 | 0s | 0 |
| `test_sentence_completion.py` | 12 | 1s | 0 |
| `test_question_evidence.py` | 6 | 2s | 0 |
| `test_objective_resource_map.py` | 2 | 1s | 0 |
| `test_learning_outcomes.py` | 3 | 1s | 0 |

**Total:** 17 modules, 175 tests, 54 seconds summed individual runtimes, 0 failures, all exit code 0.

## JavaScript regression

Invocation pattern: `node tools/tests/<suite>.mjs`. All 38 `.mjs` suites in `.github/workflows/validate-data.yml` were executed individually; **38/38 exit code 0**. Per-suite logs and `summary.tsv` are in `javascript-final/`. The summary records wall-clock seconds and exit code, not assertion counts.

## Validators and build checks

| Command | Exit code | Evidence |
|---|---:|---|
| `python tools/validate-data.py --verbose` | 0 | `final-validators/validate-data.log` |
| `python tools/validate-learning-content.py` | 0 | `final-validators/validate-learning-content.log` |
| `python tools/audit-repository-integrity.py` | 0 | `final-validators/repository-integrity.log` |
| `python tools/audit-design-tokens.py` | 0 | `final-validators/design-token-audit.log` |
| `python tools/validate-part1-photo-assets.py` | 0 | `final-validators/part1-photo-audit.log` |
| `python tools/sync-version.py --check` | 0 | `final-validators/version-sync.log` |
| `python tools/audit-toeic-coverage.py` | 0 | `final-validators/coverage-report.log` |
| `python tools/report-project-progress.py` | 0 | `final-validators/progress-report.log` |
| `python -m compileall -q tools` | 0 | `final-validators/compileall.log` |
| `node --check sw.js` plus `node --check` on each `assets/js/*.js` via temp `.mjs` files | 0 | `final-validators/node-check-bundle.log` |
| `git diff --check` | 0 | `final-validators/diff-check.log` |

## Patch replay

- Clean tree created from `git archive 85be68a`.
- Each v2.95.13 patch was run once in `--dry-run` and then `--apply` mode using `--patch`.
- Patch replay exit code: 0. Full output: `patch-replay/clean-replay.log`.
- Byte comparison of the ten modified letter files and related-term glossary: PASS. ID set matches at 1,141; see `patch-replay/byte-compare.log`.
- Initial incorrect `--file` invocation exited 2 during CLI parsing and made no changes; see `patch-replay/initial-cli-usage-error.log`.
- An early `test_vocabulary_family_links.py` run failed 1/6 because the `valuable → value` gloss was stale. The underlying data link was corrected via its own expect-old patch, and the final rerun passed 6/6; both logs are included.

## Known incomplete runs

- Full Python `unittest discover` aggregate did not finish within the execution window. It is not counted.
- `test_validator.py` was not run to completion in this candidate cycle. Claude may run it separately.
- No GitHub remote Actions, Pages, browser/device, offline, two-tab or physical TTS test was run.

## Files changed by the candidate

See `CHANGE_MANIFEST_v2.95.13.md` and `git diff 85be68a..HEAD` after the release commits are created. The source package is assembled from the final candidate commit, not from untracked working files.
