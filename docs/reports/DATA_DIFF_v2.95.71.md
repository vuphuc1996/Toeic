# Data Difference Report — v2.95.71 vs v2.95.70

## Baseline

- Sole predecessor: `TOEIC_Dictionary_v2.95.70_FullSource.zip`
- SHA-256: `1a0df44d309d127df3d3fb5012e7a6654c93a450c591f1f67575f4d15822e672`
- ZIP CRC and extraction were verified before edits; baseline contained 864 files.

## `data/` comparison

- Files in predecessor: 68
- Files in target: 68
- Added / removed data files: 0 / 0
- Two data files changed:
  - `data/manifest.json`: only the `version` value changes `2.95.70` → `2.95.71`.
  - `data/related-terms.json`: 23 existing records receive the five approved metadata fields in Batch 045; no record is added/deleted, no term identity changes, no Vietnamese meanings or relation arrays change.
- All other 66 data files are byte-identical.

## Protected identities and learning data

- Canonical vocabulary: 1,141 records; baseline IDs +0 / −0; ID-set SHA-256 `adccbdb4c9887220…`.
- All 567 related-glossary entries retain their term identity.
- No question IDs, choice IDs, answer keys, protected learning-bank files, Mock eligibility, learner IndexedDB schema or data migrations changed.
- No learner device IndexedDB database was available for direct record-by-record inspection; the source makes no schema or migration change.

## Validation

`tools/validate-data.py`: **PASS**, 1,141 records, 0 errors, 0 legacy warnings, +0/−0 IDs.
