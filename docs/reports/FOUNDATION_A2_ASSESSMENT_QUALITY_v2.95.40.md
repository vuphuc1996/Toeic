# Foundation A2 Assessment Quality Pass — v2.95.40

## Scope
- 13 core A2 Reading resources + 13 core A2 Listening resources; the new 13 supplementary A2 Listening clips (39 questions) are separately scoped and pending independent review.
- Focused review of within-resource q2/q3 repetition, answer-key uniqueness, four-choice integrity and explicit source traceability for changed/retained focus questions.
- Five question prompts/answer tasks were materially revised; six reviewed question records now carry exact source-evidence pointers.

## Automated integrity results
| Bank | A2 resources | A2 questions | A2 answer positions A/B/C/D |
|---|---:|---:|---:|
| Reading | 13 | 39 | 10 / 10 / 10 / 9 |
| Listening | 13 | 39 | 10 / 10 / 10 / 9 |

- All A2 questions require four unique choices, a valid answer index, a non-empty prompt and rationale.
- Each A2 resource must have three questions with non-identical q2/q3 correct answers.
- Each source-evidence pointer is checked as an exact substring of its Reading passage or spoken Listening segment.
- Core Reading answer positions remain A/B/C/D = 15/15/15/14; Listening full bank including supplementary practice is A/B/C/D = 25/25/24/24.
- Existing A2 q1/q2 objects remain protected by the v2.75.0 canonical-hash baseline tests.

## Focused changes
| Question | Change |
|---|---|
| `a2-quantities::reading1::q3` | Replaced q3 with a consequence/inference question about the delivery timing and preparation of training materials. |
| `a2-comparisons::reading1::q3` | Replaced q3 with an inference about the customer's priority: dependable, on-time delivery versus lowest price. |
| `a2-obligation-permission::reading1::q3` | Replaced q3 with the separate departure requirement to return the visitor badge. |
| `a2-comparisons::listening1::q3` | Reworded q3 to test the stated reliability/on-time advantage; q2 remains byte-identical to the v2.75.0 baseline. |
| `a2-sequencing-instructions::listening1::q3` | Replaced q3 with the immediately preceding action before preparing the return label. |

## Review boundary
- The pass fixes five identified cases of repeated information and records six exact source pointers. It does not certify every distractor for semantic plausibility or uniqueness.
- The work is an internal single-author review. Independent second-person language review and psychometric validation remain pending.
- The local A2 three-question / 67% rule is a practice threshold only; it is not a CEFR standard, mastery declaration or ETS equivalence.

## Automated audit status
- **PASS** — all registered structural, source-evidence, pair-distinction and answer-position checks passed.
