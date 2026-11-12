# Test report — TOEIC Dictionary v2.10.2

**Build:** v2.10.2 — Lexical Audit Batch 002 & Documentation Consolidation  
**Date:** 2026-11-09  
**Base:** v2.10.1  
**Runtime:** Python 3.13.5; Node.js 22.16.0

## Unit tests

| Test module | Cases | Result | Execution note |
|---|---:|---|---|
| `test_baseline_ids.py` | 13 | PASS 13/13 | Complete module run |
| `test_patch_data.py` | 11 | PASS 11/11 | Complete module run |
| `test_sync_version.py` | 12 | PASS 12/12 | Complete module run after docs paths migrated to `docs/` |
| `test_validator.py` | 33 | PASS 33/33 | 23 cases passed before the combined process timed out; remaining 10, including the timed-out case, were run individually and passed |
| **Total** | **69** | **PASS 69/69** | Counted by isolated modules/groups and individual cases; no claim of one monolithic discovery run |

## Data and version checks

- `python tools/validate-data.py`: PASS — 928 records, 0 ERROR, 12 legacy warnings unchanged (DF005=3, EX006=1, FD001=8 violations across 7 records).
- Coverage: IPA=574/928; `word_family`=131/928; `verb_forms`=291/928; collocations=758/928; synonyms=361; antonyms=213.
- Missing IPA: 354. Missing word-family list: 797; many records may legitimately have no relevant in-dictionary family.
- `python tools/sync-version.py --check`: PASS — `data/manifest.json`, `sw.js`, `index.html`, `docs/README.md`, `docs/MASTER_STATUS.md` and `docs/CHANGELOG.md` all match v2.10.2.
- `python -m py_compile tools/validate-data.py tools/sync-version.py tools/patch-data.py`: PASS.
- `node --check sw.js` and every `assets/js/*.js`: PASS.
- `.github/workflows/validate-data.yml`: YAML parse PASS.
- Service Worker APP_SHELL: 65 entries, 0 missing resources.
- HTML ID audit: 201 IDs, 0 duplicates.

## Data patch audit

- IPA patch: 11 operations, all previously blank values; sources and normalization are documented in `docs/sources/SOURCES_TOEIC_Dictionary_v2.10.2.md`.
- Word-family patch: 9 operations among existing headwords; no new headwords or off-dictionary forms.
- Both patch files passed dry-run before apply and use `baseDataVersion=2.10.1`, `targetDataVersion=2.10.2`, `idSetSha256` and `expect.old`.
- 928 IDs / 26 A–Z files / 32 topics retained. No data ID added, removed or renamed.

## Documentation consolidation

- All 22 project `.md` files are inside `docs/`; root contains no `.md` files.
- `docs/MASTER_STATUS.md` is the single authoritative project master.
- `docs/README.md` is the documentation index; `docs/CHANGELOG.md` is the version history.
- Historical reports, batches and source notes are sorted into `docs/reports/`, `docs/batches/`, and `docs/sources/`.
- Version synchronization tooling, its test fixtures and GitHub Actions path filters were updated for the new structure.

## Not yet verified

- GitHub Actions on the remote repository (requires push).
- GitHub Pages deployment, production Service Worker update/cache behavior.
- Real browser UI regression across desktop/laptop viewport sizes and zoom levels.
- iPhone Safari / Android Chrome real-device listening and voice quality.
- Actual Daniel en-GB voice availability remains OS/browser dependent; the user's earlier listening observation is not treated as a device lab QA result.

Do not mark deployment, CI remote, visual QA or physical-device QA as complete until tested on the target environment.
