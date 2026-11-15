# TOEIC Dictionary v2.65.0 — Documentation

- Current candidate: `v2.65.0` — `versions/CURRENT_VERSION.md`.
- Previous release: `v2.64.0` — `versions/PREVIOUS_VERSION.md`.
- Master status: `MASTER_STATUS.md`.
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.65.0.md`.
- Progress baseline: `reports/PROJECT_PROGRESS_BASELINE_v2.65.0.md`.
- Speech pipeline: `prepareSpeechEngine()` waits for the device voice catalog, applies a startup buffer and protects against stale/canceled utterances.
- Listening Part 1: dedicated configurable pause between A–D statements.
- Reading: passage/document/Part 5 question-set read-aloud uses the same prepared TTS pipeline.
- Personal settings: `appSettings.tts.startupDelayMs` and `appSettings.tts.part1OptionPauseMs` are additive; existing settings and learning progress are preserved.
- Design governance: `design/design-profile.json`, `docs/DESIGN_SYSTEM.md`, `docs/DESIGN_BRIEF_TEMPLATE.md`.
- Deployment status: local candidate only; strict Part 1 asset validator remains blocked by 8 missing original JPG binaries inherited from the previous source archive.
