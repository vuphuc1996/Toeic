# TOEIC DICTIONARY — MASTER STATUS

> **Nguồn trạng thái và lộ trình duy nhất.** Mọi release cập nhật trực tiếp file này. `CHANGELOG.md` là log phát hành; `archive/PROJECT_HISTORY.md` lưu lịch sử đã chỉnh lý; `COMPATIBILITY.md` là sổ tương thích duy nhất.

- **Ngày kiểm kê:** 2026-11-16.
- **Phiên bản mã nguồn đang kiểm kê:** v2.84.1 — Robot Buddy Learning Insights & Knowledge Expansion.
- **Product source:** GitHub Pages static PWA; GitHub-only, không có backend riêng cho Robot.
- **Robot Buddy:** đầu Robot SVG, biểu cảm/animation; giữ nguyên 500 câu hội thoại offline, 59 lời hướng dẫn tính năng cho 12 đích đến (11 khu vực menu và Placement), 6 FAQ và 16 quick prompts. “Bạn là ai?” giới thiệu Robot được tạo bởi nhà phát triển Vũ Nguyễn Hoàng Phúc.
- **Learning Insights:** Robot có thể nhận snapshot tiến độ local đã được ứng dụng nạp sẵn để phân loại Cần học / Cần luyện / Cần ôn. Cần học = bài/mục chưa có bằng chứng hoàn thành; Cần luyện = theo ngưỡng bằng chứng của từng module (Từ vựng ≥3 lượt, Flashcard ≥3 câu quiz, Grammar/Reading/Listening ≥5 câu, Foundation ≥3 mục độc lập, Mock theo kết quả bài hoàn thành); Cần ôn = lịch ôn từ vựng/Flashcard, recall Objective và Foundation đã đến hạn. Robot có thể liệt kê tối đa 5 nội dung mẫu trong mỗi nhóm để người học mở tiếp. Dữ liệu ít được báo chưa đủ bằng chứng, không kết luận kỹ năng yếu.
- **Read-only boundary:** Robot không tự mở IndexedDB/LocalStorage. Ứng dụng chỉ truyền snapshot trong bộ nhớ từ các kho hiện hữu; aggregator thuần không sửa dữ liệu. Tắt Learning Insights không ảnh hưởng hội thoại/hướng dẫn. Không gửi tiến độ tới API, server, Google AI hoặc bên thứ ba.
- **Preservation:** IndexedDB vẫn schema v1; giữ nguyên các key `studyProgress`, `flashProgress`, `grammarProgress`, `readingProgress`, `listeningProgress`, Foundation localStorage và Mock history. Không migration, overwrite hoặc delete progress trong release này.
- **SW / offline shell:** `assets/js/robot-buddy.js`, `assets/js/robot-learning-insights.js`, `data/robot/robot-library.json` nằm trong `REQUIRED` và `APP_SHELL`; cache version 2.84.1.
- **Local release gates:** PASS — 29/29 JavaScript suites; 56/56 selected Python tests across the CI/version/layout/design/project-status checks; vocabulary validator 0 ERROR/0 WARNING; learning-content validator 0 errors/0 warnings; 11/11 objective map; 294/294 resource links; question/distractor/photo audits PASS; version sync PASS. Full Python unittest discovery and the standalone `test_validator` did not finish within the 300-second execution window and are not counted as PASS. Details in `reports/TEST_REPORT_TOEIC_Dictionary_v2.84.1.md`.
- **Release QA still pending:** push GitHub, GitHub Actions, Pages production, browser visual QA, desktop 15.6-inch at 100% zoom and mobile/iOS/Android.
- **Previous release:** v2.84.0.

## v2.84.1 changes — Robot Buddy Learning Insights & Knowledge Expansion

- Restored evidence-based local learning insights with the categories learn, practice and due review.
- Replaced the v2.84.0 statement that Robot never reads learning progress. Current behavior is opt-in/read-only and local-only.
- Added explicit privacy toggle, developer identity response, updated quick prompts and menu guidance for all 11 actual menu areas plus Placement. The home overview includes learning statistics; there is no separate Statistics navigation item in this release.
- Kept offline dialogue library, head-only robot, idle safeguards, first-run Placement choice and feature-level Google AI actions separate.
- No changes to vocabulary corpus, learning content, test banks, Placement/Mock logic, TTS, IndexedDB v1 or progress storage formats.

## v2.84.0 changes — Head-only Robot Buddy & Offline Interaction Library

- Replaced the progress-aware companion with one head-only SVG mascot. Added emotion states `happy`, `thinking`, `celebrate`, `caring`, `sleepy`, `greeting`, `surprised`, `motivation`, `concerned`, `playful`, `listening` and `speaking`; eye, pupil, mouth, antenna and floating/micro-animation states respect `prefers-reduced-motion`.
- Added `data/robot/robot-library.json`: 500 unique local dialogue lines across seven core groups (greeting 60, encouragement 100, caring 60, learning 80, help 100, reaction 60, rest 40), plus feature help for 11 destinations, FAQs and 12 quick prompts.
- Added keyword-only local intent matching and feature routing. Free text is handled only by the pre-authored intent groups; unknown messages receive an explicit limitation response. No hosted LLM, Google AI, API, server, learner progress, IndexedDB or learning localStorage is used by Robot Buddy.
- Added idle prompts after 90 seconds, then a 5-minute / 10-minute cadence, maximum 3 notices per rolling hour; notice auto-dismiss, 10-minute snooze and mute control. No prompts during timed Mock Exam, active learning-focus/modal, typing, speech playback, hidden tab or unfocused window.
- First-run onboarding asks whether to open the existing Placement Diagnostic or skip. The Robot records only that choice and the mute preference in `toeic:robot-buddy-settings:v1`. Placement is opened by explicit user action; Robot does not read the Placement result.
- Chat messages are rendered as text nodes and kept only in current memory session. No chat transcript persistence. Existing Google AI feature-level actions remain unchanged and independent.
- Retired the v2.83 progress-reader implementation; `assets/js/learning-assistant.js` is a compatibility tombstone. `assets/js/quick-help.js` remains a compatibility tombstone. Both stay in the cache shell along with the new Robot runtime and static JSON library.
- No vocabulary, question-bank, learning content, IndexedDB schema, progress key, Foundation evidence, A2 portfolio or Mock Exam engine changes.

## AI and Robot product contract — current

- **Google AI:** preserve the existing v2.79 user-initiated feature-level Google AI actions for Vocabulary/term, Practice answer/review, Grammar, Reading and Listening. These remain separate from Robot Buddy.
- **Robot Buddy:** a static, scripted, offline companion. It can greet, encourage, answer supported feature-navigation questions, show FAQs, and proactively ask whether the user needs help. It does not understand unrestricted natural language, learn from activity, analyze ability, monitor scores or summarize learner progress.
- **No learner-data connection:** Robot Buddy must not import progress readers, subscribe to score/result events, access IndexedDB, inspect learner localStorage keys, or use personal vocabulary/Placement/Mock data. Only the Robot's own onboarding/mute preferences may be persisted.
- **No external AI:** no API, remote model, server, external transfer, analytics or hidden data upload. Do not describe the local keyword/dialogue engine as realtime generative AI. Its responses are selected locally from the bundled content library.
- **Idle safeguards:** respect the published timers, rate limits, mute/snooze, reduced motion and suppression conditions. Never cover or interrupt practice, audio, modals or timed Mock Exam.
- **Historical correction (as of v2.84.0):** v2.83.0 had a progress-aware Robot implementation. v2.84.1 intentionally restores a safer opt-in, read-only local insights path. The old v2.83 behavior remains only as release history, not current product scope.

## v2.83.0 historical — progress-aware Robot Buddy (superseded in v2.84.0)

- Replaced the Quick Help headset launcher with the SVG robot icon. The panel no longer contains an in-app usage guide or vocabulary prefix/letter-completion search.
- On a device with no recorded learning footprint and no onboarding decision, Robot Buddy opens once and asks whether the learner wants the existing Placement Diagnostic. Choosing to start opens the existing diagnostic; choosing to skip records that choice and lets the learner begin normally. A returning learner is detected from existing local learning evidence and is not shown the first-run prompt again.
- Robot Buddy reads existing vocabulary, Flashcard, Grammar, Reading, Listening, Foundation, A2 writing portfolio, Placement and Mock Exam progress. It celebrates verified milestones, summarizes available progress, identifies a Reading/Listening Part only after at least three unique questions have answers, and offers direct actions to relevant existing review surfaces. It does not claim skill weakness from one or two answers or combine different A2 rubrics into a fake total score.
- Added animation for launcher/avatar/panel/message/action cards, a compact mobile/tablet layout, independent panel scrolling, safe positioning above mobile navigation and `prefers-reduced-motion` support. Robot is hidden during a timed Mock Exam.
- `assets/js/learning-assistant.js` is deterministic, read-only aggregation over existing local progress; it makes no network/API/Google call. Legacy v2.79 per-feature Google AI preview/actions remain separately available at their original feature entry points.
- `assets/js/quick-help.js` remains as a no-op compatibility tombstone so updating an older GitHub checkout does not leave a stale Quick Help script active. Both JS files are registered in Service Worker `REQUIRED` and `APP_SHELL`, fixing SW002 for these assets. Cache version is bumped to 2.83.0.
- Removed all Quick Help usage-guide markup/actions and the former prefix/masked-letter word search; no vocabulary records are added or fabricated.
- The only new localStorage key is `toeic:robot-companion-onboarding:v1`. Existing vocabulary, Foundation/Reading/Listening progress, A2 revision history, IndexedDB v1 and stable question IDs are unchanged.
- Consolidated the AI rules into the single authoritative contract below; old implementation regressions are recorded only as corrections, not accepted product features.

## AI product contract — corrected and authoritative

- **Google AI:** chỉ giữ các thao tác Google AI theo từng chức năng đã có từ v2.79.0: tra cứu từ vựng/term, phân tích đáp án và ôn tập, Grammar, Reading và Listening. Đây là luồng do người học chủ động mở, có preview/xác nhận rồi chuyển sang Google; không phải chatbot nằm trong ứng dụng.
- **Robot Buddy:** là logic tất định chạy tại thiết bị, đọc tiến độ local hiện có để chúc mừng, tổng hợp và gợi ý ôn tập. Robot không sinh câu trả lời bằng mô hình, không gọi Google/API/backend và không chuyển lịch sử học ra ngoài.
- **Không thuộc phạm vi sản phẩm:** trợ lý AI nổi dùng chung, prompt theo ngữ cảnh trang, hội thoại tiếp nối hoặc cơ chế copy/transfer nội dung sang AI. Không thêm các luồng này vào Robot Buddy hay Quick Help.
- **Lịch sử sửa sai:** một lần triển khai v2.81 đã vô tình ẩn một số nút Google AI có trước; v2.82 khôi phục đúng các nút v2.79. Đây là lỗi tương thích đã sửa, không phải thay đổi chủ trương loại bỏ AI.

