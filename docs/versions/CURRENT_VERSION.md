# Current Version

- Version: **2.65.1**
- Status: local hotfix candidate; deployment hold until the inherited Part 1 original JPG binaries are restored and the strict validator passes.
- Focus: restore `refreshSpeechVoiceSelectors()` so app initialization, voice-catalog updates and manual refresh no longer throw a ReferenceError.
- Voice preferences: saved male/female voice URIs remain authoritative; if a saved URI is absent on the current device, the selector preserves it as an explicitly unavailable option instead of silently replacing it.
- The v2.65.0 TTS readiness delay, Part 1 A–D pause and Reading read-aloud pipeline are unchanged.
- No user progress, IndexedDB schema/stores or local TTS settings were reset/migrated.
- Real-device audio QA, GitHub Actions remote result and GitHub Pages deployment are not verified in this workspace.
