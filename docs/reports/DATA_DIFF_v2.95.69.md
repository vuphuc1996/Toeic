# Data Difference Report — v2.95.68 → v2.95.69

## Baseline and method

- Sole predecessor: `TOEIC_Dictionary_v2.95.68_FullSource.zip`
- Predecessor SHA-256: `2313f612e536c618b91fa1462611dffba7c9539f9e1a019a9b3ac4de79941c2a`
- Predecessor archive: 816 files; ZIP CRC verified before development.
- Comparison used the extracted contents of that exact FullSource ZIP and the v2.95.69 working source, including byte comparisons for files and structural comparisons for canonical vocabulary IDs and guarded glossary fields.

## Data file differences

Exactly two existing files under `data/` differ:

1. `data/manifest.json`: only the release marker changed from `2.95.68` to `2.95.69`.
2. `data/related-terms.json`: 15 existing rows had approved metadata fields updated.

No data file was added or deleted. Every other `data/` file is byte-identical to the predecessor.

## Related Glossary rows

The 15 existing terms are: `alternative`, `area`, `attentive`, `check`, `connect`, `constantly`, `continually`, `conveyance`, `courtyard`, `depot`, `diary`, `disadvantage`, `get`, `notification`, and `products`.

Only these fields changed on each selected row: `pos`, `definition_en`, `source`, `sourceUrls`, and `sourceRelease`. No term identity, Vietnamese meaning, synonym array or antonym array changed. Each row was selected only when an existing canonical vocabulary synonym/antonym edge supplied a defensible relationship anchor. Cambridge definitions are paraphrases of indexed Cambridge Dictionary entry excerpts reviewed 2026-11-26; direct page fetch was not consistently available, and independent editorial review remains pending. No IPA or example sentences were added.

## Protected content and identity

- Canonical vocabulary: **1,141 records**; canonical IDs match exactly between predecessor and target; zero added or removed.
- Canonical word/headword records and relation arrays: unchanged.
- Protected learning-bank files: **4/4 byte-identical** (Grammar, Listening, Reading and Part 5 protected files in the comparison scope).
- TOEIC question IDs, choice IDs, answer keys and Mock eligibility: no data file changes affecting these identities/content.
- IndexedDB: no schema version, migration or persistence code change is included; installed learner databases were not directly inspected on physical devices.
- UI and Robot Buddy layout: unchanged.

The source-level comparison script asserted the exact changed data paths, 567-row glossary identity set, allowed metadata field set and canonical ID equality. It completed successfully.
