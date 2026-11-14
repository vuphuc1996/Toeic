# TOEIC Dictionary — consolidated release changelog

> The single chronological release log. Detailed implementation records live only for the previous/current release pair in `batches/` and `reports/`. Older releases are summarized here and in `archive/PROJECT_HISTORY.md`; do not create duplicate changelogs.

## v2.30.0 — Repeatable Practice & Vocabulary Batch 020 (2026-11-14)

- Added per-question and full-lesson retry to Reading, Listening and Grammar. Retrying archives the current submitted response instead of deleting it; previous answers remain visible in attempt history.
- Added attempt records containing selected option, stable `choiceId`, correctness, expected answer, explanation, timestamp and attempt number. Latest-attempt accuracy and unique-question coverage are separate from total attempts.
- Kept IndexedDB at `toeic-vocabulary-phase1` v1 / `workspace`. Existing progress objects with only `answers` remain compatible; `attemptHistory` is additive.
- Added Vocabulary Batch 020 with 13 unique TOEIC headwords; canonical total increases 979 → 992. US IPA is not guessed when the checked dictionary source does not provide a US transcription.
- Registered `assets/js/practice-progress.js` in the Service Worker required/precache lists and added retry regression coverage to local tests and GitHub Actions.
- Updated Master, Compatibility, Content Operations, version notes and this changelog. Release rotation keeps v2.29.0 + v2.30.0 active; v2.28.0 and older are compact history only.
- Detailed source/data changes: `batches/TOEIC_VOCABULARY_BATCH_020_v2.30.0.md`; verification: `reports/TEST_REPORT_TOEIC_Dictionary_v2.30.0.md`.

## v2.29.0 — Shared Learning Workspace & Flashcard Single Scroll (2026-11-13)

- Refactored Flashcard into an upper vocabulary panel and an expanding lower meaning/example panel; removed the inner fixed-height scrolling face.
- Standardized Flashcard, Review, Grammar, Reading and Listening detail flows on the same `learningFocusBackdrop` shell. Grammar/Reading/Listening mount through `openLearningDetail()`.
- Made `.learning-focus-content` the single vertical scroll owner. Short content stays natural-height; long passage/transcript/explanation content scrolls once in the shared workspace.
- Updated responsive phone/tablet rules and reduced-motion behavior without changing question data, vocabulary IDs, TTS defaults, Mock logic or IndexedDB schema.
- Consolidated documentation around one Master, Compatibility, Design System, Content Operations, Changelog and compact Project History. Release-specific notes rotate as previous + current only.
- Detailed record: `batches/TOEIC_SHARED_LEARNING_WORKSPACE_BATCH_019_v2.29.0.md`; verification: `reports/TEST_REPORT_TOEIC_Dictionary_v2.29.0.md`.

## Older release index

- **v2.28.0** — Vocabulary Batch 018; introduced the two-version release rotation and consolidated historical documentation.
- **v2.27.0** — Focus learning workspace and Vocabulary Batch 017.
- **v2.26.0** — Flashcard image relevance and responsive card layout.
- **v2.25.0** — Timed TOEIC Mock Practice Beta (15/60/120-minute modes).
- **v2.24.0** — Listening/TTS playback reliability hardening.
- **v2.23.0** — Part 1 photo QA hardening and Listening reserve content.
- **v2.22.0** — Licensed Part 1 photo integration and offline-safe image loading.
- **v2.21.0** — Legacy collocation cleanup and CI failure investigation.
- **v2.20.0** — Vocabulary examples, sense-linked POS and data-detail improvements.
- **v2.19.0** — Listening/Reading second-pass editorial review.
- **v2.18.0** — Responsive sidebar and Part 7 review.
- **v2.17.0** — Answer-position balance and choice-history migration safety.
- **v2.16.0** — Stable choice identity and CI failure isolation.
- **v2.15.1 / v2.15.0** — Reading/Grammar hotfix, CI maintenance and distractor audit.
- **v2.14.0–v2.11.0** — Design system, editorial evidence, question-pool expansion, TOEIC-only content operations.
- **v2.10.2–v2.9.1** — Vocabulary lexical audit, IPA/word-family work, definitions/examples, TTS and Flashcard refinements.

The complete historical inventory and retired-note mapping is maintained in `archive/PROJECT_HISTORY.md`.
