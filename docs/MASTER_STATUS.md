# TOEIC DICTIONARY — MASTER STATUS

> **Nguồn trạng thái và lộ trình duy nhất.** Mọi release cập nhật trực tiếp file này; không tạo Master/Roadmap riêng. Chi tiết phát hành nằm trong `CHANGELOG.md`; tài liệu đã nghỉ hưu nằm trong `archive/PROJECT_HISTORY.md`; tương thích nằm trong `COMPATIBILITY.md`.

- **Ngày kiểm kê:** 2026-11-14.
- **Phiên bản mã nguồn đang kiểm kê:** v2.30.0 (Repeatable Practice, Attempt History & Vocabulary Batch 020; local candidate).
- **Current candidate:** v2.30.0, phát triển từ v2.29.0.
- **Previous baseline:** v2.29.0.
- **Repository:** `vuphuc1996/Toeic`; app source nằm ở root repository.
- **Nền tảng:** GitHub Pages + static PWA; không backend/GAS/iframe/Cloudflare.
- **Mục tiêu:** hoàn tất các hạng mục có thể kiểm chứng trước 2026-12-01 để người dùng bắt đầu học. Không cam kết “hoàn hảo 100%” tuyệt đối; bắt buộc phân biệt automated PASS, editorial review, remote deployment và physical-device QA.
- **Trạng thái triển khai:** local candidate; code-level release gates cho retry + Batch 020 PASS. Remote GitHub Actions/Pages và QA thiết bị thật chưa xác nhận.

## 1. Tóm tắt thay đổi v2.30.0

### Luyện tập và làm lại câu hỏi

1. Reading, Listening và Grammar có nút **Làm lại câu này** sau khi đã trả lời. Lựa chọn được mở lại nhưng kết quả cũ không bị xóa.
2. Có nút **Làm lại toàn bộ bài** để mở lại các câu đã trả lời hiện tại; thao tác yêu cầu xác nhận.
3. `answers` tiếp tục lưu kết quả hiện tại/lần gần nhất; `attemptHistory` lưu các lần trước theo chỉ số câu hỏi.
4. Mỗi attempt mới lưu đáp án đã chọn, stable `choiceId`, đúng/sai, đáp án chuẩn, giải thích, timestamp và số thứ tự lần làm. Các attempt cũ được hiển thị lại bên dưới câu hỏi.
5. Độ phủ câu hỏi tính theo **câu duy nhất đã từng làm**, không cộng dồn số lần thử. Accuracy theo kết quả lần làm mới nhất; tổng số lần thử được hiển thị riêng.
6. Không nâng IndexedDB: vẫn DB `toeic-vocabulary-phase1`, version `1`, store `workspace`. Dữ liệu progress v1 cũ không có `attemptHistory` vẫn hoạt động; history là trường additive trong cùng object.
7. Choice-ID migration xử lý cả đáp án hiện tại và attempt đã archive; không đổi question index/ID.

### Vocabulary Batch 020

- Bổ sung 13 từ: `accrual`, `receivable`, `collateral`, `escrow`, `consignor`, `consignee`, `stockout`, `bottleneck`, `throughput`, `outlay`, `covenant`, `timesheet`, `replenishment`.
- Canonical bank tăng từ 979 lên **992 headwords**; 979 ID cũ được giữ nguyên, 13 ID mới được thêm.
- `data/vocabulary/A.json`–`Z.json` vẫn là runtime source duy nhất; `batch-008.json` chỉ là provenance.
- US IPA chỉ được điền khi nguồn kiểm tra có cung cấp; `consignor` và `receivable` không có US transcription trên trang Cambridge đã kiểm tra nên được để trống, không suy đoán.
- CEFR remains editorial estimate; chưa được chuyên gia độc lập chứng nhận.

## 2. Baseline dữ liệu và module

| Hạng mục | Baseline v2.30.0 |
|---|---:|
| Vocabulary canonical | **992 headwords** |
| US IPA | Được ghi khi có nguồn US rõ ràng; không ép đủ 100% |
| Word-family records | 131 (trước Batch 020; batch mới không thêm family) |
| Verb-form records | 303 (trước Batch 020; batch mới không thêm verb) |
| Collocations | 822 (cập nhật từ 809; kiểm tra validator) |
| Listening | 63 units / 113 questions |
| Reading | 35 resources / 109 questions |
| Grammar | 25 lessons / 54 exercises |
| Mock practice | 15m/25Q · 60m/100Q · 120m/200Q |

Các con số là kiểm kê cấu trúc dữ liệu; không tự chứng minh độ đúng ngữ nghĩa, chất lượng đề thi hoặc tương đương ETS. Mock score là practice indicator, không phải điểm ETS quy đổi.

## 3. Ràng buộc kỹ thuật và dữ liệu

1. `data/vocabulary/A.json`–`Z.json` là runtime source duy nhất. `batch-*.json` chỉ là editorial provenance.
2. Giữ stable vocabulary IDs, reading/listening/grammar resource IDs, question indices và choice IDs. Chỉ append question mới; không reorder câu đã có progress.
3. IndexedDB giữ `toeic-vocabulary-phase1`, version `1`, store `workspace`. Không import/export, inspect, reset hoặc migrate hồ sơ cá nhân nếu chưa có yêu cầu riêng.
4. `attemptHistory` là trường bổ sung trong object progress hiện tại, không tạo object store hay schema version mới. `answers` giữ kết quả hiện tại; lịch sử không xóa khi retry.
5. Bảo toàn `assets/listening/*.jpg` thuộc người dùng và SVG fallbacks. Snapshot ZIP hiện không kèm 8 JPG Part 1; phải giữ ảnh đã có trên GitHub khi merge.
6. Browser SpeechSynthesis là audio tổng hợp, không phải ETS audio/recording native speaker. Mock analytics không phải điểm TOEIC chính thức.
7. Local PASS không chứng minh remote Actions, Pages hay kiểm thử browser/device.

