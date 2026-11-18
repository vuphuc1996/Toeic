# Project Roadmap Status — v2.94.0

**Date:** 2026-11-18  
**Current source:** TOEIC Dictionary v2.94.0  
**Active scope:** TOEIC Listening & Reading. B1 remains blueprint-only. Speaking/Writing and IELTS remain deferred.

## 1. Fixed product targets

- **System target:** TOEIC L/R product quality intended to support learners toward 850+. This is a design target, not an individual score guarantee.
- **Personal progression target:** 500+ first, then 600, 700, 750, 800, 850 and 900+. A learner may begin below 500 and use the same system.
- **Vocabulary:** 3,000 interim minimum; 5,000 planning target.
- **Sequence:** finish and accept TOEIC L/R before building TOEIC Speaking/Writing; IELTS follows only after that phase and an explicit owner decision.

## 2. Current inventory

| Area | Current | Qualification |
|---|---:|---|
| Vocabulary | 1,141 headwords | 38.0% of 3,000 minimum / 22.8% of 5,000 plan; independent lexical review remains separate |
| Grammar | 50 lessons / 137 exercises | TOEIC L/R support; 42 examples across 17 newest lessons have bilingual breakdowns; earlier lessons remain on editorial backlog |
| Listening | 121 units / 239 questions | 102 Mock-eligible; 137 pending editorial review; covers Part 1–4 |
| Reading | 65 resources / 263 questions | Covers Part 5–7; 63 new Part 7 questions from batches 024/025 remain pending independent review |
| Separate Part 5 practice | 80 questions | Practice-only and pending independent review; excluded from Mock |
| Foundation | Pre-A1/A1/A2 implemented | B1 is blueprint only; supplementary A2 requires independent review and learner validation |
| Score Readiness | Local Full Mock history | Requires 3 qualifying 200-question Full Mocks; reports practice L/R trends, not an ETS score estimate |

No global completion percentage is asserted because multiple libraries do not yet have approved total targets and inventory is not quality, review or mastery.

## 3. v2.94.0 completed

- Fixed `question_evidence` stale CI counters and made tests derive counts from current source. The audit indexes 502 current TOEIC questions: 239 Listening + 263 Reading.
- Consolidated the speech engine after removing duplicate shadowing functions. All TTS routes use one guarded engine with synchronous first-utterance queueing, system-default retry for a failed named voice, start/end watchdogs and explicit error states.
- Corrected the obsolete fixed two-second startup message; real audible output still awaits physical-device acceptance.
- Prevented automatic mobile/tablet focus zoom in Robot Buddy by using a 16px chat-input font and usable tap targets, without disabling pinch zoom.
- Added an explicit Robot Buddy progress-analysis action and accessible per-module colored progress meters for local Cần học / Cần luyện / Cần ôn results.
- Enriched 42 bilingual examples and structured sentence analyses across the newest 17 Grammar lessons.
- Added repository integrity preflight for PWA assets, HTML/CSS/JS local references, workflow test coverage and JSON validity.
- Updated historical batch fingerprint handling and vocabulary identity checks so append-only batches 006–013 resolve to 1,141 stable canonical headwords.
- Preserved existing local data, IndexedDB v1, Mock inclusion boundaries and L/R-first roadmap.

## 4. Open quality gates

### P0 — acceptance and independent review
1. User device acceptance of Voice across Listening and Reading, including selected/default voice behavior, stop/replay and status/error feedback.
2. Mobile/tablet Robot Buddy no-focus-zoom acceptance; retain pinch zoom.
3. User acceptance of the progress dashboard and local data preservation.
4. Independent review of all 137 pending Listening questions.
5. Independent review of 63 Batch 024/025 Part 7 questions and 80 separate Part 5 questions.
6. Independent lexical review of the four Batch 013 vocabulary records and previous pending vocabulary additions.
7. Independent review and learner validation of Foundation A2 extended content.

### P1 — complete TOEIC L/R product
1. Grow vocabulary toward 3,000 minimum and 5,000 plan; improve sourced US IPA, definitions, examples, word family, verb forms, collocations, synonyms and antonyms.
2. Expand reviewed Listening Part 1–4 content and diversify question skills, voices and contexts.
3. Expand Reading Part 5–7, especially multi-document inference, paraphrase and timed comprehension.
4. Fill gaps in Grammar examples/translations/analysis, always tied to L/R outcomes.
5. Accumulate enough independently reviewed, non-duplicated questions for multiple Full Mock forms.
6. Validate Mock timing, selection, answer review, scoring, score readiness and local result history.
7. Complete production/device validation: GitHub Actions, Pages cache, desktop at 100%, iOS, Android, tablets, offline/reconnect and TTS.

### P2 — deferred phases
- B1 remains a curriculum blueprint only, not a learner pathway.
- Do not implement TOEIC Speaking/Writing before L/R is complete and accepted.
- Do not begin IELTS before the later S/W phase and explicit owner approval.

## 5. Score readiness policy

The current tracker is an evidence summary, not a calibrated prediction. It shows local L/R accuracy trends from three completed Full Mocks. A genuine ETS score estimate requires equivalent independently reviewed forms, a documented equating/calibration method, consented official-score validation, a defined sample-size policy and uncertainty reporting. Until that exists, do not label a learner “ready for 500+ / 850+” from raw accuracy alone.

## 6. v2.94.0 verification and release status

- JavaScript regression suites: 33/33 PASS.
- Impacted Python modules: question evidence 6/6; TTS readiness 14/14; Grammar example quality 4/4; responsive layout 7/7; content batches 024/025 + vocabulary identity 18/18; project progress 4/4; CI coverage 2/2; repository integrity 1/1.
- Vocabulary validator: 1,141 records / 0 new errors / 0 warnings (legacy baseline retained).
- Learning content: 0 errors / 0 warnings; objective links 339/339; distractor audit 240 questions; Foundation A2 audit PASS; photos 9/9.
- Repository integrity preflight: 361 local references/data files / 0 errors / 0 optional warnings.
- Version synchronization and design profile PASS (54 tokens / 406 legacy font-floor selector groups).
- Complete Python discovery exceeded the local time limit; remote GitHub Actions has not been run/verified in this session.
- GitHub Pages deployment, production cache, real browser audio, physical-device visual QA and user acceptance remain pending.

## 7. Next gate

The next action is the consolidated user acceptance test in `USER_ACCEPTANCE_TEST_v2.94.0.md`. Do not open another development release before its results are recorded in the Master ledger. After acceptance, close defects as one prioritized batch and then continue substantial L/R expansion.
