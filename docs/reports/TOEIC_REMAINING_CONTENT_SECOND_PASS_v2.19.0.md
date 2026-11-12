# TOEIC Listening & Reading — Remaining Content Second-pass Review v2.19.0

Ngày: 11/11/2026  
Trạng thái: hoàn tất vòng tự rà soát nội bộ; không thay đổi nội dung câu hỏi.

## Phạm vi

Rà soát toàn bộ **148 câu không thuộc Part 7**: Listening 102 câu (P1=8, P2=25, P3=39, P4=30) và Reading 46 câu (P5=30, P6=16). Part 7 gồm 63 câu đã có báo cáo second-pass riêng trong v2.18.0. Tổng ngân hàng Listening/Reading vẫn là 211 câu.

## Tiêu chí rà soát

- **Part 1:** đối chiếu chi tiết trong hình minh họa SVG với câu mô tả và phương án; giữ nhãn illustration, không mô tả đây là ảnh chụp.
- **Part 2:** xác định loại câu hỏi/hành động lời nói (WH-, yes/no, lựa chọn, đề nghị, xác nhận, phản hồi gián tiếp) và độ tự nhiên/liên quan của câu trả lời; distractor phải không trả lời đúng ý định giao tiếp.
- **Part 3–4:** đối chiếu từng key với transcript, người nói, thời gian, địa điểm, mục đích và bước tiếp theo; kiểm tra các phương án nhiễu không tạo ra key thứ hai hoặc mâu thuẫn transcript.
- **Part 5:** kiểm tra cấu trúc câu, từ loại, hòa hợp chủ-vị, thì, bị động, so sánh, liên từ/giới từ; chỉ giữ key khi có một lựa chọn tốt nhất theo ngữ cảnh.
- **Part 6:** kiểm tra ngữ pháp ở vị trí trống, liên kết câu/đoạn, trình tự logic và tính phù hợp của câu chèn; giải thích phải nêu được mối liên hệ.
- Đối chiếu lại lựa chọn đúng và giải thích tiếng Việt; giữ nguyên định danh lựa chọn (`choiceIds`).

## Kết quả

Không phát hiện lỗi nội dung đủ căn cứ để sửa mà không có nguy cơ làm giảm độ chính xác. Vì vậy batch này **giữ nguyên key và nội dung**, không sửa chỉ để tạo khác biệt phiên bản. Không thay đổi `answerIndex`, text phương án, `choiceIds`, thứ tự câu hỏi hoặc số lượng câu. Kết quả bảo thủ này không có nghĩa là nội dung đã được chuyên gia độc lập hoặc ETS chứng nhận.

| Part | Số câu | Kết quả |
|---|---:|---|
| Listening P1 | 8 | Rà hình minh họa / mô tả / key; giữ nguyên |
| Listening P2 | 25 | Rà speech-act / response fit / distractor; giữ nguyên |
| Listening P3 | 39 | Rà transcript / speaker / timeline / distractor; giữ nguyên |
| Listening P4 | 30 | Rà transcript / detail / inference / distractor; giữ nguyên |
| Reading P5 | 30 | Rà cấu trúc ngữ pháp / single-best-answer; giữ nguyên |
| Reading P6 | 16 | Rà cohesion / insertion / syntax / context fit; giữ nguyên |
| **Tổng** | **148** | **Không có hiệu chỉnh nội dung** |

## Danh mục câu đã rà

Các mã dưới đây dùng định danh ổn định dạng `unitId#Qn` vì dữ liệu hiện tại chưa gán question ID độc lập cho từng câu. File máy đọc `tools/remaining-content-review-v2.19.0.json` lưu đủ 148 mã, vị trí đáp án hiện tại, tiêu chí rà và SHA-256 của hai file nguồn để buộc rà soát lại khi dữ liệu thay đổi.

### Part 1 (8 câu)

