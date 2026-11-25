# Test Report — TOEIC Dictionary v2.95.63

- Date: 2026-11-25
- Exact source baseline: `TOEIC_Dictionary_v2.95.62_FullSource.zip`
- Baseline SHA-256: `b9d56cd27d0d13c4c8781732ac72c17b526b2aa451fa1393c39fd30820260f96` (matched the supplied `.sha256` sidecar; ZIP CRC and one-root archive check passed before editing).
- This report covers the v2.95.63 local implementation. It does not claim a hosted GitHub Actions run or device/browser acceptance.

## Scope verified

1. GitHub Actions Batch 035 Python test selection now uses `test_related_glossary_batch_035*.py`. This matches the unittest discovery glob semantics for both `test_related_glossary_batch_035.py` and a split module named `test_related_glossary_batch_035_cambridge.py`. The current v2.95.62 source archive did not contain the split module itself; the user's remote error therefore could not be reproduced from this exact checkout, but the workflow defect was confirmed (the old exact-name selector could not match the split filename) and the corrected glob is covered by `test_ci_coverage.py`.
2. `modalBackdrop` close lifecycle: the result modal, answer-explanation review modal and auto-advance wait modal expose visible close controls and use one state-aware dispatcher for X/Escape. Backdrop clicks remain intentionally ignored while a result is pending; explicit X/Escape remain usable.
3. Result modal: existing completion view continues to report **Đúng / Chưa đúng / Tổng câu** before answer/explanation reveal. Closing a pending result calls the existing confirm/save route; for a single practice answer this commits the learning progress and leaves the explanation/feedback inline rather than opening another blocking modal. Closing review preserves the saved answer and allows manual next-question flow. Closing the wait dialog cancels the auto-next timer and retains the current question.
4. `modalActionInProgress` prevents repeated confirmation calls while persistence is in progress. Modal reset clears the modal type, stale review/wait/detail classes and content. Focus is moved to the explicit close button when result/wait dialogs open.

## JavaScript regression suites

- **43/43 Node `.mjs` regression scripts PASS**, including `modal-dismissal-workflow.mjs`, `assessment-deferred-workflow.mjs`, `runtime-render-smoke.mjs`, `learning-focus-workspace.mjs`, `practice-progress.mjs`, `service-worker-update.mjs` and all existing suites.
- Modal regression checks: 1/0/1 single-answer statistics and 8/2/10 multi-question completion statistics render; close is visible and focused; closing a result commits the pending answer; closing review persists the session and removes the overlay; closing wait cancels auto-next; regular close clears stale overlay classes; click and Escape listeners route through the same dispatcher.
- `node --check` on the ES-module app source and service worker: PASS.

## Focused Python regression suites

**42/42 tests PASS across 8 modules:**

| Module | Tests | Result |
|---|---:|---|
| `test_ci_coverage.py` | 4 | PASS |
| `test_repository_integrity.py` | 1 | PASS |
| `test_pwa_readiness.py` | 3 | PASS |
| `test_responsive_layout.py` | 8 | PASS |
| `test_learning_surface_consistency.py` | 5 | PASS |
| `test_practice_mode_fallback.py` | 6 | PASS |
| `test_sync_version.py` | 12 | PASS |
| `test_package_source.py` | 3 | PASS |
| **Total** | **42** | **PASS** |

- Python syntax compilation: **99/99 paths** from the explicit GitHub Actions `py_compile` command PASS.

## Validators and release checks

| Check | Result |
|---|---|
| `tools/audit-repository-integrity.py` | PASS — 443 local references/data files inspected; 0 errors, 0 optional warnings |
| `tools/validate-data.py` | PASS — 1,141 records; 0 ID additions / 0 removals; 0 errors / 0 warnings; ID-set SHA remains `adccbdb4c9887220…` |
| `tools/validate-learning-content.py` | PASS — Listening 145 units / 295 questions; Reading 73 / 287; Grammar 58 / 169; 0 errors / 0 warnings |
| `tools/validate-part1-photo-assets.py` | PASS — 9/9 files; 0 missing-photo warnings |
| `tools/sync-version.py --check` | PASS — all 13 version markers and changelog entry synchronized to 2.95.63 |
| `tools/sync-design-profile.py --check` | PASS — 54 tokens and 406 legacy font-floor selector groups |
| `git diff --check` | PASS |
| Protected data comparison against v2.95.62 | PASS — only `data/manifest.json` changed, and only its release version marker; every other `data/**` file is byte-identical |

The read-only Related Glossary quality audit remains 567 rows / 157 flagged (103 missing definitions, 50 placeholders, 153 missing POS, 52 missing provenance; 0 duplicate normalized-term groups). No glossary row was changed in v2.95.63.

## Not run / unverified

- The complete Python unittest inventory was **not run**. Only the eight focused modules listed above were executed; full discovery and its aggregate pass/skip/error counts are not claimed.
- The reported remote GitHub Actions failure was not re-run on GitHub from this environment. The workflow glob and local CI coverage regression were verified locally.
- GitHub Pages deployment, real installed-PWA service-worker cache propagation, offline reload, cross-tab behavior, Safari/iOS/iPadOS/Android and physical-device modal interaction were not run.
- Human acceptance is still required for the modal interaction on actual desktop and mobile browsers.

## Suggested manual acceptance

1. Open Review or TOEIC Part 5 and answer a question. Verify the completion modal shows Đúng, Chưa đúng and Tổng câu. Check that X is visible and receives focus.
2. Press Escape or click X. Verify the answer is saved, the overlay disappears, inline answer feedback remains available, and Next can be used. Reopen a new question and use **Xác nhận & xem đáp án** to verify the full explanation path still works.
3. In a multi-question Grammar/Reading/Listening/Foundation exercise, answer all questions and open the completion summary. Verify counts match the completed set; close with X/Escape and ensure the answer review is still available.
4. With auto-next enabled, acknowledge the explanation to open the countdown. Close with X/Escape; the timer must stop and the current question must remain available for manual navigation.
