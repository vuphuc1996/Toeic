# Project Progress Snapshot — generated

- Source version: **2.95.72**
- Basis: canonical JSON inventory; counts are not editorial approval.

## Target-based progress

| Workstream | Current | Target / denominator | Progress | Interpretation |
|---|---:|---:|---:|---|
| Vocabulary headwords | 1,181 | 3,000 minimum | **39.4%** | Lower-bound target coverage; quality review separate |
| Vocabulary headwords | 1,181 | 5,000 planning ceiling | **23.6%** | Conservative ceiling coverage; not a quality score |
| Related-term glossary exact reference join | 556/804 | **69.2%** | 248 distinct terms / 249 occurrences remain unglossed; exact case-insensitive join only |
| Guided pathway stages represented | 3/6 | Pre-A1, A1, A2, B1, B2, C1 | **50.0%** | Stage presence only; not full-stage completion |
| Placement question mapping | 16/16 | All diagnostic questions | **100.0%** | Structural mapping coverage only |
| Canonical objective-resource links | 379/379 | 100.0% | ID links only; not learning-outcome completion |
| Learning objectives with linked resources | 11/11 | 100.0% | Availability only; review and mastery separate |
| Foundation Listening core scripts mapped | 23/23 | **100.0%** | One core device-synthesized script per existing Pre-A1/A1/A2 lesson; supplementary A2 counted separately |
| Foundation Listening questions | 59 core + 39 supplementary | Chưa đo được — supplementary A2 practice remains review-pending; TTS, not ETS audio |
| Foundation A–Z letter records | 26/26 | **100.0%** | Complete letter-data coverage only; not pronunciation accuracy or learner mastery |
| Outcome criteria defined | 33/33 | 100.0% | Framework definition coverage; not learner mastery |
| Outcomes with evidence instrumentation | 6/33 | 18.2% | Collection path only; no learner completion inferred |
| TOEIC objective practice evidence wired | 9/9 | 100.0% | Latest result per unique question; practice threshold only, not learner mastery |
| Foundation outcome evidence wired | 6/6 | 100.0% | Recognition, learner self-report for explanation/production, and 1/3-day delayed recall; wiring is not mastery |
| Delayed-recall scheduling across wired TOEIC groups | 9/9 | 100.0% | 1/3-day scheduling rule; not a retention guarantee |
| Response-time capture across wired TOEIC groups | 9/9 | 100.0% | Structured Grammar/Reading/Listening plus separate Part 5; duration is not a speed score |

## Inventory (no approved numeric target)

| Workstream | Current inventory | Progress |
|---|---:|---|
| Grammar | 58 lessons / 169 exercises | Chưa đo được — no agreed total lesson target |
| Listening | 145 units / 295 questions | Chưa đo được — no agreed unit/question target |
| Reading | 73 resources / 287 questions | Chưa đo được — no agreed resource/question target |
| Separate Part 5 practice | 80 questions | Chưa đo được — no agreed size target; independent review remains separate |
| Independent review queue | 193 Listening + 87 Reading Part 7 + 80 Part 5 = 360 questions | Reviewer handoff only; no reserve item is Mock-approved by queue inclusion |
| Foundation Reading | 23/23 passages / 59 questions | 100.0% within current Pre-A1/A1/A2 scope | Separate reading bank; not Foundation mastery |
| Foundation Listening | 23/23 core scripts / 59 core questions + 13 supplementary A2 scripts / 39 questions | 100.0% core lesson coverage | Device Speech Synthesis; supplementary A2 is review-pending, not authentic ETS recordings |
| Foundation A–Z sound lab | 26/26 letters | 100.0% | Two TTS actions per letter; action count is not pronunciation mastery |

## Vocabulary field coverage (against current 1,181-headword base; not editorial approval)

| Field | Records | Coverage |
|---|---:|---:|
| US IPA | 1,102/1,181 | **93.3%** |
| Word family | 322/1,181 | **27.3%** |
| Verb forms | 328/1,181 | **27.8%** |
| Collocations | 1,011/1,181 | **85.6%** |
| Synonyms | 405/1,181 | **34.3%** |
| Antonyms | 210/1,181 | **17.8%** |
| Word-family directed links | 420 links | — |

These ratios show whether a field is populated, not whether its content is accurate, natural or complete. Relationship counts are reported separately from headword counts.

## Quality / verification status

- Content counts do not equal completed learning outcomes.
- Outcome framework: 33/33 criteria defined; 6/33 have an evidence-collection path. Neither count measures learner mastery.
- TOEIC objective tracker: aggregates latest answer per stable unique question; minimum 10 unique items and 80% accuracy. A passing label is a practice threshold only, not CEFR/ETS certification or proof of every outcome.
- Objective evidence is connected for Grammar, Listening Parts 1–4, Reading Parts 5–7 and separate Part 5 practice. Reserve Listening items are excluded until editorial review; Reading Part 7 remains second-review-gated; the separate 80-item Part 5 practice pool is review-pending and cannot earn a threshold status.
- Listening Part 1 currently has 8 eligible unique questions (one additional mapped item is reserve-pending), below the 10-item minimum; at least 2 more unique, reviewed questions are needed before it can reach the practice threshold.
- Foundation outcome evidence now records recognition, a learner-authored sentence with three self-report explanation/production ratings, and delayed recall. Self-report is not auto-graded; delayed recall is scheduled 1/3 days and is not a retention guarantee.
- Foundation Listening stores attempts under a separate localStorage key; its bank coverage does not imply the learner has completed the questions or met the local practice threshold.
- Supplementary A2 Listening has 13 six-turn dialogues (75–100 words each), 39 questions across detail, purpose/context and inference/next-action, with exact source-evidence snippets; all remain pending independent review and use browser TTS.
- v2.92.0 batch 024 adds 8 Grammar lessons / 24 exercises, 6 TOEIC Listening units / 18 questions, and 6 TOEIC Reading Part 7 resources / 27 questions. All 12 new Listening/Reading resources remain reserve-pending-independent-review and excluded from Mock eligibility. v2.93.0 batch 025 adds 9 Grammar lessons / 27 exercises, 8 TOEIC Listening units / 20 questions, 8 TOEIC Reading Part 7 resources / 36 questions and 4 vocabulary headwords; new Listening/Reading items remain pending independent review and Mock-excluded.
- Foundation A–Z records TTS play-button actions in `toeic:alphabet-sound-progress:v1`; no pronunciation analysis or mastery inference is performed.
- Part 5 practice: pending independent review; do not count as Mock-eligible.
- Independent-review handoff queue: 193 Listening questions across 89 units + 87 Reading Part 7 questions across 22 resources + 80 separate Part 5 questions = 360 item-level decisions. Queue presence means traceable reviewer handoff only, not approval or Mock eligibility.
- Listening pending-review pool and Mock-eligible counts must be tracked separately from raw inventory.
- Placement is a short sample, not official CEFR/ETS certification.
- TOEIC score readiness is a local evidence tracker based on three completed 200-question Full Mocks; it shows L/R practice-accuracy trends only and does not convert raw accuracy into ETS scaled scores or claim 500+/850+ readiness.
- Remote CI, GitHub Pages deployment and physical-device QA are not inferred from local checks.

## Reporting rule

A percentage is shown only when a defensible target or denominator exists. Otherwise the report says “Chưa đo được” and records the current inventory without inventing a target.