## 4. Quy chuẩn giao diện dùng chung

- Flashcard, Review, Grammar, Reading và Listening detail dùng một Focus Workspace shell.
- Chỉ `.learning-focus-content` sở hữu cuộn dọc; không tạo scrollbar lồng trong question/card detail.
- Nội dung ngắn co tự nhiên; nội dung dài cuộn ở workspace. Mobile/tablet giữ cùng thứ bậc nội dung, không tạo UI học thứ hai.
- Thay đổi shell trong CSS/JS dùng chung; không thêm modal/backdrop riêng theo từng module nếu không có lý do chức năng rõ ràng.
- Giữ keyboard access, focus visible, touch target khoảng 44px và `prefers-reduced-motion`.

## 5. Cổng nghiệm thu TOEIC — IELTS vẫn tạm hoãn

1. Blueprint 200 câu: Listening P1=6, P2=25, P3=39, P4=30; Reading P5=30, P6=16, P7=54 (29 single +25 multiple).
2. Mở rộng reserve để hỗ trợ nhiều full forms; pool-size không thay thế editorial/psychometric review.
3. Duyệt transcript, passage, distractor và tiếng Việt cho mọi câu trước khi đưa reserve vào Mock.
4. Vocabulary target 3,000–5,000 TOEIC-priority headwords là mục tiêu nội bộ, không phải danh sách ETS chính thức.
5. Duy trì Grammar coverage, local progress, retry/history, mock timer/submit/review và score integrity.
6. Chỉ chuyển IELTS khi cổng TOEIC đạt, ít nhất một full 200-question mock hoàn chỉnh đã được review và người dùng đồng ý rõ ràng.

## 6. Lộ trình và mục tiêu trước 2026-12-01

| Ưu tiên | Hạng mục | Trạng thái / tiêu chí hoàn thành |
|---|---|---|
| P0 | v2.30 practice retry | **LOCAL PASS** — Reading/Listening/Grammar retry từng câu + toàn bài; history, stable choice ID, stats và legacy v1 regression đạt |
| P0 | Vocabulary Batch 020 | **LOCAL PASS** — 13 từ có source note, ID duy nhất, A–Z canonical, ví dụ/dịch và IPA không suy đoán; editorial review vẫn cần |
| P0 | Remote + device QA | **PENDING USER QA** — GitHub Actions/Pages, laptop 15.6 inch 100%, tablet, iPhone Safari, Android Chrome; ghi PASS/FAIL cụ thể |
| P0 | Part 1 photo gate | **BLOCKED IN SNAPSHOT** — cần xác nhận đủ 8 JPG thực tế trên repository và strict photo validator đạt |
| P1 | Grammar expansion | Chưa triển khai — tăng phủ Part 5/6, bài tập không trùng, rationale và distractor được rà soát |
| P1 | Listening reserve | Chưa triển khai — duyệt độc lập 11 câu Batch 013; sau đó mở rộng P2/P3/P4 để giảm lặp |
| P1 | Reading/Mock pool | Bổ sung resource/question có source trace; nâng số đề ít lặp hơn 1 full form |
| P2 | Vocabulary quality pass | Ưu tiên kiểm tra definition/example, collocation, IPA và lexical relation của ngân hàng cũ; không ép đủ trường |

Thứ tự triển khai: kiểm tra v2.30 code-level retry + data → Vocabulary/Grammar → Listening/Reading reserve → Mock pool → remote/device QA và tổng nghiệm thu. Có thể triển khai song song chỉ khi không đụng cùng dữ liệu/ID.

## 7. Kiểm thử và giới hạn v2.30.0

- Chi tiết kết quả từng command/test chỉ ghi trong `reports/TEST_REPORT_TOEIC_Dictionary_v2.30.0.md` sau khi chạy thực tế; không điền PASS trước.
- Validator kiểm tra cấu trúc, không xác nhận đầy đủ độ tự nhiên/đúng nghĩa của tất cả từ/câu hỏi.
- Strict Part 1 photo gate chỉ PASS khi đủ 8 JPG thực tế trong repository.
- GitHub Actions/Pages chỉ PASS sau khi có run/deployment thực tế; browser/device QA phải có kết quả từ thiết bị thật.

## 8. Quy trình phát hành hai thế hệ

```bash
python tools/rotate-release-files.py          # dry-run
python tools/rotate-release-files.py --apply  # only after review
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/sync-version.py --check
```

Mỗi bản bàn giao chỉ giữ release-specific docs của previous + current. Khi v2.31.0 được xuất bản, v2.30.0 trở thành previous; v2.29.0 được tóm tắt vào `archive/PROJECT_HISTORY.md` rồi nghỉ hưu khỏi batch/report/update-notes đang hoạt động. Rotator không được chạm app source, canonical JSON, assets, PWA shell hay local learner profiles.
