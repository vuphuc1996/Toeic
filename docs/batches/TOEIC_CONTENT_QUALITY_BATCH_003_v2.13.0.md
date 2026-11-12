# TOEIC Content Quality & Dashboard Layout — Batch 003 (v2.13.0)

- **Date:** 2026-11-10
- **Baseline:** v2.12.0
- **Scope:** TOEIC-only; 211-question practice pool and dashboard diagnostics presentation.
- **Non-goals:** no new question/resource IDs; no new vocabulary headwords; no IndexedDB schema change; no mock engine or IELTS content.

## Dashboard / layout

- Removed the generic `panel` class from `#toeicProgressPanel`; the diagnostics heading no longer renders as one large boxed card.
- Introduced a clearer hierarchy: `TOEIC LEARNING DIAGNOSTICS` eyebrow, `Tiến độ theo 7 Parts` H2, concise explanation and `TOEIC L&R` context label.
- Split content into Listening Parts 1–4 and Reading Parts 5–7 groups with separate labels and exam-form counts.
- Kept individual Part buttons framed and interactive; the priority recommendation is a light, left-accented note rather than another heavy card.
- Preserved local analytics calculation, click-to-filter behavior, `role="status"`, `aria-live="polite"`, visible keyboard focus and responsive tablet/mobile breakpoints.

## Listening edits

- All 8 Part 1 prompts now refer to an `illustration`, matching the current SVG assets and `visualType=illustration` provenance. The runtime variable and CSS frame class were also renamed from “photo” to “illustration”. The items are not described as photographs.
- Retained image-specific Vietnamese rationales that explicitly name the correct A/B/C/D option.
- Updated the Part 2 invoice-approval distractors to remove two choices that repeated the same page-two clue.
- Reworded the supplier-samples tag question and answer to make the confirmation (“They did…”) explicit instead of relying on a potentially confusing bare “Yes”.
- Made selected Part 3/4/2 explanations more complete and clearly Vietnamese; existing 38 Part 3/4 explanations previously in English remain localized.

## Reading edits

- Localized the remaining legacy English question explanations into Vietnamese, including the analyst-position question.
- Strengthened short explanations in selected Part 5, Part 6 and Part 7 questions so the learner sees the clue or grammatical reason rather than only a copied answer phrase.
- No passage, question ID, answer index or choice order was intentionally changed.

## Preservation and scope

- Vocabulary remains 928 records / 928 stable IDs / 26 A–Z files.
- Listening remains 56 units / 102 questions; Reading remains 35 resources / 109 questions; Grammar remains 25 lessons / 54 exercises.
- No personal-progress migration, local storage key or IndexedDB schema change.
- No ETS question, passage or audio is included. Browser TTS and SVG illustrations keep their existing provenance labels.

## QA gates

- `test_learning_content.py` adds checks for Vietnamese connective/explanatory wording (an accented English token alone is insufficient), Part 1 illustration labeling/rendering semantics and Part 2 invoice distractor separation.
- `test_dashboard_layout.py` adds static checks for section unboxing, hierarchy, independent Listening/Reading mount points, responsive breakpoints, keyboard focus and accessible status announcements.
- GitHub Actions now runs the dashboard layout test module too.
- Automated tests validate structure and selected editorial invariants; they do not constitute third-party proofreading or final semantic signoff of every answer.
