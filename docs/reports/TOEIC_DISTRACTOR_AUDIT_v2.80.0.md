# TOEIC Distractor & Answer-Uniqueness Audit — v2.80.0

## Scope and method
- Scope covers **177 questions** across Listening Part 3 (39), Listening Part 4 (30) and Reading Part 7 (108). The 63-question historical Part 7 review baseline remains traceable in Project History. The 45 new Part 7 questions in v2.33.0 include source-label/quotation evidence and passed structural key/choice checks; they are not represented as independently reviewed or covered by the historical 132-item semantic distractor certificate.
- The historical 132-item semantic review was performed against full transcripts/passages, keyed options and distractors. For the v2.33 additions, this release adds traceable source quotes, answer-key checks, four-distinct-choice checks, stable choice IDs and balanced answer positions. Semantic distractor uniqueness for new items still requires second-person review.
- Structural checks in this script verify four distinct options and a valid key. They do **not** certify semantic uniqueness by algorithm and are not a substitute for a second human reviewer or psychometric analysis.

## Reviewed coverage
| Library | Part | Sets | Questions in audit scope |
|---|---|---:|---:|
| Listening | Part 3 | 13 | 39 |
| Listening | Part 4 | 10 | 30 |
| Reading | Part 7 | 30 | 108 |

### Question sets included
| Library | Set ID | Questions in audit scope |
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
| Reading | `customer-refund-email` | 2 |
| Reading | `facility-maintenance-notice` | 2 |
| Reading | `job-posting-analyst` | 2 |
| Reading | `supplier-invoice-followup` | 2 |
| Reading | `travel-itinerary` | 2 |
| Reading | `double-passage-order` | 5 |
| Reading | `training-announcement` | 2 |
| Reading | `triple-passage-meeting` | 5 |
| Reading | `part7-single-equipment-memo` | 4 |
| Reading | `part7-single-training-email` | 4 |
| Reading | `part7-double-order-delay` | 5 |
| Reading | `part7-triple-conference-arrangements` | 5 |
| Reading | `part7-double-equipment-order` | 5 |
| Reading | `part7-double-training-reimbursement` | 5 |
| Reading | `part7-triple-regional-sales-meeting` | 5 |
| Reading | `part7-triple-facility-renovation` | 5 |
| Reading | `part7-single-vendor-delivery-calendar` | 4 |
| Reading | `part7-single-safety-procedure-update` | 4 |
| Reading | `part7-single-contract-renewal-notice` | 3 |
| Reading | `part7-single-facility-reservation` | 3 |
| Reading | `part7-double-vendor-credit` | 5 |
| Reading | `part7-triple-conference-exhibitor-logistics` | 5 |

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

## Answer-position distribution — balanced with stable choice identity
| Part | A | B | C | D | Total |
|---|---:|---:|---:|---:|---:|
| Part 3 | 10 | 10 | 10 | 9 | 39 |
| Part 4 | 8 | 8 | 7 | 7 | 30 |
| Part 7 | 27 | 27 | 27 | 27 | 108 |

**Rebalancing method:** 27 question groups had only the keyed option exchanged with a distractor position: 8 in Part 3, 5 in Part 4 and 14 in Part 7. The answer text, source evidence, explanation, question IDs and question order were retained. Each changed question carries `previousChoices` and `previousChoiceIds` from v2.16.0; the matching `choiceIds` moved with the option. At startup, progress containing a v2.16 `choiceId` is relocated to its new index; older records without an ID are mapped through the v2.16 snapshot. The prior index is preserved in `previousChoiceIndex`. No random shuffle was used.

## Quality decision and remaining limitations
- The 12 revised groups now use distractors closer to the same document purpose, role, travel record, service request, business action or visitor-access context. The correct answer text and `answerIndex` were kept unchanged for every revised question.
- Historical reviewed groups were retained where the three alternatives are distinct and the transcript/passage supports one clear key. For the new v2.33 Part 7 groups, close dates/times, locations, delivery steps and document-purpose alternatives were authored to be plausible, but an independent reviewer must confirm that exactly one option is defensible.
- Listening reserve total: 99 questions across 51 units. This script structurally checks Part 3/4 reserve blocks; Part 2 response-fit is tracked separately. Structural checks never approve a reserve for Mock.
- This is editorial review of original-authored content. It is not official ETS content, two-person independent review, statistical item analysis, difficulty calibration or proof of score equivalence.
- Part 1 uses source-tracked licensed Pexels and AI-generated photographs with a JPG-only runtime contract; Listening audio remains browser SpeechSynthesis. Physical-device audio/voice review is still pending.
