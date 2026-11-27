# Change Manifest — TOEIC Dictionary v2.95.76

**Base branch:** `candidate`
**Base commit:** `d5648916cf62b3f07b1ffb9b98425c48ff3e63fe`
**Target source version:** `2.95.76`

## Content changes

- Add 40 canonical vocabulary records in 11 A–Z runtime files and provenance ledger `data/vocabulary/batch-028.json`.
- Add Vietnamese transcript translations to 8 existing Listening resources (4 Part 3, 4 Part 4).
- Update vocabulary manifest counts and CEFR estimates to 1,221 headwords.
- Add regression coverage for Batch 028 and full Listening unit translation availability.
- Update historical Batch 026/027 test reconstruction so later additions do not contaminate historical snapshots.
- Refresh project progress, TOEIC content coverage, vocabulary and listening remediation reports.

## Protected

No existing canonical vocabulary ID/headword/sense, question/choice ID, answer key, Mock eligibility, learner IndexedDB schema/record, UI layout or service architecture was changed. All 360 existing reserve questions remain reserve-pending and excluded from Mock.

## Verification boundary

Hosted CI, Pages deployment, FullSource archive creation, installed-PWA cache propagation and physical-device QA must be reported only from exact remote evidence; they are not inferred from this manifest.
