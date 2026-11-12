# TOEIC Distractor & Answer-Uniqueness Audit — v2.16.0

## Scope and method
- Reviewed **132 questions** across Listening Part 3 (39), Listening Part 4 (30) and Reading Part 7 (63). This covers the 126 direct/lexical evidence pointers and six paraphrase/inference items identified in the v2.14.0 evidence map.
- Each question was examined with its full transcript or passage, keyed option and all three distractors. Review criteria: source support for the key, exactly one defensible answer, grammatical/semantic fit to the prompt, plausibility of distractors, and whether alternatives draw on realistic confusions or nearby details.
- Structural checks in this script verify four distinct options and a valid key. They do **not** certify semantic uniqueness by algorithm and are not a substitute for a second human reviewer or psychometric analysis.

## Reviewed coverage
| Library | Part | Sets | Questions |
|---|---|---:|---:|
| Listening | Part 3 | 13 | 39 |
| Listening | Part 4 | 10 | 30 |
| Reading | Part 7 | 24 | 63 |

### Question sets included
| Library | Set ID | Questions reviewed |
|---|---|---:|
| Listening | `part3-shipping-delay` | 3 |
| Listening | `part3-business-trip` | 3 |
| Listening | `part3-interview-schedule` | 3 |
| Listening | `part3-invoice-error` | 3 |
| Listening | `part3-facility-repair` | 3 |
| Listening | `part3-budget-review` | 3 |
| Listening | `part3-interview-arrangement` | 3 |
| Listening | `part3-software-upgrade` | 3 |
| Listening | `part3-client-presentation` | 3 |
| Listening | `part3-procurement-quotation` | 3 |
| Listening | `part3-hotel-reservation` | 3 |
| Listening | `part3-marketing-campaign` | 3 |
| Listening | `part3-elevator-maintenance` | 3 |
| Listening | `part4-office-announcement` | 3 |
| Listening | `part4-conference-update` | 3 |
| Listening | `part4-safety-announcement` | 3 |
| Listening | `part4-product-launch` | 3 |
| Listening | `part4-quarterly-town-hall` | 3 |
| Listening | `part4-customer-voicemail` | 3 |
| Listening | `part4-warehouse-safety-briefing` | 3 |
| Listening | `part4-training-registration` | 3 |
| Listening | `part4-travel-service-update` | 3 |
| Listening | `part4-quarterly-inventory-report` | 3 |
| Reading | `office-schedule` | 3 |
| Reading | `meeting-notice` | 3 |
| Reading | `business-travel` | 3 |
| Reading | `invoice-payment` | 3 |
| Reading | `shipping-update` | 3 |
| Reading | `job-opening` | 3 |
| Reading | `customer-service` | 3 |
| Reading | `facility-maintenance` | 3 |
| Reading | `customer-refund-email` | 1 |
| Reading | `facility-maintenance-notice` | 1 |
| Reading | `job-posting-analyst` | 1 |
| Reading | `supplier-invoice-followup` | 1 |
| Reading | `travel-itinerary` | 1 |
| Reading | `double-passage-order` | 1 |
| Reading | `training-announcement` | 1 |
| Reading | `triple-passage-meeting` | 1 |
| Reading | `part7-single-equipment-memo` | 4 |
| Reading | `part7-single-training-email` | 4 |
| Reading | `part7-double-order-delay` | 4 |
| Reading | `part7-triple-conference-arrangements` | 5 |
| Reading | `part7-double-equipment-order` | 4 |
| Reading | `part7-double-training-reimbursement` | 4 |
| Reading | `part7-triple-regional-sales-meeting` | 3 |
| Reading | `part7-triple-facility-renovation` | 3 |

## Twelve distractor revisions applied
| Library / set / question | Editorial change |
|---|---|
| Listening · `part3-hotel-reservation` · Q1 | Replaced unrelated hotel-service alternatives with other plausible booking requests. |
| Listening · `part3-client-presentation` · Q3 | Aligned all alternatives with realistic presentation-preparation actions. |
| Listening · `part4-training-registration` · Q1 | Aligned alternatives as plausible employee groups. |
| Reading · `business-travel` · Q2 | Made all alternatives plausible travel records while keeping reimbursement evidence unique. |
| Reading · `customer-refund-email` · Q1 | Replaced the unrelated hotel refund with realistic keyboard/order-resolution requests. |
| Reading · `supplier-invoice-followup` · Q1 | Aligned alternatives with common invoice/payment verification issues. |
| Reading · `double-passage-order` · Q1 | Replaced off-topic alternatives with plausible causes of a shipment delay. |
| Reading · `part7-double-equipment-order` · Q1 | Aligned alternatives with realistic supplier/order enquiries. |
| Reading · `part7-single-training-email` · Q1 | Aligned alternatives as plausible employee audiences. |
| Reading · `training-announcement` · Q1 | Aligned alternatives as internal employee groups. |
| Reading · `part7-triple-regional-sales-meeting` · Q1 | Aligned alternatives with plausible meeting materials. |
| Reading · `part7-triple-facility-renovation` · Q3 | Aligned alternatives with plausible visitor-access arrangements. |

## Answer-position distribution — retained, not shuffled
| Part | A | B | C | D | Total |
|---|---:|---:|---:|---:|---:|
| Part 3 | 10 | 18 | 10 | 1 | 39 |
| Part 4 | 9 | 12 | 7 | 2 | 30 |
| Part 7 | 13 | 27 | 19 | 4 | 63 |

**Important finding:** answer positions are currently uneven, especially D in Part 3/4/7. They were deliberately not shuffled in this release because `readingProgress` and `listeningProgress` currently persist `choiceIndex` (A/B/C/D index) against question order. Reordering choices without a stable choice identity and migration would make previously saved answers appear to point at a different option. A future release must first add stable `choiceId`/choice-text persistence and a legacy progress migration, then rebalance answer positions with regression tests.

## Quality decision and remaining limitations
- The 12 revised groups now use distractors closer to the same document purpose, role, travel record, service request, business action or visitor-access context. The correct answer text and `answerIndex` were kept unchanged for every revised question.
- Other reviewed groups were retained where the three alternatives are distinct and the transcript/passage supports one clear key. In particular, close dates/times, locations, meeting materials and process steps remain useful distractors when they are contradicted or not supported by the source.
- This is editorial review of original-authored content. It is not official ETS content, two-person independent review, statistical item analysis, difficulty calibration or proof of score equivalence.
- Part 1 remains SVG illustration-based; Listening audio remains browser SpeechSynthesis. Physical-device audio/voice review is still pending.
