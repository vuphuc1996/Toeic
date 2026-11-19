## v2.95.10 — Flashcard fixed batch, vocabulary identity baseline, safe data patching and consent-based PWA updates

- Removed the inactive 5-word Flashcard option from the UI and runtime. Every Flashcard entry route (all topics, Học tổng hợp, continue/next batch and wrong-answer review) now uses one consistent maximum of 10 words; the wrong-answer flow prioritizes missed words and fills remaining slots with new words. This does not modify vocabulary records or learner progress.
- Expanded `tools/baseline-ids.json` from 928 to 1,141 canonical vocabulary IDs after confirming 213 additive IDs and zero missing IDs. The resulting baseline has 1,141 unique IDs; validation now reports `ID: thêm 0, mất 0`.
- Hardened `tools/patch-data.py`: `/id`, `/word` and `/topics` roots (including descendants) are immutable; every patch must declare exact `allowedPaths`; an out-of-allowlist operation rejects the entire batch; and each operation writes an audit record with timestamp, batch ID, ID, pointer, old/new values and result. If the final audit record cannot be written after data replacement, the tool restores every original file byte-for-byte before returning an error. Existing patch operation payloads were not changed; their path allowlists were added from the paths they already use.
- Changed the Service Worker lifecycle: first install can activate immediately, later updates wait for explicit user consent through the “Có bản mới – Tải lại” banner and `SKIP_WAITING` message. Failed installs preserve the old cache; optional asset failures do not block installation; cache cleanup remains TOEIC-prefix-scoped.
- The update banner now uses shared typography tokens; the design-profile typography-floor regression remains green without changing the proposed visual profile.
- Re-audited content: 1,141 vocabulary headwords; Listening 121 units / 239 questions (102 Mock-eligible, 137 pending independent review); Reading 65 resources / 263 questions; Grammar 50 lessons / 137 exercises; separate Part 5 practice 80 questions (practice-only, review pending). No pending item was promoted to Mock eligibility.
- Local verification: 37/37 JavaScript `.mjs` suites PASS. Focused Python modules: baseline IDs 13/13, patch data 17/17, practice fallback 6/6, PWA readiness 3/3, CI coverage 3/3, design profile 6/6, version sync 12/12 and release rotation 6/6 and repository integrity 1/1. These focused Python modules total 67 passing cases; the whole Python inventory is not claimed as complete. Vocabulary validator: 1,141 records, 0 errors/0 warnings, 0 missing IDs; learning-content validator: 0 errors/0 warnings; repository integrity: 366 references/data files, 0 errors/0 optional warnings.
- `test_validator.py` did not complete within the available execution window and is not claimed as PASS. A broad Python discovery run was also interrupted; only the individually completed modules above are counted. GitHub Actions, GitHub Pages, real-browser two-tab update behavior, PWA offline behavior and physical-device acceptance remain external gates.
- No vocabulary A–Z record, stable ID, headword, topic, question, answer key, learner record, IndexedDB schema, localStorage learner key, TTS cadence or Mock eligibility was modified. No backend, AI API or remote learner-data transfer was added.

## v2.95.9 — Robot Buddy progressive response streaming and context-aware local composition

- Replaced the 320 ms whole-message reveal in ordinary Robot Buddy chat with a progressive character/grapheme stream, a blinking response cursor, an initial thinking indicator and delayed action buttons that appear after the reply is complete.
- Added a safe stream-completion path: a new user turn finishes the previous partial response before appending the next turn; streamed text is rendered with `textContent`; reduced-motion preferences skip the character animation.
- Improved the local response engine: feature help, FAQ, contextual help, identity, encouragement and clarification replies are composed from varied openings, transitions, current-page/current-item details and next-step language. FAQ selection now scores phrase matches rather than accepting a weak first substring match.
- Unsupported questions now receive an honest, context-aware clarification prompt instead of repeating a rigid generic statement. The Buddy does not claim it can answer unrestricted questions.
- Updated the visible product disclosure: replies are composed locally from bundled support content, lightweight rules and in-memory app context; no generative model, external AI/API, backend or learner-data transmission is introduced.
- Added `robot-buddy-streaming.mjs` and registered it in CI. Existing Robot Buddy routing, Placement, Learning Insights, dashboard, privacy and idle safeguards remain in place.
- No learner data, vocabulary/question content, stable IDs, IndexedDB schema, localStorage keys, TTS timing or Mock eligibility changed. Remote Actions, deployed Pages, browser animation and physical-device acceptance remain external verification gates.

## v2.95.8 — Five-defect consolidation, Robot Buddy Learning Insights preservation and source cleanup

- Consolidated the five regression groups previously delivered across v2.95.1–v2.95.5: Buddy page-only routing; Part 7 editorial validation/CI guard; Guided Mock Listening lead-in handoff; exact A/B/C/D pause assertions; and single visual progress dashboard without duplicate prose.
- Reaffirmed the approved Robot Buddy behavior: retain opt-in, local read-only Learning Insights and dashboard. The app passes an in-memory snapshot to the pure aggregator; no direct storage access, writes, migrations or external transmission are added. The v2.95.7 privacy-only removal of this feature is intentionally not carried forward.
- Added context-aware Buddy guidance for the active page and current in-session word, Flashcard, practice question, Grammar lesson, Reading item, Listening item or Foundation lesson. Idle nudges use that current item first and only compute progress-derived reminders when no current item is open.
- Adopted v2.95.7's documentation consolidation policy and safe dry-run-first release rotation utility, while retaining the five-defect tests and learning-insight regressions.
- Removed generated Python bytecode/cache artifacts from the distributable source. Intentional compatibility tombstones remain documented and tested; they are not duplicate active modules.
- No vocabulary/question bank, answer key, stable ID, IndexedDB schema, localStorage learner key or learner record was reset or migrated.
- Local test and validation outcomes are recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.8.md`; remote CI, Pages deployment and physical-device acceptance remain separate gates.

## v2.95.5 — Robot Buddy duplicate progress output regression guard
- Added an executable DOM-level regression for both explicit progress analysis and natural-language insight requests.
- The test invokes the real dashboard renderer and both entry points, confirming each request creates exactly one visual dashboard, one set of three totals, and no second prose summary repeating the same progress.
- Registered the new JavaScript regression in GitHub Actions. No learner progress, Robot dialogue library, insight thresholds or dashboard calculations were changed.

## v2.95.4 — TTS A–D one-second cadence regression guard
- Hardened the Listening/Reading TTS regression to assert the exact 1,000 ms pauses before answer-option sets, after each spoken A/B/C/D label, and between an option and the next label across Listening Parts 2–4, Reading Parts 5–7 and Guided Mock playback.
- Kept the intentional Part 1 timing contract separate: 1,500 ms after each spoken label and 1,300 ms between descriptions.
- No TTS timing constants or runtime behavior needed changing; the existing one-second contract is now explicitly executable and protected against regression.

## v2.95.3 — Listening / Reading narration sequence correction
- Fixed the shared Listening player to honor `skipLeadIn` when Guided Mock has already spoken its Part transition and lead-in; Mock no longer repeats the Part heading/instruction before the conversation or talk.
- Expanded TTS sequence regression coverage for Reading Part 6 and the Guided Mock Listening handoff, while retaining Parts 1–4 and Reading Parts 5/7 checks.
- No question content, answer keys, voice settings, learner progress, IndexedDB schema or standalone practice sequence changed.

## v2.95.2 — Editorial review regression and CI guard
- Expanded Part 7 editorial unit coverage to reject blank/duplicate answer choices and invalid `answerIndex` types (including booleans and strings), in addition to existing structure and reviewed-scenario checks.
- Added a focused CI guard requiring exactly one dedicated `test_editorial_review.py` execution step and retained workflow path triggers for test/workflow changes.
- Scope is limited to editorial review tests and CI coverage; no learner content, answer keys, progress, IndexedDB, voice, Robot Buddy runtime or dashboard behavior changed.

## v2.95.1 — Robot Buddy page-only shortcut regression coverage

- Kept the existing page-only action implementation unchanged: the delegated Buddy click listener accepts `data-robot-page`, closes the Buddy panel, then navigates to the selected page.
- Strengthened `tools/tests/robot-buddy.mjs` to execute the actual delegated click-listener body and actual `handleRobotCommand()` handler with a page-only `data-robot-page` action. The regression now asserts the panel closes and the exact destination is opened; it no longer relies only on testing action generation or source text.
- Scope is limited to Robot Buddy page-only shortcut dispatch and its regression test. No changes to `editorial_review`, Listening/Reading narration, TTS pause timing, progress-dashboard wording, learning content, or learner storage.
- Release gate: Robot Buddy navigation regression, all registered JavaScript regression suites and repository-integrity preflight must pass locally. Remote GitHub Actions, Pages deployment and physical-device acceptance remain unverified until actually run.

## v2.95.0 — Review-mode recovery, flashcard confirmation layering and interaction regressions

- Fixed the Robot Buddy action delegation so buttons returned with a destination page are handled as well as command buttons. Page actions close the Buddy panel and navigate to the intended module; the progress-insight response continues to render one visual dashboard with its navigation actions inside the dashboard, without repeating a prose summary.
- Fixed Review question selection so built-in Part 5 items remain usable even when a learner has hidden a linked headword from their personal dictionary. The effective personal vocabulary is preferred, missing built-in Part 5 targets are resolved from the immutable release vocabulary, and unavailable selected modes retry through a smart/common practice mode instead of stopping with an empty-question error.
- Corrected the Part 5 recall route to pass an exact question ID only when it still exists in the current bank; stale recall IDs safely fall back to a valid question. The review header reflects the question mode actually opened.
- Fixed the Flashcard completion confirmation stacking context: the assessment-result modal now renders above the focused learning workspace, so the user can confirm a completed 5/10-word quiz without the prompt being obscured by the flashcard panel. Existing confirmation-before-progress-write behavior remains unchanged.
- Updated the Part 5 recall-queue regression to match the safe exact-ID/fallback contract, aligned Robot Buddy and TTS tests with the current UI/runtime behaviour, and added dedicated tests for Part 5 vocabulary resolution, all review-mode fallback routes and modal stacking. CI coverage verifies every Python test module and JavaScript regression suite is invoked by the workflow.
- Preserved vocabulary content, Mock eligibility boundaries, review/Flashcard evidence, existing learner data keys and IndexedDB v1. No learner progress is reset, migrated or uploaded. TOEIC L/R remains the active scope; B1 remains blueprint-only and Speaking/Writing and IELTS stay deferred.
- Local verification is recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.0.md`. Remote GitHub Actions, deployed GitHub Pages and device QA are only considered verified after the user pushes/deploys and reports the actual results.

