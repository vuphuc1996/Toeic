# TOEIC Dictionary v2.95.65 — Project Documentation

## Current source — v2.95.65 (Batch 035 and shared modal overlay repair)

- **Exact predecessor:** `TOEIC_Dictionary_v2.95.64_FullSource.zip`; SHA-256 `03ec4c80e88bc76e435cfc0782e933474be882a4f271318a23375a35e9242673`. This exact complete FullSource was verified before editing; no older source or Patch was used as the baseline.
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.65.md`.
- Current implementation report: `reports/GITHUB_CAMBRIDGE_AND_MODAL_OVERLAY_FIX_v2.95.65.md`.
- Current package verification: `reports/PACKAGE_VERIFICATION_v2.95.65.md`.
- Current change manifest: `reports/CHANGE_MANIFEST_v2.95.65.md`.
- Current command-log index: `reports/COMMAND_LOG_INDEX_v2.95.65.md`.
- The Batch 035 split Cambridge test is included in source and selected by the wildcard discovery step; historical rows, corrections, relation anchors and base hash are reconstructed instead of using stale fixed values.
- `learningFocusBackdrop` is the only screen-wide dimming/blur layer; `modalLayer` contains only the modal panel. Both ordinary and focused-session modals use the same root.
- GitHub Actions now runs a dedicated single-overlay contract test in addition to all Node modal and full Python discovery tests.
- No vocabulary/question/answer data, stable IDs, learner IndexedDB records/schema, PWA storage contract, UI layout or hosting architecture changed.
- Hosted GitHub Actions, GitHub Pages deployment, PWA cache/offline behavior and physical-device acceptance remain unverified until directly tested.

## Single source of truth

- **Current candidate / accepted source ledger:** `versions/CURRENT_VERSION.md`.
- **Immediately previous official source:** `versions/PREVIOUS_VERSION.md`.
- **Project status and active backlog:** `MASTER_STATUS.md`.
- **Development contract / anti-drift rules:** `MASTER_DEVELOPMENT_PROMPT.md`.
- **Chronological release history:** `CHANGELOG.md`.
- **Runtime, storage, offline and retirement contracts:** `COMPATIBILITY.md`.
- **Historical report index:** `archive/PROJECT_HISTORY.md`.
- **Current manual test checklist:** `reports/MANUAL_ACCEPTANCE_CHECKLIST.md`.

Never use a working directory, unverified candidate, same-version/different-hash ZIP or Patch as the official baseline. Verify the exact FullSource SHA-256 recorded in the version ledger before editing.

## Product and architecture

- GitHub Pages static PWA; GitHub-only; no app backend, GAS, iframe or Cloudflare runtime.
- UI is frozen; do not redesign or add menus without a reproduced defect and a narrow fix.
- Local learner data remains on-device. IndexedDB contract: `toeic-vocabulary-phase1`, schema version 1, store `workspace`.
- TOEIC Listening and Reading are the active exam-development tracks. B1 remains a blueprint; Speaking/Writing and IELTS are deferred.
- Robot Buddy remains an offline bundled-content companion under its documented privacy boundary.
- Browser/device SpeechSynthesis is device-dependent and is not authentic ETS/native audio.

## Canonical inventory snapshot — v2.95.45 baseline

| Area | Inventory |
|---|---:|
| Canonical vocabulary | 1,141 headwords across A–Z |
| Related Glossary | 567 entries; 556/804 exact relation targets covered; 248 unique terms / 249 occurrences remain |
| Grammar | 58 lessons / 169 exercises |
| TOEIC Listening | 145 units / 295 questions: 102 eligible, 193 reserve |
| TOEIC Reading | 73 resources / 287 questions |
| Separate Part 5 practice | 80 questions; practice-only / review-pending |
| Part 7 reserve | 87 questions; separate from Listening and Part 5 |
| Foundation | 23 lessons: 10 Pre-A1/A1 and 13 A2 |
| Python tests | 88 modules in v2.95.45 official baseline; v2.95.46 candidate dynamically discovers 89 (88 baseline + 1 added fingerprint test); future discovery is dynamic, not capped |

Counts describe source inventory, not editorial approval, learner completion, mastery or Mock eligibility. Current reports recalculate live metrics from source data. Do not copy this historical baseline into a new release without remeasurement.

## Documentation retention

- Keep current and immediately previous release reports active, plus explicitly pinned current working reports and the manual acceptance checklist.
- Retire superseded versioned report files only after checking active references. The complete original Markdown and release-note content is consolidated into `docs/archive/PROJECT_HISTORY.md` with original paths, byte sizes and SHA-256 markers; no full historical text is discarded by rotation.
- Never delete canonical data, stable IDs, source/provenance ledgers, patch payloads, learning content, fixtures, open review handoffs, storage contracts or required test inputs as presumed dead files.
- Exact byte-identical report duplicates are checked separately; none were found in the v2.95.46 pre-cleanup scan. Near-duplicate versioned outputs are archived independently with their original content and hashes.

## Release evidence

See the current Test Report, Command Log, Change Manifest, Package Verification and Manual Acceptance Checklist. Remote GitHub Actions, GitHub Pages deployment/cache and physical-device checks remain `UNVERIFIED` until directly performed.
