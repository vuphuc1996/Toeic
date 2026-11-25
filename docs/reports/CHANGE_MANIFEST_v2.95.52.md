# Change Manifest — TOEIC Dictionary v2.95.52

## Scope

1. Batch 041: exact-guarded enrichment of eleven existing Related Glossary rows: `present`, `associate`, `contender`, `daily`, `deal`, `deny`, `direction`, `endpoint`, `fee`, `legitimate`, `occupation`.
2. Added batch ledger and patch payload with pre-batch SHA-256, exact old-value guards, Cambridge URLs, POS and sense-alignment rationale.
3. Updated the quality audit and relation-frequency queue reports to the new source counts.
4. Extended historical regression reconstruction so Batch 041 is reversed before Batch 040 and 039; refreshed backfill and candidate-audit expectations and placeholder Node guard count.
5. Registered Batch 041 syntax/test execution in `.github/workflows/validate-data.yml`.
6. Updated version markers, changelog, Master Status, current version, project documentation and release reports.

## Protected data / invariants

- Related Glossary remains 567 entries; no new term identity was created.
- Vietnamese glosses, canonical vocabulary headwords/IDs/senses and all synonym/antonym arrays are unchanged.
- No Listening / Reading / Grammar / Part 5 question, choice, answer key or Mock eligibility changed.
- No IndexedDB schema, learner record, review history or Mock history changed.
- No UI redesign, CSS/layout change, backend, Cloudflare, GAS or iframe change.

## Files of particular interest

- `data/related-terms.json`
- `patches-related-terms/v2.95.52/related-terms-041.json`
- `patches-related-terms/v2.95.52/batch-041-glossary-ledger.json`
- `tools/tests/test_related_glossary_batch_041.py`
- `tools/tests/test_related_glossary_backfill_025.py`
- `tools/tests/test_related_glossary_candidate_audit.py`
- `tools/tests/test_related_glossary_batch_039.py`
- `tools/tests/test_related_glossary_merge_038.py`
- `tools/tests/glossary_test_helpers.py`
- `tools/tests/related-glossary-quality.mjs`
- `.github/workflows/validate-data.yml`

## Test status

- Full Python suite: 91 modules / 705 cases; 704 PASS, 1 accepted environment SKIP, 0 fail/error/timeout/not-run.
- Related Glossary regression family: 131/131 PASS.
- Data validator, objective audit, resource audit and version sync: PASS.
- Workflow replay status and package verification are in their dedicated reports.
