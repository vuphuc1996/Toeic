# Answer Position Balance Regression — v2.95.41

## Defect

GitHub Actions failed `test_no_question_or_choice_identity_is_removed_by_reorder` because the test expected 161 Listening reserve questions; canonical data contained 193. The old test also carried a 263-question total that was no longer current.

## Root cause

v2.95.37 Batch 027 added 16 original-editorial Listening resources / 32 questions, all with `editorialStatus=reserve-pending-independent-review`: Part 2=8, Part 3=12, Part 4=12. The updated canonical Listening inventory has 145 units / 295 questions. The older assertion had not been updated after this batch.

## Current source-derived contract

| Part | Mock eligible | Pending independent review | Total |
|---|---:|---:|---:|
| Part 1 | 8 | 1 | 9 |
| Part 2 | 25 | 36 | 61 |
| Part 3 | 39 | 84 | 123 |
| Part 4 | 30 | 72 | 102 |
| **Total** | **102** | **193** | **295** |

Batch 027 additions: 16 resources / 32 questions (Part 2=8, Part 3=12, Part 4=12). Every Batch 027 item remains pending independent review and is excluded from Mock.

## Regression strengthening

`tools/tests/test_answer_position_balance.py` now:

- classifies eligible items only when status is absent or explicitly `approved-for-mock`;
- rejects unknown editorial statuses rather than counting them as eligible;
- checks eligible and pending counts per Part;
- checks the canonical 102 + 193 = 295 Listening inventory and 287 Reading total;
- checks exactly 16 Batch 027 reserve resources and 32 questions with the expected per-Part distribution;
- retains checks for choice lengths, unique choice IDs, valid answer indexes, all 27 historic key moves and answer-text/choice-ID identity following each option.

## Safety decision

No question, answer text, answer key/index, resource ID, choice ID, question order, editorial status, learner progress, IndexedDB, UI or Mock-eligibility source data was changed. The 32 new reserve questions remain Mock-excluded pending independent review. GitHub Actions already invoked this test module; CI coverage remains registered and passes.