## v2.82.1 historical — remove Quick Help word search

- Removed prefix-based search, suggestions, masked-letter completion and exact-word lookup from Quick Help.
- Preserved the existing feature-level Google AI actions, A2 writing portfolio and Mock Exam SVG icons.
- The remaining usage guide was subsequently replaced by Robot Buddy in v2.83.0.

## v2.82.0 historical — restore existing feature-level actions

- Restored the original v2.79 feature-level Google AI actions after a temporary implementation regression in v2.81.0.
- Preserved the A2 writing portfolio, response revision history and Mock Exam SVG icons.
- No shared assistant, page-context prompt, follow-up conversation or copy/transfer AI flow was added.

## v2.81.0 historical — A2 writing portfolio

- Added the A2 writing portfolio using existing `productionEvidence` and `toeic:foundation-progress:v1`.
- A temporary regression hid some pre-existing Google AI entry points; v2.82.0 restored the original v2.79 behavior. Do not treat that temporary state as the product contract.

## v2.80.0 historical — Mock Exam icon refresh

- Retained the Mock Exam SVG icon family: clipboard/check, bolt, stopwatch and trophy.
- No shared AI assistant or contextual AI handoff is part of the accepted v2.80 product scope.
- The original feature-level Google AI actions predate v2.80 and remain governed by the v2.79 feature contract.

## v2.79.0 changes — A2 guided writing revision and response history

- Detailed implementation contract: `archive/PROJECT_HISTORY.md`.
- Automated verification: `archive/PROJECT_HISTORY.md` (historical v2.79 test summary).

- Added a task-specific guided revision workspace to all 13 A2 contextual production tasks. Each has three topic-specific review checks and a tailored hint; learners compare the previous version, confirm each check, rewrite and self-rate the three existing criteria.
- New production attempt rows retain response text. Each guided revision stores `basedOnResponse`, revised `response`, three review confirmations, three self-ratings, word count and timestamp. Identical text, fewer than eight words, incomplete review confirmations or missing self-ratings are rejected.
- First and revised versions stay in the existing `productionEvidence` map under `toeic:foundation-progress:v1`. Existing `::produce1` task IDs and legacy `::apply1` records remain separate. No localStorage key or IndexedDB v1 schema migration is introduced.
- Historical v2.78.0 attempt rows did not store response text; they are preserved without fabricated backfill. The last currently stored response serves as the next revision's comparison source.
- A versioned SHA-256 baseline covers all 13 revision guides. Dedicated Python and JavaScript regressions verify multi-revision chaining, data isolation and validation gates.
- No automatic AI/grammar grading, backend upload, vocabulary/Reading/Listening content change or progress reset. Self-ratings are not mastery or CEFR evidence.
- Remote GitHub Actions, Pages deployment, independent review and physical-device QA remain unverified.

## v2.78.0 changes — A2 contextual writing and production evidence

- Added 13 task-specific A2 writing prompts. Each has a distinct workplace scenario, clear instruction, three task requirements, a sentence frame, customized three-point learner self-review and a collapsed model-answer example.
- The response field now shows a live word count and requires at least 8 words for A2; older Pre-A1/A1 production retains the prior three-word minimum and fallback rubric.
- Added unique `::produce1` IDs separate from the existing A2 `::apply1` application task IDs. Both use the existing `productionEvidence` map inside `toeic:foundation-progress:v1`; the current A2 outcome summary reads the new production ID, while old records remain untouched and are explicitly explained in the UI.
- The new task content is protected by `tools/foundation-a2-production-baseline-v2.78.0.json` SHA-256 hashes. Regression tests cover all 13 task contracts, model-answer feature checks, minimum-word validation, self-report aggregation, and legacy evidence preservation.
- Foundation task count remains 23 lessons; Reading remains 23 passages / 59 questions; Listening remains 23 clips / 59 questions. No vocabulary, question bank, IndexedDB, storage key, profile or Mock-pool changes.
- Production ratings remain learner self-report, not automated assessment or mastery. Remote Actions/Pages and physical-device testing remain unverified.

## v2.77.0 changes — A2 assessment quality and source evidence

- Reviewed the A2 question sets for within-resource q2/q3 repetition. Revised five question prompts/answer tasks: Reading quantities, comparisons and visitor obligations; Listening comparison and process sequencing. This improves information coverage without adding arbitrary questions or changing the three-question A2 bank size.
- Added exact `evidenceText` pointers to five reviewed questions. Each pointer must occur in the source reading passage or spoken listening segment and is recorded in `tools/foundation-a2-assessment-review-v2.77.0.json`.
- Added a dedicated quality audit for the 26 A2 resources / 78 question records: four unique options, valid answer key, non-empty prompt/rationale, distinct q2/q3 correct information, source-evidence integrity and balanced full-bank answer positions.
- **Preservation:** all pre-existing A2 q1/q2 question objects remain identical to the v2.75.0 canonical baseline; A2/Pre-A1/A1 IDs and progress storage, 23 Foundation lessons, 23 Reading / 59 questions, 23 Listening / 59 questions, 67% A2 practice threshold and configured multi-speaker SpeechSynthesis remain unchanged.
- Local review: focused A2 quality audit and 8/8 dedicated tests PASS. Broader local test and validator counts are recorded in `archive/PROJECT_HISTORY.md`.
- **Boundary:** this is a focused internal single-author review, not complete distractor certification, independent second-person review, psychometric validation or CEFR/ETS mastery. Remote GitHub Actions, Pages deployment and physical-device QA remain unverified.

## v2.76.0 changes — A2 Reading & Listening depth

- Expanded all 13 A2 Reading passages to **69–80 words** and added one third distinct comprehension question to each. The previous A2 q1/q2 question objects are protected by the exact v2.75.0 baseline hashes; all 10 Pre-A1/A1 passages remain unchanged.
- Expanded all 13 A2 Listening resources to **four dialogue turns**, with two female and two male speaker turns; added a third question per dialogue. Playback uses saved/configured device voice selections, the existing configurable `sentencePauseMs`, turn status and Stop control. Older scripts that do not have explicit `segments` continue through sentence-splitting fallback.
- Reading and Listening now each contain **23 resources / 59 questions**: Pre-A1/A1 remains 10 resources / 20 questions; A2 is 13 resources / 39 questions. A2 has a minimum of 3 unique questions and a local practice threshold of 67%; legacy levels remain 2 / 80%. Neither threshold is an external proficiency standard or proof of mastery.
- Answer positions are balanced across each full Foundation Reading/Listening bank (A/B/C/D = 15/15/15/14). No new audio asset, runtime dependency, IndexedDB migration or learner-data reset was introduced. Existing TOEIC L&R bank counts are separate and unchanged.
- Foundation lesson position labels now use the level-specific denominator (A2 x/13; combined Pre-A1/A1 x/10). Path cards now use the resource-specific Reading/Listening question totals and thresholds rather than a hard-coded two-question display.
- Local validation: **139 selected Python tests across 19 fully executed modules and 22/22 JavaScript regression suites PASS**; Python compile 62/62; JavaScript syntax 12/12 plus `sw.js`; data validator 1,137 records / 0 errors / 0 warnings; learning-content 0 errors / 0 warnings; Part 1 photos 9/9; resource map 294/294; outcome audit 11/11 objectives / 33 criteria / 6 evidence paths; design and version sync PASS.
- Remote GitHub Actions, Pages deployment, independent A2 language review and physical iOS/Android/desktop QA remain unverified.

## v2.75.0 changes — A2 core grammar expansion

- Expanded A2 from 10 to **13 stable guided lessons** by adding Present Perfect for current results/experience (`have/has + V3`, already/yet/ever), basic Passive Voice (`am/is/are/was/were + V3`) and defining Relative Clauses (`who/which/that`). Each new lesson includes an objective, Vietnamese-supported explanation, bilingual examples, usage tip, three stable recognition questions with rationales and one separate contextual application task.
- Added one aligned short Reading passage (two questions) and one device-TTS Listening script (two questions) for each new lesson. Foundation Reading and Listening inventories now each contain 23 resources / 46 questions. The new listening content remains SpeechSynthesis, not recorded or ETS audio.
- Expanded the `foundation-a2` lesson mapping from 10/10 to 13/13; canonical objective-resource coverage is now **294/294** across 11 objectives. A2 content is kept in the existing Foundation resource files; no parallel data store was introduced.
- New A2 answer-position distributions remain balanced: recognition A/B/C/D = 10/10/9/10; contextual application = 4/3/3/3; Reading = 7/7/6/6; Listening = 6/6/7/7. Legacy Pre-A1/A1/A2 lesson IDs, prior question IDs, answer keys, passage/script IDs and progress records remain unchanged.
- No vocabulary records, IndexedDB schema/store, localStorage key, profile, learner progress or TTS settings were reset or migrated. New data is additive; existing Foundation outcome evidence and its 1/3-day delayed-recall behavior are preserved. A direct v2.74.0 archive comparison passed 52/52 checks across prior Foundation records, objective mappings, outcome registry, vocabulary files/batches and Part 1 JPG assets.
- **Content boundary:** the A2 starter now covers the three named grammar topics at introductory level; this does not mean the entire A2 curriculum is finished. Longer/more varied texts, broader independent application, and independent linguistic/editorial review remain open. The A2 objective remains `content_exists_review_depth_required`; no CEFR mastery or formal completion claim is made.
- **Local validation:** 131 selected Python tests across 19 fully executed modules and 22/22 JavaScript regression suites PASS; data validator 1,137 records / 0 errors / 0 warnings; learning-content validator 0 errors / 0 warnings; Part 1 photos 9/9; objective-resource map 294/294; outcome audit 11/11 objectives / 33 criteria / 6 evidence paths; design-profile and version sync PASS.
- Tests and release checks: see `archive/PROJECT_HISTORY.md` (tài liệu release cũ đã được gom vào lịch sử). Remote GitHub Actions, Pages deployment and physical-device QA are not inferred from local checks.

## v2.74.0 changes — Foundation outcome evidence, learner production and delayed recall

