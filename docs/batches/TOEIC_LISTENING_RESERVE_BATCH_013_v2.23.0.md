# TOEIC Listening Reserve Content — Batch 013 — v2.23.0

- **Date:** 2026-11-11
- **Base:** v2.22.0 Part 1 photo-path integration, carried into v2.23.0
- **Scope:** 11 original-authored reserve questions across Listening Parts 2–4
- **Status:** Structurally validated; pending independent TOEIC editorial review. These items are excluded from the prior answer-position and distractor quality certificate until reviewed.

## Items added

| Part | Unit ID | Questions | Primary skill |
|---|---|---:|---|
| Part 2 | `part2-monitor-delivery-arrival` | 1 | Yes/no status and delivery timing |
| Part 2 | `part2-revised-budget-approval` | 1 | WH-question asking for a person |
| Part 2 | `part2-visitor-parking` | 1 | WH-question asking for a location |
| Part 2 | `part2-training-session-reschedule` | 1 | Polite request / acceptance |
| Part 2 | `part2-customer-survey-sent` | 1 | Negative question / completed action |
| Part 3 | `part3-training-handouts` | 3 | Delayed material, event timing, alternative distribution |
| Part 4 | `part4-east-elevator-maintenance` | 3 | Workplace announcement, facility, schedule and instruction |
| **Total** | **7 units** | **11** | — |

## Pool after Batch 013

| Part | Units | Questions | Reference form |
|---|---:|---:|---:|
| Part 1 | 8 | 8 | 6 |
| Part 2 | 30 | 30 | 25 |
| Part 3 | 14 | 42 | 39 |
| Part 4 | 11 | 33 | 30 |
| **Listening** | **63** | **113** | **100** |

The pool has 13 Listening questions beyond the first-form blueprint selection. The reserve questions are for repeat practice and future forms; they are not a claim that a second independent 100-question Listening form is complete or validated.

## Editorial and identity safeguards

- All new items carry `contentBatch: "batch-013-listening-reserve"` and `editorialStatus: "reserve-pending-independent-review"`.
- Part 2 items use three answer choices. Part 3 and Part 4 use four choices and exactly three questions per set.
- New question IDs and `choiceIds` are unique. Each key is structurally valid and has a Vietnamese rationale.
- These questions are excluded from the 132-question historic Part 3/4/7 distractor/answer-position certificate. A dedicated structural check confirms distinct choices and valid answer indexes. They must undergo independent human review before inclusion in a scored Full Mock or any answer-position-balance certification.
- The old 148-question v2.19 second-pass registry remains intact through per-question SHA-256 fingerprints plus per-unit content fingerprints; five approved Part 1 transcript/visual-alignment edits are explicitly permitted. The registry fails on unapproved edits to historical questions or unit-level transcript/translation/source metadata. Any new question outside the registry must be marked reserve-pending-independent-review.

## Existing Part 1 photo alignment

Two statements were made more precise against the Pexels source descriptions:

- `part1-warehouse-box` (key B): “A worker is organizing cartons on a warehouse shelf.”
- `part1-technician-inspection` (key C): “A technician is repairing an air-conditioning unit outdoors.”

The Part 1 key distribution remains A/B/C/D = 0/1/2/3 twice. No Part 1 question ID, answer index, choice text/order or `choiceIds` changed.

## Explicit limitations

- No external TOEIC teacher signoff has been performed for these 11 reserve questions.
- The user’s Pexels JPG binaries were not present in the working snapshot. Source-page descriptions and attribution mapping were reviewed, but binary-level visual matching and strict JPG validation remain pending.
- No personal IndexedDB data was imported, exported, inspected, reset or migrated. Database schema/version/store remain unchanged.
