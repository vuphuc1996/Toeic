# Test report — TOEIC Dictionary v2.26.0

## Scope
Flashcard image relevance and responsive layout only. This is a targeted regression batch, not a claim that every historical test suite was rerun.

## Results

| Check | Result | Notes |
|---|---|---|
| `node --check assets/js/app.js` | PASS | App JavaScript syntax |
| `node tools/tests/flashcard-image-policy.mjs` | PASS | 928 canonical A–Z records; no generic topic art on word cards; explicit approved image metadata contract; responsive frames |
| `node tools/tests/mock-ui-integrity.mjs` | PASS | 235 unique HTML IDs, 3 Mock modes, split score report, usage ledger, no Mock IndexedDB writes |
| `node tools/tests/runtime-render-smoke.mjs` | PASS | Existing Reading/Listening/Grammar runtime smoke and historical migration fixtures |
| `python -m py_compile ...` | PASS | Validator and version tool syntax |
| `python tools/validate-data.py` | PASS | 928 records, 928 stable IDs, 0 errors, 0 warnings |
| `python tools/validate-learning-content.py` | PASS with warnings | 0 errors; 8 expected missing JPG warnings in this source snapshot; SVG fallback remains available |
| `python tools/sync-version.py --check` | PASS | Manifest, SW, HTML, README, Master and Changelog all v2.26.0 |

## Image behavior
- No vocabulary item currently has an explicitly approved `image` + `imageAlt` + `imageStatus: "approved"` mapping, so every individual flashcard correctly renders without an illustration.
- Topic selection tiles retain category illustrations only.
- No JPG/PNG/WebP vocabulary illustration has been downloaded or placed in the repository during this batch.
- The 8 Part 1 JPG files remain absent from this local source snapshot; this is unrelated to the vocabulary flashcard policy. Strict Part 1 photo gate remains unverified here.

## Not claimed
- No GitHub Actions remote run, push, Pages deployment or physical-device visual QA was performed.
- CSS responsiveness is implemented with viewport/media-query rules; actual iPhone/Android/tablet visual confirmation remains pending.
- No independent TOEIC editorial signoff is implied.
- No personal IndexedDB profile was inspected, imported, exported, reset or migrated.
