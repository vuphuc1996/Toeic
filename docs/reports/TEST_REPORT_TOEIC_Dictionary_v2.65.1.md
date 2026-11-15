# Test Report — TOEIC Dictionary v2.65.1

**Scope:** hotfix for `refreshSpeechVoiceSelectors()` missing declaration in v2.65.0.  
**Environment:** local source workspace; Node.js and Python. Real browser/device audio output was not available.

## Defect

The v2.65.0 app still called `refreshSpeechVoiceSelectors()` from `bindPracticeEvents()`, `bindTtsSettings()`, the `voiceschanged` event and `syncSettingsUI()`, but the function declaration was missing from `assets/js/app.js`. This caused the observed startup failure:

`ReferenceError: refreshSpeechVoiceSelectors is not defined`

The helper existed in v2.64.0, confirming a declaration omission during the v2.65.0 TTS refactor rather than a device voice-catalogue problem.

## Fix

- Restored `refreshSpeechVoiceSelectors()` beside the other shared speech-voice selection helpers.
- The helper reads the currently available English voice catalog and populates both male and female selectors.
- It keeps the saved `maleVoiceURI` / `femaleVoiceURI` values. If a saved voice URI is not exposed by the current device, the selector retains it as an explicit “voice unavailable on this device” option instead of silently selecting a different voice.
- If the device has no English voice available yet, both selectors are disabled and the settings status explains the situation. The existing `voiceschanged` callback and manual refresh action can populate them later.
- The v2.65.0 `prepareSpeechEngine()` behavior, 750 ms startup delay, Part 1 A–D pauses and Reading playback are unchanged.

## Verification results

| Check | Result |
|---|---:|
| `test_tts_readiness.py` | **10/10 PASS** |
| `test_sync_version.py` | **12/12 PASS** |
| JavaScript regression files | **19/19 PASS** |
| Runtime render / migration smoke | PASS (included in 19 JS suites) |
| TTS voice-selector runtime regression | PASS: empty catalog, populated catalog, saved URI and unavailable saved URI |
| `node --check` on `sw.js` and all `assets/js/*.js` | PASS |
| `python tools/sync-version.py --check` | PASS |
| Vocabulary validator | 992 records; 0 errors; 0 warnings |
| Learning-content validator | 0 errors; 8 missing-JPG warnings |
| Strict Part 1 photo validator | **FAIL: 8 missing original JPG binaries; 1/9 present** |

The JavaScript regression specifically invokes the restored helper in a mocked device environment and confirms that the manual voice setting remains selected. It also confirms a device-missing saved URI is preserved with a visible unavailable label.

## Data and compatibility safety

- No vocabulary record, listening/reading content, stable ID, question/answer, IndexedDB schema/store, personal vocabulary or learning progress was changed.
- No TTS preferences were reset or migrated; existing voice URIs are retained.
- Service Worker and app release version advanced together to v2.65.1 so an installed PWA can fetch the hotfix under a new cache namespace.

## Release limitation

This is a local source hotfix. The strict photo validator still fails because eight licensed Part 1 JPG files are missing from the local archive. Keep the validator enabled and preserve the original files already in GitHub when applying source changes. Real-device audible QA, remote GitHub Actions and GitHub Pages deployment are not claimed.