## v2.94.0 — Voice reliability, Robot Buddy progress dashboard and repository-wide release preflight

- Fixed the `question_evidence` CI regression: stale 401-question assertions were replaced by source-derived inventory and reserve counts. The current audit indexes all 502 TOEIC questions (239 Listening / 263 Reading), and its six unit tests pass.
- Consolidated Text-to-Speech through one `speakText()` and one guarded `speakUtterance()` implementation. Removed duplicate legacy declarations that overrode the guarded path. Playback queues the first utterance synchronously in the tap/click call stack, checks the voice catalogue without a fixed startup delay, retries once with the system voice when a selected named voice fails, and reports start/end watchdog, permission, network and synthesis failures clearly. The retry path ignores stale callbacks from the failed utterance, does not cancel the new fallback queue, and safely handles a throwing voice catalogue or utterance constructor.
- Listening, Reading, Foundation and vocabulary playback use the same local browser SpeechSynthesis engine. Part 1 pacing and inter-speaker pauses are preserved. Regression coverage includes an empty or throwing voice catalogue, selected-voice failure/fallback, stale cancellation/end/error callbacks, a throwing utterance constructor, missing start/end events, cancellation and Reading playback. Actual speaker output still requires device-level acceptance.
- Prevented Robot Buddy input focus from triggering automatic mobile/tablet zoom by keeping the chat input at a minimum 16px font size and adding mobile-friendly tap targets. User pinch zoom remains available.
- Added a one-tap Robot Buddy progress-analysis action to the welcome message and intent flow. The local-only dashboard presents Cần học / Cần luyện / Cần ôn totals plus color-coded, accessible per-module study-coverage bars and evidence notes. Coverage is not course completion or ETS score readiness; no unsupported global percentage is shown.
- Completed bilingual example and sentence-analysis enrichment for 42 examples across the 17 newest Grammar lessons (batches 024 and 025). Earlier Grammar lessons remain on the progressive editorial backlog.
- Added a repository-integrity preflight to GitHub Actions. It checks Service Worker REQUIRED/APP_SHELL/OPTIONAL paths, HTML local references, CSS url() files, static JS imports and data URLs, workflow script/test references, Python test selection, Node suite registration and JSON validity. Current run: 361 local references/data items inspected, zero errors and zero optional warnings.
- Preserved original Batch 024/025 fingerprints as historical release hashes and added separate v2.94 current-source grammar-enrichment fingerprints. Updated the vocabulary identity regression to compare the baseline plus append-only batches 006–013 (1,141 unique canonical headwords), avoiding a stale hard-coded total.
- Corrected the obsolete TTS note claiming every play waits two seconds before audio. Automated test suites and audit tools remain developer/CI controls and are not learner-facing test content; no learner-facing test/debug module was added.
- Preserved IndexedDB v1, existing learner-progress keys and Mock review boundaries. No progress reset/overwrite, external data transfer, new server/API or change to TOEIC L/R-only roadmap scope. B1 remains blueprint-only; Speaking/Writing and IELTS remain deferred.
- Local verification: 33/33 JavaScript regression suites; impacted Python modules pass (question evidence 6/6, TTS readiness 14/14, Grammar example quality 4/4, responsive layout 7/7, Batch 024/025 + vocabulary identity 18/18, project progress 4/4, CI coverage 2/2, repository integrity 1/1); vocabulary and learning-content validators, objective links 339/339, distractor audit, Foundation A2 audit, Part 1 photos 9/9, design profile and repository preflight pass. Complete Python discovery, remote GitHub Actions, Pages deployment and physical-device QA are not claimed.

## v2.93.0 — TOEIC L&R coverage expansion and score-readiness evidence tracker

- Added 9 Grammar lessons / 27 exercises, 8 Listening units / 20 questions (2 Part 2, 3 Part 3, 3 Part 4), and 8 Reading Part 7 resources / 36 questions (4 single passages and 4 double passages).
- Added 4 source-linked vocabulary headwords; US IPA is populated only where a single CMUdict pronunciation is available.
- Added a local-only Full Mock trend tracker. It requires three completed 200-question Full Mocks before showing L/R averages and trend; it never converts raw accuracy into an ETS scaled score.
- Updated objective-resource mapping and added batch integrity/evidence tests. All new Listening and Reading items remain practice-only pending independent review and excluded from Mock eligibility.
- Preserved existing local progress keys and IndexedDB v1. B1 remains design-only; Speaking/Writing and IELTS are deferred.

## v2.92.0 — TOEIC content batch 024: Grammar, Listening and Reading expansion

- Added eight original Grammar lessons with 24 exercises covering business conditionals, reported speech, comparison structures, countability/quantifiers, gerund/infinitive patterns, passive voice, relative clauses and time/deadline prepositions. Lessons are tagged for TOEIC Parts 5/6 and use stable unique choice IDs.
- Added six TOEIC Listening units / 18 questions: three multi-speaker Part 3 conversations and three Part 4 announcements/talks. Each item includes transcript translation, Vietnamese answer rationale and exact transcript evidence. All remain reserve-pending-independent-review and are excluded from Mock eligibility.
- Added six TOEIC Reading Part 7 resources / 27 questions: three single passages (four questions each) and three double passages (five questions each) across HR, shipping, office administration, finance and quality assurance. Each includes Vietnamese translation, four-option questions and source-label/quote evidence. All remain reserve-pending-independent-review and are excluded from Mock eligibility.
- Added `tools/content-batch-024-v2.92.0.json` with SHA-256 fingerprints for all 20 new resources, batch regression tests, and CI registration. Existing baseline resources and question IDs remain unchanged.
- Added a 12-unit Foundation B1 curriculum blueprint defining four-skill outcomes and acceptance gates. B1 is not exposed as a completed or selectable pathway in this release.
- Updated inventory reporting: Grammar 41 lessons / 110 exercises; Listening 113 units / 219 questions; Reading 57 resources / 227 questions. No invented completion percentages are used where total targets are undefined.
- No learner progress reset, localStorage key change, IndexedDB v1 schema migration, vocabulary changes, Mock promotion, API/backend, or external learner-data transfer.
- Independent second-person review of new reserve content, learner validation, remote GitHub Actions, Pages deployment and physical-device QA remain pending.

## v2.91.0 — A2 extended Listening multi-turn and inference upgrade

- Reworked all 13 supplementary A2 Listening clips in place, preserving stable clip/question IDs and the existing `{lessonId}::listening2` progress scope. Each now has six alternating speaker turns and 75–100 spoken words, up from the earlier four-turn, shorter dialogue format.
- Rebuilt the 39 questions into a consistent progression: listening for detail, understanding purpose/context, and inferring the next action. Each question now carries an exact source-turn `evidenceText`; four choices remain unique and answer positions are balanced across the full Foundation Listening bank at A/B/C/D = 25/25/24/24.
- Updated the lesson panel to disclose the six-turn dialogue format. Expanded regression coverage and the A2 assessment audit to check turn count, script length, question-skill sequence, exact evidence snippets, hash registry and isolated progress scope.
- Added a project roadmap status report with defensible coverage figures and explicit review/deployment gates. It does not invent a single overall completion percentage because no approved total denominator or workstream weighting exists.
- Preserved the 23 core Foundation Listening clips / 59 questions, all existing learner progress scopes and localStorage keys, IndexedDB schema v1, 99 TOEIC Listening reserve questions and Mock eligibility. No new backend, API or data transfer.
- New supplementary material remains `pending-independent-review`, practice-only, device SpeechSynthesis (not authentic ETS audio), and excluded from official A2 outcome or Mock eligibility. Learner validation, independent editorial review, remote GitHub Actions, Pages and physical-device QA remain pending.

## v2.90.0 — Foundation A2 supplementary Listening expansion

