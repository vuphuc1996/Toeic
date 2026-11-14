# TOEIC DICTIONARY — MASTER STATUS

> **Nguồn trạng thái và lộ trình duy nhất.** Mọi release cập nhật trực tiếp file này; không tạo Master/Roadmap riêng. Lịch sử chi tiết nằm trong `CHANGELOG.md`; mô tả tài liệu đã nghỉ hưu nằm trong `archive/PROJECT_HISTORY.md`; tương thích nằm trong `COMPATIBILITY.md`.

- **Ngày kiểm kê:** 2026-11-13.
- **Phiên bản mã nguồn đang kiểm kê:** v2.29.0 (Shared Learning Workspace, Flashcard single-scroll and documentation consolidation; local candidate).
- **Current candidate:** v2.29.0, phát triển từ v2.28.0.
- **Previous baseline:** v2.28.0.
- **Repository:** `vuphuc1996/Toeic`; app source nằm ở root repository.
- **Nền tảng:** GitHub Pages + PWA tĩnh; không backend/GAS/iframe/Cloudflare.
- **Trạng thái triển khai:** local candidate. Chưa xác nhận GitHub Actions, GitHub Pages hoặc QA thiết bị thật.

## 1. Tóm tắt thay đổi v2.29.0

### Giao diện / trải nghiệm học tập

1. Flashcard được đổi thành hai vùng xếp dọc: vùng trên giữ từ vựng/IPA/chủ đề; khi lật, vùng dưới mở phần nghĩa, định nghĩa, ví dụ, collocations, quan hệ từ và verb forms.
2. Chỉ `.learning-focus-content` sở hữu cuộn dọc. Khung từ, mặt sau Flashcard và vùng nội dung bài không tự tạo scrollbar dọc riêng. Nội dung ngắn không cần cuộn; nội dung dài dùng một scrollbar của workspace.
3. Flashcard, Vocabulary Review, Grammar, Reading và Listening detail dùng chung `#learningFocusBackdrop` / `#learningFocusDialog` với header, nút đóng và vùng nội dung đồng nhất. Grammar/Reading/Listening chuyển qua helper `openLearningDetail()`; không còn mở một detail-modal riêng cho từng module.
4. Responsive: desktop/tablet giữ bố cục tập trung; mobile xếp một cột, giữ safe-area và cuộn cùng một vùng. Không ép chiều cao cố định cho nội dung học.
5. Vocabulary editor/detail và popup giải thích đáp án Review vẫn là modal tiện ích riêng theo chức năng; chúng không tạo một kiểu workspace riêng cho các bài học.

### Quản lý tài liệu

- Giữ một Master, một Compatibility Register, một Design System, một Content Operations, một Changelog và một Project History tổng.
- Mỗi thời điểm chỉ giữ tài liệu release-specific của **previous + current** trong `docs/batches/`, `docs/reports/` và root `V*_UPDATE_NOTES.txt`.
- File release hiện tại giữ đầy đủ nội dung phát triển mới. Khi phát hành bản kế tiếp, file hiện tại trở thành file previous; file previous cũ được tóm tắt gọn vào `archive/PROJECT_HISTORY.md` rồi nghỉ hưu.
- Source/editorial links nằm trong batch file của release tương ứng; không tạo một file nguồn `.md` riêng cho từng batch.
- `CHANGELOG.md` giữ chronology; `PROJECT_HISTORY.md` là index lịch sử ngắn, không sao chép nguyên văn các báo cáo cũ.

## 2. Baseline dữ liệu và module

| Hạng mục | Trạng thái nền từ v2.28.0 |
|---|---:|
| Vocabulary canonical | **979 headwords** |
| US IPA | 631/979 |
| Word-family records | 131 |
| Verb-form records | 303 |
| Collocations | 809 |
| Listening | 63 units / 113 questions |
| Reading | 35 resources / 109 questions |
| Grammar | 25 lessons / 54 exercises |
| Mock practice | 15m/25Q · 60m/100Q · 120m/200Q |

v2.29.0 không bổ sung vocabulary hay thay đổi question pool. Các số liệu được giữ làm baseline, không phải xác nhận độc lập về chất lượng từ vựng/đề thi. CEFR vẫn là editorial estimate; mock scores là practice indicators, không phải điểm ETS quy đổi.

## 3. Ràng buộc kỹ thuật và dữ liệu

