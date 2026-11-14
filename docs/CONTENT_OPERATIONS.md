# TOEIC Content Operations — governed update workflow

> Quy trình chuẩn cho dữ liệu học tập, kiểm duyệt nội dung, Mock Exam và phát hành. Không tạo tài liệu hướng dẫn riêng cho từng module nếu có thể bổ sung quy tắc tại đây.

## 1. Scope

- Chỉ phát triển TOEIC Listening & Reading cho đến khi Master ghi nhận đủ cổng nghiệm thu và người dùng đồng ý chuyển giai đoạn.
- Nội dung mới là tài liệu luyện tập do dự án tự biên soạn; không sao chép câu hỏi/audio ETS.
- Phân biệt rõ `draft`, `internal-editorial-reviewed`, `reserve-pending-independent-review` và kết quả kiểm thử tự động. Không dùng automated PASS để tuyên bố đã có reviewer độc lập.

## 2. Canonical sources

| Content | Canonical path | Rule |
|---|---|---|
| Vocabulary | `data/vocabulary/[A-Z].json` | 26 file A–Z là runtime source duy nhất; giữ stable IDs. |
| Vocabulary batches | `data/vocabulary/batch-*.json` | Provenance biên tập, không phải runtime source thứ hai. |
| Topics | `data/categories.json` | Không tự tạo topic ID ngoài danh mục chuẩn. |
| Related gloss | `data/related-terms.json` | Chỉ thêm gloss khi nghĩa/quan hệ có cơ sở. |
| Listening | `data/listening/listening-library.json` | Part, unit, transcript/segments, choices, key, explanation và editorial status. |
| Reading | `data/readings/reading-library.json` | Part, document type, passage/documents, questions, key, explanation và source evidence. |
| Grammar | `data/grammar/lessons.json` | Stable lesson/exercise IDs, bốn choices, answerIndex và rationale. |

## 3. Vocabulary quality

- Rà spelling/lemma, POS theo sense, Vietnamese meaning, English definition, examples + translations, topics và CEFR estimate.
- IPA chỉ ghi khi xác định được đúng giọng US/UK và có nguồn; không suy đoán để lấp trường trống.
- Word family, verb forms, synonyms, antonyms và collocations là trường có điều kiện; không ép thêm dữ liệu không tự nhiên.
- Word-family chỉ liên kết các lemma có quan hệ hình thái/từ loại rõ ràng. Ưu tiên từ đã tồn tại trong từ điển; POS và `meaning_vi` phải khớp sense tương ứng của mục được liên kết. Không suy diễn quan hệ chỉ vì hai từ giống mặt chữ; tránh các trường hợp khác nghĩa hoặc chỉ liên quan theo chủ đề.
- Khi một cặp có hai mục từ trong kho, giữ liên kết hai chiều nếu phù hợp với POS. Không thay ID, thứ tự sense, ví dụ hoặc tiến độ học của headword hiện hữu.
- Mỗi data patch pin `baseDataVersion`, `targetDataVersion`, ID-set hash, stable ID, JSON Pointer và `expect.old`; dry-run trước khi apply.

## 4. Listening quality and reserve lifecycle

- **Part 1:** một ảnh, bốn câu mô tả, một đáp án; phân biệt photograph và SVG illustration; giữ attribution và fallback.
- **Part 2:** một prompt và ba phản hồi tự nhiên; chỉ một phản hồi tốt nhất.
- **Part 3:** hội thoại nhiều lượt, ít nhất hai speaker, ba câu liên kết.
- **Part 4:** một bài nói/thông báo có ba câu liên kết.
- Giải thích cần nêu dấu hiệu trong transcript và lý do; TTS là audio tổng hợp, không phải bản ghi ETS/native speaker.
- Unit chờ reviewer thứ hai phải có `editorialStatus: "reserve-pending-independent-review"`. Vẫn cho phép luyện Listening thông thường nhưng Mock sampler loại toàn unit, không cắt riêng một số câu của Part 3/4.
- Mock eligibility fail-closed: status-less legacy và trạng thái `internal-editorial-reviewed` đã tồn tại ở v2.33 được giữ tương thích; `approved-for-mock` được phép. Reserve và trạng thái chưa biết bị loại. Nội dung mới không được gắn `internal-editorial-reviewed` để lách vòng duyệt; sau reviewer thứ hai mới chuyển reserve sang `approved-for-mock`.
- Internal source/key/rationale check không thay thế independent review. Chỉ chuyển trạng thái sau khi reviewer ghi nhận transcript grounding, key, distractors, naturalness, tiếng Việt, stable IDs và quyết định cụ thể.

## 5. Reading quality and block integrity

