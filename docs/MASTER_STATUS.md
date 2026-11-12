# TOEIC DICTIONARY — PROJECT MASTER

> **Tài liệu chuẩn duy nhất về trạng thái, phạm vi và lộ trình phát triển.** Mọi cập nhật tiến độ tiếp theo phải sửa trực tiếp file này; không tạo thêm roadmap/master trùng lặp.

- **Phiên bản mã nguồn đang kiểm kê:** v2.27.0 (focused learning workspace, responsive practice flows & Vocabulary Batch 017; local release candidate)
- **GitHub / CI:** người dùng cung cấp Actions run `42981524564`, job `130392820806`, `validate (push)` thất bại sau 13 giây với annotation chung `Process completed with exit code 1`. Nếu run dùng đúng workflow V2.20.0 thì step #14 là `Unit tests — choice_history`; step này local PASS 5/5. `python tools/validate-data.py` local PASS 0 lỗi/0 cảnh báo. Remote commit SHA, workflow revision và log lỗi gốc vẫn chưa được đọc; không được kết luận root cause hoặc Pages deploy. GitHub connector chưa được kết nối.
- **Ngày kiểm kê:** 12/11/2026
- **Nền tảng:** GitHub Pages + PWA; không cần backend/Cloudflare.
- **Repository đích:** `vuphuc1996/Toeic`; nội dung ứng dụng nằm trực tiếp ở root repository.
- **Gói bàn giao hiện tại:** V2.27.0 update overlay patch trên nền Full Source V2.26.0; dùng chung focus workspace cho Flashcard/Ôn tập và focus modal đồng bộ cho Grammar/Listening/Reading; bổ sung 43 vocabulary headwords, tổng 971. Flashcard lật thẻ ở lần chạm đầu và chuyển từ ở lần chạm kế tiếp; Review có dashboard, 8 dạng bài và nút bắt đầu. Layout dựa trên viewport/safe-area, nội dung cuộn trong khung thay vì đẩy page. Không thay schema IndexedDB hoặc thao tác hồ sơ cá nhân. Snapshot vẫn không có byte 8 JPG Part 1; phải giữ ảnh đã có trên GitHub khi áp dụng patch. GitHub Actions/Pages và QA thiết bị thật chưa được xác minh.


> **QUYẾT ĐỊNH PHẠM VI MỚI — 09/11/2026 (ưu tiên cao nhất): TOEIC FIRST, IELTS DEFERRED.**
> Tất cả công việc phát triển mới chỉ phục vụ TOEIC Listening & Reading (7 Parts). Không tạo thêm IELTS vocabulary, IELTS lessons, IELTS filters, IELTS prompts hoặc IELTS roadmap tasks cho đến khi các cổng nghiệm thu TOEIC tại Mục 1A đều đạt và người dùng xác nhận chuyển giai đoạn. Các đoạn lịch sử nói về English Master/IELTS ở dưới được giữ để truy vết, không còn là chỉ thị triển khai hiện hành.

## Historical content/platform baseline — v2.15.1 (superseded by current code v2.27.0)

- **Code version:** v2.15.1 (v2.15.0 content baseline + Reading/Grammar runtime fixes and CI runner maintenance; release candidate, not deployed).
- **Baseline:** v2.14.0; 928 stable vocabulary IDs; 26 A–Z files; 32 topics; static GitHub Pages + PWA; personal vocabulary and progress remain local in IndexedDB/LocalStorage.
- **Vocabulary:** 928 headwords; US IPA=580/928 (62.5%); word-family=131/928 (14.1%); verb_forms=291; collocations=758; synonyms=361; antonyms=213. All 31 JSON files under `data/vocabulary/` are byte-identical to v2.14.0 in this release.
- **Listening:** 56 units / 102 questions. P1=8, P2=25, P3=13 sets/39 Q, P4=10 talks/30 Q. Part 1 uses SVG illustrations, not photographs. Audio uses browser SpeechSynthesis, not recorded/ETS audio. All 23 old generic Part 2 translation placeholders were replaced with Vietnamese translations of the actual spoken line; the supplier-samples prompt was standardized and one negative-tag response clarified.
- **Reading:** 35 resources / 109 questions. P5=30, P6=16, P7=63 (38 single-passage, 25 double/triple). Every multi-document set keeps separately labeled/content-bearing `documents[]`.
- **One-form pool gate:** 102 Listening +109 Reading đã tạo được form đầy đủ 200 câu theo blueprint (P7 chọn 29 single +25 multiple). V2.25.0 đã triển khai Mock Beta; hiện đây là một blueprint 200 câu, chưa đủ dữ liệu cho nhiều Full Test không trùng nhau. Cần ưu tiên mở rộng ngân hàng trước khi cam kết không lặp giữa các đề Full. 11 câu Listening Batch 013 reserve chưa được đưa vào thi thử vì còn chờ duyệt độc lập; điểm hiển thị là số câu đúng/tỷ lệ, không phải điểm ETS-equated.
- **Grammar:** 25 lessons / 54 exercises.
- **Editorial evidence + distractor audit:** all 211 questions remain source-mapped. The 132 Part 3/4/7 questions (126 direct/lexical mappings + 6 inference/paraphrase items) have now had their keyed answer and all distractors manually reviewed against the transcript/passage. Twelve weak option groups were improved; question IDs, question order, correct answer text and `answerIndex` remain unchanged. The 12 revised questions carry `legacyChoices` snapshots so old `choiceIndex` history can still display the original distractor text; new attempts store additive `choiceText`. No IndexedDB object-store/schema migration or progress reset was made. P1=8 visual/key, P2=25 response-fit, P5=30 grammar and P6=16 context/cohesion checks remain recorded from v2.14. Internal review is not independent expert/psychometric/ETS approval. See `docs/reports/TOEIC_REMAINING_CONTENT_SECOND_PASS_v2.19.0.md`, `docs/reports/TOEIC_DISTRACTOR_AUDIT_v2.19.0.md` and `docs/reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.19.0.md`.
- **Shared design system:** `assets/css/design-system.css`, loaded after `app.css` and pre-cached by the service worker. System font stack, body 15–16 px, regular helper 12–14 px, eyebrow 11 px, 44 px primary/touch controls, 44 × 44 px alphabet/icon actions on coarse pointers, 18–22 px icons, visible keyboard focus; phone 320–640 px, compact tablet 641–850 px, tablet/compact laptop 851–1199 px, laptop/desktop ≥1200 px. iOS safe-area, `100svh`/`100dvh`, 16 px mobile input text, tablet icon rail (no phone bottom nav), reduced-motion and high-contrast preferences included.
- **Effects policy:** modest page/modal entry, button press/hover feedback only on fine pointers, card shadow/border feedback and actual progress-fill transitions; existing toast entry stays brief. No looping decorative animation; `prefers-reduced-motion` turns off non-essential movement. Hover is never required for touch users.
- **Content operations:** guarded patching, vocabulary and learning validators, content coverage, answer-to-source traceability, distractor audit, version sync, unit tests and GitHub Actions are release gates. See `docs/DESIGN_SYSTEM.md`, `docs/reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.19.0.md`, `docs/reports/TOEIC_DISTRACTOR_AUDIT_v2.19.0.md`, `docs/reports/TOEIC_REMAINING_CONTENT_SECOND_PASS_v2.19.0.md` and `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.19.0.md`.
- **Static shell checks:** 206 HTML IDs are unique; 74/74 APP_SHELL paths exist; all 52 Markdown files are located under `docs/` and none are at repository root.
- **Unit tests:** 129/129 PASS (126 baseline v2.15.0 methods + 3 Reading/Grammar runtime regression methods). Slow subprocess-based suites were accounted for individually when grouped sandbox execution timed out; no combined discovery PASS is claimed. Runtime render smoke via Node VM: PASS for Reading P5, Reading P7 multi-document and Grammar. Slow tests are run by module/group where needed to avoid Python 3.13 sandbox timeouts; no monolithic-discovery PASS is claimed.
- **ZIP QA:** v2.15.1 ZIP contains 169 files; `testzip()` CRC PASS; clean extraction exact comparison 169/169; 31/31 `data/vocabulary/*.json` files match v2.15.0 byte-for-byte. SHA-256 is stored in a sidecar outside the archive.
- **CI configuration:** action references are now checkout/setup-python/setup-node v7 with Node 24 and a pinned Ubuntu 24.04 runner; remote workflow execution after this change is pending.
- **QA boundary:** automated CSS/HTML/static checks can verify tokens, breakpoints, PWA precache and source links. Local Chromium navigation was blocked by the sandbox (`ERR_BLOCKED_BY_ADMINISTRATOR`); no browser interaction/screenshot or physical device QA is claimed. Remote GitHub Actions, GitHub Pages deploy and iPhone/iPad/Android/PC physical browser verification are pending.

### Competitive position — summary

The app's current differentiators are an owner-controlled, static GitHub Pages PWA; local/offline study data; source-traceable JSON updates; a single documented baseline; editable local TTS voice settings; and a clear content QA pipeline. Its current disadvantages versus specialist TOEIC products are much smaller content volume, no complete 100+100 question timed mock test, no official ETS audio/question bank, no psychometrically equated score, and no server-synced multi-device progress or AI tutor. See `docs/reports/TOEIC_APP_BENCHMARK_2026.md` for the sourced comparison.

## 1A. TOEIC acceptance gates — IELTS remains blocked until all pass

1. **Exam blueprint:** all 7 Parts have an explicit item-type schema and official-format target distribution: Listening P1=6, P2=25, P3=39, P4=30; Reading P5=30, P6=16, P7=54 (29 single-passage +25 multiple-passage). Total 200 questions; 45-minute Listening and 75-minute Reading practice timing. The IIBC reference describes approximately two hours and 200 questions. The official score scale is not to be imitated without validation.
2. **Content volume:** first-form minimum is now met in v2.12.0 (102 Listening / 109 Reading; includes the Part 7 split of at least 29 single-passage + 25 multiple-passage questions). This is only a pool-size gate, not approval to release a mock: finish semantic/editorial review, mock-engine QA and at least one complete 200-question form. Further work should add reserve content for repeatable/non-repeating forms.
3. **Listening quality:** all Parts 1–4; image/P1 material must be photo-realistic or explicitly labeled illustrative; Part 2 concise natural responses; Part 3 multi-speaker conversations; Part 4 short talks; transcripts, Vietnamese explanations, accent variety and playback review. TTS must not be described as recorded native-speaker/ETS audio.
4. **Reading quality:** Part 5 sentence completion; Part 6 text completion including sentence insertion where appropriate; Part 7 single/double/triple passages with linked questions and cross-document reasoning. Every item must have a unique answer key and reviewed rationale.
5. **Vocabulary quality:** target 3,000–5,000 TOEIC-priority headwords/lemmas as an internal planning target, not an ETS official list. Preserve IDs; attach sense-level meaning, POS, example + translation, topics, evidence/known source, review status; add IPA/family/relations only when verified. No forced completion of inapplicable fields.
6. **Grammar & strategy:** maintain a TOEIC grammar coverage matrix; map grammar topics into P5/P6 error patterns; avoid duplicate lessons and generic distractors.
7. **Practice and analytics:** review wrong answers, spaced repetition, bookmarks, adaptive part recommendations, per-Part accuracy and history; export/import remains local and testable.
8. **Mock engine:** timer, question navigation, flags, section boundaries, submission, answer review, analysis by Part and clear practice-only score estimation. Never label local estimates as an official ETS score.
9. **Release/QA:** validators, patch dry-run, tests, offline app-shell validation, desktop/tablet/iPhone/Android QA and export/import QA. Do not call Phase 5 complete until physical-device QA is recorded.
10. **Gate to IELTS:** all items above pass, at least one full 200-question mock is complete and reviewed, and user explicitly approves shifting scope. Until then IELTS remains deferred.

## 1B. Retained implementation baseline — v2.23.0 (cumulative updates recorded through v2.27.0)

