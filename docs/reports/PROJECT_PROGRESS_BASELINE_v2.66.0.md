# Project Progress Baseline — TOEIC Dictionary v2.66.0

## Release scope

This release changes assessment timing and the Mock Exam guidance model while preserving existing learning data.

- Dashboard progress is grouped as `exam → skill → Part`. TOEIC Listening Parts 1–4 and Reading Parts 5–7 use independent full-width rows; the same group contract can accept future Writing, Speaking and IELTS tracks.
- Formative results follow `answer → aggregate summary → explicit confirmation → detailed answer/explanation review`. Selection drafts do not include correctness, answer keys or explanations. Commit/evidence writes occur only after confirmation.
- Mock Exam uses a time-weighted schedule across the full section budget. It reserves a transition/lead-in allowance per question, announces section/Part/question context and moves active focus automatically. Listening audio is played once at group entry, not restarted for each question in the same conversation.

## Target-based progress

- TOEIC vocabulary: 992 / 3,000 minimum = **33.1%**. This is bank size, not learning mastery.
- TOEIC objective-resource links: 281 / 281 = **100% link coverage**; this does not mean outcomes are taught or mastered.
- Current dashboard tracks: 2 / 2 active TOEIC skills (Listening and Reading) = **100% current L+R structure**. Writing, Speaking and IELTS are supported as extensible data groups but are not yet populated active tracks.
- Deferred assessment workflow: 8 / 8 implemented entry paths (single-question Smart Review/Part 5, Flash Quiz, Grammar, Reading, Listening, Foundation, Placement, Mock Exam) = **100% implementation coverage for the currently enumerated flow types**. This is code-path coverage, not learner completion.
- Mock Exam timing modes: 3 / 3 configured (Quick 15 minutes / 25 questions, Half 60 minutes / 100 questions, Full 120 minutes / 200 questions). The scheduled slots include question context and transition allowance and end at the configured section deadline.
- Listening inventory: 107 units / 201 questions; Reading: 51 resources / 200 questions; Grammar: 33 lessons / 86 exercises. No approved total content target exists, so expansion percentages are **not measurable**.

## Verification

- JavaScript regression: **21 / 21 suites PASS**.
- Focused Python checks: **259 / 259 test cases PASS across 36 modules**. This is a selected test set, not a claim that the entire Python test discovery completed.
- `sync-version.py --check`: PASS.
- `sync-design-profile.py --check`: PASS (54 tokens; 362 legacy font-floor selector groups).
- Vocabulary validation: 992 records; **0 errors, 0 warnings**.
- Learning-content validation: **0 errors, 8 missing original Part 1 JPG warnings**; SVG fallbacks remain present.
- JavaScript syntax checks: `sw.js` and all `assets/js/*.js` PASS.
- CSS parsing: `assets/css/app.css` (1,503 top-level rules) and `assets/css/design-system.css` (266 top-level rules) PASS.
- Full `test_validator.py` / broad validator discovery exceeded the execution time limit and is not counted as passing.

## Not measured / outstanding

- Actual learner mastery, TOEIC score prediction, CEFR certification and learning transfer are not measured by structural coverage.
- Browser-rendered desktop/mobile review and physical-device tests remain outstanding.
- Actual OS Speech Synthesis timing, pronunciation and audible transitions require real devices; automated tests validate application ordering and cancellation behavior only.
- GitHub Actions and GitHub Pages deployment are not verified from this workspace.
- Strict Part 1 photo validation is still blocked: **1/9 original JPGs present; 8 missing**, including `part1-photocopier.jpg`. Keep the validator enabled and preserve the original assets already in the remote GitHub repository when merging source.

## Data preservation

- No IndexedDB schema/store migration was introduced.
- No vocabulary/question/lesson stable IDs or answer keys were changed.
- Existing answer history, user vocabulary, preferences and learner progress are preserved.
- Draft selections and pending mock summaries use additive fields/keys; they are not committed as completed learning evidence until confirmation.
