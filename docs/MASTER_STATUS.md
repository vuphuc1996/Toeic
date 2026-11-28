# TOEIC Dictionary — Master Status

**Phiên bản mã nguồn đang kiểm kê:** v2.95.83

**Current source release candidate:** v2.95.83 — Part 4 Inference / Part 6 Discourse Evidence Batch. Sole predecessor baseline: candidate HEAD `5eb3b736c3252a38702438efbbbc75e74864189a` (v2.95.82). `main` remains unchanged at `256ca21461e78a7685bed773ddd622a64050e33a`.

## Current release — v2.95.83

- **Scope:** add ten new Part 4 next-step/action practice items, ten Part 6 discourse-purpose mappings, question-level Mock exclusion and human-review handoff. No UI redesign or learner-data migration.
- **Mapping inventory:** **1,139 links / 648 unique stable question IDs**; TOEIC criteria **25/27**; Foundation **6/6**; total **31/33**. Two criteria remain uninstrumented.
- **Part 4:** ten questions appended to ten existing non-reserve talks. All ten use `mockEligible: false`; the Mock engine filters question-level eligibility when selecting, counting and building groups. Part 4 Mock remains 30 questions and all talk blocks remain three questions.
- **Part 6:** ten mappings reference existing questions from four internally reviewed resources; no source question, option or answer key is changed.
- **Review handoff:** Part 1 photo visual verification and Part 7 independent second review are queued. Neither criterion is promoted; reserve/review boundaries remain active.
- **Progress:** provisional weighted measurable curriculum-build index **76.00%**; not learner mastery or total-system completion.
- **Acceptance:** exact-commit mapping audit, Mock engine regressions, full tests, version synchronization and Pages deployment pending.
- **Protected boundaries:** no `main` change, no IndexedDB migration, no UI/layout/navigation or Robot Buddy change; Listening reserve 193, Reading Part 7 reserve 87 and Separate Part 5 review-only 80 remain excluded.

## Previous release — v2.95.82
## Previous release — v2.95.81