- **Stable choice identity:** all Reading questions (109), Listening questions (113) and Grammar exercises (54) retain stable `choiceIds`; each identity moves with its option. Duplicate option text continues to use distinct IDs. The 11 new reserve questions also carry unique choice IDs.
- **Audited answer-position balance:** exactly 27 questions were adjusted by swapping only the keyed option with one distractor: Part 3 = 8, Part 4 = 5, Part 7 = 14. New distributions are P3 A10/B10/C10/D9; P4 A8/B8/C7/D7; P7 A16/B16/C16/D15. Question IDs/order, passages/transcripts, explanations, all option text and keyed-answer text remain unchanged; only option position and `answerIndex` change.
- **v2.16 baseline snapshots:** each changed question includes `previousChoices`, `previousChoiceIds`, `previousAnswerIndex` and `choiceOrderRevision: "2.17.0"`. Exact old/new positions and answer text are recorded in `tools/answer-position-balance-v2.17.0.json` and `docs/batches/TOEIC_ANSWER_POSITION_BALANCE_BATCH_007_v2.17.0.md`. No random shuffling.
- **Progress migration hardening:** v2.16 progress with `choiceId` resolves the current index by identity and preserves the prior numeric position in `previousChoiceIndex`. Profiles without an ID use the saved v2.16 option snapshot on changed questions. Legacy distractors from the 12 v2.15 revisions retain separate archived IDs. Ambiguous stored text and invalid indices are not guessed/overwritten; the migration is idempotent across consecutive app starts.
- **History rendering:** wrong-answer highlighting resolves stable `choiceId` first, avoiding a stale-index highlight after reordering. Archived historical options remain displayed as archived rather than being misrepresented as a current option.
- **No schema reset:** IndexedDB remains database `toeic-vocabulary-phase1`, version 1, store `workspace`; no object-store/database-version change, progress reset or personal data deletion. Vocabulary remains 928 records, 928 stable IDs and 26 A–Z files. Listening 113, Reading 109 and Grammar 25 lessons /54 exercises are unchanged.
- **Current Listening inventory:** 63 units / 113 questions (P1=8, P2=30, P3=42, P4=33). The first-form selection remains 6/25/39/30; 13 Listening questions are additional practice/reserve beyond the 100-question Listening blueprint. Reading remains 109 and Grammar 54.
- **Part 1 media:** 8 Pexels photo paths plus source/license attribution are implemented. JPG is an OPTIONAL Service Worker cache asset and SVG is REQUIRED fallback. Missing OPTIONAL assets no longer fail the general structural validator; the strict `validate-part1-photo-assets.py` CI step still requires eight valid local JPEGs (1280×960 minimum). The current working copy has 0/8 JPG bytes, so the strict photo gate and image-level/offline photo QA remain pending. Do not replace missing photos with placeholders.
- **Reserve content — Batch 013:** Part 2 +5, Part 3 +3 and Part 4 +3 questions. These 11 original-authored items are marked `reserve-pending-independent-review`; they pass structure/key/choice-ID checks but are excluded from the historic answer-position/distractor certificate until independent review. The existing 132 reviewed Part 3/4/7 questions retain their certified distributions.
- **Listening/TTS playback — Batch 014 / v2.24.0:** manual male/female voice preferences, Daniel fallback, speaker mapping, rate and configured pauses are retained. `activeSpeechCancel` now settles the app-owned playback promise before browser cancellation, so a missing browser cancel callback cannot stall sequential dialogue/vocabulary playback. Expected canceled/interrupted preview events no longer show a false voice error. A deterministic mocked-SpeechSynthesis regression is registered in CI; it does not replace acoustic QA on actual devices.
- **Historical review registry:** 148 v2.19 reviewed questions are protected by per-question SHA-256 fingerprints plus per-unit content fingerprints for transcripts, segments, translations and source metadata, not one whole-file Listening hash. Five declared Part 1 wording alignments are allow-listed; unapproved changes to historical question or unit content remain test failures. Any new question outside the 148-item registry must be explicitly marked reserve-pending-independent-review. This fixes the known stale whole-file baseline collision caused by intentional Part 1 editorial updates and additive reserve questions.
- **Optional cache semantics:** `validate-data.py` still errors for missing `APP_SHELL`/required resources, but missing entries in `OPTIONAL` are permitted. Strict photo validation is a separate CI gate, so missing Part 1 JPGs cannot silently pass release validation.
- **V2.23.0 local test gate:** 177/177 unit-test methods PASS across 17 test modules (36 validator methods accounted for in isolated chunks). Vocabulary validator: 0 errors / 0 legacy warnings; learning validator: 0 errors and 8 warnings solely because JPG binary files are absent from this snapshot. Strict photo validation: not PASS (0/8 actual JPG bytes available); `--allow-missing` diagnostic passes with 8 explicit warnings. Version sync, coverage/evidence/distractor audits, Python/JavaScript syntax and runtime smoke PASS. Full-source ZIP (227 files) and overlay patch (39 files) both pass CRC and clean-extraction byte comparison. The archives intentionally omit the 8 absent JPG binaries; apply the overlay while preserving the JPGs already in the target repository. Remote CI/Pages and physical-device QA remain pending.
- **Runtime/CI gate:** 147/147 test methods PASS in the v2.18.0 run; the 33 validator methods were executed individually after grouped execution hit the sandbox time limit. Migration smoke covers Reading, Listening and Grammar, profiles with and without `choiceId`, archived legacy choices, stale-index rendering, preservation of correctness/time/text, ambiguous-data preservation and idempotency. Workflow has a separate `answer_position_balance` step. The slower validator/version-sync suites were accounted for by isolated method runs after grouped discovery timed out in the sandbox.
- **Sidebar / viewport-height correction:** on desktop layouts (`min-width: 851px`), the sidebar is constrained to `100dvh`; its navigation area has `min-height: 0` and independent vertical scrolling, while `.sidebar-bottom` is non-shrinking and pinned at the bottom. At heights up to 820 CSS px, vertical padding and nav row spacing are compacted; a tighter mode applies at 680 px. The local-data card and version text are not hidden in this desktop range. Automated CSS regression checks pass; a real 100% zoom browser check is still pending.
- **Part 7 second-pass review:** all 63 questions across 24 Part 7 sets were rechecked internally against their source documents, chronology, key uniqueness, distractor fit and explanation. Two source inconsistencies/ambiguities were corrected: hotel stay nights/departure dates and course completion relative to the reimbursement effective date. No answer key, choice ID, question ID, choice text, order or question count changed. Two legacy multi-document sets with only one question (one double, one triple) are flagged for richer cross-document coverage in a reserve-content batch. This is an internal model second pass, not external two-person signoff.
- **Personal IndexedDB profile test — deferred by user request:** for now use the app's default local profile; do not run personal-data import/export or migration tests. Revisit only when requested. No personal data was imported, inspected or reset in this batch.
- **v2.19.0 internal second pass:** the remaining 148 questions outside Part 7 were reviewed in Batch 009; with the 63 Part 7 items from v2.18.0, second-pass coverage spans all 211 Listening/Reading questions. No question/answer/choice content changed in Batch 009. See the report and machine-readable review registry.
- **v2.19.0 test gate:** 152/152 test methods PASS: 107 fast/feature/review methods (including five new review-registry guards), 12 version-sync methods and 33 validator methods. The grouped validator run exceeded the sandbox time; all 33 methods returned PASS when isolated in two batches. Local validators: 0 errors/12 known legacy vocabulary warnings; learning validator 0 errors/0 warnings.
- **v2.20.0 current gate (historical):** 164/164 test methods PASS; vocabulary validator 0 errors/8 known legacy FD001 warnings; learning validator 0 errors/0 warnings. See `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.20.0.md`.
- **v2.21.0 Batch 011 gate:** 7 guarded collocation replacements resolve all 8 FD001 legacy entries; baseline tightened by removing exactly 8 resolved entries and adding none. Final vocabulary validator 0 errors/0 warnings; learning validator 0 errors/0 warnings; version sync PASS; Python/JavaScript syntax and runtime smoke PASS. Targeted unit tests: 54/54 methods PASS across baseline IDs 13/13, patch data 11/11, sync version 12/12, choice history 5/5, vocabulary detail/examples 10/10 and new collocation regression 3/3. The complete validator unit module stalled in grouped sandbox execution; a total release-wide unit-test count is not claimed for v2.21.0. See `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.21.0.md`.
- **v2.22.0 Part 1 photograph integration (historical):** eight item records now define `photo` JPG plus existing SVG `image` fallback; `visualType` is photograph. Three correct statements B/C/D are aligned to their corresponding photos while answerIndex and choiceIds remain unchanged. JPG paths are OPTIONAL Service Worker assets; SVG fallbacks remain REQUIRED. `assets/listening/ATTRIBUTION.csv` records photographers, source URLs and Pexels license URL. Current local copy does not include JPG binaries, so exact remote file existence, actual pixels and offline photo display remain unverified.
- **v2.22.0 local integration checks (historical):** JavaScript/Python syntax, version sync, Part 1 photo/fallback rendering tests and answer-to-source audit pass; targeted learning/evidence regression tests 32/32 PASS. Learning validator reports 0 errors and 8 warnings because the eight JPG binaries were not in this local snapshot; all eight SVG fallbacks are present. The user reports the JPGs have been uploaded to the GitHub repository, but their remote bytes could not be read in this session; `validate-data.py` APP_SHELL/cache existence and offline JPG verification must be rerun on the full repository after patch application.
- **Remote CI / production boundary:** the user-reported run `42981524564` is FAIL. The local v2.20 workflow’s 14th declared step is `choice_history`, which passes locally 5/5; the remote log/commit/workflow revision remain unavailable. The remote failure is not yet diagnosed or fixed. V2.23 separately fixes known stale whole-file review-baseline and reserve-scope test defects in the current source line, but these local repairs are not confirmed as the cause of that earlier remote run. A failed check does not revert the push or mutate app data; merge/deploy blocking depends on branch protection/deployment dependencies. GitHub Pages status is unverified. Real browser navigation remains blocked in this sandbox (`ERR_BLOCKED_BY_ADMINISTRATOR`); physical-device QA is pending.

## 1C. Next TOEIC-only development priorities after v2.27.0

1. **Expand TOEIC vocabulary first.** Preserve all 928 original baseline IDs plus the 43 Batch 017 additions (971 current headwords) and existing personal word/progress data. Continue source-based batches toward the internal 3,000–5,000 headword target; prioritize practical workplace/business topics, sense-level examples, US IPA and collocation quality. Never invent IPA, CEFR, word families or lexical relations.
2. **Expand and strengthen Grammar.** Keep the existing Grammar module and question identity stable; add structured lessons/exercises with answer rationale and progressive difficulty. Avoid large redesigns while data is still being expanded.
3. **Add relevant decorative/study images.** Provide the user direct download links and an explicit approved filename plus destination folder for every asset (for example, under `assets/topics/` or a dedicated `assets/grammar/`/`assets/reading/` folder). Do not depend on decorative assets for core app startup; preserve the eight Part 1 JPGs and their SVG fallbacks.
4. **Extend Listening reserve.** First obtain independent review for all 11 Batch 013 reserve questions, then add new non-duplicate content by Part. Build enough extra Part 2/3/4 sets to create several distinct mock forms and avoid repeating the same Part 3/4 units. Add more P7 double/triple passages when the Reading phase resumes.
5. **Compare the app with current TOEIC learning platforms.** Research current, publicly available features, study paths, test engines, mock score reports, AI, audio, content scale, pricing and offline/data practices. Cite official product pages/recent sources and clearly distinguish observed features from estimates. Do this after the content priorities above, as requested.
6. **Mock Beta regression and real-device QA.** Verify 15/60/120-minute timers, answer navigation/flags, automatic Listening→Reading transition, refresh/resume, submissions, score/report review and PWA offline behavior. Check laptop at 100% zoom, tablet, iPhone Safari and Android Chrome. The current sandbox cannot establish physical audio/viewport signoff.
7. **Editorial and scoring boundary.** Internal second-pass coverage (211/211) is not independent expert or psychometric signoff. Mock reports show raw counts/accuracy and a 75% internal practice target; do not generate ETS 10–990 or CEFR claims without a trustworthy conversion/equating dataset and explicit labeling.
8. **Remote release verification.** Confirm GitHub Actions, Pages deployment/base path, service-worker update/offline behavior and strict Part 1 photo validation after the user applies the patch. The current local snapshot still lacks JPG bytes; remote images have not been read in this session.
9. **Personal IndexedDB profile QA (deferred).** Do not import/export/inspect/reset/migrate personal data unless the user explicitly requests it. Keep the IndexedDB schema and existing learning progress unchanged.

The next content sequence is explicitly: Vocabulary → Grammar → downloadable decorative image assets → reviewed Listening reserve → current TOEIC platform benchmark. IELTS remains excluded from data, lessons, filters and active roadmap until every TOEIC acceptance gate passes and the user explicitly approves the transition.

### v2.27.0 delivery record — Focus learning workspace & Vocabulary Batch 017

- **Flashcard topic selection:** the Flashcard page continues to show the topic selector/dashboard. Choosing a topic moves `#flashSession`, `#flashQuiz` and `#flashResult` into one fixed focus workspace; the rest of the application is dimmed/blurred. The first click/keyboard activation flips the card to meaning, definition, example, collocations and word relations; the next click advances to the next word. The close × restores the topic-selection view.
- **Vocabulary check after learning:** the quiz stage remains inside the same focus workspace, using the same bounded frame and close control. It does not expand or push the page layout.
- **Review dashboard:** shows reviewed count, accuracy, due/weak vocabulary and mastered count; eight review modes are selectable before starting. The quiz panel is hidden on the dashboard and moved into the focus workspace only after Start; closing restores the dashboard.
- **Grammar, Listening and Reading detail:** these flows now use the shared centered/dimmed focus-modal presentation. Internal content scrolls within a max-height container; mobile uses bottom-sheet/safe-area spacing, wider screens use a centered dialog; reduced-motion preference is honored.
- **Vocabulary Batch 017:** added 43 TOEIC-focused words to canonical A–Z files and provenance batch file `data/vocabulary/batch-006.json`; canonical headword total rises from 928 to 971. CEFR values are editorial estimates and these records remain pending editorial verification. Existing IDs are unchanged.
- **Profile safety:** IndexedDB remains `toeic-vocabulary-phase1`, version 1, store `workspace`. No personal profile import/export/inspection/reset/migration or schema change was performed. TTS and question banks are unchanged.
- **Tests:** added `tools/tests/learning-focus-workspace.mjs`; CI invokes it. It checks unique HTML IDs, flash flip/advance, topic close/return, Review modes/dashboard/start/close, common Grammar/Listening/Reading focus styling, responsive layout contracts and unchanged IndexedDB v1.
- **QA boundary:** automated/static checks can verify source contracts and viewport CSS. Physical-device interaction and remote GitHub Actions/Pages are not verified. Local snapshot is still missing the eight JPG Part 1 binaries, so strict photo validation remains pending.
- **Package QA:** Update Overlay contains 35 entries (27 changed +8 added, no deletions), Full Source contains 256 files; both passed ZIP CRC, clean extraction and byte-for-byte comparison. SHA-256 sidecars accompany both packages.

### v2.26.0 delivery record — Flashcard image relevance & responsive layout

- Individual vocabulary flashcards no longer inherit an image from the first topic tag. Default is a clean text-first card; this removes mismatched generic illustrations across the existing vocabulary bank.
- Future word-specific images render only when all metadata is explicit and approved: `image` path under `./assets/vocabulary/`, descriptive `imageAlt`, and `imageStatus: "approved"`. Topic thumbnails remain on topic-selection cards and are not reused as word images.
- Approved image frame uses responsive 4:3 aspect ratio with `object-fit: contain`; very narrow phones use a compact square frame. Text-only cards expand to the available width and remove the old fixed-height image column. CSS is viewport-based, not device-inch-specific, so it adapts to actual available screen width across phone sizes.
- No image assets were added in this batch. No vocabulary content/IDs, Mock Test questions, Grammar, Listening, Reading, TTS, or IndexedDB schema/personal profile were changed.
- Test: `node tools/tests/flashcard-image-policy.mjs`; JS syntax, validators, runtime smoke and version sync are recorded in the v2.26.0 test report.

### v2.25.0 delivery record — Full TOEIC Mock Practice Beta (Batch 015)

- Added `assets/js/mock-engine.js` and the `page-mock` workspace. The three modes are: quick 15 minutes (25Q: 12 Listening/13 Reading; 05:22/09:38), half test 60 minutes (100Q: 50/50; 22:30/37:30) and full test 120 minutes (200Q: 100/100; 45:00/75:00).
- Uses only the internally reviewed historical question pool: 102 Listening questions and 109 Reading questions. The 11 additional Listening Batch 013 reserve questions marked `reserve-pending-independent-review` are excluded until independent review. The full blueprint uses Listening P1–P4=6/25/39/30; Reading P5–P7=30/16/54, with P7 split 29 single +25 multiple-passage questions.
- Sampling is data-driven and random while preserving entire Part 3/4 audio blocks (3 questions), Part 6 text blocks (4 questions), and Part 7 document blocks. IDs are checked for uniqueness within every generated test. A lifetime LocalStorage usage ledger prioritizes never-used questions even after attempts roll out of the 60-row history list. Because the reviewed pool only supports one full blueprint in several Parts, a subsequent Full Test must reuse questions; the report shows the exact reused count.
- UI includes section countdowns, map navigation, answer selection, flagging, automatic transition from Listening to Reading, manual/automatic submission, answer key/rationale, post-submit Listening transcript and Reading passage review, Part-level accuracy and improvement tips. Part 1 prefers JPG and falls back to its corresponding SVG.
- Active test, up to 60 visible attempt histories, latest detailed result and a persistent lifetime question-usage ledger are stored in dedicated `toeic:mock-*` LocalStorage keys. The usage ledger does not reset when old attempt rows roll out of the 60-row history. No `dbSet`/IndexedDB interaction was added; no database version, object store, personal vocabulary, study progress or existing TTS configuration was modified.
- Score report: visual separate Listening/Reading score rings, raw correct count, accuracy, blank count, per-Part breakdown and gap to the internal 75% target. No ETS 5–495/10–990 or CEFR conversion is generated. ETS score conversion requires form equating/calibration beyond the current local content bank.
- Tests: `mock-exam-engine.mjs` (including lifetime rotation), `mock-ui-integrity.mjs`, `runtime-render-smoke.mjs`, `listening-tts-regression.mjs`, JavaScript syntax and static HTML ID uniqueness checks. Physical device/browser, remote GitHub Actions, Pages and 8 JPG bytes remain pending.
- User-requested next content sequence after Mock Beta: vocabulary expansion → Grammar expansion → downloadable decorative image assets with explicit filenames/folders → reviewed Listening reserve expansion → current TOEIC study-platform comparison. Personal IndexedDB import/export remains deferred.

