# Related-term Glossary Expansion — v2.95.15

## Purpose

This batch fills the four highest-frequency remaining gaps in the exact synonym/antonym term join. Each selected term occurs at least three times in existing canonical vocabulary relationships. The additions are lookup glosses only; no synonym/antonym relationship or canonical headword was changed.

| Term | POS | Vietnamese gloss | Current reference count | Source |
|---|---|---|---:|---|
| `aim` | n | mục tiêu; mục đích; điều hướng tới hoặc nhằm đạt được | 3 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/aim) |
| `avoid` | v | tránh; né; phòng tránh hoặc ngăn điều gì xảy ra | 3 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/avoid) |
| `cause` | n/v | nguyên nhân; lý do; gây ra hoặc khiến điều gì xảy ra | 3 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/cause) |
| `conceal` | v | che giấu; giấu đi; giữ kín để người khác không nhìn thấy hoặc biết được | 3 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/conceal) |

## Coverage after the patch

- Related-term glossary: **387 entries**, up from 383.
- Canonical synonym/antonym data references: **804 distinct terms** across **1,037 occurrences**.
- Exact case-insensitive term join: **376/804** distinct terms have a glossary entry; **428** distinct terms remain without one.
- At occurrence level: **465/1,037** synonym/antonym links still reference a term without a gloss.
- The four additions account for 12 previously unglossed link occurrences.
- The validator's informational counter now reports `321/804` under its own legacy counting rule. It is not the same measure as the exact case-insensitive term join above and should not be compared as though the denominators were defined identically.

## Editorial status

**Provisional — independent lexical review pending.** Cambridge Dictionary entries support the concise English definitions and the Vietnamese paraphrases. The POS labels reflect the forms used by the existing relationship graph: `aim` as a noun; `avoid` and `conceal` as verbs; `cause` as noun/verb. A reviewer should still confirm contextual sense fit before approval.

## Integrity boundary

No headword, stable ID, topic, synonym array, antonym array, word-family relation, question, answer key or learner record was modified. Provenance ledger: `data/vocabulary/batch-022.json`; safe patch: `patches-related-terms/v2.95.15/related-terms-001.json`.
