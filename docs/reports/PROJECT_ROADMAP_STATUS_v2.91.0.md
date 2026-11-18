# TOEIC Dictionary — Overall Roadmap Status v2.91.0

**Snapshot date:** 2026-11-18  
**Source baseline:** v2.91.0  
**Product direction:** TOEIC-first; IELTS remains deferred.  
**Interpretation rule:** This report separates implementation, content coverage, editorial acceptance and deployment/device acceptance. It does not calculate a single overall percentage because there is no approved global denominator or weighting across workstreams.

## Executive assessment

The project has moved beyond a basic vocabulary PWA. The current product has a broad learning shell, local-first learner data, Smart Practice/Mock workflows, Robot Buddy, objective tracking and a Pre-A1–A2 Foundation pathway. The main remaining work is no longer just adding UI modules: it is expanding the TOEIC content bank, improving dictionary metadata quality, completing higher Foundation levels, obtaining independent editorial review and passing production/device acceptance.

**Overall state: advanced product foundation, partial content completion, not yet final TOEIC acceptance.** The navigation's `Phase 5` label is a product/UI phase marker; it must not be interpreted as 100% completion of the full roadmap.

## Roadmap workstreams

| Workstream | Current evidence | Status | What remains before calling it complete |
|---|---|---|---|
| PWA / local-first platform | GitHub Pages static PWA; Service Worker shell; local learning stores; IndexedDB v1 retained | Implemented; acceptance pending | GitHub Actions, Pages deployment, offline/reconnect and browser/device checks |
| Vocabulary | 1,137 headwords; 37.9% of 3,000 minimum and 22.7% of 5,000 planning ceiling | In progress | Expand to at least 3,000; resolve 93 missing US IPA records conservatively; improve word-family/verb-form coverage; independent lexical and CEFR review |
| Smart Practice / learner workflows | Flashcards, practice, review scheduling, timed Mock and local progress tracking exist | Broadly implemented; quality gates remain | Review reserve questions, validate timed flows and verify data continuity after real deployment |
| TOEIC Grammar | 33 lessons / 86 exercises | Inventory established; total target not defined | Define coverage target and review quality; no defensible completion percentage yet |
| TOEIC Listening | 107 units / 201 questions; 102 currently Mock-eligible; 99 pending independent review | In progress | Independent review of 99 reserve questions; add 3 distinct reviewed Part 1 items for two zero-repeat Full forms |
| TOEIC Reading | 51 resources / 200 questions; two zero-overlap Full Reading forms supported by current inventory audit | In progress | Second-person review of 45 expanded Part 7 questions; keep evidence and distractor quality gates |
| Separate Part 5 practice | 80 questions | Practice-only; review pending | Independent item-level review before any promotion to Mock eligibility |
| Foundation Pre-A1–A2 | 23 lessons across 3 of 6 represented stages; 23 core Reading / 59 Q; 23 core Listening / 59 Q; 26 A2 writing tasks; extended A2 Reading and Listening each add 13 resources / 39 Q | Strong base; A2 not accepted as complete | Independent review of extended writing/Reading/Listening; learner validation; confirm all four skills and learning outcomes before closure |
| Foundation B1–C1 | Stage selector and placement mapping represent 6 bands, but only Pre-A1, A1 and A2 have lesson stages | Not built as complete pathways | Define B1 outcomes, scope, skill coverage and review gates before implementation; then B2/C1 |
| Learning outcomes / evidence | 33 criteria defined; 6/33 have evidence instrumentation (18.2%); 9/9 TOEIC objective groups wired | Framework present; evidence incomplete | Instrument remaining valid outcomes without confusing evidence collection with mastery |
| Robot Buddy / support | 500 offline dialogue variants, 59 help messages, 6 FAQ, 16 quick prompts; optional read-only local insights | Implemented locally | Real-device UX/accessibility verification; maintain privacy and evidence limits |
| IELTS | Explicitly deferred | Not started by design | Begin only after TOEIC backlog/acceptance gates and owner approval |

## Quantitative checkpoints