### v2.24.0 delivery record — Listening/TTS playback reliability hardening

- Added app-owned active-speech cancellation so sequential TTS playback resolves deterministically even when a browser speech engine does not emit a cancellation callback. Expected canceled/interrupted preview events are suppressed; genuine synthesis errors remain visible.
- Registered `tools/tests/listening-tts-regression.mjs` in GitHub Actions. Local deterministic regression covers manual voice priority, Daniel en-GB fallback, stable speaker mapping, per-item rate, configured turn/word pauses and cancellation behavior.
- No changes to Listening content, question/choice identity, transcripts, default voice/pause configuration, audio provider or asset. No vocabulary/Reading/Grammar data or IndexedDB schema/profile changed. Personal profile import/export/inspection/reset/migration remains deferred.
- This is playback orchestration QA only, not a claim that male voice quality, accent naturalness or sound clarity has passed physical-device listening. Windows/iPhone/Android audio QA remains pending.
- Part 1 JPG availability remains 0/8 in the local snapshot; strict photo validation, remote Actions/Pages, previous remote CI run diagnosis and external TOEIC editorial review remain unresolved.
- See `docs/batches/TOEIC_TTS_PLAYBACK_HARDENING_BATCH_014_v2.24.0.md` and `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.24.0.md`.

### v2.23.0 delivery record — Part 1 photo QA hardening, CI baseline & reserve Listening content

- Part 1 remains eight questions. Photo IDs and source attribution are listed in `assets/listening/ATTRIBUTION.csv`; JPG path is preferred, existing SVG fallback remains on load failure. Photo files are OPTIONAL for PWA cache availability but REQUIRED by the release validator; this avoids blocking startup while preventing an incomplete photo release from passing CI.
- Editorially aligned statements for warehouse and technician images; updated three earlier V2.22 descriptions remain recorded. For all eight Part 1 items answer positions remain A/B/C/D = 0/1/2/3 twice; no question IDs, answer indexes or choice IDs changed.
- New reserve content: Part 2 +5, Part 3 +3, Part 4 +3 questions. Pool: P1=8, P2=30, P3=42, P4=33; Listening total=113. A first blueprint-compliant form still selects 6/25/39/30; 13 Listening questions are reserve beyond the first-form target.
- Historical v2.19.0 reviewed-question registry now uses per-question fingerprints so additive content does not invalidate the 148-question review set. Five approved Part 1 photo/transcript alignment amendments are explicitly recorded; existing keys/options/choice IDs remain stable.
- IndexedDB: database `toeic-vocabulary-phase1`, version 1, store `workspace`; no schema/profile changes. User's request to defer personal import/export/migration QA remains active.
- Actual Pexels JPG bytes are not present in this local working copy; local strict photo validator therefore cannot be marked PASS (0/8). The user reports uploading them to the repository, but the remote bytes were not retrieved in this session. Check all eight `assets/listening/part1-*.jpg` on the actual branch and rerun strict photo validation before release. Remote Actions, Pages and real-device browser QA remain unverified. The generic data validator now correctly ignores missing OPTIONAL files while the strict photo CI step remains blocking.

### v2.21.0 delivery record — Legacy collocation cleanup / CI investigation

- Batch 011 applied 7 guarded changes across 6 vocabulary JSON files: `apprentice-n`, `event-coordinator-n`, `fare-n`, `replace-v`, `reserve-v`, `warehouseman-n`, `zero-based-budgeting-n`. These replace derived/broad associations with direct headword collocation phrases verified against dictionary, occupational and budgeting references.
- `tools/quality-baseline.json` was tightened only after the validator reported exactly 8 FD001 entries resolved. No new debt was added. Final state: 928 records, 928 stable IDs, 0 ERROR / 0 WARNING.
- No sense/definition/example/IPA/family/ID, Listening/Reading/Grammar question, choice identity, answer key or IndexedDB schema/profile was changed. Personal IndexedDB import/export/inspection/reset/migration remains deferred.
- Targeted tests: baseline IDs 13/13, patch data 11/11, sync version 12/12, choice history 5/5 and new collocation cleanup 3/3 PASS. Validator unit suite grouped execution stalled in the local sandbox; the release report intentionally does not claim a complete suite-wide PASS.
- GitHub Actions investigation: run 42981524564 / job 130392820806 shows a generic exit 1. On the exact local V2.20 workflow the 14th declared step is `choice_history`, not the data validator; local test_choice_history passes 5/5. Remote command, commit SHA and workflow revision still need direct log access; no CI fix/deploy is claimed. See `docs/reports/GITHUB_ACTIONS_CI_INVESTIGATION_2026-11-11.md`.
- Test report: `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.21.0.md`; batch record: `docs/batches/TOEIC_LEXICAL_CLEANUP_BATCH_011_v2.21.0.md`.

### v2.20.0 delivery record — Vocabulary examples, POS cards & Data Workspace detail

- **Typography:** English examples are 13.25px and Vietnamese translations 12px with 1.65 line-height; list/reference examples also receive a readability adjustment.
- **Sense-aware details:** the word-detail modal groups senses into one card per POS. Senses of the same POS share a card; definitions, relations, examples and verb forms are nested in the relevant group. The old duplicate global POS strip is removed.
- **Data Workspace:** clicking a word-name row now handles `data-detail` and opens the detail modal. Edit and delete actions remain separate.
- **Canonical vocabulary:** 928/928 stable IDs preserved. The 928 canonical headwords now contain 954 examples, each linked by `sense_index`; all 51 senses across 25 multi-sense entries have a dedicated example. Twenty-eight short examples were rewritten; 26 sense-specific examples were added. Three cross-POS duplicate definitions and two additional wording/usage issues were corrected.
- **Quality gate:** `EX010` validates example `sense_index`; `EX011` requires a mapped example for every sense. Vocabulary validator reports 0 errors and 8 known legacy FD001 warnings (down from 12); learning validator reports 0 errors/0 warnings. Automated corpus checks do not replace native-speaker or TOEIC-teacher review.
- **Tests:** 164/164 methods PASS, accounted for via 129 non-validator methods and 35 validator methods run in successful groups after the monolithic sandbox run hit its limit. Runtime smoke, JS syntax and version sync PASS.
- **Preservation:** all 211 Listening/Reading questions and their IDs/keys/options are unchanged. IndexedDB remains database `toeic-vocabulary-phase1`, version 1, store `workspace`; no schema change. Personal profile import/export/reset/inspection/migration testing remains deferred; default profile only.
- **QA boundary:** local Chromium/Playwright navigation was blocked by `ERR_BLOCKED_BY_ADMINISTRATOR`; no real-browser screenshot/interaction or 15.6-inch laptop 100% zoom verification is claimed. Remote GitHub Actions, commit/push and Pages deploy are pending. Independent TOEIC-teacher signoff is pending.
- **Evidence:** `docs/batches/TOEIC_VOCABULARY_EXAMPLE_POS_BATCH_010_v2.20.0.md` and `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.20.0.md`.

### v2.19.0 delivery record — Remaining Listening/Reading second pass

- Re-reviewed all 148 questions outside Part 7: Listening 102 (P1=8/P2=25/P3=39/P4=30) and Reading 46 (P5=30/P6=16). Combined with the 63 Part 7 items reviewed in v2.18.0, internal second-pass coverage reaches 211/211 Listening/Reading questions.
- No verified content defect warranted an answer/choice edit in this batch. The existing answer keys, option text/order/IDs, question order and counts remain unchanged. This conservative outcome is not external expert or ETS signoff.
- Added review inventory with SHA-256 source fingerprints and five regression tests to enforce the 148-question coverage scope and structural integrity.
- Sidebar footer fix from v2.18.0 remains in the v2.19.0 package: desktop sidebar nav scrolls independently, while the local-data block and version text stay pinned. It still requires visual confirmation in a real browser at 100% zoom on the user's 15.6-inch laptop.
- Personal IndexedDB import/export/migration tests remain deferred; default app profile only, no personal data touched, database version/store/schema unchanged.
- User confirms v2.17.0 was the version uploaded to GitHub. v2.19.0 is a new local package for the user's next GitHub update; no commit, push, Pages deploy or remote CI pass is claimed.
- Test and package evidence: `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.19.0.md` and `docs/reports/TOEIC_REMAINING_CONTENT_SECOND_PASS_v2.19.0.md`.

### v2.18.0 delivery record — Sidebar visibility + Part 7 second pass

- Version strings are synchronized to 2.18.0 in manifest, Service Worker, HTML, README and Master. The PWA cache name rotates to `toeic-vocab-github-only-v2.18.0`; required/optional app-shell resources remain unchanged.
- Sidebar fix: desktop nav can scroll independently while local-data card/version stays anchored and visible. Short laptop height spacing is compacted at 820 px and 680 px media thresholds. No desktop UI text is hidden by this fix.
- Part 7: 63 questions / 24 sets received a second internal review. Two document inconsistencies were clarified in the source and translation; answer text, answerIndex, stable question identity, choiceIds and sequence were preserved.
- The older double-passage-order and triple-passage-meeting sets each contain only one question and do not use every document to require cross-document reasoning. They remain correct-key items but are flagged for future content expansion rather than being silently counted as strong integrated multi-passage practice.
- Vocabulary remains 928 / 928 stable IDs; Listening 56 units / 102 questions; Reading 35 resources / 109 questions (P7 38 single / 25 multiple); Grammar 25 lessons / 54 exercises. No IndexedDB version/store/schema change.
- Personal profile import/migration QA is deferred at the user's request; the app's default local profile is used for current development. No personal data was imported or modified.
- Local test accounting: 147/147 test methods PASS; grouped validator execution hit the sandbox time limit, so its 33 methods were verified individually. Exact execution record is in `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.18.0.md`. Browser visual QA, GitHub Actions remote, commit/push and Pages deployment are not claimed.

---

## Historical dashboard — v2.10.2 (superseded by current v2.14.0 dashboard above)

| Workstream | Tiến độ hiện tại | Còn phải làm | Trạng thái quản lý |
|---|---|---|---|
| Nền tảng GitHub Pages / PWA | App shell, Service Worker, offline cache, GitHub Pages base path đã có trong mã nguồn | Xác nhận deploy, CI remote, cache update và offline trên production | **Có mã nguồn — chưa deploy/QA production** |
| Vocabulary A–Z | 928 headwords / 928 stable IDs, 26 tệp A–Z, 32 topic; 954 contextual examples with per-sense mapping; 25 multi-sense entries grouped by POS in detail view | Continue sourced IPA/Word Family/relations/CEFR audit and TOEIC expansion; independent lexical review remains needed | **Đang làm — v2.20.0 Batch 010** |
| Hồ sơ dữ liệu | 954 contextual examples; all multi-sense examples mapped to `sense_index`; EX010/EX011 enforce mapping; 8 legacy FD001 warnings remain | Continue evidence-based lexical QA and source-backed enrichment; no forced metadata completion | **Đang làm — v2.20.0 Batch 010** |
| Smart Practice / Ôn tập | Nhiều dạng câu hỏi; modal giải thích; chờ countdown sau OK; manual next; khôi phục trạng thái chờ | Browser interaction, auto-next on/off/cancel/reload và QA responsive thực tế | **Có mã nguồn — chờ QA thiết bị** |
| Flashcard / hình ảnh | Khung ảnh ổn định, ảnh không bị phủ emoji, responsive card và content scroll | Rà viewport laptop/zoom/nội dung dài/ảnh lỗi; ảnh riêng từng từ vẫn chưa triển khai | **Có mã nguồn — chờ visual QA** |
| Listening / TTS | Part 2–4 hiện có 14 bài; chọn voice nam/nữ, preview, Daniel en-GB ưu tiên khi máy cung cấp, word gap 900 ms mặc định | Bổ sung Part 1; tăng bài Part 2–4; QA voice thật trên iPhone/Android/desktop và hội thoại nhiều speaker | **Đang hoàn thiện** |
| Reading | 16 bài, 32 câu hỏi, 1.491 từ khai báo; có một số single/double/triple passage | 8 bài thiếu `documentType`; cần tăng độ dài, dạng tài liệu, câu hỏi và giải thích | **Có mã nguồn — cần mở rộng** |
| Grammar | 21 bài, 42 bài tập | Lập ma trận độ phủ và mở rộng có kiểm chứng, tránh bài trùng | **Có mã nguồn — cần mở rộng** |
| Dữ liệu cá nhân | IndexedDB default profile; database version 1, store `workspace`; personalVocabulary schema v3 + `overrideBaseSigs` | Import/export and migration QA only when user explicitly requests; do not touch personal profile meanwhile | **Đã hoãn theo yêu cầu người dùng** |
| Full TOEIC Mock Test | Chưa triển khai | Khung đủ 7 Part / 200 câu, timer, navigation, scoring và report | **Chưa bắt đầu — Phase 6** |
| Tài liệu / quy trình | Tất cả `.md` đã gom trong `docs/`; một Master duy nhất; reports/batches/sources chia thư mục | Mỗi batch mới phải cập nhật Master + report + source trong đúng thư mục | **Đã tái cấu trúc trong v2.10.2** |

### Các quyết định đã thống nhất và cần giữ (theo kế hoạch Claude + ChatGPT đã được ghi nhận)

Các mục dưới đây được kế thừa từ kế hoạch đã thống nhất trước đây; lần cập nhật này không giả định đã có phiên trao đổi mới với Claude. Nếu có thay đổi, phải ghi decision và ngày phê duyệt trong Master trước khi sửa mã nguồn.

1. **Một Master duy nhất:** `docs/MASTER_STATUS.md` là nguồn sự thật về phạm vi, tiến độ, quyết định và roadmap. Không tạo master/roadmap/data-guide thứ hai.
2. **GitHub Pages-only:** giữ triển khai tĩnh + PWA; không thêm backend, Cloudflare hay dịch vụ ngoài nếu chưa có yêu cầu mới. Dữ liệu cá nhân lưu trên thiết bị.
3. **Không làm mất dữ liệu:** giữ 928 stable IDs, không xóa/đổi ID khi biên tập; base vocabulary read-only trong UI; dữ liệu cá nhân không ghi ngược vào JSON gốc.
4. **Không bịa dữ liệu để lấp trường:** IPA, CEFR, word family, verb forms, collocations, synonyms/antonyms phải có căn cứ theo POS/sense và nguồn. Trường không áp dụng hoặc chưa chắc phải để trống có chủ đích.
5. **Batch nhỏ, có khóa:** dùng patch `baseDataVersion`, SHA-256 ID set, stable ID, `expect.old`; dry-run trước apply; chạy validator và báo cáo before/after. Không mass reclassification.
6. **TOEIC-only until acceptance:** tập trung 100% vào TOEIC Listening & Reading; chưa đưa IELTS/Academic vào dữ liệu, UI, bộ lọc, lộ trình hoặc batch nội dung. Chỉ mở IELTS sau khi đạt các cổng nghiệm thu TOEIC được ghi trong Master. Mục tiêu 3.000–5.000 TOEIC headwords/lemma là mốc quản trị, không phải danh sách chính thức của ETS.
7. **Tách loại đơn vị:** headword/lemma, sense, word family, phrasal verb, idiom và collocation không cộng gộp thành một con số “từ vựng”.
8. **Phase 5 trước Phase 6:** hoàn thiện chất lượng dữ liệu, các module học tập và QA thực tế trước khi xây Full Mock Test 200 câu.
9. **TTS phụ thuộc thiết bị:** app chỉ chọn voice browser/OS cung cấp; không khẳng định khử ồn hoặc chất lượng premium khi không có; giữ lựa chọn thủ công ưu tiên cao hơn fallback Daniel.
10. **Bàn giao trung thực:** không ghi deploy/commit/CI/thiết bị đã PASS nếu chưa có bằng chứng thao tác trực tiếp.

