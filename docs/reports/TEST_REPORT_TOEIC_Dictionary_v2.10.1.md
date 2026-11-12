# Test report — TOEIC Dictionary v2.10.1

**Build:** v2.10.1 — Smart Review Wait Modal, Laptop Flashcard Layout & Daniel en-GB Priority  
**Date:** 2026-11-09  
**Base:** v2.10.0 ZIP  
**Runtime:** Python 3.13.5; Node.js 22.16.0

## Automated test results

| Test module/check | Cases | Result | Execution note |
|---|---:|---|---|
| `test_baseline_ids.py` | 13 | PASS 13/13 | Grouped run |
| `test_patch_data.py` | 11 | PASS 11/11 | Grouped run |
| `test_sync_version.py` | 12 | PASS 12/12 | Each test case was run individually after the combined command was unstable |
| **Confirmed unit tests in this patch run** | **36** | **PASS 36/36** | Does not include the validator unit suite |
| `python tools/validate-data.py` | 928 records | PASS | 0 ERROR; 12 known legacy warnings (DF005=3, EX006=1, FD001=8 violations across 7 records) |
| `python tools/sync-version.py --check` | 8 markers | PASS | Manifest, Service Worker, HTML, README, Master and Changelog all identify 2.10.1 |
| JavaScript syntax | all project JS | PASS | `node --check` for `assets/js/app.js` and `sw.js` |
| Python compile | 3 tools | PASS | validator, sync-version and patch-data |

The 33 validator unit tests were not rerun as a full suite in this patch turn. The validator implementation was unchanged from v2.10.0, whose grouped report recorded 33/33 PASS. This patch's actual-data validator CLI was rerun and passed.

## Implemented changes

- Smart Review: after the learner confirms the explanation with OK, auto-next opens a dedicated waiting modal showing an animated loader, circular countdown, progress bar and status message. The modal cannot be dismissed by backdrop/Escape while waiting. The learner can cancel the countdown and use the manual Next button. Disabling auto-next closes the wait modal and enables manual navigation.
- Session restore: `practiceSession.autoAdvanceWaiting` restores the pending state and wait modal after reload. The progress-ring duration is reset to the configured 3/5/10-second delay, so its visual progress matches the real timer.
- Flashcard: container-aware layout stacks vertically when the available card width is narrow; fixed image aspect ratio, `object-fit: contain`, `min-width: 0`, bounded content and inner scrolling prevent long vocabulary details from widening the card. Wider cards retain a balanced two-column layout.
- TTS: if no male voice URI has been manually saved and the device offers `Daniel — en-GB`, it is preferred as the male fallback. A manually chosen URI retains priority; female default behavior is unchanged. The selected voice's own locale is applied to the utterance.
- Vocabulary and personal data: no base vocabulary records, IDs, schema or study progress were changed in this UX patch.

## Static and package checks

- `data/manifest.json`: version 2.10.1; all 8 version marker locations are synchronized.
- HTML: 201 IDs, all unique.
- CSS/JS assertions: wait modal, cancel action, correct countdown duration after restore, Daniel en-GB preference, chosen voice locale, Flashcard container query, bounded image frame and internal scrolling all present.
- Service Worker app shell: 65 listed resources; 0 missing files (38 required + 27 optional).
- ZIP package: 112 files at archive root; `ZipFile.testzip()` returned no corrupt entry.
- Re-extracted package: `sync-version.py --check`, `validate-data.py`, `node --check assets/js/app.js`, `node --check sw.js` and `py_compile` all PASS.
- Compared against the v2.10.0 base ZIP: all `data/` content files except the intentionally version-bumped `data/manifest.json` are byte-identical; all 928 IDs and the ID/quality baseline files are retained.

## Not yet verified

- Visual regression/browser interaction test: attempted with headless Chromium, but the execution environment blocked navigation to the local HTTP test server (`ERR_BLOCKED_BY_ADMINISTRATOR`). Therefore no visual browser pass is claimed.
- iPhone Safari, including Daniel en-GB voice availability and perceived male-voice clarity. The app can select Daniel only when iOS exposes that voice to Web Speech API.
- Android Chrome and physical desktop/laptop viewport/zoom QA.
- GitHub Actions on the remote repository, GitHub Pages deployment and production Service Worker/cache behavior.

Do not mark these target-environment checks as passed until performed on the actual devices/repository.
