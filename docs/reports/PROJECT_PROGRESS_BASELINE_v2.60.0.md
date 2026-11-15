# Project Progress Baseline — v2.60.0

## Target coverage

| Metric | Result | Progress | Interpretation |
|---|---:|---:|---|
| Canonical GitHub vocabulary | 992/992 | 100% | Runtime/build integrity against current manifest; not editorial approval |
| Vocabulary minimum target | 992/3,000 | 33.1% | Canonical headword quantity only |
| Vocabulary planning ceiling | 992/5,000 | 19.8% | Planning ceiling coverage, not a quality score |
| Objective groups with resources | 10/10 | 100% | Availability, not mastery |
| Canonical resource links | 281/281 | 100% | Link coverage |
| Learning-outcome criteria framework | 30/30 | 100% | Criteria defined, not learner attainment |
| TOEIC objective groups with practice evidence | 9/10 | 90% | Instrumentation coverage |
| TOEIC groups with recall scheduling | 9/9 | 100% | Wired groups only |
| TOEIC groups with response-time capture | 9/9 | 100% | Wired groups only |
| TOEIC groups with explanation self-report | 1/9 | 11.1% | Part 5 self-report; not independently graded |
| Foundation recognition bank | 30/30 | 100% | Three stable checks in each of 10 lessons |
| Foundation contextual application | 10/10 | 100% | One contextual MCQ per lesson |
| Foundation short-reading passages | 10/10 | 100% | One short passage per existing lesson |
| Foundation reading questions | 20/20 | 100% | Two stable comprehension questions per passage |
| Foundation learner reading threshold | Not measured | — | Requires actual learner attempts |

## Vocabulary release-integrity diagnosis

- Canonical source contains 992 unique headwords across 26 A–Z JSON files; every per-letter count and the manifest total agree.
- The 13 release additions that bridge the known 979→992 gap are explicitly listed in `data/manifest.json` and match `data/vocabulary/batch-008.json` by stable ID.
- v2.59.0 used cache-first for all `/data/` requests, which could return stale JSON even when the app called `fetch(..., {cache: 'no-store'})`; the Service Worker did not honor that cache option.
- The previous legacy migration treated records absent from an older workspace snapshot as deleted base words. A 979-word snapshot could therefore hide all 13 newer records.
- v2.60.0 uses versioned request keys, validates manifest/per-letter/total counts and uniqueness at runtime, reloads after a Service Worker controller swap, and repairs only the exact 979→992 migration fingerprint. Other hidden base words and personal edits/additions are preserved.
- Dashboard reports canonical GitHub count separately from effective visible count and local hidden/add/edit counts.

## Inventory (no approved numeric target)

| Workstream | Current inventory | Progress |
|---|---:|---|
| Grammar | 33 lessons / 86 exercises | Chưa đo được — no agreed total lesson target |
| Listening | 107 units / 201 questions | Chưa đo được — no agreed unit/question target |
| Reading | 51 resources / 200 questions | Chưa đo được — no agreed resource/question target |
| Separate Part 5 practice | 80 questions | Chưa đo được — independent review remains separate |

## Verification status

- JavaScript regression scripts: 17/17 PASS.
- Focused Python tests: 33/33 PASS across version sync, PWA readiness, responsive layout, project progress and Foundation pathway/reading.
- Full Python discovery was attempted but exceeded the 240-second execution window during the existing baseline-ID suite; it is not claimed as a full-suite pass.
- `tools/validate-data.py`: 992 records, 0 errors, 0 new warnings.
- `tools/validate-learning-content.py`: 0 errors, 8 known missing-Part-1-JPG warnings; SVG fallbacks remain.
- Objective resource map: 281/281; outcome criteria: 30/30.
- Version synchronization: PASS.
- Remote GitHub Actions, Pages deployment, iOS installed-PWA update behavior and physical-device QA: not run / not verified.

## Reporting rule

Inventory coverage, data integrity, content quality and learner attainment are separate measures. A 100% source-integrity result means the files agree with the manifest; it does not mean all vocabulary has passed editorial review or that the learner has mastered it.
