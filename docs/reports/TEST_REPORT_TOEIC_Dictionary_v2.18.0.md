# Test Report — TOEIC Dictionary v2.18.0

Ngày: 11/11/2026  
Trạng thái: local release candidate; chưa push/deploy.

## Kết quả tổng hợp

| Nhóm kiểm tra | Kết quả | Ghi chú |
|---|---:|---|
| Nhóm test chức năng nhanh | 102/102 PASS | Baseline IDs, guarded patch, learning content, dashboard, design system, evidence, distractor, choice history/identity, answer-position balance, editorial review |
| `test_sync_version` | 12/12 PASS | Chạy theo module hoàn chỉnh |
| `test_validator` | 33/33 PASS | Module discovery chạm timeout sandbox; các method ở cuối nhóm được chạy riêng thành công |
| **Tổng xác nhận** | **147/147 PASS** | Tất cả methods đã có kết quả PASS; suite validator hoàn tất bằng chạy tách method sau khi module timeout |

Lưu ý: chạy toàn bộ `test_validator` trong một process bị chạm giới hạn thời gian sandbox ở phần cuối suite. Các method còn lại (bao gồm hai test siết baseline) đã được chạy riêng; toàn bộ 33/33 method đều trả về PASS. Không dùng kết quả timeout của lần chạy module để kết luận test thất bại.

## Validator và nội dung

- `python tools/validate-data.py`: **PASS**, 928 records, 0 ERROR, 12 cảnh báo legacy đã biết (DF005=3, EX006=1, FD001=8); 0 ID thêm, 0 ID mất so với baseline. SHA-256 ID set prefix `dd1705e64c8df4ad`.
- `python tools/validate-learning-content.py`: **PASS**, Listening 56 units/102 questions; Reading 35 units/109 questions (P7 63); Grammar 25 lessons/54 exercises; 0 errors, 0 warnings.
- `python tools/sync-version.py --check`: **PASS**, manifest, Service Worker, HTML, README, Master và Changelog cùng 2.18.0.
- Evidence audit: 211 câu được lập bản đồ bằng chứng. Distractor structural audit: 132 câu Part 3/4/7. Coverage audit: 928 từ và số liệu Listening/Reading/Grammar đúng baseline.

## Runtime, cú pháp và đóng gói nguồn

- `node tools/tests/runtime-render-smoke.mjs`: **PASS**; Reading/Listening/Grammar, historical choice, choice-ID migration smoke và idempotency.
- `python -m py_compile tools/*.py tools/tests/*.py`: **PASS**.
- `node --check sw.js` và toàn bộ `assets/js/*.js`: **PASS**.
- GitHub Actions workflow YAML parse: **PASS**, một job `validate`, 24 steps.
- 74/74 đường dẫn APP_SHELL tồn tại. Ba dòng sidebar status có trong HTML. Không có Markdown đặt ngoài `docs/`.

## Nội dung/UX thay đổi

- Sidebar desktop giữ footer trạng thái cuối menu trong viewport; menu cuộn độc lập ở chiều cao thấp. Đã thêm 2 CSS regression tests.
- Internal second-pass review đã rà 63 câu Part 7 /24 sets; hai điểm timeline trong tài liệu nguồn được làm rõ. Đã thêm 4 editorial regression tests.
- Không thay đổi đáp án, ID, thứ tự câu hỏi hoặc số lượng câu trong Part 7.
- Không thay đổi 928 vocabulary IDs hoặc IndexedDB schema/version/store.
- Người dùng hoãn kiểm thử import dữ liệu cá nhân IndexedDB; không import, đọc hoặc chỉnh sửa profile cá nhân.

## Chạy lại tại local

```bash
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/sync-version.py --check
node tools/tests/runtime-render-smoke.mjs
cd tools/tests
PYTHONPATH=. python -m unittest test_design_system test_editorial_review -v
```

Để hoàn tất phần test còn thiếu, có thể chạy lại `PYTHONPATH=. python -m unittest test_validator -v` trong môi trường không giới hạn thời gian để quan sát một lần chạy module trọn vẹn; các 33 method đã được chạy riêng và PASS trong lần xác minh này.

## ZIP/package verification

- ZIP chứa 190 tệp.
- ZIP CRC: PASS; giải nén sạch và đối chiếu từng tệp: 190/190 giống chính xác.
- SHA-256 được lưu trong sidecar `.sha256` ngoài gói.
- Các validator, version sync, runtime smoke, Python compile và JavaScript syntax đã chạy lại trên thư mục giải nén sạch.

## Chưa được xác minh

- Không có bằng chứng chạy GitHub Actions từ xa sau commit/push.
- Không có bằng chứng GitHub Pages deploy mới.
- Không có visual QA trình duyệt thật ở 100% zoom trên laptop 15,6 inch; CSS regression không thay thế ảnh chụp/interaction trên thiết bị.
- Không có kiểm thử iOS Safari, Android Chrome, iPadOS Safari hoặc PWA offline trên thiết bị vật lý.
- Không thực hiện import/export hoặc migration test với IndexedDB cá nhân theo yêu cầu người dùng.
