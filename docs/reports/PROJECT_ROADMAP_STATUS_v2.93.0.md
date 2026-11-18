# Project Roadmap Status — v2.93.0

**Date:** 2026-11-18  
**Current release:** TOEIC Dictionary v2.93.0  
**Scope decision:** TOEIC Listening & Reading only. B1 is blueprint-only. TOEIC Speaking/Writing and IELTS are deferred.

## 1. Confirmed product targets

- **System design target:** build a TOEIC Listening & Reading learning system capable of supporting learners toward **850+**. This is a product-quality target, not a guarantee for every learner.
- **Initial personal milestone:** the learner's first target is **500+**, with later milestones 600, 700, 750, 800, 850 and 900+. A learner can begin below 500 and progress through the same system.
- **Vocabulary:** 3,000 headwords is the interim minimum; 5,000 is the planning target. Count coverage is not vocabulary-quality coverage.
- **Scope gate:** complete and accept TOEIC L/R before starting TOEIC Speaking/Writing. IELTS begins only after the later S/W phase and explicit owner approval.

## 2. Current canonical inventory

| Workstream | Current inventory | Status / qualification |
|---|---:|---|
| Vocabulary | 1,141 headwords | 38.0% of 3,000 interim minimum; 22.8% of 5,000 planning target; lexical/CEFR review remains separate |
| Grammar | 50 lessons / 137 exercises | TOEIC-oriented content expanded; no approved total lesson denominator |
| Listening | 121 units / 239 questions | 102 questions remain Mock-eligible; 137 pending review; inventory includes Part 1–4 |
| Reading | 65 resources / 263 questions | Part 5/6/7; 63 new Part 7 questions from v2.92.0/v2.93.0 remain pending independent review |
| Separate Part 5 practice | 80 questions | Practice-only; pending independent review and excluded from Mock |
| Foundation | Pre-A1/A1/A2 present | Existing Foundation work remains supportive; A2 extended material still needs independent review and learner validation |
| Score readiness | Local Full Mock evidence tracker | Requires three completed 200-question Full Mocks; reports practice accuracy trends only, not ETS score estimates |

No overall project completion percentage is asserted because several content libraries have no approved target denominator and quality/review gates are separate from inventory size.

## 3. v2.93.0 completed development

- Grammar Batch 025: 9 lessons / 27 exercises.
- Listening Batch 025: 8 units / 20 questions — 2 Part 2, 3 Part 3 and 3 Part 4.
- Reading Batch 025: 8 Part 7 resources / 36 questions — 4 single passages with 4 questions each and 4 double passages with 5 questions each.
- Vocabulary Batch 013: 4 new headwords; all four US IPA entries are single-pronunciation CMUdict matches. No IPA was guessed.
- Added a local Full Mock score-readiness evidence tracker. It requires 3 completed Full Mock attempts (200 questions each) before displaying L/R average accuracy and direction of change. It does not convert raw accuracy into an ETS scaled score.
- Added 339/339 objective-resource links, batch SHA-256 registry, item-level review checklist and automated tests.
- Preserved IndexedDB v1 and all existing learner progress keys. No new learning-data storage key or external transfer was introduced.

## 4. Quality gates still open

### P0 — editorial and learner validation
1. Independent second-person review of 137 pending Listening questions, including all new Batch 024/025 items.
2. Independent second-person review of the 63 new Part 7 reserve questions (27 from v2.92.0 and 36 from v2.93.0).
3. Independent review of the 80 separate Part 5 practice questions.
4. Independent review of the 4 new vocabulary entries, sense definitions, examples, collocations, IPA and editorial CEFR estimates.
5. Independent review of Foundation A2 extended Reading, Listening and existing Writing tasks; learner validation before marking A2 complete.

### P1 — L/R coverage and product quality
1. Grow vocabulary toward 3,000 minimum and 5,000 planning target while improving US IPA, word family, verb forms, collocations, synonyms and antonyms from sources.
2. Expand and diversify Listening Part 1–4, especially reviewed unique Part 1 items; keep Mock-eligible and reserve counts separate.
3. Expand Reading Part 5–7, including multi-document inference, paraphrase and time-pressure practice.
4. Improve Grammar coverage only where it supports L/R outcomes; avoid unrelated grammar volume.
5. Build sufficient independently reviewed question inventory for multiple full Mock forms with controlled reuse.
6. Validate Full Mock timing, answer review, scoring, result analysis and local history preservation.
7. Validate responsive UI, offline cache, reconnect, TTS and data integrity on desktop, iOS, Android and tablet.

### P2 — phase transition (not active now)
- B1 remains a 12-topic four-skill blueprint only; do not implement B1 lessons or add it as a learner-selectable completed pathway before L/R acceptance.
- Do not start TOEIC Speaking/Writing until TOEIC L/R is completed and accepted.
- Do not start IELTS until the later S/W phase is completed and the owner approves the transition.

## 5. Score-readiness policy

The v2.93.0 tracker is an evidence summary, not a score predictor. A future ETS score estimate requires independently reviewed equivalent forms, a documented calibration/equating method, consented official-score validation data, sample-size policy and uncertainty reporting. Until those gates exist, show only local practice accuracy and trends. The 500+ personal goal and 850+ product target remain goals, not algorithmic predictions.

## 6. Release acceptance status

- Local source/data gates: PASS as listed in `TEST_REPORT_TOEIC_Dictionary_v2.93.0.md`.
- Independent content review: PENDING.
- Learner validation: PENDING.
- GitHub Actions: NOT VERIFIED in this release session.
- GitHub Pages deployment: NOT VERIFIED in this release session.
- Real browser/device QA: NOT VERIFIED in this release session.

## 7. Next development policy

Do not split the next work into small user-facing releases. Continue to consolidate a substantial L/R batch and close related content, quality, Mock and UX work together. The user will perform one consolidated acceptance test after the agreed release package is complete. v2.93.0 is the consolidated acceptance-test target requested by the user. Hold the next release until the user returns this test round and the findings are recorded in Master.
