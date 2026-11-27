# TOEIC 7-Part Content Quality & Answer-Evidence Audit — v2.95.75

Generated: 2026-11-27 · Read-only deterministic audit (source SHA-256 verified unchanged).

## 1. Epistemic Boundaries & Status Separation

- **`APPROVED_FOR_MOCK` (legacy eligible / `internal-editorial-reviewed`)**: **102 Listening** + **200 Reading** = **302 questions**. Eligible for local Mock sampling; reflects internal repository review only — **not** two-person independent certification or official ETS equating.
- **`HUMAN_REVIEW_REQUIRED` (`reserve-pending-independent-review`)**: **193 Listening** + **87 Reading Part 7** + **80 Separate Part 5** = **360 questions**. Explicitly excluded from Mock; automated structural passes never promote reserve items.
- **`PRACTICE_SUPPORT` (Grammar)**: **58 lessons / 169 exercises** supporting Parts 5 & 6 learning only.
- **`AI_TRIAGE / STRUCTURAL`**: Automated lexical, length, cross-question overlap, and Part-alignment flags are review heuristics, **not** proof of a wrong key or semantic validity.

## 2. Authoritative 7-Part & Support Inventory

| Bank / Part | Units | Questions | `APPROVED_FOR_MOCK` | `HUMAN_REVIEW_REQUIRED` | `PRACTICE_SUPPORT` | Explanations | Translations | `choiceIds` | Structural Errors | `AI_TRIAGE` Flagged |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Listening Part 1 | 9 | 9 | 8 | 1 | 0 | 9/9 | 9/9 | 9/9 | 0 | 0 |
| Listening Part 2 | 61 | 61 | 25 | 36 | 0 | 61/61 | 61/61 | 61/61 | 0 | 3 |
| Listening Part 3 | 41 | 123 | 39 | 84 | 0 | 123/123 | 111/123 | 123/123 | 0 | 6 |
| Listening Part 4 | 34 | 102 | 30 | 72 | 0 | 102/102 | 90/102 | 102/102 | 0 | 1 |
| Reading Part 5 | 13 | 60 | 60 | 0 | 0 | 60/60 | 60/60 | 60/60 | 0 | 0 |
| Reading Part 6 | 8 | 32 | 32 | 0 | 0 | 32/32 | 32/32 | 32/32 | 0 | 3 |
| Reading Part 7 | 52 | 195 | 108 | 87 | 0 | 195/195 | 195/195 | 195/195 | 0 | 6 |
| Separate Part 5 Practice | 1 | 80 | 0 | 80 | 0 | 80/80 | 80/80 | 0/80 | 0 | 0 |
| Grammar Support (Part 5/6) | 58 | 169 | 0 | 0 | 169 | 169/169 | N/A (lesson-level) | 169/169 | 0 | 1 |
| **Total across all TOEIC & Support banks** | **277** | **831** | **302** | **360** | **169** | — | — | — | **0** | **37** |

## 3. Answer-Key Distribution by Part & Eligibility Bucket

| Part / Bank | Epistemic Bucket | A | B | C | D | Total |
|---|---|---:|---:|---:|---:|---:|
| Listening Part 1 | `APPROVED_FOR_MOCK` | 2 | 2 | 2 | 2 | 8 |
| Listening Part 1 | `HUMAN_REVIEW_REQUIRED` | 1 | 0 | 0 | 0 | 1 |
| Listening Part 2 | `APPROVED_FOR_MOCK` | 11 | 7 | 7 | — | 25 |
| Listening Part 2 | `HUMAN_REVIEW_REQUIRED` | 20 | 13 | 3 | — | 36 |
| Listening Part 3 | `APPROVED_FOR_MOCK` | 10 | 10 | 10 | 9 | 39 |
| Listening Part 3 | `HUMAN_REVIEW_REQUIRED` | 26 | 32 | 23 | 3 | 84 |
| Listening Part 4 | `APPROVED_FOR_MOCK` | 8 | 8 | 7 | 7 | 30 |
| Listening Part 4 | `HUMAN_REVIEW_REQUIRED` | 19 | 29 | 20 | 4 | 72 |
| Reading Part 5 | `APPROVED_FOR_MOCK` | 13 | 23 | 16 | 8 | 60 |
| Reading Part 6 | `APPROVED_FOR_MOCK` | 15 | 10 | 4 | 3 | 32 |
| Reading Part 7 | `APPROVED_FOR_MOCK` | 27 | 27 | 27 | 27 | 108 |
| Reading Part 7 | `HUMAN_REVIEW_REQUIRED` | 22 | 22 | 22 | 21 | 87 |
| Separate Part 5 Practice | `HUMAN_REVIEW_REQUIRED` | 20 | 20 | 20 | 20 | 80 |
| Grammar Support (Part 5/6) | `PRACTICE_SUPPORT` | 33 | 63 | 53 | 20 | 169 |

