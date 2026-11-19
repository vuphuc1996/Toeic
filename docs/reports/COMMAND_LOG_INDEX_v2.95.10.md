# Command Log Index — v2.95.10

All paths below refer to the companion `TOEIC_v2.95.10_Test_Logs.zip` unless stated otherwise. Logs retain full command output where captured. An interrupted log is explicitly marked and must not be counted as a passing test run.

## Completed change-specific checks

| Log | Command / scope | Result |
|---|---|---|
| `01-flashcard-fixed-batch.log` | `git diff --check`; `node --check assets/js/app.js`; Flashcard 10-card regression; Robot Buddy streaming; `test_practice_mode_fallback.py` | All commands exit 0; practice fallback 6/6 |
| `02-baseline-before.log` | Pre-update validation and ID comparison | 1,141 unique IDs; 213 additions; 0 missing |
| `02-baseline-update.log` | `validate-data.py --update-ids`; baseline unit tests; validation; independent set hash/count | Baseline test 13/13; final 1,141 IDs; 0 added / 0 missing |
| `03-patch-data-hardening.log`, `03-patch-data-tests.log`, `24-patchdata-post-audit-rollback.log` | Patch path guard, allowlists and final-audit-failure recovery; `test_patch_data.py` | 17/17 PASS; covers protected paths, out-of-allowlist rejection, operation audit, optimistic locking, rollback and byte-for-byte recovery when the final audit write fails |
| `03-ci-coverage-tests.log`, `04-ci-coverage-tests.log` | `test_ci_coverage.py` | 3/3 PASS; workflow has 0 `continue-on-error` occurrences |
| `04-sw-update-simulation.log` | `node tools/tests/service-worker-update.mjs` | PASS; first install, waiting update, consent activation, failed install/cache preservation, optional asset and 404 behavior |
| `04-pwa-readiness-tests.log` | `test_pwa_readiness.py` | 3/3 PASS |
| `04-validate-data.log`, `04-vocab-integrity.log` | Full vocabulary validator and JS release integrity | PASS; 1,141 records, no missing IDs |
| `04-repository-integrity.log` | Repository preflight | 366 references/data files, 0 errors, 0 optional warnings |
| `05-listening-readiness.log`, `05-toeic-coverage.log`, `05-learning-content.log`, `05-foundation-a2.log`, `05-progress.log` | Content inventory and review-status audits | Reports regenerated; reserve content remains review-pending |
| `06-node-regression-all.log` | Run each `tools/tests/*.mjs` file | 37/37 PASS before version sync |
| `11-node-regression-post-version.log` | Re-run every `.mjs` after v2.95.10 version sync | 37/37 PASS |
| `13-design-profile-final.log` | `test_design_profile.py` | 6/6 PASS |
| `14-sync-version-tests.log` | `test_sync_version.py` | 12/12 PASS |
| `15-release-rotation-tests.log` | `test_release_rotation.py` | 6/6 PASS |
| `16-release-checks-post-version.log` | Version sync, data/content validation, repository audit, design sync, JS syntax, Flashcard/SW tests and diff check | Every listed command exit 0 |
| `17-repository-integrity-tests.log` | `test_repository_integrity.py` | 1/1 PASS |
| `23-python-test-inventory-ast.log` | Static AST inventory | 54 Python modules / 433 declared test methods; not a pass count |
| `25-final-verification.log` | Final post-fix verification: patch-data, CI coverage, repository-integrity tests, vocabulary/content validators, repository audit, version/design sync, JS syntax and all `.mjs` regressions | All commands exit 0; 17/17 patch-data, 3/3 CI coverage, 1/1 repository integrity, 37/37 JS suites; data validators 0 errors/0 warnings |

The focused complete Python modules listed above total 67 passing cases: baseline IDs 13, patch data 17, practice fallback 6, PWA readiness 3, CI coverage 3, design profile 6, version sync 12, release rotation 6 and repository integrity 1.

## Interrupted / incomplete attempts (not PASS)

- `07-python-modules-independent.log`: broad per-module sweep was interrupted by the execution time limit after the beginning of the Foundation outcome module. It is not a 54-module result.
- `08-final-targeted-python.log` and `12-python-focused-post-version.log`: repeated targeted sweeps were interrupted. Complete module results must be taken from the dedicated completed logs above, not from these partial attempts.
- `test_validator.py`: the full module did not complete within the available execution window. The current direct full-data command `python tools/validate-data.py -v` did pass, but that does not substitute for the incomplete unit module.
- `baseline-python-tests.log` is an earlier aggregate attempt from v2.95.9 and is provided only as historical context, not as v2.95.10 proof.

## Documentation rotation

`python tools/rotate-release-files.py --apply` archived five obsolete v2.95.7/v2.95.8 report files into `docs/archive/PROJECT_HISTORY.md`; the post-rotation repository-integrity audit remains green. The utility uses no `--dry-run` flag: running it without arguments previews the plan.

## Version commands

- `09-version-dry-run.log`: `python tools/sync-version.py --set 2.95.10 --dry-run` — exit 0; showed the precise marker edits and wrote nothing.
- `10-version-apply.log`: `python tools/sync-version.py --set 2.95.10 --apply` — exit 0; version changed through the required tool.
- `16-release-checks-post-version.log`: final `python tools/sync-version.py --check` — PASS across app, Service Worker, all HTML markers, README, Master Status and Changelog.

## Not covered by local command logs

Remote GitHub Actions, GitHub Pages deployment, browser/PWA installation and offline/reconnect, real two-tab update consent, actual iOS/Android TTS and physical-device visual acceptance remain for user-side verification.
