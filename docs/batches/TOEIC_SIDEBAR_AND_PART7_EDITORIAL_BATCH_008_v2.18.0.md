# TOEIC Sidebar & Part 7 Editorial — Batch 008 / v2.18.0

Ngày: 11/11/2026

## Phạm vi

Batch này xử lý hai hạng mục: khả năng nhìn thấy footer sidebar trên laptop 15,6 inch ở zoom 100%, và vòng rà soát nội bộ lần hai cho Reading Part 7. Không thêm chức năng IELTS.

## A. Sidebar

- Desktop sidebar được giới hạn theo dynamic viewport height.
- Navigation list cuộn độc lập; phần trạng thái cục bộ và phiên bản ghim ở đáy và không bị ẩn.
- Giảm spacing cho viewport cao ≤820 CSS px; compact sâu hơn ở ≤680 CSS px.
- Thêm 2 regression tests cho footer và vùng cuộn.
- Chưa thực hiện visual QA thực tế tại laptop do trình duyệt đồ họa không khả dụng trong sandbox.

## B. Part 7 second pass

- Phạm vi 63 câu / 24 bộ Part 7.
- Chỉnh hai chi tiết nguồn: ngày đặt phòng hội nghị và ngày hoàn thành khóa học đối với chương trình hoàn phí.
- Đồng bộ passage, translation và rationale bị ảnh hưởng.
- Không đổi question ID, question order, choice text, choiceIds, `answerIndex`, đáp án đúng hoặc số câu.
- Hai bộ multi-document một câu được đánh dấu để bổ sung câu tích hợp tài liệu ở reserve-content batch.

## C. Bảo toàn dữ liệu

- 928 vocabulary IDs giữ nguyên; không thêm/xóa vocabulary.
- Listening 102; Reading 109; Grammar 25 lessons /54 exercises.
- Không đổi IndexedDB version/store/schema.
- Theo yêu cầu người dùng, chưa kiểm tra import/export hoặc migration trên profile IndexedDB cá nhân; chỉ sử dụng profile local mặc định.

## D. Tệp bàn giao

- `docs/reports/RESPONSIVE_SIDEBAR_FIX_v2.18.0.md`
- `docs/reports/TOEIC_PART7_SECOND_PASS_REVIEW_v2.18.0.md`
- `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.18.0.md`
- `docs/MASTER_STATUS.md` và `docs/CHANGELOG.md`
