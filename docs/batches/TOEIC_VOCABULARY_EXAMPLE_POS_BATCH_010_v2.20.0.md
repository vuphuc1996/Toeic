# Vocabulary Example, Sense/POS Cards & Data Detail — Batch 010 (v2.20.0)

- **Date:** 2026-11-11
- **Baseline:** v2.19.0
- **Release:** v2.20.0
- **Scope:** canonical vocabulary examples, word-detail presentation, Data Workspace detail action and validator coverage.

## User requirements addressed

1. Make the English example and Vietnamese translation easier to read without overwhelming the word-detail layout.
2. Make clicking a vocabulary name in **Quản lý dữ liệu** open its detail view; preserve edit/create-personal/delete as separate actions.
3. Replace the repeated global POS strip plus repeated POS labels with one nested card per POS group. Put definitions, examples, relations and verb forms inside the appropriate group. Multiple senses sharing the same POS remain within one card.

## Implementation

- English examples use 13.25px text, Vietnamese translations 12px, 1.65 line-height and responsive spacing; reference examples in the vocabulary list are also enlarged.
- The detail view groups senses by POS. Examples are filtered by `sense_index`; same-POS senses are shown together. Verb forms are nested in the verb card rather than repeated as a separate redundant section.
- The Data Workspace table's delegated click handler now handles `[data-detail]` and opens the detail modal before the separate edit/delete branches.
- Runtime normalization preserves, validates and sorts `sense_index`; creating a personal copy preserves additional sense-linked examples.
- Vocabulary validator adds `EX010` for invalid/out-of-range example `sense_index` and `EX011` when a sense has no dedicated example.

## Corpus review and conservative data edits

- Reviewed the complete canonical set of **928 headwords** with structural/heuristic checks for example completeness, duplicate English strings, capitalization/punctuation, Vietnamese translation presence and headword traceability. These automated checks do not establish that every sentence is idiomatic or pedagogically optimal; this is not external TOEIC-teacher signoff.
- Rewrote **28** short examples to give fuller, contextualized TOEIC workplace usage.
- Added **26** sense-specific examples to the **25** multi-sense headwords (there are 51 senses in those records). Every canonical example now has a valid `sense_index`; every sense has at least one mapped example. Canonical example count is **954**.
- Corrected three duplicated cross-POS definition/meaning cases (`advocate`, `approximate`, `decline`), the Vietnamese rendering of `cashier`, and the adjective usage in `worldwide`.
- Stable headword IDs remain **928/928**; no vocabulary item was added or removed. The remaining eight validator warnings are legacy collocation/headword traceability warnings (FD001), not new EX010/EX011 issues.

## Preservation / safety

- No question IDs, question order, choice text/order, `answerIndex`, `choiceIds` or answer keys changed.
- No IndexedDB database version, object store or schema change. The app continues with the default local profile.
- Per the user's instruction, **no personal IndexedDB profile import/export, reset, inspection or migration test was performed**.
- V2.19.0 sidebar viewport-height correction and previous batches remain in the package.

## Tests

See `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.20.0.md` for exact counts. Vocabulary detail/data interaction tests and example-to-sense tests were added; validator rejects invalid `sense_index` and uncovered senses.

## Next gates

- Real browser and physical-device responsive verification, including the 15.6-inch laptop at 100% zoom, remains pending because the sandbox browser navigation was blocked.
- Independent TOEIC-teacher review remains pending; automated corpus checks are not a substitute.
- Personal IndexedDB import/migration QA remains deferred until the user requests it.
