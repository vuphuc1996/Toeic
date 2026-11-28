# Change Manifest — TOEIC Dictionary v2.95.83

**Branch:** `candidate`
**Sole predecessor:** `5eb3b736c3252a38702438efbbbc75e74864189a` (v2.95.82)
**Target:** Part 4 inference/action and Part 6 discourse-purpose evidence; question-level Mock preservation.

## Changes

1. Listening Part 4
   - Append 10 next-step/action inference questions to 10 existing non-reserve original-editorial talks.
   - Add stable choice IDs, exact audio quote, inference type and rationale.
   - Set `mockEligible: false` on all ten new questions; existing three-question talk blocks remain unchanged.
2. Reading Part 6
   - Add 10 mappings to existing questions in four `internal-editorial-reviewed` resources.
   - Store exact passage excerpt, canonical correct-choice text, discourse function and rationale; no question or answer key is edited.
3. Outcome and evidence audit
   - Instrument `listening-part-4-inference-action` and `reading-part-6-discourse-purpose` only.
   - Add fail-closed Part 4/Part 6 validators and positive/negative regressions.
   - Update the registry, dynamic progress tests and criterion inventory.
4. Mock and readiness protection
   - Mock engine filters question-level `mockEligible: false` when counting pools, selecting questions and building audio groups.
   - Readiness audits count only question-eligible items; approved Part 4 Mock pool stays at 30 and total approved Listening stays at 102.
5. Independent-review handoff
   - Document Part 1 visual/provenance checks and Part 7 independent second review without promoting either criterion.
6. Release shell
   - Synchronize manifest/package/HTML/app/Service Worker/mock-engine markers to v2.95.83.

## Reconciliation

- Mapping inventory: **1,139 links / 648 unique stable question IDs**.
- TOEIC criteria with evidence paths: **25/27**; Foundation **6/6**; total **31/33**.
- New Part 4 questions: **10**, practice-only and excluded from Mock.
- New Part 6 mappings: **10**, reusing internally reviewed questions.
- Remaining uninstrumented: Part 1 paraphrase recognition and Part 7 paraphrase/inference.
- Provisional weighted measurable curriculum-build index: **76.00%**; not learner mastery or total product completion.

## Protected boundaries

- No existing question text, option, answer key, stable question/choice ID, vocabulary ID, learner IndexedDB record/schema, UI/layout/navigation, Robot Buddy behavior or hosting architecture is changed.
- Listening reserve 193, Reading Part 7 reserve 87 and Separate Part 5 review-only 80 remain Mock-excluded.
- Part 1 visual review and Part 7 independent second-review gates remain active.
- `main` stays at `256ca21461e78a7685bed773ddd622a64050e33a`.

## Acceptance

Exact-commit source validation, Mock-engine tests, full Python discovery, version synchronization and Pages deployment are pending for this candidate source commit. FullSource ZIP and device/offline QA remain separate gates.
