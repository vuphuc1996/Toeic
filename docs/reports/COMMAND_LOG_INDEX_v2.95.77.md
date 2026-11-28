# Command Log Index — v2.95.77

| Command / tool | Outcome | Evidence |
|---|---|---|
| `python3 tools/sync-version.py --set 2.95.77 --apply` & `--check` | PASS; all release markers, app imports, and Service Worker precache URLs synchronized to `2.95.77` | Test report |
| `python3 tools/audit-repository-integrity.py` | PASS; `414` local references/data files inspected; `0` errors, `0` warnings | Test report |
| `python3 tools/validate-data.py` | PASS; `1,221` canonical records; IDs `+0/−0`; `0` errors, `0` warnings | Test report |
| `python3 tools/validate-learning-content.py` | PASS; `145` Listening units/`295Q`, `73` Reading units/`287Q`, `58` Grammar lessons/`169Q`, `80` Separate Part 5Q; `0` errors/warnings | Test report |
| `python3 tools/validate-part1-photo-assets.py` | PASS; `9/9` Part 1 photo files valid, `0` warnings | Test report |
| `python3 tools/audit-seven-part-content.py` | PASS; `831` questions (`302` approved, `360` human-review-required, `169` support), `0` structural errors, `37` `AI_TRIAGE` flags | Test report |
| `python3 tools/audit-mock-readiness.py` | PASS; Reading `200Q` (2 disjoint Full forms); Listening `102Q` (1 Full form / `98%` 2nd-form overlap) | Test report |
| `node --check server.js`, `sw.js`, `assets/js/*.js` + `tools/tests/*.mjs` | PASS; all JS syntax valid, **45/45** Node regression scripts PASS (`NODE_SUITE_PASS`) | Test report |
| `node tools/tests/vocabulary-release-integrity.mjs` | PASS; all 8 legacy migration repair profiles validated against 1,221-word inventory | Test report |
| `python3 tools/run-python-tests-sharded.py --timeout-per-module 180` | PASS WITH SKIPS; **114/114** modules (`113` PASS, `1` PASS WITH SKIPS), **838** cases (`837` passed, `0` failed, `1` accepted Git-metadata skip) | `logs/test-shards/PYTHON_TEST_SHARDS_v2.95.77.md/.json` & Test report |
| `python3 tools/run-release-acceptance.py` | PASS; **12/12** acceptance checks PASS | `logs/release-acceptance/RELEASE_ACCEPTANCE_v2.95.77.md/.json` |
| `git diff --check` & `python3 tools/audit-git-commit-readiness.py --require-clean` | PASS (`0` errors, `0` warnings) | Git commit readiness |
| Clean source packaging & `compile_applet` + `lint_applet` | PASS; `/tmp/TOEIC_Dictionary_v2.95.77_FullSource.zip` CRC & clean extraction verified; build & lint PASS | `PACKAGE_VERIFICATION_v2.95.77.md` |

No hosted GitHub Actions run, remote `candidate` push, live GitHub Pages deployment, installed-PWA cache/device verification, or `main` modification was performed.
