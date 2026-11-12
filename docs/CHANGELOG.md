## v2.27.0 — Focus learning workspace & Vocabulary Batch 017 (2026-11-12)

- Added one shared fixed focus workspace with a dimmed/blurred backdrop, internal scrolling and a persistent close (×) control. Flashcard sessions and their follow-up vocabulary check now share the same workspace; the first card tap flips to meaning/examples and the next tap advances to the next word. Closing returns to topic selection.
- Rebuilt the Review landing view as a dashboard with learning statistics, eight selectable practice modes, weak-word list and a Start action. The question panel is hidden until Start, then moves into the focus workspace; closing returns to the dashboard.
- Normalized the detail presentation for Grammar, Listening and Reading into a centered, scroll-contained focus modal with the same dimmed background, close control and responsive sizing. Added phone safe-area and reduced-motion handling, with CSS containment to prevent page-layout expansion.
- Continued the next roadmap item with Vocabulary Batch 017: 43 additional TOEIC headwords. The canonical A–Z bank now contains 971 records. New CEFR classifications remain editorial estimates and the batch is marked pending editorial verification.
- Added `tools/tests/learning-focus-workspace.mjs` and registered it in GitHub Actions. The test guards unique HTML IDs, focus/close/flip/navigation structure, responsive CSS, all review modes, canonical vocabulary inclusion and unchanged IndexedDB v1.
- No personal IndexedDB schema/profile migration, reset, import/export or inspection was performed. TTS configuration and existing Listening/Reading/Grammar question banks were not changed.
- Local automated/static checks only. Real phone/tablet/laptop browser interaction, remote GitHub Actions/Pages, and the eight Part 1 JPG binaries are not verified in this snapshot.

## v2.26.0 — Flashcard image relevance & responsive layout

- Removed the generic topic illustration from individual vocabulary flashcards. A word card is text-first by default so an unrelated office/travel/finance image can no longer imply the wrong meaning.
- Added a strict opt-in image contract for future word-specific illustrations: `image` must point inside `./assets/vocabulary/`, `imageAlt` must describe the actual image, and `imageStatus` must equal `approved`. Topic thumbnails remain on the topic-selection screen only.
- Added responsive 4:3 approved-image frames on mobile/tablet/desktop, with a compact square frame on very narrow phones; images use `object-fit: contain` to avoid cropping important vocabulary details. No image is downloaded or added in this batch.
- No vocabulary records, stable IDs, mock questions, Listening/Reading/Grammar content, TTS settings, or IndexedDB schema/profile were changed.
- Added `tools/tests/flashcard-image-policy.mjs` to guard against generic topic art returning to individual word cards and to enforce the approved asset contract.

## v2.25.0 — Full TOEIC Mock Practice Beta (2026-11-11)

- Added three timed test modes: 15-minute quick test (25 questions), 60-minute half test (100 questions) and 120-minute full test (200 questions), with Listening/Reading timers (5:22/9:38, 22:30/37:30 and 45:00/75:00 respectively).
- Added data-driven form assembly from the internally reviewed pool: 102 Listening questions and 109 Reading questions. The 11 Listening Batch 013 reserve questions remain excluded while their independent editorial review is pending.
- Random selection preserves entire Part 3/4 conversations/talks, Part 6 text sets and Part 7 single/multiple-passage blocks. No question is duplicated inside a test; recent attempts are used to prioritize unused questions and repeated question count is disclosed when the current pool cannot create a fully new form.
- Added exam navigation map, answer/flag controls, persistent test timer, auto-transition Listening→Reading, timeout/manual submission, per-section/Part result analysis, targeted improvement guidance, answer explanations and post-test transcript/passage review. Part 1 prefers the JPG photo and falls back to its SVG illustration.
- Added a visual TOEIC-style result panel with separate Listening and Reading score rings, raw correct counts, accuracy, blank answers and the exact number of additional correct answers needed for the internal 75% practice target. The report does not invent an ETS-equated score.
- Added a dedicated lifetime question-use ledger (`toeic:mock-usage:v1`) so question rotation persists beyond the 60 most recent attempts shown in the history list. Added regression checks for lifetime rotation and Mock UI integrity.
- Test history, active exam and latest detailed result are stored in dedicated LocalStorage keys; no IndexedDB store, schema, personal vocabulary or existing study progress is changed.
- ETS-equated 10–990 scores are not fabricated. Results show raw correct counts and accuracy; 75% is an internal practice target, not an ETS/CEFR conversion.
- Added `tools/tests/mock-exam-engine.mjs` to local checks and GitHub Actions; cached `assets/js/mock-engine.js` as a required PWA shell resource.
- Local Chromium/physical device QA, remote GitHub Actions/Pages, actual remote JPG bytes and independent TOEIC expert signoff remain unverified. The local snapshot does not include the 8 JPG files; do not remove the user-owned GitHub assets when applying the patch.
- Next roadmap: vocabulary expansion → Grammar expansion → decorative study image assets (with exact download filenames/folders) → reviewed Listening reserve expansion → current TOEIC learning-platform benchmark. Personal IndexedDB import/export remains deferred.

## v2.24.0 — Listening/TTS playback reliability (2026-11-11)

