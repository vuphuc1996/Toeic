# Test Report — TOEIC Dictionary v2.71.0

- Date: 2026-11-16
- Release: **v2.71.0**
- Scope: Batch 012 vocabulary data, reciprocal word-family relationships, IPA ledger, release migration profiles, progress reporting, Part 1 recovery tooling and retained learning-content regressions.

## 1. Focused Python unit tests

**100 tests passed across 11 selected Python test modules.**

| Module | Tests | Result |
|---|---:|---|
| `test_cmudict_ipa_backfill.py` | 5 | PASS |
| `test_vocabulary_family_links.py` | 5 | PASS |
| `test_project_progress.py` | 4 | PASS |
| `test_part1_photo_restore.py` | 3 | PASS |
| `test_vocabulary_batch_012.py` | 4 | PASS |
| `test_ci_coverage.py` | 2 | PASS |
| `test_sync_version.py` | 12 | PASS |
| `test_part1_photo_assets.py` | 5 | PASS |
| `test_learning_content.py` | 34 | PASS |
| `test_vocabulary_detail_examples.py` | 13 | PASS |
| `test_baseline_ids.py` | 13 | PASS |
| **Total** | **100** | **PASS** |

`test_vocabulary_detail_examples.py` was updated for the current 1,137-headword manifest and now confirms that Batch 012 stable IDs are present. `test_ci_coverage.py` confirms every Python test module and JavaScript regression file is invoked by the CI workflow. A separate broad loop over 22 modules exceeded the local execution limit and is not counted as a pass.

## 2. JavaScript regression and syntax

- **21/21 JavaScript regression suites PASS**.
- `node --check assets/js/app.js`: PASS.
- `node --check sw.js`: PASS.
- Vocabulary release-integrity regression: PASS — 1,137 records; unique headwords/IDs; cumulative migration repair for 979, 992, 1,026, 1,063 and 1,100-headword snapshots; batches 008–012.

## 3. Data and release checks

| Check | Result |
|---|---|
| `python tools/validate-data.py` | PASS — 1,137 records; 0 errors; 0 warnings |
| `python tools/cmudict_ipa.py --check` | PASS — 333 source-linked IPA records |
| `python tools/audit-toeic-coverage.py` | PASS — coverage report generated |
| `python tools/sync-version.py --check` | PASS — all markers synchronized to 2.71.0 |
| `python tools/sync-design-profile.py --check` | PASS — 54 tokens and 361 legacy font-floor selector groups |
| Python compile checks for recovery tooling and new tests | PASS |

## 4. Learning media and photo release gate

`python tools/validate-learning-content.py` reports **0 errors and 8 warnings**. Each warning names one of the eight original repository-owned Part 1 Pexels JPG files missing from this workspace.

The strict command `python tools/validate-part1-photo-assets.py` reports **1/9 valid photo files and 8 missing-file errors**; it exits with code 1. The strict gate remains enabled. No replacement or generated photo was created.

The archive includes `tools/restore_part1_photos.py`, which downloads all eight approved original Pexels assets in a single run from `assets/listening/ATTRIBUTION.csv` when the CDN is reachable; it validates the JPEG signature/dimensions and does not overwrite existing files. `restore-part1-photos.bat` is included as a Windows launcher. The restore script is not a substitute for the missing image binaries: those eight original JPEG bytes are not embedded in this archive.

## 5. Deployment status

- Local vocabulary/data and selected regression checks: PASS.
- Strict Part 1 photo gate: **FAIL — 8 original JPG binaries missing**.
- Broad Python test discovery: exceeded local execution limit; no pass claim.
- Remote GitHub Actions: not run/verified from this workspace.
- GitHub Pages deployment: not verified.
- Physical iOS/Android/desktop responsive, speech and playback QA: not performed.

Release state: **local release candidate / deployment hold**. Do not label v2.71.0 production-ready until all original JPG binaries are restored and strict validation plus remote CI/deployment checks pass.
