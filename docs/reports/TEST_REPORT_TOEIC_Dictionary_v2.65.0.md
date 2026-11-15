# Test Report — TOEIC Dictionary v2.65.0

**Scope:** speech engine readiness, Listening A–D playback, Reading read-aloud and adjacent learning modules.  
**Environment:** local source workspace; Node.js and Python checks. Browser/device audio output was not available for direct listening validation.

## Findings and implementation

The previous playback path could call `speechSynthesis.cancel()` and queue the next utterance immediately. It also selected from `getVoices()` without waiting when the device initially returned an empty voice catalog. This made cold-start and cancellation-to-restart transitions a plausible source of clipped opening phonemes/words, especially when Part 1 A–D descriptions were sent as four separate utterances.

The updated path:

1. Polls the platform voice catalog for up to 1.2 seconds, while remaining cancellable.
2. Clears residual `speaking` / `pending` work if the platform still reports it.
3. Waits the configured pre-play buffer before queuing the first content utterance.
4. Resolves the chosen voice after catalog preparation, so a delayed voice list can be used.
5. Uses a playback token so Stop/navigation invalidates preparation waits and active utterances; no stale utterance should start later.
6. Keeps a dedicated pause between Listening Part 1 A–D options, separate from conversation turn timing.

## Default and configurable timing

| Setting | Default | UI range | Purpose |
|---|---:|---:|---|
| `startupDelayMs` | 750 ms | 500–1,500 ms | Buffer after voice-catalogue preparation and before first content utterance |
| `part1OptionPauseMs` | 1,300 ms | 1,000–2,300 ms | Rest between Part 1 descriptions A–D |
| `sentencePauseMs` | 850 ms | existing | Existing pause between dialogue/short-talk turns |
| `wordPauseMs` | 900 ms | existing | Existing slow-vocabulary pause |

If the device never publishes a voice catalog, the app stops waiting after the timeout and allows the platform default voice to be used; it does not wait forever.

## Routes covered

- Listening Parts 1–4 and mock-exam Listening audio call `playListeningAudio()` and prepare before the first segment.
- Part 1 statements are surfaced as `Mô tả A/4` through `Mô tả D/4`, with the dedicated option pause.
- Slow vocabulary reads prepare once, then keep the configured pause between words.
- Word pronunciation, flashcards, flash quiz, Foundation Listening and A–Z sound practice go through `speakText()` and share the same readiness buffer.
- Reading passages and document content now have a read-aloud control; Part 5 can read its question-and-choice set. Reading playback exposes status and a Stop control.

## Test results

- Python: **59/59 PASS** across 10 test modules: TTS readiness (9), Listening expansion (5), Reading expansion (9), Foundation Listening (7), A–Z (7), responsive layout (5), learning surface consistency (5), Part 1 image metadata (4), design profile (6), CI coverage (2).
- JavaScript: **19/19 regression suites PASS**.
- Enhanced `listening-tts-regression.mjs` specifically verifies:
  - voice catalog initially returns empty and becomes available;
  - no utterance is queued before the startup buffer;
  - all four Part 1 options are queued in A–D order;
  - Part 1 uses a 1,300 ms gap between descriptions;
  - Stop during startup preparation prevents the first utterance;
  - Stop during active speech resolves even when the browser omits a cancellation callback;
  - Reading read-aloud uses the same engine path and updates status.
- All JS assets and `sw.js`: syntax PASS.
- All Python tools: `py_compile` PASS.
- CSS parsing: 0 parse errors in both main stylesheets.
- Version sync: PASS. Design profile: 54 tokens / 362 legacy selector groups synchronized.
- Vocabulary data: 992 / 992 records, 0 errors, 0 warnings.
- Learning content: 0 errors, 8 missing-Part-1-JPG warnings.
- Objective resources: 281/281 linked. Outcome criteria: 30/30 structurally valid.

## Known blockers and limitations

- `python tools/validate-part1-photo-assets.py` still fails: only 1/9 JPG binaries are present in the local workspace; eight original licensed images are missing, including `part1-photocopier.jpg`. This is inherited from the previous source snapshot and is independent of TTS code. The strict validator has not been disabled.
- No physical iPhone/iPad/Android/desktop speech-engine run was performed. The delay and queue protections lower the app-side truncation risk but cannot guarantee every vendor TTS engine will render every phoneme identically.
- GitHub Actions, GitHub Pages deployment and PWA update behavior were not verified remotely.

## Manual verification after deployment

1. Open Settings → Giọng đọc & nhịp nghe. Keep startup delay at 0.75 seconds and Part 1 gap at 1.3 seconds initially.
2. Open Listening → Part 1 → select a photo with four descriptions → tap “Nghe bốn mô tả A–D”. Confirm the first word of A is audible and all four descriptions are heard in sequence with a clear gap.
3. Press Stop while the “Đang tải voice và chuẩn bị bộ đọc…” state is visible. Confirm that no delayed speech starts afterward.
4. Repeat with Part 2/3/4 and compare speaker turn pauses.
5. Open Reading → a Part 6/7 passage → “Nghe đọc bài”. Confirm the passage begins at its first word, status changes to reading/complete and Stop works.
6. Repeat after force-closing/reopening the iPhone PWA; voice availability and audio startup differ by OS/browser and need this real-device check.

Do not clear site data or remove the PWA for this test; learner progress is stored locally.
