# TOEIC Dictionary v2.95.69 — Project Documentation

## Current source — v2.95.69 (Glossary Batch 044 and release cache coherence)

- **Exact predecessor:** `TOEIC_Dictionary_v2.95.68_FullSource.zip`; SHA-256 `2313f612e536c618b91fa1462611dffba7c9539f9e1a019a9b3ac4de79941c2a`. This is the sole baseline for v2.95.69.
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.69.md`.
- Python inventory: `reports/PYTHON_TEST_SHARDS_v2.95.69.md/.json` (104 modules, 785 cases, 784 PASS, 1 accepted SKIP, 0 FAIL).
- Node regression: `reports/NODE_TEST_REPORT_v2.95.69.md` (44/44 PASS).
- Current data comparison: `reports/DATA_DIFF_v2.95.69.md`.
- Current Word Family read-only audit: `reports/WORD_FAMILY_GRAPH_AUDIT_v2.95.69.md/.json`.
- Current package verification: `reports/PACKAGE_VERIFICATION_v2.95.69.md`.
- Current change manifest: `reports/CHANGE_MANIFEST_v2.95.69.md`.
- Current command-log index: `reports/COMMAND_LOG_INDEX_v2.95.69.md`.
- Batch 044 enriches 15 existing Related Glossary rows using paraphrased Cambridge-derived definitions, POS and source provenance. Quality flags decline 157→142; independent editorial review remains pending.
- Release cache consistency is enforced across 17 local `app.js` imports and 42 Service Worker cache URLs. `tools/sync-version.py --check` validates these against the manifest and future `--apply` updates them.
- The test suite also corrects a stale Robot Buddy layout assertion to require a single Learning Focus result surface, not a stacked modal.
- No canonical vocabulary ID/headword/relation, question/choice ID, answer key, Mock eligibility, protected learning-bank content or learner IndexedDB schema/record changed. UI layout is frozen; GitHub Pages/GitHub-only architecture remains.
- Local candidate verification is complete within the report's scope. Hosted Actions, Pages deployment, installed-PWA cache/offline migration and physical-device acceptance remain **UNVERIFIED**. Do not treat this candidate as production-deployed.

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
