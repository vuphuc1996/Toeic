# TOEIC Dictionary — Master Status

> Single source for current product state, decisions, release gates and active backlog. Chronological details belong in `CHANGELOG.md`; retired documents are indexed in `archive/PROJECT_HISTORY.md`.

## 1. Current release

- **Phiên bản mã nguồn đang kiểm kê:** v2.95.15 — adds four Cambridge-sourced related-term glosses for the highest-frequency remaining synonym/antonym terms; no canonical headword or learner-data change.
- **Previous source:** v2.95.14 — ten Cambridge-sourced related-term glosses; v2.95.13 remains the prior sense-expansion release.
- **Product:** GitHub Pages static PWA, GitHub-only. No backend/GAS/iframe/Cloudflare runtime dependency.
- **Scope:** TOEIC Listening & Reading is the active exam-development track. Foundation Pre-A1/A1/A2 remains available. B1 is blueprint-only; TOEIC Speaking/Writing and IELTS are deferred.
- **This release changes:** adds ten sourced Vietnamese glosses to the existing related-term glossary, raising it from 373 to 383 entries. It retains the fixed maximum 10-card Flashcard, Robot Buddy streaming, data-patch safety, consent-based PWA updates and the GitHub-only/offline architecture. No canonical headword, relationship, learner storage or runtime API was changed.

### v2.95.14 candidate verification record

- Candidate baseline: v2.95.13 source and patch history bundle at commit `a04a4d97472cb856c2459aab19d2a18090204e40`; candidate version: v2.95.14.
- Vocabulary remains 1,141 canonical headwords; stable ID-set SHA-256 unchanged; 0 IDs added / 0 missing. Multi-sense headwords remain 49 with 105 linked examples. Related-term glossary rises from 373 to 383.
- Ten new entries are for terms already referenced by canonical synonym/antonym fields. Exact-term join: 372/804 referenced terms have glosses; 432 distinct terms remain unglossed. At occurrence level, 477/1,037 links remain unglossed. These metrics are not the same as the validator's informational `323/804` value.
- Focused Python regression: five modules / 43 cases passed (glossary batch 021: 6; related-term patcher: 11; vocabulary detail/examples: 19; CI coverage: 3; project progress: 4). JavaScript regression: 38/38 `.mjs` suites passed.
- Data validator: 1,141 records; ID additions 0 / missing 0; 0 errors / 0 warnings. Learning-content validator: 0 errors / 0 warnings. Repository integrity: 382 references/data files, 0 errors / 0 optional warnings. Version synchronization and the release-integrity test passed.
- The related-term patch was rollback-tested, dry-run tested and applied with absent-only preconditions; all ten additions are represented in `batch-021.json` and a dedicated CI test.
- This does not mean the entire 57-module Python inventory or remote GitHub Actions completed. Remote Pages, real browser/PWA/offline/two-tab behavior and device TTS remain unverified. All 21 owner-run acceptance rows remain **Chưa kiểm**.
- All ten new glosses remain provisional pending independent lexical review. No GitHub push or deployment was performed.
- Detailed evidence: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.14.md`, `reports/COMMAND_LOG_INDEX_v2.95.14.md` and `reports/VOCABULARY_GLOSSARY_EXPANSION_v2.95.14.md`.

### v2.95.15 candidate verification record

- Candidate baseline: v2.95.14 at parent commit `e269173`; candidate version: v2.95.15.
- Vocabulary remains 1,141 canonical headwords; stable ID-set SHA-256, headwords and topic arrays are unchanged. Related-term glossary rises from 383 to 387 entries.
- New entries: `aim` (n), `avoid` (v), `cause` (n/v), `conceal` (v). Each already exists in canonical synonym/antonym relationships at least three times. Exact-term join after the batch: 376/804 distinct references have glosses; 428 distinct terms / 465 occurrences remain unglossed.
- Patch: four `expect.absent=true` operations, exact base-file SHA-256 and Cambridge host/path checks. Dry-run and apply passed; rollback in a disposable workspace restored the exact baseline SHA-256 `57c97c32c8d681ebbbb0129e9b21dc0ba3d4c7f8e12731a9d0f54d6a42b83fbc`.
- Focused Python regression: 5 modules / 36 cases passed (batch 022: 9; batch 021: 7; related-term patcher: 11; CI coverage: 3; release rotation: 6). JavaScript regression: 38/38 `.mjs` suites passed. JavaScript syntax checks and Python `compileall` passed. Vocabulary validator: 1,141 records, 0 ID additions/missing, 0 errors / 0 legacy warnings; learning-content validator: 0 errors / 0 warnings; repository integrity: 384 references/data files, 0 errors / 0 optional warnings; version synchronization and vocabulary release integrity passed. All newly added glosses remain provisional pending independent lexical review.
- Full Python discovery is not claimed. Remote GitHub Actions/Pages, real browser/PWA/offline/two-tab behavior and physical-device TTS remain unverified. All 22 owner-run manual acceptance rows remain **Chưa kiểm**. No GitHub push or deployment was performed.
- Detailed evidence: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.15.md`, `reports/COMMAND_LOG_INDEX_v2.95.15.md` and `reports/VOCABULARY_GLOSSARY_EXPANSION_v2.95.15.md`.

