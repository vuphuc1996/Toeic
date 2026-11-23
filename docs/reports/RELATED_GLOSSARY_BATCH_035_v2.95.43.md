# Related Glossary Batch 035 — v2.95.43

## Scope

Added 26 source-backed lookup entries to `data/related-terms.json` for terms that already appeared in canonical TOEIC vocabulary synonym arrays but had no Related Glossary row.

Each addition contains:
- English term identity preserved from the canonical relationship list.
- Vietnamese lookup meaning.
- Part of speech.
- Concise paraphrased English definition.
- Direct Cambridge Dictionary entry URL.

## Added terms

| Term | POS | Vietnamese lookup | Source headword |
|---|---|---|---|
| administer | v | quản lý; điều hành; quản trị | manage |
| alike | adj | giống nhau; tương tự nhau | similar |
| appeal | n | lời kêu gọi; yêu cầu hỗ trợ chính thức | solicitation |
| article | n | món đồ; vật phẩm; mặt hàng | item |
| ask for | v phr | yêu cầu; đề nghị cung cấp | request |
| assist | v | hỗ trợ; giúp đỡ | support |
| assume | v | đảm nhận; nhận trách nhiệm | undertake |
| backer | n | người hậu thuẫn; nhà tài trợ | sponsor |
| bargaining | n | sự thương lượng; đàm phán | negotiation |
| begin | v | bắt đầu; khởi đầu | embark |
| book | v | đặt trước; giữ chỗ | reserve |
| bring | v | mang đến; đưa đến | deliver |
| caller | n | người đến thăm; khách ghé thăm | visitor |
| capable | adj | có năng lực; có khả năng thực hiện hiệu quả | efficient |
| carry | v | mang; vận chuyển | transport |
| change | n | sự thay đổi; sự chuyển đổi | transition |
| characteristic | n | đặc điểm; đặc trưng | feature |
| choice | n | sự lựa chọn; khả năng lựa chọn | option |
| clothing | n | quần áo; trang phục | attire |
| comments | n pl | các nhận xét; ý kiến phản hồi | feedback |
| communicate with | v phr | liên lạc với; trao đổi thông tin với | contact |
| comparable | adj | có thể so sánh; tương đương | similar |
| compute | v | tính toán; tính ra | calculate |
| connection | n | mối liên hệ; sự kết nối | network |
| consequence | n | kết quả; hệ quả | outcome |
| consideration | n | sự cân nhắc; điều cần xem xét | consider |

## Measured impact

| Metric | Before Batch 035 | After Batch 035 |
|---|---:|---:|
| Raw glossary rows | 527 | 553 |
| Normalized unique rows | 527 | 553 |
| Duplicate normalized rows | 0 | 0 |
| Referenced unique relationship terms | 804 | 804 |
| Covered referenced terms | 516 | 542 |
| Coverage | 64.2% | 67.4% |
| Unglossed unique terms | 288 | 262 |
| Unglossed reference occurrences | 289 | 263 |

The 26 new terms correspond to 26 previously unglossed unique relationship terms. This raises exact relation lookup coverage by 3.2 percentage points. It does not change the source relationship arrays or prove that every synonym relationship is interchangeable in every context.

## Source and safety policy

- Each row points to its Cambridge Dictionary entry; the English definition is paraphrased rather than copied.
- The batch is applied with an absent-only guard and a SHA-256 precondition against the exact v2.95.42 `related-terms.json` baseline.
- The patch updater writes atomically and records the operation. The test reconstructs the exact pre-batch payload and checks its SHA-256.
- Regression verifies that each added term remains in its source headword's canonical synonym array.
- No canonical vocabulary headword, vocabulary ID, synonym/antonym array, question, answer key, choice ID, resource ID, learner record, IndexedDB schema, UI or Mock eligibility is modified.
- These are lookup glosses, not independent lexical/pedagogical approval. Human review remains pending.

## Remaining content debt

- 262 unique relationship terms / 263 occurrences remain unglossed.
- 150 glossary rows still have no English definition.
- 73 glossary rows remain placeholder definitions.
- The current audit still reports no exact canonical headword candidates suitable for automatic definition backfill. These are retained for sourced editorial work; no definitions were inferred from unrelated canonical headwords.