- Vocabulary: **1,137 / 3,000 minimum = 37.9%**; **1,137 / 5,000 planning ceiling = 22.7%**. This is headword quantity only, not quality.
- Vocabulary metadata coverage: US IPA 1,044/1,137 (91.8%); word family 276/1,137 (24.3%); verb forms 325/1,137 (28.6%); collocations 967/1,137 (85.0%); synonyms 404/1,137 (35.5%); antonyms 213/1,137 (18.7%). Field presence does not certify accuracy or usefulness.
- Guided Foundation stages represented: **3/6 (50%)** — Pre-A1, A1, A2. This is stage presence, not stage completion.
- Foundation A2 extended Listening after v2.91.0: **13 six-turn dialogues, 75–100 words each, 39 questions** covering detail, purpose/context and inference/next action. Exact source snippets and content hashes are recorded. Still pending independent review.
- Learning outcomes: 33/33 criteria defined, 6/33 evidence paths instrumented. TOEIC objective evidence is wired for 9/9 objective groups; practice thresholds are not CEFR/ETS certification.
- Grammar, TOEIC Listening, TOEIC Reading and full Foundation have no approved total target. Their inventories are shown without invented percentages.

## Acceptance gates

| Gate | Current state | Evidence required to close |
|---|---|---|
| Local automated regression | PASS for v2.91.0: 32/32 JS suites; 114/114 selected Python tests across 17 focused modules | Keep passing after each change; full Python discovery is not claimed |
| Data / content validation | PASS: 1,137 vocabulary records; learning content 0 errors / 0 warnings; Part 1 assets 9/9 | Preserve strict validators and no fabricated IPA/content |
| Version / design synchronization | PASS: version markers 2.91.0; canonical design profile 54 tokens / 400 generated typography groups | Re-run sync checks for every release |
| Independent editorial review | PENDING | Named second reviewer, item-level decisions, corrections and recorded approval; self-review is not a substitute |
| Learner validation | PENDING | Real learner completes A2 pathway tasks; collect usability, comprehension and audio feedback |
| Remote CI / Pages | NOT VERIFIED | Push the release, record GitHub Actions run and confirm the deployed commit/version |
| Device / browser QA | NOT VERIFIED | Desktop 15.6-inch at 100%, mobile/iOS/Android, landscape, TTS voice clarity, pause timing, offline/reconnect and cache refresh |
| Production acceptance | HOLD | Close relevant editorial, CI, Pages and device gates before claiming a production-stable release |

## Recommended next sequence

1. **Independent A2 review:** use `FOUNDATION_A2_LISTENING_REVIEW_CHECKLIST_v2.91.0.md` for the 13 extended Listening clips. Apply the same item-level second-person review discipline to 13 extended Reading passages and 26 A2 writing tasks. Do not change review state until a second reviewer records approval.
2. **Learner validation:** test the full A2 path on desktop and mobile, especially six-turn TTS playback, voice quality, inter-speaker pauses, transcript toggle and separate progress persistence.
3. **TOEIC exam-bank review:** prioritize 99 Listening reserve questions, 80 Part 5 practice questions and 45 expanded Part 7 questions. Keep all pending items out of Mock eligibility.
4. **Two-form Listening readiness:** add at least three distinct Part 1 questions with reviewed images/audio descriptions, then re-run the no-repeat form audit.
5. **Vocabulary quality and growth:** resolve missing IPA only with reliable pronunciation evidence; expand word families/verb forms/collocations and add carefully sourced headwords toward 3,000.
6. **B1 design before implementation:** write measurable outcomes, lesson coverage, four-skill scope, evidence model and independent-review criteria first; do not generate a superficial stage just to make the selector show 4/6.
7. **Production acceptance:** after the above changes, push and verify Actions/Pages and complete physical-device/offline tests.

## Non-negotiable preservation rules

- No IndexedDB schema migration or learner progress reset without explicit approval.
- Keep GitHub-only product and device-local learning records; do not upload personal learning data.
- Do not treat device SpeechSynthesis as authentic ETS audio.
- Do not promote pending-review questions into Mock pools.
- Do not describe practice thresholds, inventory counts or placement samples as official CEFR/ETS certification or learner mastery.
- Keep IELTS deferred until TOEIC is ready and the owner approves the phase change.
