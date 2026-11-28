# TOEIC Learning Outcome Evidence & Reconciliation — v2.95.78

Được xây dựng từ khung kết quả, bản đồ tài nguyên, bản đồ câu hỏi–tiêu chí và ngân hàng câu hỏi hiện hành.

## Tổng hợp

- Mục tiêu: **11**; tiêu chí: **33**.
- Có đường thu thập minh chứng cấp tiêu chí: **28/33 (84.8%)**; trong đó Foundation giữ **6/6**, TOEIC **22/27**.
- Còn **5** tiêu chí TOEIC chưa đo riêng: `listening-part-1-paraphrase-recognition`, `listening-part-2-distractor-resistance`, `listening-part-4-inference-action`, `reading-part-6-discourse-purpose`, `reading-part-7-paraphrase-inference`.
- Bản đồ có **1,082** liên kết câu hỏi–tiêu chí, trên **638** ID câu hỏi ổn định.
- Ứng dụng ghi nhận trong kho IndexedDB `objectiveProgress` đang có; không đổi schema IndexedDB v1 và không tạo DB mới.
- Các mục tiêu theo kỹ năng sử dụng câu trả lời đã hoàn tất; kết quả theo tiêu chí tính trên ID câu hỏi duy nhất. Thử lại không làm tăng mẫu số câu duy nhất.
- Rubric giải thích cho Grammar và Reading Part 5 là tự đánh giá của người học; không được diễn giải thành chấm tự động.
- Separate Part 5 timed accuracy dùng mốc nội bộ 30 giây/câu; không phải tiêu chuẩn thời gian hoặc quy đổi điểm ETS.
- 8 câu Listening Part 1 được ánh xạ nhưng vẫn dưới ngưỡng tối thiểu 10 câu. Không ánh xạ Listening reserve.
- Reading Part 7 còn cổng second-review; Separate Part 5 còn cổng independent-review. Việc ánh xạ không bỏ qua các cổng này.
- Đây là năng lực thu thập minh chứng ở mức phần mềm, không phải bằng chứng người học đã đạt, chứng nhận CEFR/ETS hoặc điểm TOEIC.

## Ma trận 33 tiêu chí

