# Test Report — TOEIC Dictionary v2.95.64

**Date:** 2026-11-25
**Base:** v2.95.63 FullSource, SHA-256 `6d43a7f44e1cc84d6ad7f3ee9dae660cceb83c792668d0966ce1060f4aa9ea80`
**Scope:** GitHub commit-readiness and CI reliability; no learning-content or UI redesign.

## Implementation summary

- Added a read-only Git preflight with explicit staged and clean-tree modes.
- Hardened GitHub Actions dependency pins, checkout depth, path filters, syntax compilation and test-coverage checks.
- Corrected repository-integrity handling of default `unittest discover` (`test*.py`).
- Removed two duplicate Python test invocations while preserving full Python discovery.
- Added `.gitignore` and `.gitattributes` protections for local artifacts and cross-platform line endings.

## Executed tests

| Check | Result |
|---|---:|
| `test_git_commit_readiness.py` | 10/10 PASS |
| `test_ci_coverage.py` | 8/8 PASS |
| `test_repository_integrity.py` | 2/2 PASS |
| `test_package_source.py` | 3/3 PASS |
| `test_python_test_shard_runner.py` | 19/19 PASS |
| `test_release_acceptance_runner.py` | 10/10 PASS |
| `test_sync_version.py` | 12/12 PASS |
| Focused Python total (the seven modules above) | **64 cases PASS** |
| Node regression inventory | **43/43 PASS** |
| `sw.js` + all application JS syntax checks | PASS |
| `python -m compileall -q tools` | PASS |
| Version sync | 13/13 PASS |
| Repository integrity | 363 refs/data files; 0 errors; 0 optional warnings |
| Data validator | 1,141 records; 0 errors; 0 legacy warnings; 0 new-debt errors |
| Learning-content validator | 0 errors; 0 warnings |
| Part 1 media validator | 9/9 PASS |
| YAML structural check | 124 steps; no missing run/uses; no duplicate labels; all actions SHA-pinned |

Additional generated read-only audit outputs: answer leakage 177 questions / 6 review flags; distractor structural audit 264 in-scope questions and 156 reserve checks; listening readiness 102 eligible / 193 reserve-pending; learning outcome map 11/11 objectives and 33 criteria, with 6/33 evidence-collection paths. These are diagnostics, not editorial or psychometric approval.

## Full Python suite status

The inventory contains **97 Python test modules**. `run-python-tests-sharded.py --timeout-per-module 180` started but the outer execution window expired after 19 modules (144 test cases) had passed; 78 modules remained pending in the checkpoint. A resume attempt encountered the same outer-window limit. The separate `test_foundation_a2_assessment_quality.py` and `test_foundation_a2_production.py` modules were each run directly and passed 8/8. No full-suite PASS is claimed.

## GitHub / deployment boundary

The actual hosted GitHub Actions workflow has not been triggered from this session. The pinned references and workflow structure were checked locally. GitHub Pages deployment, browser installation/update, offline cache propagation and physical device behavior remain UNVERIFIED.

## Data and product boundaries

Only the version value in `data/manifest.json` changed. Vocabulary IDs/headwords/meanings/relations, Related Glossary entries, question IDs, choice IDs, answer keys, Mock eligibility, learner IndexedDB schema/data, Robot Buddy data boundary and all other canonical content remain byte-identical to v2.95.63. The UI was not redesigned; no runtime or backend feature was added.
