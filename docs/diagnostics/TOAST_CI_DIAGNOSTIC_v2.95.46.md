# v2.95.46 Toast / CI Diagnostic Update (Candidate)

Status: **development candidate; not a production release**

## Toast change
- Success toast now uses `role=status`; error toast uses `role=alert`.
- Adds a keyboard-focusable close button labeled `Đóng thông báo`.
- Keeps automatic dismissal and extends the timeout to 5 seconds.
- Long text can wrap; close control has hover and focus-visible styles.
- Adds a regression test in `tools/tests/test_visual_composition.py`.

## Verified checks
- `node --check assets/js/app.js`: PASS
- `python -m unittest discover -s tools/tests -p 'test_visual_composition.py' -v`: 9/9 PASS
- `python -m unittest discover -s tools/tests -p 'test_patch_data.py' -v`: 20 PASS, 1 skipped (Git metadata required)
- `python tools/audit-repository-integrity.py`: PASS, 420 local references/data files inspected, 0 errors, 0 optional warnings
- `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v`: 3/3 PASS
- `python tools/validate-data.py`: PASS, 0 errors/warnings
- `python tools/validate-learning-content.py`: PASS, 0 errors/warnings
- `python tools/validate-part1-photo-assets.py`: PASS, 9/9
- `python tools/sync-version.py --check`: PASS, all version markers v2.95.46
- CI workflow inventory: 86 py_compile targets present; 91 unittest discovery patterns each match a test module.

## Incomplete
- Full `python -m unittest discover -s tools/tests -v` exceeded the execution time limit; the log is partial and cannot be treated as a completed run.
- Remote GitHub Actions run, browser/device checks, and production deployment are not verified.
- The generic CI exit code 1 is not reproduced locally; a GitHub Actions run log is still needed to isolate its exact failing step.

## Preservation
- No canonical vocabulary IDs/headwords/relations, question/choice IDs, answer keys, Mock eligibility, IndexedDB schema, learner progress, or UI layout were intentionally changed.