### Thứ tự triển khai được giữ

- **Nhánh 2.10.x — hoàn thiện dữ liệu:** tiếp tục IPA có nguồn → Word Family theo quan hệ hình thái → synonyms/antonyms + related gloss theo sense → CEFR và nguồn → mở rộng headwords TOEIC theo ma trận. Mỗi batch chỉ xử lý nhóm nhỏ, không đổi ID.
- **Phase 5E — Listening:** bổ sung Part 1 bằng ảnh và câu mô tả; sau đó tăng dần Part 2–4, hội thoại 2–3 người, short talks, transcript, bản dịch, câu hỏi và QA TTS trên thiết bị.
- **Phase 5F — Reading & Grammar:** chuẩn hóa `documentType`, mở rộng độ dài/loại văn bản và câu hỏi; lập ma trận Grammar cơ bản → nâng cao.
- **Phase 5H — QA & phát hành:** desktop/laptop, tablet, iPhone Safari, Android Chrome; PWA install/offline/cache; IndexedDB/export/import; sau đó mới đánh dấu Phase 5 DONE.
- **Phase 6 — Full Mock Test:** khung thi thử 7 Parts / 200 câu, timer, điều hướng, đánh dấu, nộp bài, giải thích, phân tích theo Part; điểm quy đổi chỉ là ước lượng học tập.

### Quy ước quản lý tài liệu

- `docs/MASTER_STATUS.md`: cập nhật bảng workstream, số liệu, blockers và next actions sau mỗi batch/release.
- `docs/batches/`: báo cáo phạm vi/ID/bản ghi đã xử lý của từng batch.
- `docs/reports/`: test report, audit và QA.
- `docs/sources/`: nguồn tham khảo và phương pháp biên tập.
- `docs/README.md`: chỉ mục tài liệu và cách chạy thử/triển khai.
- `docs/CHANGELOG.md`: nhật ký phiên bản. Mọi Markdown mới phải đặt đúng folder; không rải `.md` ở root.

---

## 1. Kết luận hiện tại

**Giai đoạn hiện tại: TOEIC-only Phase 5 — hoàn tất hai vòng rà soát nội bộ toàn bộ 211 câu Listening/Reading, tiếp tục QA giao diện và độ phủ nội dung. Phase 6 (Full Mock 200 câu) chỉ bắt đầu khi có rà soát độc lập và QA nền tảng đạt cổng nghiệm thu. IELTS đang bị khóa phạm vi.**

Nền tảng ứng dụng, từ điển A–Z, ôn tập, flashcard, Grammar, Reading, Listening, PWA và lưu dữ liệu cục bộ đã có mã nguồn. Việc còn thiếu lớn nhất không phải thêm nhiều màn hình mới, mà là:

1. Làm giàu và kiểm chứng dữ liệu từ vựng hiện có.
2. Bổ sung hình minh họa riêng cho từng từ và nội dung nghe/đọc có chiều sâu.
3. Hoàn thiện Listening theo cấu trúc đủ Part, hội thoại tự nhiên và chất lượng giọng trên thiết bị thật.
4. Rà soát nguồn của các dạng bất quy tắc/ngoại lệ còn lại; hoàn thiện word family, IPA và quan hệ từ.
5. Kiểm thử toàn bộ luồng học tập trên desktop, tablet, iPhone và Android trước khi mở rộng sang Full Mock Test.

**Số liệu dữ liệu tại baseline v2.10.2 (trước v2.11.0):** 928 bản ghi trong 26 tệp A–Z; 32 chủ đề; CEFR A1=64, A2=227, B1=276, B2=294, C1=67 (ước lượng biên tập; riêng `competitor` được Cambridge xác nhận B1). Validator: 0 ERROR, 12 WARNING legacy (DF005=3, EX006=1, FD001=8 vi phạm/7 hồ sơ). IPA=574/928; `word_family`=131/928; synonyms=361 hồ sơ, antonyms=213; verb_forms=291, collocations=758. ID set giữ nguyên. v2.10.2 không thêm nợ validator mới.

> Đính chính kiểm toán lịch sử (06/11/2026): ZIP v2.9.0 có 577 bản ghi; ZIP v2.9.2 chỉ còn 492. Đối chiếu theo `word ID` xác nhận 85 bản ghi đã mất; đã khôi phục đủ 85 bản ghi. Đây là mốc phục hồi lịch sử v2.9.2, không phải tổng hiện tại: các Batch 001–005 sau đó nâng dữ liệu lên 928 bản ghi.

## 2. Phạm vi sản phẩm đã thống nhất

- Từ điển TOEIC A–Z, tìm kiếm và lọc theo chữ cái/chủ đề/loại từ/CEFR.
- Phân nhóm từ vựng theo chủ đề; mở rộng từ cơ bản đến nâng cao, có mức CEFR và độ khó tham khảo.
- Ôn tập thông minh: câu hỏi ngẫu nhiên, điền chữ còn thiếu, nghĩa → từ, từ → nghĩa, loại từ, đồng nghĩa/trái nghĩa và dạng động từ.
- Flashcard thân thiện với người học trẻ: hình minh họa, từ, phát âm, nghĩa, cách dùng và ví dụ; học theo lượt 10 từ, kiểm tra nhanh, trộn từ sai với từ mới.
- Grammar: cấu trúc câu, điểm ngữ pháp, ví dụ và bài tập tách bạch câu hỏi/đáp án/giải thích.
- Reading: email, thư, thông báo, quảng cáo tuyển dụng, lịch trình, văn bản đơn/đôi/ba và câu hỏi đọc hiểu.
- Listening: Part 1–4, audio/hội thoại, nhiều người nói, câu hỏi, transcript và giải thích.
- Nhắc học theo chu kỳ 60/90/120/180 phút.
- Từ cá nhân có thể thêm/sửa/ẩn/xóa; dữ liệu từ điển gốc chỉ đọc.
- Google AI theo cơ chế prompt một chiều: tạo prompt trong app rồi mở Google AI Mode bên ngoài.
- Giao diện responsive desktop/tablet/mobile, PWA và khả năng dùng offline với app shell/dữ liệu đã cache.
- Tiến độ, từ cá nhân và cài đặt được lưu trên thiết bị; có Export/Import để sao lưu/chuyển thiết bị.
- Footer ghi nhận tác giả: **Vũ Nguyễn Hoàng Phúc**.

## 3. Kiểm kê chức năng hiện có

| Module | Đã có trong mã nguồn | Còn thiếu / giới hạn | Trạng thái |
|---|---|---|---|
| Nền tảng & điều hướng | GitHub Pages, PWA, menu chính, CSS responsive, Service Worker | Chưa nghiệm thu đầy đủ trên thiết bị vật lý; cần kiểm tra cập nhật cache sau deploy | Có mã nguồn; chờ QA |
| Từ điển A–Z | 928 từ, 26 tệp JSON, tìm kiếm/lọc, chi tiết từ | Quy mô còn nhỏ so với mục tiêu dài hạn 3.000–5.000 từ; chất lượng trường dữ liệu còn không đồng đều | Đang phát triển nội dung |
| Chủ đề | 32 chủ đề gốc; 12 nhóm tổng hợp Flashcard; bộ lọc | 12 nhóm tổng hợp là bộ lọc ảo, không phải 12 bộ dữ liệu độc lập | Có mã nguồn |
| Smart Practice | Nhiều dạng câu hỏi: từ/nghĩa, điền chữ, loại từ, đồng/trái nghĩa, verb forms; lưu tiến độ | Cần rà độ phủ từng dạng câu hỏi, cân bằng độ khó và chất lượng distractor | Có mã nguồn; cần QA nội dung |
| Flashcard | Lượt 10 từ, lật thẻ, phát âm, ví dụ, nghĩa, collocations, synonyms/antonyms, verb forms; quiz và ôn từ sai | Hình hiện tại chủ yếu theo chủ đề, chưa có ảnh riêng từng từ; hồ sơ từ chưa đồng đều | Đã có nền tảng; đang hoàn thiện |
| Grammar | 21 bài, 42 bài tập; có công thức, giải thích, ví dụ | Cần mở rộng từ nền tảng đến nâng cao, thêm bài tập theo từng dạng và kiểm chứng giải thích | Có mã nguồn; cần mở rộng |
| Reading | 16 bài, 32 câu hỏi; có lọc, lưu tiến độ và giải thích | Tổng 1.491 từ, trung bình khoảng 93 từ/bài; cần tăng độ dài/đa dạng và bổ sung đủ email/thư/văn bản đơn–đôi–ba | Có mã nguồn; cần mở rộng mạnh |
| Listening | 14 bài, 41 lượt lời, 28 câu hỏi; Part 2: 2, Part 3: 8, Part 4: 4 | Chưa có Part 1; số bài còn ít; audio tổng hợp TTS, không phải thu âm người thật; cần QA voice thiết bị thật | Đang hoàn thiện |
| AI hỗ trợ | Tạo prompt theo từ/Grammar/Reading/Listening/Practice và mở Google AI Mode ngoài app | Không phải API AI nhúng; không kiểm soát được giao diện Google hoặc ngăn người dùng hỏi tiếp bên ngoài | Có mã nguồn; giới hạn theo thiết kế |
| Nhắc học | Chu kỳ 60/90/120/180 phút; popup/thông báo hệ thống khi khả dụng | GitHub-only không bảo đảm push đúng giờ khi app/browser đóng hoàn toàn nếu không có backend push | Có mã nguồn; giới hạn nền tảng |
| Dữ liệu cá nhân | IndexedDB, LocalStorage dự phòng, Export/Import; dữ liệu gốc chỉ đọc | Cần kiểm thử chuyển thiết bị, import/export và phục hồi dữ liệu thực tế | Có mã nguồn; cần QA |
| Full Mock Test | Chưa thấy module đề thi thử đầy đủ 200 câu trong bản hiện tại | Chưa có cấu trúc đề đủ 7 Part, đồng hồ, điều hướng câu, nộp bài, chấm điểm và báo cáo mô phỏng | Chưa triển khai |

## 4. Kiểm kê dữ liệu chi tiết

### 4.1 Vocabulary

- **Tổng:** 928 bản ghi; A1: 64, A2: 227, B1: 276, B2: 294, C1: 67. Phân loại CEFR là ước lượng biên tập, chưa phải xác nhận chính thức theo Cambridge/ETS.
- Mỗi từ hiện có một ví dụ tiếng Anh.
- Mỗi bản ghi có `senses`, `topics`, CEFR và một ví dụ; IPA US có ở 574/928 hồ sơ sau v2.10.2; 354 hồ sơ còn thiếu IPA.
- `word_family` có dữ liệu ở 131/928; còn trống ở 797 hồ sơ. v2.10.2 thêm 9 quan hệ hình thái có nguồn giữa các headword đã tồn tại.
- `verb_forms` có dữ liệu ở 291/928; còn trống ở 637 hồ sơ không có sense động từ. Cả 291/291 hồ sơ có sense động từ đều đã có forms; VF001/VF002 chặn tái phát.
- `collocations` có dữ liệu ở 758/928; còn trống ở 170 hồ sơ chưa có collocation phù hợp. Cả 291/291 hồ sơ có sense động từ đều có ít nhất một collocation; FD003 chặn tái phát.
- Có 347 mục trong `related-terms.json`; validator đếm synonyms=361 và antonyms=213 quan hệ trong hồ sơ từ. `competitor` được bổ sung challenger/contender/rival theo Cambridge. Cần tiếp tục kiểm tra ngữ cảnh, không tự động suy diễn quan hệ.
- Dạng động từ được lưu trực tiếp trong `verb_forms` của từng hồ sơ; file `data/verbs/irregular-verbs.json` rỗng và không có consumer đã được gỡ khỏi v2.9.10. Những dạng bất quy tắc/ngoại lệ trong 122 hồ sơ mới được rà riêng; không tạo một kho irregular verbs song song chưa được runtime sử dụng.
- Mỗi hồ sơ chỉ có một ví dụ; cần tăng ví dụ theo nghĩa/ngữ cảnh, kèm bản dịch và ghi chú cách dùng.

### 4.2 Grammar

- 21 bài học, 42 bài tập.
- Đã có các nhóm như câu cơ bản, thì, từ loại, giới từ, mạo từ, bị động, điều kiện, mệnh đề quan hệ, liên từ và so sánh.
- Cần lập ma trận độ phủ ngữ pháp TOEIC, xác định nội dung thiếu và bổ sung bài tập theo cấp độ; không tạo bài trùng chủ đề chỉ để tăng số lượng.

### 4.3 Reading

- 16 bài, 32 câu hỏi; tổng độ dài khai báo 1.491 từ.
- Có một số dạng như EMAIL, NOTICE, JOB POSTING, ITINERARY, ANNOUNCEMENT, DOUBLE PASSAGE, TRIPLE PASSAGE; 8 bài chưa khai báo `documentType`.
- Cần bổ sung email/thư trao đổi dài hơn, memo, advertisement, invoice/order, schedule, policy, article và bộ văn bản đôi/ba có liên kết thông tin.
- Cần tăng số câu hỏi theo bài, đa dạng câu hỏi mục đích/chi tiết/suy luận/từ vựng/tham chiếu và giải thích đáp án.

### 4.4 Listening

- 14 bài: Part 2 có 2; Part 3 có 8; Part 4 có 4. Tổng 41 segments và 28 câu hỏi.
- Part 1 chưa có dữ liệu.
- v2.9.2 đã có cơ chế ưu tiên voice nữ/nam theo nhãn speaker, giữ voice ổn định theo speaker và nghỉ ngẫu nhiên 650–850 ms giữa lượt lời.
- Cơ chế giới tính voice dựa vào tên/nhãn voice do hệ điều hành công bố; Web Speech API không chuẩn hóa metadata giới tính. Thiết bị thiếu voice phù hợp có thể phát voice dự phòng.
- TTS là giọng tổng hợp trên trình duyệt, không phải audio người thật/đề ETS. Chưa xác nhận chất lượng trên từng voice pack iOS/Android/desktop.
- Cần bổ sung Part 1, thêm hội thoại 2–3 người và short talks, tăng câu hỏi, transcript/bản dịch/từ vựng và kiểm thử khoảng nghỉ/dừng/phát lại.

### 4.5 Hình ảnh