## 4. Part-Specific Grounding & Structural Checks

### Listening Part 1
- **Evidence classification**: `photo-source-reviewed`=8, `reserve-pending-independent-review`=1
- **Part-specific checks**: `attribution_verified`=9, `four_spoken_statements`=9
- **Triage signals (`AI_TRIAGE / STRUCTURAL`)**: none (cross-question leakage cues: 0)

### Listening Part 2
- **Evidence classification**: `reserve-pending-independent-review`=36, `response-fit-checked`=25
- **Part-specific checks**: `keyword_echo_distractor_items`=44, `prompt_Choice-or-Aux`=2, `prompt_Statement/Request`=2, `prompt_Tag/Other-question`=4, `prompt_WH-question`=30, `prompt_Yes/No-question`=23
- **Triage signals (`AI_TRIAGE / STRUCTURAL`)**: `KEY_UNUSUALLY_LONG`=3 (cross-question leakage cues: 0)

### Listening Part 3
- **Evidence classification**: `direct-text-match`=15, `lexical-evidence`=21, `manual-paraphrase-verified`=3, `reserve-pending-independent-review`=84
- **Part-specific checks**: `two_plus_speakers`=41
- **Triage signals (`AI_TRIAGE / STRUCTURAL`)**: `CROSS_QUESTION_KEY_LEAKAGE_CUE`=7, `KEY_UNUSUALLY_LONG`=6 (cross-question leakage cues: 7)

### Listening Part 4
- **Evidence classification**: `direct-text-match`=17, `lexical-evidence`=13, `reserve-pending-independent-review`=72
- **Part-specific checks**: `valid_talk_segments`=34
- **Triage signals (`AI_TRIAGE / STRUCTURAL`)**: `CROSS_QUESTION_KEY_LEAKAGE_CUE`=1, `KEY_UNUSUALLY_LONG`=1 (cross-question leakage cues: 1)

### Reading Part 5
- **Evidence classification**: `grammar-checked`=60
- **Part-specific checks**: `single_blank_prompts`=60
- **Triage signals (`AI_TRIAGE / STRUCTURAL`)**: none (cross-question leakage cues: 0)

### Reading Part 6
- **Evidence classification**: `context-fit-checked`=32
- **Part-specific checks**: `blank_markers_matched`=8, `sentence_insertion_items`=10, `word_phrase_cohesion_items`=22
- **Triage signals (`AI_TRIAGE / STRUCTURAL`)**: `KEY_DISTRACTOR_HIGH_OVERLAP`=3 (cross-question leakage cues: 0)

### Reading Part 7
- **Evidence classification**: `direct-text-match`=34, `explicit-source-evidence`=132, `lexical-evidence`=26, `manual-paraphrase-verified`=3
- **Part-specific checks**: `single_passage_units`=35, `valid_double_passage`=12, `valid_triple_passage`=5
- **Triage signals (`AI_TRIAGE / STRUCTURAL`)**: `CROSS_QUESTION_KEY_LEAKAGE_CUE`=7, `KEY_DISTRACTOR_HIGH_OVERLAP`=1, `KEY_UNUSUALLY_LONG`=5 (cross-question leakage cues: 7)

### Separate Part 5 Practice
- **Evidence classification**: `single-answer-rationale-recorded`=80
- **Part-specific checks**: `four_option_explanations_valid`=80, `single_blank_sentences`=80
- **Triage signals (`AI_TRIAGE / STRUCTURAL`)**: none (cross-question leakage cues: 0)

