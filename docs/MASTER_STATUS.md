# TOEIC Dictionary — Master Status

**Phiên bản mã nguồn đang kiểm kê:** v2.95.60

**Current source:** v2.95.60 — consolidated read-only missing-US-IPA and Related Glossary quality queues, developed exclusively from the verified v2.95.59 FullSource archive.

## Current release

- Predecessor FullSource: `TOEIC_Dictionary_v2.95.59_FullSource.zip` (SHA-256 `b5dbb4e7c974814c8d59fc6bf653737f7208e7da2c2d49141078efff385d993c`).
- FullSource: `TOEIC_Dictionary_v2.95.60_FullSource.zip` (720 files; final SHA-256 is in the adjacent sidecar).
- Patch: `TOEIC_Dictionary_v2.95.60_Patch_From_v2.95.59.zip` (exact 720/720 file replay; final SHA-256 is in the adjacent sidecar).
- Package verification: `docs/reports/PACKAGE_VERIFICATION_v2.95.60.md`.
- Missing US IPA queue: 79 entries; CMUdict 1.1.3; 5 single-variant candidates, 49 multi-variant review cases, 25 no exact dictionary key. No IPA applied.
- Related Glossary: 567 entries; 198 flagged; 0 normalized duplicate groups; 248 distinct referenced terms / 249 reference occurrences remain uncovered.
- Read-only complexity report: 582 questions; 280 reserve-pending (193 Listening, 87 Reading) remain excluded from Mock.
- Data and learning-content validators: 0 errors / 0 warnings; canonical vocabulary, glossary and question data are byte-identical to v2.95.59.
- Python full suite: INCOMPLETE (17/94 modules, 126/126 cases passed in completed modules, 77 modules NOT RUN); focused new/related tests 37/37 PASS.
- Node regression: 42/42 scripts PASS; JS syntax checks PASS.
- Hosted GitHub Actions, Pages deployment, PWA cache propagation/offline behavior and physical-device acceptance remain UNVERIFIED.

## Stage 2 progress

| Audit item | Status | Notes |
|---|---|---|
| 5. Full learner data export/import | Implemented in v2.95.55 | Full IndexedDB workspace + `toeic:` localStorage backup, integrity validation and guarded merge restore |
| 6. Listening reuse / trend integrity | Implemented in v2.95.56 | Listening trend requires two distinct question-ID forms; high overlap is disclosed; Reading remains independent |
| 7. Answer leakage / distractor overlap | Implemented in v2.95.57 | Read-only lexical/length triage; 6 review signals; no answer/content mutation |
| 8. Answer-position skew | Existing implementation verified | Historical controlled reorder certificates retain stable choice identity; 27 changes in v2.17.0 and 6 in v2.33.0 |
| 9. Evidence and difficulty | Structural triage implemented; independent review/calibration open | Source evidence + transparent complexity signals; no CEFR/ETS difficulty claims |
| 10. Learning outcome accuracy | Implemented in v2.95.58 | First-attempt and latest-attempt accuracy are reported separately from the same retained attempt history |

Stage 2: **6/6 workstreams implemented (100%)**; item 9 is structurally instrumented but independent review and psychometric calibration remain external acceptance gates, not marked complete.

## Non-negotiable data boundaries

- The 193 Listening reserve questions and 87 Reading reserve questions remain excluded from Mock until independent approval.
- No vocabulary IDs/headwords/meanings/relations, question IDs, choices, answer keys, Mock eligibility, learner-history schema, or Robot Buddy access boundary changed in v2.95.58.
- The v2.95.55 complete learner-data backup and guarded restore remains intact. Existing attempt-history records are read without migration.
- UI layout and navigation were not redesigned.

## Acceptance boundary

Local source, Node tests, data validation and version synchronization are recorded. Full Python discovery was not run for this release. Hosted GitHub Actions, GitHub Pages, installed-PWA cache propagation and physical iOS/iPadOS/Android behavior remain **UNVERIFIED**.

## Previous completed work

- v2.95.56: Listening Mock form-diversity gate. See `reports/MOCK_LISTENING_FORM_DIVERSITY_v2.95.56.md`.

- v2.95.55: full learner-data backup and guarded restore. See `docs/reports/LEARNER_DATA_BACKUP_v2.95.55.md` and `docs/reports/RELEASE_ACCEPTANCE_v2.95.55.md`.
- v2.95.54: Stage 1 independent audit remediation and release evidence.

## v2.95.59 — item complexity review queue (2026-11-24)

- Added read-only complexity triage for the full Listening/Reading question inventory. Observable signals include source length, prompt length, answer-option length spread, inference/purpose wording and multi-document indicators.
- Does not infer difficulty or CEFR, does not use learner response statistics, and does not modify question content or Mock eligibility.
- Reserve-pending items remain excluded from Mock. Independent review, pilot response data and psychometric calibration remain open.

## v2.95.60 — consolidated IPA and Related Glossary quality queues (2026-11-24)

- Development base: exact `TOEIC_Dictionary_v2.95.59_FullSource.zip`; SHA-256 `b5dbb4e7c974814c8d59fc6bf653737f7208e7da2c2d49141078efff385d993c`.
- Added a deterministic missing-US-IPA review inventory from exact-headword CMUdict lookup. 79 records: 5 single-pronunciation candidates, 49 multi-variant cases requiring review, 25 with no exact dictionary key. CMUdict package version is recorded; ARPABET remains the evidence format. No IPA was converted or inserted.
- Added a Markdown renderer and regression tests for queue counts, variant display and the no-auto-apply boundary.
- Rebuilt Related Glossary quality and relation-frequency queues: 567 entries; 198 flagged (194 high, 2 medium, 2 low); 131 missing definitions; 63 placeholders; 190 missing POS; 65 missing provenance; 0 normalized duplicate groups.
- Candidate coverage audit: 567 glossary entries, 804 distinct referenced terms, 248 distinct terms / 249 reference occurrences not covered; no canonical candidate was auto-imported.
- The v2.95.59 non-calibrated complexity inventory remains part of the baseline: 582 questions; 280 reserve-pending (193 Listening, 87 Reading); all reserve remain excluded from Mock.
- No canonical vocabulary fields, IDs, headwords, relation arrays, question content/IDs/choices/answer keys, learner data, IndexedDB schema, Mock eligibility, UI layout or hosting architecture changed. This release adds reports/tooling/tests and synchronized release markers only.
- Full hosted Actions, Pages deployment, cache propagation and physical-device acceptance remain unverified.
