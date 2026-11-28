# Change Manifest — TOEIC Dictionary v2.95.82

**Branch:** `candidate`
**Sole predecessor:** `4d1eead800e3378cf91b5b83ddb14bc3c8fb8737` (v2.95.81)
**Target:** Part 2 lexical distractor evidence instrumentation

## Changes

1. `data/learning-path/objective-criterion-map.json`
   - Add 16 links to `listening-part-2-distractor-resistance` using existing non-reserve Part 2 items.
   - Preserve 638 unique question IDs; total links become 1,119.
2. `data/learning-path/objective-outcomes.json`
   - Instrument only the Part 2 distractor-resistance criterion; retain the 10 unique items / 80% latest-accuracy threshold.
3. `tools/audit-objective-criterion-map.py` and tests
   - Check exact prompt text, distractor choice index, non-answer-key selection, exact distractor text, repeated whole-word cue and mismatch evidence.
   - Add positive and negative regressions; keep Part 1/4/6/7 unsupported criteria uninstrumented.
4. Progress and release shell
   - Derive remaining criterion counts from the outcome registry.
   - Synchronize canonical/package/app/index/Service Worker/mock-engine markers to v2.95.82.
   - Add evidence, progress, change, command and test reports.

## Reconciliation

- Mappings: **1,119** links / **638** unique stable question IDs.
- TOEIC outcome evidence paths: **23/27**; Foundation **6/6**; total **29/33**.
- Remaining uninstrumented: Part 1 paraphrase recognition; Part 4 inference/action; Part 6 discourse purpose; Part 7 paraphrase/inference.
- Selected Part 2 resources: 16, all non-reserve. Listening reserve mappings: 0.
- Weighted measurable curriculum-build index: **74.49%** (provisional; not learner mastery or total product completion).

## Unchanged boundaries

- No question, transcript segment, option or answer key is edited. No stable question or choice identity is created or renamed.
- No vocabulary record, Mock eligibility, reserve state, learner IndexedDB record/schema, UI/layout/navigation, Robot Buddy behavior or hosting architecture changes.
- Existing multi-criterion questionKey support and local `objectiveProgress` persistence are reused.
- `main` remains at `256ca21461e78a7685bed773ddd622a64050e33a`.

## Acceptance

Exact candidate source/test HEAD `ad6401282fdb6cf86e2321339ee4181d2fc2fb21` passed GitHub Validate [run 46120842790](https://github.com/vuphuc1996/Toeic/actions/runs/46120842790) (151/151 steps; 855 Python tests) and GitHub Pages [run 46120842377](https://github.com/vuphuc1996/Toeic/actions/runs/46120842377) (build, status-report and deploy jobs). The FullSource ZIP remains not generated or verified.
