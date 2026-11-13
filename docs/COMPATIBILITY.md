# Compatibility & Retirement Register

> **Single register** for supported versions, incompatible implementation details and retirement decisions. Update this file when a release changes storage, routes, cache, data contracts or deployment architecture. Do not create one-off compatibility reports.

## Current support window — 2026-11-13

| Role | Version | Policy |
|---|---|---|
| Previous stable/base | v2.27.0 | Immediate baseline used to build v2.28.0; retain as the rollback/overlay reference for this handoff. |
| Current candidate | v2.28.0 | Latest local candidate; GitHub Actions, Pages deployment and device QA are not confirmed. |
| Older versions | ≤ v2.26.0 | Retired from active handoff; historical evidence is consolidated in `archive/PROJECT_HISTORY.md`. |

## Current compatibility contracts

- **Deployment:** GitHub Pages + static PWA. No GAS, iframe, server backend or Cloudflare runtime is part of the active product architecture.
- **Vocabulary:** `data/vocabulary/A.json`–`Z.json` are canonical runtime data. Batch JSON files are editorial provenance only. Stable word IDs are immutable.
- **Learning content:** Listening, Reading and Grammar IDs/choice identities are stable. Append new material; do not reorder/replace existing question indices when local progress may refer to them.
- **Local profile:** IndexedDB database `toeic-vocabulary-phase1`, version 1, object store `workspace`. No import/export, inspection, reset or migration is allowed in this workstream unless the user explicitly requests it.
- **Service worker:** cache version is synchronized from `VERSION` in `sw.js`; every release runs `python tools/sync-version.py --check`.
- **Images:** preserve all user-owned `assets/listening/*.jpg` and SVG fallbacks. The current source snapshot does not include the eight Part 1 JPG bytes; absence from this ZIP is not evidence that the GitHub copy is absent.
- **Audio/scoring:** browser SpeechSynthesis is synthesized audio, not ETS/native-speaker recording. Mock analytics are practice indicators, not equated ETS scores.

## Retired or incompatible implementation references

- Older GAS/iframe/cloud-backend deployment proposals are historical and must not be reintroduced into the GitHub Pages PWA without an explicit architecture decision.
- Do not overlay a non-adjacent release onto the current repository. Use the immediate previous release overlay or review a Full Source migration explicitly.
- Do not add compatibility aliases, legacy fallbacks or duplicate runtime data sources just to keep obsolete code paths alive. Resolve supported routes/schema in the current implementation and document any retirement here.
- Version-specific update notes, batches and reports older than the previous/current pair are archived, then their separate files are retired from the active tree.

## Rotation rule

For each new release, keep exactly the immediate previous version and the new current version. Move older batch/report evidence into `archive/PROJECT_HISTORY.md`, retire older root update notes, then update this register and `docs/MASTER_STATUS.md`. Use `tools/rotate-release-files.py` (dry-run first, `--apply` only after review). Never rotate or delete runtime data, assets, personal profiles or source provenance files.
