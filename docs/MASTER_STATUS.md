# TOEIC Dictionary — Master Status

> Single source for current product state, decisions, release gates and active backlog. Chronological details belong in `CHANGELOG.md`; retired documents are indexed in `archive/PROJECT_HISTORY.md`.

## 1. Current release

- **Phiên bản mã nguồn đang kiểm kê:** v2.95.11 — fixed 10-card Flashcard sessions, protected 1,141 vocabulary IDs, guarded patch operations and consent-based PWA updates; v2.95.9 Robot Buddy baseline retained.
- **Previous source:** v2.95.9 — Robot Buddy progressive response streaming and context-aware local response composition.
- **Product:** GitHub Pages static PWA, GitHub-only. No backend/GAS/iframe/Cloudflare runtime dependency.
- **Scope:** TOEIC Listening & Reading is the active exam-development track. Foundation Pre-A1/A1/A2 remains available. B1 is blueprint-only; TOEIC Speaking/Writing and IELTS are deferred.
- **This release changes:** retains the complete v2.95.9 functional baseline, removes the inconsistent 5-card Flashcard option in favor of a fixed maximum of 10, protects all 1,141 vocabulary IDs, enforces patch path allowlists/audit logs, and requires user consent for Service Worker updates. No generative AI or remote learner-data transfer was added.

### v2.95.11 local working changes — not yet deployed

- Patch audit output now labels every row as `dry-run`, `apply` or `rollback`; `.gitignore` excludes `logs/`. The patch-data suite has 20 cases.
- Added a CSS design-token governance specification, `tools/design-token-rules.json`, `tools/audit-design-tokens.py`, an identity-based baseline and a CI step. The current CSS scan reports 2,778 legacy warning identities and zero new violations. The baseline was tightened only by removing three update-banner entries fixed by token migration.
- The update banner now uses existing shared typography, color, spacing, radius and shadow tokens. CSS has not been mass-refactored.
- `calm-study-blue` is documented as a conditional development/audit default. The profile remains `proposed-default-awaiting-user-preferences`; owner approval is not recorded.
- `reports/MANUAL_ACCEPTANCE_CHECKLIST.md` contains 14 owner-run checks. All 14 are **Chưa kiểm**; no GitHub Actions/Pages, PWA install, offline, two-tab, iOS/Android TTS or physical display/photo check is marked confirmed.
- Robot Buddy progressive local replies and the fixed maximum 10-card Flashcard remain because they were explicitly requested by the owner. No vocabulary IDs, words, topics, questions, answer keys, learner records or IndexedDB schema were changed.
- All changes in this workspace are local commits only. No push, remote CI run or Pages deployment has been performed.

### v2.95.11 verification record

- Focused Python verification: 10 modules / 95 tests passed; JavaScript: 37/37 suites passed. These are targeted results, not a claim that the full Python inventory completed.
- Current local validators: vocabulary 1,141 records, ID additions 0 / missing 0, 0 errors / 0 warnings; learning content 0 errors / 0 warnings; repository integrity 367 references, 0 errors / 0 warnings; Part 1 photos 9/9 valid.
- Design-token audit: 2,778 legacy warning identities, 0 new violations, no `RULE-DRIFT`. The audit scanner reports 979 hex values / 1,508 uses, 128 font-size values / 921 declarations, 47 border-radius values, 70 box-shadow values, 114 `!important`, 24 distinct media breakpoint values and 34 keyframes. Its font-size declaration count and breakpoint count differ from Claude's independent scanner (918 and 25); see `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.11.md` for measurement notes.
- The aggregate Python discovery did not complete within this execution environment and is not counted as PASS. Claude's supplied 433-test result applied to v2.95.10, not this release.
- Every item in `reports/MANUAL_ACCEPTANCE_CHECKLIST.md` remains `Chưa kiểm` until performed by the owner. No GitHub Actions/Pages or device-level results are marked confirmed.
- Detailed commands, durations and exit codes: `reports/COMMAND_LOG_INDEX_v2.95.11.md`; independent rerun instructions are packaged in `TOEIC_v2.95.11_Test_Logs.zip`.

## 2. Current canonical inventory

| Area | Inventory | Boundary |
|---|---:|---|
| Vocabulary | 1,141 headwords / 26 letter files | 3,000 minimum target; lexical quality is a separate backlog |
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

1. Deploy v2.95.11 to the intended GitHub branch; verify remote Actions and Pages show the same version.
2. Complete all 14 rows in `reports/MANUAL_ACCEPTANCE_CHECKLIST.md` on Windows first, then iPhone/iPad and Android where available. Every item remains Chưa kiểm until the owner records date/device and result.
3. Instrument the remaining 27 learning-outcome criteria only after each criterion has a defensible evidence source, stable scope, threshold policy and tests. Do not infer mastery from inventory or resource links.

### P1 — content quality and coverage

1. Grow vocabulary toward 3,000 minimum; review 93 missing US IPA entries and improve word-family, verb-form, collocation, synonym and antonym coverage with source support, including glosses for the 338 currently unglossed synonym/antonym terms.
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
