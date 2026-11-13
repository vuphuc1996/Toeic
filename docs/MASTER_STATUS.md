# TOEIC DICTIONARY — MASTER STATUS

> **Nguồn trạng thái và lộ trình duy nhất.** Cập nhật trực tiếp file này ở mọi release; không tạo Master/roadmap riêng theo phiên bản. Nội dung lịch sử được lưu tại `docs/archive/PROJECT_HISTORY.md`; quyết định tương thích nằm tại `docs/COMPATIBILITY.md`.

## 1. Trạng thái hiện tại — v2.28.0

- **Ngày kiểm kê:** 2026-11-13.
- **Phiên bản mã nguồn đang kiểm kê:** v2.28.0 (Vocabulary Batch 018; documentation/release rotation; local release candidate).
- **Current candidate:** `v2.28.0`, phát triển trực tiếp từ baseline `v2.27.0`.
- **Previous stable/base:** `v2.27.0`.
- **Repository:** `vuphuc1996/Toeic` — ứng dụng nằm tại repository root.
- **Nền tảng:** GitHub Pages + PWA tĩnh; không có backend, GAS, iframe hoặc Cloudflare dependency.
- **Trạng thái phát hành:** local release candidate. Không khẳng định GitHub Actions, Pages deployment hay QA thiết bị thật đã đạt.

### Nội dung và số liệu hiện hành

| Hạng mục | Trạng thái v2.28.0 |
|---|---:|
| Từ vựng canonical | **979** headwords (971 ở v2.27.0 + 8 Batch 018) |
| US IPA | 631/979 |
| Word-family records | 131 |
| Verb-form records | 303 |
| Collocation records | 809 |
| Listening | 63 units / 113 questions |
| Reading | 35 resources / 109 questions |
| Grammar | 25 lessons / 54 exercises |
| Mock practice | Quick 15 phút / 25 câu; Half 60 phút / 100 câu; Full 120 phút / 200 câu |

Các số trên mô tả dữ liệu ứng dụng, không phải xác nhận nội dung đã được ETS hoặc chuyên gia độc lập chứng nhận. CEFR là ước lượng biên tập; chỉ số luyện tập và tỷ lệ đúng không phải điểm TOEIC quy đổi.

### Thay đổi của v2.28.0

- Batch 018 thêm `affidavit`, `bidder`, `bond`, `broker`, `capital`, `claimant`, `lien`, `margin`; tổng canonical 979. Batch provenance ở `data/vocabulary/batch-007.json`; A–Z JSON vẫn là nguồn runtime duy nhất.
- Lịch sử batch/report cũ được gom vào `docs/archive/PROJECT_HISTORY.md`.
- Quyết định nghỉ hưu/tương thích được tập trung tại `docs/COMPATIBILITY.md`.
- Handoff chỉ giữ hai thế hệ gần nhất: v2.27.0 (previous) và v2.28.0 (current).

## 2. Phạm vi sản phẩm

- Chỉ phát triển **TOEIC Listening & Reading (7 Parts)**.
- IELTS/Academic vocabulary, lessons, filters và roadmap tasks tiếp tục tạm hoãn cho đến khi toàn bộ cổng nghiệm thu TOEIC tại Mục 4 đạt và người dùng xác nhận chuyển giai đoạn.
- Không sao chép câu hỏi/audio có bản quyền của ETS; nội dung bài tập là nội dung biên soạn riêng. Browser SpeechSynthesis là âm thanh tổng hợp, không phải audio ETS hoặc bản thu native speaker.

## 3. Ràng buộc kỹ thuật và dữ liệu

