# Related-term Glossary Expansion — v2.95.21 (Batch 027)

## Purpose and selection

Continue the existing glossary work rather than replacing it with a new workstream. Batch 027 prioritizes the 23 source-verified highest-frequency terms that were still missing from the case-insensitive lookup join and each appeared exactly twice in the canonical synonym/antonym graph. Terms without a confirmed Cambridge lookup page were deliberately deferred.

| Term | POS | Vietnamese lookup gloss | References | Cambridge source |
|---|---|---|---:|---|
| `activity` | n | hoạt động; hoạt động kinh doanh | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/activity) |
| `answer` | n/v | câu trả lời; lời giải; trả lời hoặc phản hồi | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/answer) |
| `carry out` | v | thực hiện; tiến hành; hoàn thành nhiệm vụ | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/carry-out) |
| `combination` | n | sự kết hợp; sự kết hợp của nhiều yếu tố | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/combination) |
| `common` | adj | phổ biến; thường gặp | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/common) |
| `continue` | v | tiếp tục; duy trì; tiếp diễn | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/continue) |
| `decrease` | n/v | giảm; sự giảm; làm giảm | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/decrease) |
| `employee` | n | nhân viên; người được thuê và trả lương | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/employee) |
| `funding` | n | nguồn tài trợ; khoản kinh phí được cấp | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/funding) |
| `goal` | n | mục tiêu; điều muốn đạt được | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/goal) |
| `inaction` | n | sự không hành động; việc không làm gì để giải quyết vấn đề | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/inaction) |
| `make` | v | làm ra; tạo ra; sản xuất; kiếm được | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/make) |
| `minor` | adj | nhỏ; không đáng kể; ít quan trọng | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/minor) |
| `objective` | n | mục tiêu; điều dự định đạt được | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/objective) |
| `oppose` | v | phản đối; chống lại | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/oppose) |
| `send` | v | gửi; chuyển đi; phái hoặc sai đi | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/send) |
| `study` | n/v | học; nghiên cứu; khảo sát hoặc xem xét kỹ | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/study) |
| `support` | n/v | hỗ trợ; ủng hộ; sự hỗ trợ hoặc ủng hộ | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/support) |
| `work` | n/v | công việc; lao động; làm việc; hoạt động có hiệu quả | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/work) |
| `maximum` | adj | mức tối đa; lớn nhất được phép hoặc có thể | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/maximum) |
| `different` | adj | khác; không giống; có sự khác biệt | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/different) |
| `determine` | v | xác định; tìm ra; quyết định | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/determine) |
| `approach` | n/v | cách tiếp cận; phương pháp; tiếp cận hoặc xử lý một vấn đề | 2 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/approach) |

## Measured coverage after patch

- Related-term glossary: **423 entries** (400 → 423).
- Canonical vocabulary: **1,141 headwords**; stable ID set unchanged.
- Exact case-insensitive join: **412/804** distinct referenced terms (**51.2%**); **392** distinct referenced terms remain unglossed.
- Occurrence-level join: **644/1,037** referenced synonym/antonym occurrences (**62.1%**); **393** occurrences remain unglossed.
- Batch 027 covers 23 distinct terms and 46 previously unglossed relation occurrences. `disorganize` is the sole remaining two-reference gap; it was deferred because the source lookup exposed pronunciation/thesaurus evidence but no direct Cambridge Dictionary definition page accepted by the patch source policy.

These are dictionary lookup-coverage measurements only. They do not measure editorial correctness, vocabulary mastery or learning outcomes. New entries are provisional paraphrases of the linked Cambridge pages and remain pending independent lexical review.

## Integrity boundary

The patch adds only absent related-term lookup records and is tied to the exact pre-patch SHA-256 of `data/related-terms.json`. No canonical headword, stable ID, topic, synonym/antonym relation, word-family relation, question, answer key, learner record, storage key or runtime behavior was changed. Patch provenance: `patches-related-terms/v2.95.21/related-terms-027.json`; full record ledger: `patches-related-terms/v2.95.21/batch-027-glossary-ledger.json`.