- **Part 5:** một câu incomplete sentence, một blank, bốn lựa chọn song song; giải thích grammar/meaning cue.
- **Part 6:** text completion/cohesion/sentence insertion khi phù hợp; số blank marker phải khớp số câu. Mỗi text là block bốn câu và Mock sampler lấy nguyên block.
- **Part 7:** single, double, triple passages; câu hỏi detail, purpose, inference, reference, vocabulary và cross-document. Single passage giữ block 2–4 câu; double/triple giữ block 5 câu và đủ 2/3 tài liệu có label/content.
- Câu hỏi mới cần stable IDs, bốn lựa chọn phân biệt, key, rationale tiếng Việt, `evidence.sourceLabels` và `evidence.quotes` đúng văn bản. Append câu hỏi; không reorder hoặc thay index cũ.
- Evidence quote chứng minh khả năng truy vết, không tự chứng minh mọi distractor đều sai. Phân biệt internal editorial review với independent semantic review.
- Các bộ câu đã qua internal review có thể xuất hiện trong Mock luyện tập nội bộ; không mô tả đó là đề ETS, đề đã equate hoặc chứng nhận psychometric. Chỉ nâng trạng thái chất lượng khi có hồ sơ reviewer thứ hai.

## 6. Grammar Part 5/6

- Dùng một Grammar library và một Focus Workspace. `parts` là metadata lọc, không tạo runtime library riêng cho từng Part.
- Part 5 luyện sentence grammar, word form, tense, agreement, collocation, determiner, preposition và clause structure.
- Part 6 phải xét ngữ cảnh cả trước/sau blank; bổ sung cohesion, reference, transition và sentence insertion khi phù hợp.
- Không duplicate lesson/exercise. Giữ stable IDs và thứ tự bài đã có progress.
- Reference links chỉ hỗ trợ rule; ví dụ/câu hỏi là nội dung dự án tự biên soạn.

## 7. Retry, attempt history and learner progress

- Reading, Listening và Grammar dùng `answers` cho kết quả mới nhất và `attemptHistory` để giữ các lần trước.
- “Làm lại câu này” chỉ mở khóa một câu; “Làm lại toàn bộ bài” phải xác nhận và archive tất cả câu đã trả lời.
- Mỗi attempt giữ selected text/index, stable `choiceId`, key, correctness, explanation, timestamp và attempt number.
- Coverage đếm câu duy nhất; accuracy theo lần mới nhất; số lượt thử báo riêng.
- IndexedDB giữ `toeic-vocabulary-phase1`, version 1, store `workspace`; field bổ sung phải tương thích progress cũ. Không reset/import/export/inspect/migrate hồ sơ cá nhân trong release thông thường.

## 8. Shared learning UI

- Flashcard, Review, Grammar, Reading và Listening detail dùng shared Focus Workspace.
- Chỉ `.learning-focus-content` sở hữu cuộn dọc; content bên trong không tự tạo nested vertical scrolling.
- Nội dung ngắn co tự nhiên; nội dung dài cuộn một lần ở outer workspace.
- Thay đổi shared shell ở stylesheet/helper hiện có; không tạo backdrop, modal, CSS và logic cuộn riêng cho từng module.
- Giữ keyboard access, focus-visible, touch target khoảng 44px, mobile safe-area và `prefers-reduced-motion`.

## 9. Mock Exam integrity

- Giữ Quick 15m/25Q, Half 60m/100Q và Full 120m/200Q.
- Listening/Reading phải đủ blueprint cho mỗi form; Part 3/4, Part 6 và Part 7 resource blocks không được cắt.
- Không lấy item/unit có `reserve-pending-independent-review` hoặc editorial status không nhận diện vào Mock. Báo cáo số câu eligible và reserve tách riêng. Existing v2.33 `internal-editorial-reviewed` Reading units remain eligible for backward compatibility; this legacy exception does not authorize new content to skip second review.
- Dùng cả attempt history và lifetime-use ledger để ưu tiên câu chưa dùng; kiểm tra ID uniqueness trong từng form và độ giao nhau giữa các form liên tiếp.
- Không tuyên bố điểm ETS/CEFR hoặc tương đương psychometric nếu chưa có mô hình equating/validation.

## 10. Content lifecycle and release gates

`Draft → source check → internal editorial review → schema validation → evidence/distractor audit → patch dry-run → apply → content QA → coverage report → version sync → unit tests → ZIP integrity → clean overlay reconstruction → Master/Changelog update`.

Required core commands:

```bash
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/audit-toeic-coverage.py
python tools/audit-question-evidence.py
python tools/audit-distractors.py
python tools/sync-version.py --check
node --check assets/js/app.js
node --check assets/js/mock-engine.js
node --check sw.js
```

Chạy unit tests theo module phù hợp thay vì dựa vào một lệnh discovery dài có thể timeout. Báo cáo phải ghi đúng số suite/test thực tế và phân biệt structural PASS với semantic review.

## 11. Coverage and documentation lifecycle

