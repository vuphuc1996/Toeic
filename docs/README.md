# TOEIC Dictionary v2.95.67 — Project Documentation

## Current source — v2.95.67 (Word Family graph integrity and sourced enrichment)

- **Exact predecessor:** `TOEIC_Dictionary_v2.95.66_FullSource.zip`; SHA-256 `30236500cfa2d8702a25cdca9c99f0eca58eaaa047928a6b12ce88b1b2a373c3`. This archive is the sole baseline for v2.95.67.
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.67.md`.
- Current Python test ledger: `reports/PYTHON_TEST_SHARDS_v2.95.67.md` and machine-readable JSON ledger; it distinguishes focused PASS evidence from the incomplete full inventory.
- Current package verification: `reports/PACKAGE_VERIFICATION_v2.95.67.md`.
- Current change manifest: `reports/CHANGE_MANIFEST_v2.95.67.md`.
- Current command-log index: `reports/COMMAND_LOG_INDEX_v2.95.67.md`.
- Batch 025 adds six reciprocal, sense-matched Word Family links across three existing canonical headword pairs. No headwords or IDs are added.
- `tools/audit-word-family-graph.py` provides read-only structural and sense-anchor checks. Missing targets, POS mismatches, Vietnamese gloss mismatches and non-reciprocal links remain explicit review findings; the tool never rewrites canonical records.
- No vocabulary meanings/examples/IPA/verb forms, synonym/antonym arrays, TOEIC question data, choice IDs, answer keys or Mock eligibility changed. Six Word Family relationship links were added; learner IndexedDB data/schema, Robot Buddy privacy boundary, UI layout and hosting architecture are unchanged.
- Hosted GitHub Actions/Pages for this release, installed-PWA cache propagation and physical-device acceptance remain unverified until a real push/deploy and device check.

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
