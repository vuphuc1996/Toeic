# Vocabulary Batch 011 — editorial record (v2.70.0)

## Scope and status

- Added: **37 canonical headwords**; total vocabulary 1,063 → **1,100**.
- Topic focus: Customer Service and Travel operations, including reservations, airports, transport, customer support, complaint handling and issue resolution.
- Status: original project-authored draft; structural validation passed; independent lexical and CEFR-by-sense review remains pending.
- All 37 records have bilingual example sentences, at least three collocations, and source-linked candidate US IPA from exact single-pronunciation CMUdict matches.
- No speculative synonym or antonym entries were added.

## Headword inventory

| Headword | ID | POS | Vietnamese gloss | CEFR estimate |
|---|---|---|---|---|
| airfare | `airfare-n` | n | giá vé máy bay | B1 |
| overbooking | `overbooking-n` | n | tình trạng đặt chỗ vượt quá số chỗ có sẵn | C1 |
| voucher | `voucher-n` | n | phiếu mua hàng; phiếu dịch vụ; phiếu thanh toán | B1 |
| excursion | `excursion-n` | n | chuyến tham quan ngắn; chuyến đi trong ngày | B2 |
| arrival | `arrival-n` | n | sự đến nơi; thời điểm đến | A2 |
| passport | `passport-n` | n | hộ chiếu | A2 |
| immigration | `immigration-n` | n | quầy hoặc thủ tục xuất nhập cảnh; sự nhập cư | B2 |
| shuttle | `shuttle-n` | n | xe trung chuyển; dịch vụ đưa đón theo tuyến | B1 |
| charter | `charter-n` | n | chuyến thuê riêng; hợp đồng thuê phương tiện | C1 |
| disembark | `disembark-v` | v | rời tàu hoặc máy bay; xuống phương tiện | C1 |
| cruise | `cruise-n` | n | chuyến du lịch bằng tàu biển | B1 |
| ferry | `ferry-n` | n | phà; tàu chở khách và phương tiện qua sông hoặc biển | B1 |
| porter | `porter-n` | n | nhân viên khuân vác hành lý | B1 |
| steward | `steward-n` | n | tiếp viên; nhân viên phục vụ trên phương tiện hoặc tại sự kiện | B2 |
| rebook | `rebook-v` | v | đặt lại vé hoặc chỗ sau khi thay đổi kế hoạch | B2 |
| ticketing | `ticketing-n` | n | việc bán, phát hành và quản lý vé | B2 |
| visa | `visa-n` | n | thị thực; giấy phép nhập cảnh | A2 |
| transportation | `transportation-n` | n | sự vận chuyển; phương tiện giao thông | B1 |
| escalation | `escalation-n` | n | việc chuyển vấn đề lên cấp xử lý cao hơn; sự leo thang | C1 |
| responsiveness | `responsiveness-n` | n | khả năng phản hồi nhanh và phù hợp | C1 |
| dissatisfied | `dissatisfied-adj` | adj | không hài lòng; không thỏa mãn | B2 |
| loyalty | `loyalty-n` | n | lòng trung thành; sự gắn bó của khách hàng | B1 |
| courteous | `courteous-adj` | adj | lịch sự; nhã nhặn | B2 |
| cancellation | `cancellation-n` | n | việc hủy bỏ; sự hủy đặt chỗ | B1 |
| agent | `agent-n` | n | nhân viên đại diện; đại lý | A2 |
| resolution | `resolution-n` | n | cách giải quyết; sự giải quyết vấn đề | B2 |
| resolve | `resolve-v` | v | giải quyết; xử lý dứt điểm | B1 |
| troubleshoot | `troubleshoot-v` | v | xác định và khắc phục sự cố | C1 |
| troubleshooting | `troubleshooting-n` | n | quá trình xác định và khắc phục sự cố | C1 |
| hotline | `hotline-n` | n | đường dây nóng; số điện thoại hỗ trợ chuyên biệt | B1 |
| consumer | `consumer-n` | n | người tiêu dùng | B1 |
| apology | `apology-n` | n | lời xin lỗi | A2 |
| faulty | `faulty-adj` | adj | bị lỗi; không hoạt động đúng | B2 |
| complain | `complain-v` | v | phàn nàn; khiếu nại | B1 |
| responsive | `responsive-adj` | adj | phản hồi nhanh; sẵn sàng đáp ứng | B2 |
| punctuality | `punctuality-n` | n | tính đúng giờ; sự đúng giờ | B2 |
| inconvenience | `inconvenience-n` | n | sự bất tiện; điều gây phiền hà | B2 |

## Field coverage

- US IPA: **37/37** populated by exact CMUdict single-pronunciation entries; IPA was generated from ARPABET using the project broad-GA converter.
- Bilingual examples: 37 original, sense-linked sentences.
- Collocations: 111 entries (three per headword).
- Word-family links: four reciprocal pairs (eight directed links): cancel/cancellation, resolve/resolution, responsive/responsiveness, troubleshoot/troubleshooting.
- Synonyms/antonyms: no entries added without a sense-specific basis.

## Source and limitation notes

- CMUdict source data: https://github.com/cmusphinx/cmudict — pronunciation candidates only; source ARPABET, raw tokens, and converted IPA are preserved in `docs/reports/CMUDICT_IPA_BACKFILL_v2.70.0.json`.
- Cambridge Dictionary: https://dictionary.cambridge.org/ — recommended independent cross-check source for subsequent human lexical and pronunciation review; this batch is not represented as independently approved.
- CMUdict supplies ARPABET, not IPA. Project IPA is a documented broad-GA conversion and is not an independent pronunciation certification.
- CEFR levels are editorial estimates by sense and not official CEFR alignment.
- These are original project practice items, not official ETS questions or materials.

## Acceptance constraints

- Stable IDs are immutable after release; every batch entry must match its canonical A–Z record.
- Every example must point to a valid sense and include a natural Vietnamese translation.
- All IPA must be source-linked; no ambiguous or guessed pronunciations are allowed.
- Existing learner progress, question IDs, answer keys and IndexedDB schema remain unchanged.
- Independent lexical review is a separate acceptance gate from automated structural validation.
