# TOEIC Content Coverage — v2.80.0

Generated: 2026-11-16

> TOEIC Listening & Reading only. IELTS and other exam-specific content are intentionally excluded until TOEIC acceptance gates are met.

## Vocabulary coverage

| Metric | Count | Coverage |
|---|---:|---:|
| Headwords | 1137 | — |
| US IPA present | 1044 | 91.8% |
| Word-family records | 276 | 24.3% |
| Word-family links | 374 | — |
| Verb-form records | 325 | 28.6% |
| Collocation records | 967 | 85.0% |
| CEFR assigned | 1137 | 100.0% |

| CEFR | Records |
|---|---:|
| A1 | 64 |
| A2 | 238 |
| B1 | 315 |
| B2 | 398 |
| C1 | 122 |
| C2 | 0 |
| Unassigned | 0 |

## Listening coverage

| Part | Units | Questions |
|---|---:|---:|
| Part 1 | 9 | 9 |
| Part 2 | 51 | 51 |
| Part 3 | 27 | 81 |
| Part 4 | 20 | 60 |
| **Total** | **107** | **201** |

- Spoken segments: 218.
- Part 1 photo assets: 8 licensed Pexels + 1 AI-generated; each source type is tracked separately in ATTRIBUTION.csv.
- Audio is browser SpeechSynthesis; it is synthesized audio, not recorded/native-speaker or ETS audio.
- Mock-eligible Listening pool: 102 questions; pending independent review: 99 questions. Pending content remains available for practice but is excluded from Mock.
- Pending batch counts: Batch 014: 17, Batch 015: 70, Batch 017: 1, Batch legacy: 11.

## Reading coverage

| Part | Resources | Questions |
|---|---:|---:|
| Part 5 | 13 | 60 |
| Part 6 | 8 | 32 |
| Part 7 | 30 | 108 |
| **Total** | **51** | **200** |

- Reading text word count (current passages/documents): 3734.
- Part 7 question mix: 58 single-passage questions / 50 multiple-passage questions.
- Structured Part 7 multi-document resources: 10/10 double/triple passages.
- Complete five-question Part 7 multiple-passage blocks: 10/10; single-passage blocks with 2–4 questions: 20/20.

## Grammar

- Lessons: 33.
- Exercises: 86.
- Part 5-tagged lessons/exercises: 7 / 28.
- Part 6-tagged lessons/exercises: 3 / 12.
- Part-focus totals may overlap when one lesson supports both Parts 5 and 6.

## Adaptive TOEIC Part 5 Sentence Completion Practice

- Separate sentence-completion questions: 80.
- Editorial status: `reserve-pending-independent-review`; content source: `original-editorial`.
- Each item has one blank, four A–D choices, one answer key, four option explanations, grammar focus, Vietnamese translation and a single-answer rationale.
- This adaptive practice bank is separate from Reading Part 5 and is not included in Reading Mock inventory or scoring.
- Independent second-person review is pending; automated validation does not approve items for Mock.
- Batch distribution: 016: 45, core: 35.
- Keyed answer positions A/B/C/D: 20 / 20 / 20 / 20.

### Grammar-group coverage

| Grammar group | Questions |
|---|---:|
| Adjectives and Adverbs | 10 |
| Articles and Determiners | 3 |
| Conjunctions and Clauses | 3 |
| Gerunds and Infinitives | 3 |
| Imperatives and Verb Forms | 1 |
| Infinitives and Verb Patterns | 13 |
| Linking Verbs | 1 |
| Modal Verbs | 2 |
| Participles and Reduced Relative Clauses | 1 |
| Passive Voice | 5 |
| Prepositions and Collocations | 13 |
| Subject–Verb Agreement | 7 |
| Verb Tense and Aspect | 8 |
| Word Forms and Nouns | 10 |
## Reference question distribution — one TOEIC L&R form

| Part | Current pool | Reference per form | Coverage |
|---|---:|---:|---:|
| Part 1 | 8 eligible | 6 | 133.3% |
| Part 2 | 25 eligible | 25 | 100.0% |
| Part 3 | 39 eligible | 39 | 100.0% |
| Part 4 | 30 eligible | 30 | 100.0% |
| **Listening eligible total** | **102** | **100** | **102%** |
| Part 5 | 60 | 30 | 200.0% |
| Part 6 | 32 | 16 | 200.0% |
| Part 7 | 108 | 54 | 200.0% |
| **Reading total** | **200** | **100** | **200%** |

These ratios compare the current practice pool with the public distribution for one test form. They do not mean the app already contains a complete, validated mock test. Part 1 Mock-eligible and total pools are tracked separately; each record has a source-specific attribution row and a JPG-only `photo` path; no SVG fallback is part of the active contract.

## Answer-key balance (A/B/C/D counts)

| Part | A | B | C | D |
|---|---:|---:|---:|---:|
| Part 1 | 2 | 2 | 2 | 2 |
| Part 2 | 11 | 7 | 7 | 0 |
| Part 3 | 10 | 10 | 10 | 9 |
| Part 4 | 8 | 8 | 7 | 7 |
| Part 5 | 13 | 23 | 16 | 8 |
| Part 6 | 15 | 10 | 4 | 3 |
| Part 7 | 27 | 27 | 27 | 27 |

## Interpretation and gaps

- Listening learning inventory has 201 questions (107 source units); currently 102 are Mock-eligible and 99 remain pending independent review. The eligible pool supports one full 100-question form; at 102 eligible questions the next Full Listening form reuses 98 questions.
- If all pending Listening questions were independently approved, projected per-Part inventory would be P1=9, P2=51, P3=81, P4=60. It would still be short by 3 Part 1 items for two entirely non-repeating Full forms.
- Reading pool has 200 questions; Part 7 includes 58 single-passage and 50 multiple-passage questions. The v2.33 Mock regression verifies two consecutive 100-question Reading forms with zero reused question IDs.
- Structured Part 7 double/triple passage resources: 10/10.
- V2.25.0 includes a timed 15/60/120-minute mock engine, answer review and local score analysis; it is an internal practice tool, not an officially equated TOEIC test. Independent editorial review remains pending for reserve content.
- Vocabulary is 1137 headwords, below the 3,000–5,000 internal TOEIC planning target. That target is not an official ETS list.
- No score conversion should be described as an ETS score until a validated scoring/equating model exists; current per-Part analytics are local-practice indicators.
- `tools/validate-learning-content.py` checks IDs, choices, answers, explanation presence, Part coverage, passages and image assets. It does not prove semantic correctness; editorial review remains required.