- Có 24 file ảnh chủ đề (SVG/WebP) được tái sử dụng trong các thẻ chủ đề.
- Chưa có bộ ảnh minh họa riêng cho 928 từ.
- Cần tạo ảnh theo batch nhỏ, ưu tiên nhóm từ TOEIC phổ biến; không tạo ảnh hàng loạt thiếu kiểm duyệt hoặc làm tăng dung lượng không cần thiết.

## 5. Lộ trình phát triển còn lại

Thực hiện tuần tự theo batch nhỏ. Hoàn thành và kiểm tra một nhóm trước khi chuyển nhóm kế tiếp.

### Ưu tiên 1 — Khôi phục và kiểm định dữ liệu từ vựng

- Đã so sánh trực tiếp 26 tệp A–Z của hai ZIP: v2.9.0 có 577 bản ghi, v2.9.2 có 492; 85 ID chỉ có ở v2.9.0, không có ID mới ở v2.9.2.
- Đã phục hồi đủ 85 bản ghi gốc vào bản làm việc v2.9.2; cập nhật số lượng từng chữ cái và CEFR trong manifest.
- Các trường còn trống sau phục hồi: `word_family` 541/577; `verb_forms` 428/577; `collocations` 209/577. Các trường này cần được rà theo từ loại và ngữ cảnh, không điền máy móc.
- Tiếp theo kiểm tra từng bản ghi phục hồi về nghĩa, IPA, ví dụ, chủ đề và CEFR; giữ nguyên ID ổn định.

### Ưu tiên 2 — Hoàn thiện và mở rộng từ vựng

- Hoàn thiện 577 bản ghi hiện có trước khi thêm hàng loạt từ mới.
- Sau đó mở rộng có kiểm soát theo chủ đề TOEIC và cấp độ A1–B2; mục tiêu định hướng 4.000–5.000 mục từ, không phải cam kết số lượng bằng mọi giá.
- Mỗi batch phải có nguồn tham khảo, kiểm tra trùng, nghĩa theo ngữ cảnh, IPA, từ loại, ví dụ dịch, CEFR ước tính và kiểm định schema.
- Định nghĩa hoàn thành: không còn trường bắt buộc thiếu; trường có điều kiện được xử lý đúng loại từ; không có bản ghi trùng hoặc nghĩa/quan hệ sai.

### Phase 5C — Ảnh minh họa riêng cho Flashcard (lùi sau từ vựng)

- Bắt đầu 10–20 từ phổ biến, ưu tiên các từ có thể minh họa trực quan trong môi trường văn phòng/du lịch/giao tiếp TOEIC.
- Mỗi ảnh phải gắn đúng `word id`, có fallback khi ảnh không tải được và tối ưu dung lượng cho mobile/PWA.
- Không thay ảnh chủ đề đang dùng; không sửa dữ liệu gốc ngoài trường tham chiếu ảnh đã thống nhất.
- Nghiệm thu: ảnh đúng nghĩa, không gây hiểu nhầm, tải được offline sau cache và không làm vỡ thẻ trên mobile.

### Phase 5D — Hoàn thiện hồ sơ từ vựng (được nâng thành ưu tiên hiện tại)

- Bổ sung bản dịch ví dụ, giải thích cách dùng và ví dụ theo nghĩa quan trọng.
- v2.9.11 đã bổ sung 24 IPA có nguồn, sửa 7 IPA lỗi, mở rộng `word_family` và xử lý một synonym/CEFR case có nguồn. Tiếp tục rà synonym/antonym, word family, IPA và CEFR theo từng batch; không mass reclassification.
- Thẩm định IPA US/UK, loại từ, nghĩa và CEFR; phân biệt từ nhiều nghĩa.
- Kiểm tra synonyms/antonyms theo đúng nghĩa, không chỉ dựa trên từ gần nghĩa chung.
- Mỗi batch có danh sách ID từ đã xử lý và kiểm tra JSON/schema trước khi nhập.

### Phase 5E — Hoàn thiện Listening

- Bổ sung Part 1 bằng bộ ảnh phù hợp và câu hỏi mô tả hình.
- Tăng dần Part 2/3/4; ưu tiên hội thoại nhiều người nói, vai rõ ràng, ngữ điệu và khoảng nghỉ tự nhiên.
- Bổ sung câu hỏi, đáp án, giải thích, transcript, bản dịch và vocabulary theo bài.
- Kiểm tra giọng nữ/nam, nhiều speaker, gap 0,5–1 giây, dừng giữa câu, phát lại và tốc độ trên iPhone/Android/desktop.
- Không quảng bá TTS như audio người thật hoặc audio đề thi chính thức.

### Phase 5F — Hoàn thiện Reading & Grammar

- Reading: mở rộng dạng văn bản và độ dài; bổ sung bộ câu hỏi theo mục tiêu đọc hiểu; rà các bài thiếu `documentType`.
- Grammar: lập ma trận kiến thức; bổ sung bài thiếu theo trình tự cơ bản → trung cấp → nâng cao; bảo đảm câu hỏi, đáp án và giải thích tách biệt.
- Không tăng số lượng bài nếu nội dung trùng hoặc câu hỏi không có giá trị học tập.

### Phase 5G — Động từ & ôn tập thích ứng

- v2.9.10 đã bổ sung 122 bộ V1/V-s/V2/V3/V-ing, nâng coverage lên 291/928; toàn bộ 291 record có verbal sense đã hoàn tất. v2.9.11 tiếp tục cập nhật 24 IPA có nguồn và word_family.
- Các đợt tiếp theo chỉ sửa form khi có bằng chứng từ POS/sense và nguồn từ điển; rà các ngoại lệ còn tranh luận, không tạo file irregular verbs riêng nếu runtime không đọc.
- Kiểm tra lịch ôn, từ sai, từ đến hạn, lựa chọn 5/10 từ, chống lặp quá sớm và khôi phục tiến độ sau reload/import.

### Phase 5H — QA tổng thể & phát hành ổn định

- Kiểm tra desktop, tablet, iPhone và Android; portrait/landscape; font, tràn ngang, modal, audio controls và menu.
- Kiểm tra PWA install, Service Worker update, offline cache, đường dẫn GitHub Pages `/Toeic/`.
- Kiểm tra IndexedDB, Export/Import, dữ liệu cá nhân và dữ liệu gốc chỉ đọc.
- Kiểm tra tất cả module từ đầu đến cuối; sửa lỗi và cập nhật báo cáo test thực tế.
- Chỉ sau khi QA đạt mới đánh dấu Phase 5 hoàn tất.

### Phase 6 — Full TOEIC Mock Test (chưa bắt đầu)

- Xây dựng bài thi mô phỏng đủ 7 Parts, tổng 200 câu: Listening 100 câu (Part 1–4) và Reading 100 câu (Part 5–7).
- Có hướng dẫn, đồng hồ đếm ngược, điều hướng câu/Part, đánh dấu câu, lưu trạng thái trong phiên, xác nhận nộp bài.
- Chấm đúng/sai, giải thích sau khi nộp, phân tích theo Part/kỹ năng và đề xuất nội dung ôn tập.
- Điểm quy đổi chỉ được ghi rõ là ước lượng học tập; không tuyên bố tương đương điểm ETS nếu không có bảng quy đổi được xác thực.
- Có thể làm nhiều đề theo batch; không tạo một kho đề lớn trước khi khung thi và cơ chế chấm được nghiệm thu.

## 6. Quy tắc kỹ thuật và dữ liệu phải giữ

- Giữ kiến trúc **GitHub Pages-only**; không thêm Cloudflare/backend nếu chưa có yêu cầu mới.
- Dữ liệu từ điển gốc trong `data/vocabulary/*.json` là read-only đối với giao diện người dùng.
- Từ cá nhân, tiến độ và cài đặt lưu cục bộ trên thiết bị; dùng Export/Import để chuyển thiết bị.
- Không để dữ liệu cá nhân ghi ngược vào kho JSON gốc.
- Dùng đường dẫn tương đối phù hợp base path `/Toeic/`.
- Thay đổi dữ liệu phải chạy `python tools/validate-data.py`; thay đổi JavaScript phải chạy `node --check assets/js/app.js` và `node --check sw.js`.
- Khi thay app shell/tài nguyên, cập nhật cache version trong `sw.js`.
- Phát triển theo từng batch nhỏ; mỗi batch ghi rõ file thay đổi, dữ liệu thêm, kiểm thử, kết quả và phần chưa kiểm thử.
- Không tuyên bố đã deploy/commit/push nếu chưa có xác nhận thao tác thực tế.

## 7. Các lỗi/điểm cần đồng bộ đã phát hiện trong ZIP

1. `data/manifest.json` đã đồng bộ version 2.9.2. Sau khi phục hồi 85 bản ghi, số lượng từng chữ cái và tổng số đã được cập nhật theo dữ liệu thực tế.
2. Đã xác nhận 85 bản ghi bị mất giữa ZIP v2.9.0 và v2.9.2; đã phục hồi nguyên bản từ v2.9.0. Cần rà soát chất lượng nội dung của các bản ghi phục hồi trước khi coi là hoàn thiện.
3. `DATA_GUIDE.md` trùng nội dung với Master. Nội dung hướng dẫn schema đã được tích hợp vào Master; không duy trì thêm roadmap/data guide riêng để tránh phân tán.
4. `data/verbs/irregular-verbs.json` rỗng, không có consumer runtime/tooling và đã được gỡ trong v2.9.10; không tái tạo file nếu chưa có thiết kế sử dụng thực tế.
5. 8/16 Reading chưa khai báo `documentType`; cần chuẩn hóa trong batch Reading.

## 8. Kiểm tra đã chạy trên gói v2.9.2

| Kiểm tra | Kết quả |
|---|---|
| `python tools/validate-data.py` | PASS — 577 từ, 26 tệp chữ cái, 32 chủ đề, 345 related-term glosses |
| `node --check assets/js/app.js` | PASS |
| `node --check sw.js` | PASS |
| Đếm dữ liệu Grammar/Reading/Listening | PASS — 21/16/14 bài; 42/32/28 bài tập/câu hỏi tương ứng |
| Kiểm tra giọng nam/nữ và delay trên thiết bị thật | Chưa nghiệm thu |
| Kiểm thử toàn bộ giao diện trên iPhone/Android/desktop | Chưa nghiệm thu trong lần kiểm kê này |
| GitHub Pages deploy v2.9.2 | Chưa xác nhận |

## 9. Việc tiếp theo đã chốt

**Trạng thái hiện tại: v2.10.0 đã triển khai bộ UX/Smart Review, Flashcard, TTS và migration `baseSig` trên mã nguồn; dữ liệu 928 hồ sơ được giữ nguyên.** Tiếp tục ưu tiên audit IPA/word family/synonym/antonym/CEFR theo batch có nguồn; song song cần QA giao diện và voice trên iPhone Safari, Android Chrome và desktop thật. Không tuyên bố giọng nam đã đạt chất lượng trên mọi thiết bị trước khi nghe thử các voice khả dụng. Chưa mở rộng lên 4.000–5.000 từ trước khi chất lượng dữ liệu hiện tại đạt tiêu chí nghiệm thu. Phase 6 chỉ bắt đầu sau khi Phase 5 và QA hoàn tất.

### Nhật ký cập nhật

| Ngày | Phiên bản | Nội dung |
|---|---|---|
| 06/11/2026 | v2.9.2 working recovery | Đối chiếu ZIP v2.9.0/v2.9.2 theo ID; xác nhận và phục hồi 85/85 bản ghi bị thiếu; cập nhật manifest lên 577; chuyển ưu tiên Phase 5 sang hoàn thiện từ vựng trước hình ảnh/Listening/Reading/Grammar. Chưa phát hành. |


## Cập nhật Vocabulary Batch 002 — v2.9.5 (06/11/2026)

- Nền dữ liệu: v2.9.3 gồm 612 từ; bổ sung 44 headwords mới, tổng hiện tại 656.
- Đã cập nhật các tệp A–Z, `data/manifest.json`, `data/vocabulary/batch-002.json`, `VOCABULARY_BATCH_002.md`, CHANGELOG và Service Worker cache version.
- Các từ mới có IPA US, nghĩa chính, định nghĩa tiếng Anh, ví dụ kèm bản dịch tiếng Việt, chủ đề và một số collocations/word family.
- CEFR vẫn là ước lượng biên tập; synonyms/antonyms và verb forms không tự điền khi chưa xác minh.
- Trạng thái: bản làm việc draft-review, chưa triển khai GitHub Pages; cần QA ngôn ngữ trước khi xem là bộ dữ liệu thi chính thức.


## v2.9.5 — Batch 003 update

- Added: 75 TOEIC-priority headwords.
- Total vocabulary: 731 headwords.
- Batch status: draft-review; not deployed.
- IPA, CEFR, synonyms/antonyms and inflections remain subject to editorial verification; blank fields are intentionally not fabricated.
- Next: continue TOEIC-specific multiword expressions, verbs/adjectives/adverbs and Part 1–7 contextual coverage.


## v2.9.6 — TOEIC Batch 004
- Added 79 TOEIC-focused entries; total vocabulary records: 810.
- Batch file: `data/vocabulary/batch-004.json`; report: `VOCABULARY_BATCH_004.md`.
- This is a draft-review data expansion; no claim of official TOEIC list completeness or deployment.


## Update v2.9.7 — Batch 005
- Baseline v2.9.6: 810 headwords.
- Added in Batch 005: 118 unique headwords.
- Current total: 928.
- Focus: TOEIC-first comprehensive expansion.
- Status: draft-review; IPA and lexical relations not verified remain blank.
- Validation: see batch report and automated checks.


## Thiết kế kỹ thuật v2.9.8 — đã thống nhất (08/11/2026)
Trạng thái: **Commit A PASS; Commit B đã xây dựng và kiểm thử trong ZIP tổng v2.9.8**. Nội dung 928 từ không thay đổi trong v2.9.8. Chưa xác nhận commit/push lên GitHub Pages.

**Phạm vi và thứ tự**
- v2.9.8 Data Quality & Release Integrity → v2.9.9 sửa 160 định nghĩa giả và 79 câu ví dụ + 79 bản dịch theo khuôn (tất cả 79 ID ví dụ đều nằm trong 160 ID định nghĩa; tổng cộng 160 bản ghi duy nhất, không phải 171) → v2.9.10 verb forms và collocations → v2.9.11 IPA/word family/synonym/CEFR batch 1 → v2.10.0 UX và migration `baseSig` cho `personalVocabulary.overrides`.
- Batch mở rộng từ vựng giảm còn 100–150 từ/batch và bắt buộc qua validator. Chưa mở rộng IELTS.

**Quy ước validator (ratchet)**
- Lỗi cấu trúc: luôn ERROR, không được miễn theo baseline.
- Vi phạm đã có trong `tools/quality-baseline.json`: WARNING. Vi phạm mới ngoài baseline: ERROR. Baseline định danh theo (mã luật, id, đường dẫn), không chỉ lưu số đếm.
- Baseline không tự cập nhật; chỉ được siết lại (xóa mục đã sửa) bằng lệnh riêng trong commit được duyệt.
- Số liệu baseline v2.9.7 đã xác nhận: DF002=160, DF003=114 (Unicode NFD), EX004=79, EX005=79, DF005=3, IP001=2 (estimate-nv và transfer-nv), IP004=5, tổng 928 ID.

