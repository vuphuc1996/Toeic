# v2.81.0 — A2 Writing Portfolio Review

## Mục tiêu

Bổ sung phần tổng hợp nhật ký viết A2 vào dashboard Foundation sau khi hoàn tất Guided Writing Revision ở v2.79.0. Báo cáo chỉ đọc tiến độ đã lưu, không tạo một hệ thống lưu trữ hoặc đánh giá song song.

## Phạm vi triển khai

- `summarizeFoundationProductionPortfolio()` trong `assets/js/foundation-evidence.js` tổng hợp bằng chứng theo từng bài A2 từ `productionEvidence` hiện có.
- Dữ liệu đầu ra gồm tổng bài có nhiệm vụ viết, bài đã bắt đầu, bài đã viết lại, số lượt tự đánh giá và xu hướng tự đánh giá từ bản đầu đến bản mới nhất.
- Chi tiết từng bài hiển thị đúng ba rubric riêng của bài đó và trạng thái tự đánh giá mới nhất.
- Bảng tổng hợp được đặt trong dashboard Foundation hiện có, mặc định thu gọn; không tạo trang, database, API hoặc kho tiến độ mới.
- Danh sách không hiển thị lại nội dung bài viết. Người học có thể mở bài gốc từ từng dòng để tiếp tục.

## Quy tắc diễn giải

- Chỉ đối chiếu bản đầu và bản mới nhất **trong cùng một bài**. Không cộng/so sánh tiêu chí số 1 của các bài khác nhau vì rubric được cá nhân hóa theo từng chủ điểm.
- `Tự đánh giá tăng/không đổi/giảm` là thay đổi do người học tự khai báo trên thang 0–3, không phải điểm chấm ngữ pháp, độ tự nhiên hay chất lượng viết khách quan.
- Không suy diễn CEFR, TOEIC score hoặc mastery.
- Chỉ đọc `::produce1` theo `productionTask` hiện tại; dữ liệu ứng dụng cũ `::apply1` được giữ nguyên và không trộn vào portfolio viết A2.

## Lưu trữ và tương thích

- Nguồn dữ liệu: localStorage key `toeic:foundation-progress:v1`, map `productionEvidence` đã được sử dụng từ các phiên bản trước.
- Không thêm key localStorage, IndexedDB store/version, backend hoặc migration.
- Không sửa câu trả lời, lịch sử attempt, ID bài học hay rubric đã lưu.
- Không gửi nội dung viết ra khỏi thiết bị.

## Kiểm thử chuyên biệt

`tools/tests/foundation-production-revision.mjs` bổ sung fixture cho ba trường hợp: một bài có xu hướng tự đánh giá tăng, một bài giảm và một bài chưa viết lại. Test kiểm tra số bài bắt đầu/viết lại, số attempt, rubric từng bài, ratings mới nhất, và bảo đảm legacy `::apply1` bị loại khỏi A2 portfolio.

Kết quả: **PASS** trong 25/25 JavaScript regression suites và 151/151 Python tests được chọn ở v2.81.0.
