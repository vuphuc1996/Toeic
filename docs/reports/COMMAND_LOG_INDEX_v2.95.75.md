# Command Log Index — v2.95.75

| Command / tool | Outcome | Evidence |
|---|---|---|
| `python3 tools/sync-version.py --set 2.95.75 --apply` & `--check` | PASS; all release markers, `17` `app.js` imports, `42` `sw.js` precache URLs, and `1` `mock-engine.js` import key synchronized | Release shell & test report |
| `python3 tools/audit-repository-integrity.py` | PASS; `414` local references/data files inspected; `0` errors, `0` optional warnings | Test report |
| `python3 tools/validate-data.py` | PASS; `1,181` canonical records; IDs `+0/−0`; `0` errors, `0` legacy warnings | Test report & `DATA_DIFF_v2.95.75.md` |
| `python3 tools/validate-learning-content.py` | PASS; `145` Listening units/`295Q`, `73` Reading units/`287Q`, `58` Grammar lessons/`169Q`, `80` Separate Part 5Q; `0` errors/warnings | Test report |
| `python3 tools/validate-part1-photo-assets.py` | PASS; `9/9` Part 1 photo files valid, `0` warnings | Test report |
| `python3 tools/audit-learning-outcomes.py` & `audit-learning-outcome-evidence.py` | PASS; `11` objectives, `33` criteria (`6/33` criterion-instrumented, `11/11` group-wired) | `TOEIC_LEARNING_OUTCOME_EVIDENCE_v2.95.75.md` |
| `python3 tools/audit-objective-resources.py` | PASS; `11` objectives, `379/379` resource links valid | Test report |
| `python3 tools/audit-seven-part-content.py` | PASS; `831` questions (`302` approved, `360` human-review-required, `169` practice support), `0` structural errors, `37` `AI_TRIAGE` flags | `TOEIC_SEVEN_PART_CONTENT_AUDIT_v2.95.75.md` |
| `python3 tools/audit-mock-readiness.py` | PASS; Reading `200Q` (2 disjoint Full forms); Listening `102Q` (1 Full form / `98%` 2nd-form overlap, Part 1 `8+1=9 < 12`) | `TOEIC_MOCK_READINESS_v2.95.75.md` |
| `python3 tools/build-editorial-review-queue.py` | PASS; `360` reserve items with structured `editorialStatus`/`reviewScope`/`certaintyLevel`/`rationale`/`proposedCorrection` | `TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.75.md` |
| `python3 tools/audit-toeic-coverage.py` & `audit-listening-readiness.py` | PASS; eligible vs reserve split (`102`/`193` Listening, `200`/`87` Reading) | `TOEIC_CONTENT_COVERAGE_v2.95.75.md`, `TOEIC_LISTENING_READINESS_v2.95.75.md` |
| `python3 tools/audit-question-evidence.py`, `audit-distractors.py`, `audit-answer-leakage.py`, `audit-item-complexity.py` | PASS; structural & diagnostic audits complete (`0` structural errors) | Corresponding `*v2.95.75.md` reports |
| `python3 tools/audit-word-family-graph.py` & `audit-related-glossary-quality.py` | PASS; `1,181` headwords, `0` non-reciprocal/POS/duplicate links; `565/567` unflagged glossary rows (`2` low-priority flags) | `WORD_FAMILY_GRAPH_AUDIT_v2.95.75.md/.json` |
| `python3 tools/project-progress-index.py` & `audit-major-release.py` | PASS; provisional weighted index **56.80%** | `PROJECT_PROGRESS_v2.95.75.md/.json`, `MAJOR_RELEASE_QUALITY_AUDIT_v2.95.75.md/.json` |
| `python3 tools/audit-design-tokens.py` & `sync-design-profile.py --check` | PASS; `0` new violations (`2,773` legacy warnings), `54` tokens / `406` typography groups synced | Test report |
| `python3 tools/cmudict_ipa.py --check` & `python3 -m compileall -q tools` | PASS; `334` source-linked CMUdict records, all `tools/` bytecode clean | Test report |
| `node --check server.js`, `sw.js`, `assets/js/*.js` + `tools/tests/*.mjs` | PASS; all JS syntax valid, **45/45** Node regression scripts PASS (`NODE_SUITE_PASS`) | Test report |
| `python3 tools/run-python-tests-sharded.py --timeout-per-module 180` | PASS WITH SKIPS; **114/114** modules (`113` PASS, `1` PASS WITH SKIPS), **838** cases (`837` passed, `0` failed, `1` accepted Git-metadata skip) | `logs/test-shards/PYTHON_TEST_SHARDS_v2.95.75.md/.json` & Test report |
| `python3 -m unittest discover -s tools/tests -v` | PASS WITH SKIPS; `Ran 838 tests` (`OK (skipped=1)`) | Test report |
| `python3 tools/run-release-acceptance.py` | PASS; **12/12** acceptance checks PASS | `logs/release-acceptance/RELEASE_ACCEPTANCE_v2.95.75.md/.json` |
| `git diff --check HEAD^ HEAD` & `python3 tools/audit-git-commit-readiness.py --require-clean` | PASS; verified in clean clone of `candidate` `c7a2f445` with Phase A fixes committed (`0` errors, `0` warnings) | Phase A CI recovery |
| Clean source packaging & `compile_applet` + `lint_applet` | PASS; `/tmp/TOEIC_Dictionary_v2.95.75_FullSource.zip` CRC & clean extraction verified; build & lint PASS | `PACKAGE_VERIFICATION_v2.95.75.md` |

No hosted GitHub Actions run, remote `candidate` push, live GitHub Pages deployment, installed-PWA cache/device verification, or `main` modification was performed.
