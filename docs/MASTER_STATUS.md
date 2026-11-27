# TOEIC Dictionary — Master Status

**Phiên bản mã nguồn đang kiểm kê:** v2.95.73

**Current source candidate:** v2.95.73 — Batch 027 Word Family reciprocity and self-reference repair. The active development branch is `candidate`; production `main` remains v2.95.71 until explicit acceptance and promotion. UI remains frozen; learner storage and canonical/assessment identities are protected.

## Current release — v2.95.73

- **Sole development baseline:** GitHub `vuphuc1996/Toeic` `candidate` commit `d068526864ccaf1ef4e3f3fca33466239890b387` (v2.95.72, 1,181 canonical headwords). This batch is based on that candidate head, not an alternate workspace or older source.
- **Batch 027:** added 10 reciprocal Word Family links on existing canonical entries and removed 2 self-referential links (`hire → hire`, `utilization → utilization`). No headword or canonical ID was added, deleted, or renamed.
- **Graph result:** 1,181 headwords; 331 headwords with family links; 428 directed links; 0 target-POS mismatches; 0 non-reciprocal links; 0 self-references; 0 duplicate links/headwords; 0 malformed records. 50 missing canonical targets and 70 Vietnamese sense-anchor flags remain explicitly open for review.
- **Vocabulary inventory:** unchanged at 1,181 (40 additions from v2.95.72 preserved). Manifest current-release additions are empty because Batch 027 is a relation repair, not a vocabulary expansion.
- **Regression guard:** the Word Family audit now reports self-references explicitly. Batch 027 tests validate every reverse link against the canonical target POS and Vietnamese sense.
- **Boundaries:** no IPA/definition/topic changes, question or choice IDs, answer keys, Mock eligibility, learner IndexedDB schema/records, Robot Buddy behavior, UI layout, or hosting architecture changes.
- **Verification status:** GitHub Actions and Pages for this commit are pending. Do not label this release accepted until the current commit's workflow and deployment complete. Physical-device and installed-PWA offline acceptance remain separate gates.
- **Reports:** `docs/reports/WORD_FAMILY_BATCH_027_v2.95.73.md`, `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.73.md`, and the generated release-keyed graph audit.
- **Source boundary:** candidate-only development. Do not update `main` as part of this batch.

## Previous release — v2.95.72

- **Vocabulary Batch 026:** added 40 canonical TOEIC headwords, increasing the inventory from 1,141 to 1,181. The original 1,141 IDs/headwords were preserved.
- **Related Glossary Batch 046:** remediated 65 existing glossary rows while retaining all 567 glossary identities, Vietnamese meanings and relation arrays.
- **Pre-repair Word Family audit:** 322 headwords with family links; 420 directed links; 50 missing targets; 1 target-POS mismatch; 72 Vietnamese sense-anchor flags; 10 non-reciprocal links.
- **Provisional progress index:** 55.88%, calculated from the v2.95.72 published workstream model. It is not overall production completion, learner mastery, official ETS alignment, or readiness certification.
- **Baseline candidate commit:** `3dff60cd9da392bc7085a3f016a8e1ad3250edbd`. Later candidate-only CI and preview-server commits are documented in Git history.
- **Acceptance:** this source is separate from production `main`; promotion requires independent QA and explicit release approval.

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
