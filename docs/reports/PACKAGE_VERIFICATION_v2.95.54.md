# Package Verification — TOEIC Dictionary v2.95.54

## Canonical base

- Base archive: `TOEIC_Dictionary_v2.95.53_FullSource.zip`
- Base SHA-256: `021961c36fa7e71611fc44ad8e2f70d9111f801ea1aecafd86e1507e6c37228b`
- Base files: 638

## Target package

- FullSource: `TOEIC_Dictionary_v2.95.54_FullSource.zip`
- Patch: `TOEIC_Dictionary_v2.95.54_Patch_From_v2.95.53.zip`
- Target root: `Toeic_Dictionary_v2.95.54/`
- Target files after final documentation commit: 650
- Patch operations after final documentation commit: 14 adds, 25 modifies, 2 deletes. The two deletes are the root-level update-note files relocated under `docs/versions/legacy/`; no application or learning data files were deleted.

## Package integrity

- FullSource ZIP CRC/root/content verification: PASS.
- Patch base SHA and every add/modify/delete precondition: PASS.
- Exact Patch replay against the canonical base: PASS.
- Replayed tree byte-for-byte comparison with FullSource: PASS.
- FullSource and Patch SHA-256 sidecars: PASS.

## Test and acceptance boundary

- Full Python discovery: 711/711 PASS; 0 FAIL / 0 ERROR / 0 SKIP; 135.824 seconds under Python 3.13.5.
- Data validator: 1,141 records; 0 ID additions/removals; 0 ERROR / 0 WARNING.
- Version synchronization: all 13 registered markers and changelog PASS.
- Patch-data tests 20/20; editorial review queue 8/8; historical glossary 036/037/038 tests 21/21; CI coverage 3/3.
- CI workflow includes full `python -m unittest discover -s tools/tests -v` after existing targeted test steps.

## Production acceptance boundary

Claude independent rerun of this new archive, hosted GitHub Actions, GitHub Pages deployment, Service Worker propagation, offline behavior, Safari/iPad physical-device behavior and TTS hardware voices remain UNVERIFIED.
