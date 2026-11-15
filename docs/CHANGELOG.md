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
