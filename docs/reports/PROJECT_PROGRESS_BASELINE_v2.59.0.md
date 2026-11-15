# Project Progress Baseline — v2.59.0

## Target coverage

| Metric | Result | Progress | Interpretation |
|---|---:|---:|---|
| Vocabulary minimum | 992/3,000 | 33.1% | Canonical headword quantity only |
| Objective groups with resources | 10/10 | 100% | Availability, not content mastery |
| Canonical resource links | 281/281 | 100% | Link coverage |
| Learning-outcome criteria framework | 30/30 | 100% | Criteria defined, not learner attainment |
| TOEIC objective groups with practice evidence | 9/10 | 90% | Instrumentation coverage |
| TOEIC groups with recall scheduling | 9/9 | 100% | Wired groups only |
| TOEIC groups with response-time capture | 9/9 | 100% | Wired groups only |
| TOEIC groups with explanation self-report | 1/9 | 11.1% | Part 5 self-report; not independently graded |
| Foundation recognition bank | 30/30 | 100% | 3 stable checks in each of 10 lessons |
| Foundation contextual application | 10/10 | 100% | One contextual MCQ per lesson |
| Foundation short-reading passages | 10/10 | 100% | One short passage per existing lesson |
| Foundation reading questions | 20/20 | 100% | 2 stable comprehension questions per passage |
| Foundation learner reading threshold | Not measured | — | Requires actual attempts on the learner's device |

## Foundation reading content profile

- 10 original beginner passages mapped one-to-one to the existing 10 Pre-A1/A1 lessons.
- 20 stable question IDs. Mix: 15 explicit-detail, 2 main-idea, 2 simple-purpose and 1 simple-inference question.
- Answer positions balanced across A/B/C/D: 5 each.
- Each passage is approximately 20–90 words and uses everyday/workplace contexts. Text length is an editorial design target, not a standardized reading-level certification.
- Evidence is stored separately in `toeic:foundation-reading-progress:v1`. Each unique question contributes once to coverage; retries append attempt history and update latest correctness.
- Local practice threshold: 2 unique questions and at least 80% latest-result accuracy. This is only a practice gate, not CEFR certification or broad reading mastery.

## Evidence and compatibility semantics

- Recognition, contextual application and short-reading evidence are three separate ledgers; none inflates the denominator of another.
- Reading retries update latest correctness and append attempt history. They do not increase unique-question coverage.
- No existing lesson, recognition-question or application-task IDs were changed.
- No IndexedDB schema migration, profile reset or import/export behavior change.
- Service Worker REQUIRED and APP_SHELL include the new reading JSON and evidence module.
- Learner achievement is not measured in this source-only snapshot; no personal localStorage profile was imported.

## Verification status

- 16/16 JavaScript regression scripts PASS.
- 20/20 focused Python tests PASS (Foundation reading, Foundation pathway, learning-start-level, PWA readiness and CI coverage).
- Vocabulary validator: 992 records, 0 errors, 0 warnings.
- Learning-content validator: 0 errors, 8 known missing-Part-1-JPG warnings (SVG fallback remains).
- Version synchronization: PASS.
- Remote GitHub Actions, Pages deployment and physical-device QA: not run / not verified.
- A pre-existing Part 1 content fingerprint test remains known to fail for `part1-meeting-documents`; this unrelated legacy discrepancy was not changed or waived in v2.59.0.
