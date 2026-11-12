# Test report — TOEIC Dictionary v2.10.0

**Build:** v2.10.0 — Smart Review, Flashcard Layout & Natural TTS  
**Date:** 2026-11-09  
**Base:** v2.9.11 IPA & Word Family Review ZIP  
**Runtime:** Python 3.13.5; Node.js 22.16.0

## Automated tests

| Test module | Cases | Result | Execution note |
|---|---:|---|---|
| `test_baseline_ids.py` | 13 | PASS 13/13 | Executed by module/group |
| `test_patch_data.py` | 11 | PASS 11/11 | Executed by module/group |
| `test_sync_version.py` | 12 | PASS 12/12 | Executed in smaller groups/individual cases; do not interpret as one monolithic discovery run |
| `test_validator.py` | 33 | PASS 33/33 | Executed in smaller groups/individual cases because the long combined process can time out in this sandbox |
| **Total** | **69** | **PASS 69/69** | Every test case was accounted for in the grouped test execution recorded for this release; a single full `unittest discover` run is not claimed |

## Data, release and static checks

- `python tools/validate-data.py`: PASS — 928 records, 0 ERROR, 12 known legacy warnings (DF005=3, EX006=1, FD001=8 violations across 7 records).
- Coverage retained from v2.9.11: IPA=563, word_family=122, verb_forms=291, collocations=758, synonyms=361, antonyms=213.
- `python tools/sync-version.py --check`: PASS — manifest and all 2.10.0 version markers match.
- `python -m py_compile tools/validate-data.py tools/sync-version.py tools/patch-data.py`: PASS.
- `node --check sw.js` and every `assets/js/*.js`: PASS.
- HTML parse and duplicate-ID inspection: PASS; 201 unique IDs, no duplicate IDs.
- Required Smart Review and TTS controls: PASS in static DOM inspection.
- Service Worker app shell: 65 resources (38 required, 27 optional), 0 missing files.
- `.github/workflows/validate-data.yml`: parsed successfully.
- Vocabulary baseline: all 928 IDs retained; 26 A–Z files remain; no base vocabulary record was changed by the UX release.
- ZIP `testzip()` and extracted-package rechecks: PASS.

## Implemented scope

- Smart Review answer modal; result/choice explanation; OK acknowledgment; auto-next countdown only after OK; manual-next fallback; review-pending state persisted in the practice session.
- Responsive font scaling and stable question/answer workspace.
- Fixed illustration/content frames for Flashcard and topic cards; no emoji/icon overlay in the image center; icon retained in the topic title; image error fallback.
- A–Z rail uses horizontal flex scrolling with larger touch targets, spacing, snap and preserved scroll position.
- On-device male/female English voice selection, manual override, per-group preview, saved voice URI, accent, rate, pitch, volume, word gap and dialogue-turn gap settings.
- Vocabulary sequence speaks one headword per utterance with a 900 ms default gap (configurable 600–1,300 ms); dialogue keeps whole sentences and pauses at turn boundaries.
- Stop cancels current speech and pending gap timers.
- `personalVocabulary` schema v3 `overrideBaseSigs` migration and Import/Export preservation.

## Not yet verified on target environments

- Real browser UI interaction and visual regression testing across viewport sizes.
- iPhone Safari, Android Chrome and physical desktop browser QA.
- Actual male/female voice availability, clarity and perceived quality on the user's voice packs. Web Speech API only exposes voices provided by the OS/browser; rate/pitch/volume do not provide EQ or noise reduction and cannot guarantee a clear male voice on every device.
- GitHub Actions on the remote repository, GitHub Pages deployment and production Service Worker/cache behavior.

Do not mark these target-environment checks as passed until performed on the actual devices/repository.