### v2.95.11 inherited controls — historical release

- Patch audit output now labels every row as `dry-run`, `apply` or `rollback`; `.gitignore` excludes `logs/`. The patch-data suite has 20 cases.
- Added a CSS design-token governance specification, `tools/design-token-rules.json`, `tools/audit-design-tokens.py`, an identity-based baseline and a CI step. The current CSS scan reports 2,778 legacy warning identities and zero new violations. The baseline was tightened only by removing three update-banner entries fixed by token migration.
- The update banner now uses existing shared typography, color, spacing, radius and shadow tokens. CSS has not been mass-refactored.
- `calm-study-blue` is documented as a conditional development/audit default. The profile remains `proposed-default-awaiting-user-preferences`; owner approval is not recorded.
- `reports/MANUAL_ACCEPTANCE_CHECKLIST.md` at v2.95.11 contained 20 owner-run checks. All 20 were **Chưa kiểm**; no GitHub Actions/Pages, PWA install, offline, two-tab, iOS/Android TTS or physical display/photo check is marked confirmed.
- Robot Buddy progressive local replies and the fixed maximum 10-card Flashcard remain because they were explicitly requested by the owner. No vocabulary IDs, words, topics, questions, answer keys, learner records or IndexedDB schema were changed.
- All changes in this workspace are local commits only. No push, remote CI run or Pages deployment has been performed.

### v2.95.11 verification record

- Focused Python verification: 10 modules / 95 tests passed; JavaScript: 37/37 suites passed. These are targeted results, not a claim that the full Python inventory completed.
- Current local validators: vocabulary 1,141 records, ID additions 0 / missing 0, 0 errors / 0 warnings; learning content 0 errors / 0 warnings; repository integrity 367 references, 0 errors / 0 warnings; Part 1 photos 9/9 valid.
- Design-token audit: 2,778 legacy warning identities, 0 new violations, no `RULE-DRIFT`. The audit scanner reports 979 hex values / 1,508 uses, 128 font-size values / 921 declarations, 47 border-radius values, 70 box-shadow values, 114 `!important`, 24 distinct media breakpoint values and 34 keyframes. Its font-size declaration count and breakpoint count differ from Claude's independent scanner (918 and 25); see `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.11.md` for measurement notes.
- The aggregate Python discovery did not complete within this execution environment and is not counted as PASS. Claude's supplied 433-test result applied to v2.95.10, not this release.
- Every item in `reports/MANUAL_ACCEPTANCE_CHECKLIST.md` remains `Chưa kiểm` until performed by the owner. No GitHub Actions/Pages or device-level results are marked confirmed.
- Detailed commands, durations and exit codes: `reports/COMMAND_LOG_INDEX_v2.95.11.md`; independent rerun instructions are packaged in `TOEIC_v2.95.11_Test_Logs.zip`.

### v2.95.13 candidate verification record

