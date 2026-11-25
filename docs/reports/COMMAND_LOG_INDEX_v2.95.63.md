# Command Log Index — v2.95.63

Date: 2026-11-25. Working root was cleanly extracted from the verified v2.95.62 FullSource and compared to that exact predecessor before release changes.

## Baseline verification

- `sha256sum TOEIC_Dictionary_v2.95.62_FullSource.zip` — matched sidecar `b9d56cd27d0d13c4c8781732ac72c17b526b2aa451fa1393c39fd30820260f96`.
- `unzip -t` / `zipfile.testzip()` — PASS; one root directory, 753 files.
- `python tools/audit-repository-integrity.py` before edits — 442 entries, 0 errors / 0 warnings. The GitHub Actions split Cambridge module named in the user log was not present in this v2.95.62 archive.

## CI and modal regression commands

```bash
node --check /tmp/toeic-app-v29563.mjs
node tools/tests/modal-dismissal-workflow.mjs
node tools/tests/assessment-deferred-workflow.mjs
node tools/tests/runtime-render-smoke.mjs
node tools/tests/learning-focus-workspace.mjs
node tools/tests/practice-progress.mjs
```

- Full Node suite: looped over every `tools/tests/*.mjs` file after the v2.95.63 version sync — **43/43 PASS**.
- The new `modal-dismissal-workflow.mjs` is registered in `.github/workflows/validate-data.yml`; it asserts single-question (1/0/1) and completed ten-question (8/2/10) statistics as well as X/Escape persistence and dismissal paths.

## Focused Python commands

```bash
python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v
python -m unittest discover -s tools/tests -p 'test_repository_integrity.py' -v
python -m unittest discover -s tools/tests -p 'test_pwa_readiness.py' -v
python -m unittest discover -s tools/tests -p 'test_responsive_layout.py' -v
python -m unittest discover -s tools/tests -p 'test_learning_surface_consistency.py' -v
python -m unittest discover -s tools/tests -p 'test_practice_mode_fallback.py' -v
python -m unittest discover -s tools/tests -p 'test_sync_version.py' -v
python -m unittest discover -s tools/tests -p 'test_package_source.py' -v
```

All eight modules passed, 42/42 test cases. The GitHub Actions Python syntax inventory was extracted from the workflow and passed `python -m py_compile` for 99/99 declared paths.

## Validators

```bash
python tools/audit-repository-integrity.py
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/validate-part1-photo-assets.py
python tools/sync-version.py --check
python tools/sync-design-profile.py --check
git diff --check
```

All commands passed. Exact counts and unverified scopes are recorded in `TEST_REPORT_TOEIC_Dictionary_v2.95.63.md`.

## Version bump and release

```bash
python tools/sync-version.py --dry-run --set 2.95.63
python tools/sync-version.py --set 2.95.63 --apply
python tools/sync-version.py --check
```

Package generation, archive integrity, patch application, byte-for-byte replay and SHA-256 commands are recorded in `PACKAGE_VERIFICATION_v2.95.63.md`.

## Deliberately not claimed

Full Python suite, remote GitHub Actions, deployed GitHub Pages, PWA offline/cache propagation, and physical-device modal tests were not run.