- Added 13 supplementary A2 listening clips, one for each of the 13 A2 lessons, with 39 new questions. Formats include phone call, announcement, discussion, voicemail, workplace update, safety briefing, directions, invitation, process instructions, planning call, status call, notice and help-desk call. Each clip contains four alternating female/male TTS turns and 50–63 spoken words.
- Added a collapsed “Nghe hiểu mở rộng” panel to each A2 lesson. Playback uses the learner's configured on-device English voices and inter-speaker pause; transcript remains hidden until requested. The UI clearly identifies this as browser SpeechSynthesis, not authentic ETS audio.
- Supplementary attempts use the existing `toeic:foundation-listening-progress:v1` ledger under `{lessonId}::listening2`. Core Listening remains keyed by the original lesson ID. The two evidence streams, draft sets and completion results are separate; no new storage key or IndexedDB migration was introduced.
- Preserved all 23 core Foundation Listening clips, their 59 questions, the v2.75.0 A2 q1/q2 content baseline, and the 99 TOEIC Listening reserve items / Mock eligibility boundary. The Foundation Listening inventory is now 23 core clips / 59 questions plus 13 supplementary A2 clips / 39 questions.
- Added a SHA-256 registry for all 13 supplementary clips and regression coverage for content structure, question IDs, answer keys, format diversity, runtime rendering, scoped evidence, CI registration and project-progress reporting. Listening answer positions are balanced across the full Foundation bank at A/B/C/D = 25/25/24/24.
- All supplementary content remains `pending-independent-review`. It is optional TTS practice only, not an official A2 outcome, CEFR certification, authentic recorded listening or TOEIC Mock content. Independent linguistic review and learner validation remain open.
- No existing lesson/question IDs, localStorage key names, IndexedDB v1 schema, learner progress, vocabulary data, TOEIC Mock pool, APIs or server contracts were changed.

## v2.89.0 — canonical design-profile CI repair & Foundation A2 extended Reading

- Fixed the CI failure in **Validate canonical design profile**. The source `assets/css/app.css` had acquired five fixed small-text selectors whose generated legacy typography-floor list in `assets/css/design-system.css` had not been regenerated. Ran `tools/sync-design-profile.py --apply`; the generated selector block now matches the canonical profile (54 tokens / 400 legacy font-floor selector groups). The exact `--check` command and all six `test_design_profile.py` tests pass locally. No validator was skipped or weakened.
- Added 13 longer A2 extended Reading passages, one per A2 Foundation lesson, with 39 new comprehension questions. Formats include workplace email, memo, comparison note, incident report, team update, notice, directions, invitation, procedure and staff information. Each passage is 90–110 words, has three questions, four unique options, a keyed answer, rationale and an exact `evidenceText` pointer.
- Extended Reading uses distinct IDs `::reading2` and the existing `toeic:foundation-reading-progress:v1` ledger under a scoped lesson ID (`{lessonId}::reading2`). Original 23 Foundation reading passages and their 59 questions remain unchanged; original A2 Reading q1/q2 baselines are still verified. New evidence is shown separately and is not folded into the official/core A2 outcome summary.
- Added a collapsed “Đọc hiểu mở rộng” area in each A2 lesson. Its open/closed state is preserved when a learner selects an answer and the lesson re-renders. The progress label and in-panel note clearly state that this is supplementary practice pending independent editorial review, not A2 certification.
- Corrected the 67% practice-threshold edge case in `foundation-reading-evidence.js`: status comparison now uses the same rounded percentage shown to learners. Thus 2/3 is represented consistently as 67% and meets a configured 67% threshold; unique-question minimums still apply.
- Registered `foundation-reading-extended.json` in Service Worker `REQUIRED` and `APP_SHELL`; added Python content/hash/ID/evidence/integration tests and JavaScript evidence-isolation/UI-state tests to CI. SHA-256 registry protects the complete passage objects.
- Preserved all old Reading IDs, original answer baselines, learner progress, local storage keys, IndexedDB v1 and Mock eligibility. No new API/server, no upload, no migration or reset. All 13 extended passages and 39 questions remain `pending-independent-editorial-review`; their presence does not certify A2 or authorize addition to the TOEIC Mock pool.
- Remote GitHub Actions/Pages and physical-device QA are not claimed as passing until the user pushes this source and verifies the remote run.

## v2.88.0 — Foundation A2 extended writing tasks and portfolio expansion

- Added 13 additional contextual A2 writing tasks, one for each of the 13 A2 lessons. The writing pathway now contains 26 distinct learner-authored production tasks: 13 original `::produce1` tasks and 13 extended `::produce2` tasks.
- Each extended task uses a separate stable ID and includes a workplace/daily-life scenario, 3–4 sentence-form instruction, three task requirements, a writing frame, minimum 20-word response, three task-specific self-review criteria, a model answer, three guided-revision checks and a topic-specific revision hint.
- Extended tasks are shown in a collapsed “Thử thách viết mở rộng” section so the existing lesson remains compact. Each task has independent response, self-rating and revision history in the existing `toeic:foundation-progress:v1` ledger.
- Updated the Foundation A2 writing portfolio, outcome evidence aggregation and Markdown export to recognize both original and extended task IDs. Export remains learner-triggered, local-only and read-only; each task and its revisions are listed independently.
- Added `tools/foundation-a2-extended-production-v2.88.0.json` with the 13 stable IDs, per-task SHA-256 fingerprints and editorial state. The original v2.78.0 and v2.87.0 scenario baselines remain unchanged.
- Updated the legacy revision regression to expect a 26-task A2 portfolio and test coexistence of original and extended tasks. The new content, registry hashes, minimum-word gate, export, aggregation, syntax, CI coverage and preservation rules are covered by tests.
- New extended prompts are explicitly marked `pending-independent-editorial-review`. The A2 pathway is not complete or CEFR-certified: varied Reading/Listening tasks, independent linguistic review and real-learner validation remain open.
- No IndexedDB schema/store/version migration, localStorage key change, existing task ID replacement, progress reset/overwrite, automated grammar grading, external transfer, vocabulary corpus change, TOEIC question-bank change or Listening reserve approval change.

## v2.87.0 — Foundation A2 writing portfolio export & task-direction quality repair

- Added a learner-initiated Markdown export to the local A2 writing portfolio. The export contains only saved A2 task context, learner-authored initial responses and revisions, task-specific self-ratings/revision checks, and the authored model answer for reference. It is generated entirely on-device and is not sent to any server or third party.
- The export preserves revision order, timestamps, word counts, self-assessment labels and the response used as the revision source. Embedded Markdown code fences in learner text are handled without breaking the exported document. The export builder is a pure function and does not mutate the progress ledger.
- Corrected the scenario direction in `a2-polite-requests`: the learner now needs the colleague to send the meeting notes, matching the task instruction, requirements, sentence frame and model answer. The task ID, legacy application task, question bank, learner progress and answer logic are unchanged. The v2.78.0 baseline remains intact; a v2.87.0 fingerprint refresh records the exact one-field change.
- Added a dedicated export regression suite and registered it in GitHub Actions. Strengthened A2 production-task checks for task requirements, rubric/checklist completeness, required model-answer features, minimum response length and the scenario/instruction alignment.
- No IndexedDB/localStorage schema or key changes, no progress migration/reset, no automatic grammar scoring, no TOEIC or CEFR mastery claim, no vocabulary/question-bank change, and no change to the Listening reserve-to-Mock approval boundary.
- Local verification: 31/31 JavaScript regression suites; 54/54 focused Python tests; CSS parse 0 errors; vocabulary validation 1,137 records / 0 errors / 0 warnings; learning-content validation 0 errors / 0 warnings; PWA readiness, CI coverage and version sync pass. Browser visual/device QA, remote GitHub Actions and Pages deployment are not claimed.

## v2.86.0 — Robot Buddy conversation layout isolation & persistent quick prompts

- Fixed the flex-layout regression where a growing conversation could compress the quick-prompt selection area. The message log now owns its own scroll region and may shrink within a bounded range; the quick-prompt menu, composer, typing indicator and privacy footer are non-shrinking siblings.
- Kept the quick-prompt menu visible and reusable throughout the current conversation instead of hiding it after the first sent message. The prompt area has its own maximum height and internal scroll so it cannot push the input or footer out of the panel.
- Reduced the privacy-note type from 7.5px to 6.5px and tightened its line-height/padding while preserving the offline, pre-authored-dialogue, local-only and no-external-transfer explanation.
- Added a dedicated Robot Buddy layout regression test and registered it in GitHub Actions coverage. Corrected an inherited malformed reduced-motion CSS rule for Listening cards so the preference is applied validly.
- Preserved the dialogue library, Learning Insights evidence thresholds, all learner content, stable IDs, IndexedDB v1, local progress keys and all existing onboarding/reminder settings. No new API, server or external transfer is introduced.
- Local source checks are documented in `reports/TEST_REPORT_TOEIC_Dictionary_v2.86.0.md`. Automated browser screenshots and physical-device validation could not be completed in this workspace; GitHub Actions and Pages deployment remain unverified.

## v2.85.0 — Robot Buddy polished layout & one-tap learning actions