- Added an additive Foundation evidence layer on the existing `toeic:foundation-progress:v1` localStorage contract. No IndexedDB version/store change, no new database and no reset or migration of existing learner progress.
- Recognition keeps the stable three-question-per-lesson bank and latest-result-per-question denominator. The first recorded recognition attempt schedules a due recall 24 hours later; an answer before due time is rejected without adding evidence.
- Delayed recall is tracked separately from recognition attempts. A correct due recall schedules the next interval at 3 days; an incorrect due recall schedules 1 day. The due queue uses stable lesson/question IDs and cannot inflate the recognition denominator.
- Added learner-authored sentence production with three explicit self-report checks: explain why the target structure fits the intended meaning; explain why an alternative does not fit; and produce a new sentence in context. Text and ratings are saved locally; there is no automated grammar grading. This is learner self-report, not independently assessed skill.
- Added separate Pre-A1/A1 and A2 outcome views for recognition, production/explanation and delayed recall. The outcome registry now identifies 6/33 criteria (18.2%) with evidence-collection paths; all six Foundation outcomes are wired (6/6). Instrumentation coverage does not mean learner completion, skill mastery, CEFR alignment or ETS certification.
- Preserved A2 content, 1,137 canonical headwords, 291 resource links, 33 criteria, existing Reading/Listening/Grammar practice and nine optimized Part 1 photos. No vocabulary or question IDs were replaced.
- Synchronized generated design typography from the canonical design profile (54 tokens; 363 legacy font-floor groups).
- Validation: 22/22 JavaScript regression suites; 129 selected Python tests across 19 fully executed modules; data validator 1,137 records / 0 errors / 0 warnings; learning-content validator 0 errors / 0 warnings; Part 1 photos 9/9; objective-resource map 291/291; outcome audit 11/11 objectives and 33 criteria with 6 evidence paths; design-profile and release-version checks PASS. Remote CI/Pages and real-device QA are not claimed.

## v2.73.0 changes — first A2 guided pathway starter

- Extended Foundation from Pre-A1/A1 into the first A2 starter: 10 stable lessons with teaching content, bilingual examples, three recognition questions and one separate contextual application task per lesson.
- Added 10 A2 Reading passages / 20 questions and 10 A2 Listening scripts / 20 questions. Listening uses browser SpeechSynthesis, not ETS or native-speaker recordings. Foundation banks remain separate from TOEIC L&R Mock pools.
- Expanded the objective-resource map to 11 objectives and 291/291 linked records; outcome criteria increased to 33. Foundation production/retention evidence was not yet instrumented in v2.73.0 and is addressed by v2.74.0.
- Preserved all prior Pre-A1/A1 IDs, Reading/Listening IDs, answer keys, vocabulary, local progress stores and IndexedDB v1. No IndexedDB schema migration or learner-data reset.
- Balanced A2 answer-key positions and corrected the sample suggestion to a natural English form. The A2 starter remains subject to independent linguistic/editorial review and is not the complete A2 curriculum.
- Local checks for v2.73.0 are recorded in the v2.73.0 release report; remote GitHub Actions, Pages and physical-device QA were not verified.

## v2.72.0 changes — complete Part 1 photo set, uniform landscape framing and lightweight assets

- Added nine photo binaries from the user-provided archive. The 8 licensed Pexels photos preserve their attribution/source/license rows; `part1-office-cleaning.jpg` remains the project-generated asset and was not re-generated or recompressed.
- All nine images are 1448×1086 (4:3 landscape), progressive JPEG, each below 400,000 bytes. The eight Pexels images total 1,664,909 bytes; the full nine-image set totals 2,063,272 bytes. Total size reduced by 91.8% relative to the supplied originals.
- `part1-photocopier.jpg` is cropped from the portrait source to the shared 4:3 landscape frame, retaining the operating hand and control panel. CSS no longer needs a one-off portrait focal override.
- Strict Part 1 photo validator now checks JPEG signature, minimum size, 4:3 landscape ratio, <=400,000-byte ceiling, local path and attribution consistency; result 9/9 PASS. Learning content: 0 errors / 0 warnings.
- Retired `restore-part1-photos.bat` and its downloader helper. The old script downloaded full-resolution stock images from Pexels, did not optimize them and is unnecessary now that the complete optimized set is embedded in Full Source.
- No question IDs, answer keys, explanations, transcripts, photo filenames, attribution/license facts, learner data or IndexedDB stores were changed.
- Vocabulary remains 1,137/3,000 (37.9%); US IPA 1,044/1,137 (91.8%); word-family 276/1,137 (24.3%). This is a photo/media quality release, not a vocabulary-growth release.
- Local checks and remaining remote/device limitations are recorded in `archive/PROJECT_HISTORY.md`.

## v2.70.0 changes — Customer Service and Travel vocabulary expansion; IPA coverage counter correction

- Added `data/vocabulary/batch-011.json` and **37 canonical A–Z headwords** about customer support, complaints, issue resolution, reservations, airports and travel transport. Vocabulary grows 1,063 → **1,100 headwords** (+37): **36.7%** of the 3,000-headword minimum and **22.0%** of the 5,000-headword planning ceiling.
- Every new headword contains an English definition, Vietnamese gloss, original bilingual context example, at least three collocations, editorial CEFR estimate, and a candidate US IPA converted from a single exact-match CMUdict ARPABET pronunciation. Independent lexical review and CEFR-by-sense review remain pending.
- Added four reciprocal, POS/sense-checked word-family pairs: cancel/cancellation, resolve/resolution, responsive/responsiveness, and troubleshoot/troubleshooting. Coverage is 267/1,100 (24.3%) with 365 directed links.
- Cumulative CMUdict IPA ledger contains 298 entries; current coverage is 1,009/1,100 (91.7%). The 91 inherited unresolved records remain blank: 60 have multiple CMUdict pronunciations, 25 have no exact match, and 6 have multiple primary-stress patterns.
- Corrected the IPA-missing information counter to count a missing phonetic object and a missing/non-string `phonetic.us`; now reports the canonical total of 91 missing records. Two new validator regression tests cover these shapes.
- Extended release migration profiles for legacy 979/992/1026-word workspaces and added the exact 1,063-word v2.69.0 profile. Existing learner changes outside the exact release fingerprint are not eligible for automatic repair.
- Structural validation: 1,100 records / 0 errors / 0 warnings; content validation: 0 errors / 8 known missing-JPG warnings; CMUdict IPA ledger: 298/298; design-profile and version sync pass. Focused Python tests: 27/27 and missing-counter regressions: 2/2.
- Strict Part 1 asset validator remains blocked because eight repository-owned original JPG binaries are absent from this source archive (1/9 present). No AI-generated replacements are permitted. Remote GitHub Actions/Pages and physical-device QA are not claimed.

## v2.69.0 changes — US IPA coverage and word-family quality pass

- Added 261 US IPA transcriptions derived from exact-match, single-pronunciation CMUdict General American ARPABET records. CMUdict does not supply IPA; source pronunciations are converted by the documented project broad-GA conversion and remain editorial candidates, not independently certified pronunciations.
- US IPA coverage rose from 711/1,063 (66.9%) to 972/1,063 (91.4%). The 91 remaining blanks are deliberate: 60 multi-pronunciation entries, 25 no-exact-match entries and 6 with multiple primary-stress patterns.
- Added provenance and raw ARPABET ledger at `reports/CMUDICT_IPA_BACKFILL_v2.69.0.json`; retained `docs/licenses/CMUdict-DATA-LICENSE.txt`; added deterministic checker `tools/cmudict_ipa.py` and five CI tests.
- Word-family records rose from 240 to 259; directed relationships rose from 338 to 357 (+19). Reciprocal relationships are checked for POS/sense consistency; no stable IDs changed.
- Vocabulary remains 1,063/3,000 (35.4%) and 1,063/5,000 (21.3%). This is a metadata-quality release, not a headword-growth release. Next planned batch: Customer Service, Travel, Contracts and Facilities, after conservative review of remaining IPA exceptions.
- Validation: `validate-data.py` 1,063 records / 0 errors / 0 warnings; CMUdict ledger check PASS (261); CMUdict IPA tests 5/5; word-family link tests 5/5; project progress tests 4/4. Overall selected test run and limitations are recorded in the v2.69.0 test report.
- CMUdict warns its data may contain errors, omissions and inconsistencies; IPA conversion is not independent review. CEFR remains editorial-estimate. No IndexedDB schema, stable vocabulary/question IDs or learner progress reset. Deployment remains on hold pending eight missing original Part 1 JPG binaries; remote CI/Pages and device QA are not claimed.

## v2.68.0 changes — verified Part 1 metadata fingerprint refresh and Vocabulary Batch 010

- Fixed the remaining-content fingerprint CI failure in `test_reviewed_data_fingerprints_have_not_drifted`. The only Part 1 unit-metadata change was the intentional removal of the obsolete SVG fallback field `image` after runtime and records moved to JPG-only. For all eight historically reviewed Part 1 units, restoring the exact previous metadata field `image: ./assets/listening/<unitId>.svg` reproduces the previously certified unit hash; all eight question hashes remain unchanged. No transcript, question, choice, answer key, order, translation, title or review decision changed.
- Added a second `fingerprintRefreshLog` entry with old/new unit hashes, exact field removed, approval context and question-hash invariance. The one-off refresh utility is fail-closed: it aborts if any difference beyond removal of the exact SVG metadata field is detected or if a question hash changes.
- Updated the remaining-content review tests to validate both historical metadata refreshes and JPG-only Part 1 records. The exact GitHub Actions command `python -m unittest discover -s tools/tests -p 'test_remaining_content_review.py' -v` passes **9/9 tests**.
- Added `data/vocabulary/batch-010.json` and **37 canonical A–Z headwords** about manufacturing, production operations, quality assurance/control, maintenance, warehouse processes and supply chain. Vocabulary grows 1,026 → **1,063 headwords** (+37): **35.4%** of the 3,000-headword minimum and **21.3%** of the 5,000-headword planning ceiling.
- Batch 010 includes English definitions, Vietnamese glosses, original bilingual TOEIC-context examples, at least three collocations per entry and editorial US IPA on all 37 entries. Added five reciprocal, POS/sense-checked word-family pairs (calibrate/calibration, contaminate/contamination, defect/defective, reliable/reliability, package/packaging). CEFR levels remain editorial estimates and independent lexical review is pending. No speculative synonyms/antonyms were added to inflate field coverage.
- Added cumulative migration repair profiles: legacy 979-headword snapshots can restore only 84 known additions through Batch 010; 992-headword snapshots can restore 71; 1,026-headword snapshots can restore only 37. Exact source count and ID fingerprints are required; unrelated hidden words, overrides and learner progress are preserved. No IndexedDB schema/store migration.
- **Local verification:** 21/21 JavaScript regression suites PASS; 40/41 Python test modules completed successfully (291 assertions/tests passed across the 40 modules). `test_validator.py` did not complete within the execution window at `test_missing_id_against_baseline_is_error`; its partial run is not counted as PASS. The remaining-content review suite is 9/9; vocabulary detail/examples 12/12; word-family links 5/5; project progress 4/4; legacy collocation cleanup 3/3; CI coverage 2/2. Data validator reports 1,063 records / 0 errors / 0 warnings; version sync and design-profile sync PASS.
- Content audits: Listening 107 units / 201 questions; Reading 51 resources / 200 questions; the question-evidence audit indexed 401 questions; distractor structural audit passed for 177 questions. These automated audits do not constitute independent semantic certification.
- **Deployment hold:** strict Part 1 photo validation reports 1/9 original JPG bytes present in this workspace and 8 missing repository-owned JPG files. Keep the eight original JPG assets when merging; do not synthesize replacements or disable strict validation. Remote GitHub Actions, GitHub Pages and physical-device QA are not verified here.

