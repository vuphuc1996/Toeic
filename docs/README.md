# TOEIC Dictionary v2.95.68 — Project Documentation

## Current source — v2.95.68 (single-surface assessment results and regression repair)

- **Exact predecessor:** `TOEIC_Dictionary_v2.95.67_FullSource(1).zip`; SHA-256 `1f262ac4d67d8d244facf397b9ea1d179c6a741f50e561b3d3e9805efef31754`. This is the sole baseline for v2.95.68.
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.68.md`.
- Current data comparison: `reports/DATA_DIFF_v2.95.68.md`.
- Current package verification: `reports/PACKAGE_VERIFICATION_v2.95.68.md`.
- Current change manifest: `reports/CHANGE_MANIFEST_v2.95.68.md`.
- Current command-log index: `reports/COMMAND_LOG_INDEX_v2.95.68.md`.
- Active Learning Focus results reuse the existing dialog; the extra result modal is not opened during a focused session. Existing modal fallback remains for other workflows.
- Confetti now runs for 2.4 seconds plus stagger, while reduced-motion users continue to receive the existing static/reduced behavior.
- Batch 036's historical vocabulary reconstruction now reverses Batch 025's six explicitly ledgered Word Family additions before reversing v2.95.54; this restores the expected historical hash without changing canonical data or the ledger.
- No UI redesign, vocabulary or assessment data change, learner IndexedDB migration, backend, Cloudflare or non-GitHub hosting is included.
- Full Python discovery was attempted but did not complete; only actual focused/local verification is marked PASS. Hosted Actions, Pages deployment and physical-device acceptance remain unverified.

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