- Rebuilt the Robot Buddy header as two clear rows: Robot name, TOEIC companion/offline status and close control remain together; the progress-analysis and reminder on/off controls sit below without pushing the title out of alignment.
- Enlarged the quick-prompt selection area and tap targets. Tightened the privacy footer while preserving the essential offline, local-only and non-generative-chatbot explanation.
- Robot replies now emphasize **Robot Buddy**, **TOEIC Dictionary** and **Vũ Nguyễn Hoàng Phúc** using safe DOM text nodes and `<strong>` elements; user messages and untrusted text remain plain text.
- Added up to four contextual navigation shortcuts after a progress analysis. Shortcuts are based only on categories and example areas actually returned by the local insight aggregator; they open existing app pages and do not alter learner records.
- Reminder and progress-analysis controls now present explicit Bật/Tắt states with accessible pressed state. Existing reminder preference semantics and `toeic:robot-buddy-settings:v1` are preserved.
- Preserved the offline dialogue library, all learning content, stable IDs, local storage keys, IndexedDB schema v1 and Service Worker shell. No learner progress is written, migrated, uploaded or reset.
- Local checks: Robot Buddy unit/regression suite, runtime render/migration smoke, JavaScript syntax and focused responsive/design/version checks are recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.85.0.md`. Browser visual QA, physical-device QA, GitHub Actions and Pages deployment remain pending.

## v2.84.1 — Robot Buddy Learning Insights & Knowledge Expansion

- Restored Robot Buddy learning-progress analysis using snapshots already loaded by the app from IndexedDB v1 and existing local progress stores. The Robot itself does not open IndexedDB or localStorage and receives only in-memory read-only snapshots.
- Added the three action buckets: **Cần học** (no completed evidence yet), **Cần luyện** (sufficient attempts with low/unstable accuracy), and **Cần ôn** (items whose existing review schedule is due). Sparse evidence is reported as insufficient rather than a weak-skill conclusion.
- Added a user-controlled progress-analysis toggle. Turning it off preserves normal dialogue, feature help and navigation.
- Updated “Bạn là ai?” with the developer introduction and a clear statement that Robot Buddy is scripted/offline, not a generative online chatbot. Learner progress is not sent to an API, server, Google AI or third party.
- Updated Robot's local privacy metadata, quick prompts and the in-app privacy explanation. Kept the 500 unique authored dialogue variants and the head-only SVG mascot.
- Registered `robot-learning-insights.js` in Service Worker `REQUIRED` and `APP_SHELL`; cache and release version moved to 2.84.1.
- Preserved IndexedDB schema version 1 and every existing learner-progress key. No progress migration, rewrite or deletion is performed by this release.
- Local test status is recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.84.1.md`. GitHub Actions, Pages deployment and physical-device checks remain pending until the user publishes and verifies the release.

## v2.84.0 — Head-only Robot Buddy & Offline Dialogue Library

- Replaced the former progress-aware Robot with a single head-only SVG mascot. Multiple expression states drive eye, pupil, eyebrow, mouth and antenna animations; reduced-motion preferences are respected.
- Added a bundled local content library with **500 unique messages** across greeting (60), encouragement (100), caring (60), learning (80), help (100), reaction (60) and rest (40), plus 55 feature-help messages for 11 app destinations, six FAQs and 12 quick prompts.
- Added offline keyword-intent recognition and feature navigation. Free-text replies are intentionally limited to authored topic groups; unknown questions receive a clear fallback rather than a false claim of open-ended AI understanding.
- Added quiet idle bubbles after 90 seconds, then 5- and 10-minute spacing, at most three notices per rolling hour, automatic dismissal, snooze and mute control. Idle prompts are suppressed during timed Mock Exams, active focus/modal dialogs, text entry, speech playback and hidden/unfocused tabs.
- First-run onboarding offers the existing Placement Diagnostic or skip. Robot stores only this choice and idle-mute preference in `toeic:robot-buddy-settings:v1`; a one-time migration reads only the v2.83 onboarding-choice key to avoid asking existing users again. It does not read the Placement result or any learner-progress store.
- Strict separation: no IndexedDB, vocabulary-progress, Flashcard, Grammar, Reading, Listening, Foundation, Mock score or personal vocabulary reads; no external API, Google AI or server; no persisted conversation transcript.
- Preserved the original v2.79 feature-level Google AI entry points outside Robot Buddy. Retired the v2.83 learner-progress assistant as a no-op compatibility tombstone.
- Added the runtime and dialogue JSON to Service Worker `REQUIRED` and `APP_SHELL`; cache version synchronized to v2.84.0.
- No vocabulary, question-bank, learning curriculum, TTS, Placement assessment logic, Mock engine, learner progress keys or IndexedDB v1 changes.
- Local validation and release status: see `reports/TEST_REPORT_TOEIC_Dictionary_v2.84.0.md`. Remote GitHub Actions, Pages deployment and physical-device QA remain unverified until tested after push.

## v2.83.0 — Robot Buddy, progress-aware support and Service Worker validation repair

- Replaced the helper launcher with an animated robot icon and a responsive Robot Buddy panel. The usage guide and Quick Help vocabulary prefix/masked-letter search are removed.
- A first-time visitor is asked whether to complete the existing Placement Diagnostic or skip. The local onboarding choice is remembered; returning learners are identified from existing local learning evidence.
- Robot Buddy uses the device's existing study records to congratulate, summarize vocabulary/review activity, identify Reading/Listening areas for additional practice only after at least three unique answered questions, surface Foundation recall due, summarize A2 writing history and open existing practice destinations.
- Milestone notifications are tied to completed learner actions (practice streak, Flashcard quiz, Placement, Mock Exam, A2 writing revision). No generic AI-generated claims or invented mastery percentages are used.
- `assets/js/learning-assistant.js` is a deterministic local read-only summary module; it does not call Google, an API, a model or a backend. Legacy v2.79 feature-level Google AI actions and their preview/explicit external handoff remain unchanged and separate.
- `assets/js/quick-help.js` is a no-op compatibility tombstone. Both it and `learning-assistant.js` are listed in Service Worker `REQUIRED` and `APP_SHELL`, resolving SW002 for the two asset paths while safely overwriting stale files in older GitHub checkouts.
- Added only `toeic:robot-companion-onboarding:v1`; no IndexedDB migration, vocabulary/question changes, old progress reset or A2 portfolio schema changes.
- Preserved the accepted v2.80 Mock Exam icons (clipboard/check, bolt, stopwatch, trophy). Updated Master and archive documentation to keep one authoritative AI product contract and remove inaccurate feature claims.

## v2.82.1 — Quick Help cleanup

- Removed Quick Help prefix search, suggestions and masked-letter completion.
- Preserved the original v2.79 feature-level Google AI controls, A2 writing portfolio and Mock Exam SVG icons.

## v2.82.0 — restore existing feature-level actions

- Restored the original v2.79 feature-level Google AI controls after a temporary implementation regression in v2.81.0.
- No new shared assistant, contextual AI prompt or copy/transfer integration was introduced.
- Preserved the A2 writing portfolio, response revision history and Mock Exam SVG icons.

## v2.81.0 — A2 writing portfolio

- Added the local A2 writing portfolio and first-to-latest self-rating view using the existing Foundation progress store.
- A temporary regression hid some existing Google AI controls; the original v2.79 behavior was restored in v2.82.0.

## v2.80.0 — Mock Exam icon refresh

- Replaced the old clock glyph with the accepted Mock Exam SVG icon family: clipboard/check, bolt, stopwatch and trophy.
- The only Google AI functionality in the product remains the original feature-level controls from v2.79; no shared assistant/contextual AI handoff is part of the accepted product scope.

## v2.79.0 — A2 guided writing revision and response history

- Added a task-specific guided revision workspace to all 13 A2 contextual production tasks. Each lesson has three review checks and a tailored revision hint; learners compare the prior response, confirm each requirement was reviewed, write a distinct revision and self-rate the existing three criteria.
- New production attempts retain their response text. Each guided revision stores `basedOnResponse`, revised `response`, three review confirmations, three learner self-ratings, word count and timestamp. A revision must meet the eight-word minimum, differ from the prior text and include all required review and self-rating fields.
- First responses and successive versions remain in the existing `productionEvidence` map and `toeic:foundation-progress:v1` localStorage key. Existing `::produce1` and legacy `::apply1` IDs remain unchanged and isolated.
- Historical v2.78.0 attempt rows did not store response text. They are preserved as-is; no missing historical response is fabricated. The last currently stored response is used as the starting point for the next revision.
- Added an immutable SHA-256 baseline for all 13 revision guides and regression tests for task-specific guidance, first-response capture, multiple revisions, response-chain linkage, validation gates and legacy-data isolation.
- No automatic AI/grammar grading, server upload, new dependency, IndexedDB migration, learner-progress reset, vocabulary change or Reading/Listening bank change. Revision ratings are learner self-reports, not a proficiency or mastery certificate.
- Local test and validator results are recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.79.0.md`. Remote GitHub Actions, GitHub Pages deployment and physical-device QA remain unverified.

## v2.78.0 — A2 contextual writing tasks and separate production evidence

- Added 13 original, lesson-specific learner-authored writing tasks across the 13 guided A2 lessons. Every task includes a workplace scenario, instruction, three content requirements, a sentence frame, three tailored self-check criteria and one collapsed model-answer example.
- Set an eight-word minimum for A2 contextual production responses and added a live word counter. Pre-A1/A1 production retains its existing three-word minimum and generic self-report rubric.
- Added the `productionTask` resource contract and new stable task IDs (`<lesson-id>::produce1`). These use the existing `productionEvidence` map inside `toeic:foundation-progress:v1`; no new localStorage key or server endpoint is introduced.
- Preserved the earlier A2 production records under their old `applicationTask` IDs (`::apply1`). They are not deleted or overwritten, but are no longer counted as completion of the new contextual writing task; the UI explains this distinction. The current A2 production outcome now reads only the dedicated `::produce1` records.
- Added an immutable SHA-256 content baseline for all 13 A2 production tasks and regression coverage for task structure, min-word validation, customized rubrics, collapsed model answers, evidence isolation and preservation of legacy records.
- No IndexedDB database/store/version migration, no Foundation localStorage key change, no vocabulary or Reading/Listening question change, no learner profile reset, and no TOEIC Mock-pool change.
- Local regression and validator counts are recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.78.0.md`. Remote GitHub Actions, Pages deployment, real-device QA and independent second-person linguistic review remain unverified.
- Production evidence remains learner self-report. The application does not automatically grade grammar or writing quality and does not certify CEFR level or mastery.

