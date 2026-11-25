# Test Report — TOEIC Dictionary v2.95.46

- Source basis: user-supplied `TOEIC_Dictionary_v2.95.46_FullSource_Candidate(1).zip`.
- Candidate input SHA-256: `4748288320b17ba4e94b1f5f064288034418ee23d1cc67a739d9614f9f410966`.
- Verification date: 2026-11-24.
- Source Release Acceptance: **PASS WITH SKIPS (policy-accepted)**.
- Production Deployment Acceptance: **UNVERIFIED**.

## Strict Python inventory

| Metric | Result |
|---|---:|
| Discovered modules | 89 |
| Completed modules | 89 |
| PASS modules | 88 |
| PASS WITH SKIPS modules | 1 |
| Test cases collected | 692 |
| Passed | 691 |
| Skipped | 1 |
| Failed / errored / timed out | 0 / 0 / 0 |
| Pending / not run | 0 |

The only skip is `test_repository_gitignore_excludes_audit_logs` in `test_patch_data.py`: the source was tested from a ZIP without Git metadata; the assertion requires a Git clone. The skip reason matches `tools/test-inventory-policy.json` and is accepted, not counted as a pass.

## Release Acceptance commands

| Gate | Status |
|---|---|
| `repository_integrity` | PASS |
| `data_validator` | PASS |
| `learning_content_validator` | PASS |
| `version_sync` | PASS |
| `listening_readiness` | PASS |
| `question_evidence` | PASS |
| `distractor_audit` | PASS |
| `learning_outcomes` | PASS |
| `major_release_audit` | PASS |
| `related_glossary_backlog` | PASS |
| `editorial_review_queue` | PASS |
| `full_python_suite` | PASS |

All 12 Release Acceptance commands returned exit code 0. The full Python suite ran as part of the acceptance sequence.

## GitHub Actions workflow shell replay

- Run steps discovered: 110
- Run steps executed: 110
- PASS: 110; FAIL: 0; TIMEOUT: 0; ERROR: 0; NOT RUN: 0.
- The exact `run:` shell commands in `.github/workflows/validate-data.yml` were replayed locally in order; the replay stopped-on-failure policy was preserved.
- Local runtime: Python 3.13.5 and Node.js 22.16.0. The workflow config requests Python 3.12 and Node.js 24; therefore this is not a same-runtime hosted-runner reproduction.
- CSS design-token audit: 0 new violations; 2,778 pre-existing legacy findings remain warnings.

## Additional final validator evidence

- Repository integrity: 420 references/data files inspected; 0 errors; 0 optional warnings.
- Vocabulary validator: 1,141 canonical records; 0 IDs added/lost; 0 errors; 0 warnings (legacy baseline warnings: 0).
- Learning content validator: Listening 145 units / 295 questions; Reading 73 / 287; Grammar 58 / 169; separate Part 5 practice 80; 0 errors / 0 warnings.
- Part 1 photo assets: 9/9 valid; no missing photo warnings.
- CSS design-token ratchet: 0 new violations; 2,778 pre-existing legacy findings remain warnings.
- Version synchronization: PASS.

## Scope and limitations

- No canonical vocabulary IDs/headwords/relationship arrays, learner question IDs, choice IDs, answer keys, Mock eligibility, or IndexedDB schema/data were edited in this batch.
- The source-level tests and CI shell replay passed locally. GitHub-hosted Actions, actual Pages deployment, deployed artifact/cache propagation, browser/PWA/offline behavior and physical iOS/Android/tablet/desktop checks remain unverified.
- This report is not an independent linguistic review or psychometric certification.
