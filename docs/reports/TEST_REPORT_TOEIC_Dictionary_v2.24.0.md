# Test report — TOEIC Dictionary v2.24.0

**Date:** 11/11/2026  
**Change:** Batch 014 — Listening/TTS playback reliability.

## New regression result

`node tools/tests/listening-tts-regression.mjs` — **PASS**.

Coverage includes manual voice priority, Daniel en-GB fallback, stable speaker voice mapping, per-lesson playback speed, configured dialogue pauses, configured inter-word pauses, cancellation without a browser `onerror` callback, and suppression of expected cancellation errors for one-off pronunciation previews.

The test uses a deterministic mock of the browser SpeechSynthesis API. It does not play sound and does not certify voice quality on a physical device.

## Existing v2.23.0 baseline carried forward

- 177/177 Python unit-test methods passed in the previous v2.23.0 full-source test accounting across 17 suites; this batch does not alter those Python modules or learning datasets.
- Re-run Python test methods for this update: `test_baseline_ids.py` 13/13, `test_patch_data.py` 11/11 and the two directly relevant version-sync cases 2/2. A grouped attempt to run the complete `test_sync_version.py` module exceeded the sandbox command limit; the complete previous v2.23.0 count remains the carried-forward 177/177 baseline, not a fresh v2.24.0 suite-wide claim.
- Re-run release checks: JavaScript syntax, runtime render/migration smoke, Listening/TTS regression, vocabulary validator, learning-content validator, TOEIC coverage audit, evidence audit, distractor audit and version synchronization all PASS within their stated scope.
- Vocabulary data remains 928 records / 928 stable IDs. Listening remains 63 units / 113 questions; Reading 109 questions; Grammar 25 lessons / 54 exercises.

## Package QA

- Update overlay patch: 15 changed/added files; ZIP CRC and exact extraction comparison PASS.
- Full-source snapshot: 234 files; ZIP CRC and exact extraction comparison PASS.
- Simulated application: overlay applied to the v2.23.0 full-source snapshot. All nine existing files under `assets/listening/` (eight SVG fallbacks plus `ATTRIBUTION.csv`) remained byte-identical after merge.
- Both packages intentionally contain 0 Part 1 JPG binaries because the working snapshot did not include those bytes. The overlay omits the `assets/listening/` folder entirely, so it will not replace JPGs already present in the user's repository.

## Current release boundary

- Part 1: actual JPG bytes are not present in the local snapshot (0/8); `validate-part1-photo-assets.py --allow-missing` is diagnostic only. Strict photo validation is not claimed PASS. GitHub Actions will require the eight valid files.
- Remote GitHub Actions, the previously reported failure run `42981524564`, GitHub Pages deployment and physical-device browser/audio QA remain unverified.
- The Batch 013 reserve items remain `reserve-pending-independent-review`; they are not promoted to expert-reviewed content.
- The user's personal IndexedDB profile import/export/inspection/reset/migration testing remains deferred. No personal profile or IndexedDB schema was touched.

## Reproduction

```bash
node --check sw.js
cp assets/js/app.js /tmp/app.mjs && node --check /tmp/app.mjs
node tools/tests/runtime-render-smoke.mjs
node tools/tests/listening-tts-regression.mjs
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/validate-part1-photo-assets.py --allow-missing
python tools/audit-toeic-coverage.py
python tools/audit-question-evidence.py
python tools/audit-distractors.py
python tools/sync-version.py --check
```

For a release candidate on the real repository, also run strict `python tools/validate-part1-photo-assets.py` after verifying the eight JPG files exist under `assets/listening/`.
