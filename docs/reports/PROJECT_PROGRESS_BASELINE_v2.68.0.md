# Project Progress Baseline — TOEIC Dictionary v2.68.0

This release baseline is based on canonical inventory and automated structural checks. Counts do not imply independent editorial approval or learner mastery.

# Project Progress Snapshot — generated

- Source version: **2.68.0**
- Basis: canonical JSON inventory; counts are not editorial approval.

## Target-based progress

| Workstream | Current | Target / denominator | Progress | Interpretation |
|---|---:|---:|---:|---|
| Vocabulary headwords | 1,063 | 3,000 minimum | **35.4%** | Lower-bound target coverage; quality review separate |
| Vocabulary headwords | 1,063 | 5,000 planning ceiling | **21.3%** | Conservative ceiling coverage; not a quality score |
| Guided pathway stages represented | 2/6 | Pre-A1, A1, A2, B1, B2, C1 | **33.3%** | Stage presence only; not full-stage completion |
| Placement question mapping | 16/16 | All diagnostic questions | **100.0%** | Structural mapping coverage only |
| Canonical objective-resource links | 281/281 | 100.0% | ID links only; not learning-outcome completion |
| Learning objectives with linked resources | 10/10 | 100.0% | Availability only; review and mastery separate |
| Foundation Listening scripts mapped | 10/10 | **100.0%** | One device-synthesized script per existing Pre-A1/A1 lesson |
| Foundation Listening questions | 20/20 | **100.0%** | Two questions per existing lesson; TTS practice, not ETS audio |
| Foundation A–Z letter records | 26/26 | **100.0%** | Complete letter-data coverage only; not pronunciation accuracy or learner mastery |
| Outcome criteria defined | 30/30 | 100.0% | Framework coverage only; criterion-level mastery remains separate |
| TOEIC objective practice evidence wired | 9/10 | 90.0% | Latest result per unique question; practice threshold only, foundation rubric outcomes not yet instrumented |
| Delayed-recall scheduling across wired TOEIC groups | 9/9 | 100.0% | 1/3-day scheduling rule; not a retention guarantee |
| Response-time capture across wired TOEIC groups | 9/9 | 100.0% | Structured Grammar/Reading/Listening plus separate Part 5; duration is not a speed score |

## Inventory (no approved numeric target)

| Workstream | Current inventory | Progress |
|---|---:|---|
| Grammar | 33 lessons / 86 exercises | Chưa đo được — no agreed total lesson target |
| Listening | 107 units / 201 questions | Chưa đo được — no agreed unit/question target |
| Reading | 51 resources / 200 questions | Chưa đo được — no agreed resource/question target |
| Separate Part 5 practice | 80 questions | Chưa đo được — no agreed size target; independent review remains separate |
| Foundation Reading | 10/10 passages / 20 questions | 100.0% within current Pre-A1/A1 scope | Separate reading bank; not Foundation mastery |
| Foundation Listening | 10/10 scripts / 20 questions | 100.0% within current Pre-A1/A1 scope | Device Speech Synthesis; not authentic ETS recordings |
| Foundation A–Z sound lab | 26/26 letters | 100.0% | Two TTS actions per letter; action count is not pronunciation mastery |

## Vocabulary field coverage (against current 1,063-headword base; not editorial approval)

| Field | Records | Coverage |
|---|---:|---:|
| US IPA | 711/1,063 | **66.9%** |
| Word family | 240/1,063 | **22.6%** |
| Verb forms | 312/1,063 | **29.4%** |
| Collocations | 893/1,063 | **84.0%** |
| Synonyms | 404/1,063 | **38.0%** |
| Antonyms | 213/1,063 | **20.0%** |

These ratios show whether a field is populated, not whether its content is accurate, natural or complete. Relationship counts are reported separately from headword counts.

## Quality / verification status

- Content counts do not equal completed learning outcomes.
- Outcome framework: 30/30 criteria defined; this is not criterion-level mastery or completed instruction.
- TOEIC objective tracker: aggregates latest answer per stable unique question; minimum 10 unique items and 80% accuracy. A passing label is a practice threshold only, not CEFR/ETS certification or proof of every outcome.
- Objective evidence is connected for Grammar, Listening Parts 1–4, Reading Parts 5–7 and separate Part 5 practice. Reserve Listening items are excluded until editorial review; Reading Part 7 remains second-review-gated; the separate 80-item Part 5 practice pool is review-pending and cannot earn a threshold status.
- Listening Part 1 currently has 8 eligible unique questions (one additional mapped item is reserve-pending), below the 10-item minimum; at least 2 more unique, reviewed questions are needed before it can reach the practice threshold.
- Foundation production/retention rubrics and explanation scoring remain uninstrumented; delayed recall and response-time capture are instrumented for the 9 wired TOEIC objective groups.
- Foundation Listening stores attempts under a separate localStorage key; its bank coverage does not imply the learner has completed the questions or met the local practice threshold.
- Foundation A–Z records TTS play-button actions in `toeic:alphabet-sound-progress:v1`; no pronunciation analysis or mastery inference is performed.
- Part 5 practice: pending independent review; do not count as Mock-eligible.
- Listening pending-review pool and Mock-eligible counts must be tracked separately from raw inventory.
- Placement is a short sample, not official CEFR/ETS certification.
- Remote CI, GitHub Pages deployment and physical-device QA are not inferred from local checks.

## Reporting rule

A percentage is shown only when a defensible target or denominator exists. Otherwise the report says “Chưa đo được” and records the current inventory without inventing a target.


## Release-specific progress

- Vocabulary: 1,063/3,000 minimum (35.4%); 1,063/5,000 planning ceiling (21.3%).
- Batch 010: 37/37 entries are present in canonical A–Z files; all have definitions, Vietnamese glosses, bilingual examples, at least three collocations and editorial US IPA. Independent lexical review is pending.
- Part 1 review integrity: all 8 historic unit hashes match after reconstructing only the removed SVG metadata field; 8/8 question hashes remain unchanged.
- Deployment: held until the 8 missing original JPG files are restored and strict photo validation reaches 9/9.
