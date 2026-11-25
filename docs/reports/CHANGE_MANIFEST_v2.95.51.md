# Change Manifest — TOEIC Dictionary v2.95.51

## Scope

1. Batch 040: exact-guarded enrichment of six existing Related Glossary rows: `charge`, `move`, `leave`, `opening`, `suggestion`, `location`.
2. Added `tools/build-related-glossary-enrichment-queue.py`, a deterministic read-only prioritizer based on relation-reference frequency, distinct source headwords and quality priority.
3. Added six queue/patch contract tests inside the existing quality audit test module; updated historical regression reconstruction to reverse later batches in descending order; refreshed dynamic quality-count expectations.
4. Registered syntax checks, focused tests and queue generation in `.github/workflows/validate-data.yml`.
5. Updated version markers, changelog, Master, current/previous version ledger and release reports.

## Protected data / invariants

- Related Glossary row count remains 567; no new glossary identity was created.
- No canonical vocabulary headword, ID, sense, synonym or antonym relation changed.
- No Listening / Reading / Grammar / Part 5 question, choice, answer key or Mock eligibility changed.
- No IndexedDB schema, learner record, review history or Mock history changed.
- No UI redesign, CSS/layout change, backend, Cloudflare, GAS or iframe change.

## Files of particular interest

- `data/related-terms.json`
- `patches-related-terms/v2.95.51/related-terms-040.json`
- `patches-related-terms/v2.95.51/batch-040-glossary-ledger.json`
- `tools/build-related-glossary-enrichment-queue.py`
- `tools/tests/test_related_glossary_quality_audit.py`
- `tools/tests/glossary_test_helpers.py`
- `tools/tests/test_related_glossary_backfill_025.py`
- `tools/tests/test_related_glossary_batch_034.py` through `037.py`, `test_related_glossary_batch_038.py`, `test_related_glossary_batch_039.py`
- `.github/workflows/validate-data.yml`

## Test status

- Full Python suite: 90 modules / 701 cases; 700 PASS, 1 accepted environment SKIP, 0 fail/error/timeout/not-run.
- Data validator, objective audit, resource audit and version sync: PASS.
- Workflow replay status and package verification are in their dedicated reports.