## v2.77.0 — A2 assessment quality and source-evidence pass

- Reviewed the 13 A2 Reading passages and 13 A2 Listening dialogues for repeated q2/q3 information. Reworked five question prompts/answer tasks across quantities, comparisons, visitor obligations and process sequencing so each resource tests distinct information.
- Added exact `evidenceText` source pointers to five reviewed questions. The new audit checks these strings against the actual passage or spoken segment, and verifies four unique choices, valid answer indices, non-empty prompts/rationales, distinct q2/q3 answer keys, stable IDs and full-bank answer-position balance.
- Kept all existing A2 q1/q2 question objects unchanged against the canonical v2.75.0 hash baseline; preserved existing lesson/resource/question IDs, progress stores, answer positions (A/B/C/D = 15/15/15/14), TTS behavior and 67% A2 practice threshold.
- Added `tools/audit-foundation-a2-assessment.py`, its focused review registry and eight Python regression tests; CI now runs both the tests and standalone audit.
- This is a focused internal single-author quality pass, not full semantic approval of all distractors, second-person language review, psychometric validation, CEFR certification or ETS equivalence. Remote CI, Pages deployment and physical-device QA remain unverified.

## v2.76.0 — A2 Reading & Listening depth expansion

- Expanded all 13 A2 Reading passages to 69–80 words and added one distinct third comprehension question per passage. The previous q1/q2 IDs, choices, answer keys and rationales are preserved byte-for-byte at the canonical question-object level; all 10 Pre-A1/A1 passages remain unchanged.
- Expanded all 13 A2 Listening scripts into four-turn dialogues (two female and two male speaker turns) and added a third comprehension question per dialogue. Playback uses the learner's saved/configured male and female device voices, retains the configured inter-speaker pause, exposes a Stop action and reports playback status. Legacy Pre-A1/A1 scripts without explicit speaker segments continue to play through sentence-splitting fallback.
- Foundation Reading and Listening now each contain 23 resources / 59 questions: 20 questions for the 10 Pre-A1/A1 resources and 39 questions for the 13 A2 resources. A2 requires 3 unique questions and uses a 67% local practice threshold; Pre-A1/A1 remains at 2 questions and 80%. These thresholds are not CEFR certification or mastery.
- Added an exact v2.75.0 question-pair baseline and regression checks proving all pre-existing A2 q1/q2 content and all Pre-A1/A1 records remain intact. Answer positions across each Foundation Reading/Listening bank are balanced A/B/C/D = 15/15/15/14.
- No vocabulary records, Foundation lesson/application IDs, learner progress key, IndexedDB v1 schema/store, personal vocabulary, settings or TOEIC L&R Mock pools were reset or migrated. No new dependency or audio asset was added; Listening audio remains device SpeechSynthesis, not ETS or recorded native-speaker audio.
- Local validation and exact test counts are recorded in `archive/PROJECT_HISTORY.md` (tài liệu release cũ đã được gom vào lịch sử). Remote GitHub Actions, Pages deployment, independent language review and physical-device audio/visual QA remain unverified.

## v2.75.0 — A2 core grammar expansion

- Added Present Perfect, basic Passive Voice and defining Relative Clauses as three A2 guided lessons; each includes teaching notes, bilingual examples, three recognition checks and a contextual-application task.
- Added three matching short Reading passages (6 questions) and three matching device-TTS Listening scripts (6 questions). Foundation totals: 23 lessons, 23 Reading passages/46 questions and 23 Listening scripts/46 questions.
- Expanded `foundation-a2` mapping to 13/13; objective-resource map now 294/294 across 11 objectives.
- Preserved all previous content IDs, answer keys, vocabulary, Foundation progress keys, IndexedDB v1 and existing learner data. Only new A2 records were added; comparison against v2.74.0 passed 52/52 prior-data preservation checks.
- Local validation: **131 selected Python tests across 19 modules and 22/22 JavaScript regression suites PASS**; vocabulary data 1,137 records / 0 errors / 0 warnings; learning-content 0 errors / 0 warnings; Part 1 photos 9/9; objective-resource links 294/294; outcome audit 11/11 objectives / 33 criteria; design-profile and version sync PASS.
- Local candidate only; independent A2 language review, remote CI, Pages deployment and physical-device QA remain pending. See `archive/PROJECT_HISTORY.md` (tài liệu release cũ đã được gom vào lịch sử).

## v2.74.0 — Foundation Outcome Instrumentation

- Instrumented Foundation recognition on stable per-question evidence without changing the unique-question denominator.
- Added 24-hour first recall scheduling and 1-day / 3-day retry intervals. Due recall is separate from recognition and cannot be recorded early.
- Added learner-authored sentence production with three explicit self-report checks; responses are stored locally and are not automatically graded.
- Added separate Pre-A1/A1 and A2 outcome dashboards. Foundation instrumentation coverage is 6/6; the complete outcome registry has 6/33 criteria with evidence paths (18.2%). No mastery or CEFR/ETS claim is made.
- Preserved the existing Foundation localStorage key and IndexedDB v1. No learner progress reset, schema migration, stable question ID change or vocabulary content change.
- Re-synchronized the canonical design profile and release markers.
- Validation: 22/22 JavaScript suites; 129 selected Python tests across 19 executed modules; all current structural, learning-content, strict Part 1 media, resource-map, outcome, design-profile and version checks pass. Remote CI/Pages/device QA remain unverified.

## v2.73.0 — A2 guided pathway starter expansion

- Extended the guided Foundation pathway from Pre-A1/A1 to a first A2 starter stage: 10 new A2 lessons with stable IDs, concise explanations, bilingual examples, three recognition checks and one separate contextual-application task per lesson.
- Added 10 A2 short-reading passages with two questions each and 10 A2 short-listening scripts with two questions each. Listening uses device SpeechSynthesis; it is not ETS audio or recorded native-speaker material. Reading/listening banks remain separate from TOEIC L&R Mock pools.
- Expanded the canonical objective-resource map to **11 objectives and 291/291 linked resource records**; the outcome registry now defines 33 criteria across 11 objectives. Foundation recognition/application progress remains separate from TOEIC objective evidence; production/retention outcomes are not yet instrumented.
- Added profile-safe, additive A2 IDs and preserved the prior Pre-A1/A1 lesson IDs, Reading/Listening IDs, answer keys, personal vocabulary, IndexedDB database/store/version and existing learner progress keys. No IndexedDB schema migration or data reset was introduced.
- Corrected an A2 suggestion example to the natural form “Why don't we meet after lunch?” and added a regression assertion for the accepted sentence and rationale. Balanced the A2 answer-key positions: recognition 8/8/7/7, contextual application 3/3/2/2, and Reading/Listening 5/5/5/5.
- Updated project progress reporting: 3/6 guided stages represented (**50.0%**), 291/291 objective-resource links and 33/33 outcome criteria defined. These are structural coverage measures, not full A2 completion, independent editorial approval or learner mastery.
- The 1,137-word vocabulary inventory and optimized 9/9 Part 1 4:3 JPEG assets remain unchanged. Part 1 strict validation continues to pass.
- Local verification: **306 Python tests passed across 42 fully executed modules**, **21/21 JavaScript regression suites**; vocabulary, learning-content, objective-resource and learning-outcome audits passed. The slow generic `test_validator.py` module was not counted because its full run did not finish within the execution window. Remote GitHub Actions, Pages deployment and physical-device QA remain unverified.
- The A2 content still requires independent linguistic/editorial review. The current A2 block is a starter stage, not the full A2 curriculum: present-perfect introduction, passive/relative clauses and wider four-skill assessment remain future work.

## v2.72.0 — embedded and optimized complete Listening Part 1 photo set

- Added all nine Part 1 JPG files directly to `assets/listening/` from the user-provided `Picture.zip`; no AI-generated or substitute images were created.
- Standardized every photo to **1448×1086 px (4:3 landscape)**, matching the shared design-system frame. `part1-photocopier.jpg` is now a landscape crop that keeps the employee's operating hand and the photocopier control panel in frame; no distortion is applied.
- Kept every image under **400,000 bytes**. The existing `part1-office-cleaning.jpg` remains byte-for-byte unchanged at 398,363 bytes. The other eight photos are optimized progressive JPEGs. Combined image payload is 2,063,272 bytes, down from 25,265,159 bytes (**91.8% smaller**).
- Extended strict Part 1 validation to enforce minimum 1280×960, 4:3 landscape ratio and the 400,000-byte ceiling. Strict validation now passes **9/9 photos**; Learning Content validation reports **0 errors / 0 warnings**.
- Removed the old `restore-part1-photos.bat` downloader shortcut and its helper/test from the current release. That utility previously downloaded full-resolution Pexels originals; it did not compress or attach photos. It is no longer needed because optimized images are embedded in this full-source archive.
- Question IDs, transcripts, answer choices, answer keys, explanations, image filenames and attribution/license records remain unchanged. Removed the per-image photocopier CSS focal override because the source asset is now prepared to the shared 4:3 frame.
- Local verification is recorded in `archive/PROJECT_HISTORY.md`. Remote GitHub Actions, Pages deployment and physical-device QA are not claimed unless separately confirmed.

## v2.71.0 — Contracts and Facilities vocabulary expansion; one-command original photo recovery

