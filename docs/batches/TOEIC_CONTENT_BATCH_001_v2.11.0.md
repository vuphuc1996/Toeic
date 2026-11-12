# TOEIC Content Batch 001 — v2.11.0

**Scope:** TOEIC L&R only; original editorial material; no ETS copyrighted questions/audio.

## Listening

- Added 8 Part 1 image-description practice sets, each with one image, four spoken statements, one correct answer, balanced A–D key positions (2 each) and explanation naming the actual correct letter.
- Added eight custom SVG illustrations. They are not photographic assets; UI copy labels them as illustrations. Audio is browser TTS, not recorded audio.
- Expanded library to 22 units / 36 questions: P1=8, P2=2, P3=18, P4=8.

## Reading

- Standardized all existing content to Part 7 where appropriate and supplied missing `documentType` values.
- Added Part 5: 4 sets / 16 sentence-completion questions.
- Added Part 6: 3 texts / 12 text-completion questions, blank marker count checked against question count.
- Added Part 7: 4 resources / 17 questions, including single/multiple document formats.
- Total: 27 resources / 77 questions.

## Grammar

- Added 4 TOEIC-focused lessons / 12 exercises.
- Total: 25 lessons / 54 exercises.

## Runtime / maintenance

- Added Reading Part filter and Listening Part 1 presentation.
- Added dashboard per-Part attempt/completion/accuracy summary based on local progress history.
- Added `tools/validate-learning-content.py` and `tools/audit-toeic-coverage.py`.
- Added new Part 1 images to required Service Worker resources to preserve offline behavior.

## QA limits

- The validator checks structure, IDs, counts, image presence, answer-index bounds and explanation presence; it cannot prove naturalness, factual correctness or perfect distractors.
- Physical photo/audio QA, native audio recordings, full 100+100 question bank, timed 200-question mock and official score equating remain future work.