- **Scope:** harden the Part 7 cross-document evidence validator and regression tests; no learner-facing feature, content-bank or UI change.
- **Guard improvements:** reject missing/non-string/duplicate document labels, repeated or non-string source labels, non-string/empty source quotes and evidence-basis substring false positives.
- **Inventory:** remains **1,103** canonical mapping links across **638** stable question IDs; TOEIC instrumentation **22/27**, Foundation **6/6**, total **28/33**.
- **Protected gates:** five unsupported TOEIC criteria remain uninstrumented; Listening reserve remains excluded; Part 7 second-review and Separate Part 5 independent-review gates remain active.
- **Protected data/UI:** no question text, choices, answers, vocabulary IDs, learner IndexedDB schema/records, Mock eligibility, layout, navigation or Robot Buddy behavior changed.
- **Release shell:** app, Service Worker and mock-engine version/cache markers advance to v2.95.81 for coherent PWA assets.
- **Acceptance:** Exact candidate source/test HEAD `047781760d0c34788e9153cc402efdec605c3d5f`: GitHub Validate [run 46118675768](https://github.com/vuphuc1996/Toeic/actions/runs/46118675768) **PASS** (151/151 steps, 0 failed, 0 skipped; 853 Python tests PASS). The Part 7 validator regression suite, canonical mapping audit and version synchronization all pass. GitHub Pages [run 46118675714](https://github.com/vuphuc1996/Toeic/actions/runs/46118675714) **PASS** (build, deploy and status-report jobs); environment URL: https://vuphuc1996.github.io/Toeic/. `main` remains unchanged at `256ca21461e78a7685bed773ddd622a64050e33a`; this is a candidate-branch deployment, not a merge to `main`.
- **Offline/device boundary:** installed-PWA/offline propagation and physical-device QA remain **UNVERIFIED**.

## Previous release — v2.95.80


- **Scope:** criterion-to-question map and its audit/tests only; no new learning item, content text or UI feature.
- **Mapping delta:** +21 links; total **1,103** canonical links across the same **638** unique stable question keys.
- **Inventory improvements:** Grammar form recognition **1 → 10**; Listening Part 3 speaker/action **1 → 10**; Part 3 purpose **5 → 7**; Part 4 talk purpose **1 → 2**.
- **Honest remaining limits:** Listening Part 1 visual/audio and detail retention remain **8** each; Reading Part 7 cross-document remains **2** because only two eligible reviewed questions currently have explicit matching quotes from two documents. No reserve item or weakly aligned question is relabeled.
- **Part 7 source guard:** mappings must be in an internally reviewed unit, have two distinct source labels declared in the resource, and have a quote that matches each source document.
- **Outcome totals:** still **22/27** TOEIC criteria instrumented; Foundation **6/6**; total **28/33**. Five unsupported criteria remain uninstrumented.
- **Progress:** provisional weighted measurable curriculum-build index remains **73.73%**. Mapping depth does not increase the instrumented-criterion count.
- **Protected data:** no question content, choice/answer, stable IDs, vocabulary, Mock eligibility, reserve status, learner IndexedDB records/schema, UI, navigation or Robot Buddy logic is changed.
- **Exact candidate acceptance:** source/test HEAD `84a6b55b53c5d07a6f127c06234605efc0098edd` — GitHub Validate **PASS** ([run 46107947688](https://github.com/vuphuc1996/Toeic/actions/runs/46107947688)); 151/151 steps, 0 failed, 0 skipped; Full Python discovery **850 tests PASS**.
- **Mapping audit:** **PASS** — 1,103/1,103 canonical links match bank IDs; 638 unique stable question IDs; 22/27 TOEIC criteria mapped; 28/33 total instrumented; 5 deliberately uninstrumented; 0 Listening reserve mapped; 2 Part 7 cross-document mappings pass the internally reviewed two-source quote check.
- **Focused tests:** mapping guard 4/4, learning outcomes 5/5, project progress tests 4/4 and weighted progress index tests 3/3 all pass.
- **Version synchronization:** **PASS** — 19 release markers, 17 app cache keys, 42 Service Worker cache keys and 1 mock-engine cache key synchronized to v2.95.80.
- **GitHub Pages build/deployment:** **PASS** ([run 46107947573](https://github.com/vuphuc1996/Toeic/actions/runs/46107947573)); build 7/7, status-report 3/3, deploy 3/3.
- **Acceptance boundary:** Source Release Accepted; Candidate CI Verified; Pages Deployment Verified for the v2.95.80 candidate source snapshot. FullSource ZIP generation, installed-PWA/offline propagation and physical-device QA remain **UNVERIFIED**. Production Deployment Accepted on `main` is not granted; `main` remains at `256ca21461e78a7685bed773ddd622a64050e33a`.
- **Test expectation follow-ups:** two narrowly scoped test-only commits refreshed stale 1,082 mapping expectations to the canonical 1,103 links; no application logic or inventory thresholds were relaxed.

## Previous release — v2.95.79

- **Scope:** source release tooling and metadata only. The canonical version remains in `data/manifest.json`; the top-level `package.json` version is now included in the exact-one synchronization registry.
- **Fail-closed behavior:** a package version mismatch is reported; a missing or duplicate package version marker stops before `--apply` writes any file.
- **Regression coverage:** package mismatch, dry-run immutability, successful synchronization, and missing/duplicate marker rejection are added to `test_sync_version.py`.
- **Cache/version sync:** manifest, package, app runtime, Service Worker, mock-engine module cache and HTML release markers target v2.95.79.
- **Protected boundaries:** no vocabulary records, learning banks, question/choice IDs, answer keys, Mock/reserve eligibility, IndexedDB schema/data, UI layout, navigation or Robot Buddy behavior are changed.
- **Exact v2.95.79 source verification:** candidate source commit `76ca52457929493a2a587f7673367bc29eeace49` — GitHub Validate **PASS** ([run 46105814708](https://github.com/vuphuc1996/Toeic/actions/runs/46105814708)); 151/151 steps successful, 0 failed, 0 skipped; Full Python discovery **848 tests PASS**; `test_sync_version.py` **16/16 PASS**. Version sync reports 19 single-instance markers and cache-key checks (17 app, 42 Service Worker, 1 mock-engine) all at 2.95.79.
- **GitHub Pages acceptance:** **PASS** ([run 46105814298](https://github.com/vuphuc1996/Toeic/actions/runs/46105814298)) on the same exact candidate source SHA `76ca52457929493a2a587f7673367bc29eeace49`; build, deploy and status-report jobs completed successfully.
- **Acceptance boundary:** Source Release Accepted; Candidate CI Verified; Pages Deployment Verified for the v2.95.79 source snapshot. FullSource ZIP generation, installed-PWA/offline propagation and physical-device QA remain **UNVERIFIED**. Production Deployment Accepted on `main` is not granted; `main` remains at `256ca21461e78a7685bed773ddd622a64050e33a`.
- **Pages warning boundary:** the prior GitHub-managed Pages workflow emitted Node.js 20 deprecation/dependency warnings while succeeding. This batch does not alter hosting configuration or claim those warnings resolved.
- **Release boundary:** candidate-only source update. `main` remains `256ca21461e78a7685bed773ddd622a64050e33a`; production deployment is not approved.

## Previous release — v2.95.78

- **Outcome instrumentation:** 22/27 TOEIC sub-skill criteria now have an explicit stable question-to-criterion mapping. With the six existing Foundation criteria, 28/33 total criteria have a local evidence-collection path.
- **Question map:** 1,082 question-to-criterion links across 638 unique stable question IDs. Exact canonical resource and question identities are preserved; no bank question, choice ID or answer key is rewritten.
- **Uninstrumented criteria:** Five remain deliberately without separate scoring until a defensible question tag or response rubric exists: Listening Part 1 paraphrase recognition; Listening Part 2 distractor resistance; Listening Part 4 inference/action; Reading Part 6 discourse purpose; Reading Part 7 paraphrase/inference.
- **Runtime:** Criterion-specific correctness, latest-answer tracking, timed accuracy, optional self-report explanation rubrics, delayed recall and source-question reopen are added to the existing learner-local `objectiveProgress` ledger.
- **Progress display:** The dashboard now has an expandable skill-level matrix under the existing Learning Outcome section. It does not redesign the page layout or navigation.
- **Storage protection:** Existing IndexedDB v1 schema, learner workspace, vocabulary records, all 831 assessment/support items, question/choice IDs, answer keys and Mock eligibility remain unchanged. No reset or data migration is introduced.
- **Editorial gates:** All Listening reserve items remain unmapped. Reading Part 7 retains its second-review gate; Separate Part 5 retains its independent-review gate. Mapping availability does not confer Mock approval.
- **Timing / self-report:** Separate Part 5 uses a 30-second internal practice target only. Grammar and Reading Part 5 explanation rubrics are optional learner self-reports, not automatic or independent grading.
- **Project progress:** The provisional weighted measurable build index becomes **73.73%** because more criterion-level software evidence paths exist. It is not learner progress, TOEIC readiness or total system completion.
- **Hosted verification on exact candidate HEAD `0187b446123fca1a8708b496e971e18b19a46c57`:** GitHub Validate **PASS** ([run 46100106836](https://github.com/vuphuc1996/Toeic/actions/runs/46100106836)); 151 steps, 0 failures, 0 skipped, including Full Python test discovery **846 tests PASS**. GitHub Pages build and deployment **PASS** ([run 46100106757](https://github.com/vuphuc1996/Toeic/actions/runs/46100106757)). Both workflows report the same exact SHA.
- **Acceptance boundary:** Source Release Accepted; Candidate CI Verified; Pages Deployment Verified. Installed-PWA cache/offline propagation and physical-device QA remain **UNVERIFIED**. FullSource ZIP generation/package verification remains **NOT DONE**. Production Deployment Accepted on `main` is not granted; `main` remains unchanged at `256ca21461e78a7685bed773ddd622a64050e33a`.

## Previous release — v2.95.77



- **Sole source baseline:** v2.95.76 candidate commit `035dd6e2001b3b049407f71acd21f9c33f33e776`; this is the only predecessor for this release.
- **Migration Profile Reconciliation:** Extended all 7 existing historical migration repair profiles (`979`, `992`, `1026`, `1063`, `1100`, `1137`, `1141`) in `manifest.json` with the exact 40 canonical IDs from Batch 028, and added a new exact profile for the 1,181-word v2.95.75 snapshot (`1181`) with those 40 Batch 028 IDs.
- **CI Recovery & Integrity Fix:** Resolved the vocabulary release integrity test failure (`1221 !== 1181` in `vocabulary-release-integrity.mjs`), ensuring full test compatibility with the 1,221-word inventory (`v2.95.76` / `v2.95.77`).
- **Version Synchronization:** Synchronized release version markers, application cache keys (`__release=2.95.77`), and Service Worker precache URLs across all 7 synchronized files via `tools/sync-version.py`.
- **Protection:** Maintained all 1,221 canonical words, all 831 question/support items, Mock eligibility rules, learner IndexedDB schema, and UI/UX layout unchanged. `main` branch remains untouched.
- **CI remediation commits (2026-11-28):** Updated historical Batch 027 and Batch 028 tests to distinguish immutable batch metadata from the current manifest version; restored the release acceptance runner's safe `--resume` flag; reconciled the 1,141-word migration profile expectation to the exact ordered 80-ID union (40 Batch 026 + 40 Batch 028). No vocabulary records or migration data were changed by these four test/runner-only commits.
- **Hosted verification on exact candidate HEAD `c9e1149352624a729e6c0881905a8d8384f0993e`:** GitHub Validate **PASS** ([run 46095139242](https://github.com/vuphuc1996/Toeic/actions/runs/46095139242)); GitHub Pages build and deployment **PASS** ([run 46095138907](https://github.com/vuphuc1996/Toeic/actions/runs/46095138907)). Both runs report the same exact HEAD SHA.
- **Acceptance boundary:** Source Release Accepted; Candidate CI Verified; Pages Deployment Verified. Installed-PWA cache/offline propagation and physical-device QA remain **UNVERIFIED**. Production Deployment Accepted on `main` remains **UNVERIFIED**; `main` is unchanged at `256ca21461e78a7685bed773ddd622a64050e33a`.


## Previous release — v2.95.75

- **Baseline source:** Local completed `v2.95.74` baseline preserved untouched against older GitHub `candidate` (`cfae6ce`, `v2.95.73`). `main` branch never modified.
- **7-Part Authoritative Inventory & Audit (`TOEIC_SEVEN_PART_CONTENT_AUDIT_v2.95.75.md`):** `831` total questions (`102` Listening + `200` Reading = `302` `APPROVED_FOR_MOCK`; `193` Listening + `87` Part 7 + `80` Separate Part 5 = `360` `HUMAN_REVIEW_REQUIRED`; `58` lessons / `169` exercises `PRACTICE_SUPPORT` Grammar). Zero structural errors, zero duplicate stems, strict separation of `AI_TRIAGE / STRUCTURAL` signals from human approval.
- **Learning Outcome Reconciliation (`TOEIC_LEARNING_OUTCOME_EVIDENCE_v2.95.75.md`):** Reconciles all 11 objectives / 33 criteria (`objective-outcomes.json` + `audit-learning-outcomes.py`). Foundation remains `6/33` (`18.2%`) criterion-instrumented; all 9 TOEIC objectives document group-level tracking (`objectiveProgress`), Part 5-only `explanation_rubric`, Listening reserve exclusion, Part 1 `8/10` eligible cap, and `content_review_pending` gates.
- **Evidence & Privacy Hardening:** Fixed `completedMocks.length > 0` array-comparison bug in `robot-learning-insights.js`, hardened null/boolean/empty-string numeric parsing across `robot-learning-insights.js`, `mock-score-readiness.js`, and `learning-outcome-progress.js`, added `attemptId` deduplication in `mock-score-readiness.js`, and wrapped `app.js` practice/rubric persistence paths cleanly in `try/catch`.
- **Enhanced Review Queue & Mock Readiness (`TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.75.md`, `TOEIC_MOCK_READINESS_v2.95.75.md`):** Added structured `editorialStatus`, `reviewScope`, `certaintyLevel`, `rationale`, `proposedCorrection`, and AI triage cross-refs to all `360` reserve items; consolidated Full (`200Q`), Half (`100Q`), Quick (`25Q`), and Part practice readiness confirming 2 disjoint Reading forms (`200Q`) vs 1 Full Listening form (`102Q`, `98%` 2nd-form overlap, Part 1 `9/12` post-review ceiling).
- **Acceptance boundary:** Source Release Accepted (local workspace only). Hosted GitHub Actions, remote `candidate` push, live Pages deployment, installed-PWA cache/offline propagation, and physical-device QA remain **UNVERIFIED**.

## Previous release — v2.95.74 / v2.95.71

- **Sole predecessor FullSource:** `TOEIC_Dictionary_v2.95.70_FullSource.zip`; SHA-256 `1a0df44d309d127df3d3fb5012e7a6654c93a450c591f1f67575f4d15822e672` (864 files; ZIP CRC verified). No older archive, alternate source or Patch was used as input.
- **Batch 045:** 23 existing Related Glossary rows receive POS, English definitions, Cambridge Dictionary provenance and exact URLs. All 567 glossary terms, Vietnamese meanings and relation arrays are preserved; no canonical headword/ID or graph edge is added.
- **Quality screening:** 119/567 glossary rows remain flagged, down from 142 (−23). Missing definitions 78, placeholders 37, missing POS 115, missing provenance 39; duplicate normalized groups 0. These are automated flags, not editorial approval.
- **Progress dashboard:** transparent weighted measurable curriculum-build index **54.47%**, based on seven published workstreams/weights. It is provisional and excludes all unmeasured or externally gated areas; it must not be represented as overall production completion or learner mastery. See `docs/reports/PROJECT_PROGRESS_v2.95.71.md` and `tools/project-progress-plan-v2.95.71.json`.
- **Pronunciation guard:** 79 missing US IPA entries were reviewed through the CMUdict preview; 0 met safe auto-apply conditions. No uncertain IPA was guessed or inserted.
- **Protection:** no vocabulary canonical IDs/headwords/senses/relations, question/choice IDs, answer keys, learning banks, Mock eligibility, learner IndexedDB schema/records or UI layout changed. No backend/Cloudflare architecture added.
- **Final local test evidence:** Python 107/107 modules, 799 cases (798 PASS, 1 accepted Git-metadata SKIP, 0 FAIL/timeout/error/unrun); Node 45/45 PASS; validator 1,141 IDs +0/−0, 0 errors/0 legacy warnings; learning content 0 errors/0 warnings; repository integrity 409 checked/0 errors; Part 1 assets 9/9; version sync 18 release markers +17 app imports +42 Service Worker URLs; design profile 54 tokens/406 typography groups; design-token audit 0 new violations with 2,773 legacy warnings.
- **Read-only graph debt:** Word Family audit retains 90 missing targets, 1 POS mismatch, 72 Vietnamese sense-anchor mismatches and 10 non-reciprocal links; no links were auto-repaired.
- **Reports:** `TEST_REPORT_TOEIC_Dictionary_v2.95.71.md`, `PYTHON_TEST_SHARDS_v2.95.71.md/.json`, `NODE_TEST_REPORT_v2.95.71.md`, `DATA_DIFF_v2.95.71.md`, `RELATED_GLOSSARY_BATCH_045_v2.95.71.md`, `PROJECT_PROGRESS_v2.95.71.md/.json`, `WORD_FAMILY_GRAPH_AUDIT_v2.95.71.md/.json`, `CHANGE_MANIFEST_v2.95.71.md`, `PACKAGE_VERIFICATION_v2.95.71.md` and `COMMAND_LOG_INDEX_v2.95.71.md`.
- **Acceptance boundary:** hosted GitHub Actions, live Pages deployment, installed-PWA cache/offline behavior and physical-device tests remain unverified. This is a locally verified source candidate, not production deployment acceptance.

## Previous release — v2.95.70

- **Sole predecessor FullSource:** `TOEIC_Dictionary_v2.95.69_FullSource.zip`; SHA-256 `4ec559a2117a1b1b38ef95d4a0d6955431b46e701cf208bd939bd38db232e853` (847 files; ZIP CRC verified). No older archive, alternate source or Patch was used as input.
- **One-way completion contract:** every shared assessment-result summary exposes exactly one explicit action, `Xác nhận & xem đáp án`. The post-completion return/recheck action, its event handler, practice/Foundation return helpers and obsolete saved-draft toast were removed. Draft data remains staged until the confirmation commit.
- **Foundation reliability:** Foundation progress is built as a separate next-state object and persisted before in-memory committed progress, pending state or answer review is advanced. A localStorage failure leaves the old progress, pending summary and draft choices intact so the existing confirmation handler can report the error and allow retry.
- **Regression coverage:** Node behavioral test covers one-action markup, absence of legacy return routes, Foundation write failure and successful persist-before-reveal. Focused suites also cover Learning Focus result reuse, deferred assessment commit, choice history and distractor quality.
- **Data protection:** no vocabulary IDs/headwords/relations, question IDs, choice IDs, answer keys, protected learning-bank JSON, Mock eligibility, IndexedDB schema or Foundation draft schema changed. No UI layout redesign or new backend/service was introduced.
- **Local verification:** Python 105/105 modules terminal (789 cases: 788 PASS, 0 FAIL, 1 accepted Git-metadata SKIP); Node 45/45 PASS. Data validator 1,141 IDs +0/-0, 0 errors/warnings; learning content 0 errors/warnings; repository integrity 409 inspected/0 errors/0 optional warnings; Part 1 assets 9/9; design tokens 0 new violations; release marker/app import/SW cache synchronization and design profile sync PASS.
- **Data comparison:** all 68 `data/` files retain the same paths; only `data/manifest.json` differs, with `version` `.69`→`.70`. All other data files are byte-identical. No learner IndexedDB migration, canonical vocabulary or question/choice/answer changes were made.
- **Reports:** `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.70.md`, `PYTHON_TEST_SHARDS_v2.95.70.md/.json`, `NODE_TEST_REPORT_v2.95.70.md`, `DATA_DIFF_v2.95.70.md`, `CHANGE_MANIFEST_v2.95.70.md`, `PACKAGE_VERIFICATION_v2.95.70.md` and `COMMAND_LOG_INDEX_v2.95.70.md`.
- **Acceptance boundary:** hosted GitHub Actions, live Pages deployment, installed-PWA cache/offline behavior and physical-device checks remain unverified. No Git push or production deployment is claimed.

## Previous release — v2.95.69

- **Sole predecessor FullSource:** `TOEIC_Dictionary_v2.95.68_FullSource.zip`; SHA-256 `2313f612e536c618b91fa1462611dffba7c9539f9e1a019a9b3ac4de79941c2a` (816 files; ZIP CRC verified). No older archive, alternate source or Patch was used as an input.
- **Batch 044:** 15 existing Related Glossary rows enriched only in `pos`, `definition_en`, `source`, `sourceUrls` and `sourceRelease`. All 567 term identities, Vietnamese meanings and relation arrays remain unchanged.
- **Glossary quality:** 567 rows; 142 flagged, down from 157. Missing definitions 92, placeholders 46, missing POS 138, missing provenance 48; duplicate normalized-term groups 0. Remaining rows stay in a review queue, not auto-applied.
- **Release cache coherence:** `tools/sync-version.py` now checks/updates cache-busting keys across `assets/js/app.js` and `sw.js`. The release has 17/17 app imports and 42/42 Service Worker URLs keyed to manifest `2.95.69`; corresponding regression tests cover discovery, apply and check.
- **Historical/test integrity:** earlier glossary snapshot tests reverse Batch 044 in chronology. The flashcard/Robot Buddy test expectations now require the active Learning Focus dialog to be reused, with a modal fallback only outside active focus; no UI/CSS redesign was made.
- **Python inventory:** 104/104 modules completed; 785 cases, 784 PASS, 0 FAIL, 1 accepted skip, 0 error/timeout/incomplete. One skip requires `.git` metadata unavailable in a FullSource ZIP; its other 19 cases passed. The aggregate joins disjoint completed module evidence; it is not represented as one uninterrupted invocation.
- **Node regression:** 44/44 scripts PASS. Data validator: 1,141 canonical records, IDs +0/-0, 0 new errors/warnings. Learning-content validation 0 errors/warnings; Part 1 assets 9/9; repository integrity 408 inspected/0 errors; version sync 18 standard markers plus 17 app imports + 42 SW cache keys; JavaScript syntax PASS.
- **Design tokens:** 0 new violations; 2,773 historical legacy warnings remain. **Word Family audit** remains read-only with review flags (90 missing targets, 1 POS mismatch, 72 Vietnamese sense-anchor mismatches, 10 non-reciprocal links); no graph repairs were auto-applied.
- **Data protection:** only `data/manifest.json` release marker and the 15 approved existing glossary metadata rows changed under `data/`. Canonical vocabulary IDs/headwords/relations, all protected learning-bank files, question/choice IDs, answer keys, eligibility and IndexedDB schema/records were not changed.
- **Reports:** see `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.69.md`, Python/Node reports, `DATA_DIFF_v2.95.69.md`, `WORD_FAMILY_GRAPH_AUDIT_v2.95.69.md`, `CHANGE_MANIFEST_v2.95.69.md`, package verification and command-log index.
- **Package evidence:** FullSource has 847 files. The Patch contains 31 added, 28 modified and 0 deleted paths; clean replay from the exact `.68` archive reproduces all 847 target files with 0 extra, 0 missing and 0 byte differences.
- **Acceptance boundary:** local source tests, validators and exact Patch replay are documented. Hosted GitHub Actions, live Pages deployment, installed-PWA cache/offline propagation and physical-device acceptance remain **UNVERIFIED**. This is a locally validated source candidate, not a production-deployment acceptance.

## Non-negotiable data boundaries

- The 193 Listening reserve questions and 87 Reading reserve questions remain excluded from Mock until independent approval.
- All canonical vocabulary IDs/headwords and TOEIC question/choice/answer-key identities remain protected. Batch 025's six Word Family links are the only recorded canonical relation additions in v2.95.67; v2.95.68 adds no data relation or question content.
- The v2.95.55 complete learner-data backup and guarded restore remains intact. Existing attempt-history records are read without migration.
- UI layout and navigation are frozen.

## Stage 2 progress

| Audit item | Status | Notes |
|---|---|---|
| 5. Full learner data export/import | Implemented in v2.95.55 | Full IndexedDB workspace + `toeic:` localStorage backup, integrity validation and guarded merge restore |
| 6. Listening reuse / trend integrity | Implemented in v2.95.56 | Listening trend requires two distinct question-ID forms; high overlap is disclosed; Reading remains independent |
| 7. Answer leakage / distractor overlap | Implemented in v2.95.57 | Read-only lexical/length triage; 6 review signals; no answer/content mutation |
| 8. Answer-position skew | Existing implementation verified | Historical controlled reorder certificates retain stable choice identity; 27 changes in v2.17.0 and 6 in v2.33.0 |
| 9. Evidence and difficulty | Structural triage implemented; independent review/calibration open | Source evidence + transparent complexity signals; no CEFR/ETS difficulty claims |
| 10. Learning outcome accuracy | Implemented in v2.95.58 | First-attempt and latest-attempt accuracy are reported separately from the same retained attempt history |

Stage 2: **6/6 workstreams implemented (100%)**; item 9 is structurally instrumented but independent review and psychometric calibration remain external acceptance gates, not marked complete.

## Non-negotiable data boundaries

- The 193 Listening reserve questions and 87 Reading reserve questions remain excluded from Mock until independent approval.
- Across v2.95.61–v2.95.66, no canonical vocabulary IDs/headwords/meanings/relations, question IDs/choices/answer keys, Mock eligibility, learner-history schema, or Robot Buddy access boundary changed. v2.95.66 modifies only runtime release-shell cache coherence, startup/DOM guards, CI test contracts, regression tests and release documentation; learner IndexedDB stores/schema and records are untouched.
- The v2.95.55 complete learner-data backup and guarded restore remains intact. Existing attempt-history records are read without migration.
- UI layout and navigation were not redesigned.

## Acceptance boundary — v2.95.66 historical

For v2.95.66, focused regression cases and all 43 Node scripts listed in the current test report pass. The 100-module Python shard excluding the heavy validator module is PASS: 727/727 collected test cases, with zero fail/skip/error. `test_validator.py` (44 methods) did not complete as a whole within the execution window: its first 21 tests completed PASS before the next test exceeded the window; the two new release-query validator cases pass separately (2/2), and the production data validator CLI passes. Therefore the overall 101-module Python inventory remains INCOMPLETE, not full-suite PASS. Hosted GitHub Actions and GitHub Pages deployment for v2.95.66, active-worker update acceptance, installed-PWA/offline propagation and physical iOS/iPadOS/Android behavior remain **UNVERIFIED**.

## Acceptance boundary — v2.95.68

- Source baseline: the uploaded `TOEIC_Dictionary_v2.95.67_FullSource(1).zip` (SHA-256 `1f262ac4d67d8d244facf397b9ea1d179c6a741f50e561b3d3e9805efef31754`) only.
- Assessment-result focus workflow: PASS; existing focus dialog reused and modal layer remains hidden; prior content and ARIA state restore; confirmation dispatch uses existing commit logic.
- JavaScript syntax and Service Worker syntax: PASS. Node regression scripts: 44/44 PASS. Python targeted regressions: Batch 025 5/5, Batch 036 6/6, Batch 037 7/7, Merge 038 8/8, single-overlay contract 3/3 PASS.
- Data validation: 1,141 canonical records, baseline ID +0/-0, 0 errors / 0 warnings; learning content 0 errors / 0 warnings; Part 1 assets 9/9; repository integrity 0 errors / 0 warnings; design-token audit 0 new violations.
- Full Python discovery was attempted but the process did not finish and yielded no final unittest summary. Overall Python inventory is INCOMPLETE, not full-suite PASS.
- No source data changes except the release marker in `data/manifest.json`; exact Patch replay and FullSource package verification are recorded in `PACKAGE_VERIFICATION_v2.95.68.md` after replay.
- Hosted GitHub Actions, live Pages deployment, installed-PWA/offline propagation and physical-device acceptance remain UNVERIFIED.

## Acceptance boundary — v2.95.67

- Source state: **candidate with focused local verification**. The full Python test inventory has not been completed for this release. Current discovery finds 102 Python test modules; 17 selected modules completed 161/161 cases PASS. Two additional targeted `test_validator.py` release-key cases pass separately. The full 44-method validator module did not complete in the available execution window, and the remaining full-suite inventory is not claimed as passed.
- Node regression: 43/43 scripts PASS. Data validator: 1,141 canonical records, 0 errors / 0 warnings, IDs +0/-0. Learning-content validator: 0 errors / 0 warnings. Part 1 assets 9/9. Version markers 18/18. JavaScript syntax and Python compileall PASS. Repository integrity: 407 references/data files, 0 errors / 0 optional warnings. Design-token audit: 0 new violations; 2,773 legacy warnings.
- Batch 025 adds six reciprocal word-family links and zero canonical headwords/IDs. No question/choice/answer-key data, Mock eligibility, learner IndexedDB schema/records, UI layout or Robot Buddy privacy boundary changed.
- GitHub-hosted Actions, Pages deployment, installed-PWA cache propagation and physical-device acceptance remain **UNVERIFIED**. The candidate has not been pushed to the live branch.

## Previous completed work

- v2.95.56: Listening Mock form-diversity gate. See `reports/MOCK_LISTENING_FORM_DIVERSITY_v2.95.56.md`.

- v2.95.55: full learner-data backup and guarded restore. See `docs/reports/LEARNER_DATA_BACKUP_v2.95.55.md` and `docs/reports/RELEASE_ACCEPTANCE_v2.95.55.md`.
- v2.95.54: Stage 1 independent audit remediation and release evidence.

## v2.95.59 — item complexity review queue (2026-11-24)

- Added read-only complexity triage for the full Listening/Reading question inventory. Observable signals include source length, prompt length, answer-option length spread, inference/purpose wording and multi-document indicators.
- Does not infer difficulty or CEFR, does not use learner response statistics, and does not modify question content or Mock eligibility.
- Reserve-pending items remain excluded from Mock. Independent review, pilot response data and psychometric calibration remain open.

## v2.95.66 — runtime shell coherence and CI regression hardening (2026-11-25)

- Exact baseline: `TOEIC_Dictionary_v2.95.65_FullSource.zip`; SHA-256 `a1b95e807e08052bfa599a08ff88bc3237ae086688557ce3ae77b78e814814fb`.
- Corrected the Batch 022 CI contract to validate the actual `unittest discover` command. The focused Batch 022 suite passes 9/9.
- Version-keyed the HTML manifest, stylesheets, app module, every local app import and data requests. Added a second `__shell` key so older active Service Workers do not normalize v2.95.66 resource URLs to old cache entries.
- Kept root navigation on the currently active worker's cached HTML while an updated worker is waiting for user approval, preventing a fresh HTML shell from being paired with old cache-first assets.
- Added the startup HTML/JavaScript release consistency guard, optional DOM binding for `#modalLayer`, a complete required listener-target contract test and service-worker mixed-release regression.
- Focused test results and the full Python-shard completion status are recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.66.md` and `reports/PYTHON_TEST_SHARDS_v2.95.66.md`.
- No learning-bank/vocabulary content, IDs, answer keys, eligibility, learner storage or Robot Buddy privacy rules were changed.

## v2.95.65 — Batch 035 Cambridge history and single shared modal overlay (2026-11-25)

- Baseline: exact `TOEIC_Dictionary_v2.95.64_FullSource.zip`; SHA-256 `03ec4c80e88bc76e435cfc0782e933474be882a4f271318a23375a35e9242673`.
- Replaced the stale hosted-only `test_related_glossary_batch_035_cambridge.py` with a checked-in historical test that reverses later Batch 036–038 additions and reviewed correction operations before asserting the Batch 035 snapshot/hash. Both modules are selected by `test_related_glossary_batch_035*.py`; 10/10 tests pass locally.
- Removed `modalBackdrop`/`.modal-backdrop`; the modal panel layer is nested within the existing `learningFocusBackdrop`, which is the sole full-screen overlay. Modal-only and active-focus cases preserve their distinct close behavior without duplicating the dimming layer.
- Added overlay contract regression tests and an explicit GitHub Actions test step. Modal dismissal simulation and all Node regression scripts pass. Design-token audit reports zero new violations after documented selector identity reconciliation.
- No learning content or learner IndexedDB data/schema changed. Hosted Actions, Pages deployment and device testing remain unverified.

## v2.95.64 — GitHub commit-readiness and CI reliability (2026-11-25)

- Baseline: exact `TOEIC_Dictionary_v2.95.63_FullSource.zip`; SHA-256 `6d43a7f44e1cc84d6ad7f3ee9dae660cceb83c792668d0966ce1060f4aa9ea80`.
- Added read-only Git commit readiness checks for clean/staged status, path portability/case collisions, symlinks, file size, release artifacts, ignored output paths, LF/binary attributes and whitespace in only the current commit/staged diff (legacy historical trailing whitespace is not mass-edited).
- Pinned official GitHub Actions at verified full SHAs; added `fetch-depth: 2` for the commit-diff preflight and trigger paths for `.gitignore`/`.gitattributes`.
- Repository-integrity audit now recognizes default `unittest discover` `test*.py`; CI coverage detects duplicate module selectors and duplicate workflow step labels. Two duplicate test executions were removed; full tools syntax check now uses `compileall`.
- No learning data or UI/runtime changes. Focused commit-preflight tests are recorded; complete 97-module Python suite started but the container execution window expired after 19 modules had passed. The full suite is therefore **INCOMPLETE**, not PASS. GitHub-hosted Actions and real Windows/macOS clone/commit checks remain unverified.

## v2.95.63 — CI discovery and modal lifecycle remediation (2026-11-25)

- Exact source baseline: v2.95.62 FullSource SHA-256 `b9d56cd27d0d13c4c8781732ac72c17b526b2aa451fa1393c39fd30820260f96`; the older uploaded v2.95.60 archive was excluded.
- Fixed unittest discovery pattern for Batch 035 to `test_related_glossary_batch_035*.py`, covering `test_related_glossary_batch_035_cambridge.py` if present in the CI checkout. Added explicit regression coverage for wildcard semantics and complete Python/Node test inventory registration.
- Repaired safe modal dismissal for result, answer explanation and auto-advance wait states. The result modal keeps the three requested stats; X/Escape commits or saves pending state safely. Closing explanation leaves inline answer feedback; closing the wait cancels auto-next and preserves the current question. Transient overlay state is cleared and focus returns to a visible close control.
- Added `tools/tests/modal-dismissal-workflow.mjs` and registered it in GitHub Actions. No CSS redesign, data change, ID migration or IndexedDB schema change.
- Local Node regression suite: 43/43 PASS. Focused Python suites: 42 test cases PASS across 8 modules (CI coverage 4, repository integrity 1, PWA 3, responsive 8, learning surface 5, practice fallback 6, sync-version 12, source package 3). Syntax and repository/data validators PASS. Complete Python suite and remote/physical deployment checks remain unverified.

## v2.95.62 — Related Glossary Batch 043 (2026-11-25)

- Exact source baseline: v2.95.61 FullSource SHA-256 `63bb04e7f9bbb15fa76ff00ab833b392bf6d48e71ecafd8740b05c2ff1cb56b7`; the uploaded v2.95.60 archive was not used.
- Added paraphrased Cambridge Dictionary definitions/POS/provenance to 21 existing relation-target rows selected via existing vocabulary synonym/antonym anchors. Batch report and per-term ledger record source URLs, sense notes and the independent-review gate.
- Quality audit: 567 rows; 157 flagged (153 high, 2 medium, 2 low); 103 missing definitions, 50 placeholders, 153 missing POS, 52 missing provenance; zero duplicate groups. Relation coverage remains 556/804.
- Preserved all term identities, Vietnamese meanings and relation arrays. No canonical vocabulary or question/choice/answer-key data, learner data/IndexedDB, Mock eligibility, Robot Buddy boundary, UI or hosting architecture changed.
- Definitions use indexed dictionary entry excerpts reviewed 2026-11-25, paraphrased; direct page fetch status was not asserted. Independent editorial review remains pending.
- Local test/validator/package results are in v2.95.62 reports. Hosted CI, Pages, installed-PWA cache/offline and physical-device acceptance remain unverified.

## v2.95.61 — Related Glossary Batch 042 (2026-11-25)

- Development base: exact `TOEIC_Dictionary_v2.95.60_FullSource.zip`; SHA-256 `b4e5404b824991208d99babb3f471b45e9e27fded1d31327854ae3a15ce58838`.
- Added sourced English definitions/POS to 20 existing relation-target rows. Sixteen are Cambridge Dictionary paraphrases; four copy every existing sense definition verbatim from the exact canonical headword in v2.95.60.
- The guarded patch binds to `data/related-terms.json` SHA-256 `dbc233b11ab0b8f351092bb404fe2010f9e54091e2590c5765b68cc1b8d3f97e`. The provenance ledger records exact URLs, source method, POS, sense alignment and relation anchors.
- Quality audit: 567 rows; 178 flagged (174 high, 2 medium, 2 low); 111 missing definitions, 63 placeholders, 174 missing POS, 65 missing provenance; zero normalized duplicate groups.
- Preserved all existing term identities and Vietnamese meanings. No canonical vocabulary/relationship arrays, question/choice IDs, answer keys, Mock eligibility, learner records, IndexedDB schema, Robot Buddy privacy boundary, UI layout or hosting architecture changed.
- Cambridge direct retrieval returned HTTP 403 for some entries; indexed dictionary excerpts were reviewed. Independent editorial review remains pending.
- Local validation and exact package replay are recorded in the v2.95.61 reports; remote CI, Pages and physical devices remain unverified.

## v2.95.60 — consolidated IPA and Related Glossary quality queues (2026-11-24)

- Development base: exact `TOEIC_Dictionary_v2.95.59_FullSource.zip`; SHA-256 `b5dbb4e7c974814c8d59fc6bf653737f7208e7da2c2d49141078efff385d993c`.
- Added a deterministic missing-US-IPA review inventory from exact-headword CMUdict lookup. 79 records: 5 single-pronunciation candidates, 49 multi-variant cases requiring review, 25 with no exact dictionary key. CMUdict package version is recorded; ARPABET remains the evidence format. No IPA was converted or inserted.
- Added a Markdown renderer and regression tests for queue counts, variant display and the no-auto-apply boundary.
- Rebuilt Related Glossary quality and relation-frequency queues: 567 entries; 198 flagged (194 high, 2 medium, 2 low); 131 missing definitions; 63 placeholders; 190 missing POS; 65 missing provenance; 0 normalized duplicate groups.
- Candidate coverage audit: 567 glossary entries, 804 distinct referenced terms, 248 distinct terms / 249 reference occurrences not covered; no canonical candidate was auto-imported.
- The v2.95.59 non-calibrated complexity inventory remains part of the baseline: 582 questions; 280 reserve-pending (193 Listening, 87 Reading); all reserve remain excluded from Mock.
- No canonical vocabulary fields, IDs, headwords, relation arrays, question content/IDs/choices/answer keys, learner data, IndexedDB schema, Mock eligibility, UI layout or hosting architecture changed. This release adds reports/tooling/tests and synchronized release markers only.
- Full hosted Actions, Pages deployment, cache propagation and physical-device acceptance remain unverified.

## v2.95.67 — Word Family graph integrity and sourced reciprocal enrichment (2026-11-26)

- Baseline: exact `TOEIC_Dictionary_v2.95.66_FullSource.zip`; SHA-256 `30236500cfa2d8702a25cdca9c99f0eca58eaaa047928a6b12ce88b1b2a373c3`.
- Added six reciprocal, sense-matched `word_family` links across apologize/apology, subscribe/subscription and transport/transportation. Zero headwords or canonical IDs added; Vietnamese meanings are copied from target senses already present in the dictionary.
- Added a Cambridge-source ledger, dedicated family-link regression tests and a read-only graph audit for missing targets, POS mismatches, sense-anchor mismatches, duplicate/malformed links and non-reciprocity. Review flags are not automatically fixed.
- No learner progress, IndexedDB schema, question/choice/answer-key data, Mock eligibility, UI, Robot Buddy behavior or hosting architecture changed.
- Local evidence and known limits are in `docs/reports/*v2.95.67*`; remote Pages/Actions and physical-device checks remain unverified.