- Added Vocabulary Batch 012 with 37 original TOEIC headwords covering Contracts, Legal Procedures and Facilities Management. The canonical A–Z inventory increases from 1,100 to 1,137 stable headwords. Every new entry has an English definition, Vietnamese gloss, one bilingual context example, at least three collocations and a sense-level editorial CEFR estimate. Independent lexical/CEFR review remains pending; none is official ETS material.
- Added 35 conservative US IPA entries from exact single-pronunciation CMUdict matches. `ventilation` remains blank because CMUdict has multiple pronunciations. `dispute` is also withheld pending syllabification review instead of using a mechanically generated transcription with uncertain syllable division. Cumulative IPA ledger: 333 source-linked records; 93 vocabulary records remain without populated IPA (91 inherited unresolved records plus these two Batch 012 exceptions).
- Added five reciprocal word-family pairs: enforce/enforcement, janitor/janitorial, accessible/accessibility, occupy/occupant, and alter/alteration. Cumulative word-family records: 276; directed links: 374. No speculative synonyms or antonyms were added.
- Extended release-repair profiles so workspaces at 979, 992, 1,026, 1,063 and 1,100 base headwords can restore only the known cumulative release additions through Batch 012. Learner progress, personal vocabulary, study settings, question IDs, answer keys and IndexedDB stores remain untouched.
- Added `tools/restore_part1_photos.py` and `restore-part1-photos.bat`. They fetch all eight original licensed Pexels photos in one operation using the filenames and direct URLs already recorded in `assets/listening/ATTRIBUTION.csv`, validate JPEG signature/dimensions, and never generate substitute images or overwrite existing files. The current build environment still cannot access the Pexels CDN and the saved Library does not contain the eight original image bytes; therefore the eight JPGs are **not yet embedded** in this release archive. Strict photo validation remains blocked until the originals are available and restored.
- Vocabulary target coverage: 1,137/3,000 minimum = 37.9%; 1,137/5,000 planning ceiling = 22.7%. US IPA field coverage: 1,044/1,137 = 91.8%; word-family coverage: 276/1,137 = 24.3%. These are target/field coverage ratios, not a single overall product-completion percentage.
- Local verification is reported in `archive/PROJECT_HISTORY.md`. Remote GitHub Actions, Pages deployment and physical-device QA are not claimed unless separately confirmed.

## v2.70.0 — Customer Service and Travel vocabulary expansion; IPA coverage counter correction

- Added Vocabulary Batch 011 with 37 original TOEIC headwords across Customer Service and Travel, increasing the canonical dictionary from 1,063 to 1,100 entries. Each new record includes an English definition, Vietnamese gloss, a contextual bilingual example, at least three collocations, a sense-level editorial CEFR estimate, and one US IPA candidate sourced from a single exact-match CMUdict pronunciation.
- Added four reciprocal, POS/sense-checked word-family pairs: cancel/cancellation, resolve/resolution, responsive/responsiveness, and troubleshoot/troubleshooting. No speculative synonyms or antonyms were added.
- Cumulative CMUdict ledger now contains 298 source-linked entries. The original 91 unresolved IPA records from the v2.69 base remain blank; no IPA is guessed. Current US IPA population is 1,009/1,100 (91.7%).
- Vocabulary quantity coverage increases to 1,100/3,000 (36.7%) and 1,100/5,000 (22.0%). These are quantity ratios only, not quality, CEFR mastery, or an overall product-completion percentage.
- Fixed the validator's IPA missing counter so absent `phonetic` objects and missing/non-string `us` values count as missing. Added regression coverage for both forms.
- Extended migration-repair profiles to recognize the 1,063-word v2.69.0 snapshot and cumulatively restore the exact known release additions without changing unrelated local deletions or learner progress.
- No IndexedDB schema/store migration, learning-question IDs, answer keys, user progress, personal vocabulary, or study settings were reset. Independent lexical review remains pending; CMUdict-derived IPA is not independently pronunciation-certified.
- Strict Part 1 photo validation remains blocked by eight missing repository-owned original JPG binaries. Remote GitHub Actions, Pages deployment and physical-device QA are not claimed.

## v2.69.0 — US IPA coverage backfill and word-family quality pass

- Added **261 US IPA entries** for exact headword matches with a single CMUdict General American ARPABET pronunciation and a single primary stress. CMUdict provides ARPABET, not IPA; the project uses a documented, deterministic broad-GA conversion. The source warns that its entries may contain errors or inconsistencies, so these remain source-linked editorial candidates rather than independent pronunciation certification. Provenance, raw ARPABET, conversion rules and exclusions are recorded in `reports/CMUDICT_IPA_BACKFILL_v2.69.0.json`; the CMUdict data license is retained in `docs/licenses/CMUdict-DATA-LICENSE.txt`.
- Increased US IPA field coverage from 711/1,063 (66.9%) to **972/1,063 (91.4%)**, a gain of 261 records / 24.5 percentage points. The remaining 91 entries stay blank by design: 60 have multiple CMUdict pronunciations, 25 have no exact entry, and 6 have multiple primary-stress patterns. No IPA was guessed for excluded items.
- Expanded word-family metadata from 240 to **259 headwords** and from 338 to **357 directed links** (+19). Added reciprocal, POS/sense-aligned relationships; corrected the Vietnamese gloss for the `transaction → transact` link without changing IDs.
- Added deterministic `tools/cmudict_ipa.py`, an embedded source/provenance ledger, a license notice and five focused tests. CI now runs the IPA ledger check and test module. Progress reporting now includes word-family directed-link counts.
- Vocabulary remains **1,063/3,000 = 35.4%** of the minimum planning target and **1,063/5,000 = 21.3%** of the planning ceiling. This release improves metadata quality and does not add new headwords. Next planned content batch remains Customer Service, Travel, Contracts and Facilities after review of the 91 IPA exceptions.
- No vocabulary stable IDs, question IDs, answer keys, IndexedDB schema/stores, personal vocabulary, hidden-word state or learning progress were reset.
- **Local verification:** vocabulary validator 1,063 records / 0 errors / 0 warnings; CMUdict IPA ledger check PASS (261 source-linked records); focused CMUdict IPA tests 5/5; word-family-link tests 5/5; project-progress tests 4/4. Full test and asset status are recorded in `archive/PROJECT_HISTORY.md`.
- CMUdict is a source dictionary and may contain errors, omissions or inconsistencies; the conversion and single-pronunciation filter reduce ambiguity but do not constitute human independent lexical review. CEFR labels remain editorial estimates. Remote GitHub Actions, GitHub Pages and physical-device QA are not claimed. Strict Part 1 photo validation remains blocked by eight original JPG binaries absent from this source workspace.

## v2.68.0 — verified Part 1 fingerprint refresh and TOEIC Vocabulary Batch 010

- Fixed the remaining-content fingerprint CI failure by recording the approved removal of the legacy Part 1 SVG `image` metadata field. All eight historic unit hashes are reproducible by restoring the exact old SVG path; all question hashes remain unchanged. Added a second fingerprint refresh audit entry and fail-closed verification.
- Added 37 stable vocabulary headwords in Batch 010 for manufacturing, production operations, quality assurance/control, maintenance, warehouse operations and supply chain. Total rises 1,026 → **1,063** (+37; 35.4% of the 3,000 minimum target, 21.3% of the 5,000 planning ceiling).
- All 37 entries include definitions, Vietnamese glosses, original bilingual examples, at least three collocations and editorial US IPA. Added five reciprocal word-family pairs. CEFR is editorial-estimate; independent lexical review remains pending.
- Updated legacy hidden-word repair profiles: 979→84 known additions, 992→71, 1,026→37. Only exact matching historical snapshots can trigger a restore; no IndexedDB schema change or reset.
- Strict Part 1 photo validation remains blocked because this source snapshot contains only 1/9 original JPG binaries. Keep the eight repository-owned JPG originals when merging; deployment remains on hold until strict validation reaches 9/9.

## v2.67.0 — JPG-only Listening media and TOEIC Vocabulary Batch 009

- Removed the redundant public UI label “Nội dung bổ sung · đang chờ kiểm duyệt độc lập · chưa dùng trong Mock Exam”. The underlying `editorialStatus=reserve-pending-independent-review` metadata and fail-closed Mock exclusion remain intact; this is a presentation cleanup, not an approval or content-promotion change.
- Converted all nine Listening Part 1 records to a strict JPG-only contract: each unit uses `photo`, no unit declares the legacy `image` SVG fallback, runtime and Mock rendering no longer contain SVG fallback behavior, and the eight obsolete `assets/listening/part1-*.svg` files were removed from the source. Service Worker Part 1 entries are JPG-only; unrelated application/topic SVG icons remain untouched.
- Added Vocabulary Batch 009 with 34 stable headword IDs focused on finance, legal/compliance, procurement, HR and logistics. Canonical A–Z vocabulary grows from 992 to **1,026 headwords** (+34; 34.2% of the 3,000 lower-bound planning target). Each new entry includes an English definition, Vietnamese gloss, original TOEIC-context example and three collocations; all CEFR labels remain editorial estimates.
- Added 32 editorial US IPA transcriptions derived from CMUdict General American ARPABET where a stable single reading was selected; two entries remain blank pending dictionary-level confirmation. Added 11 reciprocal, POS/sense-matched word-family relationships to existing canonical headwords. No unsupported synonyms/antonyms or verb forms were invented.
- Added cumulative legacy migration repair profiles for devices whose old hidden-word snapshot was based on either 979 or 992 canonical headwords. The repair restores only the exact known additions for a matching historical fingerprint; unrelated user-hidden IDs and personal data remain untouched. No IndexedDB schema/store migration was added.
- Local validation: 117/117 selected Python tests and 21/21 JavaScript regression suites; vocabulary validator 1,026 records / 0 errors / 0 warnings; learning-content validator 0 errors / 8 warnings for missing original JPG bytes in this inherited workspace; focused JPG-only, PWA, learning-content, vocabulary family, example, progress and legacy-collocation suites passed. Strict photo validation remains blocked at 1/9 local JPG binaries; restore the eight repository-owned JPGs before deployment.
- Independent lexical review of Batch 009 remains pending. Automated checks and internal author review do not qualify as independent approval. Remote GitHub Actions, Pages deployment and real-device visual/audio QA are not claimed.

