# Command Log Index — TOEIC Dictionary v2.95.65

All commands below were executed locally against the exact v2.95.64 FullSource extraction after changes. Paths are repository-relative unless noted.

| Area | Command | Result |
|---|---|---|
| Source baseline | `sha256sum TOEIC_Dictionary_v2.95.64_FullSource.zip` and `unzip -t` | SHA verified; ZIP CRC PASS |
| Batch 035 historical regression | `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_035*.py' -v` | 10/10 PASS |
| Shared overlay regression | `python -m unittest discover -s tools/tests -p 'test_single_overlay_contract.py' -v` | 2/2 PASS |
| CI coverage | `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v` | 8/8 PASS |
| Repository integrity tests | `python -m unittest discover -s tools/tests -p 'test_repository_integrity.py' -v` | 2/2 PASS |
| Git commit readiness tests | `python -m unittest discover -s tools/tests -p 'test_git_commit_readiness.py' -v` | 10/10 PASS |
| Design system | `python -m unittest discover -s tools/tests -p 'test_design_system.py' -v` | 19/19 PASS |
| Practice fallback | `python -m unittest discover -s tools/tests -p 'test_practice_mode_fallback.py' -v` | 6/6 PASS |
| Version sync | `python -m unittest discover -s tools/tests -p 'test_sync_version.py' -v` | 12/12 PASS |
| Release runner | `python -m unittest discover -s tools/tests -p 'test_release_acceptance_runner.py' -v` | 10/10 PASS |
| Test fingerprints | `python -m unittest discover -s tools/tests -p 'test_test_fingerprints.py' -v` | 10/10 PASS |
| Package builder | `python -m unittest discover -s tools/tests -p 'test_package_source.py' -v` | 3/3 PASS |
| Python test sharder | `python -m unittest discover -s tools/tests -p 'test_python_test_shard_runner.py' -v` | 19/19 PASS |
| Node regressions | `for f in tools/tests/*.mjs; do node "$f"; done` | 43/43 PASS |
| JavaScript syntax | `node --check sw.js` and loop over `assets/js/*.js` as `.mjs` | PASS |
| Python syntax | `python -m compileall -q tools` | PASS |
| Repository integrity preflight | `python tools/audit-repository-integrity.py` | 363 references; 0 errors / 0 warnings |
| Data validator | `python tools/validate-data.py` | 1,141 rows; 0 errors / 0 warnings; IDs +0/-0 |
| Learning content | `python tools/validate-learning-content.py` | 0 errors / 0 warnings |
| Part 1 assets | `python tools/validate-part1-photo-assets.py` | 9/9 PASS |
| Design token audit | `python tools/audit-design-tokens.py` | 0 new violations; 2,773 historical findings |
| Staged Git readiness | `python tools/audit-git-commit-readiness.py --staged` | 779 indexed paths; 0 errors / 0 warnings |
| Post-commit Git readiness | `python tools/audit-git-commit-readiness.py --require-clean` | 779 indexed paths; 0 errors / 0 warnings; clean worktree |
| Patch replay | `git apply --check` + `git apply` on clean predecessor extraction | 779/779 files byte-identical |
| Version sync check | `python tools/sync-version.py --check` | 13/13 markers PASS |
| Workflow shape | PyYAML parse of `.github/workflows/validate-data.yml` | 125 unique steps; PASS |

The exact full Python discovery command across all 97 modules was not completed in this batch. Hosted GitHub Actions and real device/browser checks remain unverified.