## v2.67.0 changes — Listening JPG-only cleanup and Vocabulary Batch 009

- Removed the redundant UI label `Nội dung bổ sung · đang chờ kiểm duyệt độc lập · chưa dùng trong Mock Exam` from Listening cards. The `editorialStatus: reserve-pending-independent-review` metadata remains in the canonical data and Mock sampler continues to exclude those units. This does not approve or promote reserve content.
- All nine Part 1 records now use only `photo: ./assets/listening/*.jpg`; no Part 1 record declares `image`. Removed eight obsolete Part 1 SVG files from `assets/listening/`, removed their Service Worker entries and deleted SVG fallback/onerror behavior from both Listening practice and Mock rendering. Other unrelated application/topic SVG icons are unchanged.
- The source archive contains only 1/9 JPG binaries. Eight original licensed JPG files, including `part1-photocopier.jpg`, are not present in this workspace. The runtime references their repository-owned JPG paths only; retain those originals when merging. `validate-learning-content.py` reports 0 errors / 8 missing-byte warnings; strict `validate-part1-photo-assets.py` remains a release blocker. Do not disable the strict validator or substitute synthetic media.
- Added `data/vocabulary/batch-009.json` and 34 canonical A–Z records: allotment, anomaly, amortization, attest, deductible, expedite, negligence, rebate, tenure, accreditation, break-even, deferment, disqualification, exporter, leasehold, pension, repayment, restructuring, shareholder, subsidy, solvency, transparency, underwriter, concession, custody, distribution, efficiency, financing, foreclosure, projection, settlement, valuation, levy and subcontracting.
- Vocabulary count rises 992 → 1,026 (+34), or 34.2% of the 3,000-headword lower-bound planning target. Batch 009 provides English definitions, Vietnamese glosses, original TOEIC-context examples, collocations and editorial CEFR estimates. 32 entries have editorial US IPA transcriptions derived from CMUdict General American ARPABET where a single stable reading was selected; IPA remains blank for `negligence` and `financing` pending dictionary-level confirmation. Added reciprocal POS/sense-checked word-family links; no speculative synonyms/antonyms were invented. Independent lexical review remains pending; CEFR labels remain estimates, not official alignment.
- Added cumulative migration repair profiles: old 979-headword snapshots can restore only the exact 47 known release additions (Batch 008 + Batch 009); 992-headword snapshots can restore only the 34 Batch 009 IDs. Repair requires the exact profile, matching source counts and all candidate IDs incorrectly marked hidden; all other hidden IDs and personal overrides are preserved. No IndexedDB schema or store migration.
- **Local verification:** vocabulary validator 1,026 records / 0 errors / 0 warnings; focused vocabulary family tests 5/5; JPG-only PWA readiness 3/3; Learning Content 34/34; Part 1 photo-contract tests 5/5; vocabulary detail/examples 11/11; legacy collocation tests 3/3; progress tests 4/4; 79/79 selected Python tests overall; release-integrity Node test PASS; version/design synchronization PASS after documentation update; all JavaScript syntax checks PASS. Learning-content validator has 0 errors / 8 missing JPG warnings. Strict Part 1 photos remain 1/9 in this workspace.
- Existing vocabulary IDs and learner progress, listening/reading question IDs and answer keys, attribution rows, IndexedDB schema/stores and personal data are preserved. No remote GitHub Actions, GitHub Pages deployment or real-device visual/audio pass is claimed.

## v2.66.1 changes — fixed Part 1 TTS sequence and GitHub test correction

- The shared Speech Synthesis readiness layer now uses a fixed 2,000 ms preparation buffer for all spoken routes after voice-catalog readiness and queue cleanup. The delay is not exposed in Settings. Existing voice, accent, rate, pitch, volume and vocabulary/turn-pause controls remain where applicable.
- Listening Part 1 speaks `Part 1: [Topic]` (using the content topic, e.g. `Warehouse & Shipping`), waits 1,000 ms, speaks `Now, listen to the four statements.`, waits 1,000 ms, then issues `A.` as a separate utterance, waits 1,500 ms, and speaks the description. B/C/D follow exactly the same label-gap-description pattern; there is a 1,300 ms gap between descriptions.
- `playListeningAudio()` remains the single implementation for Practice and Mock Exam. The guided Mock Exam routes Part 1 directly through this full script, avoiding a duplicate generic transition line. Other Listening parts retain their existing conversation/segment sequencing.
- The transcript and Mock audio hint communicate the spoken order. Delay settings were removed from the Settings UI to prevent users from accidentally creating inconsistent exam/practice pacing.
- Updated `test_distractor_quality.py`, whose old assertion expected immediate `recordPracticeAnswer()` on option selection. The app now intentionally stages the choice and commits through `commitPracticeDraftSet()` after complete-set confirmation; the test was aligned to this already-shipped behavior.
- The escaped `app.js` content in the GitHub traceback was Python's escaped rendering of the source string attached to `AssertionError`, not malformed JavaScript. `buildOneWayGoogleAIUrl()` remains a normal URL builder and Node syntax checks pass.
- **Local verification:** 21/21 JavaScript regression scripts PASS; 85/85 selected Python tests PASS across 10 modules; TTS readiness 13/13; distractor quality 6/6; CI coverage 2/2; version synchronization and design-profile synchronization PASS; 992 vocabulary records / 0 errors / 0 warnings; learning content 0 errors / 8 missing original JPG warnings. Strict Part 1 photo validation still FAILS because 8/9 original JPG binaries are available in this source snapshot.
- No question text, answer keys, stable IDs, IndexedDB schema/stores, learner history, vocabulary, saved voices or personal data were changed. Physical-device audio and remote GitHub Actions/Pages remain unverified.

## v2.66.0 changes — balanced skill progress and deferred assessment reveal

- Dashboard progress is separated by exam and skill: TOEIC Listening (Parts 1–4) and Reading (Parts 5–7) each own a full-width row and independent Part grid. The group model leaves explicit room for future IELTS and Writing/Speaking tracks instead of assuming only two English skills.
- Multi-question practice for Grammar, Reading, Listening and Foundation stages answers in a device-local draft. No correct/wrong styling, feedback panel, objective evidence or answer history is committed until the set is complete and the learner confirms the summary modal.
- Single-question Smart Review / Part 5 now uses the same summary-before-explanation step. Flash Quiz waits until all answers are entered; its review then shows each chosen meaning beside the correct meaning. Placement diagnostics show the summary automatically immediately after the last answer.
- Mock Exam still scores against the timed test, but it does not show correctness while the learner is working. At manual submit or timeout it stores a pending result and shows only aggregate correct/incorrect counts. Transcript, answer keys and explanation review are opened only after confirmation. Pending mock summaries survive reload in `toeic:mock-pending-review:v1`; they do not appear in completed history until confirmed.
- Mock question scheduling allocates the Listening and Reading time budget across every question using group context/passage weight and reserves a 2.4-second transition/lead-in allowance per question within the fixed section deadline. UI highlights and scrolls to the active question; the timer drives transitions automatically. Listening conversations play once at group entry; later questions within the same conversation receive a spoken transition without restarting the audio.
- **Local v2.66.0 verification:** 21/21 JavaScript regression suites PASS; 259/259 focused Python test cases PASS across 36 selected modules; version sync and design-profile sync PASS; 992-word validation reports 0 errors/0 warnings; learning-content validation reports 0 errors and 8 missing original JPG warnings; all JS syntax and both CSS parsers PASS. The broad `test_validator.py` execution exceeded the tool time limit and is not counted as passing.
- **Strict photo gate:** 1/9 original Part 1 JPG files present in this workspace; strict validation fails with 8 missing binaries. Keep the gate enabled and preserve existing remote GitHub JPG files when merging.
- Added regression coverage for draft-before-commit semantics, hidden answer feedback, flash/mock confirmation, reload persistence, and local section numbering. `mock-flow.js` is now in both Service Worker required and app-shell caches for offline operation.
- No IndexedDB schema migration, question/answer key edits, stable IDs, learner history reset or vocabulary reset. The draft fields are additive, and the mock pending result uses a separate localStorage key.
- Source checks and focused test groups only; no real browser/device audio check or remote GitHub Pages deployment has been performed. The inherited strict Part 1 JPG validator remains a release blocker where original binaries are missing from this workspace.

## v2.65.2 changes — Listening Part 1 lead-in and spoken A–D labels

- Added the Part 1 spoken lead-in “Now, listen to the four statements.” after the shared voice-readiness/startup process and before option A.
- Each of the four descriptions is spoken as its own labeled utterance (`A.`, `B.`, `C.`, `D.`). The existing 1,300 ms gap remains between each option; a new configurable 1,000 ms pause is applied between the lead-in and option A.
- Practice mode (`data-listening-play`) and Mock Exam (`data-mock-audio`) both call `playListeningAudio()` with the same listening unit ID. Consequently, their Part 1 speech order, labels, selected voices and pauses are identical by implementation rather than duplicated logic.
- The in-app transcript displays the lead-in and A–D labels; the Mock Exam audio hint communicates the same sequence. The library keeps clean description strings; runtime formatting adds labels and strips any already-present leading A–D label to prevent duplication.
- Part 1 source validation at playback time requires exactly four segments. All 9 current Part 1 units were checked and contain four descriptions each.
- Added `part1LeadInPauseMs` (default 1,000 ms; supported settings range 800–1,800 ms) additively to `appSettings.tts`. Existing `part1OptionPauseMs` stays at 1,300 ms by default. Existing voice, rate, pitch, volume, startup delay and progress remain intact.
- Local tests cover lead-in → A → B → C → D, all gaps, cancellation during the lead-in gap, transcript text and common playback path for Practice and Mock. Real device playback remains unverified.
- No question data, answer keys, stable IDs, IndexedDB schema/store, learning history or personal data were changed.
- **Local verification:** 13/13 TTS/readiness Python tests and 35/35 selected Python checks PASS; 19/19 JavaScript regression suites PASS (including the Listening/TTS regression) (lead-in, spoken A–D labels, pauses, Stop during transition); all 9 Part 1 units have four segments; all 19 JS regression files are invoked by CI; version synchronization PASS; vocabulary validation 992 records / 0 errors / 0 warnings. Actual voice rendering and remote Pages deployment remain unverified.

## v2.65.1 changes — TTS voice-selector initialization hotfix

