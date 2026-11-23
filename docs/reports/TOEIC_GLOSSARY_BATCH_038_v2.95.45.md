# Related Glossary Batch 038 — v2.95.45

## Scope

Extend the lookup-only Related Glossary using terms already present in canonical synonym/antonym relationships. Preserve all canonical headwords, IDs and relation arrays.

## Five additions

| Term | POS | Vietnamese lookup meaning | English definition summary | Provenance |
|---|---|---|---|---|
| `ask for` | v phr | yêu cầu; đề nghị cung cấp | request that someone give or provide something | Cambridge Dictionary `ask` entry |
| `change` | n | sự thay đổi; sự chuyển đổi | process or result of becoming different | Cambridge Dictionary `change` entry |
| `comments` | n pl | các nhận xét; ý kiến phản hồi | remarks or opinions expressed about a subject or situation | Cambridge Dictionary `comment` entry |
| `communicate with` | v phr | liên lạc với; trao đổi thông tin với | share information or exchange messages with a person/group | Cambridge Dictionary `communicate` entry |
| `connection` | n | mối liên hệ; sự kết nối | state of being related to someone or something | Cambridge Dictionary `connection` entry |

Each row contains a part of speech, Vietnamese lookup meaning, paraphrased English definition, source description and Cambridge headword URL. No example sentence, IPA or pronunciation variant was generated.

## Three guarded sense corrections

| Term | Previous sense | Corrected sense | Relationship alignment |
|---|---|---|---|
| `caller` | person making a telephone call | visitor to a house/building | existing `visitor` anchor |
| `article` | broad entry mixing object and written-piece senses | a particular object/item | existing `item` anchor |
| `assume` | accepted-as-true sense mixed with take-responsibility sense | take responsibility, control or a role | existing `undertake` anchor |

The guarded correction patch checks the expected previous values before updating only `meaning_vi`, `pos`, `definition_en`, `source` and `sourceUrls` for the three exact terms. Relations and term identities do not change. Previous and corrected values are retained in `patches-related-terms/v2.95.45/glossary-corrections-038.json` and the batch ledger.

## Patch/provenance

- Addition patch: `patches-related-terms/v2.95.45/related-terms-038.json`
- Correction patch: `patches-related-terms/v2.95.45/glossary-corrections-038.json`
- Ledger: `patches-related-terms/v2.95.45/batch-038-glossary-ledger.json`
- The addition patch is based on the post-correction `related-terms.json` SHA-256 recorded in the patch.
- Canonical vocabulary and protected learning-bank fingerprints are included in the ledger/tests.

## Result

- Related Glossary: 562 → 567 rows.
- Normalized unique terms: 567; duplicates: 0.
- Exact relation coverage: 551/804 (68.5%) → 556/804 (69.2%).
- Remaining: 248 unique terms / 249 occurrences.

## Verification and limitations

Batch-specific tests: 8/8 PASS. Historical Batch 035–037 tests were also updated and rerun to reconstruct their original baselines despite the later guarded corrections.

Cambridge definitions were paraphrased from dictionary entries/search excerpts; some Cambridge entry pages may not be directly fetchable in this environment. The per-record Cambridge URLs are retained. These records remain provisional pending independent lexical/editorial review; the source check is not a second-person pedagogical approval.