- Hardened speech cancellation so the app resolves its active utterance immediately before calling the browser speech engine. The Listening playback sequence can no longer remain stuck waiting for a cancellation callback that some speech engines may omit.
- Unified cancellation behavior for vocabulary playback, multi-speaker Listening playback and one-off pronunciation previews. Expected `canceled`/`interrupted` browser events no longer appear as voice-failure errors.
- Added a deterministic Node regression harness for manual voice priority, Daniel fallback, stable speaker-to-voice mapping, per-lesson speed, configured turn/word pauses, stop behavior without a browser cancellation callback and preview interruption.
- Registered the TTS regression in GitHub Actions. No audio engine, voice timbre, default pause setting, Listening question, vocabulary record, IndexedDB schema or personal profile was changed.
- Local browser/device listening QA remains pending; this release verifies playback orchestration with a mocked speech engine, not the acoustic quality of Windows/iOS/Android voices. Existing Part 1 JPG, remote CI/Pages and independent TOEIC editorial blockers remain unchanged.

## v2.23.0 — Part 1 photo QA hardening & Listening reserve batch (2026-11-11)

- Re-audited all eight Part 1 photo/answer pairs against the Pexels source descriptions. Correct statements for the warehouse and air-conditioning items now describe the visible actions more precisely; answer indexes, option arrays, choice IDs and question IDs are unchanged.
- Added a strict photo-asset validator for all eight local JPGs: expected file names, JPEG signature, decodable dimensions (minimum 1280×960), Pexels attribution mapping and matching Part 1 IDs. CI now fails if the photo binaries are absent or invalid; the SVG rendering fallback remains available at runtime.
- Added a first reserve Listening batch: five new Part 2 responses, one three-question Part 3 conversation and one three-question Part 4 announcement (11 questions). Total Listening pool is now 113; blueprint selection remains 6/25/39/30 for the first form, leaving 13 Listening reserve questions beyond the first-form requirement.
- Replaced the v2.19.0 whole-file Listening SHA guard with per-question and per-unit fingerprints for its 148 reviewed items (including transcript segments and translations), so later reserve content can be appended without invalidating older review records. Approved photo-alignment amendments are recorded explicitly.
- Preserved all prior IDs, answer positions, choice text/identity for existing questions, 928 vocabulary IDs and the IndexedDB schema/profile. No personal profile import/export/reset/migration was performed.
- 177/177 local unit-test methods pass across the workflow modules; Python/JavaScript syntax, runtime render smoke, coverage/evidence/distractor audits and version sync pass. Validator tests were executed in small groups because the sandbox timeouts interrupt larger combined runs.
- Local vocabulary validator passes with 0 errors/0 warnings; learning validator has 0 errors and 8 missing-JPG warnings in this snapshot. The generic Service Worker validator now treats only `OPTIONAL` paths as optional; missing `APP_SHELL`/required files still fail. The strict photo validator remains a blocking release gate and requires all eight actual JPEG bytes; current working copy has 0/8. Do not mark remote Actions/Pages or physical-device QA as complete on this basis.

## v2.22.0 — Licensed Part 1 photographs & offline-safe image loading (2026-11-11)

- Replaced the primary Part 1 visual source with eight locally hosted Pexels JPG paths from the user's asset manifest; each item keeps its existing SVG fallback for missing/corrupt photo files.
- Added per-photo provenance (photographer, source page, direct-download URL and Pexels license URL) in `assets/listening/ATTRIBUTION.csv`.
- Updated the Part 1 renderer to prefer the JPG, recover to the SVG on image load failure, label the visual as a photograph, and render a responsive 4:3 frame.
- Added the eight JPG paths to the Service Worker's OPTIONAL cache list while retaining the SVG fallbacks in REQUIRED. A missing JPG will not abort Service Worker installation; available JPGs are cached for offline practice.
- Aligned the correct spoken descriptions for reception plant (B), restaurant table-setting (C) and photocopier (D) with the corresponding photographs. Existing correct answers remain A/B/C/D = 0/1/2/3; resource/question IDs, choiceIds, answer order and progress keys are unchanged.
- No IndexedDB schema, personal profile, vocabulary IDs, question counts or unrelated Listening/Reading content changed. No personal import/export/migration or reset was performed.
- The local source snapshot did not contain the JPG binaries; the patch references the filenames from the supplied manifest and assumes the user-added JPGs are already present in the GitHub repository. SVG fallback remains active if an asset is absent. Remote CI, Pages deployment and browser/device visual verification remain pending.

# CHANGELOG

## v2.21.0 — Legacy collocation cleanup & CI diagnosis (2026-11-11)

- Corrected 8 baseline FD001 collocation violations across 7 stable vocabulary records using guarded Batch 011 operations. The revised phrases keep headword-level collocation patterns and are recorded with dictionary/occupational/budgeting sources.
- Tightened `tools/quality-baseline.json` by removing exactly the 8 resolved FD001 entries; no new baseline debt was added. Final vocabulary validator: 928 records, 0 errors, 0 legacy warnings.
- Added regression coverage for the seven reviewed records, the zero-FD001 baseline and preservation of all 928 stable IDs.
- No question content, answer keys, stable choice IDs, vocabulary IDs, example/sense data, IndexedDB schema or personal profile data changed. No personal import/export/migration test was run.
- Investigated the user-reported GitHub Actions run `42981524564`: local `validate-data.py` and `choice_history` tests pass, but the remote failing command / commit SHA / workflow revision remain unconfirmed because the full job log has not yet been accessed. This batch does not claim to fix that remote CI failure.

## v2.20.0 — Vocabulary example readability, sense-linked POS cards & data detail fix (2026-11-11)

