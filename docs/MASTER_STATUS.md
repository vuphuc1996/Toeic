# TOEIC DICTIONARY — MASTER STATUS

> **Nguồn trạng thái và lộ trình duy nhất.** Mọi release cập nhật trực tiếp file này. `CHANGELOG.md` là log phát hành; `archive/PROJECT_HISTORY.md` là chỉ mục tài liệu đã nghỉ hưu; `COMPATIBILITY.md` là sổ tương thích duy nhất.

- **Ngày kiểm kê:** 2026-11-15.
- **Quy ước báo cáo tiến độ:** luôn có % khi tồn tại target/denominator rõ; tách độ phủ số lượng, chất lượng nội dung, kiểm thử phiên bản và xác minh triển khai. Không có target thì ghi “Chưa đo được”.
- **Phiên bản mã nguồn đang kiểm kê:** v2.62.0 (application-wide typography, Foundation Listening; local candidate).
- **Current candidate:** v2.62.0 — application-wide typography normalization, responsive learning surfaces, and Foundation Listening (TTS) for all 10 Pre-A1/A1 lessons.
- **Previous release:** v2.61.0 — test-scope correction, metadata-only Part 1 fingerprint refresh with audit log, and unified Spaced Recall/Foundation UI.
- **Current progress snapshot:** `docs/reports/PROJECT_PROGRESS_SNAPSHOT_v2.62.0.md`; vocabulary 992/3,000 minimum (33.1%); 10/10 objective groups with resources (100% availability); 281/281 unique canonical resource records linked (100% link coverage). These are not quality or mastery scores. Outcome criteria: 30/30 defined (100% framework coverage); objective-level TOEIC practice evidence is wired for 9/10 groups; delayed recall is instrumented for the 9 wired TOEIC objective groups; response-time evidence covers structured Grammar/Reading/Listening and separate Part 5 practice (9/9 wired TOEIC groups). Part 5 explanation self-report is instrumented for 1/9 TOEIC objective groups; due recall is now surfaced in a dashboard queue; actual explanation quality and CEFR/real-world mastery remain unverified. Foundation recognition bank is 30/30 (100%); contextual application is 10/10 (100%); short reading is 10/10 passages and 20/20 questions (100% bank coverage); Foundation Listening is 10/10 scripts and 20/20 questions (100% bank coverage; synthesized TTS, not ETS recordings). Listening evidence is isolated in `toeic:foundation-listening-progress:v1`. Reading evidence is isolated in `toeic:foundation-reading-progress:v1`; threshold is 2 unique questions and 80% latest-result accuracy, not CEFR certification. Learner attainment remains unmeasured in this source-only snapshot.
- **Immediate base:** v2.61.0; static GitHub Pages PWA, no backend/GAS/iframe/Cloudflare dependency.
- **Release state:** local candidate — deployment hold. The strict Part 1 photo validator currently fails because eight original JPG binaries are missing from the inherited v2.60.0 source archive. Remote GitHub Actions, Pages deployment and physical-device behavior are not verified from this workspace.
- **Development rule:** finish the internal product/content backlog first. Do not issue acceptance reminders or a broad acceptance checklist while development is active. The eventual test plan should target high-risk flows rather than repeat a 100% manual inventory sweep.







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
- Strict `python tools/validate-part1-photo-assets.py` fails 8 missing JPG checks; SVG fallbacks remain, but CI calls the strict validator. See `docs/reports/PART1_PHOTO_ASSET_RECOVERY_v2.61.0.md`; restore the original binaries before deployment.
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
- Verification: `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.57.0.md`; progress: `docs/reports/PROJECT_PROGRESS_BASELINE_v2.57.0.md`.

## v2.56.0 changes — objective-level Recall Queue

- Added a dashboard queue for objective questions whose existing spaced-recall due time has arrived; sorted earliest due first and capped at 60 displayed items.
- Displays objective/Part, stable question ID, due timestamp, latest correctness and attempt count. Unknown objective IDs are excluded from the display, not deleted from storage.
- Grammar, Reading and Listening open the matching resource and scroll to the corresponding question. Part 5 passes the stable due ID to its selector and forces that exact item for the review action.
- Queue opening is read-only: it does not count as a recall attempt, change the due date or mutate answer history.
- No IndexedDB schema change, progress reset, canonical question change or stable-ID change.
- Verification report: `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.56.0.md`; progress report: `docs/reports/PROJECT_PROGRESS_BASELINE_v2.56.0.md`.
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
- Added `docs/archive/PROJECT_HISTORY.md` (bản tóm tắt lịch sử) with vocabulary coverage against the 3,000 minimum / 5,000 planning ceiling, pathway stage representation, diagnostic mapping coverage, and inventories whose total targets are not yet defined.
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

