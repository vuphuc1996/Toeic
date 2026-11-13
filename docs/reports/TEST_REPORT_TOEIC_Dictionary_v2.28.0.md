# Test Report — TOEIC Dictionary v2.28.0

**Scope:** Vocabulary Batch 018, documentation consolidation, two-version release rotation and local regression suite.

## Results

| Check | Result |
|---|---|
| `python tools/validate-data.py` | PASS — 979 records, 0 errors, 0 warnings |
| `python tools/validate-learning-content.py` | Structural PASS — 0 errors, 8 warnings because the eight Part 1 JPG binaries are not in this source snapshot; strict photo gate NOT passed |
| `python tools/sync-version.py --check` | PASS — every registered marker is 2.28.0 |
| Python unit tests | **PASS — 67/67** across `test_vocabulary_detail_examples`, `test_legacy_collocation_cleanup`, `test_sync_version`, `test_patch_data` and `test_learning_content` |
| `learning-focus-workspace.mjs` | PASS — 243 unique HTML IDs, Flashcard/Review flows, responsive contract, IndexedDB v1 unchanged, 979 vocabulary records |
| `flashcard-image-policy.mjs` | PASS — no generic topic image on word cards; approved image contract intact |
| `mock-ui-integrity.mjs` | PASS — three modes, split skill report, persistent usage ledger, no IndexedDB writes |
| `mock-exam-engine.mjs` | PASS — 15/60/120-minute modes, question blueprint, no in-form duplicates, timer/scoring and usage rotation |
| `listening-tts-regression.mjs` | PASS — voice priority/fallback, speaker mapping, pauses, safe stop/cancellation |
| `runtime-render-smoke.mjs` | PASS — Reading/Listening/Grammar rendering and v2.15→v2.17 / v2.16→v2.17 choice-ID migration smoke |
| Release rotation on merged v2.27.0 copy | PASS — dry-run reviewed; `--apply` archived/retired older documentation; final dry-run reports 0 files to retire; exactly v2.27.0 + v2.28.0 active release generations remain |

## Vocabulary delta

- Baseline before Batch 018: 971 canonical headwords.
- Batch 018 adds 8 non-duplicate headwords: `affidavit`, `bidder`, `bond`, `broker`, `capital`, `claimant`, `lien`, `margin`.
- Canonical total: **979**. Existing 971 headwords and IDs retained; no duplicate IDs.
- CEFR labels remain editorial estimates; independent lexical verification is pending.

## Documentation/release rotation

- The previous long `docs/MASTER_STATUS.md` is preserved verbatim in `docs/archive/PROJECT_HISTORY.md`; the active `docs/MASTER_STATUS.md` is now a concise state, acceptance-gate, roadmap and rotation authority.
- `docs/COMPATIBILITY.md` is the single compatibility/retirement register; `docs/README.md` is navigation only.
- `docs/CHANGELOG.md` remains a single cumulative changelog. `docs/batches/` and `docs/reports/` keep the previous/current release pair only after rotation.
- On a copy of v2.27.0 merged with the 23-file overlay, the rotator preview listed 101 old Markdown files and 4 old root update notes. After `--apply`, those historical documents were preserved in `docs/archive/PROJECT_HISTORY.md`; active root notes are exactly `V2.27.0_UPDATE_NOTES.txt` and `V2.28.0_UPDATE_NOTES.txt`. A second dry-run returned 0 files to retire.
- No `assets/`, user JPG, canonical question/vocabulary data, `patches/`, or IndexedDB profile files were removed by rotation.

## Explicit limitations

- The source snapshot has 0/8 Part 1 JPG binaries. SVG fallbacks remain. The strict photo gate is **NOT PASSED** in this snapshot; verify the actual GitHub repository before release.
- Remote GitHub Actions, GitHub Pages deployment and physical browser/device QA are unverified.
- No IndexedDB personal-profile import/export, inspection, reset or migration was performed. Database version remains 1.
- Independent TOEIC editorial/psychometric signoff is still pending; local tests prove structural/runtime contracts, not test-equating validity.
- This is a local release candidate, not a confirmed remote deployment.