- Enlarged vocabulary example typography to a balanced 13.25px English sentence and 12px Vietnamese translation, with clearer line spacing and responsive sizing; also improved example text in learning references.
- Ran a full-corpus structural/heuristic audit over all 928 canonical examples for completeness, repeated English sentences, punctuation/capitalization, Vietnamese translation presence, and target-word traceability. The automated scan is a regression screen, not a substitute for human semantic proofing. Rewrote 28 overly short examples into fuller TOEIC workplace contexts.
- Added 26 sense-specific contextual examples across the 25 multi-sense headwords. Every example now carries `sense_index`; each sense is illustrated by at least one dedicated example. The 928 stable headword IDs remain unchanged.
- Replaced the repeated POS strip + repeated sense labels in word detail with one nested card per part-of-speech group. Multiple senses with the same POS share a card; definitions, synonyms/antonyms, contextual examples and verb forms sit inside their relevant POS card.
- Fixed the Data Workspace table click delegation so the word-name `data-detail` action opens the vocabulary detail modal; edit and delete actions remain separate and functional.
- Added validator rules for out-of-range example `sense_index` and senses without their own mapped example; expanded UI/data regression coverage. No IndexedDB database version, object store, or personal-profile import/export behavior changed.
- Preserved the v2.19.0 sidebar viewport fix and prior TOEIC content/question IDs. Remote GitHub Actions, GitHub Pages deployment and real-device visual QA remain pending.

## v2.19.0 — Remaining Listening/Reading second-pass review (2026-11-11)

- Completed an internal second-pass review of the 148 Listening/Reading questions outside Part 7: Listening P1=8, P2=25, P3=39, P4=30; Reading P5=30 and P6=16. Part 7's 63-question review remains recorded in v2.18.0.
- Checked Part 1 illustration-to-description fit; Part 2 speech-act/response fit; Part 3/4 transcript evidence, speaker/time/place details and distractors; Part 5 grammar and single-best-answer quality; and Part 6 syntax/cohesion/insertion fit. No substantive defect was confirmed, so no speculative content change was made.
- Added a machine-readable 148-question review inventory with source fingerprints and five regression tests for exact coverage, part distribution, source drift, key/choice/choice-ID/explanation integrity and conservative no-change decisions. These automated tests guard coverage/structure; they do not replace semantic review.
- Preserved question/option text, answer indexes, stable choice IDs, sequence, pool counts, 928 vocabulary IDs and IndexedDB schema/database version/store. The v2.18 desktop sidebar correction remains included.
- Personal IndexedDB profile testing remains deferred; no personal import/export/migration or reset was performed.
- Local validators, test results and package verification are recorded in `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.19.0.md`. Browser visual QA at 100% zoom, remote GitHub Actions and Pages deployment are not claimed.

## v2.18.0 — Sidebar height adaptation & Part 7 second-pass review (2026-11-11)

- Fixed the desktop sidebar vertical layout for short laptop viewports: the sidebar uses the dynamic viewport height, the navigation area scrolls independently when space is insufficient, and the local-data/version footer remains pinned and visible.
- Added compact vertical spacing at desktop heights up to 820 CSS px, with a tighter fallback up to 680 CSS px. The adjustment targets laptop layouts such as 1366×768 without hiding the local-data text.
- Added two sidebar regression tests and four Part 7 editorial regression tests. Mobile and tablet navigation breakpoints remain unchanged.
- Performed an internal second-pass review of all 63 Reading Part 7 questions across 24 sets. Clarified the hotel-room stay/departure dates and moved the reimbursement course completion date after the program effective date; updated the affected Vietnamese translation/rationale.
- Kept all Part 7 question IDs, question order, choice text, choice IDs, answer indices and question counts unchanged. Two legacy multi-document sets with one question each remain flagged for future integrated-question expansion.
- Deferred personal IndexedDB import/migration testing at the user's request. No personal profile data was imported, inspected or reset.
- Updated the distractor audit writer to derive its output filename from the manifest version. Vocabulary remains 928 records/928 stable IDs; Listening 102, Reading 109, Grammar 25 lessons/54 exercises.
- Local checks: vocabulary validator 0 errors/12 known legacy warnings; learning validator 0 errors/0 warnings; version sync, runtime smoke, syntax and workflow YAML checks pass. All 147 unit-test methods are confirmed PASS (102 grouped fast-suite methods, 12 version-sync methods and 33 validator methods; the validator methods were isolated after grouped execution hit the sandbox time limit). Browser/device QA, remote GitHub Actions and GitHub Pages deployment remain unverified.

## v2.17.0 — TOEIC answer-position balance & progress migration safety (2026-11-11)
- Evidence audit output now derives its report filename/version from `data/manifest.json`, so future releases no longer overwrite a file named for v2.15.0.

- Rebalanced the keyed-option positions for 132 reviewed items: Part 3 = A10/B10/C10/D9, Part 4 = A8/B8/C7/D7, Part 7 = A16/B16/C16/D15. Exactly 27 questions were changed by swapping the correct option with one distractor; no random shuffle was used.
- Preserved the original v2.16.0 `choices`, `choiceIds` and `answerIndex` for each changed question in `previousChoices`, `previousChoiceIds` and `previousAnswerIndex`. Stable IDs travel with their option; question IDs, question order, source text, explanation and correct answer text remain unchanged.
- Hardened startup migration for Reading, Listening and Grammar progress. Existing v2.16 records resolve their `choiceId` to the new index; older records without an ID use the v2.16 snapshot. `previousChoiceIndex` retains the pre-reorder index. Archived choices from the 12 v2.15 revisions remain separate; records with ambiguous text or invalid indices are not guessed or overwritten.
- Added regression coverage for all 27 mappings, answer-position targets, legacy/old/current progress migration, stable-ID rendering, migration idempotency and preservation of unknown historical text.
- No IndexedDB schema/object-store/database-version change, progress reset, vocabulary change, question-ID change or question-order change. Remote GitHub Actions, Pages deployment and physical-device QA remain pending until the package is pushed and tested in the target environment.

## v2.15.1 — Reading/Grammar runtime hotfix & CI runner maintenance (2026-11-10)