**Manifest và phiên bản**
- `data/manifest.json` là nguồn phiên bản duy nhất. Giữ nguyên `letters` (mảng), `categories` và các khóa app/validator đang dùng; chỉ đổi `version` và bỏ `wordCount`.
- `tools/sync-version.py` có `--check`, `--dry-run`, `--apply`; mỗi marker phải khớp đúng 1 lần, CHANGELOG chỉ kiểm tra, không tự sửa.

**Service Worker**
- Giữ tiền tố cache `toeic-vocab-github-only-v${VERSION}`. Tài nguyên bắt buộc lỗi thì install thất bại và giữ cache cũ; ảnh tùy chọn lỗi không chặn app. Chỉ xóa cache cũ khi cache mới hoàn chỉnh.
- Giữ `skipWaiting` + `clients.claim` ở v2.9.8–v2.9.9 vì dữ liệu chỉ tải một lần trong `loadData()` và schema không đổi; release nào đổi schema thì chuyển sang chờ + banner.
- Cache dữ liệu: cache-first theo từng release. `irregular-verbs.json` bị loại khỏi danh sách cache, file giữ trên đĩa đến v2.9.10.

**Patch dữ liệu (từ v2.9.9)**
- JSON Pointer theo ID, mỗi operation có `expect.old` (và `expect.pos` với sense), `--dry-run`, hủy toàn batch nếu một operation sai, log từng field, rollback kiểm lại giá trị hiện tại, mỗi batch một commit. `tools/patch-data.py` làm ở đầu v2.9.9.

**Phân công**: Claude viết và chạy công cụ, sinh baseline; ChatGPT soạn nội dung patch; mọi patch qua cổng dry-run + validator + so sánh tập ID. File này là nguồn trạng thái duy nhất.

**Đang chờ người dùng**: (1) kiểm thử v2.9.8 trên iPhone Safari và Android Chrome; (2) xác nhận deploy GitHub Pages sau khi tự triển khai; (3) nếu dùng thiết bị khác, export/kiểm tra dữ liệu cá nhân trên từng thiết bị trước các thay đổi nền dữ liệu lớn. Trên thiết bị chính đã xác nhận additions=0, overrides=0, deletedBaseIds=0.


## Phát hành mã nguồn v2.9.8 — Data Quality & Release Integrity (09/11/2026)

- Commit A: PASS, 55/55 unit test; `py_compile`, validator dữ liệu gốc, JavaScript syntax và workflow YAML đều đạt. `sync-version.py --check` trên nền v2.9.7 còn 4 marker cũ lệch; đây là trạng thái dự kiến của Commit A và đã được xử lý trong Commit B.
- Commit B: manifest 2.9.8; giữ `letters` dạng mảng, giữ `categories`, `totalWords=928`; bỏ `wordCount` vì trùng `totalWords` và không được runtime sử dụng.
- Service Worker dùng cache `toeic-vocab-github-only-v2.9.8`; 38 tài nguyên bắt buộc, 27 tùy chọn. Install thất bại nếu tài nguyên bắt buộc lỗi; tài nguyên tùy chọn chỉ cảnh báo; chỉ xóa cache release TOEIC cũ sau khi cache mới cài đủ. Không xóa cache ứng dụng khác.
- `skipWaiting()` và `clients.claim()` được giữ theo quyết định v2.9.8–v2.9.9; response lỗi không được cache như `index.html`; `irregular-verbs.json` khi phát hành v2.9.8 vẫn còn trên đĩa; file rỗng này được gỡ ở v2.9.10 sau khi xác nhận không có consumer.
- Unit test: 55/55 PASS theo log `unittest discover` đầy đủ trên Python 3.12.3 được cung cấp; sau Commit B, 55 test được xác nhận PASS theo các nhóm riêng trong sandbox (13 baseline-ID + 12 sync-version + 30 validator). Commit B không sửa `tools/` hoặc `tools/tests/`. Lượt `unittest discover` tổng hợp trên Python 3.13.5 trong sandbox không ổn định ở tiến trình con, nên không dùng làm bằng chứng PASS bổ sung.
- Kiểm tra Commit B: validator 0 ERROR, 611 WARNING legacy, 8 cảnh báo SW002 đã resolved; ID 928/928; `sync-version.py --check` PASS; JS syntax PASS; workflow YAML hợp lệ và sync-version là bước bắt buộc.
- Service Worker lifecycle smoke test (Node): PASS — required 404 abort install và giữ cache cũ; optional 404 không chặn; activate chỉ xóa cache TOEIC cũ, giữ cache ứng dụng khác; điều hướng HTTP 404 không ghi đè `index.html` trong cache.
- APP_SHELL 65 mục (38 required + 27 optional); dữ liệu A–Z không đổi byte-for-byte so với v2.9.7.
- Trạng thái giao: ZIP tổng v2.9.8 đã đóng gói; chưa deploy, chưa xác nhận kiểm thử iPhone Safari/Android Chrome.

## Phát triển v2.9.9 — Definition & Example Correction (09/11/2026)

**Trạng thái:** Đã hoàn tất 4/4 batch và tạo ZIP tổng v2.9.9. Chưa xác nhận GitHub deploy hoặc kiểm thử thiết bị thật.

### Kết quả kiểm toán mục tiêu
- Baseline gốc v2.9.7: DF002=160 IDs, DF003=114, EX004=79 IDs, EX005=79 IDs.
- Đối chiếu theo ID: toàn bộ 79 ID của EX004 và 79 ID của EX005 đều thuộc tập 160 ID của DF002. Vì vậy union chính xác là **160 bản ghi duy nhất**, không phải 171 như bản kế hoạch cũ ghi nhầm.
- Đã biên tập 160 `definition_en`, rà soát 160 ví dụ tiếng Anh và cập nhật 160 bản dịch tiếng Việt. Có 159 trường English example thực sự thay đổi; 1 câu đã đạt chất lượng nên được giữ nguyên.
- Không thay đổi số lượng bản ghi, ID, POS, IPA, CEFR, schema hoặc các dữ liệu cá nhân IndexedDB.

### Các batch đã áp dụng
| Batch | Phạm vi | Patch operations | Kết quả validator sau batch |
|---|---|---:|---|
| 001 | 40 headwords A–C | 120 | 0 ERROR; 454 WARNING legacy sau siết baseline |
| 002 | 40 headwords C–E | 119 | 0 ERROR; 303 WARNING legacy sau siết baseline |
| 003 | 40 headwords E–P | 120 | 0 ERROR; 150 WARNING legacy sau siết baseline |
| 004 | 40 headwords P–V | 120 | 0 ERROR; 19 WARNING legacy sau siết baseline |

- Patch: `patches/v2.9.9/batch-001.json` đến `batch-004.json`; công cụ: `tools/patch-data.py`; mỗi batch dry-run trước khi apply, khóa theo base version + SHA-256 ID set + ID + JSON Pointer + `expect.old` + POS khi sửa sense.
- Báo cáo: `VOCABULARY_BATCH_006.md` (Batch 001), `VOCABULARY_BATCH_007.md` (Batch 002), `VOCABULARY_BATCH_008.md` (Batch 003), `VOCABULARY_BATCH_009.md` (Batch 004).
- Baseline được siết sau mỗi batch, chỉ xóa vi phạm đã sửa; tổng cộng 600 mục vi phạm đã được loại khỏi baseline, không thêm mục mới.

### Kết quả kiểm tra working tree sau Batch 004
- `validate-data.py`: PASS — 928 bản ghi, 928 ID; 0 ERROR, 19 WARNING legacy.
- Các mục tiêu đã hết: DF002=0, DF003=0, DF004=0, EX004=0, EX005=0.
- Nợ còn lại: DF005=3 (cần rà soát thủ công các từ nhiều sense), EX006=1, FD001=8 vi phạm/7 bản ghi, IP001=2 (`estimate-nv`, `transfer-nv`), IP004=5. Không tự sửa các nhóm này bằng batch định nghĩa.
- Coverage tại thời điểm chốt v2.9.9: IPA=539, word_family=74, verb_forms=169, collocations=719, synonyms=360, antonyms=213, multi_sense=25. v2.9.10 đã nâng verb_forms lên 291 và collocations lên 758.

### Kiểm tra và bàn giao release v2.9.9
- Manifest, Service Worker, README, CHANGELOG và mọi marker version đã đồng bộ 2.9.9; schema, 928 ID và 26 tệp A–Z được giữ.
- `py_compile`: PASS. Unit tests: 64/64 PASS khi chạy theo nhóm/ca độc lập (13 baseline-ID + 9 patch engine + 12 sync-version + 30 validator). Lệnh `unittest discover` tổng hợp trong sandbox Python 3.13.5 có hiện tượng treo; workflow pin Python 3.12 và chia module riêng. CI GitHub chưa được chạy vì chưa push.
- Validator: PASS — 928 records, 0 ERROR, 19 WARNING legacy. `sync-version.py --check`: PASS. JavaScript syntax: PASS. Workflow YAML parse: PASS.
- ZIP giải nén kiểm tra: `testzip` PASS; validator và version sync chạy trực tiếp trên bản giải nén đều PASS. 26 file A–Z trong ZIP giống working tree byte-for-byte.
- ZIP: `TOEIC_Dictionary_v2.9.9_Definition_Example_Correction.zip`; SHA-256 của gói phát hành được ghi trong biên bản bàn giao tại cuộc trò chuyện (không nhúng hash tự tham chiếu vào chính ZIP).
- Trạng thái: ZIP tổng đã bàn giao; chưa deploy GitHub Pages và chưa QA iPhone Safari/Android Chrome.
- Kế hoạch tại thời điểm bàn giao v2.9.10: tiếp tục v2.9.11 rà IPA/word family/quan hệ từ/CEFR; UX được triển khai ở v2.10.0 (xem mục phát triển v2.10.0).

## Phát triển v2.9.10 — Verb Forms & Collocations (09/11/2026)

**Trạng thái:** Đã hoàn tất dữ liệu, validator, đồng bộ version và đóng gói ZIP tổng; chưa xác nhận GitHub deploy hoặc QA thiết bị thật.

### Kết quả kiểm kê và patch
- Rà lại POS ở cấp `senses`, tách token `v` trong các dạng POS ghép (`n/v`, `v/n`, `adj/v`...) và sense riêng; xác nhận 122 hồ sơ còn thiếu `verb_forms` (số liệu chính xác theo dữ liệu v2.9.9, điều chỉnh từ 121 dự kiến cũ).
- Bổ sung 122 bộ forms; giữ nguyên 169 bộ forms đã có. V1 khớp headword trong cả 291 record có ít nhất một sense động từ.
- Bổ sung collocations cho 39 hồ sơ động từ/mixed-POS trước đó rỗng; mỗi record thêm hai cụm theo ngữ cảnh TOEIC. Coverage collocations tăng 719 → 758.
- 4 patch file: `patches/v2.9.10/batch-001.json` đến `batch-004.json`; 122 operations `/verb_forms` + 39 operations `/collocations` = 161 JSON Pointer operations; 39 danh sách mới chứa tổng cộng 78 cụm collocation.
- Mỗi patch khóa `baseDataVersion=2.9.9`, `targetDataVersion=2.9.10`, SHA-256 tập ID và `expect.old`; verb-related operations yêu cầu `expect.verbSense=true`. Rollback chỉ chấp nhận khi giá trị hiện tại vẫn bằng giá trị new, tránh ghi đè chỉnh sửa xen giữa.
- So sánh trước/sau: 928 ID và tập ID không đổi; chỉ `verb_forms` và `collocations` thay đổi trong các record được patch. `quality-baseline.json` và `baseline-ids.json` không đổi.
- Đã gỡ `data/verbs/irregular-verbs.json` (rỗng, không được app/runtime/tooling đọc); không tạo dependency mới.

### Validator và chất lượng
- Thêm structural rules: VF001 (record có verbal sense phải có verb_forms), VF002 (verb_forms.v1 phải khớp headword), FD003 (record có verbal sense phải có ít nhất một collocation).
- Validator: 928 records, 0 ERROR, 19 WARNING legacy; không phát sinh nợ mới.
- Coverage sau release: IPA=539, word_family=74, verb_forms=291, collocations=758, synonyms=360, antonyms=213, multi_sense=25.
- 19 cảnh báo còn lại: DF005=3, EX006=1, FD001=8 violations/7 records, IP001=2 (`estimate-nv`, `transfer-nv`), IP004=5. Không tự động sửa trong v2.9.10.

### Kiểm thử và bàn giao
- `py_compile`: PASS. Baseline ID 13/13; patch engine 11/11; sync-version 12/12; validator 33/33 — tổng 69/69 tests PASS khi chạy theo module hoặc test case riêng. Lệnh chạy gộp validator trong Python 3.13.5 sandbox có hiện tượng timeout giữa lượt; từng test đều được thực thi riêng và trả PASS. GitHub Actions pin Python 3.12; CI thực tế vẫn chờ push.
- `validate-data.py`: PASS — 928 records, 0 ERROR, 19 WARNING legacy. `sync-version.py --check`: PASS sau khi đồng bộ 2.9.10. JavaScript syntax và YAML workflow: PASS.
- Kiểm tra APP_SHELL và ZIP integrity được chạy sau đóng gói; 26 file A–Z giữ 928 ID, các baseline không đổi.
- ZIP tổng: `TOEIC_Dictionary_v2.9.10_Verb_Forms_Collocations.zip`; SHA-256 ghi trong biên bản bàn giao ở cuộc trò chuyện. Chưa deploy GitHub Pages, chưa QA iPhone Safari/Android Chrome.

### Bước tiếp theo
- v2.9.11 Batch 001 đã hoàn tất: 31 IPA operations, 49 word_family operations và một case synonym/CEFR. Tiếp tục các batch sau cho 365 IPA còn thiếu, synonym/antonym theo sense và các family còn trống; không mass reclassification.
- v2.10.0 đã triển khai UX/Smart Review, ảnh Flashcard, TTS voice selector và khoảng nghỉ tự nhiên, kho từ A–Z responsive; đã thực hiện migration `baseSig`. Công việc tiếp theo là QA thiết bị thật và tiếp tục audit từ vựng theo nguồn.

## Phát triển v2.9.11 — IPA, Word Family & Lexical Audit Batch 001 (09/11/2026)

**Trạng thái:** Đã áp dụng 3 batch dữ liệu có khóa, chạy validator và cập nhật Master/CHANGELOG/README. ZIP tổng đã được đóng gói và kiểm tra integrity; chưa commit/push, chưa triển khai GitHub Pages và chưa QA thiết bị thật.

