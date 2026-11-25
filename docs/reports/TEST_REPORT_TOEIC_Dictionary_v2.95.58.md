# Test Report — TOEIC Dictionary v2.95.58

## Scope

- Sole development baseline: `TOEIC_Dictionary_v2.95.57_FullSource.zip`.
- Baseline SHA-256: `2ccae0e8c00e8e79dfbfb4b80d071d09cf86b8608236ee59241e9fc54e0db104`.
- Change: derive first-attempt accuracy separately from latest-attempt accuracy using existing attempt history. No learner schema or storage write-path change.
- Current evidence report: `TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.58.md`.

## Verified results

| Check | Result | Detail |
|---|---|---|
| Node regression scripts | PASS | 42/42 scripts exit code 0 |
| Focused Python tests | PASS | 17/17 across answer-position balance, learning outcome progress, outcome registry and question evidence |
| Data validator | PASS | 1,141 records; 0 ID additions/removals; 0 ERROR; 0 WARNING |
| Learning outcome registry audit | PASS | 11/11 objectives; 33 criteria; 6/33 have an evidence-collection path; 6/6 Foundation outcomes instrumented |
| Question evidence audit | PASS | 582 questions indexed: 193 reserve Listening + 389 non-reserve; classifications recorded in the generated report |
| Version synchronization | PASS | 13 registered markers + changelog at 2.95.58 |
| JavaScript syntax | PASS | `sw.js` and all `assets/js/*.js` syntax checks exit 0 |
| Mock score readiness regression | PASS | Same-form gate, distinct forms, overlap caution, legacy fail-closed and Reading independence |
| Full Python discovery | INCOMPLETE | Command exceeded the 300-second execution limit. 337 test result lines were emitted before termination; no terminal unittest summary was produced, so no full-suite pass/fail total is claimed. |

## Failed invocation corrected

- Initial focused Node run exposed an incorrect new test expectation (the first-attempt metric correctly remained 100% while latest-attempt accuracy was 90%). The assertion was corrected to reflect the intended separate metrics; the rerun passed.
- Initial unittest module invocation omitted `PYTHONPATH=tools/tests`, causing one import error. Re-run with `PYTHONPATH=tools/tests` passed all 17 focused tests.
- These invocation errors are retained in the command log; they are not represented as passing attempts.

## Behavioral guarantees

- `firstAttemptItems` includes only records with a valid explicit first attempt.
- `firstAttemptCorrect`, `firstAttemptAccuracy`, and `firstAttemptAccuracyPercent` are separate from existing latest-attempt fields.
- A retry does not inflate the unique-item denominator or overwrite the first attempt.
- Records without usable attempt history are excluded from first-attempt metrics rather than guessed from latest results.
- Existing learner records are read as-is. No IndexedDB schema, object-store, vocabulary/question IDs, answer keys, choice identity, Mock eligibility, reserve status, UI, or Robot Buddy permission changed.

## Remaining acceptance gates

- Full Python discovery: incomplete due runtime timeout.
- Hosted GitHub Actions, GitHub Pages deployment, installed-PWA cache propagation, physical iOS/iPadOS/Android QA: unverified.
- Difficulty calibration and independent semantic review remain open; lexical evidence classification is not psychometric calibration or proof of one-best-answer uniqueness.