- Fixed the reported startup error `ReferenceError: refreshSpeechVoiceSelectors is not defined` at `bindTtsSettings()` / `bindPracticeEvents()`. The helper declaration had been omitted in the v2.65.0 TTS refactor while its call sites and `voiceschanged` listener remained.
- Restored the helper to populate male/female selectors from the device's English voice catalog, retain manually saved voice URIs, preserve a URI no longer offered by the current device as an explicit unavailable option, and disable selectors when no English voices are available. The existing manual-refresh button and `voiceschanged` listener continue using the same helper.
- Added regression coverage that executes the helper with an empty catalog and populated catalog; verifies that manually selected voices remain selected; and verifies an unavailable saved URI is not silently overwritten.
- **Local verification:** 10/10 TTS Python tests PASS; 12/12 version-sync Python tests PASS; 19/19 JavaScript regression suites PASS (including TTS and runtime-render smoke); all `assets/js/*.js` and `sw.js` pass Node syntax; `sync-version.py --check` PASS; vocabulary validation 992 records / 0 errors / 0 warnings; learning-content validation 0 errors / 8 missing JPG warnings.
- **Known deployment blocker unchanged:** strict Part 1 asset validator FAILS 8 missing original licensed JPGs (1/9 present), including `part1-photocopier.jpg`. The validator remains enabled. Preserve any originals already in the GitHub repository when merging this source; do not delete or replace licensed media.
- No vocabulary/question content, stable IDs, IndexedDB schema/stores, local progress keys, or TTS preferences were reset or migrated. The v2.65.0 TTS readiness buffer and A–D pauses are unchanged.
- Browser/iOS/Android audible QA, remote GitHub Actions and GitHub Pages deployment are not verified from this local workspace.

## v2.65.0 changes — Speech Synthesis readiness, Part 1 A–D pacing and Reading read-aloud

- Unified all text-to-speech entry points behind `prepareSpeechEngine()` and `speakUtterance()`. Playback waits for the speech voice catalog (up to 1.2 seconds), checks/cancels residual engine work, and applies a startup buffer before queuing the first content utterance. Cancellation invalidates the token and releases pending waits so stale playback cannot begin after Stop or navigation.
- Default startup buffer: 750 ms (configurable 500–1,500 ms in UI; runtime safety range 350–1,600 ms). If the device has no published voice catalog, playback uses the platform default after the catalog wait timeout instead of hanging indefinitely.
- Listening Part 1 labels and sequences the four descriptions A–D and uses an independent 1,300 ms default inter-option gap (configurable 1,000–2,300 ms). Parts 2–4 retain sentence/turn pause settings. The audio is still device/browser-generated TTS, not authentic ETS audio.
- One-shot speech routes (dictionary pronunciation, flashcards, flash quiz, Foundation Listening and A–Z alphabet practice) inherit the 750 ms startup buffer. The slow-vocabulary sequence also waits for preparation before its first word.
- Added Reading read-aloud for passages/documents and Part 5 question-choice sets. It shares the same prepared engine, status messages and Stop handling. The reading content is assembled from the current local JSON resource; no external service is called.
- Added two additive TTS settings in `appSettings.tts`: `startupDelayMs` and `part1OptionPauseMs`. Existing user settings and local progress remain intact; no IndexedDB schema/store migration or key reset.
- Regression checks cover a voice catalog initially returning empty, voice readiness before playback, configured first-start delay, 4 sequential Part 1 descriptions with 1.3-second gaps, safe Stop, one-shot pronunciation and Reading read-aloud. Nine Python checks and the JavaScript TTS regression execute in CI.
- **Local verification:** 59/59 selected Python tests and 19/19 JavaScript regression suites PASS; every JS asset and `sw.js` passes syntax, all Python tools pass `py_compile`, both main CSS files parse with 0 errors, 54 design tokens / 362 legacy font-floor groups sync, vocabulary data is 992/992 with 0 errors/0 warnings, learning content has 0 errors/8 missing-JPG warnings, objective resources are 281/281 and outcome criteria are 30/30. The strict Part 1 validator still FAILS (1/9 original JPGs; 8 missing). Mocked tests do not prove real-device audible onset; details are in `archive/PROJECT_HISTORY.md`.

## v2.64.0 changes — responsive composition, Part 1 media normalization and A–Z sound lab

- Standardized Listening Part 1 illustrations/photographs into the same 4:3 visual frame, using `object-fit: cover`, shared radius, common max width and caption treatment. The photocopier item receives the stable focal point `50% 42%`; licensed source bytes are not mutated by CSS. Existing SVG fallback stays in the same frame.
- Equalized card-row geometry for learning, Foundation, practice chooser, mock-test setup and objective tracker. Cards use a shared title baseline, minimum three-line copy area, footer baseline and safe long-text wrapping. Content is not clipped to force equal size; long text expands row height. Common action buttons may wrap and retain the 44 px target.
- Refined responsive grid density: A–Z sound lab now uses 4 desktop / 3 tablet landscape / 2 tablet portrait or phone / 1 narrow phone columns. New rules keep tablet columns from becoming too narrow when the sidebar is visible.
- Extended Pre-A1 `pa1-alphabet` with all 26 letters, letter-name/example-word IPA, Vietnamese meaning, representative sound, notes for non-one-to-one spelling/sound relationships and two TTS actions per letter. Exposure counts are stored separately in `toeic:alphabet-sound-progress:v1` and are explicitly not mastery or pronunciation scoring.
- Added `alphabet-sounds.json`, `alphabet-sound-progress.js`, Python/JavaScript regression tests and the relevant Service Worker resources. Fixed CI coverage so both `test_alphabet_sound_lab.py` and `test_visual_composition.py` are actually executed, not just compiled.
- Final local validation: 94/94 selected Python tests across 16 modules and 19/19 JavaScript regression suites pass; `sw.js` and all `assets/js/*.js` pass Node syntax checks; touched Python files pass `py_compile`; both main CSS stylesheets parse with 0 errors; design profile passes (54 tokens / 362 legacy selector groups); release-version synchronization passes; vocabulary validation is 992 records / 0 errors / 0 warnings; learning-content validation is 0 errors / 8 missing-JPG warnings. The strict Part 1 photo validator still fails 8 missing-JPG checks (1/9 files present), so deployment remains held. Browser visual QA is blocked by the execution environment (`ERR_BLOCKED_BY_ADMINISTRATOR` for localhost and file fixtures); no device/remote CI/Pages pass is claimed. Existing 992 vocabulary records, stable lesson/question IDs, IndexedDB schema/stores and all other learner progress remain unchanged; the only new localStorage key is `toeic:alphabet-sound-progress:v1`.
- Asset caveat: eight original licensed Part 1 JPG files are missing from the inherited local source snapshot. The strict validator remains enabled. The user-supplied GitHub repository may still contain originals; this workspace cannot claim the binaries were restored or included in the package until their presence is verified. No synthetic or replacement photo files were created.
- Deployment status: local candidate only; remote Actions, GitHub Pages and real iOS/Android visual QA are not verified.


## v2.63.0 changes — unified design system, canonical profile and design governance

- Audited the existing design stack and found that `design-system.css` had accumulated multiple incremental overrides over earlier feature-specific typography rules. The new final contract maps every module to semantic type roles and shared surface/control geometry so features no longer introduce their own font, palette, radius or spacing systems.
- Introduced `design/design-profile.json` as the canonical source for 51 design tokens: font family and semantic type scale, color palette, line heights, spacing, radii, shadows, touch target, page width and motion. A generated legacy font-floor audit covers 362 selector groups that previously declared fixed text sizes below 12.5px; CI detects new drift. `tools/sync-design-profile.py` synchronizes the marked token block and legacy font-floor block; CI fails on token or selector drift.
- Reworked the governance guide `docs/DESIGN_SYSTEM.md` with the overview, type scale, palette, component recipes, responsive breakpoints, prohibited patterns, release gates and new-module checklist. Added `docs/DESIGN_BRIEF_TEMPLATE.md` for owner preferences.
- Applied one shared visual language to Dashboard cards, Learning Objective tracker, Spaced Recall, Foundation path/listening, practice-mode selection, TOEIC mock setup, live mock test, review/results, forms, navigation and shared buttons. Essential content and mock-test questions/options are assigned readable semantic sizes; layout reflows before text is reduced.
- Canonical default profile is `Calm Study Blue`: neutral canvas/white surfaces, navy-blue brand, green semantic progress, 15–16 px body, 14 px supporting copy, 12.5 px metadata, shared 16/18 px card/panel radii and 44 px controls. The visual direction is implemented as a safe default; owner preference questionnaire remains pending.
- Added `test_design_profile.py` and CI synchronization check. Workflow now watches `design/**` and validates the profile and generated CSS, including all 362 legacy font-floor selector groups.
- Preserved all vocabulary IDs/data, IndexedDB schema/stores, personal vocabulary and learning progress. No destructive data migration or learning-progress reset.
- Local source validation: 82/82 selected Python tests and 18/18 JavaScript regression scripts pass; CSS parser reports 0 errors and design tokens/floor audit pass. Browser visual QA is not claimed. The inherited strict Part 1 asset blocker remains: eight original JPG binaries are absent; `python tools/validate-part1-photo-assets.py` must pass before deployment. Remote GitHub Actions, Pages and actual iOS/Android visual QA are not claimed.

## v2.62.0 changes — application-wide typography and Foundation Listening

- Added a consistent typography layer across the existing application: learning objective cards, practice-mode chooser, TOEIC mock-test setup/results/review, common cards/panels, forms, captions and mobile bottom navigation. Ordinary reading copy is at least 13.5px; supporting metadata is at least 12px, with control labels at 14px or larger. Scores and timers keep their distinct visual hierarchy.
- Explicitly reset `.foundation-intro.panel` to a one-column layout to remove the legacy two-column inheritance. Objective/practice/mock grids now reflow based on available content width; breakpoints are viewport-based, not physical device inches.
- Added `data/learning-path/foundation-listening.json`: 10 original short scripts mapped one-to-one to the existing 10 Pre-A1/A1 lesson IDs, with two comprehension questions each (20 total). Answer-key positions are balanced 5/5/5/5.
- Added `assets/js/foundation-listening-evidence.js`, keeping latest-result and attempt history in the separate localStorage key `toeic:foundation-listening-progress:v1`. It does not affect recognition-question denominators or previous reading/application progress.
- Playback uses browser/device Speech Synthesis and the learner's existing TTS voice settings. Transcript is opt-in; the feature is explicitly not represented as authentic recorded TOEIC/ETS audio or official CEFR evidence.
- Added the helper/data to Service Worker REQUIRED and APP_SHELL and added Python/JavaScript/CI regression tests.
- Preserved all previous stable lesson/question IDs, 992 vocabulary records, prior localStorage keys, IndexedDB stores/schema, personal vocabulary and existing learner progress. No reset or destructive migration.
- Local regression only. Strict Part 1 photo-asset validation remains a pre-deployment blocker inherited from v2.60.0/v2.61.0: eight original licensed JPG binaries are absent from the source archive. Do not disable the strict validator or substitute synthetic image files. Browser visual QA, remote CI, Pages and physical-device QA remain unverified.

## v2.61.0 changes — test integrity and unified learning surfaces

