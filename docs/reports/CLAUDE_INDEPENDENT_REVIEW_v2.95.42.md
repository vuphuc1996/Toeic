# Independent Claude Review Brief — TOEIC Dictionary v2.95.42

## Review target
- Candidate: TOEIC Dictionary v2.95.42 FullSource
- Baseline: v2.95.41
- Review style: independent, skeptical, evidence-first; do not assume release notes are correct.

## What this candidate consolidates
- v2.95.39 regression-test maintenance foundation and canonical vocabulary boundaries.
- v2.95.40 glossary metric reconciliation and guarded canonical correction (revision).
- v2.95.41 Listening reserve regression: 102 eligible + 193 pending = 295; Batch 027 remains reserve pending.
- v2.95.42 release-acceptance runner with command sequencing, timeout handling, captured output, report generation and fail-fast semantics.

## New v2.95.42 implementation to inspect
- `tools/run-release-acceptance.py`
- `tools/tests/test_release_acceptance_runner.py`
- CI registration in `.github/workflows/validate-data.yml`
- Changelog and version synchronization for 2.95.42

## Questions for review
1. Is the acceptance runner safe, deterministic, portable on Python 3.12, and does it correctly record non-zero exit codes and timeouts?
2. Does fail-fast behavior hide useful downstream diagnostics, and should separate fast/full profiles be introduced?
3. Are report paths/version labels reliable when `--root`, `--report-dir`, or `--version` is overridden?
4. Does its audit sequence cause expected report-file mutations or side effects? Identify any unexpected writes.
5. Are runner tests meaningful and sufficient? Identify untested failure paths (timeout, subprocess exception, non-zero, partial output, empty command list).
6. Did CI coverage registration include the new test and is there any workflow omission?
7. Check all source/data changes between v2.95.41 and candidate. Flag anything unrelated, accidental, or destructive.
8. Verify content preservation: vocabulary IDs/relations, questions, answer keys, learner progress storage, IndexedDB schema, UI, Robot Buddy, Mock eligibility.
9. Run the complete Python suite, JS suites, validators, audits, version sync, repository integrity, and packaging checks. Report exact commands, exit codes, durations, skips, and timeouts. Do not call a partial run PASS.
10. Recommend BLOCK / ACCEPT WITH FIXES / ACCEPT. Give P0–P3 issues with file and line references and actionable fixes.


## Scope constraints
- Do not silently change data, IDs, answer keys, or review states during review.
- Keep findings separate from suggested edits. Do not edit candidate source unless explicitly asked.
- Distinguish locally verified results from remote CI, Pages deployment, and real-device QA.
- The candidate is not a final release until full acceptance and external checks are complete.

## Expected review deliverable
A concise verdict, severity-ranked findings, commands/results, regression risks, data/UI preservation verification, and a prioritized next-work plan. If no critical issue is found, still list remaining release gates and areas needing content/editorial review.