- Candidate baseline: v2.95.12, Git commit `85be68a`; candidate source version: v2.95.13.
- Vocabulary: 1,141 canonical headwords; stable ID-set SHA-256 unchanged; 0 IDs added / 0 missing; validator 0 errors / 0 legacy warnings. Multi-sense headwords 39 → 49; linked examples 81 → 105; related-term glossary 369 → 373 (then 373 → 383 in v2.95.14).
- Learning-content validator: 0 errors / 0 warnings. Listening 121 units / 239 questions; Reading 65 resources / 263 questions; Grammar 50 lessons / 137 exercises; separate Part 5 practice 80 questions.
- Repository integrity: 380 references/data files, 0 errors / 0 optional warnings. Part 1 photos: 9/9 valid. Design-token audit: 2,778 pre-existing legacy warning identities, 0 new violations. Version synchronization: PASS.
- Focused Python verification: 17 modules / 175 test cases passed in 54 seconds combined across individual module runs. JavaScript regression: 38/38 `.mjs` suites exited 0. This is not a claim that the full Python test inventory or aggregate discovery completed; `test_validator.py` and the complete aggregate remain NOT RUN to completion.
- Patch replay: all three vocabulary patches and the related-term patch were dry-run/applied from a clean archive of baseline commit `85be68a`; 10 A–Z files and `related-terms.json` matched the candidate byte-for-byte. Replay validator: 1,141 records, 0 IDs added/missing, 0 errors/warnings.
- All 20 owner-run manual acceptance items remain **Chưa kiểm**. GitHub Actions/Pages, real browser layout, PWA/offline, two-tab update, iOS/Android TTS and independent lexical approval remain unverified.
- Detailed commands and logs: `reports/COMMAND_LOG_INDEX_v2.95.13.md`; candidate comparison: `reports/CHANGE_MANIFEST_v2.95.13.md`.

## 2. Current canonical inventory

| Area | Inventory | Boundary |
|---|---:|---|
| Vocabulary | 1,141 headwords / 26 letter files | 3,000 minimum target; lexical quality is a separate backlog |
| Related-term glossary | 387 sourced/legacy entries | Four additions in v2.95.15; independent lexical review is pending |
| Grammar | 50 lessons / 137 exercises | No approved total-size target |
| TOEIC Listening | 121 units / 239 questions | 102 eligible / 137 reserve-pending-independent-review |
| TOEIC Reading | 65 resources / 263 questions | Part 7 second-review gate remains |
| Separate Part 5 practice | 80 questions | Practice-only; independent review pending; not Mock eligible |
| Foundation pathway | 23 lessons: 10 Pre-A1/A1 + 13 A2 | Separate from TOEIC exam inventory and evidence |
| Foundation Reading | 23 core passages / 59 questions + 13 supplementary A2 / 39 questions | Supplementary A2 content remains independent-review pending |
| Foundation Listening | 23 core clips / 59 questions + 13 supplementary A2 / 39 questions | Supplementary A2 content remains independent-review pending; device TTS, not ETS audio |

Counts are canonical source inventory, not proof of learner completion, editorial approval, mastery, CEFR certification or Mock eligibility.

## 3. Runtime and data contracts

- Canonical vocabulary is `data/vocabulary/A.json`–`Z.json`; `data/manifest.json` declares release version and counts. `data/vocabulary/batch-*.json` is editorial provenance, not runtime data.
- Canonical TOEIC resources are the Listening, Reading, Grammar and separate Part 5 JSON libraries. Stable resource/question/choice IDs are immutable; content additions are additive.
- `objective-resource-map.json` currently links 339/339 resource records across 11 objectives. The separate learning-outcome registry defines 33 criteria; only 6/33 currently have an evidence-collection path. These figures measure different layers and must not be conflated. Do not mark the remaining 27 criteria instrumented without an explicit evidence mapping and regression coverage.
- Robot Buddy is head-only, local-first and library-driven. It may use its own onboarding/reminder preferences, the active app surface, the current word/question/lesson being viewed and idle time. Context-aware guidance uses only that current in-session item. When Learning Insights is enabled, the app passes an in-memory snapshot of already-loaded local progress to the pure read-only aggregator; Robot does not open IndexedDB/localStorage, mutate records or transmit learner data. The dashboard must not be duplicated by a second prose statistics report.
- TTS uses browser/device SpeechSynthesis, not authentic ETS/native recordings. Listening order is Part title → lead-in → audio/dialogue → questions → options; Part 2 audio itself is the question. Reading order is Part title → lead-in → passage/documents → questions → options. Guided Mock must not repeat a title/lead-in already spoken by its transition.
- TTS option cadence: Listening Parts 2–4 and Reading Parts 5–7 use 1,000 ms pauses around A/B/C/D labels and options; Listening Part 1 retains its distinct 1,500 ms label pause and 1,300 ms description gap. Actual audible timing/voice quality remains device-dependent.
- IndexedDB remains `toeic-vocabulary-phase1`, version 1, store `workspace`. Preserve existing localStorage keys and learner records; no reset, migration or cross-device sync is authorized by this release.
- Part 1 images are JPG-only with source attribution. Do not reintroduce SVG fallbacks or replace licensed/project-owned images with unrelated assets.

