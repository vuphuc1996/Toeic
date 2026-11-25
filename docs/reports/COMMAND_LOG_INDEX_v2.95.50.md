# Command Log Index — TOEIC Dictionary v2.95.50

## Data / version

- `python tools/update-related-terms.py --patch patches-related-terms/v2.95.50/related-terms-039.json --dry-run` — PASS.
- `python tools/update-related-terms.py --patch patches-related-terms/v2.95.50/related-terms-039.json --apply` — PASS; 12 exact-guarded updates.
- `python tools/sync-version.py --check` — PASS; all 13 markers and changelog synchronized.
- `python tools/validate-data.py` — PASS; 1,141 records, zero ID changes, 0 ERROR / 0 WARNING.
- `python tools/audit-learning-outcomes.py` — PASS; 11 objectives / 33 criteria; 6 evidence paths.
- `python tools/audit-objective-resources.py` — PASS; 379/379 linked.
- `python tools/audit-related-glossary-quality.py` — PASS; 567 rows, 215 flagged, 356 definitions present, 140 missing, 71 placeholders.
- `python tools/audit-related-glossary-candidates.py` — PASS; 248 uncovered unique relation terms / 249 occurrences.

## Focused tests

- Batch 039 regression: 4/4 PASS.
- Related glossary quality audit: 11/11 PASS.
- Related glossary candidate audit: 4/4 PASS.
- Batch 038 historical reconstruction: 8/8 PASS.
- Backfill 025 history: 6/6 PASS.
- Batch 034 / 035 / 036 / 037 historical reconstruction: 6/6 / 5/5 / 6/6 / 7/7 PASS.
- Patch-related-terms safety tests: 11/11 PASS.
- Related-term explanation context: 4/4 PASS.
- Node related-glossary display-safety regression: PASS.
- Python syntax compilation for changed test/tool files: PASS.

## Incomplete checks

- Full 90-module Python suite: INCOMPLETE due repeated outer execution timeouts. Historical tests that failed against the new live data were corrected and individually rerun; this does not replace the full-suite run.
- Full local replay of every workflow `run:` step: INCOMPLETE.
- Hosted GitHub Actions / Pages deployment / physical-device acceptance: UNVERIFIED.
