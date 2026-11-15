# Test Report — TOEIC Dictionary v2.59.0

## Feature under test

Foundation short reading: 10 passages / 20 questions; independent evidence ledger `toeic:foundation-reading-progress:v1`; retry history; 2-unique-question / 80%-latest-result practice threshold.

## Passed checks

- JavaScript regression scripts: 16/16 PASS, including the new `foundation-reading-evidence.mjs` and existing Foundation, Recall Queue, Reading/Listening/Grammar runtime, mock and TTS suites.
- Focused Python tests: 20/20 PASS across Foundation reading, Foundation pathway, learning-start-level, PWA readiness and CI coverage.
- JavaScript syntax: `assets/js/app.js`, `assets/js/foundation-reading-evidence.js`, `sw.js` PASS; all JS regression scripts executed successfully.
- Version synchronization: PASS for manifest, Service Worker, title, sidebar, phase note, footer, README, Master and Changelog.
- Vocabulary validation: 992 records, 0 errors, 0 warnings.
- Learning-content validation: 0 errors, 8 known warnings for missing original Part 1 JPG bytes in this source snapshot; SVG fallbacks remain.
- Objective resource map: 281/281 links; learning outcome criteria 30/30.
- New content audit: 10 passages mapped to 10 existing lessons; 20 unique stable question IDs; 4 answer choices per question; answer positions balanced A/B/C/D = 5/5/5/5; 15 detail, 2 main-idea, 2 purpose and 1 simple-inference questions.
- PWA shell: new JSON and JS module are listed in REQUIRED and APP_SHELL.

## Known limitations

- The 2-question / 80% gate is a local practice threshold only, not CEFR certification or comprehensive reading mastery.
- All new reading checks are multiple-choice; no free-response, timed fluency, listening, speaking or writing evidence is claimed.
- Learner progress cannot be reported without using the app on the learner's device; no personal localStorage data was imported.
- The full Python discovery suite was not certified as all-green in this run. It previously exposed a known, unrelated fingerprint mismatch for Listening `part1-meeting-documents`; this release does not modify that content or its fingerprint.
- Eight original Listening Part 1 JPG files are not present in this source snapshot; SVG fallback remains. Strict GitHub asset validation depends on those original repository assets.
- Remote GitHub Actions, GitHub Pages deployment, offline browser behavior and physical-device QA were not run.