### Kết quả thay đổi
- IPA: 31 operations — sửa 7 giá trị cũ không hợp lệ (5 trường hợp `ər`, 2 trường hợp IPA bị gộp nhiều POS) và bổ sung 24 IPA US còn trống theo Cambridge. Coverage tăng 539 → 563/928 (61%).
- `word_family`: 49 hồ sơ được cập nhật bằng quan hệ hình thái đã rà trong nhóm từ vựng hiện có; không thêm headword hoặc đổi ID. Coverage tăng 74 → 122/928 (13%).
- Synonym/related glossary: `competitor` được bổ sung `challenger`, `contender`, `rival` theo Cambridge; thêm gloss cho `challenger` và `rival` vào `data/related-terms.json`. Synonym coverage tăng 360 → 361 records; glossary tăng 345 → 347 mục.
- CEFR: sửa riêng `competitor` từ A2 lên B1 theo nhãn Cambridge; đồng bộ word-level, sense-level và manifest. Không mass reclassification. CEFR count: A1=64, A2=227, B1=276, B2=294, C1=67.
- Giữ nguyên 928 ID và 26 tệp A–Z; không sửa ví dụ, definition, POS, verb_forms hoặc collocations trong batch này.

### Patch và baseline
- `patches/v2.9.11/batch-001-ipa.json`: 31 operations.
- `patches/v2.9.11/batch-002-word-family.json`: 49 operations.
- `patches/v2.9.11/batch-003-competitor-synonyms-cefr.json`: 4 operations.
- Mỗi patch dùng `baseDataVersion=2.9.10`, `targetDataVersion=2.9.11`, SHA-256 ID set và `expect.old`; tất cả dry-run PASS trước khi apply.
- `tools/quality-baseline.json` được tighten để loại đúng 7 cảnh báo IPA đã sửa; không thêm mục baseline mới. Còn 12 warning legacy: DF005=3, EX006=1, FD001=8 vi phạm trên 7 hồ sơ.

### Kiểm định dữ liệu sau batch
- 928 records; 0 ERROR; 12 WARNING legacy.
- Coverage: IPA=563, word_family=122, verb_forms=291, collocations=758, synonyms=361, antonyms=213. IPA còn thiếu 365; chưa tự điền khi chưa có nguồn.
- `CEFR word ≠ sense` vẫn bằng 0.
- Lưu ý `estimate` có hai cách phát âm theo POS trong Cambridge; do schema hiện chỉ có một `phonetic.us`, giá trị lưu là danh từ vì đây là sense đầu tiên. Phát âm động từ cần nâng schema/runtime riêng trong đợt sau, không gộp hai IPA vào một chuỗi.
- Test report v2.9.11 ghi 62/69 test cases xác nhận tại thời điểm đó. Trong v2.10.0 đã chạy lại theo module/nhóm và xác nhận 69/69 test cases PASS (13 baseline IDs + 11 patch engine + 12 version sync + 33 validator); không dùng kết quả chạy monolithic discovery làm bằng chứng.
- `py_compile`, JS syntax, YAML workflow, `sync-version.py --check` và APP_SHELL (65 mục, 0 file thiếu) đều PASS.
- Tiếp tục audit từ vựng v2.9.11 ở các batch kế tiếp: IPA theo nguồn, synonym/antonym theo sense, family còn thiếu và rà CEFR có căn cứ. Không coi Batch 001 là hoàn tất audit toàn bộ 928 mục.

## Phát triển v2.10.0 — Smart Review, Flashcard, Natural TTS & responsive UI (09/11/2026)

**Trạng thái:** Đã sửa mã nguồn và đóng gói release candidate; chưa deploy GitHub Pages hoặc QA thiết bị thật.

### Phạm vi và thay đổi
- Ôn tập: câu hỏi/đáp án có vùng làm việc ổn định; sau khi trả lời mở modal phân tích đúng/sai, lựa chọn, nghĩa, POS, word family, verb forms, collocations và ví dụ. Chỉ sau khi nhấn OK mới hiện countdown; khi tắt auto-next hoặc hủy timer, thao tác chuyển thủ công được mở.
- TTS: chọn voice nam/nữ từ voice tiếng Anh hiện có trên thiết bị; nghe thử và lưu URI theo nhóm. Có accent US/UK, rate, pitch, volume, word pause và turn pause. Đọc từ vựng từng headword với gap 900 ms mặc định; hội thoại đọc liền câu và nghỉ ở ranh giới lượt lời. Dừng hủy speech/timer.
- Flashcard: ảnh theo chủ đề nằm trong khung tỉ lệ ổn định; phần nghĩa/ví dụ cuộn trong khung nội dung; bỏ icon/emoji khỏi vùng ảnh, chỉ giữ icon nhỏ cạnh tiêu đề; thêm fallback khi ảnh lỗi.
- Từ điển: ALL/A–Z chuyển thành rail flex cuộn ngang; tăng khoảng cách, vùng chạm và giữ vị trí cuộn sau khi chọn chữ; typography và card responsive.
- Dữ liệu cá nhân: `personalVocabulary` schema v3 thêm `overrideBaseSigs`; migration lưu chữ ký baseline mà không ghi đè nội dung override; Import/Export giữ hoặc khởi tạo chữ ký này.
- Không thay đổi 928 bản ghi gốc, baseline ID, dữ liệu học cá nhân hiện có hoặc tiến độ học.

### Kiểm thử
- Validator: PASS — 928 record, 0 ERROR, 12 WARNING legacy.
- Version sync: PASS — toàn bộ marker 2.10.0 đồng bộ.
- `node --check`: PASS — `sw.js` và tất cả `assets/js/*.js`.
- `py_compile`: PASS — validator, sync-version và patch-data.
- Unit tests: PASS 69/69 khi chạy theo module/nhóm (13 + 11 + 12 + 33); không dùng kết quả một lần `unittest discover` bị treo làm bằng chứng.
- APP_SHELL: 65 mục, 0 file thiếu; ZIP CRC/integrity được xác nhận sau khi đóng gói và kiểm tra giải nén.
- Kiểm tra giao diện thực tế qua browser/thiết bị vật lý không được hoàn thành trong sandbox; iPhone Safari, Android Chrome và voice packs thực tế vẫn chờ nghiệm thu.

### Giới hạn TTS cần hiểu đúng
- Giới tính voice được ước lượng từ metadata/tên voice; người dùng có thể chọn thủ công nếu nhãn không đúng.
- Rate, pitch và volume chỉ điều khiển các thuộc tính Web Speech API hỗ trợ. Không có bộ lọc EQ/noise reduction; không thể cam kết chất giọng nam rõ như nhau trên mọi hệ điều hành.
- TTS là giọng hệ thống, không phải audio người thật hoặc audio ETS.

## Yêu cầu UX đã thống nhất cho v2.10.0 — không được bỏ khỏi phạm vi

**Trạng thái: ĐÃ TRIỂN KHAI trong mã nguồn v2.10.0; chưa được nghiệm thu trên thiết bị vật lý.** Các yêu cầu sau là tiêu chí thiết kế và QA; các thay đổi mã nguồn được ghi nhận tại mục “Phát triển v2.10.0” bên dưới.

### Ôn tập / Smart Review
- Cố định bố cục vùng câu hỏi và trả lời để nội dung thay đổi không làm khung nhảy hoặc vỡ giao diện.
- Sau khi trả lời, mở modal giải thích chi tiết: kết quả đúng/sai, đáp án, giải thích nghĩa/loại từ và phân tích các lựa chọn. Nút OK đóng modal và chuyển sang bước kế tiếp.
- Nếu `autoNextEnabled=true`, sau OK hiển thị modal chờ riêng với countdown, tiến trình và trạng thái loading, sau đó tự chuyển. Nếu tắt cấu hình hoặc người học hủy countdown, nút chuyển câu thủ công phải khả dụng. Không tự chuyển khi modal AI/giải thích còn mở.
- Tăng cỡ chữ theo thang responsive (`rem`/`clamp`), line-height và wrap phù hợp; không để tăng font gây tràn, chồng lấn hoặc đổi chiều rộng bất thường.

### Flashcard và ảnh minh họa
- Ảnh phải nằm trong khung cố định theo aspect ratio, có `object-fit: cover/contain` được chọn theo ảnh; không làm méo ảnh khi lật thẻ hoặc chuyển từ mặt tổng quan sang mặt chi tiết.
- Giữ kích thước/khung flashcard ổn định giữa mặt trước và mặt sau; phần nội dung chi tiết được cuộn bên trong khi cần, không làm bố cục nhảy.
- Ảnh chỉ đóng vai trò minh họa. Loại bỏ emoji/icon đặt giữa ảnh gây rối; icon chức năng/chủ đề chỉ nằm ở title hoặc nhãn nhỏ, không phủ lên trung tâm ảnh.

### Listening / giọng đọc
- Có danh sách voice đọc được trên thiết bị để người học tự chọn riêng giọng nam và giọng nữ; có nút nghe thử từng voice và lưu lựa chọn trên thiết bị.
- Không tự chọn voice nam đầu tiên theo tên như hiện tại. Ưu tiên voice English-US/English-UK rõ, natural/neural khi thiết bị có hỗ trợ; cho phép chọn voice khác nếu nhãn giới tính không chính xác.
- Bổ sung điều chỉnh tốc độ, âm lượng và pitch/tone trong giới hạn trình duyệt hỗ trợ. Giọng nam phải được nghe thử và lựa chọn rõ ràng; không tăng âm lượng bù cho voice bị ồm.
- Nhịp đọc tự nhiên: giữ speaker nhất quán trong một lượt thoại, có khoảng nghỉ hợp lý giữa lượt lời và giữa câu/ý; mặc định chậm rãi vừa phải, người học có thể chọn nhanh/chậm.
- Khi phát danh sách từ vựng liên tiếp, phải có khoảng nghỉ rõ giữa từng headword (mục tiêu mặc định khoảng 700–1.100 ms, có thể chỉnh); khi phát câu/hội thoại thì giữ ngữ điệu tự nhiên, chỉ ngắt ở ranh giới cụm/câu, không chèn khoảng nghỉ máy móc sau từng từ đơn.
- Khi một thẻ phát theo chuỗi “từ → nghĩa → ví dụ”, thêm khoảng ngắt ngắn giữa các phần để người học kịp tiếp nhận; nút dừng phải hủy cả speech hiện tại lẫn timer đang chờ.
- Nêu rõ voice/TTS phụ thuộc trình duyệt và hệ điều hành; iOS Safari, Android Chrome và desktop cần QA riêng. Không tuyên bố voice premium/neural có sẵn nếu thiết bị không cung cấp.

### Kho từ vựng / A–Z / responsive
- Căn lại ảnh minh họa trên thẻ từ, giữ cùng chiều cao và tỉ lệ; không stretch hoặc crop làm mất nội dung chính.
- Thanh ALL/A–Z phải có padding, gap và vùng chạm đủ rộng; không đặt sát chữ hoặc dính nhau trên màn hình hẹp. Cho phép cuộn ngang mượt mà và giữ trạng thái chữ đang chọn.
- Tăng cỡ chữ và cân bằng lại spacing trên desktop/mobile; mọi card, modal, menu và chuyển trang phải kiểm tra không overflow, không nhảy khung.

### Triển khai v2.10.0 — kết quả trong mã nguồn

- `assets/js/app.js`: modal review riêng; chặn đóng modal ngoài nút OK; countdown chỉ bắt đầu sau OK; manual-next khi auto-next tắt; lưu trạng thái review đang chờ để reload không bỏ qua giải thích.
- `assets/js/app.js`: voice discovery từ `speechSynthesis.getVoices()`, chọn URI riêng cho nhóm nam/nữ, preview từng nhóm, lưu cấu hình accent/rate/volume/pitch/word gap/turn gap trong IndexedDB; giữ cùng voice cho từng speaker trong suốt lượt thoại; dừng sẽ hủy speech và timer.
- `assets/js/app.js`: phát từng headword riêng trong thao tác “Đọc từ vựng chậm”; gap mặc định 900 ms, cấu hình 600–1300 ms. Hội thoại không bị tách thành từng từ, chỉ giữ ngắt ở ranh giới lượt lời.
- `index.html`: thêm cấu hình voice nam/nữ, nghe thử và các tùy chọn nhịp đọc trong trang Cấu hình.
- `assets/css/app.css`: kích thước chữ responsive, khung câu hỏi giữ chỗ, modal có vùng cuộn, Flashcard có khung ảnh/khung nội dung ổn định, A–Z rail dùng flex ngang có touch target rộng.
- `assets/js/app.js`: bỏ emoji giữa ảnh; icon chủ đề chỉ ở title; ảnh lỗi được ẩn và hiện placeholder; HTML ảnh chủ đề đã được sửa thẻ.
- `personalVocabulary` schema v3: `overrideBaseSigs` ghi chữ ký từ điển gốc cho từng override; migration từ schema cũ không thay đổi nội dung override. Import/export giữ chữ ký hoặc gán chữ ký baseline hiện tại cho tệp cũ.
- Không sửa `data/vocabulary/*.json`, không thêm/xóa/đổi ID, không đổi tiến độ học; validator vẫn 928 record, 0 ERROR, 12 WARNING legacy.

**Giới hạn còn lại:** Web Speech API chỉ dùng voice mà trình duyệt/hệ điều hành cung cấp. Chọn voice và pitch/rate không thể khử nhiễu, EQ hoặc biến một voice nam gốc kém rõ thành giọng thu âm chất lượng cao. Người học cần nghe thử các voice trên thiết bị đang dùng; iOS/Android/desktop chưa được nghiệm thu ở đợt này.

### Tiêu chí nghiệm thu v2.10.0
- Test modal giải thích đúng/sai, nút OK, auto-next bật/tắt, countdown bị hủy và chuyển thủ công.
- Test flashcard mặt trước/mặt sau, ảnh thiếu/lỗi, nội dung dài và màn hình nhỏ.
- Test tối thiểu 2 voice nam và 2 voice nữ khi thiết bị có cung cấp; chọn, preview, lưu, reload và phát lại đúng voice; kiểm tra speaker không đổi giọng giữa lượt; kiểm tra độ rõ, không bị ồm/ồn và khoảng nghỉ giữa từng headword trong danh sách cũng như giữa các cụm/câu trong hội thoại.
- Test kho từ A–Z ở desktop, iPhone Safari và Android Chrome; kiểm tra font tăng không làm vỡ giao diện.
- Không thay đổi dữ liệu học cá nhân; migration `baseSig` cho personal overrides vẫn nằm trong phạm vi v2.10.0 như đã chốt.

### Nhật ký mới
| Ngày | Phiên bản | Nội dung |
|---|---|---|
| 09/11/2026 | v2.9.9 working / Batch 001–004 | Hoàn tất 160 định nghĩa, 160 bản dịch và rà soát 160 ví dụ; mục tiêu DF002/DF003/DF004/EX004/EX005 về 0; validator 0 ERROR, 19 WARNING legacy; ZIP tổng v2.9.9 đã tạo và kiểm tra integrity. |
| 09/11/2026 | v2.9.10 | Hoàn tất 122 verb forms + 39 collocation lists, thêm VF001/VF002/FD003, giữ nguyên 928 ID và baseline; validator 0 ERROR/19 WARNING; ZIP v2.9.10 đã tạo, chưa deploy. |
| 09/11/2026 | v2.9.11 | Sửa 7 IPA lỗi, thêm 24 IPA theo Cambridge, cập nhật 49 word_family records, thêm 3 synonym cho competitor và gloss cho 2 term, sửa CEFR competitor A2→B1 có nguồn. Validator 0 ERROR/12 WARNING legacy; 928 ID giữ nguyên; ZIP tổng đã tạo, chưa deploy/QA thiết bị thật. |
| 09/11/2026 | v2.10.0 | Triển khai Smart Review modal/auto-next sau OK, responsive typography, khung Flashcard và ảnh không overlay icon, bộ chọn/nghe thử TTS nam-nữ, tốc độ/volume/pitch/pause, A–Z rail cuộn ngang, migration personalVocabulary schema v3/baseSig. 69/69 unit tests PASS; 928 ID giữ nguyên. Chưa deploy/QA thiết bị thật. |