- Added `docs/archive/PROJECT_HISTORY.md` (bản tóm tắt lịch sử), comparing the canonical source inventory against the Pre-A1–C1 four-skill curriculum.
- Identified Pre-A1 foundations, sequenced learning, placement, Speaking and Writing as missing/partial rather than complete.
- Prioritized a Pre-A1/A1 guided pathway and objective-level placement/mapping.

## 2. Previous v2.42.0 — focused debugging and traceability

- Added `docs/DEBUG_TRACEABILITY.md`: feature → runtime code → canonical data → shared dependency → focused tests/validators.
- Added a compact defect-report contract and evidence-first diagnosis workflow.
- Added rules to preserve stable IDs, IndexedDB, canonical data ownership and Service Worker asset consistency.
- No runtime code, canonical content, learner storage, IDs or PWA behavior changed.

## 3. Previous baseline v2.41.0 — TOEIC curriculum and architecture governance

- Canonical target curriculum: `docs/MASTER_CURRICULUM.md` (Pre-A1–C1, four skills, TOEIC L&R primary, S&W complementary, workplace communication).
- Static architecture audit: `docs/archive/PROJECT_HISTORY.md` (bản tóm tắt lịch sử).
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
- No IndexedDB change: `toeic-vocabulary-phase1`, v1, store `workspace`. Vocabulary 992, Reading 200, Grammar 33 lessons/86 exercises, separate Part 5 bank 80; no changes to their IDs or progress.

## 6. Baseline inventory

| Area | Inventory | Current development status |
|---|---:|---|
| Vocabulary | 992 headwords | 207 word-family records; 292 links; US IPA 642/992 |
| Listening | **201 questions / 107 units** | P1=9, P2=51, P3=81, P4=60; 102 Mock-eligible; 99 pending independent review |
| Reading | **200 questions / 51 resources** | Two Full Reading forms can be selected without repeated eligible IDs |
| Grammar | **33 lessons / 86 exercises** | Retry and shared Focus Workspace preserved |
| Guided foundation | **10 lessons** | Pre-A1/A1 first-stage pathway; learner can select a start level from All / Pre-A1 / A1 / A2 / B1 / B2 / C1; higher-level content is still in development |
| Separate TOEIC Part 5 practice | **80 questions** | 14 grammar groups; practice-only, pending independent review |
| Mock formats | 15m/25Q · 60m/100Q · 120m/200Q | Blueprint and indivisible passage/conversation blocks preserved |

## 7. Content readiness and known limits

1. Listening pending pool: 99 questions (Batch 013=11, Batch 014=17, Batch 015=70, Batch 017 Part 1=1). Pending questions are available for ordinary practice but excluded from Mock until a second reviewer records an approval decision.
2. Current eligible Listening pool remains 102: P1=8, P2=25, P3=39, P4=30. One Full Listening form can be assembled; a second currently reuses 98/100 question IDs. After all 99 pending items are approved, two zero-repeat Full forms still require three additional distinct Part 1 items beyond the current photo-only item.
3. Part 1 has eight licensed Pexels records and one AI-generated project asset. `ATTRIBUTION.csv` must cover exactly the Part 1 IDs. AI-generated provenance must not be labelled as Pexels or assigned an invented human photographer.
4. Eight original Pexels JPG bytes are intentionally absent from this source snapshot; the eight old SVG fallbacks remain. The new office-cleaning JPG is present at 1448×1086. Do not overwrite or remove repository-owned original Pexels JPGs.
5. The new office-cleaning record is photo-only. No `image` fallback is declared; do not add `part1-office-cleaning.svg` to JSON, Service Worker arrays, mock rendering or tests as a required file.
6. Part 1 strict photo validation is not certified by this source snapshot because only 1/9 JPG binaries are present. The source validator passes only with `--allow-missing`; strict CI on GitHub requires all nine JPG files.
7. Reading's 200-question bank supports two zero-overlap Full forms according to the local inventory audit. The 45 expanded Part 7 questions still need semantic second-person review.
8. All 80 separate Part 5 practice items remain pending independent review and practice-only. Do not promote to Mock until key uniqueness, distractors, grammar and naturalness have independent review.
9. Mock scores are raw practice counts/accuracy, not ETS-equated results. No ETS questions or recordings are included.
10. Vocabulary remains 992 headwords, below the internal 3,000–5,000 planning target. Sense-level IPA, word families, verb forms, collocations, synonyms/antonyms, definitions and examples remain active editorial work.

