# Project Progress Baseline — TOEIC Dictionary v2.69.0

- Snapshot date: 2026-11-15
- Source version: **2.69.0**
- Basis: canonical A–Z vocabulary records, manifest, objective-resource map and current learning-content inventory.
- Reporting rule: percentages are shown only where a target or defensible denominator exists. Inventory coverage is not editorial approval, completed instruction or learner mastery.

## 1. Vocabulary plan

| Measure | v2.68.0 baseline | v2.69.0 current | Change | Progress / interpretation |
|---|---:|---:|---:|---|
| Canonical headwords | 1,063 | 1,063 | 0 | **35.4%** of 3,000 minimum target |
| Planning ceiling | 5,000 | 5,000 | — | **21.3%** of planning ceiling |
| US IPA populated | 711/1,063 | 972/1,063 | +261 records | **91.4%** current coverage; +24.5 percentage points |
| Word-family records | 240/1,063 | 259/1,063 | +19 records | **24.4%** coverage |
| Word-family directed links | 338 | 357 | +19 links | Relationship inventory; no fixed target agreed |
| Verb forms | 312/1,063 | 312/1,063 | 0 | 29.4% coverage |
| Collocations | 893/1,063 | 893/1,063 | 0 | 84.0% coverage |
| Synonym coverage | 404/1,063 | 404/1,063 | 0 | 38.0% coverage |
| Antonym coverage | 213/1,063 | 213/1,063 | 0 | 20.0% coverage |

### US IPA source and conservative exclusions

261 records were filled using exact headword matches in CMUdict that have a single pronunciation and one primary-stress pattern. CMUdict supplies ARPABET, not IPA; project tool `tools/cmudict_ipa.py` applies a documented broad General American conversion. The ledger stores source ARPABET, resulting IPA, provenance and conversion metadata.

The remaining **91 records are deliberately left blank**:

- 60 have multiple CMUdict pronunciations;
- 25 have no exact CMUdict entry;
- 6 have multiple primary-stress patterns.

Do not fill these by guessing. A lexical/editorial decision or another reliable dictionary source is required. CMUdict itself cautions that its data may contain errors, omissions and inconsistencies; this pipeline is source-linked editorial normalization, not independent pronunciation certification.

## 2. TOEIC / Foundation structural coverage

| Workstream | Current | Target / basis | Progress | Limitation |
|---|---:|---:|---:|---|
| Guided pathway stages represented | 2/6 | Pre-A1, A1, A2, B1, B2, C1 | 33.3% | Stage presence only; higher-stage completion not implied |
| Placement question mapping | 16/16 | All diagnostic items | 100% | Mapping only |
| Canonical objective-resource links | 281/281 | All catalog records | 100% | ID links only |
| Learning objectives with linked resources | 10/10 | Current objective list | 100% | Availability only |
| Outcome criteria defined | 30/30 | Current outcome registry | 100% | Definition, not instrumentation or mastery |
| TOEIC objective practice evidence wired | 9/10 | Current objective map | 90% | Latest answer evidence; practice threshold only |
| Foundation Listening | 10 scripts / 20 questions | 10 current lessons / 20 questions | 100% inventory | Device TTS; not authentic ETS audio |
| Foundation Reading | 10 passages / 20 questions | 10 current lessons / 20 questions | 100% inventory | Not learner mastery |
| Foundation A–Z | 26/26 letters | Alphabet | 100% data coverage | TTS action is not pronunciation scoring |

## 3. Current TOEIC inventory

- Grammar: 33 lessons / 86 exercises.
- Listening: 107 units / 201 questions.
- Reading: 51 resources / 200 questions.
- Separate Part 5 practice bank: 80 questions; independent review remains pending and the bank is practice-only.
- Foundation Reading: 10 passages / 20 questions.
- Foundation Listening: 10 scripts / 20 questions.
- A–Z sound lab: 26 letter records.

No numeric total target has been agreed for the full Grammar, Listening or Reading inventory; their overall completion percentage is therefore **not measurable** at this time.

## 4. Overall product progress

There is no defensible single percentage for the whole TOEIC Dictionary because the project includes separate modules, learning outcomes, quality metadata, test infrastructure, and future Writing/Speaking/IELTS tracks without one common weighted denominator. The most meaningful current summary is:

- Vocabulary quantity: **35.4%** of the 3,000-headword minimum.
- Vocabulary US IPA population: **91.4%**.
- Word-family coverage: **24.4%**.
- Guided stage presence: **33.3%** (not content completion).
- Objective resource mapping: **100%** (not learning outcome mastery).
- Practice evidence wiring: **90%**.

## 5. Next planned work

1. Review the 91 unresolved IPA records individually using another reliable pronunciation source; keep ambiguous entries blank until a reading is confirmed.
2. Expand word-family relationships only when POS and sense align in both directions.
3. Continue new TOEIC headwords in the planned groups: Customer Service, Travel, Contracts and Facilities.
4. Expand definitions, sense-linked examples, synonyms/antonyms and collocations only where a defensible source/sense exists.
5. Keep IELTS, TOEIC Writing and TOEIC Speaking as separately tracked future workstreams rather than inflating the TOEIC L&R percentage.

## 6. Release and validation status

- Vocabulary validator: 1,063 records / 0 errors / 0 warnings.
- CMUdict ledger integrity: 261/261 source-linked entries pass.
- Strict Part 1 photo validator: **FAIL 8 missing original JPG files** in this workspace (only 1/9 file bytes present). Keep the eight repository-owned original JPGs when merging the source; do not synthesize replacements or disable strict validation.
- Remote GitHub Actions, GitHub Pages deployment and physical-device QA are not inferred from local verification.
