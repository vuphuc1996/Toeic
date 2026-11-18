# Voice Playback Regression — v2.94.0

**Scope:** browser-local SpeechSynthesis used by TOEIC Listening, Reading, Foundation and vocabulary read-aloud.

## Changes

- Removed duplicate legacy `speakText()` and `speakUtterance()` declarations. Before the repair, the later declarations shadowed the guarded implementation.
- First utterance is queued synchronously in the user click/tap stack. No fixed two-second startup timer or asynchronous `voiceschanged` wait blocks the first `speechSynthesis.speak()` call.
- Voice catalogue is queried synchronously and can refresh via `voiceschanged`. A transient exception or empty catalogue is handled as an unavailable catalogue; the app sends an utterance with the requested English locale and lets the browser use its system voice.
- If a named/selected voice raises a synthesis error, the app attempts one fallback utterance with the browser's system voice. It does not retry cancellation/interruption. A per-attempt sequence guard ignores stale callbacks from the failed utterance, and the fallback path does not call `cancel()` (which can itself emit a delayed cancellation event on some engines). Utterance-constructor exceptions are handled as visible playback failures.
- A start watchdog reports failure when the browser does not send `onstart` within 10 seconds. An end watchdog handles engines that begin but never send `onend`.
- Errors for permission, unavailable voice/language, network and synthesis are translated into actionable Vietnamese messages. Stop/cancel settles the active promise and clears watchdog timers.
- Listening Part 1 lead-in/label pacing and configured inter-speaker pauses remain intact. Reading uses the same guarded one-shot pipeline.

## Local regression evidence

- `tools/tests/listening-tts-regression.mjs`: PASS. Covers empty and throwing voice catalogues, immediate queue, selected-voice failure and one system-default retry, stale callbacks/cancellation-event race, throwing utterance constructor, 10-second start watchdog, cancellation, Part 1 pacing, vocabulary, Foundation and Reading read-aloud.
- `tools/tests/test_tts_readiness.py`: 14/14 PASS.
- `node --check assets/js/app.js`: PASS.

## Device acceptance still required

SpeechSynthesis is implemented by each browser/operating system. Local tests can verify the queue, fallback call, callbacks and watchdog handling, but cannot prove that a physical speaker actually emits audible sound. Verify at least one Listening item and one Reading passage on the target desktop and mobile/tablet browsers. When there is no sound, note the browser, OS, selected voice, whether the status reaches “Đang đọc/Đang nghe”, and whether a clear failure appears within 10 seconds. The application does not send audio or learner data to a server.