1. `data/vocabulary/A.json`–`Z.json` là runtime source duy nhất. `batch-*.json` chỉ là provenance biên tập. Không tạo nguồn runtime trùng.
2. Giữ stable vocabulary IDs và IDs câu hỏi/choice. Không đổi ID hay thứ tự câu hỏi có thể liên kết tiến độ học.
3. IndexedDB vẫn là `toeic-vocabulary-phase1`, version `1`, store `workspace`. Không import/export, inspect, reset hoặc migrate hồ sơ cá nhân trong release này.
4. Bảo toàn `assets/listening/*.jpg` thuộc người dùng và SVG fallbacks. Snapshot ZIP hiện không kèm 8 JPG Part 1; phải giữ bản đã có trên GitHub khi merge overlay.
5. Browser SpeechSynthesis là audio tổng hợp, không phải ETS audio/recording native speaker. Mock analytics không được mô tả là điểm TOEIC đã equate.
6. Không coi local PASS là bằng chứng remote Actions, Pages hoặc browser/device QA.

## 4. Quy chuẩn giao diện dùng chung

- Mọi Learning Unit detail (Flashcard, Review session, Grammar, Reading, Listening) dùng một Focus Workspace shell.
- Thay đổi shared shell chỉ thực hiện trong `assets/css/app.css`, `assets/css/design-system.css` và helper JS hiện hữu; không thêm CSS modal riêng cho từng page.
- Một vertical scroll owner duy nhất: `.learning-focus-content`. Content node khi chuyển vào workspace phải `overflow: visible`; không dùng max-height cố định/overflow auto bên trong trừ khi có lý do chức năng và được duyệt.
- Nội dung ngắn để khung co tự nhiên; nội dung dài cuộn ở workspace. Mobile/tablet dùng cùng thứ bậc nội dung, không tạo layout học thứ hai.
- Giữ keyboard access, focus visible, nút chạm tối thiểu khoảng 44px và `prefers-reduced-motion`.

## 5. Cổng nghiệm thu TOEIC — IELTS vẫn tạm hoãn

1. Blueprint 200 câu: Listening P1=6, P2=25, P3=39, P4=30; Reading P5=30, P6=16, P7=54 (29 single + 25 multiple).
2. Mở rộng reserve để hỗ trợ nhiều full forms; pool-size chưa thay thế editorial/psychometric review.
3. Review transcript, passage, distractor và tiếng Việt cho mọi câu trước khi đưa reserve vào full mock.
4. Vocabulary target 3,000–5,000 TOEIC-priority headwords là mục tiêu nội bộ, không phải danh sách ETS chính thức.
5. Duy trì Grammar coverage, local spaced repetition/progress, mock timer/submit/review và score integrity.
6. Chỉ chuyển IELTS khi các cổng TOEIC đạt, ít nhất một full 200-question mock hoàn chỉnh được review và người dùng đồng ý rõ ràng.

## 6. Lộ trình tiếp theo

1. **Vocabulary Batch 020:** ưu tiên business/workplace, finance, purchasing, HR và logistics; kiểm tra duplicate lemma/sense, ví dụ theo ngữ cảnh, IPA nguồn và collocations tự nhiên.
2. **Grammar expansion:** tăng độ phủ theo lỗi TOEIC P5/P6; tránh lesson/exercise trùng.
3. **Listening reserve:** duyệt độc lập 11 câu Batch 013 trước khi đưa vào mock; sau đó mở rộng P2/P3/P4 để giảm lặp.
4. **Hình trang trí:** chỉ thêm asset có filename/nguồn rõ; không biến hình trang trí thành dependency bắt buộc của PWA shell.
5. **Remote + device QA:** lấy log Actions gốc, kiểm tra Pages/base path/service worker và 8 JPG Part 1; test laptop 15.6 inch 100%, tablet, iPhone Safari, Android Chrome.

## 7. Kiểm thử v2.29.0 và giới hạn

- Code-level/local checks sẽ được ghi ở `reports/TEST_REPORT_TOEIC_Dictionary_v2.29.0.md` sau khi hoàn tất.
- Automated viewport/layout checks không thay thế thử nghiệm thiết bị thật. Không claim kiểm thử vật lý khi chưa thực hiện.
- Strict Part 1 photo gate chỉ PASS khi đủ 8 JPG thực tế trong repository test. Snapshot thiếu ảnh không được đánh dấu đạt.
- GitHub Actions/Pages chỉ được đánh dấu đạt sau khi có run và deployment thực tế.

## 8. Quy trình phát hành hai thế hệ

```bash
python tools/rotate-release-files.py          # dry-run
python tools/rotate-release-files.py --apply  # chỉ sau khi review danh sách
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/sync-version.py --check
```

Mỗi bản bàn giao chỉ giữ release docs của vX (previous) và vY (current). Rotator chỉ xử lý Markdown trong `docs/batches/`, `docs/reports/`, `docs/sources/` và root release notes. Các file cũ chuyển thành mô tả ngắn trong history. Tuyệt đối không động vào source app, JSON canonical, `assets/`, PWA shell, patches hoặc IndexedDB.