- `docs/MASTER_STATUS.md`: trạng thái, số liệu, blockers và next action duy nhất.
- `docs/CHANGELOG.md`: chronological release log duy nhất.
- `docs/COMPATIBILITY.md`: storage/data/cache/support contract.
- `docs/DESIGN_SYSTEM.md`: layout và interaction dùng chung.
- `docs/CONTENT_OPERATIONS.md`: quy trình này.
- `docs/batches/` và `docs/reports/`: chỉ giữ file chi tiết của previous + current release.
- `docs/archive/PROJECT_HISTORY.md`: mô tả ngắn tài liệu đã nghỉ hưu; không chép lại toàn văn báo cáo cũ.
- Nguồn và editorial method ghi trong batch hiện tại; không tạo một source `.md` riêng cho mỗi nhóm.

Khi xuất bản phiên bản mới: current thành previous; previous cũ được tóm tắt vào Project History rồi nghỉ hưu. Chạy `python tools/rotate-release-files.py` trước, rà danh sách, rồi mới chạy `--apply`. Rotator không được đụng app source, canonical JSON, assets, PWA shell, patches hoặc learner profiles.


## 12. CI coverage and development-to-acceptance sequencing

- Every `tools/tests/test_*.py` module and every `tools/tests/*.mjs` suite must be called by `.github/workflows/validate-data.yml`. `test_ci_coverage.py` checks that relationship; include it in CI whenever the test inventory changes.
- A suite being listed in the workflow is not the same as a remote workflow run passing. Keep local test evidence and remote Actions evidence separate.
- During active development, prioritize fixes to demonstrated failure modes and high-risk flows. Do not issue a broad acceptance checklist or reminder while core development work is still open.
- After the development backlog is closed, create one risk-weighted acceptance/test plan focused on mock assembly and section boundaries, saved attempts/Retry history, IndexedDB continuity, PWA cache/offline/reconnect, responsive layout and real device/browser voice behavior. Avoid repeating a 100% manual sweep of stable areas unless a changed component puts them at risk.


## 13. Author-pass refinements to reserve Listening content

- An internal author pass may correct demonstrable answer-response, transcript or evidence-pointer issues before an independent reviewer sees the material.
- Keep reserve status unchanged after an author pass. A correction is not a second-person approval, and neither evidence-text matching nor automated regression checks can promote an item into Mock.
- When a corrected option is only clarified, preserve its existing `choiceId` and index so saved selections remain linked to the same answer concept. If the option meaning or identity changes, create a new choice ID and record an explicit migration path rather than silently reusing the old identity.
- For an answer with multiple supporting transcript details, evidence text should point to the complete supporting phrase or the question should be narrowed so the key does not claim more than the cited source.

## 14. TOEIC Part 5 Sentence Completion practice bank

- Canonical file: `data/practice/part5-sentence-completion.json`. This is a separate adaptive practice bank, not a duplicate of `data/readings/reading-library.json` Part 5 and not part of the Mock Exam pool.
- Every item has exactly one `_____` gap, four unique A–D choices, one `answerIndex`, four aligned `optionExplanations`, a canonical `wordId`, a supported `grammarCategory`, `grammarPoint`, full explanation, Vietnamese translation and a reason why the intended answer is uniquely best.
- Allowed grammar categories are the 14 named in `data/practice/part5-sentence-completion.json`; each question must be represented in the generated coverage report. Batch 016 uses `editorialBatch="016"` and `contentBatch="batch-016-part5-grammar-expansion"`.
- Keep answer-key positions balanced across A/B/C/D over the complete authored bank, and preserve choice/explanation identity whenever an answer index is rebalanced.
- The key must satisfy grammar, part of speech, agreement/tense/verb pattern and sentence meaning. Distractors should be plausible but demonstrably wrong in the actual sentence; avoid prompts where two choices become valid under different unstated assumptions.
- Prefer familiar TOEIC contexts (office administration, HR/recruitment, finance, purchasing, customer service, shipping/logistics, travel and facilities). Keep vocabulary IDs stable; do not add a duplicate headword just to support a practice item.
- The UI shuffles choices, so answer-specific explanations must be shuffled in lockstep. Tests must assert that the keyed explanation remains attached to the correct choice after randomization.
- The Part 5 seen-question list uses question IDs and is stored as optional `sentenceCompletionSeenIds` inside the existing `practiceSession` record. Do not reuse `sessionSeenIds` from other modes. Correct/incorrect outcomes still update the linked vocabulary word's existing `studyProgress` entry.
- The complete 80-question bank remains `reserve-pending-independent-review` and practice-only until a second reviewer checks grammar, naturalness, semantic uniqueness, key and all distractors. Internal author review and automated validation are not independent approval. Automated schema/selector tests and an internal author pass are not independent approval and never add these records to Mock.
- Include the bank JSON and selector module in Service Worker `REQUIRED` and `APP_SHELL`; keep the DB at `toeic-vocabulary-phase1` version 1 unless a separately justified storage migration is approved.

