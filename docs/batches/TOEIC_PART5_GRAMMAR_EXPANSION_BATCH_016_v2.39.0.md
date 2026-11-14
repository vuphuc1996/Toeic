# TOEIC Part 5 Grammar and Structure Expansion — Batch 016 — v2.39.0

## Scope

Extend the separate adaptive TOEIC Part 5-style sentence-completion practice bank from 35 to 80 questions. Batch 016 contributes 45 original project-authored questions (`p5-sc-036` through `p5-sc-080`). It does not modify the official Reading Part 5 bank, Mock Exam inventory or vocabulary headword list.

## Inventory and structure

- Core bank: 35 questions (`p5-sc-001`–`p5-sc-035`).
- Batch 016: 45 additional questions (`p5-sc-036`–`p5-sc-080`).
- Total: 80 questions, 80 unique question IDs and 80 unique links to existing canonical vocabulary IDs.
- Every record has one blank, four distinct choices, one answer index, four option-aligned explanations, grammar category, grammar point, full answer explanation, Vietnamese translation and a single-answer rationale.
- Answer-key position distribution across the 80 records is A/B/C/D = 20/20/20/20. Runtime shuffling retains the option-to-explanation mapping.
- All 80 questions use original project-authored content and remain `reserve-pending-independent-review`.

## Grammar-group coverage

| Grammar group | Questions | Example focus |
|---|---:|---|
| Adjectives and Adverbs | 10 | adjective after linking verb; adjective before noun; frequency adverb |
| Articles and Determiners | 3 | a/an with count nouns; determiners and noun forms |
| Conjunctions and Clauses | 3 | because/before; relative clause connectors |
| Gerunds and Infinitives | 3 | consider + V-ing; spend time + V-ing |
| Imperatives and Verb Forms | 1 | direct instruction / base-form command |
| Infinitives and Verb Patterns | 13 | require/plan/designed to + base form |
| Linking Verbs | 1 | remain + adjective |
| Modal Verbs | 2 | modal + base form |
| Participles and Reduced Relative Clauses | 1 | present participle modifying a noun |
| Passive Voice | 5 | modal/passive; present and past passive |
| Prepositions and Collocations | 13 | adjacent to; participate in; prevent from; notify of |
| Subject–Verb Agreement | 7 | singular department/software; neither…nor; number of |
| Verb Tense and Aspect | 8 | past simple; future/past perfect; present perfect continuous |
| Word Forms and Nouns | 10 | noun, adjective and other form discrimination |


## Topics represented

Office administration, finance, procurement, travel/transportation, recruitment and human resources, technology, e-commerce, workplace safety, warehouse/logistics, facilities/maintenance, legal and project management.

## Editorial refinements made during author pass

- Removed `for` as a distractor in the `beneficial to` item because `beneficial for` is also valid English in many contexts.
- Removed `about` as a distractor in the `notify someone of` item because `notify someone about` can also be valid.
- Reframed a supplier-contact item around `purpose of + V-ing` to make the gerund requirement explicit.
- Reframed the room-reservation item around `keep available for` so the beneficiary meaning is explicit rather than conflated with a passive agent introduced by `by`.
- Rebalanced the stored answer keys after choice swaps and preserved each option's matching explanation.

## Runtime behavior

- The existing Focus Workspace displays the grammar group and sentence, and the answer-review panel repeats the grammar group, rule, Vietnamese translation and single-answer rationale.
- Part 5 question history remains keyed by question ID in `sentenceCompletionSeenIds`; it is not mixed with the legacy vocabulary `sessionSeenIds`.
- Existing adaptive weighting uses the linked vocabulary item's due/weak/new progress. Correct/incorrect outcomes still update the existing `studyProgress` record.
- No new screen, database, storage migration or Service Worker path was required. Existing `REQUIRED` and `APP_SHELL` entries cover the Part 5 JS module and JSON bank.

## Editorial status and review boundary

- Core 35 + Batch 016 45 = 80 items, all `reserve-pending-independent-review`.
- The internal author re-check addressed obvious alternative-preposition and form-selection ambiguity, but this is not an independent second-person review.
- Structural validation, option-key alignment, answer-position balancing and runtime tests do not prove semantic uniqueness or naturalness for every question.
- Keep the bank practice-only and excluded from Reading Mock until a second reviewer records a decision for every item.

## Compatibility

- Vocabulary headwords remain 992; no canonical vocabulary IDs are added or changed.
- Reading remains 200 questions, including 60 official Reading Part 5 questions; this separate practice bank is not counted in Reading coverage or Mock.
- IndexedDB remains `toeic-vocabulary-phase1` version 1, store `workspace`; no profile reset or migration.
- Listening, Reading, Grammar lesson data, Mock blueprint, TTS, Retry and Attempt History are otherwise unchanged.
