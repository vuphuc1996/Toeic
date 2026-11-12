# TOEIC Listening/TTS playback hardening — Batch 014 (v2.24.0)

**Date:** 11/11/2026  
**Scope:** Make Listening/TTS playback cancellation deterministic across browser speech engines. This is a reliability fix, not a new recorded-audio/voice-quality claim.

## Findings

- Existing TTS already supported separate male/female voice selection, a Daniel en-GB male fallback when exposed by the device, per-speaker voice reuse, per-lesson speed, a configurable pause between words and a configurable pause between dialogue turns.
- Playback cancellation previously depended on the browser firing an utterance `onerror` callback after `speechSynthesis.cancel()`. Browser implementations may not always deliver the callback consistently; a sequential playback promise could remain pending and block the next session's UI flow.
- A normal user stop/interruption could also be surfaced as a generic voice error in the one-off pronunciation preview.

## Changes

1. Added an app-owned `activeSpeechCancel` resolver for the current speech utterance.
2. `stopSpeech()` now resolves that app-owned callback before asking the browser to cancel the audio queue. This guarantees that the current playback sequence unwinds even if the browser emits no cancel event.
3. `speakUtterance()` clears the active resolver on completion, failure or cancellation, while preserving the playback-token guard that prevents stale sessions from advancing.
4. One-off pronunciation previews suppress expected `canceled` and `interrupted` events; real synthesis errors still show a useful error message.
5. Added `tools/tests/listening-tts-regression.mjs` and registered it in GitHub Actions.

## Preservation

- No changes to Listening content, question/choice IDs, answer keys, transcripts, vocabulary or Reading/Grammar datasets.
- No changes to `DEFAULT_TTS_SETTINGS`, voice recommendation rules, default pauses or the speaker/voice model.
- No audio provider, paid voice API, remote endpoint or audio asset was introduced.
- IndexedDB remains database `toeic-vocabulary-phase1`, version 1, store `workspace`; no schema/profile migration or reset. Personal profile import/export/inspection remains deferred.

## Local regression coverage

The deterministic mocked-speech test checks:

- A manually selected male voice takes precedence over automatic selection.
- Daniel en-GB remains the automatic male fallback when present and no manual voice is saved.
- Multi-speaker playback keeps a stable selected voice for each named speaker.
- The configured playback rate and turn pause are applied.
- Vocabulary is spoken as separate words with the exact configured gap.
- `stopSpeech()` resolves the active sequence even when the mock browser emits no cancellation event; queued subsequent turns are not started.
- Expected cancellation of a one-off voice preview does not show a false synthesis error.

## QA boundary / next actions

- Automated tests validate JavaScript orchestration only. They cannot assess accent authenticity, male-voice timbre, loudness, noise, pronunciation quality or actual pause perception.
- Listen and compare available male/female voice packs on Windows desktop, iPhone Safari and Android Chrome. Prefer a device-provided natural voice only after listening; do not infer acoustic quality from a voice name or `localService` flag.
- If recorded or commercial TTS audio is considered later, evaluate licensing, redistribution rights, file size, offline behavior and the GitHub-only/no-backend constraint before adding assets.
- Part 1 strict image QA remains blocked by missing JPG bytes in this local snapshot (0/8); remote GitHub Actions/Pages and physical-device QA are not claimed.
