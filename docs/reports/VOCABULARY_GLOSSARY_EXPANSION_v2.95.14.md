# Related-term Glossary Expansion — v2.95.14

## Purpose

This batch fills ten Vietnamese gloss gaps for terms already used in the canonical synonym/antonym relationships. It adds supporting explanations without changing the relationship graph or canonical word list.

| Term | POS | Vietnamese gloss | Existing synonym/antonym references | Source |
|---|---|---|---:|---|
| `requirement` | n | điều kiện; yêu cầu bắt buộc | 4 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/requirement) |
| `pay` | n/v | tiền lương; khoản thanh toán; trả tiền hoặc trả lương | 4 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/pay) |
| `ignore` | v | phớt lờ; không chú ý đến | 4 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/ignore) |
| `withhold` | v | giữ lại; không cung cấp hoặc chi trả | 3 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/withhold) |
| `retain` | v | giữ lại; duy trì; giữ chân | 3 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/retain) |
| `earnings` | n (plural) | thu nhập; tiền kiếm được từ công việc; lợi nhuận doanh nghiệp | 3 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/earnings) |
| `duty` | n | nhiệm vụ; nghĩa vụ; trách nhiệm | 3 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/duty) |
| `distribute` | v | phân phát; phân phối; cung ứng | 3 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/distribute) |
| `discourage` | v | làm nản lòng; khiến ai ít sẵn lòng; ngăn cản | 3 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/discourage) |
| `decline` | n/v | giảm; suy giảm; từ chối; sự suy giảm | 3 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/decline) |

## Coverage after the patch

- Related-term glossary: **383 entries**, up from 373.
- Canonical synonym/antonym data references: **804 distinct terms** across **1,037 occurrences**.
- Exact case-insensitive term join: **372/804** distinct terms now have a glossary entry; **432** distinct terms remain without one.
- At occurrence level: **477/1,037** synonym/antonym links still reference a term without a gloss.
- The ten additions account for 33 previously unglossed link occurrences.

The validator's informational text `syn/ant chưa có nghĩa=323/804` is produced by a different legacy counting rule. It is recorded as-is and is not treated as interchangeable with the exact-term join above.

## Editorial status

**Provisional — independent lexical review pending.** Cambridge pages were used as source references for short English definitions and Vietnamese paraphrases. Because these words can have multiple senses and domain-specific uses, a reviewer should confirm the precise sense used by each linked TOEIC headword before the entries are considered approved.

## Integrity boundary

No headword, stable ID, topic, synonym, antonym, word-family relationship, question, answer key or learner record was modified. The source ledger is `data/vocabulary/batch-021.json`; the safe patch is `patches-related-terms/v2.95.14/related-terms-001.json`.
