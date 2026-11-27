# Data Difference Report — v2.95.72 vs v2.95.71

## Baseline

- Sole predecessor: `TOEIC_Dictionary_v2.95.71_FullSource.zip` (GitHub `vuphuc1996/Toeic` `main` commit `256ca21461e78a7685bed773ddd622a64050e33a`).
- Baseline records: 1,141 canonical headwords, 567 Related Glossary entries.

## `data/` comparison

- Files in target: 68
- Added/removed data files: 0 / 0
- Modified data files:
  - `data/manifest.json`: version `2.95.71` → `2.95.72`, `totalWords` `1141` → `1181`, release addition IDs populated for Batch 026, release repair profile added for `1141`.
  - `data/related-terms.json`: 65 existing records remediated in Batch 046 (36 placeholders, 2 missing provenance, 27 missing definitions); term identities, Vietnamese meanings, and relation arrays preserved.
  - `data/vocabulary/[A-Z].json`: 40 canonical records added for Vocabulary Batch 026.
- All other data files are byte-identical.

## Protected identities and learning data

- Canonical vocabulary: 1,181 records (+40 Batch 026 additions; original 1,141 preserved).
- All 567 Related Glossary entries retain their term identity.
- No question IDs, choice IDs, answer keys, protected learning-bank files, Mock eligibility, learner IndexedDB schema or data migrations changed.

## Validation

`tools/validate-data.py`: **PASS**, 1,181 records, 0 errors, 0 legacy warnings, +40/−0 IDs.