| Mục tiêu | Tiêu chí | Metric | Câu hỏi có ánh xạ | Ngưỡng mẫu số / đạt | Trạng thái | Cổng / ghi chú |
|---|---|---|---:|---|---|---|
| `foundation-pre-a1-a1` | `foundation-pre-a1-a1-recognition` — Nhận biết từ/cấu trúc nền tảng trong ngữ cảnh quen thuộc | `correct_rate` | 0 | 10 câu / 80% | `instrumented_practice_evidence` | content_exists_review_depth_required |
| `foundation-pre-a1-a1` | `foundation-pre-a1-a1-production` — Tạo câu ngắn đúng mẫu đã học | `rubric_score` | 0 | 10 câu / 80% | `instrumented_learner_self_report` | content_exists_review_depth_required |
| `foundation-pre-a1-a1` | `foundation-pre-a1-a1-retention` — Nhớ lại nội dung ở lần ôn cách quãng | `delayed_correct_rate` | 0 | 10 câu / 80% | `instrumented_delayed_recall` | content_exists_review_depth_required |
| `foundation-a2` | `foundation-a2-recognition` — Nhận biết và hiểu cấu trúc A2 trong ngữ cảnh công việc quen thuộc | `correct_rate` | 0 | 10 câu / 80% | `instrumented_practice_evidence` | content_exists_review_depth_required |
| `foundation-a2` | `foundation-a2-application` — Vận dụng cấu trúc A2 vào tình huống giao tiếp ngắn | `rubric_score` | 0 | 10 câu / 80% | `instrumented_learner_self_report` | content_exists_review_depth_required |
| `foundation-a2` | `foundation-a2-retention` — Nhớ lại nội dung A2 qua ôn tập cách quãng | `delayed_correct_rate` | 0 | 10 câu / 80% | `instrumented_delayed_recall` | content_exists_review_depth_required |
| `grammar-core` | `grammar-core-form-recognition` — Nhận diện cấu trúc ngữ pháp phù hợp trong câu | `correct_rate` | 1 | 10 câu / 80% | `instrumented_practice_evidence` | editorial_review_status_not_structured |
| `grammar-core` | `grammar-core-contextual-choice` — Chọn đáp án đúng theo cấu trúc và ngữ cảnh TOEIC | `correct_rate` | 168 | 10 câu / 80% | `instrumented_practice_evidence` | editorial_review_status_not_structured |
| `grammar-core` | `grammar-core-error-explanation` — Giải thích được lý do chọn đáp án và loại phương án nhiễu | `explanation_rubric` | 169 | 10 câu / 80% | `instrumented_learner_self_report` | editorial_review_status_not_structured |
| `listening-part-1` | `listening-part-1-visual-audio-match` — Ghép mô tả nghe được với hành động/vị trí trong ảnh | `correct_rate` | 8 | 10 câu / 80% | `instrumented_practice_evidence` | mixed_or_pending_review_check_item_level |
| `listening-part-1` | `listening-part-1-paraphrase-recognition` — Nhận diện cách diễn đạt tương đương trong audio | `correct_rate` | 0 | 10 câu / 80% | `criteria_defined_not_yet_instrumented` | mixed_or_pending_review_check_item_level |
| `listening-part-1` | `listening-part-1-detail-retention` — Nhớ chi tiết chính sau khi nghe một lần | `delayed_correct_rate` | 8 | 10 câu / 80% | `instrumented_delayed_recall` | mixed_or_pending_review_check_item_level |
| `listening-part-2` | `listening-part-2-response-intent` — Nhận diện loại câu hỏi và ý định giao tiếp | `correct_rate` | 21 | 10 câu / 80% | `instrumented_practice_evidence` | mixed_or_pending_review_check_item_level |
| `listening-part-2` | `listening-part-2-natural-response` — Chọn phản hồi tự nhiên, đúng ngữ cảnh | `correct_rate` | 25 | 10 câu / 80% | `instrumented_practice_evidence` | mixed_or_pending_review_check_item_level |
| `listening-part-2` | `listening-part-2-distractor-resistance` — Tránh bẫy lặp từ và đáp án nghe có vẻ liên quan | `correct_rate` | 0 | 10 câu / 80% | `criteria_defined_not_yet_instrumented` | mixed_or_pending_review_check_item_level |
| `listening-part-3` | `listening-part-3-conversation-purpose` — Xác định mục đích cuộc hội thoại | `correct_rate` | 5 | 10 câu / 80% | `instrumented_practice_evidence` | mixed_or_pending_review_check_item_level |
| `listening-part-3` | `listening-part-3-detail-inference` — Tìm chi tiết và suy luận từ hội thoại | `correct_rate` | 33 | 10 câu / 80% | `instrumented_practice_evidence` | mixed_or_pending_review_check_item_level |
| `listening-part-3` | `listening-part-3-speaker-linking` — Liên kết người nói, vai trò và hành động | `correct_rate` | 1 | 10 câu / 80% | `instrumented_practice_evidence` | mixed_or_pending_review_check_item_level |
| `listening-part-4` | `listening-part-4-talk-purpose` — Xác định mục đích thông báo/bài nói | `correct_rate` | 1 | 10 câu / 80% | `instrumented_practice_evidence` | mixed_or_pending_review_check_item_level |
| `listening-part-4` | `listening-part-4-detail-tracking` — Theo dõi thời gian, địa điểm, con số và hành động | `correct_rate` | 29 | 10 câu / 80% | `instrumented_practice_evidence` | mixed_or_pending_review_check_item_level |
| `listening-part-4` | `listening-part-4-inference-action` — Suy luận bước tiếp theo hoặc đối tượng nghe | `correct_rate` | 0 | 10 câu / 80% | `criteria_defined_not_yet_instrumented` | mixed_or_pending_review_check_item_level |
| `reading-part-5` | `reading-part-5-sentence-completion` — Hoàn thành câu dựa trên ngữ pháp và từ vựng | `correct_rate` | 60 | 10 câu / 80% | `instrumented_practice_evidence` | editorial_review_status_mixed |
| `reading-part-5` | `reading-part-5-word-form-selection` — Chọn đúng dạng từ và kết hợp từ | `correct_rate` | 14 | 10 câu / 80% | `instrumented_practice_evidence` | editorial_review_status_mixed |
| `reading-part-5` | `reading-part-5-distractor-explanation` — Giải thích được khác biệt giữa đáp án đúng và nhiễu | `explanation_rubric` | 60 | 10 câu / 80% | `instrumented_learner_self_report` | editorial_review_status_mixed |
| `reading-part-6` | `reading-part-6-text-cohesion` — Chọn câu/từ/cụm từ bảo đảm mạch văn | `correct_rate` | 10 | 10 câu / 80% | `instrumented_practice_evidence` | editorial_review_status_mixed |
| `reading-part-6` | `reading-part-6-context-completion` — Hoàn thành chỗ trống theo ngữ cảnh toàn đoạn | `correct_rate` | 32 | 10 câu / 80% | `instrumented_practice_evidence` | editorial_review_status_mixed |
| `reading-part-6` | `reading-part-6-discourse-purpose` — Nhận diện mục đích và liên kết thông tin trong văn bản | `correct_rate` | 0 | 10 câu / 80% | `criteria_defined_not_yet_instrumented` | editorial_review_status_mixed |
| `reading-part-7` | `reading-part-7-information-location` — Tìm đúng thông tin trong một hoặc nhiều văn bản | `correct_rate` | 195 | 10 câu / 80% | `instrumented_practice_evidence` | part7_expansion_requires_second_review |
| `reading-part-7` | `reading-part-7-paraphrase-inference` — Nhận diện diễn đạt lại và suy luận có căn cứ | `correct_rate` | 0 | 10 câu / 80% | `criteria_defined_not_yet_instrumented` | part7_expansion_requires_second_review |
| `reading-part-7` | `reading-part-7-cross-document-link` — Kết nối chi tiết giữa các văn bản đơn/kép/ba | `correct_rate` | 2 | 10 câu / 80% | `instrumented_practice_evidence` | part7_expansion_requires_second_review |
| `part5-sentence-completion` | `part5-sentence-completion-accuracy` — Chọn đáp án đúng trong câu Part 5 | `correct_rate` | 80 | 10 câu / 80% | `instrumented_practice_evidence` | pending_independent_review_practice_only_not_mock_eligible |
| `part5-sentence-completion` | `part5-sentence-completion-time-management` — Hoàn thành câu trong giới hạn thời gian mục tiêu | `timed_accuracy` | 80 | 10 câu / 80% | `instrumented_practice_evidence` | pending_independent_review_practice_only_not_mock_eligible |
| `part5-sentence-completion` | `part5-sentence-completion-error-review` — Phân loại lỗi và giải thích đáp án sau luyện tập | `explanation_rubric` | 80 | 10 câu / 80% | `instrumented_learner_self_report` | pending_independent_review_practice_only_not_mock_eligible |

## Giải thích trạng thái

- `instrumented_practice_evidence`: có đường ghi nhận độ chính xác sau khi người học xác nhận kết quả.
- `instrumented_learner_self_report`: có rubric tự đánh giá, không phải chấm độc lập.
- `instrumented_delayed_recall`: có lịch ôn cách quãng và lưu lần nhớ lại đến hạn.
- `criteria_defined_not_yet_instrumented`: tiêu chí vẫn được định nghĩa nhưng chưa nhận điểm riêng.
- `content_review_pending`: nội dung còn cổng biên tập; kết quả không thể nâng trạng thái thành đạt ngưỡng.

> Mọi tỷ lệ trong báo cáo mô tả khung đo lường hoặc dữ liệu do người học ghi nhận trên thiết bị; không tự suy ra năng lực thực tế, chứng nhận hay mức độ sẵn sàng cho Mock.