- Fixed the `ReferenceError: item is not defined` in `openReadingDetail()` by rendering each Reading choice directly from the active question's `choice` value; the function no longer references an out-of-scope `item` variable.
- Fixed the same out-of-scope `item.part` reference in `openGrammarLesson()` so Grammar exercise options render without a runtime exception.
- Hardened Reading card word-count rendering for Part 5 records that intentionally have no `passage` text; the display now falls back to structured document content or question text and computes a safe count.
- Added three regression tests covering Reading scope, Grammar scope and passage-less Part 5 card metadata.
- Updated GitHub Actions to Node 24-compatible `actions/checkout@v7`, `actions/setup-python@v7` and `actions/setup-node@v7`; pinned `runs-on: ubuntu-24.04` to avoid an unplanned `ubuntu-latest` OS migration during the Ubuntu 26 rollout.
- Local `validate-data.py` on the v2.15.0 source snapshot returns 928 records, 0 errors and 12 known legacy warnings. The precise cause of the user's historical remote run exit code 1 cannot be confirmed without the red log lines; the Node 20 and `ubuntu-latest` messages are deprecation/migration warnings, not proof of the failing assertion.
- This is a runtime/CI maintenance hotfix only: no vocabulary records, question content, answer keys, IDs, choice order, IndexedDB schema or learning progress are changed.

## v2.15.0 — TOEIC Distractor Quality Audit & Answer-Key Safety (2026-11-10)

- Completed a question-level distractor review of 132 items: Listening Part 3 (39), Part 4 (30) and Reading Part 7 (63), covering the 126 direct/lexical evidence mappings plus six paraphrase/inference items.
- Improved 12 option groups so distractors better match the relevant hotel, presentation, employee audience, travel record, refund, invoice, order, meeting and visitor-access context.
- Kept all correct answer texts, `answerIndex` values, question IDs, question order and question-pool counts unchanged. Added per-question `legacyChoices` snapshots for the 12 revised sets and additive `choiceText` persistence on new Reading/Listening attempts, so historical selected text is not silently replaced by a new distractor. No IndexedDB object-store/schema migration or progress reset was performed.
- Added `tools/audit-distractors.py`, a detailed audit report and five regression tests. The structural tool checks unique choices and valid key indices but does not claim to prove semantic quality automatically.
- Recorded answer-position imbalance in Part 3/4/7. Choices were not shuffled because saved `readingProgress`/`listeningProgress` currently store `choiceIndex`; safe rebalancing requires stable choice identity and a legacy progress migration first.
- Release is a local release candidate; physical-device/browser QA, remote CI and GitHub Pages deployment remain pending.
- Final local verification recorded 126/126 unit-test methods PASS (including saved-choice-history compatibility and isolated execution of the two slow suites), vocabulary validator 0 errors / 12 legacy warnings, learning-content validator 0 errors / 0 warnings, evidence/distractor audits PASS and version sync PASS. See `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.15.0.md`.

## v2.14.0 — Cross-device design system & editorial evidence traceability (2026-11-10)

- Added `assets/css/design-system.css` as the shared authority for typography, spacing/radii, control sizing, icon scale, focus feedback, touch behavior and responsive guardrails; documented the rules in `docs/DESIGN_SYSTEM.md`.
- Defined phone (≤640 CSS px), compact tablet (641–850), tablet/small laptop (851–1199) and desktop (≥1200) behavior. iPhone/Android bottom navigation respects safe-area insets; tablet hides the phone bar and keeps the icon rail. Inputs are 16 px on phones to reduce iOS Safari focus zoom.
- Added restrained motion: page transition, button/card feedback and progress-fill transitions; touch devices do not depend on hover; `prefers-reduced-motion` disables non-essential animation.
- Added accessible labels/tooltips to sidebar navigation for compact tablet mode; normalized shared control/icon sizes. Raised legacy 7–10 px micro-labels to a consistent 11 px minimum, supporting copy to 12 px where appropriate and compact action labels to 14 px; small icon/alphabet actions reach 44 × 44 px on touch devices.
- Corrected 23 generic Part 2 transcript-translation placeholders with translations of the actual spoken lines. Standardized the Part 2 response-selection prompt for the supplier-samples item and replaced an ambiguous bare “Yes” in the negative-tag room statement with “That’s right…”.
- Added `tools/audit-question-evidence.py` to map all 211 Listening/Reading keys to source content or explicit editorial review categories; it distinguishes direct text, lexical evidence, Part 1 visual review, Part 2 response-fit, Part 5 grammar and Part 6 contextual-fit rather than treating string overlap as semantic proof.
- Extended learning-content validation and tests for non-placeholder Part 2 translations and consistent prompts; added design-system and answer-to-source audit regression tests for typography, breakpoints, safe areas, touch targets, reduced motion, PWA precache and 211-item audit traceability. Unit tests: 116/116 PASS across grouped suite executions.
- Preserved 928 vocabulary records/IDs, all 26 A–Z files, the question IDs/order except the reviewed Part 2 response text, the 102/109 Listening/Reading pool sizes, Grammar totals and local personal-progress schema.
- Final package verification: 156 files, CRC PASS, clean extraction comparison 156/156 exact; both validators and version sync passed again on the extracted package; all 26 A–Z vocabulary files are byte-identical to v2.13.0.
- Responsive breakpoints, safe-area rules, typography/control sizes, Service Worker caching and CSS structure are covered by automated static regression tests. A local Chromium preview attempt was blocked by the sandbox (`ERR_BLOCKED_BY_ADMINISTRATOR`), so no browser screenshot/interaction QA is claimed. Physical iPhone/iPad, Android, remote CI and production deploy remain unverified. IELTS remains deferred.