## v2.66.1 — fixed Listening Part 1 pacing and GitHub test correction

- Standardized every Speech Synthesis route on a fixed **2,000 ms** engine-preparation buffer after voice-catalog readiness and cleanup. The delay is no longer configurable, preventing different settings from making practice and exam audio behave differently.
- Listening Part 1 now speaks the topic header (`Part 1: [Topic]`, e.g. `Part 1: Warehouse & Shipping`), waits **1,000 ms**, speaks `Now, listen to the four statements.`, waits **1,000 ms**, then speaks each option label (`A.`, `B.`, `C.`, `D.`) as its own utterance. Each label is followed by a fixed **1,500 ms** pause before its description; descriptions are separated by **1,300 ms**.
- Practice and Mock Exam use the same Part 1 pipeline. The Mock Exam no longer speaks an extra generic transition before Part 1; the shared player owns the full topic → lead-in → A–D sequence. Parts 2–4 retain their existing segment/turn handling, with the new fixed 2-second startup readiness.
- The Practice transcript now includes the spoken topic header, lead-in and option labels. Mock audio guidance describes the same fixed timing. The timing controls were removed from Settings so users cannot accidentally create divergent schedules.
- Fixed the GitHub Actions failure in `test_distractor_quality.py`: an old assertion expected `recordPracticeAnswer()` to run immediately on selection. Since the v2.66.0 assessment contract intentionally stages choices and commits them only after the complete-set confirmation, the test now asserts `stagePracticeChoice()` on selection and `commitPracticeDraftSet()` after confirmation. No application scoring behavior was weakened or reverted.
- The long escaped `app.js` fragment in the Python traceback was the unittest representation of the source string in `AssertionError`, not escaped/corrupt JavaScript. The Google URL builder remains `new URL('https://www.google.com/search')`; Node syntax checks pass.
- Preserved Listening question text, answer keys, explanations, stable IDs, answer history, personal vocabulary, existing IndexedDB stores, voice selections, rate, pitch and volume. Legacy saved timing keys are ignored; no data reset or schema migration was added.
- Local verification: 21/21 JavaScript regression scripts PASS; 85/85 selected Python tests PASS across 10 modules; `test_tts_readiness.py` 13/13; `test_distractor_quality.py` 6/6; `test_ci_coverage.py` 2/2; version/design sync and syntax checks PASS; vocabulary validation 992 records / 0 errors / 0 warnings; learning-content validation 0 errors / 8 original JPG warnings. The strict Part 1 photo validator still fails because 8/9 original JPG binaries are present in the inherited source archive; keep the release hold.
- Real audible timing on Windows, iOS/iPadOS and Android, remote GitHub Actions, and GitHub Pages deployment remain unverified from this workspace.

## v2.66.0 — assessment summary-before-review and guided mock flow

- Balanced dashboard progress into full-width exam/skill rows; TOEIC Listening and Reading no longer compete in one uneven 4-Part/3-Part grid. The structure is extensible to Writing, Speaking and IELTS.
- Deferred correctness and explanations until a complete set is answered and the learner confirms the summary. Applied to Grammar, Reading, Listening, Foundation, Placement, Flash Quiz and single-question Smart Review/Part 5.
- Added a shared completion modal with correct/incorrect/total counts and a restrained bottom-up confetti animation. Existing answers, explanations and history are committed/opened only after confirmation.
- Mock Exam shows no correct/wrong feedback while in progress. Manual submission or timeout moves to a persisted pending summary; confirming opens the detailed answers, transcripts and explanations. Pending summaries survive reload and do not enter completed history until confirmed.
- Timed Mock Exam now reserves lead-in time within the overall 15/60/120-minute schedule and automatically advances focus across all Listening/Reading questions. A spoken transition identifies the current Part/question; Listening audio is replayed only when entering a new group, not on every sub-question in the same dialogue.
- Added `assessment-deferred-workflow.mjs`; updated mock guided-flow tests for section-local question numbering. Added `mock-flow.js` to the Service Worker required/app-shell cache.
- Preserved prior progress and IndexedDB schema. Validation is local only; physical device playback/visual rendering and remote GitHub Actions/Pages are not verified. Eight inherited Part 1 JPG binaries remain absent from this workspace, so strict media validation continues to block deployment.

## v2.65.2 — TOEIC Part 1 lead-in and spoken A–D option sequence

- Added a shared Part 1 lead-in: “Now, listen to the four statements.” The lead-in is spoken after voice preparation and before option A.
- Listening Part 1 options are now spoken as separate, explicitly labeled utterances: “A. [description]”, “B. [description]”, “C. [description]”, and “D. [description]”. Existing source descriptions stay clean and are labeled at playback time; already-prefixed source text is normalized to avoid duplicated labels.
- Added a configurable pause after the lead-in and before A (default 1,000 ms; 800–1,800 ms). The existing 1,300 ms default pause between A/B/C/D remains independently configurable.
- Practice Listening and Mock Exam use the same `playListeningAudio()` pipeline, so lead-in, spoken labels, voice selection, startup readiness and A–D pacing are identical in both modes. The Mock Exam audio hint and practice transcript now expose the same order and labels.
- Part 1 clips with anything other than four descriptions are blocked with a clear message rather than silently reading an incomplete A–D sequence.
- Added regression tests for the lead-in, spoken A–D labels, transition gaps, stop-during-lead-in, transcript labels, configuration persistence, the nine current Part 1 units, and shared Practice/Mock playback.
- Existing question text, answer keys, explanation text, stable IDs, personal vocabulary, IndexedDB stores, learner progress and existing TTS voice/rate/pitch/volume settings remain unchanged. `part1LeadInPauseMs` is additive to `appSettings.tts`.
- Local source verification only. Device-specific audio pronunciation and timing still require real browser/device listening. The inherited strict Part 1 photo validator remains blocked by eight missing original JPG binaries in this archive; do not remove existing GitHub image assets when applying this update.

# TOEIC Dictionary — Changelog

## v2.65.1 — TTS voice-selector startup hotfix

- Fixed the v2.65.0 initialization crash `ReferenceError: refreshSpeechVoiceSelectors is not defined`. The helper was still invoked by `bindTtsSettings()` and `syncSettingsUI()` but its function declaration had been dropped during the TTS readiness refactor.
- Restored the shared voice-selector refresh helper. It repopulates English voice choices when the device exposes its voice catalog, keeps the learner's manually saved male/female voice URI, preserves a saved URI that is unavailable on the current device with a clear option label, and disables selectors while no English voice is available.
- The `voiceschanged` listener and manual refresh button continue to use the same helper. TTS playback readiness, startup delay, Part 1 A–D pause, saved settings and learner progress are otherwise unchanged.
- Added a source-level regression assertion and expanded the JavaScript TTS regression to execute the helper with an empty catalog, a populated catalog, a saved voice, and an unavailable saved voice.
- Local hotfix verification: 10/10 TTS Python checks and the Listening/TTS JavaScript regression pass after the fix. Full syntax/runtime and data checks are recorded in `archive/PROJECT_HISTORY.md`.
- No vocabulary content, stable IDs, IndexedDB schema/stores, local progress keys, or TTS preferences were reset or migrated. Existing saved voice URIs remain preserved.
- Deployment remains on hold until the eight inherited original Part 1 JPG binaries are restored and the strict photo validator passes. Real-device audio QA and remote GitHub Actions/Pages remain unverified.

## v2.65.0 — speech engine readiness, protected audio starts and Reading read-aloud

- Centralized every browser Speech Synthesis path behind one readiness sequence: wait briefly for the device voice catalog, clear residual pending/speaking work after cancellation, then apply a configurable pre-play buffer before the first real utterance. This is intended to reduce clipped initial phonemes/words when a voice engine is cold or an utterance has just been canceled; browser/OS behavior still needs physical-device verification.
- Listening playback now prepares the voice catalog before the first segment. TOEIC Listening Part 1 has a dedicated configurable 1.3-second default gap between answer descriptions A–D; other conversation/short-talk content retains the configurable turn pause. Per-lesson playback rate and manual voice selection are preserved.
- Vocabulary slow playback, flashcards, alphabet sound lab, Foundation Listening and word-pronunciation buttons now inherit the same startup preparation and safe cancellation logic through `speakText` / the shared utterance queue.
- Added Reading read-aloud for passage/document content and Part 5 question-choice sets. It uses the same prepared voice path, status announcements and Stop action; no reading or learner-progress records are changed.
- Added settings for startup preparation delay (default 750 ms) and Part 1 A–D option gap (default 1,300 ms). Legacy `appSettings.tts` objects receive these defaults additively; existing voice, rate, pitch, volume and pause settings remain intact.
- Added regression coverage for initially empty voice catalogs, delay-before-first-speech, Part 1 A–D spacing, reading passage playback, status updates, and the single guarded `speechSynthesis.speak()` call. The new Python design/integration checks are included in CI.
- No vocabulary, listening/reading content, stable question IDs, IndexedDB stores/schema, learner history or personal progress are reset. Only two additive TTS preference fields are introduced.
- Local source verification only. Device TTS output and iOS/Android PWA behavior are not guaranteed by mocked tests. The inherited strict Part 1 asset validator remains blocked by eight missing original JPG binaries; deployment remains on hold until those original assets are restored and strict validation passes.