## 8. Runtime and storage compatibility

- Stable vocabulary/resource/question/choice IDs are immutable. Append new records; do not reorder legacy question indexes linked to saved progress.
- IndexedDB remains `toeic-vocabulary-phase1`, version 1, store `workspace`; no profile reset, import/export or migration in v2.44.0. New foundation progress is isolated in localStorage.
- Retry and Attempt History remain device-local; latest answer and prior attempts are preserved.
- Part 1 image rule: `photo` is the primary local JPG. `image` is an optional SVG fallback only when the file exists and is listed in Service Worker `REQUIRED`/`APP_SHELL`. Photo-only records are valid.
- Service Worker static array tests do not prove real browser offline/reconnect behavior. Browser SpeechSynthesis remains synthesized audio, not ETS/native recordings.

## 9. Active development backlog

- Expand objective mapping into outcome-level mastery criteria, then connect each objective to the existing shared practice/review engine without duplicating canonical content.
- Expand A2–C1 guided pathways and beginner four-skill coverage before claiming those pathways are complete.

- v2.43.0 audit: `docs/archive/PROJECT_HISTORY.md` (bản tóm tắt lịch sử). v2.44.0 implements the first 10-lesson Pre-A1/A1 pathway; next add objective mapping, diagnostic placement and remaining beginner skills.

| Priority | Workstream | Next implementation |
|---|---|---|
| P0 | Beginner pathway | Extend Pre-A1/A1 from the first 10 lessons; add diagnostic placement, alphabet/sound practice and foundational listening/reading outcomes. |
| P0 | Listening reserves | Continue second-person review of 99 pending questions; do not promote unreviewed units to Mock |
| P1 | Part 1 photo pool | Add three more distinct photo-description items after reviewing source/photo quality; preserve all original Pexels assets |
| P1 | Part 5 editorial review | Independent item-level review of all 80 sentence-completion questions; no expansion/promotion to Mock before review |
| P1 | Reading editorial quality | Second review of 45 expanded Part 7 questions, focusing on semantics and distractor uniqueness |
| P1 | Vocabulary | Continue sense-level work on IPA, word family, verb forms, collocations, definitions and example accuracy |
| P1 | PWA/device behavior | Continue targeted hardening for offline cache, reconnect and image fallback; reserve full physical-device QA for the eventual final test plan |
| P0 | Beginner pathway | First implementation milestone: Pre-A1/A1 guided lessons with stable objective IDs, prerequisites, examples, guided/independent practice, explanations and mastery gates using the existing shared workspace |
| P0 | Placement & objective map | Map existing content to objective IDs and design diagnostic placement without resetting IndexedDB v1 or duplicating canonical records |
| P1 | Shared architecture | Build dependency map and tests around existing shared learning workspace before extracting runtime components |
| P1 | A2/B1 bridge | Complete staged grammar, vocabulary, Listening and Reading objectives and connect them to the shared review engine |
| P2 | Speaking & Writing | Define content schema, recording/feedback contracts and staged learning flow; do not claim implementation yet |

IELTS remains deferred until TOEIC development backlog is closed and the user approves a phase change.

### v2.43.0 local verification

- `python tools/sync-version.py --check`: PASS; all registered markers = 2.43.0.
- `python tools/validate-data.py`: PASS; 992 vocabulary records, 0 errors / 0 warnings (legacy informational debt remains documented by validator).
- `python tools/validate-learning-content.py`: PASS; 0 errors, 8 known missing-Pexels-JPG snapshot warnings.
- `python tools/audit-toeic-coverage.py`: PASS; generated v2.43.0 inventory report.
- `node --check assets/js/app.js`, `mock-engine.js`, `sw.js`: PASS.
- `test_sync_version.py`: 12/12 PASS; `test_release_rotation.py`: 3/3 PASS.
- No runtime code or canonical learning data changed. GitHub Actions, Pages deployment and physical-device behavior are not verified.

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
- Verification report: `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.58.0.md`; progress: `docs/reports/PROJECT_PROGRESS_BASELINE_v2.58.0.md`.


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