## v2.13.0 — Editorial rationale QA & balanced TOEIC diagnostics layout (2026-11-10)

- Reworked the TOEIC Learning Diagnostics dashboard into an unboxed section heading and description, with separate Listening/Reading groups, seven independently framed Part cards, a lighter priority note and responsive tablet/mobile rules. Added visible keyboard focus and an accessible live status for the priority recommendation.
- Per-Part cards remain interactive and keep the same local progress source; no analytics calculation or local-storage/IndexedDB schema was changed. The explanatory note clearly identifies the diagnostic as an internal learning metric, not an ETS score conversion.
- Corrected all eight Part 1 prompts to call the current SVG assets illustrations rather than photographs; retained the explicit illustration provenance and specific A–D rationales.
- Reviewed the 211-question pool for rationale language and distractor quality. Localized 38 Part 3/4 explanations and seven legacy Reading explanations to Vietnamese; strengthened terse explanations in selected Listening/Reading items.
- Improved Part 2 invoice distractors so two choices no longer repeat the same page-two clue; clarified the supplier-delivery tag question and explicit response; retained the explicit contract-review completion response from the baseline. No question IDs or answer-array order were changed.
- Strengthened the test gate so an accented English token alone cannot satisfy the Vietnamese-rationale check; added prompt/provenance, distractor and illustration-rendering regression checks plus six static dashboard-layout regression tests. The dashboard suite is now part of GitHub Actions test commands; local test accounting is 97/97 PASS.
- Preserved 928 vocabulary records, all 928 IDs and 26 A–Z files; no Grammar totals, personal IndexedDB schema or study-history fields changed. Listening remains 102 questions, Reading 109, Grammar 25 lessons / 54 exercises.
- This is an editorial quality pass, not external/native-speaker certification or final Full Mock signoff. Browser visual screenshot, remote CI, GitHub Pages deploy and physical-device QA remain unverified. IELTS remains deferred.
- Final local package: 146 files; ZIP CRC PASS; fresh extraction comparison 146/146 byte-for-byte; extracted validators, version sync and static checks PASS. No GitHub commit/push or deploy is claimed.

## v2.12.0 — TOEIC question-pool expansion & structural content QA (2026-11-10)

- Expanded Listening to 56 units / 102 questions: Part 2=25, Part 3=39 across 13 three-question multi-speaker conversations, Part 4=30 across 10 three-question talks; Part 1 remains 8 explicitly labeled SVG illustrations.
- Expanded Reading to 35 resources / 109 questions: Part 5=30, Part 6=16, Part 7=63 (38 single-passage + 25 multiple-passage questions).
- Added 4 original Part 7 multi-document sets (two double and two triple passages); normalized two legacy double/triple records into structured `documents[]` with 2/3 labeled document objects while preserving `passage` and question order.
- Appended missing questions to three legacy Part 3 conversations and two Part 4 talks without changing existing question order/index. Preserved all 928 vocabulary records and all 26 A–Z files byte-for-byte; no personal IndexedDB migration.
- Strengthened learning-content validation and tests for one-form blueprint thresholds, Part 2 one-question units, Part 3/4 three-question sets, multi-speaker Part 3 conversations and structured Part 7 double/triple documents.
- A single 200-question form can now be selected from the pool according to the public blueprint. This is **not** a completed Full Mock, and it does not imply semantic validation of all answers, recorded/ETS audio or an ETS-equated score.
- ZIP release candidate contains 140 files; CRC and exact 140/140-file clean-extraction comparison PASS. Data validator, learning validator, version sync and static checks pass on the extracted package; unit tests 86/86 PASS with slow suites isolated.
- Full release evidence and remaining unverified QA are recorded in `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.12.0.md`; remote CI, GitHub Pages deployment and physical-device QA are not claimed; IELTS remains deferred.

## v2.11.0 — TOEIC-only coverage expansion & content operations (2026-11-09)

- Scope reset: focus 100% on TOEIC Listening & Reading (7 Parts); IELTS is deferred until the TOEIC acceptance gates in `MASTER_STATUS.md` are met and the user approves the transition.
- Listening expanded from Parts 2–4 to Parts 1–4 with 8 original SVG-based image-description practice sets; all Part 1 assets are required offline resources. These illustrations and browser TTS are not official ETS photos/audio.
- Reading standardized across Parts 5, 6 and 7; new P5/P6/P7 content brings the library to 27 resources / 77 questions.
- Grammar expanded to 25 TOEIC-oriented lessons / 54 exercises.
- Added per-Part dashboard progress and accuracy based on local practice history; added Reading Part filter and Part 1 visual/audio flow.
- Added a locked six-operation sourced IPA patch; preserved 928 stable vocabulary IDs.
- Added learning-content validator, TOEIC coverage report generator, tests and CI workflow gates.
- Added competitor benchmark, content update operations guide, batch/source/report files under `docs/`; `docs/MASTER_STATUS.md` remains the only Master.
- Full 200-question timed mock, official ETS material, calibrated score prediction, remote CI, deployment and physical-device QA remain outstanding.
- Release gate: 82/82 unit tests PASS across five suites (validator cases run in groups/individually); vocabulary validation 0 new errors / 12 known legacy warnings; learning-content validation 0 errors / 0 warnings; version sync, Python/JavaScript syntax, 73-resource APP_SHELL and extracted ZIP recheck PASS. Remote GitHub Actions and real-device/browser UI QA remain unverified.
- Final verification on 2026-11-10: reran 82/82 tests with per-method isolation for the two slow suites; re-extracted the package, re-ran both validators and version sync, checked 206 unique HTML IDs and 73 APP_SHELL resources, and rebuilt the ZIP without generated Python cache files. Remote CI/deploy/device QA remain pending.