## v2.64.0 — responsive composition, Part 1 media normalization and A–Z sound lab

- Standardized all Listening Part 1 images to a common 4:3 frame with `object-fit: cover`, consistent radius, frame width and caption. `part1-photocopier` now has a stable focal-point adjustment so the portrait source fills the same visual area as the other illustrations. The licensed JPG binary itself is not rewritten; the existing SVG fallback remains in the same shared frame.
- Balanced learning, Foundation, practice-mode, mock-exam and objective cards: equal grid-row height, title/copy baseline, common footer alignment, safe wrapping, minimum-width reset and non-clipping content. Long copy can expand a card/row; button labels wrap without overlap.
- Refined device-width behavior: alphabet sound lab uses 4 desktop / 3 tablet-landscape / 2 tablet-portrait-and-phone / 1 very narrow phone columns. Other learning cards keep two columns where space allows and one column at phone width. All breakpoints are CSS viewport based.
- Extended the existing Pre-A1 alphabet lesson into a 26-letter A–Z sound lab with letter names, example words, IPA, Vietnamese meanings, common focus sounds and two TTS actions per letter. Playback requests are recorded under the additive localStorage key `toeic:alphabet-sound-progress:v1`; this is exposure/interaction evidence only, not pronunciation accuracy, mastery, or free-speaking ability.
- Added the new alphabet data/helper to Service Worker REQUIRED and APP_SHELL; added Python and JavaScript tests. Added both Python test modules to CI execution after the coverage test exposed that they were only being syntax-checked, not run.
- Preserved every existing vocabulary/question/lesson stable ID, existing localStorage/IndexedDB schemas and learner progress. No destructive migration or data reset.
- Local verification only. The inherited archive still lacks eight licensed Part 1 JPG binaries; the strict photo validator remains enabled and blocks deployment until original files are restored. Browser/physical-device QA, remote GitHub Actions and GitHub Pages deployment are not claimed.

## v2.63.0 — Unified Design System & Design Profile

- Added canonical `design/design-profile.json` with 51 tokens and `tools/sync-design-profile.py` to synchronize both the token block and the generated legacy typography floor; CI checks drift in both.
- Consolidated cross-module typography roles, colors, component surfaces, buttons, controls, spacing, radii and shadows into a single visual contract. A 362-selector audit now raises every legacy fixed `px`/`rem` text rule below 12.5px across feature CSS and the old design-system prefix to the shared caption token; semantic content and control sizes are reasserted after the floor.
- Aligned Dashboard, Objective Tracker, Spaced Recall, Foundation, practice modes and the full TOEIC mock-test flow with the shared type and component hierarchy.
- Replaced the stale design guide with explicit rules, a new-module checklist and `docs/DESIGN_BRIEF_TEMPLATE.md` for owner preference selection.
- No vocabulary, IndexedDB or learner-progress data migration. Deployment remains held by eight inherited missing Part 1 JPG assets; remote CI/Pages/device QA pending.

## v2.62.0 — application-wide typography and Foundation Listening

- Audited the existing CSS cascade and added a shared application-wide typography floor. Main reading copy, card descriptions, objective-tracker evidence, practice-mode options, mock-test setup/results/review, form controls, captions and mobile navigation now use a consistent readable scale; large scores/timers retain their data hierarchy.
- Fixed the Foundation introduction layout by explicitly keeping the intro panel in one column; its content controls reflow separately on narrow viewports. Practice-mode and mock-test cards use content-first grids (auto-fit / tablet two-column / phone one-column) instead of squeezed fixed columns.
- Added a consistent type scale for Objective Learning Tracker cards, practice selection and TOEIC mock-test cards. Supporting metadata no longer uses the inherited 6–11px microtype styles for the audited reading surfaces.
- Added Foundation Listening for all 10 existing Pre-A1/A1 lessons: 10 original short workplace/everyday scripts, 20 stable multiple-choice comprehension questions, and balanced answer positions (5 each across A–D).
- Listening playback uses the learner's current browser/device Speech Synthesis voice settings. Transcript is hidden until requested. The UI and content metadata explicitly state that this is synthesized practice, not authentic ETS audio or a recorded TOEIC test.
- Added a separate `toeic:foundation-listening-progress:v1` ledger with stable question IDs, latest result and attempt history. Listening evidence is not merged with recognition, contextual application or reading evidence; retries do not add new unique-question IDs. Existing lesson progress and local data are preserved.
- Added the listening data and evidence helper to Service Worker REQUIRED and APP_SHELL; added Python/JavaScript tests and CI coverage.
- No vocabulary records, existing learning IDs, answer keys, IndexedDB schema/stores or existing localStorage progress keys were reset or migrated. Existing user data remains additive and separate.
- Local source verification only. Browser visual QA, remote GitHub Actions, GitHub Pages deployment and physical iOS/Android PWA behavior are not verified in this workspace. The inherited strict Part 1 photo-asset blocker remains: 8 original licensed JPG binaries are absent; restore them before deployment. SVG fallbacks remain available and the strict validator must remain enabled.

## v2.61.0 — Learning UI consistency and test integrity

- Fixed the false-positive scope test by isolating one top-level function at a time; the check continues to catch an actual `item.` reference inside `openGrammarLesson()` while allowing local callback variables in separate helpers.
- Re-verified the eight reviewed Listening Part 1 units. The old unit hash for each matched exactly after removing only `photoSourceType: "licensed-stock"`; all eight question hashes still match. Refreshed the eight `unitContentSha256` values and added `fingerprintRefreshLog` with old/new digests, scope and precondition results.
- Rebuilt the dashboard Spaced Recall queue using shared `panel`, `panel-header`, `learning-card`, shared count label and button styles. The human-facing card no longer prints internal stable question IDs; the ID remains bound to the correct review action.
- Rebuilt the Foundation learning-path overview with the same shared panels/cards, standard heading hierarchy and controls; increased body/status type sizes and made progress meter accessible.
- Added viewport-first responsive rules for the intro, cards and recall queue; no device-inch breakpoints or fixed-width-only layouts were introduced.
- Added CI coverage for the new learning-surface consistency test and the fingerprint refresh guard; expanded version synchronization checks to include `APP_RELEASE_VERSION`.
- No canonical learning content, question answer, ordering, stable IDs, personal data, IndexedDB schema or learner progress was changed/reset.
- Local verification only. The source ZIP inherited from v2.60.0 is missing 8 of the 9 licensed Part 1 JPG binaries; the strict asset validator run by CI therefore fails until those original Pexels files are restored. Exact recovery links are in `archive/PROJECT_HISTORY.md`. Do not deploy this candidate before the strict validator reports 9/9. GitHub Pages deployment and physical iOS/Android PWA presentation are not verified in this workspace.

## v2.60.0 — Vocabulary release integrity and PWA cache synchronization

- Fixed release/data mismatch risk: versioned `__release` query keys are used for the manifest and all JSON data requests, so an older Service Worker cache cannot silently return previous vocabulary files.
- Added runtime integrity gates: manifest version, per-letter counts, total word count, unique IDs and unique headwords must agree before the dictionary is rendered.
- Added a visible dashboard integrity line showing the validated GitHub base-dictionary count versus the manifest total, release version and personal additions separately.
- Service Worker update checks bypass HTTP cache; when an already-controlled PWA receives a new controller, it reloads once so HTML/JS/data are from one release.
- Kept canonical cache keys in the current versioned cache so precached data remains available offline; query strings are normalized only inside the current release cache.
- Preserved all 992 vocabulary records and existing stable IDs, personal vocabulary, IndexedDB schema and learner progress. No content count was fabricated or manually adjusted.
- Local source verification only; GitHub Actions, Pages and physical-device behavior remain unverified until deployed.

## v2.58.0 — Foundation contextual application evidence

- Added one stable contextual-application task to each of the 10 Pre-A1/A1 lessons (10 tasks).
- Application results and retry history are stored separately from recognition-question evidence; retries do not inflate unique recognition-question counts.
- Lesson detail explains that these are contextual multiple-choice checks, not free production or spontaneous communication.
- Preserved existing lesson/question IDs, `toeic:foundation-progress:v1`, legacy fields and IndexedDB schema.
- Local verification only; remote CI, GitHub Pages and physical-device QA are not claimed.

## v2.57.0 — Foundation learning evidence (Pre-A1/A1)

- Added 30 stable recognition/understanding checks across 10 lessons.
- Added unique-question evidence with latest-result accuracy and retry history.

## v2.59.0 — Foundation short reading comprehension

- Added 10 short reading passages (one per existing Pre-A1/A1 lesson) and 20 stable comprehension questions.
- Question skills cover locating explicit details and understanding simple purpose/context; passages are short, beginner-level workplace/everyday texts.
- Added separate reading evidence ledger `toeic:foundation-reading-progress:v1`, keyed by stable question IDs with latest result and attempt history. Retries do not inflate unique-question coverage.
- Local practice threshold: 2 unique questions and 80% latest-result accuracy. This is not CEFR certification or a broad reading-mastery claim.
- Added reading progress line to Foundation lesson cards and responsive passage styling.
- Added module/data to Service Worker REQUIRED and APP_SHELL for offline availability.
- Preserved existing lesson, recognition-question and contextual-application IDs; no IndexedDB schema migration or learner-data reset.