## 4. v2.95.10 — fixed Flashcard count, protected data operations and PWA update consent

- Flashcard now has one consistent maximum of 10 cards per session. The 5-card UI/runtime setting and the inconsistent post-Quiz branch are removed. All topics, mixed learning, continue/next batch and wrong-answer review share the same cap; fewer than 10 cards are shown only when fewer eligible items remain.
- `tools/baseline-ids.json` now protects all 1,141 canonical vocabulary IDs. It was updated only after validation reported 213 additions and zero missing IDs. Current validation reports 0 additions and 0 missing IDs; set hash is `adccbdb4c98872207d2bede7bdc530e1c079bbd8b3679e7e4f6288054c7e404b`.
- `tools/patch-data.py` rejects `/id`, `/word` and `/topics` (including descendants), requires exact patch-level `allowedPaths`, rejects a whole batch on any out-of-allowlist operation and writes an operation-level audit log. Existing patch operation content remains unchanged; the allowlists reflect the operations already present. If the final audit record fails after replacement, original file bytes are restored before returning an error. Dry-run/apply/rollback protections remain.
- Service Worker first install can activate immediately; later releases wait for explicit confirmation through the update banner and `SKIP_WAITING`. Failed required installs retain the old cache. Optional assets do not block installation; cleanup is restricted to the TOEIC cache namespace; 404 navigation does not replace the app shell.
- The update banner uses shared typography tokens. `design-profile.json` remains `proposed-default-awaiting-user-preferences`; no unapproved visual profile change or bulk CSS conversion was made.
- Automated evidence: 37/37 JavaScript suites; focused Python modules baseline IDs 13/13, patch-data 17/17, practice fallback 6/6, PWA readiness 3/3, CI coverage 3/3, design profile 6/6, sync-version 12/12 and release rotation 6/6 and repository integrity test 1/1; 67 focused Python cases in total. Vocabulary validator: 1,141 records, ID additions 0/missing 0, 0 errors/0 warnings. Learning-content validator: 0 errors/0 warnings. Repository integrity: 366 references/data files, 0 errors/0 optional warnings.
- `test_validator.py` did not complete within the available execution window; a broad Python module sweep was also interrupted. These are not counted as full PASS results. Remote Actions/Pages, browser visual behavior, two-tab update confirmation, actual offline operation and mobile TTS are not locally verifiable.
- No vocabulary A–Z record, headword, topic, stable ID, TOEIC question, answer key, learner record, IndexedDB schema or learner localStorage key was changed. No pending content was promoted to Mock eligibility.
- Full evidence and Claude's assessment of the supplied audit are in `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.10.md`, `reports/CLAUDE_AUDIT_ASSESSMENT_v2.95.10.md`, `reports/TOEIC_CONTENT_COVERAGE_v2.95.10.md`, `reports/TOEIC_LISTENING_READINESS_v2.95.10.md` and `reports/COMMAND_LOG_INDEX_v2.95.10.md`.

## 5. v2.95.9 — Robot Buddy progressive responses

