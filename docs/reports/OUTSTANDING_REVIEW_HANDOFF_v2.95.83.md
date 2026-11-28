# Outstanding Independent Review Handoff — TOEIC Dictionary v2.95.83

**Purpose:** traceable human-review queue for the two remaining outcome gaps. This handoff is not editorial approval or learner evidence.

## Listening Part 1 — visual verification and paraphrase recognition

- Objective remains `mixed_or_pending_review_check_item_level`. Eight non-reserve resources have photo assets but lack item-level independent visual sign-off. `part1-office-cleaning` remains reserve-pending.
- No Part 1 paraphrase mapping is added and the 10-item minimum is not relaxed.

| Resource ID | Image | Source | Reviewer check |
|---|---|---|---|
| `part1-meeting-documents` | `assets/listening/part1-meeting-documents.jpg` | licensed-stock | Verify visible action/subject against all four descriptions and confirm attribution |
| `part1-warehouse-box` | `assets/listening/part1-warehouse-box.jpg` | licensed-stock | Verify carton/shelving action and distractor-image mismatch |
| `part1-technician-inspection` | `assets/listening/part1-technician-inspection.jpg` | licensed-stock | Verify technician, outdoor unit and repair action |
| `part1-airport-suitcase` | `assets/listening/part1-airport-suitcase.jpg` | licensed-stock | Verify traveler, suitcase and terminal context |
| `part1-presentation-room` | `assets/listening/part1-presentation-room.jpg` | licensed-stock | Verify empty conference room and presentation screen |
| `part1-reception-plant` | `assets/listening/part1-reception-plant.jpg` | licensed-stock | Verify visible watering action and plant placement |
| `part1-restaurant-setting` | `assets/listening/part1-restaurant-setting.jpg` | licensed-stock | Verify table-setting action, not paying/cleaning/moving tables |
| `part1-photocopier` | `assets/listening/part1-photocopier.jpg` | licensed-stock | Verify employee operating a photocopier |
| `part1-office-cleaning` | `assets/listening/part1-office-cleaning.jpg` | ai-generated | Still reserve-pending; independent visual/provenance review required |

Review output must record visible subject/action, distractor-image mismatch and source/provenance confirmation. Alt text alone is not sufficient evidence.

## Reading Part 7 — independent second-review queue

- Parent gate remains `part7_expansion_requires_second_review`.
- Six resources (24 questions) have `internal-editorial-reviewed` status but still require an independent second reviewer. Twenty-two reserve resources and twenty-four resources without item-level review status remain gated.
- No Part 7 paraphrase/inference mapping or Mock promotion occurs in this batch.

| Resource ID | Question key | Intent | Existing source cue |
|---|---|---|---|
| `part7-single-vendor-delivery-calendar` | `reading:part7-single-vendor-delivery-calendar:1` | Notice purpose | Final office-supply deliveries for the year |
| `part7-single-safety-procedure-update` | `reading:part7-single-safety-procedure-update:1` | Memo purpose | Marked pedestrian lanes and revised warehouse routes |
| `part7-double-vendor-credit` | `reading:part7-double-vendor-credit:1` | Reason / inference | Fabric color did not match approved sample |
| `part7-double-vendor-credit` | `reading:part7-double-vendor-credit:5` | Business-policy inference | Delivery charge excluded because order was delivered as scheduled |

Second reviewer must independently validate document support, paraphrase quality, inference scope, distractor plausibility, answer key and quote-to-document matching. No review status is inferred from this queue.

## Protected boundaries

- Part 1 and Part 7 remain uninstrumented; their review gates stay active.
- Ten new Part 4 questions are practice-only and Mock-excluded.
- Listening reserve 193, Reading Part 7 reserve 87 and Separate Part 5 review-only 80 remain Mock-excluded.