`part1-meeting-documents#Q1`, `part1-warehouse-box#Q1`, `part1-technician-inspection#Q1`, `part1-airport-suitcase#Q1`, `part1-presentation-room#Q1`, `part1-reception-plant#Q1`, `part1-restaurant-setting#Q1`, `part1-photocopier#Q1`

### Part 2 (25 câu)

`part2-report-deadline#Q1`, `part2-meeting-room#Q1`, `part2-visitor-badge#Q1`, `part2-invoice-approval#Q1`, `part2-training-date#Q1`, `part2-database-owner#Q1`, `part2-printer-arrival#Q1`, `part2-seat-preference#Q1`, `part2-room-unavailable#Q1`, `part2-workshop-copies#Q1`, `part2-sales-figures#Q1`, `part2-wrong-branch#Q1`, `part2-business-trip#Q1`, `part2-proposal-selection#Q1`, `part2-airport-taxi#Q1`, `part2-product-demo#Q1`, `part2-access-code#Q1`, `part2-inspection-duration#Q1`, `part2-missing-payment#Q1`, `part2-cafeteria-notice#Q1`, `part2-contract-review#Q1`, `part2-registration-extension#Q1`, `part2-first-shuttle#Q1`, `part2-website-update#Q1`, `part2-supplier-samples#Q1`

### Part 3 (39 câu)

`part3-shipping-delay#Q1`, `part3-shipping-delay#Q2`, `part3-shipping-delay#Q3`, `part3-business-trip#Q1`, `part3-business-trip#Q2`, `part3-business-trip#Q3`, `part3-interview-schedule#Q1`, `part3-interview-schedule#Q2`, `part3-interview-schedule#Q3`, `part3-invoice-error#Q1`, `part3-invoice-error#Q2`, `part3-invoice-error#Q3`, `part3-facility-repair#Q1`, `part3-facility-repair#Q2`, `part3-facility-repair#Q3`, `part3-budget-review#Q1`, `part3-budget-review#Q2`, `part3-budget-review#Q3`, `part3-interview-arrangement#Q1`, `part3-interview-arrangement#Q2`, `part3-interview-arrangement#Q3`, `part3-software-upgrade#Q1`, `part3-software-upgrade#Q2`, `part3-software-upgrade#Q3`, `part3-client-presentation#Q1`, `part3-client-presentation#Q2`, `part3-client-presentation#Q3`, `part3-procurement-quotation#Q1`, `part3-procurement-quotation#Q2`, `part3-procurement-quotation#Q3`, `part3-hotel-reservation#Q1`, `part3-hotel-reservation#Q2`, `part3-hotel-reservation#Q3`, `part3-marketing-campaign#Q1`, `part3-marketing-campaign#Q2`, `part3-marketing-campaign#Q3`, `part3-elevator-maintenance#Q1`, `part3-elevator-maintenance#Q2`, `part3-elevator-maintenance#Q3`

### Part 4 (30 câu)

`part4-office-announcement#Q1`, `part4-office-announcement#Q2`, `part4-office-announcement#Q3`, `part4-conference-update#Q1`, `part4-conference-update#Q2`, `part4-conference-update#Q3`, `part4-safety-announcement#Q1`, `part4-safety-announcement#Q2`, `part4-safety-announcement#Q3`, `part4-product-launch#Q1`, `part4-product-launch#Q2`, `part4-product-launch#Q3`, `part4-quarterly-town-hall#Q1`, `part4-quarterly-town-hall#Q2`, `part4-quarterly-town-hall#Q3`, `part4-customer-voicemail#Q1`, `part4-customer-voicemail#Q2`, `part4-customer-voicemail#Q3`, `part4-warehouse-safety-briefing#Q1`, `part4-warehouse-safety-briefing#Q2`, `part4-warehouse-safety-briefing#Q3`, `part4-training-registration#Q1`, `part4-training-registration#Q2`, `part4-training-registration#Q3`, `part4-travel-service-update#Q1`, `part4-travel-service-update#Q2`, `part4-travel-service-update#Q3`, `part4-quarterly-inventory-report#Q1`, `part4-quarterly-inventory-report#Q2`, `part4-quarterly-inventory-report#Q3`

