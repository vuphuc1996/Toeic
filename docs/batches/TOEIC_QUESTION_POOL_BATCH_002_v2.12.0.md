# TOEIC Question Pool Batch 002 — v2.12.0

- **Date:** 2026-11-10
- **Scope:** TOEIC Listening & Reading only. IELTS is deferred.
- **Baseline:** v2.11.0 (Listening 36 questions; Reading 77 questions; 928 vocabulary records).
- **Method:** original editorial practice material; ETS/IIBC/Korea official references are used only to confirm exam distribution, not to copy protected questions/audio.

## Listening changes

| Part | v2.11.0 | Added | v2.12.0 |
|---|---:|---:|---:|
| Part 1 | 8 | 0 | 8 |
| Part 2 | 2 | 23 | 25 |
| Part 3 | 18 | 21 | 39 |
| Part 4 | 8 | 22 | 30 |
| **Total** | **36** | **66** | **102** |

- Added 23 independent Part 2 items; each has one spoken prompt and three response options.
- Added five Part 3 conversations (15 questions).
- Appended two questions to each of three legacy Part 3 conversations that previously contained one question. Existing first questions remain first.
- Added six Part 4 talks (18 questions).
- Appended two questions to each of two legacy Part 4 talks that previously contained one question. Existing first questions remain first.
- Final structure: 13 Part 3 conversations × 3 questions; 10 Part 4 talks × 3 questions. All Part 3 conversations contain at least two named speakers.

## Reading changes

| Part | v2.11.0 | Added | v2.12.0 |
|---|---:|---:|---:|
| Part 5 | 16 | 14 | 30 |
| Part 6 | 12 | 4 | 16 |
| Part 7 | 49 | 14 | 63 |
| **Total** | **77** | **32** | **109** |

New resource IDs:

- Part 5: `part5-tense-voice-set-05`, `part5-adjectives-adverbs-set-06`, `part5-connectors-prepositions-set-07`.
- Part 6: `part6-product-workshop-registration`.
- Part 7: `part7-double-equipment-order`, `part7-double-training-reimbursement`, `part7-triple-regional-sales-meeting`, `part7-triple-facility-renovation`.

Part 7 question mix is now 38 single-passage questions + 25 double/triple-passage questions. Two legacy resources, `double-passage-order` and `triple-passage-meeting`, were normalized into structured `documents[]` (2 and 3 documents respectively); the existing `passage`, questions, answer keys and order were retained. Every multi-document set now exposes the expected number of labeled documents.

## Blueprint selection capability

The pool supports selection of one 200-question form: Listening 6/25/39/30 (choose six of eight Part 1 practice images) and Reading 30/16/(29 single + 25 multi). There are 9 reserve single-passage Part 7 questions and 2 reserve Part 1 practice items. This is not a complete mock engine and does not yet provide multiple non-repeating forms.

## Preservation and limits

- Vocabulary: 928 IDs and 26 alphabet JSON files unchanged byte-for-byte against v2.11.0.
- Grammar: 25 lessons / 54 exercises, unchanged.
- App runtime and personal IndexedDB/local data schema: no intentional changes.
- Part 1 art remains SVG illustration, not a real photo. Browser SpeechSynthesis remains synthesized audio, not studio/ETS recording.
- Automated structure checks do not establish semantic answer correctness. A full editorial pass is required before Full Mock.
- Not committed, pushed or deployed by this batch.
