# Test Report — TOEIC Dictionary v2.95.75

## Source baseline

- Preserved predecessor: verified local `v2.95.74` workspace snapshot (ahead of older GitHub `candidate` `cfae6ce`, which remained at `v2.95.73`).
- Canonical vocabulary: `1,181` headwords (`A`–`Z`, `+0/−0` IDs).
- Related Glossary: `567` entries (`565` unflagged, `2` low-priority `short-definition-review` flags).
- Assessment inventory: `831` total questions (`302` `APPROVED_FOR_MOCK`, `360` `HUMAN_REVIEW_REQUIRED`, `169` `PRACTICE_SUPPORT` Grammar exercises).

## Node & JavaScript regression

- Syntax checks (`node --check server.js`, `node --check sw.js`, and all `22` browser modules in `assets/js/*.js`): **PASS**.
- Node regression suite (`tools/tests/*.mjs`): **45/45 scripts PASS**, terminal marker `NODE_SUITE_PASS (45 scripts)`.
- Python bytecode check (`python3 -m compileall -q tools`): **PASS**.

## Sharded Python test suite

- Runner: `python3 tools/run-python-tests-sharded.py --timeout-per-module 180`
- Modules executed: **113 / 113** (`112` PASS, `1` PASS WITH SKIPS, `0` FAIL, `0` TIMEOUT, `0` INCOMPLETE, `0` ERROR, `0` NOT RUN)
- Test cases: **828** collected (`827` passed, `0` failed, `1` skipped, `0` errored, `0` unapproved skips)
- Accepted skip detail: `tools/tests/test_patch_data.py::PatchDataTests.test_repository_gitignore_excludes_audit_logs` — `source archive has no Git metadata; gitignore assertion requires a clone` (approved in `tools/test-inventory-policy.json`).
- Acceptance wrapper (`python3 tools/run-release-acceptance.py`): **12/12** checks PASS.

## Validators & domain audits

| Check | Result |
|---|---|
| `tools/validate-data.py` | PASS; `1,181` records; IDs `+0/−0`; `0` errors, `0` legacy warnings |
| `tools/validate-learning-content.py` | PASS; `295` Listening + `287` Reading + `169` Grammar + `80` Separate Part 5 (`0` errors/warnings) |
| `tools/validate-part1-photo-assets.py` | PASS; `9/9` local Part 1 photos valid; `0` warnings |
| `tools/audit-repository-integrity.py` | PASS; `414` local references/data files inspected; `0` errors, `0` optional warnings |
| `tools/sync-version.py --check` | PASS; all release markers + `17` `app.js` keys + `42` `sw.js` keys + `1` `mock-engine.js` key synchronized to `2.95.75` |
| `tools/sync-design-profile.py --check` | PASS; `54` tokens and `406` typography selector groups synchronized |
| `tools/audit-design-tokens.py` | PASS; `0` new violations; `2,773` legacy warnings remain |
| `tools/audit-learning-outcomes.py` & `audit-learning-outcome-evidence.py` | PASS; `11/11` objectives, `33` criteria (`6/33` Foundation criterion-instrumented, `11/11` group-level wired) |
| `tools/audit-objective-resources.py` | PASS; `379/379` canonical resource links valid |
| `tools/audit-seven-part-content.py` | PASS; `831` questions (`302` approved, `360` human-review-required, `169` support), `0` structural errors, `0` duplicate stems, `37` `AI_TRIAGE` flags |
| `tools/audit-mock-readiness.py` | PASS; Reading `200Q` (2 disjoint Full forms); Listening `102Q` (1 Full form, `98%` 2nd-form overlap, Part 1 `8+1=9 < 12` bottleneck) |
| `tools/build-editorial-review-queue.py` | PASS; `360` reserve items with structured editorial metadata + AI triage cross-refs |
| `tools/audit-distractors.py`, `audit-answer-leakage.py`, `audit-item-complexity.py` | PASS; `264` distractor scope + `156` reserve structural checks PASS; `6/177` leakage flags (read-only); `106/582` complexity signals, `0` errors |
| `tools/project-progress-index.py` | PASS; provisional weighted curriculum-build index **56.80%** (`565/567` unflagged glossary rows) |
| `compile_applet` & `lint_applet` | PASS; static Express server and PWA assets verified |

## Implemented workstreams completed in v2.95.75

1. **7-Part Inventory & Evidence Audit (Workstreams A & B):** Authoritative audit across `831` questions separating `302` `APPROVED_FOR_MOCK`, `360` `HUMAN_REVIEW_REQUIRED`, and `169` `PRACTICE_SUPPORT`, keeping structural/lexical AI triage signals strictly separate from human approval.
2. **33-Criterion Learning Outcome Reconciliation (Workstream C):** Reconciled `objective-outcomes.json`, `audit-learning-outcomes.py`, and `audit-learning-outcome-evidence.py` across all `11` objectives (`6/33` Foundation criterion-level instrumented, `11/11` group-level runtime tracked, Part 5-only `explanation_rubric`, Part 1 `8/10` eligible cap, zero certification claims).
3. **Learner Evidence & Storage Hardening (Workstream D):** Fixed `completedMocks.length > 0` in `robot-learning-insights.js`, added finite-number/bounds/deduplication hardening across `robot-learning-insights.js`, `mock-score-readiness.js`, and `learning-outcome-progress.js`, and wrapped `app.js` practice/rubric writes in `try/catch` error-toast recovery.
4. **Independent Review Queue & Full-Mock Readiness Consolidation (Workstreams E & F):** Enriched all `360` reserve items with structured editorial decision metadata and documented exact Full (`200Q`), Half (`100Q`), Quick (`25Q`), and Part readiness including the Part 1 (`8+1=9/12`) Listening bottleneck.
5. **Release Shell, Test & CI Coherence (Workstream G):** Synchronized `mock-engine.js` `__release` keys, updated `.github/workflows/validate-data.yml`, updated `test_project_progress_index.py` / `test_sync_version.py` / `test_release_shell_coherence.py`, and produced all `v2.95.75` audit & release documentation.

## Acceptance boundary — Source Release Accepted vs Production Deployment Accepted

- **Source Release Accepted (local workspace):** Verified across all `113` Python test modules, `45` Node regression scripts, data/content/asset/design/version/repository validators, build/lint checks, and clean ZIP packaging.
- **Production Deployment Accepted (UNVERIFIED / NOT CLAIMED):**
  - Git push to `candidate` was not executed (`main` remains untouched).
  - Hosted GitHub Actions workflow execution was not triggered or observed.
  - Live GitHub Pages deployment, installed-PWA cache/update propagation, and physical iOS/iPadOS/Android device QA were not performed.
  - Zero ETS scaled score conversion and zero CEFR/ETS certification claims are made.