### Part 5 (30 câu)

`part5-workplace-grammar-01#Q1`, `part5-workplace-grammar-01#Q2`, `part5-workplace-grammar-01#Q3`, `part5-workplace-grammar-01#Q4`, `part5-business-vocabulary-02#Q1`, `part5-business-vocabulary-02#Q2`, `part5-business-vocabulary-02#Q3`, `part5-business-vocabulary-02#Q4`, `part5-forms-and-agreement-03#Q1`, `part5-forms-and-agreement-03#Q2`, `part5-forms-and-agreement-03#Q3`, `part5-forms-and-agreement-03#Q4`, `part5-prepositions-and-connectors-04#Q1`, `part5-prepositions-and-connectors-04#Q2`, `part5-prepositions-and-connectors-04#Q3`, `part5-prepositions-and-connectors-04#Q4`, `part5-tense-voice-set-05#Q1`, `part5-tense-voice-set-05#Q2`, `part5-tense-voice-set-05#Q3`, `part5-tense-voice-set-05#Q4`, `part5-tense-voice-set-05#Q5`, `part5-adjectives-adverbs-set-06#Q1`, `part5-adjectives-adverbs-set-06#Q2`, `part5-adjectives-adverbs-set-06#Q3`, `part5-adjectives-adverbs-set-06#Q4`, `part5-adjectives-adverbs-set-06#Q5`, `part5-connectors-prepositions-set-07#Q1`, `part5-connectors-prepositions-set-07#Q2`, `part5-connectors-prepositions-set-07#Q3`, `part5-connectors-prepositions-set-07#Q4`

### Part 6 (16 câu)

`part6-training-center-newsletter#Q1`, `part6-training-center-newsletter#Q2`, `part6-training-center-newsletter#Q3`, `part6-training-center-newsletter#Q4`, `part6-customer-service-email#Q1`, `part6-customer-service-email#Q2`, `part6-customer-service-email#Q3`, `part6-customer-service-email#Q4`, `part6-job-posting#Q1`, `part6-job-posting#Q2`, `part6-job-posting#Q3`, `part6-job-posting#Q4`, `part6-product-workshop-registration#Q1`, `part6-product-workshop-registration#Q2`, `part6-product-workshop-registration#Q3`, `part6-product-workshop-registration#Q4`

## Kiểm thử và giới hạn

- Bộ kiểm thử bổ sung kiểm tra đủ 148/148 mã, phân bố đúng theo Part, tính toàn vẹn key/choice/choice ID/explanation, và fingerprint nguồn. Đây là kiểm tra phạm vi + cấu trúc; **không** tự động chứng minh ngữ nghĩa.
- Full validator và test suite được chạy lại ở mức local; kết quả chi tiết nằm trong `TEST_REPORT_TOEIC_Dictionary_v2.19.0.md`.
- Cần thêm người rà soát độc lập (giáo viên/người có chuyên môn TOEIC) trước khi dùng ngân hàng làm Full Mock tính điểm.
- Không kiểm thử import/export/migration với profile IndexedDB cá nhân. Dùng profile mặc định; không reset, không đọc/chỉnh sửa dữ liệu cá nhân.

## Kết luận

Đã hoàn thành second-pass nội bộ cho toàn bộ phần Listening và Reading ngoài Part 7. Không có thay đổi câu hỏi/đáp án nên lịch sử học tập và identity của lựa chọn không bị ảnh hưởng. Hạng mục kế tiếp theo Master là rà soát trực quan trình duyệt thật cho sidebar ở zoom 100% và QA responsive trên thiết bị; phần profile IndexedDB cá nhân vẫn để sau theo yêu cầu người dùng.
