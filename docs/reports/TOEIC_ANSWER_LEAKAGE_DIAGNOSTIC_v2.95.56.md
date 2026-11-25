# TOEIC Answer Leakage & Distractor Overlap Diagnostic — v2.95.56

## Purpose and safety boundary
- Read-only triage of question-stem lexical cueing, correct-answer/distractor lexical similarity, and keyed-answer length imbalance.
- A flag is a review signal, **not evidence of a wrong key, answer leakage, or an invalid item**. TOEIC questions legitimately reuse vocabulary and paraphrase source evidence.
- No automatic rewriting, key changes, choice reordering, eligibility promotion, or reserve approval is performed.
- Scope: Mock-eligible Listening Part 3/4 and Reading Part 7 only. Listening reserve-pending-independent-review remains excluded.

## Part summary
| Part | Questions | Flagged questions | Stem cue | Key/distractor overlap | Key long | Key short |
|---|---:|---:|---:|---:|---:|---:|
| Part 3 | 39 | 2 | 0 | 0 | 2 | 0 |
| Part 4 | 30 | 1 | 0 | 0 | 1 | 0 |
| Part 7 | 195 | 6 | 0 | 1 | 5 | 0 |

## Flagged question review queue
| Part / set / question | Signal(s) | Stem | Keyed answer | Stem overlap | Key/distractor Jaccard | Key words / distractor median |
|---|---|---|---|---:|---:|---:|
| Part 3 · `part3-invoice-error` · Q3 | KEY_UNUSUALLY_LONG | When is payment due to be processed? | By the end of the week | 0% | 0% | 6 / 2 |
| Part 3 · `part3-budget-review` · Q2 | KEY_UNUSUALLY_LONG | What will the man do this afternoon? | Update a spreadsheet and send a revised copy | 0% | 0% | 8 / 4 |
| Part 4 · `part4-training-registration` · Q3 | KEY_UNUSUALLY_LONG | When will confirmation emails be sent? | Within two business days after the deadline | 0% | 0% | 7 / 3 |
| Part 7 · `facility-maintenance` · Q2 | KEY_UNUSUALLY_LONG | Which area may have limited access? | The east wing on the fourth floor | 0% | 17% | 7 / 3 |
| Part 7 · `double-passage-order` · Q5 | KEY_UNUSUALLY_LONG | Why are the items needed soon? | A product launch is scheduled for the following week | 0% | 0% | 9 / 5 |
| Part 7 · `part7-triple-regional-sales-meeting` · Q5 | KEY_UNUSUALLY_LONG | What is planned for the afternoon? | One-to-one discussions with the sales director | 0% | 0% | 8 / 4 |
| Part 7 · `part7-double-delivery-reschedule` · Q3 | KEY_UNUSUALLY_LONG | Why is there no additional charge? | The request was made more than three business days in advance | 0% | 0% | 11 / 6 |
| Part 7 · `batch025-part7-double-conference-booking` · Q3 | KEY_DISTRACTOR_HIGH_OVERLAP | Which room does the product team request? | Training Room 2 | 50% | 100% | 3 / 3 |
| Part 7 · `batch026-part7-schedule-email` · Q3 | KEY_UNUSUALLY_LONG | What should employees do by Thursday? | Contact HR if unable to work the new hours | 0% | 0% | 9 / 4 |

## Metric definitions
- **Stem overlap** = content-word intersection between the keyed answer and question stem divided by keyed-answer content words.
- **Key/distractor Jaccard** = intersection-over-union of content-word sets for the keyed answer and each distractor; report stores the maximum.
- **Length ratio** = keyed-answer word count divided by median distractor word count.
- Stopwords are removed; tokens are case-folded. This deliberately simple lexical model cannot detect semantic paraphrase, negation scope, audio prosody, visual evidence, or discourse inference.
- Thresholds are conservative triage heuristics: keyed stem overlap ≥60% and ≥30 percentage points above distractors; key/distractor Jaccard ≥75%; length outlier requires ≥4 words and ≥1.8× median.

## Decision
- Do not auto-edit flagged items. Review the original audio/transcript or passage, evidence quote, explanation, and all four options together. Preserve answer keys unless a human editorial review proves a defect.
- This report is deterministic for the same source bytes and is not an ETS benchmark, psychometric analysis, or certification of answer uniqueness.
