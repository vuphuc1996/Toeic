# TOEIC Dictionary v2.95.42 — Consolidated Development Plan

## Objective
Carry forward the stable fixes from v2.95.39–v2.95.41 and add a reproducible release acceptance runner so the next independent review can verify a coherent candidate rather than several small patches.

## Included
1. Regression-test baseline and canonical vocabulary source boundaries.
2. Glossary raw/unique/duplicate metric distinction and guarded canonical correction.
3. Listening eligible/reserve counts and fail-closed reserve policy.
4. New release acceptance runner: ordered checks, fail-fast, per-command timeout, captured logs, JSON/Markdown output.
5. Five focused runner tests and CI registration.
6. Claude review brief and acceptance scope.

## Non-goals / preserved
- No new UI or UX feature.
- No learner-record migration, IndexedDB schema change, or progress data modification.
- No question IDs, choice IDs, answer keys, content order, editorial status, or Mock eligibility changes.
- No bulk vocabulary rewrite or guessed definitions.
- No claim of remote Actions, Pages, mobile/device QA without evidence.

## Acceptance gates
- Focused tests for the runner and CI coverage guard pass.
- Python syntax compilation and JS syntax checks pass.
- Data/content validators and version sync pass.
- Release runner dry-run lists the complete deterministic sequence.
- Full test suite completes with exit code 0 before full-suite PASS is claimed.
- Packaging integrity and source comparison pass.
- External Claude review is recorded separately and is not substituted for automated testing.

## Known content backlog carried forward
- Listening reserve questions awaiting independent review.
- Related Glossary uncovered terms and placeholder definitions.
- Learning-outcome criteria requiring instrumentation/evidence.
- Editorial quality review for Reading/Listening distractors, source evidence, naturalness, and skill alignment.
