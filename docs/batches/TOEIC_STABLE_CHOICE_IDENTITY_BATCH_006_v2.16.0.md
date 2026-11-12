# Batch 006 — Stable Choice Identity & CI Failure Isolation (v2.16.0)

## Scope
- Stable option identifiers for Reading, Listening and Grammar.
- Backward-compatible progress migration from `choiceIndex` to additive `choiceId`.
- Split GitHub Actions unit-test suites into separately visible steps.

## Data changes
- Reading: 109 question records receive `choiceIds` arrays.
- Listening: 102 question records receive `choiceIds` arrays.
- Grammar: 54 exercise records receive `choiceIds` arrays.
- IDs are deterministic and option-position-specific. Duplicate option text retains distinct IDs. The 12 question sets revised in v2.15.0 have separate `legacyChoiceIds` to represent archived option text independently from the replacement distractors.

## Runtime changes
- Startup migration adds `choiceId` to valid historical answers while preserving `choiceIndex`, `choiceText`, `correct` and `answeredAt`.
- New answers persist `choiceId` and `choiceText` in all three learning areas.
- No IndexedDB schema/object-store migration or progress reset.

## Safety boundary
No answer choices have been reordered. Do not balance answer positions until migration and editorial reorder review have passed.

## Verification
See `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.16.0.md`. Remote GitHub Actions is pending a new push/run; a one-line historical annotation is insufficient to identify the original failing assertion.
