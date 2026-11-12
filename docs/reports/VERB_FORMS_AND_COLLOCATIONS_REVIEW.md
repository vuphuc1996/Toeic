# v2.9.10 — Verb Forms & Collocations Review

- Base: v2.9.9; total records: 928; unique IDs: 928; ID-set SHA-256: `dd1705e64c8df4ad7ebca188a6ad856fff1d180d99730d2d77d2ba6fbdc12656`.
- Missing verb forms after POS/sense audit: 122 records. All contain at least one sense whose POS tokens include `v`.
- Curated collocations added to 39 records (two phrases each; only where the record previously had an empty list).
- POS-only noun records were not assigned verb forms. Existing 169 verb-form records were not rewritten.
- Spelling convention: US English, consistent with the dataset phonetic field `us`.

## Irregular forms checked against dictionary entries

| Headword | Third-person | Past | Past participle | -ing |
|---|---|---|---|---|
| foresee | foresees | foresaw | foreseen | foreseeing |
| undergo | undergoes | underwent | undergone | undergoing |
| underwrite | underwrites | underwrote | underwritten | underwriting |
| withhold | withholds | withheld | withheld | withholding |

Sources: Cambridge Dictionary entries for [foresee](https://dictionary.cambridge.org/dictionary/english/foresee) and [undergo](https://dictionary.cambridge.org/dictionary/english/undergo); Oxford Learner’s Dictionaries entries for [underwrite](https://www.oxfordlearnersdictionaries.com/definition/english/underwrite), [withhold](https://www.oxfordlearnersdictionaries.com/definition/english/withhold), and [incur](https://www.oxfordlearnersdictionaries.com/us/definition/english/incur).

Regular forms follow standard US English inflection rules. For debated spelling variants, this project uses `benefited/benefiting` and `channeled/channeling`; accepted alternatives are intentionally not duplicated in this compact five-field schema.

## Patch batches

- `patches/v2.9.10/batch-001.json`: 31 verb-form records; 10 collocation lists updated.
- `patches/v2.9.10/batch-002.json`: 31 verb-form records; 8 collocation lists updated.
- `patches/v2.9.10/batch-003.json`: 31 verb-form records; 12 collocation lists updated.
- `patches/v2.9.10/batch-004.json`: 29 verb-form records; 9 collocation lists updated.

All operations use `expect.old`, the base version and the SHA-256 of the complete ID set. Verb-related changes also require `expect.verbSense=true`.
