# Change Manifest — TOEIC Dictionary v2.95.50

## Base

- Exact predecessor: `TOEIC_Dictionary_v2.95.49_FullSource.zip`
- Base SHA-256: recorded in package verification after archive validation.

## Changes

1. Related Glossary batch 039: twelve guarded updates to existing rows with Cambridge Dictionary source URLs, paraphrased English definitions, POS labels and source release metadata.
2. Added `patches-related-terms/v2.95.50/related-terms-039.json` and `batch-039-glossary-ledger.json`.
3. Added regression coverage `tools/tests/test_related_glossary_batch_039.py` and shared historical reconstruction helper `tools/tests/glossary_test_helpers.py`.
4. Updated historical glossary tests so their base-hash reconstruction reverses batch 039 before checking earlier release patches; refreshed backfill audit counts.
5. Registered batch 039 regression in `.github/workflows/validate-data.yml`.
6. Updated version markers, changelog, Master Status and quality/audit reports.

## Protected invariants

- Vocabulary IDs, headwords, sense identities and synonym/antonym arrays unchanged.
- Listening/Reading/Grammar/Part 5 questions, choices, answer keys and Mock eligibility unchanged.
- IndexedDB schema and learner history unchanged.
- UI layout and GitHub Pages-only hosting unchanged.

## Editorial boundary

The twelve definitions are Cambridge-backed paraphrases. They are source-checked but remain pending independent editorial review. No unsupported missing glossary terms were automatically created.
