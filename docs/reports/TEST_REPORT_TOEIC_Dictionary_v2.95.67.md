# Test Report — TOEIC Dictionary v2.95.67

## Source baseline

- Sole predecessor: `TOEIC_Dictionary_v2.95.66_FullSource.zip`.
- Predecessor SHA-256: `30236500cfa2d8702a25cdca9c99f0eca58eaaa047928a6b12ce88b1b2a373c3`.
- Release version: `2.95.67`.
- GitHub Pages was not pushed or deployed during this local build.

## Verified results

| Validation | Result |
|---|---:|
| Focused Python regression suites | **17 modules; 161/161 tests PASS** |
| Additional `test_validator.py` release-key checks | **2/2 PASS** (targeted methods only) |
| Node regression scripts | **43/43 PASS** |
| `python tools/validate-data.py` | **1,141 records; 0 errors / 0 warnings; canonical IDs +0 / -0** |
| `python tools/validate-learning-content.py` | **0 errors / 0 warnings** |
| `python tools/validate-part1-photo-assets.py` | **9/9 PASS** |
| `python tools/sync-version.py --check` | **18/18 version markers PASS** |
| Repository integrity preflight | **407 local references/data files; 0 errors / 0 optional warnings** |
| Design-token audit | **0 new violations; 2,773 legacy findings remain warnings** |
| Python syntax (`python -m compileall -q tools`) | PASS |
| JavaScript syntax (`node --check sw.js` and every `assets/js/*.js`) | PASS |
| Service Worker update lifecycle | PASS; included in the 43/43 Node result |
| Word Family batch 025 tests | 5/5 PASS; included in the 161 Python result |
| Project progress report tests | 4/4 PASS after refreshing stale expected counts to 282/1,141 and 380 links |

The 17 fully executed focused Python modules and individual test counts are recorded in `PYTHON_TEST_SHARDS_v2.95.67.md` and its JSON companion. The two release-key validator cases are additional targeted tests and are not counted among those 161.

## Full Python inventory — explicitly incomplete

- Dynamic test discovery found **102 Python modules**. The 17 selected modules were run to completion and passed; this is not a full-suite run.
- `tools/tests/test_validator.py` contains 44 test methods. A full-module run did not finish within the available execution window and produced no final unittest summary. Two release-key-specific methods pass separately (2/2); the remaining module methods are not certified by that focused result.
- A subsequent sharded attempt also did not produce a completed inventory report. No incomplete module is promoted to PASS. The other unselected modules remain NOT RUN for this release.
- Therefore the overall Python inventory is **INCOMPLETE**, not 102/102 PASS. No Python test failures were observed in the 17 completed focused modules or the two targeted validator methods.

## Batch 025 and data audit

- Added six reciprocal `word_family` links across `apologize/apology`, `subscribe/subscription` and `transport/transportation`.
- Zero canonical headwords or IDs were added; the validator confirms the 1,141-ID baseline is unchanged.
- The read-only Word Family audit reports 1,141 headwords, 282 with at least one family link, and 380 directed links. Remaining review findings: 90 missing canonical targets, 1 target POS mismatch, 72 Vietnamese sense-anchor mismatches and 10 non-reciprocal links. Duplicate links, duplicate headwords and malformed records/links: 0. These are editorial triage flags, not automatic proof of incorrect family relationships.
- Related Glossary remains 567 entries; 248 distinct relation terms / 249 occurrences are still not joined to a canonical glossary entry. Placeholder definitions and missing IPA remain review queues; no unsupported definitions or pronunciation values were invented or inserted.

## Preservation / external acceptance

- No canonical headword spelling/ID, senses, definitions, examples, IPA, verb forms, synonyms or antonyms changed. Only the three existing canonical records' `word_family` arrays gained six reciprocal links; `data/manifest.json` carries the release marker, and `data/vocabulary/batch-025.json` records the provenance and exact before/after link snapshots.
- Question IDs, choice IDs/order, answer keys, Mock eligibility, learner IndexedDB schema/records, Robot Buddy privacy boundary and UI layout are unchanged.
- GitHub-hosted Actions, GitHub Pages deployment, update acceptance with an already-active old Service Worker, installed-PWA offline behavior and physical-device checks remain **UNVERIFIED**. Production deployment is not accepted by this local report.
