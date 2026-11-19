# Manual Acceptance Checklist — TOEIC Dictionary v2.95.11

**Purpose:** checklist for the project owner to execute on GitHub and real browsers/devices. This document is a blank record; it does not assert that any remote or device-level check has passed.

**Rule:** every result starts as `Chưa kiểm`. Fill in the result, date and device only after performing that exact check. Do not clear IndexedDB or learner localStorage to make a test easier; use a separate browser profile for clean-install scenarios.

| # | Hạng mục | Cách làm | Kết quả mong đợi | Đạt / Không đạt / Chưa kiểm | Ngày | Thiết bị |
|---:|---|---|---|---|---|---|
| 1 | GitHub Actions | Mở repository `vuphuc1996/Toeic` → Actions → chạy workflow kiểm tra source hiện tại; mở từng job nếu workflow đỏ. | Toàn bộ jobs kết thúc xanh; không có `continue-on-error`; có bước `Audit CSS design-token ratchet` chạy test và `tools/audit-design-tokens.py`. | **Chưa kiểm** | Chưa ghi | Chưa ghi |
| 2 | GitHub Pages deploy | Sau khi Actions xanh, mở Pages URL của repository và xác nhận phiên bản ở title/sidebar/footer. | Trang tải thành công; hiển thị v2.95.11; không có lỗi 404 asset hoặc lệch manifest/version. | **Chưa kiểm** | Chưa ghi | Chưa ghi |
| 3 | Đường dẫn con `/Toeic/` | Mở trực tiếp URL có path `/Toeic/`, refresh; mở thêm một route/hash nội bộ và quay lại trang chủ. | CSS/JS/data/image nạp đúng dưới `/Toeic/`; không bị điều hướng nhầm về domain root; refresh không thành 404. | **Chưa kiểm** | Chưa ghi | Chưa ghi |
| 4 | Cài PWA | Truy cập website bằng HTTPS trên trình duyệt hỗ trợ; dùng lệnh cài ứng dụng của trình duyệt/OS. Mở ứng dụng đã cài. | PWA được cài; icon, tên và app shell đúng; không mất đường dẫn con hoặc tài nguyên cục bộ. | **Chưa kiểm** | Chưa ghi | Chưa ghi |
| 5 | Offline ở lần mở đầu chưa có cache | Dùng một browser profile thử nghiệm mới, tắt mạng trước lần truy cập đầu tiên; không xóa dữ liệu profile đang học. | Trường hợp chưa từng tải cache phải báo trạng thái không có mạng một cách rõ ràng; không treo hoặc hiển thị trang trắng khó hiểu. Không kỳ vọng tải nội dung chưa cache khi offline. | **Chưa kiểm** | Chưa ghi | Chưa ghi |
| 6 | Offline sau khi đã online | Bật mạng, mở và tải hoàn chỉnh ứng dụng ít nhất một lần; sau khi trang hoạt động ổn định thì tắt mạng và reload. Mở các module cốt lõi đã precache. | App shell và tài nguyên đã cache mở được; chức năng dùng dữ liệu cục bộ hoạt động; phần phụ thuộc mạng báo giới hạn rõ ràng. | **Chưa kiểm** | Chưa ghi | Chưa ghi |
| 7 | Cập nhật từ bản cũ lên mới | Mở ứng dụng từ cache phiên bản cũ, để tab hoạt động; deploy phiên bản mới; chờ banner xuất hiện. Chụp/ghi version trước khi bấm. | Banner “Có bản mới – Tải lại” xuất hiện; app không tự đổi phiên bản trước khi người dùng chấp thuận; tab hiện tại tiếp tục dùng được cho tới khi chọn tải lại. | **Chưa kiểm** | Chưa ghi | Chưa ghi |
| 8 | Xác nhận cache mới trước khi xóa cache cũ | Trong DevTools → Application → Cache Storage, theo dõi cache cũ/mới trong lúc cập nhật; bấm “Tải lại” sau khi cache mới đã cài hoàn chỉnh. | Cache cũ chỉ bị dọn sau khi cache mới cài thành công và activation diễn ra; lỗi cài đặt bắt buộc giữ lại cache cũ. | **Chưa kiểm** | Chưa ghi | Chưa ghi |
| 9 | Hai tab đang mở khi cập nhật | Mở hai tab cùng origin/PWA ở bản cũ; deploy bản mới; quan sát cả hai tab; chỉ bấm cập nhật ở một tab. | Có thông báo cập nhật phù hợp; thao tác chấp thuận không làm tab còn lại rơi vào trạng thái trắng/hỏng; tab cũ có thể reload an toàn để nhận bản mới. Ghi nhận nếu cần reload tab thứ hai thủ công. | **Chưa kiểm** | Chưa ghi | Chưa ghi |
| 10 | TTS — iPhone Safari | Trên iPhone thật, mở Safari; nghe tối thiểu một Listening Part 1 và một bài có nhiều người nói/đáp án A–D; thử giọng nam và nữ nếu thiết bị có. | Phát âm không bị cắt; khoảng nghỉ và thứ tự nội dung hợp lý; giọng có thể khác theo iOS nhưng không rè/ồn bất thường hoặc tự dừng. Ghi lại tên voice và iOS version nếu biết. | **Chưa kiểm** | Chưa ghi | Chưa ghi |
| 11 | TTS — Android Chrome | Trên Android thật, mở Chrome; chạy cùng kịch bản Listening như iPhone; thử thay voice và tốc độ đọc. | Âm thanh phát hết; khoảng nghỉ giữa speaker/option hợp lý; giao diện điều khiển không che câu hỏi. Ghi mẫu máy, Android và voice engine nếu biết. | **Chưa kiểm** | Chưa ghi | Chưa ghi |
| 12 | Flashcard 10 từ — gồm hồ sơ cũ từng chọn 5 | Dùng một hồ sơ thử nghiệm còn giữ cấu hình cũ từng chọn 5 (nếu có); không xóa IndexedDB/localStorage. Mở Học tổng hợp, một chủ đề, Học tiếp và Ôn từ sai. | Không còn lựa chọn 5; mỗi lượt có tối đa 10 thẻ, hoặc ít hơn nếu thiếu từ hợp lệ; không lỗi runtime khi gặp key cũ; dữ liệu và lịch sử học được giữ nguyên. | **Chưa kiểm** | Chưa ghi | Chưa ghi |
| 13 | Part 1 photo 4:3 và crop photocopier | Kiểm tra ảnh Part 1 trong Learning và Mock ở desktop/mobile; kiểm kích thước khung 4:3 và điểm lấy nét của ảnh photocopier. So với source/crop chuẩn; nếu cần `object-position`, điểm dọc mục tiêu là `50% 66%` (không dùng vị trí cũ `50% 42%`). | Ảnh không méo, không cắt mất chủ thể; khung 4:3 thống nhất ở Learning/Mock; photocopier lấy nét đúng phần máy/người thao tác. | **Chưa kiểm** | Chưa ghi | Chưa ghi |
| 14 | Giữ dữ liệu người học khi nâng cấp | Trước và sau cập nhật, kiểm tra một hồ sơ học thử có lịch sử, từ đã lưu và thiết lập; không dùng lệnh clear site data. | Tiến độ, từ cá nhân và cấu hình người học vẫn còn; không có thông báo yêu cầu reset storage hoặc nâng IndexedDB ngoài kế hoạch. | **Chưa kiểm** | Chưa ghi | Chưa ghi |

## Kết luận nghiệm thu

- Tổng số hạng mục: **14**.
- Đạt: Chưa ghi.
- Không đạt: Chưa ghi.
- Chưa kiểm: **14/14**.
- Người thực hiện: Chưa ghi.
- Ngày nghiệm thu: Chưa ghi.

Chỉ thay đổi trạng thái của một hàng sau khi kiểm đúng hướng dẫn, ghi ngày và thiết bị tương ứng. Kết quả của GitHub Actions không thay thế kiểm thử trình duyệt/thiết bị thật; kiểm tra mô phỏng cục bộ cũng không được ghi nhận như kết quả QA thực tế.