1. `data/vocabulary/A.json`–`Z.json` là nguồn dữ liệu từ vựng canonical. Batch JSON chỉ là provenance/biên tập, không được đọc như nguồn runtime thứ hai.
2. Stable vocabulary IDs và IDs câu hỏi/đáp án đã có phải được bảo toàn. Không đổi ID chỉ để làm đẹp dữ liệu hoặc đổi thứ tự câu hỏi đã có tiến độ người học.
3. Chỉ thêm IPA, CEFR, word family, verb forms, synonyms, antonyms và collocations khi có căn cứ. Không tự điền dữ liệu để tăng tỷ lệ coverage; CEFR chưa được kiểm định độc lập phải ghi rõ là editorial estimate.
4. IndexedDB giữ nguyên database `toeic-vocabulary-phase1`, version `1`, object store `workspace`. Không import/export, inspect, reset hoặc migrate hồ sơ cá nhân trong các batch này; người dùng đã hoãn kiểm thử dữ liệu cá nhân.
5. Giữ nguyên `assets/listening/*.jpg` do người dùng sở hữu trên GitHub. Snapshot nguồn hiện tại không chứa 8 JPG Part 1; SVG fallback có sẵn. Cần kiểm tra byte ảnh trên repository thật trước khi release; không xóa thư mục ảnh khi merge overlay.
6. Mock report chỉ trình bày số câu đúng, accuracy và chỉ báo luyện tập nội bộ. Không giả lập điểm ETS 10–990 hoặc CEFR khi chưa có mô hình equating được xác thực.
7. Không coi local PASS là bằng chứng cho remote CI, GitHub Pages hoặc kiểm thử trình duyệt/thiết bị vật lý.

## 4. Cổng nghiệm thu TOEIC — điều kiện trước khi mở IELTS

1. **Blueprint:** đủ 200 câu theo phân phối P1=6, P2=25, P3=39, P4=30; P5=30, P6=16, P7=54 (29 single-passage + 25 multiple-passage), Listening 45 phút và Reading 75 phút.
2. **Content volume:** pool hiện đáp ứng tối thiểu lựa chọn một form, nhưng cần mở rộng reserve để tạo nhiều form khác nhau mà không lặp quá nhiều; số lượng chưa thay thế editorial review.
3. **Listening:** Parts 1–4 có transcript, giải thích tiếng Việt, câu hỏi/distractors tự nhiên; Part 1 phân biệt rõ ảnh có bản quyền với SVG illustration; TTS không được mô tả là audio ETS/recorded.
4. **Reading:** Parts 5–7 gồm câu đơn, text completion và single/double/triple passages; mỗi đáp án phải có căn cứ và giải thích.
5. **Vocabulary:** mục tiêu nội bộ 3,000–5,000 TOEIC-priority headwords/lemmas, không phải danh sách chính thức của ETS; giữ ID và thông tin sense/POS/meaning/example/source/review status.
6. **Grammar:** duy trì coverage matrix TOEIC, gắn bài học với lỗi P5/P6; tránh lesson trùng lặp và distractor chung chung.
7. **Practice/analytics:** review sai, spaced repetition, bookmark, gợi ý theo Part, lịch sử và thống kê; bảo toàn dữ liệu học cục bộ.
8. **Mock engine:** timer, navigation, flags, section transition, resume, submit, answer review và phân tích theo Part; nêu rõ practice-only.
9. **Release QA:** validators, patch dry-run, tests, app-shell/offline checks, browser/device QA và package verification. Phase 5 chưa hoàn tất nếu chưa có kết quả QA thiết bị thật.
10. **IELTS gate:** chỉ chuyển giai đoạn khi tất cả điều kiện trên đạt, tối thiểu một full 200-question mock được review và người dùng đồng ý rõ ràng.

## 5. Lộ trình ưu tiên tiếp theo

1. **Vocabulary Batch 019:** mở rộng TOEIC vocabulary theo nguồn, ưu tiên business/workplace, finance, purchasing, HR và logistics; kiểm tra trùng lemma/sense, ví dụ theo ngữ cảnh, IPA có nguồn và collocations tự nhiên.
2. **Grammar expansion:** thêm lesson/exercise theo cấu trúc và độ khó tăng dần; bảo toàn IDs và các bài hiện có.
3. **Study/decorative images:** cung cấp link tải trực tiếp, tên file và thư mục đích cụ thể; ảnh trang trí không được là dependency bắt buộc của app shell.
4. **Listening reserve:** duyệt độc lập 11 câu Batch 013 trước khi đưa vào form; sau đó bổ sung Part 2/3/4 để tạo nhiều đề ít lặp.
5. **Current platform benchmark:** so sánh tính năng/giá/AI/audio/offline của các nền tảng TOEIC bằng nguồn chính thức và ngày truy cập rõ ràng.
6. **Regression + device QA:** kiểm tra Mock 15/60/120 phút, refresh/resume, PWA offline, layout laptop 15.6 inch ở 100%, tablet, iPhone Safari và Android Chrome.
7. **Remote release verification:** lấy log GitHub Actions gốc, xác minh Pages deployment/base path/service worker và strict validation 8 JPG. Run người dùng đã cung cấp `42981524564` / job `130392820806` từng báo `exit code 1`; chưa có log gốc/commit/workflow revision nên nguyên nhân vẫn chưa được kết luận.

