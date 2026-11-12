# Vocabulary Batch 003 — v2.11.0

**Status:** Applied after patch dry-run. No new headwords or ID changes.

| ID | Headword | Field | New US IPA |
|---|---|---|---|
| allowance-n | allowance | `phonetic.us` | /əˈlaʊ.əns/ |
| annually-adv | annually | `phonetic.us` | /ˈæn.ju.ə.li/ |
| appoint-v | appoint | `phonetic.us` | /əˈpɔɪnt/ |
| approval-n | approval | `phonetic.us` | /əˈpruː.vəl/ |
| asset-n | asset | `phonetic.us` | /ˈæs.et/ |
| availability-n | availability | `phonetic.us` | /əˌveɪ.ləˈbɪl.ə.t̬i/ |

- Patch: `patches/v2.11.0/batch-001-ipa.json`.
- Operations: 6. `baseDataVersion=2.10.2`, `targetDataVersion=2.11.0`, locked by baseline ID-set SHA-256 and `expect.old`.
- `python tools/patch-data.py --patch ... --dry-run`: PASS; apply: PASS.
- IPA count increased 574 → 580 / 928. `annual` was already populated and was not changed.
- Sources and editorial caveats: `docs/sources/TOEIC_SOURCES_v2.11.0.md`.