## Phát triển v2.10.1 — Smart Review Wait Modal, Flashcard Laptop Layout & Daniel Voice Priority (09/11/2026)

**Trạng thái:** Đã hoàn tất mã nguồn, đồng bộ version marker và đóng gói ZIP v2.10.1. Chưa deploy GitHub Pages hoặc QA trực tiếp trên thiết bị thật.

### Thay đổi đã thực hiện
- Smart Review: sau khi nhấn OK, nếu bật tự chuyển thì giữ modal chờ riêng trên màn hình, hiển thị vòng đếm, tiến trình, nội dung trạng thái và nút “Giữ câu này · Chuyển thủ công”. Modal không đóng bằng backdrop/Escape trong lúc chờ; hủy countdown sẽ đóng modal và bật nút Next. Khi tắt tự động ngay từ cấu hình, modal chờ được đóng và chuyển câu thủ công khả dụng.
- Khôi phục trạng thái chờ qua reload: `practiceSession.autoAdvanceWaiting` ghi lại trạng thái đã bấm OK nhưng chưa chuyển câu; khi tải lại, ứng dụng dựng lại wait modal và chạy countdown mới thay vì tự bỏ qua bước chờ. Thời lượng của vòng tiến trình được đồng bộ đúng với cấu hình 3/5/10 giây, tránh vòng chạy nhanh hơn bộ đếm.
- Flashcard: sử dụng `min-width:0`, `max-width:100%`, tỷ lệ ảnh cố định và `object-fit:contain`; nội dung dài cuộn trong panel; chuyển sang bố cục dọc khi khung flashcard thực tế hẹp (container query) hoặc viewport laptop không đủ. Topic grid giảm số cột theo chiều rộng.
- TTS: nếu chưa lưu voice nam thủ công và hệ điều hành cung cấp voice tên Daniel, ưu tiên `Daniel — en-GB` làm fallback nam theo phản hồi nghe thực tế của người dùng. URI do người dùng chọn luôn có ưu tiên cao nhất. `utterance.lang` dùng locale của voice thực sự được chọn. Không thay đổi mặc định giọng nữ.
- Cấu hình và ghi chú làm rõ Daniel là voice gợi ý khi thiết bị cung cấp; rate/pitch/volume không khử nhiễu hoặc thay thế voice gốc.
- Không sửa dữ liệu vocabulary, ID, schema `personalVocabulary` hoặc tiến độ học trong release này.

### Kiểm định
- `python tools/validate-data.py`: PASS — 928 records, 0 ERROR, 12 cảnh báo legacy (DF005=3, EX006=1, FD001=8 trên 7 hồ sơ).
- `node --check assets/js/app.js` và `node --check sw.js`: PASS; `py_compile`: PASS.
- Baseline IDs + patch engine: 24/24 PASS. Version sync: 12/12 PASS. Tổng 36/36 ca unit test đã xác nhận trong patch run. Validator CLI: PASS — 928 record, 0 ERROR, 12 cảnh báo legacy. Validator unit suite 33 ca không chạy lại toàn bộ trong lượt này; mã validator không thay đổi so với v2.10.0 (bản trước đã ghi nhận 33/33 PASS).
- HTML: 201 ID duy nhất; CSS/JS assertions cho wait modal, cancel, restore countdown duration, Daniel en-GB, locale và responsive Flashcard đều PASS; APP_SHELL 65/65 tài nguyên tồn tại. ZIP 112 files: `testzip()` PASS; sau giải nén, version sync, validator, JS syntax và Python compile tiếp tục PASS. Dữ liệu nội dung `data/` ngoài manifest version byte-identical với v2.10.0; 928 ID và baseline giữ nguyên.
- Headless Chromium bị môi trường chặn khi mở localhost (`ERR_BLOCKED_BY_ADMINISTRATOR`), do đó không ghi nhận visual regression/browser interaction là PASS. QA iPhone/Android/PC thật vẫn chờ.
- Chưa có bằng chứng visual regression trên trình duyệt thật, chưa QA iPhone Safari, Android Chrome và laptop/PC vật lý. Voice Daniel chỉ được ưu tiên nếu hệ điều hành của thiết bị hiện tại trả về voice phù hợp.

### Bước kế tiếp theo lộ trình
1. Nghiệm thu modal chờ, hủy countdown và manual next trên desktop/mobile; kiểm tra restore khi reload.
2. Nghiệm thu layout Flashcard tại chiều rộng desktop/laptop phổ biến, zoom 80–125%, nội dung dài và ảnh lỗi.
3. Trên iPhone, kiểm tra Daniel — en-GB, nữ mặc định, lưu lựa chọn và phát hội thoại nhiều speaker.
4. v2.10.2 đã triển khai Lexical Audit Batch 002 (11 IPA có nguồn + 9 Word Family operations). Tiếp theo là Batch 003, ưu tiên IPA có nguồn và lexical relations/gloss theo sense; song song chuẩn bị Listening Part 1 sau đợt audit.

### Nhật ký cập nhật bổ sung
| Ngày | Phiên bản | Nội dung |
|---|---|---|
| 09/11/2026 | v2.10.1 | Chuyển countdown sau OK vào modal chờ có loading và nút hủy; chống tràn Flashcard laptop bằng layout tự xếp dọc; ưu tiên Daniel en-GB làm male fallback khi thiết bị cung cấp; sửa tiến trình countdown khi khôi phục phiên; giữ nguyên 928 bản ghi gốc và dữ liệu cá nhân. |


## Phát triển v2.10.2 — Lexical Audit Batch 002 & Documentation Consolidation (09/11/2026)

**Trạng thái:** Đã áp dụng patch IPA/Word Family, đồng bộ tài liệu vào `docs/`, cập nhật version tooling/test/CI và chạy kiểm tra cục bộ. ZIP tổng đã tạo sau khi kiểm thử. Chưa commit/push, chưa deploy GitHub Pages, chưa xác nhận GitHub Actions hoặc QA trực tiếp trên thiết bị thật.

### Batch dữ liệu đã áp dụng
- IPA: thêm 11 phiên âm US theo Cambridge Dictionary cho `absence`, `absorb`, `accommodate`, `accountant`, `accounting`, `accurate`, `activate`, `additional`, `adequate`, `adjacent`, `administration`. Coverage tăng 563 → 574/928.
- Word Family: thêm 9 JSON Pointer operations trên 9 hồ sơ hiện có, nối các cặp/nhóm `accommodate/accommodation`, `accountant/accounting`, `administration/administrative/administrator`, `annual/annually`. Coverage tăng 122 → 131/928. Chỉ liên kết headword hiện có trong dữ liệu; không tạo mục từ mới.
- Patch files: `patches/v2.10.2/batch-001-ipa.json` (11 operations) và `batch-002-word-family.json` (9 operations); cả hai dry-run PASS trước khi apply, khóa base `2.10.1`, target `2.10.2`, SHA-256 tập ID và `expect.old`.
- Giữ nguyên 928 ID, 26 tệp A–Z, 32 chủ đề, verb_forms=291, collocations=758, synonyms=361, antonyms=213. Không cập nhật CEFR khi không có căn cứ cho từng sense.

### Gom và chuẩn hóa tài liệu Markdown
- Đã chuyển toàn bộ 19 file `.md` hiện hữu vào `docs/`; root dự án không còn Markdown rải rác.
- `docs/MASTER_STATUS.md` là Master duy nhất; `docs/README.md` là chỉ mục; `docs/CHANGELOG.md` là changelog. Báo cáo cũ nằm trong `docs/reports/`, báo cáo vocabulary batch trong `docs/batches/`, nguồn trong `docs/sources/`.
- Cập nhật `tools/sync-version.py` để kiểm tra marker `docs/README.md`, `docs/MASTER_STATUS.md`, `docs/CHANGELOG.md`; cập nhật fixtures của `test_sync_version.py`; workflow GitHub Actions theo dõi `docs/**`.
- Bổ sung dashboard workstream, quyết định từ kế hoạch Claude + ChatGPT đã ghi nhận, thứ tự triển khai, tiêu chí Phase 5/6 và quy ước quản lý tài liệu.

### Kiểm định sau batch
- `python tools/validate-data.py`: PASS — 928 records, 0 ERROR, 12 cảnh báo legacy (DF005=3, EX006=1, FD001=8 vi phạm/7 hồ sơ).
- `python tools/sync-version.py --check`: PASS — marker 2.10.2 ở manifest, Service Worker, index và tài liệu đều đồng bộ.
- `py_compile`, unit tests baseline/patch/version-sync/validator, JavaScript syntax, workflow YAML, ZIP integrity và re-check sau giải nén được ghi chi tiết trong `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.10.2.md`.
- APP_SHELL không được đưa thêm tài liệu docs vào cache; mã nguồn tiếp tục dùng `index.html`, CSS/JS và JSON như trước.
- Unit tests: baseline IDs 13/13, patch engine 11/11, version sync 12/12, validator 33/33 — tổng 69/69 PASS theo module/nhóm và test case riêng. Bộ validator group bị timeout sau 23 ca; 10 ca cuối được chạy riêng, gồm ca timeout, và đều PASS. Không tuyên bố một lần `unittest discover` nguyên khối đã PASS.
- Remote CI, GitHub Pages deployment, visual regression trên browser thực và QA iPhone/Android/PC thật vẫn chưa được thực hiện.

### Bước kế tiếp
1. v2.10.3 / Lexical Audit Batch 003: ưu tiên các IPA còn thiếu theo nguồn, tiếp tục word family nếu có headword liên quan; bắt đầu audit synonym/antonym và `related-terms` theo sense, không dùng gloss suy diễn.
2. Bổ sung báo cáo coverage theo CEFR/topic/POS và tỷ lệ trường có căn cứ; không chỉ theo một tỷ lệ tổng.
3. Sau Batch dữ liệu, bắt đầu Listening Part 1 và tăng Part 2–4 theo lộ trình.
4. QA các yêu cầu UX v2.10.1/v2.10.2 trên máy thật trước khi coi Phase 5 hoàn tất.

### Nhật ký
| Ngày | Phiên bản | Nội dung |
|---|---|---|
| 09/11/2026 | v2.10.2 | Thêm 11 IPA, 9 Word Family operations; gom toàn bộ Markdown vào `docs/`; duy trì một Master duy nhất và cập nhật version sync/tests/CI. Validator 0 ERROR/12 WARNING; 928 ID giữ nguyên. |


## Phát triển v2.11.0 — TOEIC-only coverage expansion & content operations (09/11/2026)

**Trạng thái:** Release candidate; code/data/docs/test đã đóng gói và kiểm tra tại môi trường làm việc. Chưa commit/push, chưa GitHub Actions từ xa, chưa deploy GitHub Pages và chưa QA thiết bị vật lý.

### Quyết định phạm vi
- User quyết định tập trung 100% TOEIC trước; IELTS/Academic bị hoãn cho đến khi toàn bộ TOEIC acceptance gates ở phần đầu Master hoàn thành và user phê duyệt.
- Benchmark app khác chỉ dùng nguồn công khai của nhà phát triển/nhà xuất bản và trang chính thức; không coi tính năng tự công bố là đánh giá chất lượng độc lập.

### Nội dung đã bổ sung
- Listening: 8 Part 1 image-description units; tổng 22 units / 36 questions (P1=8, P2=2, P3=18, P4=8 questions).
- Reading: 27 resources / 77 questions (P5=16, P6=12, P7=49); chuẩn hóa `part`, `documentType`, nguồn biên tập và câu hỏi/đáp án/giải thích.
- Grammar: 25 lessons / 54 exercises.
- Vocabulary: 6 IPA US bổ sung qua `patches/v2.11.0/batch-001-ipa.json`; tổng IPA 580/928; các ID khác giữ nguyên.
- Dashboard tiến độ theo Part; lọc Reading theo Part 5/6/7; Listening Part 1 có hình và 4 lựa chọn đọc bằng TTS.
- 8 SVG Part 1 trở thành required offline assets; APP_SHELL được kiểm tra thực tế có 73 resources (46 required + 27 optional), không thiếu file.
- Thêm `tools/validate-learning-content.py`, `tools/audit-toeic-coverage.py`, `tools/tests/test_learning_content.py`; workflow CI chạy cả data validator, learning validator và coverage audit.
- Thêm `docs/CONTENT_OPERATIONS.md`, benchmark competitor, source notes, batch report, coverage report và test report.

### Giới hạn cần nói rõ
- Part 1 hiện dùng SVG illustrations, không phải ảnh chụp chân thực; browser TTS không phải audio thu âm và không phải audio ETS.
- Listening hiện 36/100 câu, Reading 77/100 câu; không có kho đề full-test 200 câu và không có score equating.
- 928 headwords còn là nền tảng, chưa đạt mục tiêu planning 3,000–5,000 TOEIC headwords; IPA coverage 62.5%, word-family 14.1%; các trường khác không được tự lấp khi chưa có nguồn.
- Per-Part analytics là dựa trên lượt làm tại thiết bị/local data, không có server sync.

### Kiểm thử release candidate
- `validate-data.py`: PASS — 928 records, 0 ERROR, 12 legacy warnings (DF005=3, EX006=1, FD001=8 trên 7 hồ sơ); không phát sinh debt mới.
- `validate-learning-content.py`: PASS — Listening 22 units/36 questions, Reading 27 resources/77 questions, Grammar 25 lessons/54 exercises; 0 ERROR / 0 WARNING.
- `audit-toeic-coverage.py`: PASS — cập nhật `docs/reports/TOEIC_CONTENT_COVERAGE_v2.11.0.md`; 928 headwords, IPA 580, Word Family 131.
- Unit tests: 82/82 PASS — baseline IDs 13 (module), patch engine 11 (module), version-sync 12 (từng ca độc lập), validator 33 (từng ca độc lập), learning content 13 (module). Các suite sync-version và validator bị giới hạn thời gian khi chạy gộp trong sandbox Python 3.13.5; từng test method đã được chạy riêng và đều PASS. Không tuyên bố một lần `unittest discover` tổng hợp duy nhất đã PASS.
- `py_compile`: PASS cho 5 công cụ Python; `node --check assets/js/app.js` và `node --check sw.js`: PASS; version sync 2.11.0: PASS; workflow YAML parse: PASS.
- HTML: 206 ID, không trùng. Service Worker: 73 tài nguyên (46 required + 27 optional), 0 thiếu. Tất cả Markdown dự án được gom trong `docs/`, không còn `.md` ở root.
- ZIP integrity (`testzip`) PASS; 136 tệp trong archive đã được giải nén và đối chiếu với working tree sạch sau khi loại `__pycache__`; không còn khác biệt. Validators và version sync được chạy trên chính thư mục giải nén. Remote GitHub Actions, deploy GitHub Pages, visual QA và thiết bị vật lý vẫn chưa xác minh.
