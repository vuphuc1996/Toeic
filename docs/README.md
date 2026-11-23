# TOEIC Dictionary v2.95.46 — Project Documentation

## Current candidate — v2.95.46

- **Baseline:** official v2.95.45 FullSource, 698 files, SHA-256 `2d4f1f58aa355c8515b311d11fe01852f80d8c4dea57f5fff8631e955a6f112e`.
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.46.md`.
  Generated evidence is excluded from source-input fingerprints by explicit policy and remains covered by the FullSource ZIP SHA-256.
- Current command-log index: `reports/COMMAND_LOG_INDEX_v2.95.46.md`.
  Generated evidence is excluded from source-input fingerprints by explicit policy and remains covered by the FullSource ZIP SHA-256.
- **Current Master contract:** `MASTER_DEVELOPMENT_PROMPT.md` (Sections 1–15; the single development policy for all future prompts).
- **Test inventory policy:** `../tools/test-inventory-policy.json` (approved roots, exclusions, baseline inventory and accepted environment skip rules).
- **Fingerprint scope policy:** `../tools/source-fingerprint-policy.json` (deterministic metadata, generated-output exclusions and symlink/path safety).
- This candidate consolidates project governance/docs, updates the manual acceptance checklist, applies safe historical-report retention, and makes Editorial Review Queue counts source-derived. It does not redesign the UI or change learner storage, canonical vocabulary identities, learning question/choice IDs or answer keys.
- Source Release / Production Deployment acceptance states are reported separately. A candidate ZIP is not proof of remote deployment or device acceptance.

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
