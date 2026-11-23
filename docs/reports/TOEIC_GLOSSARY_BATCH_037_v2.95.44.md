# TOEIC Dictionary — Related Glossary Batch 037 (v2.95.44)

## Scope and baseline

- Base source: v2.95.43 Full Source, directly opened and CRC/SHA-256 verified before editing.
- Canonical A–Z vocabulary: 1,141 headwords.
- Previous Related Glossary: 546 unique rows, 535/804 relation targets covered; 269 unique terms / 270 occurrences remained uncovered.
- Selected scope: source-backed lookup glosses for existing relation targets. No new canonical headwords or relation links were created.

## Implemented data

Added 16 entries, each absent from the glossary before the patch and present as an existing canonical synonym/antonym relation target:

| Term | POS | Vietnamese lookup meaning | Relationship anchor | Cambridge source |
|---|---|---|---|---|
| begin | v | bắt đầu; khởi đầu | embark | https://dictionary.cambridge.org/dictionary/english/begin |
| book | v | đặt trước; đăng ký trước (chỗ, phòng, vé hoặc lịch hẹn) | reserve | https://dictionary.cambridge.org/dictionary/english/book |
| bring | v | mang; đem; đưa đến | deliver | https://dictionary.cambridge.org/dictionary/english/bring |
| characteristic | n | đặc điểm; đặc trưng; tính chất tiêu biểu | feature | https://dictionary.cambridge.org/dictionary/english/characteristic |
| clothing | n | quần áo; trang phục | attire | https://dictionary.cambridge.org/dictionary/english/clothing |
| comparable | adj | có thể so sánh; tương đương về quy mô, số lượng hoặc chất lượng | similar | https://dictionary.cambridge.org/dictionary/english/comparable |
| compute | v | tính toán; tính ra bằng phương pháp toán học hoặc máy tính | calculate | https://dictionary.cambridge.org/dictionary/english/compute |
| consequence | n | kết quả; hậu quả | outcome | https://dictionary.cambridge.org/dictionary/english/consequence |
| currency | n | tiền tệ; đơn vị tiền tệ được sử dụng tại một quốc gia | cash | https://dictionary.cambridge.org/dictionary/english/currency |
| down payment | n | khoản trả trước; tiền đặt cọc một phần giá mua | deposit | https://dictionary.cambridge.org/dictionary/english/down-payment |
| disturbance | n | sự gián đoạn; sự náo động; tình trạng gây rối | disruption | https://dictionary.cambridge.org/dictionary/english/disturbance |
| development | n | sự phát triển; quá trình tiến bộ hoặc tạo ra điều mới | progress | https://dictionary.cambridge.org/dictionary/english/development |
| declaration | n | bản tuyên bố; lời khai; sự công bố chính thức | statement | https://dictionary.cambridge.org/dictionary/english/declaration |
| eager | adj | háo hức; rất mong muốn làm hoặc có điều gì | willing | https://dictionary.cambridge.org/dictionary/english/eager |
| entire | adj | toàn bộ; trọn vẹn; đầy đủ | complete | https://dictionary.cambridge.org/dictionary/english/entire |
| eventuality | n | tình huống có thể xảy ra; khả năng bất ngờ cần dự liệu | contingency | https://dictionary.cambridge.org/dictionary/english/eventuality |

Definitions are concise paraphrases of Cambridge Dictionary entry content retrieved through Cambridge search results on 2026-11-23. Each record retains an exact Cambridge URL and provenance text. Some records draw on Business English or Academic Content Dictionary entries as identified in the ledger. Full-page independent editorial review remains pending; these entries must not be represented as independently approved. No example sentences, IPA or speculative pronunciations were added.

## Coverage impact

| Metric | v2.95.43 | v2.95.44 |
|---|---:|---:|
| Raw glossary rows | 546 | 562 |
| Unique normalized terms | 546 | 562 |
| Duplicate normalized terms | 0 | 0 |
| Covered unique relation targets | 535/804 | 551/804 |
| Coverage | 66.5% | 68.5% |
| Missing unique terms | 269 | 253 |
| Missing relation occurrences | 270 | 254 |
| Non-placeholder English definitions | 323 | 339 |
| Missing English definitions | 150 | 150 |
| Placeholder English definitions | 73 | 73 |

## Regression and preservation

- Added seven tests in `tools/tests/test_related_glossary_batch_037.py` for inventory/patch agreement, historical base reconstruction, exact ledger/data provenance, relation-target membership, POS/anchor preservation, canonical/learning-bank SHA-256 and normalized duplicates.
- Updated Batch 036 historical patch reconstruction so any later additive glossary batch is excluded dynamically when rebuilding its historical baseline.
- Updated Batch 027, candidate audit, major-release audit and project-progress tests to compare current generated metrics instead of obsolete 535/767 or pre-Batch-037 literals.
- Updated the historical vocabulary detail examples test to allow only known later provenance fields on the record while keeping original fields checked.
- CI Python compile and dedicated test commands now include Batch 037.
- Canonical A–Z headwords/IDs, synonym/antonym arrays, question/choice IDs, answer keys, learner IndexedDB records/schema and Mock eligibility are unchanged. Protected canonical and learning-bank fingerprints are recorded in the ledger.

## Backlog and unchanged status

- Current backlog: 253 unique terms / 254 relation occurrences.
- `disorganize` remains uncovered (two antonym references). It was deliberately not added in this batch because the candidate research available did not establish a direct, sufficiently verified exact dictionary entry for this lexical item. No-match/insufficient-source outcome: unchanged; keep pending rather than infer a meaning.
- No new headwords or relationship changes were made.
