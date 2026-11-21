# US IPA Backfill — v2.95.18 / Batch 024

## Scope and result

- Base release: v2.95.17.
- Candidate release: v2.95.18.
- Updated 13 existing canonical headwords with source-checked US IPA.
- US IPA coverage: **1,048/1,141 (91.8%) → 1,061/1,141 (93.0%)**.
- Remaining blank entries: **80**.
- Stable headword count and ID-set SHA-256 unchanged: `adccbdb4c98872207d2bede7bdc530e1c079bbd8b3679e7e4f6288054c7e404b`.
- Only `/phonetic/us` was changed. All changes require the previous value to be blank.

## Source-backed records

| Stable ID | Headword | US IPA | Source |
|---|---|---|---|
| `accountable-adj` | accountable | `/əˈkaʊn.t̬ə.bəl/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/accountable) |
| `admission-n` | admission | `/ədˈmɪʃ.ən/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/admission) |
| `backlog-n` | backlog | `/ˈbæk.lɑːɡ/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/backlog) |
| `carrier-n` | carrier | `/ˈker.i.ɚ/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/carrier) |
| `confidentiality-n` | confidentiality | `/ˌkɑːn.fə.den.ʃiˈæl.ə.t̬i/` | [Cambridge pronunciation](https://dictionary.cambridge.org/pronunciation/english/confidentiality) |
| `creditor-n` | creditor | `/ˈkred.ɪ.t̬ɚ/` | [Cambridge pronunciation](https://dictionary.cambridge.org/pronunciation/english/creditor) |
| `credential-n` | credential | `/krɪˈden.ʃəl/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/credential) |
| `designation-n` | designation | `/ˌdez.ɪɡˈneɪ.ʃən/` | [Cambridge pronunciation](https://dictionary.cambridge.org/pronunciation/english/designation) |
| `documentation-n` | documentation | `/ˌdɑː.kjə.menˈteɪ.ʃən/` | [Cambridge pronunciation](https://dictionary.cambridge.org/pronunciation/english/documentation) |
| `duration-n` | duration | `/duːˈreɪ.ʃən/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/duration) |
| `eligible-adj` | eligible | `/ˈel.ə.dʒə.bəl/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/eligible) |
| `emerge-v` | emerge | `/ɪˈmɝːdʒ/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/emerge) |
| `exemption-n` | exemption | `/ɪɡˈzemp.ʃən/` | [Cambridge pronunciation](https://dictionary.cambridge.org/pronunciation/english/exemption) |

## Exclusions and limitations

- `advocate`, `affiliate` and `approximate` were not filled in this batch because the selected canonical IDs cover parts of speech with different pronunciations; a singular `phonetic.us` field must not hide the variant.
- Other blank headwords remain blank until a directly verified US reading is selected. No pronunciation is inferred from spelling.
- Cambridge US forms were copied into the project's existing IPA display convention. Independent phonetic review remains pending; “source-checked” is not the same as final editorial approval.
- Provenance ledger: `data/vocabulary/batch-024.json`; guarded patch: `patches/v2.95.18/batch-001-ipa.json`; regression: `tools/tests/test_ipa_backfill_batch_024.py`.
