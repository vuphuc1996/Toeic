# Foundation A2 Extended Listening — v2.91.0

## What changed

All 13 supplementary A2 Listening clips were upgraded in place. Each now contains six alternating turns (three male and three female voice assignments) and 75–100 spoken words. The 39 questions consistently cover:

1. Listening for detail.
2. Understanding purpose or context.
3. Inferring the next action.

Each question has four unique choices, a rationale and an exact source-turn `evidenceText` excerpt. Full-bank answer positions remain balanced A/B/C/D = 25/25/24/24. A SHA-256 registry fingerprints each complete supplementary clip object.

## Runtime and progress

- Existing clip IDs, question IDs and `{lessonId}::listening2` evidence scope are unchanged, so the learner's existing supplementary Listening progress remains attached to the same IDs.
- The panel remains collapsed by default and now discloses that the dialogue contains six turns.
- Playback uses the learner's configured browser SpeechSynthesis voices and existing inter-speaker pause settings. It is not an authentic ETS recording.
- Transcript remains hidden until requested. Core Listening progress remains separate from the supplementary scope.
- No new storage key, IndexedDB migration, API or server is introduced.

## Review status

**`pending-independent-review` — all 13 clips / 39 questions.** Automated checks verify structure, stable IDs, exact evidence snippets, answer-key uniqueness, balance and content hashes. They do not prove natural spoken English, psychometric validity, true A2 level or learner comprehension. A second reviewer should listen to every clip and complete `FOUNDATION_A2_LISTENING_REVIEW_CHECKLIST_v2.91.0.md` before any approval state is changed.

## Validation

See `TEST_REPORT_TOEIC_Dictionary_v2.91.0.md` for the complete local test record and the remaining remote/device acceptance gates.