## v2.10.2 — Lexical Audit Batch 002 & Documentation Consolidation (2026-11-09)

- Continued lexical audit from v2.10.1: added 11 US IPA transcriptions checked against Cambridge Dictionary pronunciation entries.
- Added 9 reviewed `word_family` relationships among headwords already present in the 928-record vocabulary. No new headwords or IDs were introduced.
- Consolidated every project Markdown file under `docs/`: single Master, documentation index, changelog, historical batches, reports and source references.
- Updated `tools/sync-version.py`, its unit tests and GitHub Actions path filters to use the new documentation paths.
- Updated the comprehensive Master with a workstream-by-workstream status matrix, accepted decisions from the previously agreed Claude + ChatGPT plan, remaining gaps, sequence and completion criteria.
- Vocabulary remains 928 records / 928 IDs / 26 A–Z files; IPA coverage increased 563 → 574, word-family records 122 → 131.
- Validator after batch: 0 ERROR, 12 known legacy warnings unchanged. Unit tests: 69/69 PASS by grouped/isolated execution. Remote CI, deployment and physical-device QA are not claimed as passed.

## v2.10.1 — Smart Review Wait Modal, Flashcard Layout & iPhone Male Voice Priority (2026-11-09)

- Moved the post-OK auto-next countdown into a dedicated blocking wait modal with a visible countdown ring, progress bar, loading state and a manual-cancel action. The manual Next button is enabled when auto-next is off or the wait is cancelled. Wait state is restored safely after reload.
- Hardened the Flashcard layout for PC/laptop widths: grid children use zero min-width, the image frame keeps a stable aspect ratio and `object-fit: contain`, long details scroll within a fixed content region, and the layout switches to a stacked card when the actual content width is narrow. Topic cards use fewer columns at smaller widths.
- Added an iPhone-informed male voice fallback: when no voice is explicitly saved and the device exposes `Daniel — en-GB`, it is recommended and selected as the male voice fallback. Manual voice URI selection remains authoritative. The utterance language follows the selected voice locale.
- Updated the voice settings note to explain the Daniel recommendation and device voice dependency. Female default voice preference remains unchanged.
- No vocabulary records, headwords, base IDs, personal overrides, or study history were intentionally changed.
- Automated data validator: 928 records, 0 ERROR, 12 known legacy warnings. JavaScript syntax checks: PASS. Remaining visual and voice quality QA on physical iPhone/desktop devices remains pending.

## v2.10.0 — Smart Review, Flashcard Layout & Natural TTS (2026-11-09)

- Added a dedicated answer-review modal with correctness, chosen answer, expected answer, vocabulary meaning, word family, verb forms, examples and per-choice explanations. The modal must be acknowledged with OK before moving on.
- Changed auto-next timing: the countdown starts only after the learner presses OK. When auto-next is disabled or cancelled, the manual Next button remains available. AI analysis and modal review do not allow a hidden timer to advance the question.
- Stabilized the practice workspace with responsive type scaling, minimum reserved heights, wrapping and mobile-specific choice layout.
- Reworked Flashcard/topic illustrations into fixed aspect-ratio frames; removed centered emoji overlays, keeping topic icons in the title. Added a graceful fallback when an illustration fails to load and a scrollable content panel so long meanings/examples do not resize the card.
- Added on-device English voice selectors for male/female, manual override when gender labels are unreliable, voice preview buttons, accent selection, rate, volume, pitch, vocabulary word-gap and dialogue-turn-gap settings. Settings are stored locally.
- Listening dialogue keeps one voice per speaker within a playback, preserves sentence/turn pauses, and exposes a slow vocabulary playback action. The default vocabulary pause is 900 ms; it can be configured from 0.6 to 1.3 seconds. Stop cancels both speech and pending gap timers.
- Rebuilt the A–Z rail as a horizontally scrollable flex row with larger touch targets, spacing, snap behavior and preserved scroll position. Increased typography and responsive spacing across the learning UI.
- Added `personalVocabulary` schema v3 `overrideBaseSigs` migration; existing personal overrides retain their content, and imports/exports preserve or initialize the source signature so later base-word changes can be flagged without overwriting personal edits.
- No vocabulary headwords, base IDs, meanings, study progress or personal word content were changed in this UX release. Data validator remains 928 records, 0 ERROR and 12 known legacy warnings.
- Automated checks: 69/69 unit tests PASS when run by module/group (13 baseline IDs, 11 patch engine, 12 version sync, 33 validator); JS syntax, data validator, version synchronization, APP_SHELL and ZIP integrity PASS.
- Release package prepared. GitHub Actions/GitHub Pages production deploy and real-device QA (iPhone Safari, Android Chrome and physical desktop/browser voices) remain unverified.

# CHANGELOG

## v2.19.0 — Remaining Listening/Reading second-pass review (2026-11-11)

- Completed an internal second-pass review of the 148 Listening/Reading questions outside Part 7: Listening P1=8, P2=25, P3=39, P4=30; Reading P5=30 and P6=16. Part 7's 63-question review remains recorded in v2.18.0.
- Checked Part 1 illustration-to-description fit; Part 2 speech-act/response fit; Part 3/4 transcript evidence, speaker/time/place details and distractors; Part 5 grammar and single-best-answer quality; and Part 6 syntax/cohesion/insertion fit. No substantive defect was confirmed, so no speculative content change was made.
- Added a machine-readable 148-question review inventory with source fingerprints and five regression tests for exact coverage, part distribution, source drift, key/choice/choice-ID/explanation integrity and conservative no-change decisions. These automated tests guard coverage/structure; they do not replace semantic review.
- Preserved question/option text, answer indexes, stable choice IDs, sequence, pool counts, 928 vocabulary IDs and IndexedDB schema/database version/store. The v2.18 desktop sidebar correction remains included.
- Personal IndexedDB profile testing remains deferred; no personal import/export/migration or reset was performed.
- Local validators, test results and package verification are recorded in `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.19.0.md`. Browser visual QA at 100% zoom, remote GitHub Actions and Pages deployment are not claimed.

