# Lexical Audit — Batch 002 (v2.10.2)

**Base:** v2.10.1  
**Target:** v2.10.2  
**Data:** 928 records / 928 stable IDs / 26 A–Z files  
**ID-set SHA-256:** `dd1705e64c8df4ad7ebca188a6ad856fff1d180d99730d2d77d2ba6fbdc12656`

## Scope and result

| Area | Operations | Coverage before | Coverage after |
|---|---:|---:|---:|
| US IPA additions | 11 | 563/928 | 574/928 |
| Word Family | 9 | 122/928 | 131/928 |
| New headwords | 0 | 928 | 928 |
| Changed IDs | 0 | 928 | 928 |

### IPA records

`absence-n`, `absorb-v`, `accommodate-v`, `accountant-n`, `accounting-n`, `accurate-adj`, `activate-v`, `additional-adj`, `adequate-adj`, `adjacent-adj`, `administration-n`. All were previously blank in `phonetic.us`; values and source URLs are listed in `docs/sources/SOURCES_TOEIC_Dictionary_v2.10.2.md`.

### Word-family records

`accommodate-v`, `accommodation-n`, `accountant-n`, `accounting-n`, `administration-n`, `administrative-adj`, `administrator-n`, `annual-adj`, `annually-adv`. All linked headwords already exist; no speculative new lexemes were added.

## Guarded patching

- `patches/v2.10.2/batch-001-ipa.json`: 11 operations on `/phonetic/us`.
- `patches/v2.10.2/batch-002-word-family.json`: 9 operations on `/word_family`.
- Both patch files use `baseDataVersion=2.10.1`, `targetDataVersion=2.10.2`, the stable ID SHA-256 and `expect.old`.
- Both dry-runs passed before apply.

## Remaining data gaps

- IPA: 354/928 records still blank. Next batch should prioritize common TOEIC/General English items and must cite a reliable pronunciation source for each record.
- Word Family: 797/928 records still have an empty family list. Many records legitimately have no useful derivational family among current headwords; do not invent or add off-dictionary forms just to raise coverage.
- Synonym/antonym glossary: 312 relation terms remain without a reference gloss under the current validator statistic; next audit should resolve context/sense and glossary meaning, not copy a generic meaning across unrelated senses.
- CEFR remains editorial-estimate unless a specific sense-level source supports a change. No CEFR reclassification was made in this batch.
