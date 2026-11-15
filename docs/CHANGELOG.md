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
- Local hotfix verification: 10/10 TTS Python checks and the Listening/TTS JavaScript regression pass after the fix. Full syntax/runtime and data checks are recorded in `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.65.1.md`.
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
- Local verification only. The source ZIP inherited from v2.60.0 is missing 8 of the 9 licensed Part 1 JPG binaries; the strict asset validator run by CI therefore fails until those original Pexels files are restored. Exact recovery links are in `reports/PART1_PHOTO_ASSET_RECOVERY_v2.61.0.md`. Do not deploy this candidate before the strict validator reports 9/9. GitHub Pages deployment and physical iOS/Android PWA presentation are not verified in this workspace.

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
