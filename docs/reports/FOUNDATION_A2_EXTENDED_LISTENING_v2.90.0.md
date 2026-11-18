# Foundation A2 Extended Listening — v2.90.0

## Scope

- 13 supplementary clips, one per A2 Foundation lesson.
- 39 new questions (3 per clip), 4 answer choices each.
- 13 formats: phone call, announcement, discussion, voicemail, workplace update, safety briefing, directions, invitation, process instructions, planning call, status call, notice and help-desk call.
- Each clip has four alternating female/male voice turns and 50–63 spoken words.
- Playback uses browser SpeechSynthesis and configured local voices; it is not an authentic ETS recording.

## Runtime and evidence

- Supplementary IDs use `{lessonId}::listening2` and question IDs beneath that clip ID.
- Supplementary evidence is stored in the existing `toeic:foundation-listening-progress:v1` ledger under `{lessonId}::listening2`.
- Original/core Listening remains stored under the original `lessonId` key.
- Draft answers, completion confirmation, summary and lesson-card counts are scoped independently.
- Transcript is hidden by default and can be opened on request.
- The supplementary section is collapsed by default and states that it is pending independent review.

## Quality controls

- 13 unique clip IDs map one-to-one to the 13 A2 lessons.
- 39 unique question IDs; every question has four unique choices, valid answer index, prompt and rationale.
- Answer positions across all 98 Foundation Listening questions: A/B/C/D = 25/25/24/24.
- Complete-clip SHA-256 registry: `tools/foundation-a2-listening-extended-v2.90.0.json`.
- Original 23 core clips / 59 questions and the v2.75.0 A2 q1/q2 baseline remain unchanged.

## Review boundary

All 13 new clips and 39 questions are `pending-independent-review`. Automated structural, source, ID, hash and runtime checks are not a substitute for a second language reviewer or learner validation. These clips are supplementary TTS practice only; they are not official A2 outcomes, CEFR certification, authentic audio or TOEIC Mock material.