### Grammar Support (Part 5/6)
- **Evidence classification**: `grammar-exercise-checked`=169
- **Part-specific checks**: `lessons_tagged_Part 5`=31, `lessons_tagged_Part 6`=16, `lessons_with_formula_and_explanation`=58
- **Triage signals (`AI_TRIAGE / STRUCTURAL`)**: `CROSS_QUESTION_KEY_LEAKAGE_CUE`=2, `KEY_DISTRACTOR_HIGH_OVERLAP`=1 (cross-question leakage cues: 2)

## 5. Structural Errors & Duplicate-Stem Screen

- Structural errors detected: **0**
- Exact duplicate normalized stem+choices within any bank: **0**

## 6. `AI_TRIAGE / STRUCTURAL` Review Queue (Read-Only Triage Signals)

| Scope | Resource · Q | Bucket | Signals | Context |
|---|---|---|---|---|
| Listening Part 3 | `part3-invoice-error` · Q3 | `APPROVED_FOR_MOCK` | KEY_UNUSUALLY_LONG | When is payment due to be processed? |
| Listening Part 3 | `part3-budget-review` · Q2 | `APPROVED_FOR_MOCK` | KEY_UNUSUALLY_LONG | What will the man do this afternoon? |
| Listening Part 2 | `part2-contract-review` · Q1 | `APPROVED_FOR_MOCK` | KEY_UNUSUALLY_LONG | Choose the most appropriate response. |
| Listening Part 4 | `part4-customer-voicemail` · Q3 | `APPROVED_FOR_MOCK` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q3 key shares rare terms ['call', 'delivery'] with Q1 |
| Listening Part 4 | `part4-training-registration` · Q3 | `APPROVED_FOR_MOCK` | KEY_UNUSUALLY_LONG | When will confirmation emails be sent? |
| Listening Part 2 | `part2-customer-survey-sent` · Q1 | `HUMAN_REVIEW_REQUIRED` | KEY_UNUSUALLY_LONG | Choose the most appropriate response. |
| Listening Part 3 | `part3-training-handouts` · Q1 | `HUMAN_REVIEW_REQUIRED` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q1 key shares rare terms ['handouts', 'printed'] with Q2 |
| Listening Part 3 | `part3-printer-maintenance-contract` · Q3 | `HUMAN_REVIEW_REQUIRED` | KEY_UNUSUALLY_LONG | What does the man ask the woman to do next? |
| Listening Part 3 | `part3-cold-storage-capacity` · Q2 | `HUMAN_REVIEW_REQUIRED` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q2 key shares rare terms ['depot', 'shipment'] with Q3 |
| Listening Part 3 | `part3-recruitment-assessment-room` · Q3 | `HUMAN_REVIEW_REQUIRED` | KEY_UNUSUALLY_LONG | What will the woman do next? |
| Listening Part 3 | `part3-conference-catering-count` · Q3 | `HUMAN_REVIEW_REQUIRED` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q3 key shares rare terms ['additional', 'meals'] with Q2 |
| Listening Part 3 | `part3-software-pilot-feedback` · Q3 | `HUMAN_REVIEW_REQUIRED` | KEY_UNUSUALLY_LONG | What condition does the woman set for keeping the launch date? |
| Listening Part 3 | `part3-business-travel-itinerary` · Q2 | `HUMAN_REVIEW_REQUIRED` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q2 key shares rare terms ['evening', 'wednesday'] with Q3 |
| Listening Part 3 | `part3-business-travel-itinerary` · Q3 | `HUMAN_REVIEW_REQUIRED` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q3 key shares rare terms ['evening', 'flight', 'wednesday'] with Q2 |
| Listening Part 3 | `part3-international-shipment-customs` · Q2 | `HUMAN_REVIEW_REQUIRED` | KEY_UNUSUALLY_LONG | What information will the woman add? |
| Listening Part 3 | `batch025-part3-invoice-clarification` · Q2 | `HUMAN_REVIEW_REQUIRED` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q2 key shares rare terms ['corrected', 'invoice'] with Q3 |
| Listening Part 3 | `batch025-part3-invoice-clarification` · Q3 | `HUMAN_REVIEW_REQUIRED` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q3 key shares rare terms ['corrected', 'invoice'] with Q2 |
| Listening Part 2 | `batch027-part2-catering-count` · Q1 | `HUMAN_REVIEW_REQUIRED` | KEY_UNUSUALLY_LONG | Choose the most appropriate response. |
| Reading Part 7 | `facility-maintenance` · Q2 | `APPROVED_FOR_MOCK` | KEY_UNUSUALLY_LONG | Which area may have limited access? |
| Reading Part 7 | `double-passage-order` · Q1 | `APPROVED_FOR_MOCK` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q1 key shares rare terms ['carton', 'incorrectly'] with Q2 |
| Reading Part 7 | `double-passage-order` · Q2 | `APPROVED_FOR_MOCK` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q2 key shares rare terms ['carton', 'incorrectly'] with Q1 |
| Reading Part 7 | `double-passage-order` · Q5 | `APPROVED_FOR_MOCK` | KEY_UNUSUALLY_LONG | Why are the items needed soon? |
| Reading Part 6 | `part6-training-center-newsletter` · Q1 | `APPROVED_FOR_MOCK` | KEY_DISTRACTOR_HIGH_OVERLAP | Choose the best phrase for blank (1). |
| Reading Part 6 | `part6-customer-service-email` · Q2 | `APPROVED_FOR_MOCK` | KEY_DISTRACTOR_HIGH_OVERLAP | Choose the best phrase for blank (2). |
| Reading Part 6 | `part6-job-posting` · Q3 | `APPROVED_FOR_MOCK` | KEY_DISTRACTOR_HIGH_OVERLAP | Choose the best phrase for blank (3). |
| Reading Part 7 | `part7-double-training-reimbursement` · Q3 | `APPROVED_FOR_MOCK` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q3 key shares rare terms ['course', 'his'] with Q4 |
| Reading Part 7 | `part7-triple-regional-sales-meeting` · Q1 | `APPROVED_FOR_MOCK` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q1 key shares rare terms ['customer', 'retention'] with Q2 |
| Reading Part 7 | `part7-triple-regional-sales-meeting` · Q5 | `APPROVED_FOR_MOCK` | KEY_UNUSUALLY_LONG | What is planned for the afternoon? |
| Reading Part 7 | `part7-triple-facility-renovation` · Q2 | `APPROVED_FOR_MOCK` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q2 key shares rare terms ['equipment', 'network'] with Q4 |
| Reading Part 7 | `part7-single-vendor-delivery-calendar` · Q2 | `APPROVED_FOR_MOCK` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q2 key shares rare terms ['12', 'december'] with Q3 |
| Reading Part 7 | `part7-double-delivery-reschedule` · Q4 | `HUMAN_REVIEW_REQUIRED` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q4 key shares rare terms ['bay', 'loading'] with Q5 |
| Reading Part 7 | `part7-double-delivery-reschedule` · Q3 | `HUMAN_REVIEW_REQUIRED` | KEY_UNUSUALLY_LONG | Why is there no additional charge? |
| Reading Part 7 | `batch025-part7-double-conference-booking` · Q3 | `HUMAN_REVIEW_REQUIRED` | KEY_DISTRACTOR_HIGH_OVERLAP | Which room does the product team request? |
| Reading Part 7 | `batch026-part7-schedule-email` · Q3 | `HUMAN_REVIEW_REQUIRED` | KEY_UNUSUALLY_LONG | What should employees do by Thursday? |
| Grammar Support (Part 5/6) | `nouns-countability` · Q2 | `PRACTICE_SUPPORT` | KEY_DISTRACTOR_HIGH_OVERLAP | The company purchased two new _____. |
| Grammar Support (Part 5/6) | `batch025-reduced-adverbial-clauses-toeic` · Q1 | `PRACTICE_SUPPORT` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q1 key shares rare terms ['having', 'reviewed'] with Q3 |
| Grammar Support (Part 5/6) | `batch025-reduced-adverbial-clauses-toeic` · Q3 | `PRACTICE_SUPPORT` | CROSS_QUESTION_KEY_LEAKAGE_CUE | Q3 key shares rare terms ['having', 'reviewed'] with Q1 |

## 7. Honest Release Boundary

- Zero canonical IDs, choices, answer keys, translations, or `editorialStatus` values were modified by this audit.
- All 193 Listening reserve items, 87 Reading Part 7 reserve items, and 80 Separate Part 5 items remain `reserve-pending-independent-review` (`HUMAN_REVIEW_REQUIRED`).
- Structural integrity (`0` structural errors) confirms machine-verifiable schema, choice uniqueness, answer-key bounds, asset links, and evidence pointers; it does **not** certify semantic uniqueness or ETS equivalence.
