# Project Progress Baseline — TOEIC Dictionary v2.67.0

Date: 2026-11-15  
Previous release: v2.66.1  
Current candidate: v2.67.0

## Release delta

| Measure | v2.66.1 | v2.67.0 | Delta |
|---|---:|---:|---:|
| Canonical vocabulary headwords | 992 | 1,026 | +34 |
| Coverage against 3,000 minimum | 33.1% | 34.2% | +1.1 percentage points |
| Coverage against 5,000 planning ceiling | 19.8% | 20.5% | +0.7 percentage points |
| US IPA records | 642 | 674 | +32 |
| Word-family records | 207 | 230 | +23 |
| Collocation records | 822 | 856 | +34 |
| Listening units / questions | 107 / 201 | 107 / 201 | unchanged |
| Reading resources / questions | 51 / 200 | 51 / 200 | unchanged |

Field counts measure populated fields only. They do not certify correctness, naturalness, sense coverage, CEFR alignment or learner mastery. CEFR labels on the new batch are editorial estimates.

## Content development completed

- Vocabulary Batch 009: 34 unique headwords in finance, legal/compliance, procurement, HR and logistics.
- All 34 records contain at least one sense with Vietnamese meaning and English definition, one original bilingual TOEIC-context example, and at least three collocations.
- 32/34 entries have editorial US IPA transcriptions derived from CMUdict General American ARPABET where a stable reading was available. `negligence` and `financing` remain blank pending dictionary-level confirmation; no speculative IPA was entered.
- 11 of the new headwords have reciprocal, POS/sense-matched word-family links to existing entries. The full family-link regression now checks 57 curated reciprocal pairs.
- No new synonyms/antonyms were added where a reliable sense-matched relation was not established. Two new verbs (`attest`, `expedite`) have verb forms; other new nouns/adjective were not given artificial verb-form fields.
- Batch 009 remains pending independent lexical review. It is not an independent reviewer approval and does not confer official CEFR alignment.

## Listening media cleanup

- Removed the redundant UI phrase `Nội dung bổ sung · đang chờ kiểm duyệt độc lập · chưa dùng trong Mock Exam` from the visible Listening list.
- Retained the underlying `reserve-pending-independent-review` status and Mock exclusion rule; status metadata is not a UI-only decoration and must not be removed.
- Part 1 now has a JPG-only data/runtime contract: no `image` fallback field, no SVG fallback handler, no Part 1 SVG files in `assets/listening/`, and no Part 1 SVG Service Worker entries.
- The workspace currently contains only 1/9 original JPG binaries. The eight repository-owned JPG files are not in this archive. Keep the strict validator enabled and preserve/restore those exact originals when merging with GitHub.

## Legacy learner-data compatibility

- Added release-repair profiles for old 979-word and 992-word snapshots.
- A 979-word legacy profile can restore only the 47 exact additions from release batches 008+009 when all matching conditions hold; a 992-word snapshot can restore only the 34 Batch 009 additions.
- Other user-hidden words, personal additions, overrides and progress are untouched. No IndexedDB version/store/schema change was introduced.

## Interpretation and next work

- Vocabulary inventory is 1,026/3,000 (34.2%) against the minimum planning target and 1,026/5,000 (20.5%) against the upper planning target.
- Next content focus: continue the 3,000–5,000 headword roadmap with carefully sourced TOEIC terms; fill missing IPA only after dictionary verification; improve word-family links, sense-level examples and collocations without padding unsupported synonym/antonym fields.
- Listening, Reading and Grammar question counts are unchanged. Continue independent review of reserve Listening/Reading/Part 5 pools separately from raw inventory growth.
- Current source is a local candidate, not deployed. Remote GitHub Actions, GitHub Pages and real-device visual/audio tests are not claimed.
