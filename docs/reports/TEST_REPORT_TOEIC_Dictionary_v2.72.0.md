# Test Report — TOEIC Dictionary v2.72.0

- Date: 2026-11-16
- Release: **v2.72.0**
- Scope: complete Part 1 JPG integration from user-provided source archive, 4:3 landscape normalization, image-size ceiling, CSS/design consistency, PWA resource integrity and retained TOEIC data/content regressions.

## 1. Part 1 image acceptance

- **9/9 JPG files embedded** in `assets/listening/`.
- Every file is **1448×1086 px (4:3 landscape)** and **below 400,000 bytes**.
- `part1-office-cleaning.jpg` is preserved byte-for-byte at 398,363 bytes.
- Eight licensed Pexels photographs were re-encoded from the supplied source images as progressive JPEGs. The portrait `part1-photocopier.jpg` was cropped to landscape with the employee's operating hand and control panel retained.
- Combined image payload: **2,063,272 bytes**, down from **25,265,159 bytes** (**91.8% smaller**).
- Original filenames, local references, item IDs, question IDs, transcripts, choices, answer keys, explanations, source attribution and license rows remain unchanged.

## 2. Python unit tests

**118 tests passed across 13 selected Python test modules.**

| Module | Tests | Result |
|---|---:|---|
| `test_part1_photo_assets.py` | 6 | PASS |
| `test_visual_composition.py` | 8 | PASS |
| `test_sync_version.py` | 12 | PASS |
| `test_pwa_readiness.py` | 3 | PASS |
| `test_ci_coverage.py` | 2 | PASS |
| `test_learning_content.py` | 34 | PASS |
| `test_vocabulary_batch_012.py` | 4 | PASS |
| `test_baseline_ids.py` | 13 | PASS |
| `test_cmudict_ipa_backfill.py` | 5 | PASS |
| `test_vocabulary_family_links.py` | 5 | PASS |
| `test_project_progress.py` | 4 | PASS |
| `test_vocabulary_detail_examples.py` | 13 | PASS |
| `test_remaining_content_review.py` | 9 | PASS |
| **Total** | **118** | **PASS** |

The focused Python selection includes the historical reviewed-data fingerprint checks, confirming that photo binary optimization did not alter question/content fingerprints. It is not a claim that every Python test in the repository was executed in this release run.

## 3. JavaScript regression and syntax

- **21/21 JavaScript regression suites PASS**.
- `node --check assets/js/app.js`: PASS.
- `node --check sw.js`: PASS.
- Service Worker cache version matches the manifest; all nine Part 1 JPGs are listed as optional local assets and can be cached by the PWA when the app is installed/updated online.

## 4. Data, media and release checks

| Check | Result |
|---|---|
| `python tools/validate-data.py` | PASS — 1,137 records; 0 errors; 0 warnings |
| `python tools/validate-learning-content.py` | PASS — 0 errors; 0 warnings |
| `python tools/validate-part1-photo-assets.py` | PASS — 9/9 photos; signature, attribution, dimensions, 4:3 ratio and size ceiling |
| `python tools/cmudict_ipa.py --check` | PASS — 333 source-linked records |
| `python tools/audit-toeic-coverage.py` | PASS — report generated |
| `python tools/report-project-progress.py` | PASS — snapshot generated |
| `python tools/sync-version.py --check` | PASS — all markers synchronized to 2.72.0 |
| `python tools/sync-design-profile.py --check` | PASS — 54 tokens and 361 legacy font-floor selector groups |
| GitHub Actions Python `py_compile` source list | PASS |

## 5. Photo restore utility change

The old `restore-part1-photos.bat` and `tools/restore_part1_photos.py` were removed from the current release. They downloaded full-resolution Pexels originals using `ATTRIBUTION.csv` and validated the JPEG signature/minimum dimensions, but **did not optimize or embed** those files in an archive. With the optimized 9/9 image set now embedded in Full Source, running that downloader would be unnecessary and could reintroduce multi-megabyte originals. Historical v2.71.0 documentation remains as the record of that earlier recovery attempt.

## 6. Deployment status and limitations

- Local source/data/media gates: **PASS** for the checks listed above.
- Remote GitHub Actions: not run/verified from this workspace.
- GitHub Pages deployment: not verified.
- Physical iOS/Android/desktop image rendering and listening playback QA: not performed.

Release state: **local release candidate**. The prior eight-image media blocker is resolved in the packaged source, but remote CI/deployment and real-device QA remain unverified; this report does not claim production deployment.
