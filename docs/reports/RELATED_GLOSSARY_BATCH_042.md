# Related Glossary Batch 042 — v2.95.61

## Scope and source identity

- Exact predecessor: `TOEIC_Dictionary_v2.95.60_FullSource.zip`.
- Predecessor SHA-256: `b4e5404b824991208d99babb3f471b45e9e27fded1d31327854ae3a15ce58838`.
- Canonical data file base SHA-256: `dbc233b11ab0b8f351092bb404fe2010f9e54091e2590c5765b68cc1b8d3f97e`.
- Patch: `patches-related-terms/v2.95.61/related-terms-042.json`; ledger: `patches-related-terms/v2.95.61/batch-042-glossary-ledger.json`.

## Completed implementation

- Enriched **20 existing Related Glossary rows** with English definitions and POS metadata. No new term row was created.
- 16 definitions are paraphrases aligned to Cambridge Dictionary entry excerpts reviewed on 2026-11-25; exact URLs are recorded in the data and ledger. Direct page retrieval returned HTTP 403 for some entries, so those records are explicitly marked as indexed-entry review rather than direct page inspection.
- 4 records (`guarantee`, `monthly`, `schedule`, `weekly`) reuse all existing canonical vocabulary sense definitions verbatim from v2.95.60. Their provenance identifies the exact canonical headword and release.
- Every target was confirmed as an existing synonym/antonym relation target; relation anchors are recorded in the ledger.
- Existing `term`, `meaning_vi`, and all canonical vocabulary relation arrays are preserved. No new canonical headwords, vocabulary IDs, examples, IPA, question/choice IDs, answer keys, Mock eligibility, learner data, IndexedDB schema, Robot Buddy scope, UI or hosting architecture were changed.

## Updated terms

| Term | POS | Existing relation anchors | Source |
|---|---|---|---|
| `enter` | `v` | `access`, `penetrate` | Cambridge Dictionary |
| `examine` | `v` | `inspect`, `review` | Cambridge Dictionary |
| `guarantee` | `n/v` | `ensure`, `warranty` | Canonical vocabulary v2.95.60 |
| `mark` | `n/v` | `date`, `label` | Cambridge Dictionary |
| `monthly` | `adj/adv` | `weekly`, `yearly` | Canonical vocabulary v2.95.60 |
| `observe` | `v` | `monitor`, `notice` | Cambridge Dictionary |
| `occasion` | `n` | `event`, `time` | Cambridge Dictionary |
| `optional` | `adj` | `necessary`, `voluntary` | Cambridge Dictionary |
| `period` | `n` | `term`, `time` | Cambridge Dictionary |
| `reach` | `v` | `access`, `contact` | Cambridge Dictionary |
| `remove` | `v` | `install`, `withdraw` | Cambridge Dictionary |
| `restriction` | `n` | `access`, `limit` | Cambridge Dictionary |
| `return` | `n/v` | `profitability`, `yield` | Cambridge Dictionary |
| `rule` | `n` | `policy`, `regulation` | Cambridge Dictionary |
| `schedule` | `n/v` | `agenda`, `itinerary` | Canonical vocabulary v2.95.60 |
| `seller` | `n` | `buyer`, `vendor` | Cambridge Dictionary |
| `shift` | `n/v` | `fluctuate`, `transfer` | Cambridge Dictionary |
| `validate` | `v` | `confirm`, `verify` | Cambridge Dictionary |
| `weekly` | `adj/adv` | `monthly`, `yearly` | Canonical vocabulary v2.95.60 |
| `business day` | `n` | `weekday` | Cambridge Dictionary |

## Quality delta

- Related Glossary entries: **567** (unchanged).
- Entries with one or more quality flags: **198 → 178** (−20).
- High-priority flagged entries: **194 → 174** (−20).
- Missing English definitions: **131 → 111** (−20).
- Missing POS: **190 → 174** (−16).
- Placeholder definitions: **63** (unchanged; no placeholder was converted without a source).
- Missing source provenance flags: **65** (unchanged).
- Normalized duplicate groups: **0**.
- Relation references across flagged entries: **212 → 173**; flagged entries used by relations: **191 → 171**.
- Candidate coverage remains 556/804; 248 unique relation terms / 249 occurrences remain uncovered and were not auto-created.

## Editorial and verification boundary

- Cambridge definitions are paraphrased, not copied examples. The exact dictionary URLs are retained per row. Sense alignment is documented in the ledger; independent editorial review remains pending.
- Four canonical definitions are exact copies from all senses of their exact current headwords; multi-sense definitions are joined only in this explicit, manually reviewed batch, not by the generic automatic backfill tool.
- Guarded patch preconditions bind to the exact pre-batch `data/related-terms.json` SHA-256. Five focused regression tests cover inventory, relation anchors, provenance, immutable meaning/identity, and exact reconstruction of the pre-batch file.

## External dictionary URLs

- [enter](https://dictionary.cambridge.org/dictionary/english/enter)
- [examine](https://dictionary.cambridge.org/dictionary/english/examine)
- [mark](https://dictionary.cambridge.org/dictionary/english/mark)
- [observe](https://dictionary.cambridge.org/dictionary/english/observe)
- [occasion](https://dictionary.cambridge.org/dictionary/english/occasion)
- [optional](https://dictionary.cambridge.org/dictionary/english/optional)
- [period](https://dictionary.cambridge.org/dictionary/english/period)
- [reach](https://dictionary.cambridge.org/dictionary/english/reach)
- [remove](https://dictionary.cambridge.org/dictionary/english/remove)
- [restriction](https://dictionary.cambridge.org/dictionary/english/restriction)
- [return](https://dictionary.cambridge.org/dictionary/english/return)
- [rule](https://dictionary.cambridge.org/dictionary/english/rule)
- [seller](https://dictionary.cambridge.org/dictionary/english/seller)
- [shift](https://dictionary.cambridge.org/dictionary/english/shift)
- [validate](https://dictionary.cambridge.org/dictionary/english/validate)
- [business day](https://dictionary.cambridge.org/dictionary/english/business-day)
