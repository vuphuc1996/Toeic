# Compatibility & Retirement Register

> One active register for supported releases, storage/data contracts and retirement decisions. Update this file only when a release changes compatibility or the active support window.

## Current support window — 2026-11-14

| Role | Version | Policy |
|---|---|---|
| Previous baseline | v2.29.0 | Immediate base and rollback reference for v2.30.0. |
| Current candidate | v2.30.0 | Adds practice retry/history and Vocabulary Batch 020; local candidate pending remote/device QA. |
| Older releases | ≤ v2.28.0 | Retired from active handoff; concise history remains in `archive/PROJECT_HISTORY.md` and `CHANGELOG.md`. |

## Runtime and data contracts

- **Deployment:** GitHub Pages + static PWA; no GAS, iframe, backend or Cloudflare dependency.
- **Vocabulary:** `data/vocabulary/A.json`–`Z.json` are the sole canonical runtime source. `data/vocabulary/batch-*.json` files are editorial provenance only. Stable vocabulary IDs are immutable.
- **Learning content:** Listening, Reading and Grammar resource/question/choice IDs remain stable. Append new material; never reorder or replace existing question indices when learner progress may refer to them.
- **Practice progress:** existing `answers` maps remain readable. v2.30 adds optional `attemptHistory` keyed by question index to the same Reading/Listening/Grammar progress objects. This is additive data, not a database schema migration. Old v1 progress without the field remains valid.
- **Choice identity:** current and archived attempts retain stable `choiceId`; migration may update `choiceIndex` by ID while preserving the original index in `previousChoiceIndex`.
- **Local profile:** IndexedDB database `toeic-vocabulary-phase1`, version `1`, object store `workspace`. v2.30 does not import/export, inspect, reset or migrate personal profiles.
- **Presentation:** Flashcard, Review, Grammar, Reading and Listening detail share the `learningFocusBackdrop` shell. One vertical scroll owner is `.learning-focus-content`.
- **Service worker:** `VERSION` and cache name sync from `data/manifest.json`; run `python tools/sync-version.py --check` for every release. `assets/js/practice-progress.js` is a required/app-shell module.
- **Images:** preserve user-owned `assets/listening/*.jpg` and SVG fallbacks. Current source snapshot may omit the eight Part 1 JPG binaries; absence from ZIP does not prove absence on GitHub.
- **Audio/scoring:** browser SpeechSynthesis is synthesized audio, not ETS/native-speaker recording. Mock analytics are practice indicators, not equated ETS scores.

## Retired / incompatible references

- Legacy GAS/iframe/cloud-backend proposals are historical and must not be reintroduced without an explicit architecture decision.
- Never overlay a non-adjacent release blindly. Use the immediate previous release overlay or review a Full Source migration.
- Do not add compatibility aliases, legacy fallbacks or duplicate runtime data sources just to preserve obsolete code paths.
- Old batch/report/source Markdown is summarized into `archive/PROJECT_HISTORY.md` when outside the previous/current window.

## Rotation rule

Keep exactly the immediate previous and current release-specific documents. When v2.31.0 is published, v2.30.0 becomes previous and v2.29.0 is retired from the active handoff. Archive concise descriptions before retiring old batch/report/source documents and root notes. Run `tools/rotate-release-files.py` in dry-run mode, review the list, then use `--apply`. Never rotate runtime data, assets, local profiles or source code.
