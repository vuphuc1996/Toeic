# Project Progress Baseline — v2.58.0

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
| Foundation contextual application tasks | 10/10 | 100% | One contextual MCQ per lesson |
| Foundation learner practice threshold | Not measured | — | No personal profile imported; must be measured on learner device |

## Evidence semantics

- Recognition and contextual application use separate ledgers within `toeic:foundation-progress:v1`.
- Application retries update latest correctness and append attempt history. They never increase recognition unique-question counts.
- The recognition threshold remains at least 3 unique checks and 80% latest-result accuracy. Application tasks do not automatically confer a lesson pass.
- All Foundation application items are contextual multiple-choice checks. No free-form production, listening comprehension, speaking, writing or spontaneous interaction is scored.
- No IndexedDB schema migration, stable lesson/question ID replacement or personal progress reset was introduced.
