# Project Progress Baseline — TOEIC Dictionary v2.66.1

## Release scope

- All Speech Synthesis entry points now wait a fixed 2,000 ms after voice-catalogue readiness and queue cleanup before the first utterance. This is fixed in source, not user-configurable.
- Listening Part 1 uses a standard script: topic title (`Part 1: [Topic]`), 1,000 ms pause, common lead-in, 1,000 ms pause, separately spoken A/B/C/D labels, 1,500 ms after each label, then its description; 1,300 ms separates the descriptions.
- Practice and Mock Exam share the same Part 1 playback implementation. Mock Exam routes Part 1 directly to it, avoiding a duplicate generic transition phrase. The transcript and exam hint match the spoken script.
- CI regression test coverage for distractor/answer persistence now reflects the deferred-assessment contract: selections remain drafts until full-set completion and confirmation.

## Target-based progress

- TOEIC vocabulary: 992 / 3,000 minimum = **33.1%**. Bank size is not learner mastery.
- TOEIC vocabulary against the planning ceiling: 992 / 5,000 = **19.8%**; not a quality score.
- Guided pathway stages represented: 2/6 = **33.3%** (Pre-A1/A1 present; A2–C1 remain future stage scope).
- Objective resource links: 281/281 = **100% link coverage**; this is not proof of outcomes mastered.
- Outcome criteria defined: 30/30 = **100% framework coverage**.
- TOEIC objective evidence wired: 9/10 = **90%**.
- Foundation A–Z data: 26/26 records = **100% bank coverage only**, not pronunciation proficiency.
- Listening inventory: 107 units / 201 questions; Reading: 51 resources / 200 questions; Grammar: 33 lessons / 86 exercises. No approved numeric expansion target exists, so total-content expansion is not measured.

## Verification

- JavaScript regression: **21/21 scripts PASS**.
- Focused Python suite: **85/85 tests PASS across 10 selected modules**. This is not the full Python discovery suite.
- TTS readiness: 13/13; distractor/deferred draft semantics: 6/6.
- Version sync: PASS; design profile sync: PASS (54 tokens, 362 legacy typography groups).
- Vocabulary validator: 992 records, **0 errors / 0 warnings**.
- Learning-content validator: **0 errors / 8 missing-JPG warnings**; SVG fallbacks remain declared.
- Strict Part 1 photo validator: **FAIL, 8 original JPGs missing (1/9 present)**. Deployment remains on hold until the originals are restored.

## Not measured / outstanding

- Physical-device audio onset, spoken letter accuracy, voice selection and perceived pacing on iPhone/iPad/Android/desktop.
- Remote GitHub Actions and GitHub Pages deployment.
- Actual learner TOEIC score prediction, CEFR certification or broad skill mastery.
- Full Python test discovery.

## Data preservation

No IndexedDB schema/store migration; no question text, answer key, stable ID, vocabulary record, personal vocabulary, progress history, voice selection, rate, pitch or volume reset. Older stored TTS delay keys are ignored because Part 1 timing is now a shared fixed contract.