- Corrected `test_learning_detail_scope.py`: test extraction now stops at the next top-level function declaration, so helper functions inserted later cannot contaminate the scope check. Added a regression assertion that confirms `renderRecallQueue()` legitimately uses its own callback parameter `item` outside the grammar lesson function.
- Confirmed all eight historical Listening Part 1 rows are affected only by the addition of `photoSourceType: "licensed-stock"`. Removing only that property reproduces each old `unitContentSha256`; all eight `questionSha256` values remain exact. Refreshed the eight unit digests and recorded old/new values, field, rationale and verification flags in `fingerprintRefreshLog`. The operation is also reproducible through `tools/refresh-photo-source-fingerprints.py`, which aborts before writing if any other field or question hash differs.
- Rebuilt Spaced Recall with the common panel/header/card/count/button components. The question's stable ID is carried only in the button's action metadata, not printed in user-facing copy; opening the queue remains read-only.
- Rebuilt the Foundation path overview with shared panel, page heading, learning-card grid, category/level indicators and shared buttons. Body and status typography now use readable fluid sizes with minimums; progress has `role="progressbar"` and `aria-valuenow`.
- Responsive cards use `auto-fit` and content-width constraints; breakpoints use CSS pixels, not device inches. No content IDs, progress keys, IndexedDB stores/schema, personal vocabulary, or learning progress were changed/reset.
- CI now includes `test_learning_surface_consistency.py`; version sync checks the app release constant as well.
- Local verification: 130 selected Python regression tests pass; 17/17 JavaScript regression scripts pass; `sw.js` and all `assets/js/*.js` pass syntax checks; vocabulary validation is 992 records / 0 errors / 0 warnings; learning-content validation has 0 errors and 8 known missing-JPG warnings; objective resources 281/281 and outcome criteria 30/30 pass; version synchronization passes. Full Python discovery exceeded 300 seconds and is not claimed as complete.
- Browser visual QA is not claimed: Chromium in this environment is blocked from accessing localhost.
- Strict `python tools/validate-part1-photo-assets.py` fails 8 missing JPG checks; SVG fallbacks remain, but CI calls the strict validator. See `archive/PROJECT_HISTORY.md`; restore the original binaries before deployment.
- Local source verification only. Remote GitHub Actions / Pages and physical iOS/Android PWA visual behavior remain unverified until deployment.

## v2.60.0 changes — vocabulary release integrity and legacy migration repair

- Root-cause findings: the v2.59 runtime used cache-first for `/data/` even when app fetches requested `cache: 'no-store'`; the Service Worker did not honor that directive. The legacy workspace migration also inferred every base ID missing from an older snapshot as a user deletion. A 979-word snapshot could therefore hide the 13 known v2.30.0 additions and leave the effective dictionary at 979 while the footer showed a newer release.
- Added versioned `__release` query parameters for the manifest and all JSON data fetches. The new release cache normalizes the query only within its version-specific cache, preserving offline precache behavior while bypassing older workers' stale cache keys.
- Added runtime integrity checks for release version, per-letter counts, manifest total, unique IDs and unique headwords. A mismatch stops rendering and reports a visible data-integrity error rather than silently showing a partial dictionary.
- Dashboard headline now reports the canonical GitHub base count; its detail line separates `GitHub base / manifest`, currently visible words, locally hidden words, personal additions/edits and release version.
- Added a conservative repair for the exact legacy 979→992 fingerprint: only when the preserved legacy workspace maps to exactly 979 base IDs and all 13 known release-addition IDs are incorrectly marked hidden are those 13 IDs unhidden. Other hidden IDs, overrides, additions and learning progress are preserved.
- Fresh migration no longer interprets absence in an older snapshot as an explicit deletion; old snapshots are not deletion ledgers.
- Service Worker update checks bypass HTTP cache; an already-controlled PWA reloads once after controller replacement. New helper is included in REQUIRED and APP_SHELL.
- Canonical vocabulary records and stable IDs remain unchanged: 992 records; 13 release-addition IDs are identified in the manifest. No IndexedDB schema change or progress reset.
- Local source verification only. GitHub Actions, Pages and real iOS PWA behavior remain unverified until deployment.

## v2.57.0 changes — Pre-A1/A1 foundation recognition evidence

- Expanded each of the 10 existing Pre-A1/A1 lessons to three stable MCQ checks (30 total), preserving lesson IDs and original q1 content.
- Foundation evidence is stored separately in the existing localStorage progress key `toeic:foundation-progress:v1`, keyed by stable question ID. Repeated attempts update the latest result and retain history; retries do not inflate unique-question coverage.
- A lesson is reported as having met the local practice threshold only at 3 unique questions and at least 80% latest-result accuracy. This is not CEFR certification, comprehensive mastery, or evidence of spontaneous communication. Listening and speaking are explicitly not assessed by this bank.
- Legacy `attempted`/`completed` fields are preserved but are not accepted as new verified evidence. No IndexedDB schema migration or reset.
- Verification: `archive/PROJECT_HISTORY.md`; progress: `archive/PROJECT_HISTORY.md`.

## v2.56.0 changes — objective-level Recall Queue

- Added a dashboard queue for objective questions whose existing spaced-recall due time has arrived; sorted earliest due first and capped at 60 displayed items.
- Displays objective/Part, stable question ID, due timestamp, latest correctness and attempt count. Unknown objective IDs are excluded from the display, not deleted from storage.
- Grammar, Reading and Listening open the matching resource and scroll to the corresponding question. Part 5 passes the stable due ID to its selector and forces that exact item for the review action.
- Queue opening is read-only: it does not count as a recall attempt, change the due date or mutate answer history.
- No IndexedDB schema change, progress reset, canonical question change or stable-ID change.
- Verification report: `archive/PROJECT_HISTORY.md`; progress report: `archive/PROJECT_HISTORY.md`.
- Regression boundary: 13/13 JavaScript suites and 32 focused Python tests pass. Full Python discovery exceeded the 180-second window; the known `part1-meeting-documents` historical editorial fingerprint mismatch remains intentionally unresolved pending review.

## v2.55.0 changes — Part 5 explanation self-assessment rubric

- Added a three-criterion self-assessment after Part 5 feedback: identify the decisive grammar/lexical clue; explain why the correct option fits; explain why at least one distractor does not fit. Each criterion is explicitly answered as “Làm được” or “Chưa làm được”.
- Saving requires all three answers. The ledger stores latest score (0–3), three ratings, timestamp and full self-assessment attempt history under the stable Part 5 question ID in the existing `objectiveProgress` record.
- Dashboard displays the count of questions self-assessed and average latest self-report score. This metric is kept separate from correctness, timed evidence, recall checks, unique-question denominator and answer attempt history.
- This is learner self-report, not an automatically graded explanation, independent reviewer score, or mastery certification. No free-text grading or AI inference is performed.
- No IndexedDB schema/store migration, canonical content/IDs, answer keys, Service Worker asset list or learner progress reset. Existing progress remains additive.
- Added `tools/tests/explanation-rubric-self-report.mjs` and CI workflow invocation.
- Local candidate only; remote GitHub Actions, Pages and physical-device QA remain unverified.

## v2.54.0 changes — TOEIC Part 5 response-time evidence

- Added a dedicated `questionStartedAt` timestamp to the shared practice runtime state. It is reset when a new question is assigned, not when feedback is rendered.
- On answer submission, Part 5 records `answeredAt` and elapsed milliseconds, then passes both to the existing `trackObjectivePractice` path. The stable Part 5 question ID remains the item identity; retries update its latest result and preserve attempt history.
- The timer starts immediately before question rendering, after practice-session persistence, and ends at answer submission. The metric represents total elapsed time through reading the sentence and selecting an option. It does not isolate reading time from decision time, is not a reaction-time metric, and has no imposed speed target.
- Added `tools/tests/part5-timing-integration.mjs` and wired it into GitHub Actions. No IndexedDB schema/store migration, canonical content/IDs, answer keys or learner progress reset.
- Local candidate only. Remote CI, GitHub Pages and physical-device QA remain unverified.

## v2.53.0 changes — timed practice evidence and spaced recall

- Extended the existing `objectiveProgress` ledger (IndexedDB v1; no store/schema migration) to retain response duration when available, schedule first delayed recall after 1 day, then 3 days after a successful recall or 1 day after an unsuccessful recall.
- A repeat becomes a recall check only when the existing item is due; immediate retries remain ordinary attempts. Recall checks never increase the independent-question denominator.
- Objective dashboard now reports average recorded response time, delayed-recall accuracy and count of due recall items. Missing evidence is explicitly shown as not measured.
- Added a compact responsive metrics row and regression coverage for elapsed time, recall intervals, failed/successful recall and unique-item preservation.
- Scope: structured Grammar, Reading and Listening multiple-choice exercises capture elapsed time from detail render to answer. Part 5 sentence-completion timing and explanation rubric scoring remain unmeasured; no speed target or mastery threshold is invented.
- No canonical question/vocabulary IDs, learning content, answer keys or existing per-resource histories changed. Local validation only; remote CI, Pages and physical-device QA remain unverified.

## v2.52.0 changes — objective-level practice evidence

- Added `assets/js/learning-outcome-progress.js`: stable objective-resource lookup, unique-question denominator, latest-attempt scoring, retry history retention, and the 80% / 10-unique-item practice threshold.
- Connected Grammar, Listening Parts 1–4, Reading Parts 5–7 and the separate Part 5 practice bank to the objective evidence ledger stored under the existing IndexedDB v1 key `objectiveProgress`.
- Added a compact responsive dashboard panel that reports independent questions, latest accuracy, attempt count and evidence status. Repeated attempts update the same question result and never inflate the unique-question denominator.
- The label “Đạt ngưỡng luyện tập” is intentionally not called mastery. It is not official CEFR/ETS certification and does not certify each individual criterion in the 30-outcome framework.
- Foundation production/retention rubrics, delayed recall, timed accuracy and explanation scoring remain uninstrumented. The foundation group is excluded from the 9-group TOEIC tracker until its own evidence can be measured validly. Reserve Listening items, Reading Part 7 (second review required) and the separate Part 5 practice bank (independent review pending) cannot receive a threshold status until their review gates are cleared. Part 1 has 8 eligible unique questions (one mapped item remains reserve-pending) against the 10-item minimum; at least 2 more reviewed questions are needed.
- Added JavaScript and Python regression coverage and precached the new module in Service Worker REQUIRED/APP_SHELL. No IndexedDB schema/store migration, existing progress reset, canonical question ID change or vocabulary ID change.

## v2.51.0 changes — measurable learning-outcome criteria

- Added `data/learning-path/objective-outcomes.json`: 30 outcome criteria across 10 objectives (three per objective), each with a stable ID, observable outcome, evidence metric, suggested 80% threshold and minimum 10 unique items.
- Added `tools/audit-learning-outcomes.py` and automated tests to validate objective coverage, metric types, thresholds and non-mastery status.
- Progress report now distinguishes 30/30 criteria defined (100% framework coverage) from actual learner mastery.
- Criteria are not yet connected to every learning activity or learner-progress record; no learner mastery percentage is claimed.
- Service Worker REQUIRED and APP_SHELL include the registry. No IndexedDB schema, learner progress key, vocabulary ID or question ID changed.

