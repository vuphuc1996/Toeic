# Project Progress Baseline — TOEIC Dictionary v2.64.0

**Date:** 2026-11-15  
**Source:** local GitHub-only PWA candidate  
**Previous base:** v2.63.0

## Product progress snapshot

The canonical inventory and target-based ratios are in `PROJECT_PROGRESS_SNAPSHOT_v2.64.0.md`. Key measures:

- Vocabulary: 992 / 3,000 minimum = **33.1%**; 992 / 5,000 planning ceiling = **19.8%**. These are record-count coverage only, not editorial quality.
- Objective resources: 281 / 281 = **100%** unique resource-link coverage; 10/10 objective groups have linked resources. Availability is not learner mastery.
- Foundation Listening: 10/10 scripts and 20/20 questions = **100% bank coverage** within current Pre-A1/A1 scope; playback is device TTS, not ETS audio.
- Foundation A–Z: 26/26 records = **100% content-bank coverage**. No pronunciation accuracy or mastery inference; only TTS button interactions are stored.
- Outcome framework: 30/30 criteria defined. This is framework coverage only.
- TOEIC objective practice evidence: 9/10 objective groups wired = **90%**; 9/9 currently wired groups have delayed-recall and response-time capture.

## v2.64.0 delivery scope

- One shared 4:3 Part 1 visual frame in Learning Listening and TOEIC Mock Exam.
- Common crop, radius, caption and per-image focal point; photocopier focus is 50% 42%.
- Card rows share consistent title baseline and footer placement; long content wraps and can increase row height instead of being clipped.
- Button labels wrap; touch targets remain at least 44px.
- Responsive A–Z grid uses 4/3/2/1 columns depending on desktop, tablet and phone viewport.
- Foundation alphabet lesson contains all 26 letter records with IPA, example word, translation and TTS actions.
- A–Z button interactions are stored in an additive separate key; existing personal data and learner progress are preserved.

## Test and release status

- Selected tests: 94/94 Python PASS; 19/19 JavaScript PASS.
- CSS parse: 0 errors; design profile and version synchronization PASS.
- Vocabulary validator: 992 records / 0 errors / 0 warnings.
- Learning-content validator: 0 errors / 8 missing-JPG warnings.
- Strict Part 1 image validator: **FAIL**, 1/9 original JPGs present; eight licensed originals are absent from this workspace.
- Browser visual QA cannot be asserted: Chromium was blocked by the environment. Remote Actions, Pages and device QA remain unverified.

## Baseline interpretation

This version improves source-level visual consistency and broadens the Foundation A–Z content bank. It does not establish visual acceptance on every device, actual mastery of alphabet sounds, full project completion, or deployment readiness. Deployment remains on hold until the original Part 1 JPGs are present and strict validation passes.

---

## Generated inventory snapshot

# Project Progress Snapshot — generated

- Source version: **2.64.0**
- Basis: canonical JSON inventory; counts are not editorial approval.

## Target-based progress

| Workstream | Current | Target / denominator | Progress | Interpretation |
|---|---:|---:|---:|---|
| Vocabulary headwords | 992 | 3,000 minimum | **33.1%** | Lower-bound target coverage; quality review separate |
| Vocabulary headwords | 992 | 5,000 planning ceiling | **19.8%** | Conservative ceiling coverage; not a quality score |
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

## Vocabulary field coverage (against current 992-headword base; not editorial approval)

| Field | Records | Coverage |
|---|---:|---:|
| US IPA | 642/992 | **64.7%** |
| Word family | 207/992 | **20.9%** |
| Verb forms | 303/992 | **30.5%** |
| Collocations | 822/992 | **82.9%** |
| Synonyms | 404/992 | **40.7%** |
| Antonyms | 213/992 | **21.5%** |

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