## v2.9.11 — IPA, Word Family & Lexical Audit Batch 001 (2026-11-09)

- Corrected 7 invalid/ambiguous IPA values, including five US rhotic transcriptions and two dual-POS IPA strings.
- Added 24 source-checked US IPA transcriptions from Cambridge Dictionary; IPA coverage increased 539 → 563/928.
- Curated word-family relationships across 49 existing records; coverage increased 74 → 122/928. No headwords or IDs were added.
- Added Cambridge-listed synonyms `challenger`, `contender`, and `rival` for `competitor`; added two missing related-term glossary entries.
- Changed `competitor` CEFR from A2 to B1 based on Cambridge's B1 label; synchronized sense, record and manifest counts. No mass CEFR reclassification.
- Applied three guarded data batches (31 IPA + 49 word-family + 4 competitor synonym/CEFR operations), each dry-run verified with base version, ID-set SHA-256 and expected old values.
- Tightened quality baseline by removing the 7 resolved IPA warnings only. Validator: 928 records, 0 ERROR, 12 known legacy warnings (DF005=3, EX006=1, FD001=8 across 7 records).
- The single `phonetic.us` field cannot hold both noun/verb pronunciations of `estimate`; the noun pronunciation is retained because noun is its first sense. POS-specific IPA requires a separate schema/runtime enhancement.
- Release package prepared; GitHub Actions, GitHub Pages deployment, and real-device QA remain unconfirmed.

## v2.9.10 — Verb Forms & Collocations (2026-11-09)

- Added 122 verb-form sets to records with at least one verbal sense; all 291 records with a verbal sense now have forms. Existing 169 form sets were preserved.
- Added two contextual TOEIC collocations to each of 39 previously empty verb/mixed-POS records. Collocation coverage is now 758/928.
- Added structural validator rules VF001 (verb sense requires forms), VF002 (V1 must match headword), and FD003 (verb sense requires at least one collocation).
- Added `expect.verbSense=true` preconditions to verb-related patches and 5 targeted validator/patch-engine tests.
- Applied four reviewed patches with base version, ID-set SHA-256 and `expect.old`; no record IDs, meanings, examples, IPA, POS, CEFR or personal data were changed.
- Removed the empty `data/verbs/irregular-verbs.json`; no runtime or tooling consumer was found.
- Final validator: 928 records, 0 ERROR, 19 preserved legacy warnings. Quality and ID baselines remain unchanged.
- Release package prepared; GitHub Pages deployment and physical-device QA remain unconfirmed.

## v2.9.9 — Definition & Example Correction (2026-11-09)

- Corrected 160 English definitions across the 928-record TOEIC vocabulary dataset.
- Reviewed all 160 English examples and updated 159 example sentences; one already suitable sentence was retained.
- Updated all 160 Vietnamese example translations for consistency with the English sentences.
- Resolved baseline debt DF002=160, DF003=114, DF004=160, EX004=79 and EX005=79. The 79 EX004/EX005 record IDs are subsets of the 160 DF002 IDs; the unique record count is 160, not 171.
- Applied four reviewed batches through `tools/patch-data.py`; every patch is locked by base version, ID-set SHA-256, stable record ID, JSON Pointer, expected old value and POS where applicable.
- Tightened the quality baseline only by removing 600 resolved violation entries; no new debt was added.
- Final validator: 928 records, 928 stable IDs, 0 errors and 19 known legacy warnings (DF005=3, EX006=1, FD001=8 violations across 7 records, IP001=2, IP004=5).
- No schema change, personal IndexedDB migration, or UI behavior change. GitHub Pages deployment and real-device QA remain unconfirmed.

## v2.9.8 — Data Quality & Release Integrity (2026-11-09)

- Added a ratcheting data validator with structural errors, legacy-debt warnings, and new-regression errors keyed by rule + record ID + JSON pointer.
- Added reviewed quality and ID baselines; baseline ID metadata is protected by count, SHA-256, schema-version, and duplicate-ID checks.
- Added validator/sync-version unit tests and GitHub Actions checks for Python, vocabulary data, app-shell resources, version markers, and JavaScript syntax.
- Updated manifest and all release markers to 2.9.8; retained the existing cache-name prefix.
- Rebuilt Service Worker installation: required resources must succeed, optional assets are best-effort, failed responses are never cached, and only prior TOEIC app caches are cleaned after successful installation.
- No vocabulary record or personal IndexedDB data was changed. All 928 records and 26 A–Z files remain byte-identical to v2.9.7.
- Release ZIP is prepared; GitHub Pages deployment and real-device QA are not yet confirmed.

## v2.9.5 — Vocabulary Batch 002 (draft)
- Added 44 unique headwords to the 612-word v2.9.3 baseline; total is now 656.
- Updated A–Z files, manifest counts and Service Worker cache version.
- Added batch-002.json and VOCABULARY_BATCH_002.md.
- Added US IPA, contextual examples with Vietnamese translations, topic tags and selected collocations/family forms.
- Synonyms/antonyms and verb inflections remain unfilled where not verified; CEFR is editorial estimate.