## v2.50.0 changes — objective-to-resource mapping

- Added a canonical map for 10 objective groups and 281 unique resource IDs across foundation, Grammar, Listening Parts 1–4, Reading Parts 5–7 and separate Part 5 practice.
- Coverage: 10/10 objective groups have resources (100% availability); 281/281 unique canonical resource records are linked (100% link coverage). Neither figure implies review approval or mastery.
- Added `tools/audit-objective-resources.py` to check objective IDs, duplicate links, collection existence and canonical resource ID resolution.
- Progress report now distinguishes objective-group availability and unique resource-link coverage from editorial review and learning mastery.
- Service Worker `REQUIRED` and `APP_SHELL` include the map. No content duplication, IndexedDB schema change, stable ID change or progress reset.
- Review status is explicit: separate Part 5 remains pending independent review; Listening and Reading require item-level review tracking.

## v2.49.0 changes — measurable progress reporting

- Added `tools/report-project-progress.py` to calculate a repeatable progress snapshot from canonical JSON inventories and explicit targets.
- Added `archive/PROJECT_HISTORY.md` (bản tóm tắt lịch sử) with vocabulary coverage against the 3,000 minimum / 5,000 planning ceiling, pathway stage representation, diagnostic mapping coverage, and inventories whose total targets are not yet defined.
- Reporting separates quantity coverage from editorial quality, independent review, local tests, remote CI, deployment and physical-device QA. “Chưa đo được” is used instead of inventing denominators.
- This is a documentation/tooling release: no app runtime, canonical learning content, stable IDs, IndexedDB or learner progress behavior changed.

## v2.48.0 changes — transparent placement evidence map

- Added `data/learning-path/placement-objective-map.json`, mapping all 16 diagnostic question IDs to stable objective IDs and sampled domains: vocabulary, grammar and short reading.
- During the diagnostic, each question identifies its sampled content domain. Results report correct/total by domain as well as by level, with an explicit warning that domain scores represent only this short sample.
- Service Worker `REQUIRED` and `APP_SHELL` include the objective map. No IndexedDB schema, learner progress keys, vocabulary IDs or question IDs changed.
- The assessment remains a short reading-oriented sample; it does not assess Listening, Speaking or Writing and is not official CEFR/ETS certification.

## 1. v2.46.0 changes — short placement diagnostic

- Added a 16-item short diagnostic, four questions each for Pre-A1, A1, A2 and B1. Scores are reported separately by band; a band is suggested at 3/4 or higher.
- The learner must explicitly apply the suggested level; the existing start-level filter then hides lower pathway stages without deleting progress.
- Results are saved locally in `toeic:placement-diagnostic:v1`. Vocabulary remains globally searchable.
- Scope is intentionally limited: this is a short vocabulary/grammar/reading-oriented sample, not an official CEFR/ETS score and not a Listening/Speaking/Writing assessment. It does not certify level or readiness.
- No IndexedDB schema or existing learner records changed.

## 2. v2.45.0 changes — personalized learning start level

- Added an explicit pathway start selector: All, Pre-A1, A1, A2, B1, B2 and C1.
- Selection is stored separately in `toeic:learning-start-level:v1`; foundation lesson progress remains in `toeic:foundation-progress:v1`.
- The selector filters only the learning pathway. Dictionary search and the full vocabulary bank are not gated by CEFR level.
- If a chosen level has no published guided lessons yet, the page says so and offers the full dictionary; it does not force the learner to repeat lower levels or fabricate content.
- No IndexedDB schema or existing learner records changed.

## 3. v2.44.0 changes — guided Pre-A1/A1 foundation

- Added `data/learning-path/pre-a1-a1.json` with 10 sequenced lessons and stable IDs (`pa1-*`, `a1-*`).
- Added the “Học từ đầu” navigation/page, lesson cards, objective/explanation/example/tip sections and one four-choice knowledge check per lesson.
- Completion is recorded only after a correct answer; attempts and latest correctness are retained in the isolated localStorage key `toeic:foundation-progress:v1`.
- Added the learning-path JSON to Service Worker `REQUIRED` and `APP_SHELL`.
- Existing vocabulary/grammar/reading/listening content, stable IDs and IndexedDB v1 schema remain unchanged. No diagnostic placement score is claimed yet; this release implements the first guided foundation stage only.

## 4. v2.43.0 — curriculum gap audit

- Added `archive/PROJECT_HISTORY.md` (bản tóm tắt lịch sử), comparing the canonical source inventory against the Pre-A1–C1 four-skill curriculum.
- Identified Pre-A1 foundations, sequenced learning, placement, Speaking and Writing as missing/partial rather than complete.
- Prioritized a Pre-A1/A1 guided pathway and objective-level placement/mapping.

## 2. Previous v2.42.0 — focused debugging and traceability

- Added `docs/DEBUG_TRACEABILITY.md`: feature → runtime code → canonical data → shared dependency → focused tests/validators.
- Added a compact defect-report contract and evidence-first diagnosis workflow.
- Added rules to preserve stable IDs, IndexedDB, canonical data ownership and Service Worker asset consistency.
- No runtime code, canonical content, learner storage, IDs or PWA behavior changed.

## 3. Previous baseline v2.41.0 — TOEIC curriculum and architecture governance

- Canonical target curriculum: `docs/MASTER_CURRICULUM.md` (Pre-A1–C1, four skills, TOEIC L&R primary, S&W complementary, workplace communication).
- Static architecture audit: `archive/PROJECT_HISTORY.md` (bản tóm tắt lịch sử).
- Two-generation notes: `docs/versions/PREVIOUS_VERSION.md` and `docs/versions/CURRENT_VERSION.md`.
- Content operations now reflect four-skill TOEIC-first direction; IELTS remains deferred.
- No app runtime, canonical learning JSON, stable IDs, IndexedDB schema or PWA deployment model changed in this foundation release.
- Local v2.41 checks: version sync PASS; vocabulary validator 992 records / 0 errors / 0 warnings; learning-content validator 0 errors / 8 known missing-Pexels-JPG snapshot warnings; CI coverage tests 2/2 PASS; release rotation tests 3/3 PASS; app/mock/SW JavaScript syntax PASS.
- Remote GitHub Actions, Pages deployment and physical-device QA remain unverified.

## 4. Previous baseline v2.40.0 — Part 1 photo-only support

- The canonical `part1-office-cleaning` record retains `photo: ./assets/listening/part1-office-cleaning.jpg` and no longer declares an `image` SVG fallback. The SVG was removed because it is no longer present in the user's GitHub repository; do not recreate it.
- Removed the stale `part1-office-cleaning.svg` path from Service Worker `REQUIRED` and `APP_SHELL`. The JPG remains in `OPTIONAL` cache assets.
- Shared Listening rendering uses the photo directly when `image` is absent. Mock rendering only adds `data-fallback-src` for records with a declared fallback. Eight existing Pexels SVG fallbacks remain unchanged.
- `ATTRIBUTION.csv` keeps nine rows (8 licensed Pexels + 1 AI-generated OpenAI asset). `part1-office-cleaning` stays a matching stable ID in the canonical Listening library. Uploading CSV without the corresponding Listening JSON causes an extra-attribution CI failure; both must be applied together.
- Updated `validate-learning-content.py`, the learning-content regression tests and PWA readiness test: SVG is optional per item; every declared fallback must exist and be in `REQUIRED`/`APP_SHELL`.
- New Part 1 item remains `reserve-pending-independent-review`: normal practice only, excluded from Mock until independent review. No answer/choice IDs changed.
- Focused checks: `test_learning_content.py` 34/34 PASS; `test_pwa_readiness.py` 3/3 PASS; `test_part1_photo_assets.py` 4/4 PASS; JS syntax checks for `assets/js/app.js` and `sw.js` PASS.
- `validate-learning-content.py`: 0 errors and 8 warnings because eight original Pexels JPG binaries are omitted from this source snapshot. `validate-part1-photo-assets.py --allow-missing`: PASS with 1/9 photo bytes present here and 8 known missing-Pexels-JPG warnings. The user's original eight JPGs must remain in GitHub for strict CI photo validation.
- No IndexedDB change: `toeic-vocabulary-phase1`, v1, store `workspace`. Vocabulary 1,100, Reading 200, Grammar 33 lessons/86 exercises, separate Part 5 bank 80; no changes to their IDs or progress.

## 6. Current inventory — v2.77.0

| Area | Inventory | Current development status |
|---|---:|---|
| Vocabulary | 1,137 headwords | 1,044 US IPA / 1,137 (91.8%); 276 word-family records / 1,137 (24.3%); 374 directed family links; 325 verb-form records; 967 collocation records |
| Grammar | 33 lessons / 86 exercises | No overall target agreed; Part 5/6 tagging retained |
| TOEIC Listening | 107 units / 201 questions | 102 Mock-eligible; 99 questions pending independent review; reserve pool is practice-only until approved |
| TOEIC Reading | 51 resources / 200 questions | 45 expanded Part 7 questions remain second-review-gated; eligible bank supports two zero-overlap Full Reading forms according to the current inventory audit |
| Guided Foundation | 23 lessons | 3/6 stages represented: Pre-A1 (3), A1 (7), A2 (13). Stage presence does not mean full-stage completion |
| Foundation Reading | 23 passages / 59 questions | 10 Pre-A1/A1 × 2 + 13 A2 × 3; separate bank, not TOEIC Mock inventory |
| Foundation Listening | 23 scripts / 59 questions | 10 Pre-A1/A1 × 2 + 13 A2 × 3; 13 A2 four-turn dialogues use device SpeechSynthesis, not authentic ETS recordings |
| Foundation A–Z sound lab | 26 letters | Two TTS actions per letter; no pronunciation scoring or mastery inference |
| Separate TOEIC Part 5 practice | 80 questions | Four-choice practice pool; independent review pending; not Mock-eligible |
| Mock formats | 15m/25Q · 60m/100Q · 120m/200Q | Existing test blueprints and indivisible passage/conversation blocks preserved |

No numeric total target has been agreed for the full Grammar, TOEIC Listening, TOEIC Reading or Foundation pathway. Do not invent a single product-completion percentage. Vocabulary quantity coverage remains 37.9% of the 3,000-headword minimum and 22.7% of the 5,000 planning ceiling.

## 7. Content readiness and known limits

