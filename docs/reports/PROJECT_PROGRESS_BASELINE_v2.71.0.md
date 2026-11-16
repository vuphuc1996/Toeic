# Project Progress Baseline — TOEIC Dictionary v2.71.0

- Snapshot date: 2026-11-16
- Source version: **2.71.0**
- Basis: canonical A–Z vocabulary records, manifest, objective-resource map and current learning-content inventory.
- Reporting rule: percentages are shown only where a target or defensible denominator exists. Inventory coverage is not editorial approval, completed instruction or learner mastery.

## 1. Vocabulary plan

| Measure | v2.70.0 baseline | v2.71.0 current | Change | Progress / interpretation |
|---|---:|---:|---:|---|
| Canonical headwords | 1,100 | 1,137 | +37 | **37.9%** of 3,000 minimum target |
| Planning ceiling | 5,000 | 5,000 | — | **22.7%** of planning ceiling |
| US IPA populated | 1,009/1,100 | 1,044/1,137 | +35 records | **91.8%** field population; not pronunciation certification |
| Word-family records | 267/1,100 | 276/1,137 | +9 records | **24.3%** field coverage |
| Word-family directed links | 365 | 374 | +9 links | Relationship inventory; no fixed target agreed |
| Verb forms | 317/1,100 | 325/1,137 | +8 records | 28.6% coverage |
| Collocations | 930/1,100 | 967/1,137 | +37 records | 85.0% coverage |
| Synonym coverage | 404/1,100 | 404/1,137 | 0 | 35.5% coverage; no speculative values added |
| Antonym coverage | 213/1,100 | 213/1,137 | 0 | 18.7% coverage; no speculative values added |

### Batch 012 content and IPA decisions

- Added 37 headwords for Contracts, Legal Procedures and Facilities Management.
- Every new entry has one sense record, an English definition, Vietnamese gloss, one bilingual example, at least three collocations and an editorial CEFR estimate.
- 35 IPA candidates are linked to exact single-pronunciation CMUdict entries and pass the project converter.
- `ventilation` remains blank because CMUdict has multiple pronunciations.
- `dispute` remains blank even though CMUdict has a single entry: the current converter's syllabification for the /spj/ cluster is not trusted for this headword; review is required before adding IPA.
- Cumulative CMUdict ledger contains **333** source-linked records. The **93** currently blank vocabulary IPA fields comprise 91 inherited unresolved records and the two Batch 012 exclusions. CMUdict supplies ARPABET rather than IPA; conversion is a documented project normalization, not independent pronunciation certification.
- Five reciprocal POS/sense-checked family pairs were reviewed: enforce/enforcement, janitor/janitorial, accessible/accessibility, occupy/occupant, and alter/alteration. The last pair adds the missing target-side link while preserving any existing relationship.

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
- Separate Part 5 practice bank: 80 questions; independent second-person review remains pending and the bank is practice-only.
- Foundation Reading: 10 passages / 20 questions.
- Foundation Listening: 10 scripts / 20 questions.
- A–Z sound lab: 26 letter records.

No numeric total target has been agreed for the full Grammar, Listening or Reading inventory; their overall completion percentage is therefore **not measurable**.

## 4. Overall product progress

There is no defensible single percentage for the whole TOEIC Dictionary because modules, learning outcomes, editorial quality, test infrastructure and future Writing/Speaking/IELTS tracks do not share one weighted denominator. Current meaningful measures:

- Vocabulary quantity: **37.9%** of the 3,000-headword minimum.
- Vocabulary US IPA population: **91.8%**.
- Word-family coverage: **24.3%**.
- Guided stage presence: **33.3%** (not content completion).
- Objective resource mapping: **100%** (not learning-outcome mastery).
- TOEIC practice evidence wiring: **90%**.

## 5. Release and verification status

- Vocabulary structural validation is expected to cover 1,137 stable IDs with no duplicates and no schema errors.
- Strict Part 1 photo validation remains a deployment blocker: only 1/9 JPG binaries is present in the current source archive. The eight source JPGs remain listed in `assets/listening/ATTRIBUTION.csv`; no substitutes are generated.
- `tools/restore_part1_photos.py` reads the exact original Pexels direct-download URLs from the attribution ledger, downloads all eight licensed JPGs in one operation when network access is available, validates JPEG dimensions and never overwrites existing assets. `restore-part1-photos.bat` is the Windows entry point. The script itself does not mean the eight binaries are already embedded in this archive.
- Remote GitHub Actions, GitHub Pages deployment and physical iOS/Android/desktop QA are not inferred from local checks.