- Current release is based on the full v2.95.8 source. It adds progressive response streaming (thinking dots, character/grapheme reveal, blinking caret and completion-time actions) and locally composed, varied replies.
- The engine composes feature help, FAQ, contextual help and clarification responses from local dialogue/FAQ content, rule-based intents, varied phrase groups and the current in-memory page/item context. Unknown prompts are clarified rather than answered by guesswork.
- This is a presentation and local-composition improvement, not live ChatGPT/LLM generation. No generative model, API, backend, WebSocket or external learner-data transfer was added.
- Reduced-motion preferences skip the typing animation. A new turn completes an outstanding partial response before appending the next turn.
- All v2.95.8 safeguards remain: five regression groups, opt-in local read-only Learning Insights, one dashboard, Placement consent/skip, idle safeguards, page shortcuts, vocabulary/question content, TTS cadence and IndexedDB v1.
- No learner records, storage keys, vocabulary, questions, answer keys, stable IDs or Mock eligibility were changed.
- Verification: 35/35 JavaScript regression suites PASS; all JS/Service Worker syntax checks, Python compileall, version sync, repository-integrity audit, vocabulary validation and learning-content validation PASS. Focused Python checks: CI coverage 3/3, repository integrity 1/1 and responsive layout 7/7 PASS.
- Python module sweep completed individually for 53/54 modules; `test_validator.py` exceeded its 300-second limit after 23/38 cases reported `ok`; two related cases passed independently. The full validator module is not claimed as PASS. Remote CI and browser/device acceptance remain open.
- New artifacts: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.9.md`, `reports/USER_ACCEPTANCE_TEST_v2.95.9.md`, `reports/ROBOT_BUDDY_v2.95.9.md` and `reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.9.md`.

## 6. v2.95.8 merged release decisions and verification


- Retains the complete five-defect regression set from v2.95.5: Robot Buddy page-only shortcut navigation; `editorial_review` validation and CI registration; Listening/Reading narration handoff; exact TTS option cadence; and one-dashboard/no-duplicate-prose behavior.
- Preserves Robot Buddy Learning Insights as opt-in, local and read-only. The app passes an in-memory snapshot of already-loaded local records; the aggregator does not open IndexedDB/localStorage, write data or transmit learner information. The dashboard and its navigation shortcuts remain available.
- Does not carry forward v2.95.7's removal of the progress dashboard/toggle/insight aggregator because that would remove a user-approved learning-support feature. v2.95.7's static library, onboarding/Placement consent, reminder controls and lightweight interaction/idle safeguards remain.
- Retains the v2.95.7 documentation consolidation and safe release-rotation utility/test. The rotation tool defaults to dry-run and protects Markdown referenced by active tests, tools and current docs.
- Excludes all generated `__pycache__`, `.pyc` and `.pyo` files from the release package. Compatibility tombstones `learning-assistant.js` and `quick-help.js` are retained intentionally: they overwrite stale paths in repository overlays and are not active runtime implementations.
- The three outstanding groups from the v2.94.2 baseline are covered by v2.95.5's `editorial_review`, Listening/Reading sequence and TTS cadence fixes. v2.95.8 reruns their tests and the complete local release checks; results are recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.8.md`.
- Remote GitHub Actions, deployed Pages cache, and actual acoustic/device behavior are not inferred from local tests.
- Current artifacts: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.8.md`, `reports/USER_ACCEPTANCE_TEST_v2.95.8.md`, `reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.8.md`, and `reports/RELEASE_COMPARISON_v2.95.5_vs_v2.95.7_v2.95.8.md`.

## 7. v2.95.6 baseline audit results

- **JavaScript regression:** 34/34 `.mjs` suites PASS.
- **Python regression:** 54/54 `test_*.py` modules PASS individually; 426 test cases total. Running all modules in one aggregate discovery exceeded the execution window, so the result is based on each module completing independently.
- **Syntax:** all 17 `assets/js/*.js` modules and `sw.js` pass `node --check`; all Python tools/tests pass `py_compile`.
- **Repository integrity:** 363 local references/data files inspected; 0 errors; 0 optional warnings. All 293 static HTML IDs are unique.
- **Data:** 1,141 vocabulary records; 213 IDs added relative to the 928-ID legacy baseline; 0 removed. Vocabulary validator: 0 errors / 0 new warnings against the retained legacy baseline. Learning-content validator: 0 errors / 0 warnings.
- **Cross-links:** 339/339 objective-resource links; question-evidence audit indexes 502 TOEIC questions; distractor structural audit PASS across 240 in-scope questions; Foundation A2 audit PASS; Part 1 photos 9/9.
- **Design/PWA:** design profile 54 tokens / 406 legacy font-floor selector groups synchronized; Service Worker required resources exist and are represented in the app shell; version synchronization PASS.
- **Editorial information, not structural failures:** 93 vocabulary entries lack US IPA; 338/809 synonym/antonym terms lack explicit glosses; four English definition pairs are identical across related headwords; one word-level/sense-level CEFR difference is reported for `package` (word-level B1; senses A2/B1). These remain editorial review items; they were not silently rewritten.
- **Known instrumentation gap:** 27 of 33 learning-outcome criteria are defined but not instrumented. Existing objective-resource links and TOEIC practice evidence are not equivalent to full outcome-level evidence.
- **External gates:** remote GitHub Actions, GitHub Pages deployment/cache update, iOS/Android/desktop visual QA, offline/reconnect and physical audio output have not been verified in this workspace.

Detailed evidence: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.6.md`, `reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.6.md`, `reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.6.md`, `reports/TOEIC_DISTRACTOR_AUDIT_v2.95.6.md`, `reports/FOUNDATION_A2_ASSESSMENT_QUALITY_v2.95.6.md` and `reports/TOEIC_LISTENING_READINESS_v2.95.6.md`.

## 8. Active backlog

### P0 — acceptance and integration

1. Reconcile Claude's pending review of v2.95.13 against baseline v2.95.12 (`85be68a`); preserve findings and apply any required correction to the current v2.95.15 candidate without losing the v2.95.14–v2.95.15 work.
2. Review the v2.95.14 → v2.95.15 glossary-only delta and approve the candidate before any deployment; then verify remote Actions and Pages show the same version.
3. Complete all 22 rows in `reports/MANUAL_ACCEPTANCE_CHECKLIST.md` on Windows first, then iPhone/iPad and Android where available. Every item remains Chưa kiểm until the owner records date/device and result.
4. Instrument the remaining 27 learning-outcome criteria only after each criterion has a defensible evidence source, stable scope, threshold policy and tests. Do not infer mastery from inventory or resource links.

### P1 — content quality and coverage

1. Grow vocabulary toward 3,000 minimum; review 93 missing US IPA entries and improve word-family, verb-form, collocation, synonym and antonym coverage with source support. Current exact-term audit: 428 distinct terms remain unglossed across 465 link occurrences (804 distinct referenced terms / 1,037 total occurrences); this differs from the validator's `321/804` informational metric and should not be compared as if the definitions were identical.
2. Editorially review the four repeated definition pairs and the `package` word/sense CEFR difference; preserve legitimate sense distinctions.
3. Complete independent review for 137 TOEIC Listening reserve questions, Part 7 second-review items, 80 separate Part 5 practice questions and supplementary Foundation A2 Reading/Listening content before changing eligibility. Active handoffs: `reports/TOEIC_BATCH_024_REVIEW_CHECKLIST_v2.92.0.md` and `reports/TOEIC_BATCH_025_REVIEW_CHECKLIST_v2.93.0.md`.
4. Continue review of grammar examples and distractor uniqueness; structural audits do not replace semantic review by a second person.

### P2 — deferred

- B1 remains blueprint-only until TOEIC L/R is complete and accepted.
- Do not start TOEIC Speaking/Writing or IELTS until the user approves the phase transition.

## 8. Documentation and cleanup policy

- `MASTER_STATUS.md`: current state and active backlog only.
- `CHANGELOG.md`: chronological release history.
- `COMPATIBILITY.md`: current runtime/storage/offline contracts and retirement decisions.
- `archive/PROJECT_HISTORY.md`: compact index of retired documentation.
- Keep only current and immediately previous release-specific reports in `docs/reports`; `tools/rotate-release-files.py` must preserve older review handoffs still referenced by active tests/tools/current docs.
- Retain canonical data, stable IDs, assets, patch payloads and vocabulary batch provenance. Do not label them dead code merely because they are not imported by the runtime.
- The inert `learning-assistant.js` and `quick-help.js` files are intentional compatibility tombstones for overlay updates; the current app does not import them. Do not reactivate them as parallel modules.
