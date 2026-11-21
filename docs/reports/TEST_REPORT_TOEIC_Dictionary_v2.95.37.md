# Test Report — TOEIC Dictionary v2.95.37


## Scope

Listening content expansion batch 027, objective-resource integration, audit/report version freshness, reserve review gating and regression compatibility.

## Implemented

- 16 original-editorial Listening resources: 8 Part 2 response items, 4 Part 3 conversations and 4 Part 4 talks.
- 32 questions total, with Vietnamese explanations, stable choice IDs, transcript evidence pointers, review notes, source/batch metadata.
- All new resources remain `reserve-pending-independent-review` and excluded from Mock.
- All 16 resource IDs mapped to Listening Part 2/3/4 objectives; objective-resource mapping is 379/379.
- Updated stale Listening reserve counts in tests and Mock-engine regression, progress report, version-aware major-release audit and dynamic distractor structural audit.

## Verification results

- Focused Python: **121 tests PASS** across 15 suites (batch 026/027, major-release audit, distractor quality, CI coverage, learning content, listening expansion, question evidence, TTS readiness, repository integrity, practice fallback, objective map, project progress).
- JavaScript regression: **39/39 `.mjs` suites PASS**.
- Vocabulary/data validator: 1,141 headwords; 0 errors / 0 warnings.
- Learning-content validator: 145 Listening units / 295 questions; 73 Reading resources / 287 questions; 58 Grammar lessons / 169 exercises; 0 errors / 0 warnings.
- Objective-resource audit: 11 objectives; **379/379 links PASS**.
- Repository integrity preflight: **407 local references/data files; 0 errors / 0 optional warnings**.
- Listening readiness: **102 eligible / 193 pending / 295 total**. Part 1 remains 8 eligible + 1 reserve; no Mock eligibility was changed.
- Question evidence audit: 582 indexed questions (295 Listening + 287 Reading); reserve classification 193.
- Distractor structural audit: **264 questions** in the scope (Mock-eligible Listening Part 3=39, Part 4=30, all Reading Part 7=195); **156** reserve Part 3/4 questions checked structurally; 12 recorded revisions; PASS.
- Version sync: PASS.

## Not verified

- Full Python test discovery was not run.
- Remote GitHub Actions/CI, Pages deployment, browser/mobile physical-device testing and independent editorial review were not performed.
- New batch 027 is not approved for Mock until a second reviewer completes the review.

## Data safety

No UI redesign, vocabulary headword IDs, glossary entries, learner progress, IndexedDB schema, answer history or existing Mock-eligible status was intentionally changed. New Listening items are review-pending and fail-closed excluded from Mock.
## Package verification — v2.95.37

- FullSource: **556 files**.
- Update Patch: **35 entries** (22 changed + 13 added), **0 deletions**.
- Patch replay on v2.95.36: **556/556 files byte-for-byte identical** to v2.95.37 FullSource.
- ZIP CRC, one-root structure, excluded-path policy and SHA-256 verification: PASS.

