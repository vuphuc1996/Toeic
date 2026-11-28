# Test Report — TOEIC Dictionary v2.95.77

## Source baseline

- Working branch: `candidate`
- Base commit: `035dd6e2001b3b049407f71acd21f9c33f33e776` (v2.95.76)
- Target release: `v2.95.77`
- Canonical vocabulary: `1,221` headwords (`A`–`Z`, `+0/−0` IDs).
- Related Glossary: `567` entries (`565` unflagged, `2` low-priority `short-definition-review` flags).
- Assessment inventory: `831` total questions (`302` `APPROVED_FOR_MOCK`, `360` `HUMAN_REVIEW_REQUIRED`, `169` `PRACTICE_SUPPORT` Grammar exercises).

## JavaScript & Node regression

- Syntax checks (`node --check server.js`, `node --check sw.js`, and all `22` browser modules in `assets/js/*.js`): **PASS**.
- Vocabulary release integrity suite (`node tools/tests/vocabulary-release-integrity.mjs`): **PASS** (all 8 migration profiles validated against the 1,221-word inventory).
- Node regression suite (`tools/tests/*.mjs`): **45/45 scripts PASS**, terminal marker `NODE_SUITE_PASS (45 scripts)`.

## Sharded Python test suite

- Runner: `python3 tools/run-python-tests-sharded.py --timeout-per-module 180`
- Full discovery check: `python3 -m unittest discover -s tools/tests -v` (`838` tests, `OK (skipped=1)`)
- Modules executed: **114 / 114** (`113` PASS, `1` PASS WITH SKIPS, `0` FAIL, `0` TIMEOUT, `0` INCOMPLETE, `0` ERROR, `0` NOT RUN)
- Test cases: **838** collected (`837` passed, `0` failed, `1` skipped, `0` errored, `0` unapproved skips, `0` deselected)
- Accepted skip detail: `tools/tests/test_patch_data.py::PatchDataTests.test_repository_gitignore_excludes_audit_logs` — `source archive has no Git metadata; gitignore assertion requires a clone` (approved in `tools/test-inventory-policy.json`).
- Acceptance wrapper (`python3 tools/run-release-acceptance.py`): **12/12** checks PASS.

## Validators & domain audits

| Check | Result |
|---|---|
| `git diff --check` & `tools/audit-git-commit-readiness.py --require-clean` | PASS (`0` errors, `0` warnings) |
| `tools/validate-data.py` | PASS; `1,221` records; IDs `+0/−0`; `0` errors, `0` legacy warnings |
| `tools/validate-learning-content.py` | PASS; `295` Listening + `287` Reading + `169` Grammar + `80` Separate Part 5 (`0` errors/warnings) |
| `tools/validate-part1-photo-assets.py` | PASS; `9/9` local Part 1 photos valid; `0` warnings |
| `tools/audit-repository-integrity.py` | PASS; `414` local references/data files inspected; `0` errors, `0` optional warnings |
| `tools/sync-version.py --check` | PASS; all release markers + `17` `app.js` keys + `42` `sw.js` keys + `1` `mock-engine.js` key synchronized to `2.95.77` |
| `tools/sync-design-profile.py --check` | PASS; `54` tokens and `406` typography selector groups synchronized |
| `tools/audit-design-tokens.py` | PASS; `0` new violations; `2,773` legacy warnings remain |
| `tools/audit-learning-outcomes.py` & `audit-learning-outcome-evidence.py` | PASS; `11/11` objectives, `33` criteria (`6/33` Foundation criterion-instrumented, `11/11` group-level wired) |
| `tools/audit-objective-resources.py` | PASS; `379/379` canonical resource links valid |
| `tools/audit-seven-part-content.py` | PASS; `831` questions (`302` approved, `360` human-review-required, `169` support), `0` structural errors, `0` duplicate stems, `37` `AI_TRIAGE` flags |
| `tools/audit-mock-readiness.py` | PASS; Reading `200Q` (2 disjoint Full forms); Listening `102Q` (1 Full form, `98%` 2nd-form overlap, Part 1 `8+1=9 < 12` bottleneck) |
| `compile_applet` & `lint_applet` | PASS; static Express server and PWA assets verified |

## Implemented workstreams completed in v2.95.77

1. **Migration Profile Reconciliation:** Extended all 7 existing historical migration repair profiles (`979`, `992`, `1026`, `1063`, `1100`, `1137`, `1141`) in `manifest.json` with the exact 40 canonical IDs from Batch 028, and added a new exact profile for the 1,181-word v2.95.75 snapshot (`1181`) with those 40 Batch 028 IDs.
2. **CI Recovery & Test Assertions:** Resolved the test failure in `vocabulary-release-integrity.mjs` (`1221 !== 1181`), ensuring full compatibility with the 1,221-word vocabulary inventory.
3. **Version & Cache Synchronization:** Synchronized all version markers and release cache keys (`__release=2.95.77`) across the repository via `tools/sync-version.py`.
4. **Release Documentation & Verification:** Generated v2.95.77 test report, change manifest, command log index, package verification, and migration compatibility audit.

## Acceptance boundary

- **Source Release Accepted (local workspace):** Verified across all `114` Python test modules (`838` cases), `45` Node regression scripts, `vocabulary-release-integrity.mjs`, all domain validators, build/lint checks, and clean ZIP packaging.
- **Candidate CI Verified:** Pending GitHub Actions run on commit to `candidate`.
- **Pages Deployment Verified:** Pending GitHub Pages deployment on commit to `candidate`.
- **Installed-PWA / Offline Propagation Verified:** Unverified.
- **Physical-Device QA Verified:** Unverified.
- **Production Deployment Accepted (`main`):** Unverified (`main` untouched).
