# Package Verification — TOEIC Dictionary v2.95.71

## Exact predecessor and target

- Sole predecessor FullSource: `TOEIC_Dictionary_v2.95.70_FullSource.zip`
- Predecessor SHA-256: `1a0df44d309d127df3d3fb5012e7a6654c93a450c591f1f67575f4d15822e672`
- Predecessor source inventory: 864 files; ZIP CRC verified before extraction/editing.
- Target FullSource source inventory: 894 files; single root `Toeic_Dictionary_v2.95.71/`.
- Change operations: 30 added, 18 modified, 0 deleted.

## Package method

- FullSource was generated with the repository's `tools/package_source.py` contract from a clean, temporary committed Git snapshot; `audit-git-commit-readiness.py --require-clean` passed in that isolated staging repository.
- Patch layout follows `PATCH/README_PATCH.md`, `PATCH/PATCH_MANIFEST.json` and `PATCH/files/<relative-path>`; every payload operation records its target SHA-256.
- The Patch was generated exclusively by comparing the verified `.70` FullSource extraction with the `.71` target tree. No Patch was used as a source baseline.

## Exact replay

- Patch was applied to a fresh clean extraction of the exact `.70` predecessor.
- Replay inventory: **894/894** files.
- Extra files: **0**; missing files: **0**; byte-different files: **0**.
- Result: **PASS — byte-for-byte identical** to the target FullSource tree.
- Patch includes 48 source payload operations (30 add, 18 replace) plus the README and manifest (50 ZIP entries total).
- Both final ZIPs pass CRC verification; SHA-256 values are stored in the external `.sha256` sidecars and `TOEIC_Dictionary_v2.95.71_SHA256SUMS.txt`.

## Deployment boundary

This confirms local source packaging and exact Patch replay only. No Git push, hosted GitHub Actions run, GitHub Pages deployment, installed-PWA/offline propagation or physical-device acceptance is claimed.
