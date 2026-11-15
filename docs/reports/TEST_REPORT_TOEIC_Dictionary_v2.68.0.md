# Test Report — TOEIC Dictionary v2.68.0

Date: 2026-11-15
Scope: Part 1 reviewed-content fingerprint repair, JPG-only contract, Vocabulary Batch 010, cumulative migration compatibility, runtime and design synchronization.

## Release checks

| Check | Result |
|---|---|
| `python -m unittest discover -s tools/tests -p 'test_remaining_content_review.py' -v` | **PASS — 9/9** |
| Python test modules completed | **PASS — 40/41 modules; 291 tests passed** |
| `test_validator.py` | **INCOMPLETE — execution timed out during `test_missing_id_against_baseline_is_error`; earlier tests completed successfully, but this module is not counted as passed** |
| JavaScript regression suites (`tools/tests/*.mjs`) | **PASS — 21/21** |
| Vocabulary release-integrity Node test | PASS — 1,063 canonical words, unique IDs/headwords, cumulative 979/992/1,026 repair profiles |
| Learning-focus workspace Node test | PASS — 267 unique learning IDs and Batch 010 integration |
| `python tools/validate-data.py` | **PASS — 1,063 records, 0 errors, 0 warnings** |
| `python tools/validate-learning-content.py` | 0 errors; 8 missing-original-JPG warnings |
| `python tools/sync-version.py --check` | PASS — all markers at v2.68.0 |
| `python tools/sync-design-profile.py --check` | PASS — 54 tokens and 361 legacy font-floor selector groups |
| JavaScript syntax (`sw.js`, `assets/js/*.js`) | PASS |
| Python compilation for refresh/validator/report scripts | PASS |
| Listening readiness audit | PASS — 107 units / 201 questions; 102 eligible / 99 pending |
| Question evidence audit | PASS — 401 indexed questions |
| Distractor structural audit | PASS — 177 questions, unique choices and valid keys |
| Strict Part 1 photo validator | **FAIL — 1/9 JPG bytes present, 8 original JPG files missing from this workspace** |

## Fingerprint failure analysis

The failing unit fingerprint was caused only by deliberate removal of the obsolete SVG fallback metadata field `image` from the eight historically reviewed Part 1 unit objects. Reconstructing the exact historical field value (`./assets/listening/<unitId>.svg`) reproduces the previous certified unit hash for all eight reviewed units. All eight stored question hashes match their existing certified values. No transcript, question, choices, answer key, order, translation, title, photo path or review decision changed.

`fingerprintRefreshLog` preserves two separate metadata amendments: (1) adding `photoSourceType: licensed-stock`; (2) removing the obsolete `image` SVG fallback. The second refresh utility fails closed unless exactly the eight expected Part 1 units match the old hash after restoring only that field and each question hash remains unchanged.

## Vocabulary Batch 010

- +37 stable IDs; canonical vocabulary 1,026 → 1,063.
- Coverage: 35.4% of 3,000 minimum; 21.3% of 5,000 planning ceiling.
- US IPA 711/1,063 (66.9%); word-family records 240/1,063 (22.6%); verb forms 312/1,063 (29.4%); collocations 893/1,063 (84.0%); synonyms 404/1,063 (38.0%); antonyms 213/1,063 (20.0%).
- Batch records: 37 US IPA; 42 bilingual examples; 111 collocations; eight directed links forming five reciprocal word-family pairs.
- Independent lexical review is pending. CEFR levels are editorial estimates, not official alignment.

## Deployment status

Local source checks do not prove remote GitHub Actions or GitHub Pages deployment. Strict photo validation remains a blocker because only one of nine original Part 1 JPG binaries is included in this source workspace. Retain/restore the eight repository-owned JPGs (including `part1-photocopier.jpg`) when merging; do not fabricate substitutes or disable the validator.

No IndexedDB schema/store migration, personal data reset, stable ID rewrite, question answer-key change or learner progress reset was made.
