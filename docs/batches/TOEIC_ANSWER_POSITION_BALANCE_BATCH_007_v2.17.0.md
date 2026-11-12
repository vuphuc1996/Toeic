# TOEIC Answer Position Balance — Batch 007 / v2.17.0

Ngày: 11/11/2026

## Mục tiêu
Giảm độ lệch vị trí đáp án đúng ở Listening Part 3, Listening Part 4 và Reading Part 7 mà không thay câu hỏi, passage/transcript, đáp án đúng về mặt nội dung hay giải thích. Không dùng random shuffle.

## Kết quả phân bố
| Part | Trước v2.17.0 (A/B/C/D) | Sau v2.17.0 (A/B/C/D) | Số câu |
|---|---|---|---:|
| Listening Part 3 | 10 / 18 / 10 / 1 | 10 / 10 / 10 / 9 | 39 |
| Listening Part 4 | 9 / 12 / 7 / 2 | 8 / 8 / 7 / 7 | 30 |
| Reading Part 7 | 13 / 27 / 19 / 4 | 16 / 16 / 16 / 15 | 63 |

Phân bố được làm gần đều nhất có thể theo tổng số câu của từng Part; số lượng từng Part không thay đổi.

## Quy tắc thay đổi và bảo toàn dữ liệu
- Đúng 27 câu được điều chỉnh: Part 3 có 8, Part 4 có 5, Part 7 có 14 câu.
- Mỗi câu chỉ hoán đổi vị trí của phương án đúng với một distractor để đưa đáp án đúng về vị trí mục tiêu. Tất cả phương án và stable `choiceIds` di chuyển cùng nhau.
- Trước khi đổi, mỗi câu lưu `previousChoices`, `previousChoiceIds`, `previousAnswerIndex`, cùng `choiceOrderRevision: "2.17.0"`.
- Mapping chi tiết được lưu tại `tools/answer-position-balance-v2.17.0.json` và được kiểm thử tự động.
- Progress đã có `choiceId` được tìm lại vị trí hiện tại; progress cũ không có ID được ánh xạ từ snapshot v2.16. Chỉ số cũ được lưu thêm ở `previousChoiceIndex`.
- 12 nhóm distractor có `legacyChoices`/`legacyChoiceIds` từ v2.15 được giữ nguyên. ID lịch sử không được nhầm với ID phương án hiện tại.
- Dữ liệu có text không khớp hoặc index không hợp lệ được giữ nguyên, không tự suy đoán ID. Migration có tính idempotent.
- Không nâng IndexedDB version (vẫn DB `toeic-vocabulary-phase1`, version 1, store `workspace`), không reset tiến độ, không thay đổi 928 từ vựng, question ID hoặc thứ tự câu hỏi.

## Mapping đầy đủ 27 câu đã đổi
| Part | Bộ câu hỏi | Câu | Vị trí cũ → mới | Đáp án đúng (text giữ nguyên) |
|---|---|---:|---|---|
| Part 3 | `part3-budget-review` | 1 | B → D | Flights were booked at short notice |
| Part 3 | `part3-business-trip` | 2 | B → D | The first hotel is fully booked. |
| Part 3 | `part3-facility-repair` | 1 | B → D | A noisy air conditioner |
| Part 3 | `part3-interview-schedule` | 1 | B → D | An HR employee |
| Part 3 | `part3-invoice-error` | 1 | B → D | The delivery fee was added twice. |
| Part 3 | `part3-procurement-quotation` | 1 | B → D | Replacement monitors |
| Part 3 | `part3-shipping-delay` | 2 | B → D | There was road construction. |
| Part 3 | `part3-software-upgrade` | 1 | B → D | Submit stock requests through the portal |
| Part 4 | `part4-conference-update` | 3 | B → D | At the information desk |
| Part 4 | `part4-office-announcement` | 1 | B → D | Customer service |
| Part 4 | `part4-product-launch` | 1 | B → D | A department readiness checklist |
| Part 4 | `part4-quarterly-town-hall` | 3 | A → D | By using an online form |
| Part 4 | `part4-safety-announcement` | 1 | B → D | Use the marked pedestrian walkway |
| Part 7 | `business-travel` | 1 | C → A | Three nights |
| Part 7 | `customer-service` | 1 | B → D | The address was incomplete |
| Part 7 | `facility-maintenance` | 1 | B → D | Saturday morning |
| Part 7 | `facility-maintenance-notice` | 1 | B → D | Saturday morning |
| Part 7 | `invoice-payment` | 2 | B → D | The transaction reference |
| Part 7 | `invoice-payment` | 3 | C → A | Maintenance services |
| Part 7 | `job-opening` | 1 | B → D | Operations Coordinator |
| Part 7 | `job-opening` | 3 | C → A | July 1 |
| Part 7 | `job-posting-analyst` | 1 | B → D | A résumé and cover letter |
| Part 7 | `meeting-notice` | 1 | B → D | Thursday, April 18 |
| Part 7 | `office-schedule` | 2 | B → D | Meeting Room B |
| Part 7 | `part7-single-equipment-memo` | 2 | B → D | Before October 11 |
| Part 7 | `part7-single-training-email` | 2 | B → D | Conference Room 3 |
| Part 7 | `shipping-update` | 1 | B → D | Severe weather |

## Kiểm thử bắt buộc
- Kiểm tra phân bố A/B/C/D đúng mục tiêu và tổng Part không đổi.
- Kiểm tra 27 mapping có đủ snapshot v2.16, stable ID đi cùng option, `answerIndex` mới trỏ đúng text đáp án cũ.
- Mô phỏng profile v2.15.1 không có `choiceId`, profile v2.16 đã có `choiceId`, progress của Reading/Listening/Grammar, và 12 lựa chọn lịch sử đã archive.
- Kiểm tra mapping vị trí cũ sang mới, `correct`, `answeredAt`, `choiceText` được giữ, unknown text / invalid index không bị đoán, migration chạy lần hai không ghi lại.
- Remote GitHub Actions, website live và IndexedDB thực tế trên thiết bị người dùng vẫn cần kiểm thử sau khi push/deploy; smoke test trong sandbox không thay thế kiểm thử profile thật.
