# Command Log Index — v2.95.11

All logs are from the local v2.95.11 worktree unless explicitly identified otherwise. Exit code `0` means that command completed successfully. Do not interpret an interrupted aggregate run as PASS.

| Log | Command | Result | Duration | Exit |
|---|---|---|---:|---:|
| `20-patch-data.log` | `python -m unittest discover -s tools/tests -p test_patch_data.py -v` | 20/20 PASS | 17.92 s wall / 16.904 s runner | 0 |
| `21-audit-design-tokens.log` | `python -m unittest discover -s tools/tests -p test_audit_design_tokens.py -v` | 8/8 PASS | 0.77 s wall / 0.016 s runner | 0 |
| `22-ci-coverage.log` | `python -m unittest discover -s tools/tests -p test_ci_coverage.py -v` | 3/3 PASS | 0.74 s wall / 0.003 s runner | 0 |
| `23-sync-version.log` | `python -m unittest discover -s tools/tests -p test_sync_version.py -v` | 12/12 PASS | 11.66 s wall / 10.892 s runner | 0 |
| `24-design-profile.log` | `python -m unittest discover -s tools/tests -p test_design_profile.py -v` | 6/6 PASS | 1.48 s wall / 0.734 s runner | 0 |
| `25-design-system.log` | `python -m unittest discover -s tools/tests -p test_design_system.py -v` | 19/19 PASS | 0.72 s wall / 0.002 s runner | 0 |
| `26-responsive-layout.log` | `python -m unittest discover -s tools/tests -p test_responsive_layout.py -v` | 7/7 PASS | 0.70 s wall / 0.006 s runner | 0 |
| `27-visual-composition.log` | `python -m unittest discover -s tools/tests -p test_visual_composition.py -v` | 8/8 PASS | 0.78 s wall / 0.001 s runner | 0 |
| `28-learning-surface.log` | `python -m unittest discover -s tools/tests -p test_learning_surface_consistency.py -v` | 5/5 PASS | runner 0.004 s | 0 |
| `29-alphabet-sound-lab.log` | `python -m unittest discover -s tools/tests -p test_alphabet_sound_lab.py -v` | 7/7 PASS | runner 0.001 s | 0 |
| `30-javascript-regressions.log` | 37 registered Node `.mjs` suites, executed individually | 37/37 PASS | Per-suite times in log | 0 |
| `31-validate-data.log` | `python tools/validate-data.py` | 1,141 records; ID +0/-0; 0 errors/warnings | 1.38 s | 0 |
| `32-validate-learning-content.log` | `python tools/validate-learning-content.py` | 0 errors/warnings | 0.87 s | 0 |
| `33-repository-integrity.log` | `python tools/audit-repository-integrity.py` | 367 references; 0 errors/warnings | 0.86 s | 0 |
| `34-part1-photo-assets.log` | `python tools/validate-part1-photo-assets.py` | 9/9 valid | 0.86 s | 0 |
| `35-design-token-audit.log` | `python tools/audit-design-tokens.py` | 2,778 legacy; 0 new; 0 drift | 0.90 s | 0 |
| `36-design-profile-sync.log` | `python tools/sync-design-profile.py --check` | 54 tokens synchronized | 0.88 s | 0 |
| `37-version-sync.log` | `python tools/sync-version.py --check` | All markers aligned to 2.95.11 | 0.73 s | 0 |

## Final post-commit checks

| Log | Command | Result | Exit |
|---|---|---|---:|
| `38-final-git-state.log` | `git status --porcelain && git rev-parse HEAD && git branch --show-current` | Worktree clean on branch `work-v2.95.11` | 0 |
| `39-final-version-check.log` | `python tools/sync-version.py --check` | All markers aligned to v2.95.11 | 0 |
| `40-final-design-token-check.log` | `python tools/audit-design-tokens.py` | 2,778 legacy warning identities; 0 new / 0 drift | 0 |
| `41-final-vocabulary-validator.log` | `python tools/validate-data.py` | 1,141 records; zero ID changes; 0 errors/warnings | 0 |
| `42-final-learning-validator.log` | `python tools/validate-learning-content.py` | 0 errors/warnings | 0 |
| `43-final-repository-audit.log` | `python tools/audit-repository-integrity.py` | 367 references; 0 errors/warnings | 0 |
| `44-final-part1-assets.log` | `python tools/validate-part1-photo-assets.py` | 9/9 valid | 0 |
| `45-checklist-state.log` | Checklist state assertion | 14 rows; 14 remain `Chưa kiểm` | 0 |
| `47-design-system-final.log` | `python -m unittest discover -s tools/tests -p test_design_system.py -v` | 19/19 PASS after final documentation wording correction | 0 |

## Incomplete runs (not counted as passing)

- `python -m unittest discover -s tools/tests -p 'test_*.py' -v` — the execution/orchestration limit was reached before a complete suite result was produced. No PASS claim is made.
- A broad module-by-module sweep was also interrupted by the same environment time limit. Partial exploratory outputs (`py-*.log`) are retained as raw traces but are **not** included in the 95 focused-test total.
- The Python `test_validator.py` full module was not completed during this local run. The production data validator command `python tools/validate-data.py` did complete with exit code 0.

See `INCOMPLETE_RUNS_v2.95.11.md` in the supplied test-log archive for the exact non-PASS status of timed-out attempts.

## Independent Claude result from supplied v2.95.10 audit

The project owner supplied Claude's result for the v2.95.10 archive: 433 Python tests and 37 `.mjs` files passed in Claude's environment. This is included as external evidence for v2.95.10 only; it does not replace the v2.95.11 focused test results above.
