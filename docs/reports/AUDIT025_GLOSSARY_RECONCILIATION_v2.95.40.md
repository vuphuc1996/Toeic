# Audit 025 — Glossary metric reconciliation (v2.95.40)

## Finding

The reported `527 != 519` failure was caused by a stale test expectation, not eight duplicate glossary rows.

- The `519` expectation represented the pre-Batch-033 glossary inventory (v2.95.34/v2.95.35).
- v2.95.39 Batch 033 added eight valid Cambridge-sourced terms: `ability`, `acceptable`, `action`, `accusation`, `advertise`, `advise`, `allow`, `announce`.
- The current canonical source `data/related-terms.json` therefore contains **527 raw rows**.
- Recount with NFKC normalization, collapsed whitespace and case-folding: **527 unique terms; 0 duplicate rows**.
- No row was deleted and the test was not changed to make invalid data fit a target count.

## Correction

1. Changed `test_major_release_quality_audit_025.py` to compare `relatedGlossary.entries` with the canonical JSON row count, assert the current 527-entry inventory, and validate unique/duplicate counters.
2. Extended `tools/audit-major-release.py` to report `entries` (raw rows), `uniqueEntries`, and `duplicateEntries` explicitly. Relation matching uses NFKC/whitespace/case-fold normalization.
3. Regenerated the current audit and glossary candidate/backlog/quality reports.
4. Retained the existing CI registration for the Audit 025 regression suite.

## Additional adjacent defect closed

The Batch 030 test loader previously globbed every `data/vocabulary/*.json`, accidentally treating editorial `batch-*.json` snapshots as canonical vocabulary. It now reads only the 26 A–Z files listed in `data/manifest.json`.

That exposed one stale current glossary definition for `revision`: its related-term row still contained `revision: sự sửa đổi; bản chỉnh sửa.` while the current exact single-sense canonical entry provides `a change made to something after it has been reviewed, or a version containing such changes`. Batch 034 corrected only `definition_en` with an exact expected-old-value + SHA-256 guard and atomic write. Vietnamese meaning, POS, term identity, `sourceHeadword`, `sourceRelease` and `sourceSenseIndex` remain unchanged.

## Verified current metrics

| Metric | Result |
|---|---:|
| Raw glossary rows | 527 |
| Normalized unique terms | 527 |
| Duplicate normalized rows | 0 |
| Referenced unique relation terms | 804 |
| Covered unique relation terms | 516 (64.2%) |
| Remaining unglossed unique terms | 288 |
| Missing reference occurrences | 289 |
| Placeholder English definitions | 73 |
| Canonical headword-sense backfills | 205 |
| Glossary entries flagged for review | 227 / 527 |
| Duplicate groups in quality audit | 0 |

Quality flags overlap by entry; priority counts are mutually exclusive: high 223, medium 2, low 2.

## Scope and limits

- Glossary additions and all existing terms remain intact; the one `revision` English definition was aligned with its current canonical sense.
- No canonical vocabulary headword IDs, synonym/antonym arrays, learner records, IndexedDB schema, learning questions/answer keys, UI or Mock eligibility changed.
- This audit verifies data-count consistency and exact-source alignment. Batch 033 dictionary research and glossary definitions still require independent lexical/editorial review.
