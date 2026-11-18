# TOEIC Dictionary — Overall Roadmap Status v2.92.0

**Snapshot:** 2026-11-18  
**Source baseline:** v2.92.0  
**Product direction:** TOEIC-first; IELTS remains deferred.

## Executive assessment

The project now has a substantial local-first learning platform and growing TOEIC content libraries. v2.92.0 is a larger content batch: 8 Grammar lessons / 24 exercises, 6 Listening sets / 18 questions, and 6 Reading Part 7 resources / 27 questions. The 12 new Listening/Reading resources are available for practice but remain pending independent review and excluded from Mock eligibility.

**Overall state: advanced product foundation; expanding content coverage; acceptance and editorial closure still pending.** No single global completion percentage is reported because there is no approved total denominator or workstream weighting.

## Roadmap workstreams

| Workstream | Current inventory / evidence | State | Remaining gate |
|---|---|---|---|
| PWA / local-first platform | GitHub Pages static PWA, Service Worker shell, local progress stores, IndexedDB v1 | Implemented locally | GitHub Actions, Pages, offline/reconnect and real-device acceptance |
| Vocabulary | 1,137 headwords; 1,044 US IPA; 276 word-family records; 325 verb-form records | In progress | Reach 3,000 minimum; improve metadata; independent lexical/CEFR review |
| Grammar | 41 lessons / 110 exercises; 8 new lessons / 24 exercises in v2.92.0 | Expanded | Define total target; editorial review; further coverage of TOEIC grammar objectives |
| Listening | 113 units / 219 questions; v2.92.0 adds 6 units / 18 questions | Expanded; mixed review states | Independently review 117 pending questions; preserve Mock eligibility boundary; add distinct reviewed Part 1 items for second zero-repeat Full form |
| Reading | 57 resources / 227 questions; v2.92.0 adds 6 Part 7 resources / 27 questions | Expanded; mixed review states | Independently review reserve Part 7 items and semantic distractors; retain source evidence |
| Separate Part 5 practice | 80 questions | Practice-only; review pending | Independent item-level review before any Mock promotion |
| Foundation Pre-A1–A2 | 23 lessons; 23 core Reading / 59 Q; 23 core Listening / 59 Q; A2 supplementary Reading and Listening each 13 resources / 39 Q; 26 A2 writing tasks | Strong base; A2 not accepted | Independent review of extended content and writing; real learner validation; verify all skill outcomes |
| Foundation B1–C1 | 12-unit B1 curriculum blueprint added; only Pre-A1/A1/A2 have actual learner lessons | Design stage | Approve blueprint, author all four skills, define evidence and review gates before exposing B1 in stage selector |
| Learning outcomes | 33 criteria defined; 6/33 have evidence collection; 11/11 objective groups have linked resource paths | Framework present; evidence partial | Instrument remaining valid outcomes without conflating collection with mastery |
| Robot Buddy | 500 offline dialogue variants, 59 help messages, 6 FAQ, 16 quick prompts; optional read-only local insights | Implemented locally | Physical-device UX/accessibility and offline verification |
| IELTS | Deferred | Not started by design | Start only after TOEIC acceptance gates and owner approval |

## Quantitative checkpoints

- Vocabulary: **1,137 / 3,000 minimum = 37.9%**; **1,137 / 5,000 planning ceiling = 22.7%**. These are headword counts, not quality scores.
- Grammar: **41 lessons / 110 exercises**; no approved total target, so no completion percentage.
- Listening: **113 units / 219 questions**; no approved total target. v2.92.0 adds 3 Part 3 conversations and 3 Part 4 talks.
- Reading: **57 resources / 227 questions**; no approved total target. Part 7 has 135 questions (70 single-passage / 65 multiple-passage by the current classification).
- Foundation stages represented: **3/6** (Pre-A1, A1, A2). B1 blueprint is not an implemented stage.
- Objective resource mapping: **314/314 canonical resources linked** after adding v2.92.0 Grammar, Listening and Reading IDs. This is structural linkage, not quality approval or mastery.
- Learning outcomes: 33/33 criteria defined; 6/33 evidence collection paths instrumented. Neither is learner mastery.

## v2.92.0 content batch 024

- Grammar: 8 lessons / 24 exercises on conditionals, reported speech, comparisons, countability/quantifiers, gerunds/infinitives, passive voice, relative clauses and time/deadline prepositions.
- Listening: 6 sets / 18 questions (3 Part 3, 3 Part 4), with Vietnamese transcript translations, Vietnamese rationales and exact transcript evidence.
- Reading: 6 Part 7 resources / 27 questions (3 single and 3 double passages), with Vietnamese passage translations, Vietnamese rationales and source-label/quote evidence.
- SHA-256 registry: `tools/content-batch-024-v2.92.0.json` protects all 20 new resource objects.
- New Listening and Reading resources remain `reserve-pending-independent-review`, practice-only and excluded from Mock. No item is described as independently approved.
- B1: a 12-unit four-skill blueprint is supplied for review, not exposed as a selectable or completed learner pathway.

## Acceptance gates

| Gate | State | Evidence needed |
|---|---|---|
| Local data/content validation | PASS | `validate-data.py`, `validate-learning-content.py`, batch-024 regression and content audits |
| Objective resource mapping | PASS | 314/314 resource IDs resolve to canonical inventory |
| Version/design synchronization | PASS | Version 2.92.0 and canonical design profile checks |
| Independent editorial review | PENDING | Named second reviewer, item-level decisions, corrections and explicit approval |
| Learner validation | PENDING | Learner completes Foundation tasks and reports comprehension/usability/audio findings |
| Remote GitHub Actions / Pages | NOT VERIFIED | Push source, record CI run and confirm deployed version |
| Browser/device QA | NOT VERIFIED | 15.6-inch desktop at 100%, mobile/iOS/Android, offline/reconnect, cache refresh and TTS |
| Production acceptance | HOLD | Close editorial, CI, deployment and device gates |

## Next consolidated development wave

1. Expand vocabulary toward 1,500+ in carefully audited batches, with IPA only where pronunciation evidence is reliable.
2. Add another coherent Grammar/Reading/Listening content batch only after defining its contribution to the mock blueprint and review workflow.
3. Prepare independent review handoffs for Listening batches 013–024, Part 7 reserve items, Part 5 practice and Foundation A2 extended content.
4. Finalize the B1 design baseline before creating actual B1 lessons; maintain four-skill balance and local evidence scopes.
5. Add further objective-evidence instrumentation only where the existing data can support valid conclusions.
6. After the user accepts the consolidated release, run a single broad learner/device acceptance cycle and record all defects against the v2.92.0 baseline.

## Non-negotiable preservation rules

- No IndexedDB schema migration or learner progress reset without explicit approval.
- Keep GitHub-only learning data local to the device; do not upload personal learner progress.
- Do not treat device SpeechSynthesis as authentic ETS audio.
- Do not promote pending-review content into Mock pools.
- Do not describe practice thresholds, inventory counts or placement samples as official CEFR/ETS certification or learner mastery.
- Keep IELTS deferred until TOEIC is ready and the owner approves the phase change.
