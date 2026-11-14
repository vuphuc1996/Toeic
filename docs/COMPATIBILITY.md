# Compatibility & Retirement Register

> One active register for supported versions, incompatible details and retirement decisions. Update this file only when a release affects storage, runtime contracts, deployment, routing or release support.

## Current support window — 2026-11-13

| Role | Version | Policy |
|---|---|---|
| Previous stable/base | v2.28.0 | Immediate overlay base and rollback reference for v2.29.0. |
| Current candidate | v2.29.0 | Shared Learning Workspace and single-scroll Flashcard interaction; local candidate pending user/remote/device verification. |
| Older versions | ≤ v2.27.0 | Retired from active handoff; compact history retained in `archive/PROJECT_HISTORY.md`, with detailed chronological release notes in `CHANGELOG.md`. |

## Runtime and data contracts

- **Deployment:** GitHub Pages + static PWA. No GAS, iframe, backend or Cloudflare dependency.
- **Vocabulary:** `data/vocabulary/A.json`–`Z.json` are the sole canonical runtime vocabulary source. `data/vocabulary/batch-*.json` are editorial provenance only. Stable vocabulary IDs are immutable.
- **Learning content:** Listening, Reading and Grammar resource/question/choice IDs remain stable. Append new material; never reorder or replace existing question indices when learner progress may refer to them.
- **Local profile:** IndexedDB database `toeic-vocabulary-phase1`, version `1`, object store `workspace`. No import/export, inspection, reset or migration is included in v2.29.0.
- **Presentation:** Flashcard, Review, Grammar, Reading and Listening detail views share the `learningFocusBackdrop` shell. One vertical scroll owner is `.learning-focus-content`; do not reintroduce nested scroll panels in a detail card or modal.
- **Service worker:** `VERSION` and cache name are synchronized from `data/manifest.json`; run `python tools/sync-version.py --check` for every release.
- **Images:** preserve all user-owned `assets/listening/*.jpg` and SVG fallbacks. Current source snapshot may omit the eight Part 1 JPG binaries; their absence from a ZIP does not prove they are absent on GitHub.
- **Audio/scoring:** browser SpeechSynthesis is synthesized audio, not ETS/native-speaker recording. Mock analytics are practice indicators, not equated ETS scores.

## Retired / incompatible references

- Legacy GAS/iframe/cloud-backend proposals are historical and must not be reintroduced without an explicit architecture decision.
- Never overlay a non-adjacent release blindly. Use the immediate previous release overlay or explicitly review a Full Source migration.
- Do not add compatibility aliases, legacy fallbacks or duplicate runtime data sources just to preserve obsolete code paths.
- Old batch/report/source Markdown is summarized into `archive/PROJECT_HISTORY.md` when outside the previous/current window. Full release chronology remains in `CHANGELOG.md`.

## Rotation rule

Keep exactly the immediate previous and current release-specific documents. When v2.30.0 is published, v2.29.0 becomes previous and v2.28.0 is retired from the active handoff. Archive concise descriptions before retiring old batch/report/source documents and root notes. Use `tools/rotate-release-files.py` (dry-run first, `--apply` after review). Never rotate runtime data, assets, local profiles or source code.
