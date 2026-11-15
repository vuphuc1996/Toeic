# Test Report — TOEIC Dictionary v2.66.0

**Status:** local release candidate; deployment hold.

## 1. Feature tests

### Dashboard progress layout
- Listening Parts 1–4 and Reading Parts 5–7 appear in separate full-width exam/skill groups.
- Group identity uses `data-progress-exam` and `data-progress-skill`; Part grids are independent and do not assume Listening and Reading will always be the only skills.
- Desktop/tablet/mobile layout remains a stacked skill-row model; the Part grids reflow inside each row.

### Deferred result reveal
- Choice staging stores the selected option and timing only; correctness and explanations are not written to draft records.
- Grammar, Reading and Listening batch practice show an aggregate summary only when the full set has choices.
- Foundation recognition/application/reading/listening, single-question Smart Review/Part 5, Flash Quiz and Placement follow the same summary-before-review contract.
- Confirmation commits attempt history and objective evidence, then opens the existing explanations/review.
- Mock Exam hides answer correctness, persists a pending summary through reload, and reveals transcript/answer/explanations only after explicit confirmation.

### Time-guided Mock Exam
- Quick mode: 15 minutes / 25 questions.
- Half mode: 60 minutes / 100 questions.
- Full mode: 120 minutes / 200 questions.
- Schedule weights include context audio/passage, question prompt and a 2.4-second transition/lead-in allowance inside each section deadline.
- The active question is updated from the current time, with section-local numbering, Part lead-ins, visual highlight and auto-scroll.
- Listening audio plays on group entry. Moving to another question in the same Part 3/4 conversation does not restart the audio.

## 2. Automated tests

### JavaScript

**21 / 21 regression suites PASS**:

- `alphabet-sound-progress.mjs`
- `assessment-deferred-workflow.mjs`
- `explanation-rubric-self-report.mjs`
- `flashcard-image-policy.mjs`
- `foundation-application-evidence.mjs`
- `foundation-evidence.mjs`
- `foundation-listening-evidence.mjs`
- `foundation-reading-evidence.mjs`
- `learning-focus-workspace.mjs`
- `learning-outcome-progress.mjs`
- `listening-tts-regression.mjs`
- `mock-exam-engine.mjs`
- `mock-guided-flow.mjs`
- `mock-ui-integrity.mjs`
- `objective-recall-timing.mjs`
- `part5-timing-integration.mjs`
- `practice-progress.mjs`
- `recall-queue.mjs`
- `runtime-render-smoke.mjs`
- `sentence-completion.mjs`
- `vocabulary-release-integrity.mjs`

### Python

**259 / 259 focused test cases PASS across 36 selected modules**, including dashboard layout, design profile, responsive composition, deferred assessment history, stable choice identity, Foundation and Placement, mock/CI coverage, Reading/Listening/Grammar content, vocabulary metadata and release synchronization.

The broad `test_validator.py` run exceeded the execution time limit. It is explicitly not reported as PASS.

## 3. Integrity checks

- `python tools/sync-version.py --check`: PASS (all v2.66.0 markers synchronized).
- `python tools/sync-design-profile.py --check`: PASS (54 design tokens and 362 legacy selector groups).
- `python tools/validate-data.py`: 992 records; 0 errors, 0 warnings.
- `python tools/validate-learning-content.py`: 0 errors, 8 missing JPG warnings; SVG fallbacks are available.
- `node --check sw.js` and all `assets/js/*.js`: PASS.
- CSS parse: `assets/css/app.css` PASS (1,503 top-level rules); `assets/css/design-system.css` PASS (266 top-level rules).
- CI coverage audit: PASS; all 21 JavaScript regression scripts are included in the workflow.

## 4. Known blockers / unverified areas

- Strict `python tools/validate-part1-photo-assets.py`: FAIL — only 1/9 JPG assets present; 8 original binaries are missing, including `part1-photocopier.jpg`. Do not disable this gate or replace licensed images with placeholders.
- Browser visual testing, device TTS playback, real iOS/Android PWA behavior, remote GitHub Actions and GitHub Pages deployment are not verified.
- The selected Python test set is not the full test discovery. `test_validator.py` exceeded the tool execution time limit.

## 5. Data safety

No IndexedDB schema/store migration, question/answer key edit, stable ID change, existing attempt history deletion, personal vocabulary reset or learner-progress reset was performed. Draft answers and pending Mock Exam review are additive and are committed as complete only after confirmation.
