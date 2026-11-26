# Change Manifest — TOEIC Dictionary v2.95.67

## Exact baseline

- Sole predecessor: `TOEIC_Dictionary_v2.95.66_FullSource.zip`.
- SHA-256: `30236500cfa2d8702a25cdca9c99f0eca58eaaa047928a6b12ce88b1b2a373c3`.
- Output release: `2.95.67`.
- No older FullSource, previous Patch, alternate branch or stale working directory was used as the source baseline.

## Vocabulary / editorial scope

- Added six reciprocal `word_family` links across the existing canonical pairs `apologize/apology`, `subscribe/subscription` and `transport/transportation`.
- All link spellings, target POS values and Vietnamese sense anchors are copied from existing canonical headword records. Cambridge Dictionary entries were cross-checked and recorded in `data/vocabulary/batch-025.json`.
- Added zero headwords and zero canonical IDs. No senses, Vietnamese meanings, English definitions, examples, IPA, verb forms, synonyms or antonyms were altered.
- Added a dedicated regression module and a read-only Word Family graph audit. Missing targets, POS mismatches, Vietnamese sense-anchor mismatches and one-way links are surfaced for human review only; nothing is auto-corrected.

## PWA / release-key correction

- Bumped synchronized source markers to `2.95.67`.
- Updated every remaining `__release=2.95.66` dependency/precache query in `assets/js/app.js`, `assets/js/mock-engine.js` and the Service Worker `REQUIRED` / `APP_SHELL` arrays to `__release=2.95.67`.
- Changed `tools/tests/service-worker-update.mjs` to derive the data request cache key from the parsed Service Worker release marker, preventing a fixed old release value from silently surviving a future version bump.
- The existing v2.95.66 shell-coherence behavior and guarded `#modalLayer` event listener are preserved.
- No visual design or navigation redesign was made. Robot Buddy behavior is unchanged.

## CI / tests / documentation

- Registered `test_vocabulary_family_batch_025.py` and `audit-word-family-graph.py` in `.github/workflows/validate-data.yml`.
- Updated the project-progress regression expectations from the previous 276/1,141 (24.2%) and 374 directed links to the current 282/1,141 (24.7%) and 380 directed links.
- Added current-release test, focused Python inventory, command, audit and package evidence reports.

## Protected data boundary

- The exact canonical vocabulary ID set remains 1,141 records; validator reports +0/-0.
- No Listening/Reading/Grammar question records, choice IDs/order, answer keys, Mock eligibility or reserve/review status changed.
- Learner IndexedDB schema/records, local progress, Robot Buddy privacy boundary, UI layout and GitHub-only static hosting architecture remain unchanged.