## v2.9.2 – Natural multi-speaker Listening
- Cải thiện nhận diện voice nữ/nam từ danh sách voice tiếng Anh mà thiết bị cung cấp.
- Giữ voice ổn định cho cùng một speaker trong một lượt phát.
- Nếu có nhiều speaker cùng giới tính, ưu tiên các voice khác nhau khi voice pack có đủ lựa chọn.
- Phát tuần tự từng câu/lượt lời; chờ lượt hiện tại kết thúc rồi nghỉ ngẫu nhiên 650–850 ms trước lượt tiếp theo.
- Nút Dừng hủy cả audio hiện tại và khoảng nghỉ đang chờ; cập nhật Service Worker cache.
- Không thay đổi transcript, câu hỏi, đáp án hoặc dữ liệu Listening.


## v2.9.1 – Flashcard refinement
- Bổ sung tìm kiếm chủ đề trong Flashcard.
- Hiển thị đủ hình minh họa theo 32 chủ đề hiện có, thay vì fallback chung.
- Bổ sung nghĩa liên quan, đồng nghĩa, trái nghĩa và verb forms ở mặt sau flashcard.
- Hoàn thiện luồng thích ứng: ưu tiên từ sai trộn với từ mới trong lượt tối đa 10 thẻ; lượt đạt từ 80% mở 5/10 từ mới.
- Cập nhật cache version Service Worker.
- Gom tài liệu Master thành README, MASTER_STATUS, DATA_GUIDE, CHANGELOG.

- Thêm 12 nhóm chủ đề tổng hợp cho Flashcard (Sales, Supply Chain, Insurance, Manufacturing, Customer Complaints, PR, R&D, Energy, Safety, Public Service, Media, Project Management).
- Tìm kiếm chủ đề bao gồm cả nhóm tổng hợp; nhóm tổng hợp lấy từ các chủ đề gốc liên quan, không sửa dữ liệu gốc.

## v2.9.2 – Project audit and master consolidation
- Kiểm kê lại dữ liệu trực tiếp từ package: 492 từ, 32 chủ đề gốc; đính chính báo cáo 577 từ trước đó.
- Đồng bộ `data/manifest.json` từ 2.9.1 lên 2.9.2.
- Hợp nhất trạng thái module, thống kê dữ liệu, giới hạn, quy tắc kỹ thuật và roadmap vào `MASTER_STATUS.md`.
- Rút gọn `README.md` thành hướng dẫn triển khai và liên kết đến Master; bỏ `DATA_GUIDE.md` trùng lặp.
- Ghi nhận dữ liệu động từ bất quy tắc hiện đang rỗng và các hồ sơ từ vựng/Reading cần hoàn thiện.

## 2.9.2 — Vocabulary recovery working update (2026-11-06)
- Compared v2.9.0 and v2.9.2 ZIP vocabulary records by stable word ID.
- Restored 85 records present in v2.9.0 but missing in v2.9.2; working total is 577.
- Updated `data/manifest.json` per-letter counts and CEFR counts.
- Reprioritized Phase 5: complete and validate vocabulary before per-word images, Listening, Reading, and Grammar expansion.
- This is a working recovery package, not a published release. Restored records still require editorial quality review.

## v2.9.3 — Vocabulary Batch 001 (draft)

- Added 35 unique headwords extending the recovered 577-word baseline.
- Updated A–Z vocabulary files and manifest counts.
- Added `data/vocabulary/batch-001.json` and `VOCABULARY_BATCH_001.md`.
- Entries remain editorial drafts: IPA, CEFR, synonym/antonym and verb-form QA is still required.

## v2.9.5 — Vocabulary Batch 003

- Added 75 TOEIC-priority headwords; total 731.
- Expanded HR, finance, procurement, logistics, manufacturing, retail, office, customer service and travel vocabulary.
- See `VOCABULARY_BATCH_003.md`.


## v2.9.6 — TOEIC Batch 004
- Added 79 TOEIC-focused entries; total vocabulary records: 810.
- Batch file: `data/vocabulary/batch-004.json`; report: `VOCABULARY_BATCH_004.md`.
- This is a draft-review data expansion; no claim of official TOEIC list completeness or deployment.

## v2.9.7 — TOEIC Batch 005
- Added 118 unique TOEIC-focused headwords; total 928.
- Expanded HR, payroll, finance, legal, management, planning, workplace and operations vocabulary.

## v2.16.0 — Stable choice identity & CI failure isolation (2026-11-10)

- Added persistent `choiceIds` arrays to all 109 Reading questions, 102 Listening questions and 54 Grammar exercises (265 question/exercise sets). IDs are scoped to the stable parent resource/question position and remain paired with their option when choices are deliberately reordered in a future reviewed patch. Duplicate option text retains distinct IDs.
- Added additive `choiceId` persistence for new Reading, Listening and Grammar attempts. Existing `choiceIndex`, `choiceText`, correctness and timestamps are retained.
- Added a safe startup migration for existing `readingProgress`, `listeningProgress` and `grammarProgress`: valid legacy `choiceIndex` records receive the corresponding `choiceId`; the 12 edited distractor groups use separate `legacyChoiceIds` so historical answers map to archived options, not replacement distractors. Malformed/out-of-range records are left untouched. No IndexedDB object store, database version or progress key is changed.
- Split GitHub Actions unit-test execution into individual steps so a failing suite is identified by its own step rather than one large `Unit tests (isolated modules)` block. Added explicit 15-minute limits to the slow validator/version-sync steps and a dedicated choice-identity suite.
- The earlier linked GitHub run's exact failing assertion cannot be reconstructed from its one-line annotation alone. This release improves diagnostic isolation; remote CI remains unverified until the user pushes and a new run completes.
- No answer choices were reordered and no answer key was changed in this batch. Position balancing remains gated on migration validation and a separate editorially reviewed reorder plan.