1. Guided Foundation currently represents Pre-A1, A1 and A2 (3/6 stages = 50.0% stage presence; not a full-stage completion ratio). The 13 A2 lessons cover polite requests, quantities, comparisons, past work events, present continuous, obligation/permission, directions, invitations/offers, sequencing, plans, introductory Present Perfect, basic Passive Voice and defining Relative Clauses. Longer-form content, broader independent application and independent four-skill review remain open.
2. A2 includes 13 Reading passages of 69–80 words (3 questions each) and 13 four-turn Listening dialogues (3 questions each). Foundation totals are 23 passages/59 questions and 23 scripts/59 questions. A2 Reading/Listening uses a local 3-question / 67% practice threshold; Pre-A1/A1 remains 2 / 80%. Listening is device SpeechSynthesis. These assets are not ETS recordings, official exam content or evidence of independent skill mastery.
3. v2.77.0 corrected five identified repeated-information A2 tasks across Reading/Listening and added exact evidence pointers; A2 q1/q2 objects remain unchanged against the v2.75.0 hash baseline. The focused audit passed structural/source checks, but independent linguistic/editorial review is still required. The “reviewState” of the A2 objective remains review-depth-required. Do not promote structural completion to editorial approval.
4. Outcome registry has 11 objectives and 33 criteria defined. Foundation recognition, learner-authored production self-report and delayed recall are wired separately; self-report is not auto-graded, and no learner mastery claim is allowed.
5. TOEIC objective practice evidence is wired across 9/9 TOEIC objective groups. Practice thresholds (minimum unique items and accuracy) are local practice indicators only, not CEFR/ETS certification.
6. Listening pending pool: 99 questions (Batch 013=11, Batch 014=17, Batch 015=70, Batch 017 Part 1=1). Pending questions remain available for ordinary practice but excluded from Mock until a second reviewer records approval.
7. Current eligible Listening pool remains 102: P1=8, P2=25, P3=39, P4=30. One Full Listening form can be assembled; a second currently reuses 98/100 question IDs. Even after the 99 pending items are approved, two zero-repeat Full forms need three additional distinct Part 1 items.
8. Part 1 uses nine JPG photos with source-specific attribution (8 licensed Pexels + 1 AI-generated project asset). All are embedded as 1448×1086 4:3 landscape JPEGs below 400,000 bytes. Strict photo validation passes 9/9; no SVG fallback or downloader step belongs to the current contract.
9. Reading's 200-question bank supports two zero-overlap Full forms according to the current inventory audit. The 45 expanded Part 7 questions still need semantic second-person review.
10. All 80 separate Part 5 practice items remain pending independent review and practice-only. Do not promote to Mock until answer-key uniqueness, distractors, grammar and naturalness have an independent review.
11. Mock scores are raw practice counts/accuracy, not ETS-equated results. No ETS questions or recordings are included.
12. Vocabulary contains 1,137 headwords, below the 3,000–5,000 internal planning target. 93 records still lack populated US IPA; no ambiguous pronunciation is to be guessed. Independent lexical/CEFR review remains active.
13. Remote GitHub Actions, GitHub Pages deployment and physical iOS/Android/desktop audio/visual QA are not inferred from local checks.

## 8. Runtime and storage compatibility

- Stable vocabulary/resource/question/choice IDs are immutable. Append new records; do not reorder legacy question indexes linked to saved progress.
- IndexedDB remains `toeic-vocabulary-phase1`, version 1, store `workspace`. v2.73.0–v2.77.0 add/extend A2 content, question metadata and Foundation outcome instrumentation only; they do not change IndexedDB schema, store names or version.
- Existing Pre-A1/A1 lesson IDs, recognition question IDs, Reading/Listening IDs, answer keys, localStorage progress keys, user vocabulary, review history and settings remain untouched. New A2 records use additive stable IDs.
- v2.77.0 changes five question tasks and adds only optional `evidenceText` source pointers; no existing progress keys are changed. Foundation recognition and contextual-application evidence continue using separate localStorage ledgers; Foundation Reading and Listening attempts remain isolated from TOEIC objective evidence.
- Part 1 image rule (current): JPG-only. `photo` is required; `image` SVG fallback is prohibited in JSON, runtime, assets and Service Worker. Keep the strict JPG validator enabled.
- Service Worker static array tests do not prove real browser offline/reconnect behavior. Browser SpeechSynthesis remains synthesized audio, not ETS/native recordings.

## 9. Active development backlog

| Priority | Workstream | Next implementation |
|---|---|---|
| P0 | Foundation outcome instrumentation | COMPLETE for current Foundation scope: recognition, learner self-report production/explanation and delayed recall are wired separately; do not infer mastery or merge with TOEIC evidence |
| P0 | Listening reserves | Continue second-person review of the 99 pending Listening questions; preserve reserve/Mock separation until recorded independent approval |
| P1 | A2 completeness | Continue A2 writing production quality, broaden varied/extended Reading and Listening, then obtain second-person linguistic review before any A2 completion status |
| P1 | B1 pathway | Start the B1 bridge only after defining level-specific outcomes, lesson/skill coverage and review gates; add no arbitrary completion denominator |
| P1 | Part 5 editorial review | Independent item-level review of all 80 sentence-completion questions; keep practice-only, no promotion to Mock before review |
| P1 | Reading editorial quality | Second review of the 45 expanded Part 7 questions, focusing on semantic support, paraphrase and distractor uniqueness |
| P1 | Vocabulary quality and growth | Continue source-supported definitions, sense-specific examples, unresolved IPA, word-family, verb forms and collocations; keep 3,000 as minimum target and distinguish quantity from quality |
| P1 | PWA/device behavior | Targeted hardening for offline cache, reconnect, TTS and responsive layout; remote Actions/Pages and physical-device QA remain release gates |
| P2 | Speaking & Writing | Define content schema, recording/feedback contracts and staged progression after TOEIC L&R acceptance gates; IELTS remains deferred |

IELTS remains deferred until TOEIC development backlog is closed and the user approves a phase change.

## 9. Focused verification commands

```bash
python -m unittest discover -s tools/tests -p 'test_learning_content.py' -v
python -m unittest discover -s tools/tests -p 'test_pwa_readiness.py' -v
python -m unittest discover -s tools/tests -p 'test_part1_photo_assets.py' -v
python tools/validate-learning-content.py
python tools/validate-part1-photo-assets.py --allow-missing
python tools/validate-data.py
python tools/sync-version.py --check
node --check assets/js/app.js
node --check sw.js
```

These are targeted source/data checks, not remote deployment or final system acceptance.

## 10. Two-generation documentation rotation

For the next release, v2.42.0 becomes Previous and the older v2.41.0 detail is summarized in `archive/PROJECT_HISTORY.md`; keep only the latest two generations of detailed release notes. The rotator must never touch app source, canonical JSON, assets or learner profiles.

### v2.41.0 audit blockers
- Two stale reserve-count assertions were aligned to the verified 99 pending / 201 total Listening inventory; targeted tests PASS.
- Historical review registry fingerprint mismatch remains for `part1-meeting-documents` unit metadata. Do not refresh the fingerprint without checking the actual editorial change and its review evidence.
- Full Python test discovery timed out; only individually completed suites and commands are reported as PASS.

## 11. Debugging policy

Use `docs/DEBUG_TRACEABILITY.md` as the first lookup for reported defects. Start from the failing test, stack frame, feature, content ID or asset path; inspect only the mapped dependencies and add a focused regression test. Do not repeatedly scan the full repository for localized issues.


## v2.47.0 — Responsive layout baseline
- Layout now responds to CSS viewport width rather than assumed device-inch categories.
- Added fluid page gutters, intrinsic grid sizing, content wrapping, overflow containment, safe-area-aware mobile navigation and viewport-bounded dialogs.
- Compact navigation activates at 820 CSS px to support tablet portrait and narrow windows without forcing a 224–248 px sidebar.
- No data model or learning behavior changed.
- Real-device QA still required at representative widths: 320, 360, 390, 430, 600, 768, 820, 1024, 1280, 1366 and 1920 CSS px; include portrait/landscape, 100% zoom and long translated text.

## Kiểm thử responsive v2.47.0
- Regression CSS: 5/5 PASS; placement diagnostic 4/4 PASS; learning start level 4/4 PASS; foundation pathway 4/4 PASS; JavaScript syntax app.js/sw.js PASS; version sync PASS.
- Chưa có browser automation hoặc thiết bị thật trong lượt này; không kết luận giao diện đã được xác nhận trên mọi kích thước vật lý.

## v2.48.0 focused verification

- Objective-map coverage test: all 16 diagnostic question IDs mapped exactly once; vocabulary/grammar/reading domains present.
- Placement diagnostic regression suite and version sync results are in `docs/archive/PROJECT_HISTORY.md` (bản tóm tắt lịch sử).
- No remote GitHub Actions, Pages deployment or physical-device QA is claimed.

## v2.58.0 changes — contextual application evidence for Foundation

- Added one stable, scenario-based application MCQ to each of 10 existing Pre-A1/A1 lessons (10/10 coverage). Scenarios apply the lesson target in a simple everyday/office context.
- Application attempts and latest outcomes are stored under `applicationEvidence` within the existing `toeic:foundation-progress:v1` lesson record. This ledger is separate from the 3-question recognition bank; it does not increase the recognition denominator or alter its 80% practice threshold.
- Learners may retry a contextual task. Latest result drives the current signal while attempt history remains available.
- These are contextual multiple-choice checks, not open-ended speaking/writing, listening comprehension, spontaneous communication, CEFR certification or mastery evidence. Such skills remain unmeasured.
- Preserved all 10 lesson IDs, 30 recognition question IDs, old progress fields and IndexedDB schema. No personal progress reset.
- Verification report: `archive/PROJECT_HISTORY.md`; progress: `archive/PROJECT_HISTORY.md`.


## v2.60.0 changes — Foundation short reading comprehension

- Added 10 short, original beginner reading passages, one mapped to each existing Pre-A1/A1 lesson, with 20 stable comprehension questions.
- Question mix: 15 explicit-detail questions, 2 main-idea questions, 2 simple-purpose questions and 1 simple-inference question. Answer-key positions are balanced 5/5/5/5 across A–D.
- Reading progress is stored separately under `toeic:foundation-reading-progress:v1`, keyed by stable question ID with latest correctness and retry history. Retries do not increase unique-question coverage.
- Local practice threshold: at least 2 unique questions and 80% latest-result accuracy. This is not CEFR certification or proof of broad reading mastery.
- Added a reading progress indicator to each Foundation lesson card and responsive passage typography.
- New data and module are included in Service Worker REQUIRED and APP_SHELL.
- Preserved existing lesson, recognition-question and contextual-application IDs; no IndexedDB schema migration or personal-data reset.
- Verification: 16/16 JavaScript regression scripts PASS; 20/20 focused Python tests PASS; vocabulary validator 992 records / 0 errors / 0 warnings; learning-content validator 0 errors / 8 known missing-JPG warnings; version sync PASS. Remote CI/Pages and physical-device QA remain unverified.


## v2.60.0 — Vocabulary release integrity

- Dashboard now reports verified GitHub vocabulary count against manifest total (base words separated from personal additions).
- Versioned data requests bypass stale cache keys; runtime validates 26 letter files, declared counts, totalWords and uniqueness before rendering.
- Service Worker update check/reload prevents a mixed release in an installed PWA.
- Canonical vocabulary unchanged: 992 records; no progress or personal data reset.
- Local tests only; deployment and device confirmation are pending.
