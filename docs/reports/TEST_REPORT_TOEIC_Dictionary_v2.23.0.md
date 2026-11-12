# Test Report — TOEIC Dictionary v2.23.0

- **Date:** 2026-11-11
- **Release type:** Local update-patch candidate; not pushed or deployed by this session.
- **Base:** v2.21.0 full source + v2.22.0 photo integration patch.

## Changes covered

1. P1 warehouse and technician statements were aligned more precisely to their Pexels source descriptions; keys and choice identities were preserved.
2. Added 11 reserve Listening questions: 5 Part 2, 3 Part 3 and 3 Part 4.
3. Replaced the brittle full-file Listening SHA gate with per-question and per-unit fingerprints for the 148 v2.19 reviewed items. The unit fingerprint protects transcript segments, translations and source metadata; approved Part 1 amendments are explicit. New out-of-registry questions must be tagged reserve-pending-independent-review.
4. Corrected Service Worker validation semantics: missing `OPTIONAL` paths do not fail general structure validation; required/app-shell paths remain strict.
5. Kept the dedicated strict Part 1 asset validator in GitHub Actions so a missing/invalid JPG still blocks release.

## Unit test accounting

**177/177 test methods PASS**, executed by test module and validator chunks to avoid the sandbox's grouped-run timeout.

| Suite | Methods | Result |
|---|---:|---|
| baseline_ids | 13 | PASS |
| patch_data | 11 | PASS |
| sync_version | 12 | PASS |
| validator | 36 | PASS (isolated chunks) |
| learning_content | 31 | PASS |
| dashboard_layout | 6 | PASS |
| design_system | 15 | PASS |
| question_evidence | 4 | PASS |
| distractor_quality | 6 | PASS |
| choice_history | 5 | PASS |
| learning_detail_scope | 3 | PASS |
| choice_identity | 9 | PASS |
| answer_position_balance | 3 | PASS |
| remaining_content_review | 6 | PASS |
| part1_photo_assets | 4 | PASS (unit fixtures + allow-missing behavior) |
| vocabulary_detail_examples | 10 | PASS |
| legacy_collocation_cleanup | 3 | PASS |
| **Total** | **177** | **PASS** |

## Validators and audits

- `python tools/validate-data.py`: **PASS — 928 vocabulary records, 0 errors, 0 legacy warnings; 928/928 stable IDs preserved.**
- `python tools/validate-learning-content.py`: **0 errors, 8 warnings.** The eight warnings are solely absent JPG binaries in this local snapshot; eight SVG fallbacks and attribution records exist.
- `python tools/validate-part1-photo-assets.py --allow-missing`: **PASS with 8 missing-photo warnings; 0/8 actual JPG files present.**
- `python tools/validate-part1-photo-assets.py` strict: **not PASS / not releasable from this snapshot** because the actual JPG binaries are not present. GitHub Actions runs the strict command.
- `python tools/audit-toeic-coverage.py`: PASS; Listening 63 units / 113 questions, Reading 35 /109, Grammar 25 /54.
- `python tools/audit-question-evidence.py`: PASS; 222 answer keys indexed (113 Listening +109 Reading); P1 entries are marked source-description reviewed, not binary-visual verified.
- `python tools/audit-distractors.py`: PASS; 132 historic reviewed questions retain their certified distributions; 6 reserve sets (3 P3 +3 P4) are separately structural-checked and excluded from the old certificate.
- `python tools/sync-version.py --check`: PASS; manifest/index/sidebar/footer/SW/docs all synchronized to 2.23.0.
- Python syntax, JavaScript syntax and `node tools/tests/runtime-render-smoke.mjs`: PASS.

## Data integrity

- Vocabulary: 928/928 stable IDs preserved; no vocabulary record addition/removal.
- Listening: 113 questions, including 11 new reserve items. Existing question IDs, option arrays, answer indices and choice IDs remain preserved except the five explicitly registered Part 1 statement/rationale alignments; no answer key or choice order changed.
- Reading: 109 questions unchanged.
- Grammar: 25 lessons /54 exercises unchanged.
- IndexedDB: database `toeic-vocabulary-phase1`, version 1, store `workspace`; no schema/database/store change.
- Personal profile: no personal import/export, inspection, reset or migration performed, as requested.

## Known release blockers / unverified items

1. Eight JPG binaries were not included in this working snapshot. The user reports they exist on GitHub, but remote byte verification was unavailable. Strict asset validation on the complete branch must pass 8/8 before release.
2. GitHub Actions and GitHub Pages remote status were not directly verified in this session. The earlier run `42981524564` still requires its exact failing log/commit correlation.
3. Real browser/device QA remains pending: laptop 15.6-inch at 100% zoom, tablet, iPhone Safari, Android Chrome, offline photo cache and audio playback.
4. Batch 013 reserve items are structurally tested but await independent TOEIC editorial review. They must not be counted as independently reviewed or certified for a scored Full Mock.
5. Personal IndexedDB import/export/migration remains explicitly deferred.

## Package integrity

- Full source archive: **227 files**, ZIP CRC PASS, clean-extraction byte comparison 227/227 PASS.
- Overlay patch against v2.21.0 baseline: **39 changed/new files**, ZIP CRC PASS, clean-extraction byte comparison 39/39 PASS.
- SHA-256 sidecars are provided next to both ZIPs. Neither archive contains the eight Pexels JPG binaries because they were not present in the working snapshot; the overlay instructions explicitly require preserving the user-owned files already in the target repository.

## Release decision

**Local code and content gates: PASS. Full production release: PENDING.** Do not delete existing user-owned JPG files when applying the patch. Apply as an overlay to the repository while retaining `assets/listening/part1-*.jpg`, then run GitHub Actions strict photo validation and real-device QA.
