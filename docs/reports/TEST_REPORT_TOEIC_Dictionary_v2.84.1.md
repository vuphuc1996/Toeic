# TOEIC Dictionary v2.84.1 — Local Test Report

## Scope

Robot Buddy Learning Insights & Knowledge Expansion, based on v2.84.0. Tests were run against the local extracted Full Source tree before packaging. GitHub Actions, GitHub Pages production and physical-device/browser visual QA have not been run in this session.

## Passed checks

| Check | Result |
|---|---|
| JavaScript regression suites | **29/29 PASS** |
| Selected Python tests (CI coverage, version sync, PWA readiness, dashboard/responsive layout, learning surface consistency, project progress, design system) | **56/56 PASS** |
| `tools/validate-data.py` | **PASS** — 1,137 vocabulary records; 0 ERROR; 0 legacy WARNING |
| `tools/validate-learning-content.py` | **PASS** — 0 errors, 0 warnings |
| `tools/audit-learning-outcomes.py` | **PASS** — 11/11 objectives; 33 measurable outcome criteria; 6/33 outcomes with evidence-collection path; Foundation instrumentation 6/6 |
| `tools/audit-objective-resources.py` | **PASS** — 11 objectives; 294/294 resource records linked |
| `tools/audit-question-evidence.py` | **PASS** — 401 indexed questions; structural review scope completed |
| `tools/audit-distractors.py` | **PASS** — 177 questions in audit scope; structural answer/choice checks passed |
| `tools/validate-part1-photo-assets.py` | **PASS** — 9/9 Part 1 photo files valid; no missing photo warnings |
| `tools/sync-version.py --check` | **PASS** — app, SW, title, sidebar, phase note, footer, README and Master Status all 2.84.1; CHANGELOG heading present |

## Robot-specific regression coverage

- 500 unique authored dialogue variants remain intact.
- Feature help covers all 11 menu areas plus Placement (12 destinations); six FAQs and 16 quick prompts.
- “Bạn là ai?” identifies the developer and accurately explains the local-only progress-analysis capability.
- Learning Insights classify Cần học / Cần luyện / Cần ôn from real-shaped local snapshots and return up to five concrete item names per category.
- Grammar/Reading/Listening are not labelled weak below five answered questions; Foundation requires at least three unique evidence items; Flashcard practice requires at least three quiz answers.
- Objective and Foundation due-recall timestamps are included.
- Snapshot aggregation is pure and does not mutate caller-owned progress objects.
- Progress analysis can be switched off without disabling dialogue/help; mobile header controls wrap at narrow viewport widths.
- Service Worker includes the new module in both `REQUIRED` and `APP_SHELL`.
- IndexedDB schema remains v1; no learner progress migration, overwrite or delete was added.

## Incomplete checks / limitations

- Full `python -m unittest discover -s tools/tests -p 'test_*.py'` exceeded the 300-second execution window. It is not reported as PASS.
- Standalone `test_validator` also exceeded the 300-second execution window. The production data validator script itself completed successfully as listed above.
- No remote GitHub Actions result, Pages deployment result, browser visual review or real iPhone/Android/15.6-inch desktop QA is claimed.

## Manual acceptance steps

1. Replace the deployed GitHub Pages source with the contents of `TOEIC_Dictionary_v2.84.1_FullSource.zip` and wait for GitHub Actions/Pages to finish.
2. Open the app and confirm the sidebar/footer shows v2.84.1; hard refresh or use the PWA update flow if the previous Service Worker is still active.
3. Open Robot Buddy and ask **“Bạn là ai?”**. Confirm the response introduces the developer and states that local progress can be analyzed without sending it outside the device.
4. Ask **“Tiến độ học của tôi”**. Confirm the response shows Cần học, Cần luyện and Cần ôn based on the device's own records. A fresh profile should report insufficient evidence rather than inventing weaknesses.
5. Switch **Phân tích tiến độ** off; ask the same question. Confirm Robot explains the feature is disabled while menu help and ordinary conversation still work. Turn it back on afterward.
6. Ask Robot to explain Trang chủ, Lộ trình học, Từ vựng, Ôn tập, Thi thử TOEIC, Flashcard, Ngữ pháp, Đọc hiểu, Nghe, Cấu hình and Quản lý dữ liệu; verify the suggested destination is correct.
7. Compare existing vocabulary/Flashcard/Grammar/Reading/Listening/Foundation/Mock progress before and after. Confirm no progress is lost or rewritten.
8. Test the Robot panel at desktop 15.6-inch / 100% zoom and on iPhone/Android; verify the new header toggle buttons do not overflow and idle prompts do not interrupt learning, audio or timed Mock Exam.

## Release status

**Local source candidate prepared; owner acceptance pending.** Continue to the next TOEIC roadmap items only after the user confirms v2.84.1 passes manual acceptance.
