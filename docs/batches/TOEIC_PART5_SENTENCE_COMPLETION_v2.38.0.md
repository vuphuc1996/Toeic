# TOEIC Part 5 Sentence Completion — v2.38.0

## Scope

Add a separate adaptive practice mode for TOEIC Part 5-style incomplete sentences. This is not the same dataset as Reading Part 5 in `data/readings/reading-library.json`, and it is not part of the Mock Exam question pool.

## Inventory

- 35 original questions (`p5-sc-001` through `p5-sc-035`).
- 35 distinct existing canonical vocabulary targets; no new vocabulary headwords or vocabulary IDs.
- Every question contains exactly one `_____` blank, four unique choices, one answer index, four option-specific explanations, grammar point, full rationale, Vietnamese translation and a single-answer explanation.
- Topics cover office administration, logistics, HR/recruitment, procurement, finance, customer service, facilities and general business operations.
- The item bank is `data/practice/part5-sentence-completion.json`; the runtime selector is `assets/js/sentence-completion.js`.

## Learning behavior

- Appears as `TOEIC Part 5 · Điền từ` in the existing Review mode picker and mode dropdown.
- Uses the shared Focus Workspace, A–D choice buttons, answer-review modal, option-specific feedback, existing auto-next and vocabulary progress scheduler.
- The selector weights questions using the linked word's existing due/weak/new practice state. It presents unseen question IDs first and cycles after the unique question bank has been seen.
- Choice shuffling preserves the mapping between each choice and its explanation.
- Part 5 question history is isolated in optional `sentenceCompletionSeenIds` within the existing `practiceSession` object. Other practice modes keep using `sessionSeenIds`. Correct/incorrect outcomes still update `studyProgress` using the canonical `wordId`.
- The displayed counter reports questions seen, not vocabulary words seen.

## Content examples

`The purchasing department plans to _____ additional laptops before the new employees arrive.`

A. order · B. ordering · C. ordered · D. orders

Key: A. `plans to + base form`; the procurement context supports `order` and the distractors have the wrong verb form.

## Editorial status and limitations

- All 35 questions are original project-authored practice items, not copied ETS questions.
- Bank-level and item-level status remains `reserve-pending-independent-review` with `internal-author-check; independent-second-review-pending`.
- Internal author checks, structural validators and automated selector tests do not constitute independent second-person review. Do not promote this bank to Mock.
- There is one keyed answer per record, but naturalness and semantic uniqueness still require a second reviewer before the bank can be marked fully reviewed.

## Compatibility

- IndexedDB remains `toeic-vocabulary-phase1`, version 1, store `workspace`.
- `sentenceCompletionSeenIds` is an optional additive property in the existing `practiceSession` payload; old sessions without this property restore as an empty list.
- No schema migration, learner-profile reset/import/export/inspection, canonical vocabulary change or Reading/Listening/Grammar question-bank change.
- Added `assets/js/sentence-completion.js` and `data/practice/part5-sentence-completion.json` to both Service Worker `REQUIRED` and `APP_SHELL`.

## Targeted verification

- Python content suite: 8/8 passed.
- PWA readiness suite: 3/3 passed.
- CI coverage suite: 2/2 passed.
- JavaScript sentence selector, Focus Workspace, practice-progress and runtime-render regression suites passed.
- Data validator: 992 vocabulary records, 0 errors and 0 warnings (legacy-only baseline warning).
- Learning-content validator: 0 errors; 8 existing Part 1 JPGs absent from this source snapshot, with SVG fallbacks available.
- These are local checks, not a remote GitHub Actions/Pages run or physical-device acceptance.