## 6. Quy tắc luân phiên phiên bản và quản lý tài liệu

### Cửa sổ phát hành hai thế hệ

- Mỗi handoff chỉ giữ **previous version + current version**.
- Khi tạo phiên bản mới từ v2.28.0 (ví dụ v2.29.0): v2.28.0 trở thành previous; v2.29.0 là current; v2.27.0 rời khỏi active handoff.
- Nội dung cần truy vết của phiên bản cũ được đưa vào `docs/archive/PROJECT_HISTORY.md` trước khi xóa bản file riêng. Không xóa dữ liệu/asset runtime chỉ vì phiên bản cũ.
- Root chỉ giữ hai file `V*_UPDATE_NOTES.txt` gần nhất. `docs/batches/` và `docs/reports/` chỉ giữ tài liệu chi tiết thuộc hai thế hệ phát hành trong handoff.

### Quy trình rotate an toàn

```bash
# 1) Preview danh sách file sẽ archive/retire
python tools/rotate-release-files.py

# 2) Chỉ sau khi kiểm tra danh sách và bảo đảm history đã được lưu
python tools/rotate-release-files.py --apply

# 3) Xác minh lại thư mục và release gates
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/sync-version.py --check
```

Script mặc định dry-run; `--apply` chỉ xử lý release notes, batch/report Markdown cũ và append lịch sử. Không được dùng lệnh dọn dẹp tổng quát để xóa `assets/`, dữ liệu canonical, `patches/`, profile hay file ảnh người dùng.

### Cấu trúc tài liệu chuẩn

```text
docs/
├── MASTER_STATUS.md          # trạng thái + roadmap duy nhất
├── COMPATIBILITY.md          # tương thích/ngừng hỗ trợ duy nhất
├── CHANGELOG.md              # lịch sử thay đổi gọn
├── CONTENT_OPERATIONS.md     # quy trình cập nhật nội dung
├── DESIGN_SYSTEM.md          # quy tắc UI
├── batches/                  # batch thuộc hai release gần nhất
├── reports/                  # test/coverage thuộc hai release gần nhất
├── sources/                  # nguồn từ điển và dữ liệu
├── reference/                # benchmark/tài liệu tham khảo
└── archive/PROJECT_HISTORY.md# lịch sử cũ đã hợp nhất
```

- Không tạo file Master, roadmap, compatibility, test summary hoặc batch summary thứ hai nếu nội dung có thể cập nhật vào file tương ứng.
- `docs/README.md` là trang mục lục, không phải nguồn chỉ thị thứ hai.
- Mỗi release phải sửa Master + Changelog và cập nhật Compatibility khi có thay đổi tương thích.

## 7. Kiểm thử và giới hạn v2.28.0

- Local PASS: data validator (979 records, 0 errors/0 warnings); learning validator (0 errors, 8 warnings do snapshot thiếu JPG); version sync; Learning Focus Workspace; Flashcard image policy; Mock UI integrity; Mock exam engine; Listening/TTS regression; runtime render/migration smoke; Python unit tests 67/67 across five modules.
- ZIP full source và overlay đã kiểm tra CRC; overlay không có thao tác xóa file. Bắt buộc chạy rotator ở repository copy để archive/retires các tài liệu cũ sau khi merge overlay.
- Chưa xác nhận: strict Part 1 photo gate 8/8; remote Actions/Pages; browser/device QA vật lý; độc lập editorial/psychometric signoff.

## 8. Tài liệu đang hoạt động

- [Documentation Center](README.md)
- [Compatibility & Retirement Register](COMPATIBILITY.md)
- [Content Operations](CONTENT_OPERATIONS.md)
- [Project History](archive/PROJECT_HISTORY.md)
- [v2.28.0 test report](reports/TEST_REPORT_TOEIC_Dictionary_v2.28.0.md)
- [v2.28.0 content coverage](reports/TOEIC_CONTENT_COVERAGE_v2.28.0.md)
- [Vocabulary Batch 018](batches/TOEIC_VOCABULARY_BATCH_018_v2.28.0.md)
