# Project Progress Baseline — TOEIC Dictionary v2.65.0

**Date:** 2026-11-15  
**Source:** local GitHub-only PWA candidate  
**Previous base:** v2.64.0

## Product progress snapshot

The generated target inventory is in `PROJECT_PROGRESS_SNAPSHOT_v2.65.0.md`.

- Vocabulary: 992 / 3,000 minimum = **33.1%**; 992 / 5,000 planning ceiling = **19.8%**. These are record-count ratios only.
- Objective resources: 281 / 281 = **100%** canonical link coverage; 10/10 objective groups have linked resources. This does not imply learner mastery.
- Foundation Listening: 10/10 scripts and 20/20 questions = **100%** current Pre-A1/A1 bank coverage; audio is device TTS, not ETS recordings.
- Foundation A–Z: 26/26 letter records = **100%** content-bank coverage; no pronunciation accuracy or mastery inference.
- Outcome framework: 30/30 criteria defined; not a learner mastery claim.
- TOEIC objective practice evidence: 9/10 groups wired = **90%**; 9/9 currently wired groups include delayed recall and response-time evidence.

## v2.65.0 delivery scope

- Speech Synthesis now waits for a device voice catalog to become available (up to 1.2 seconds), clears residual pending/speaking work after cancellation, and waits a configurable pre-play buffer before the first real utterance.
- Default startup buffer is **750 ms**. The supported UI choices range from 500 ms to 1,500 ms; runtime guard limits the value to 350–1,600 ms.
- Listening Part 1 labels its four sequential statements A–D and uses a separate **1,300 ms** default pause between options. The UI permits 1,000–2,300 ms. Listening Parts 2–4 retain the existing conversation/turn pause setting.
- Vocabulary playback, one-shot vocabulary/flashcard/alphabet pronunciation, Foundation Listening and other shared `speakText()` routes inherit the same readiness/cancel guard.
- Added Reading read-aloud for passage/document content and Part 5 question/choice sets. It uses the same pipeline, live status and Stop behavior.
- Added only two preference values to `appSettings.tts`: `startupDelayMs` and `part1OptionPauseMs`. Existing voice, rate, pitch, volume, word/sentence pauses and learner progress remain intact.

## Test and release status

- Python: **59/59 selected tests PASS** across 10 relevant modules.
- JavaScript: **19/19 regression suites PASS**, including the enhanced Listening/TTS regression.
- JavaScript syntax: all `assets/js/*.js` and `sw.js` pass Node syntax checks.
- Python syntax: all `tools/**/*.py` pass `py_compile`.
- CSS parsing: `assets/css/app.css` and `assets/css/design-system.css` both parse with 0 errors.
- Design profile: 54 tokens and 362 legacy font-floor selector groups synchronized.
- Version synchronization: PASS for manifest, app.js, Service Worker, HTML, README and Master.
- Vocabulary validator: 992 records, 0 errors and 0 warnings.
- Learning-content validator: 0 errors and 8 warnings for missing Part 1 JPG binaries; SVG fallbacks remain.
- Objective resource audit: 281/281 canonical resources linked; learning-outcome audit: 30/30 criteria structurally valid.
- Strict Part 1 image validator: **FAIL**, 1/9 JPG binaries present; the same 8 original licensed files are still missing from this workspace.
- No physical-device audio QA is claimed. Mocked tests prove queue ordering, readiness waits and safe cancellation; they do not prove audible onset quality on iOS/Android/desktop speech engines.

## Baseline interpretation

The release addresses the app-side risk of issuing the first TTS utterance before the device voice catalog/engine is ready, as well as rapid A–D utterance transitions. It cannot control all browser/OS TTS internals; real-device validation is still required. Release deployment remains held by the independent missing Part 1 original JPG binaries and strict validator failure.
