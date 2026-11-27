# Package Verification — TOEIC Dictionary v2.95.75

## Predecessor & target inventory

- Preserved baseline: local completed `v2.95.74` snapshot (ahead of GitHub `candidate` `cfae6ce`, which was at `v2.95.73`).
- Target FullSource archive: `/tmp/TOEIC_Dictionary_v2.95.75_FullSource.zip` (generated outside `/app/applet` to keep the source tree clean of release artifacts).
- Sidecar checksum: `/tmp/TOEIC_Dictionary_v2.95.75_FullSource.zip.sha256` (external sidecar prevents self-referential hash recursion inside the source tree).
- Single archive root folder: `Toeic_Dictionary_v2.95.75/`
- Target packagable file inventory: **1,550** files (`data/`: 70 files; `docs/`: 1,100 files; `tools/`: 235 files; `assets/`: 59 files; `patches-related-terms/`: 47 files; `patches/`: 26 files; root & `.github/`/`design/`: 13 files).

## Exclusion & cleanliness policy

- Built using the exact exclusion rules defined in `tools/package_source.py` and `.gitignore`:
  - Excluded directories: `.git/`, `node_modules/`, `logs/`, `__pycache__/`, `.pytest_cache/`, `release/`, `releases/`, `archive/`, `release_*`.
  - Excluded suffixes: `.zip`, `.bundle`, `.log`, `.pyc`, `.tmp`, `.sha256`, `.tar`, `.tar.gz`.
- Verified zero `.zip` or `.sha256` archives exist inside `/app/applet`.

## Verification checks

- `zipfile.ZipFile.testzip()` CRC integrity check: **PASS** (0 corrupted entries).
- Single root prefix check (`Toeic_Dictionary_v2.95.75/`): **PASS**.
- Exclusion audit against archived entry paths: **PASS** (0 excluded auxiliary/build/log paths included).
- Clean temp extraction check (`/tmp/extract_v29575_check/`): **PASS** (`1,550` extracted files; `package.json` and `data/manifest.json` both read `2.95.75` and match `/app/applet` byte-for-byte).
- Patch archive note: a standalone `PATCH` ZIP was not generated because the workspace contains no `.git` history and no external `v2.95.74` FullSource base archive was mounted; instead `DATA_DIFF_v2.95.75.md` and `CHANGE_MANIFEST_v2.95.75.md` document the exact file-level delta.

## Deployment boundary

This confirms local FullSource ZIP packaging, CRC integrity, exclusion compliance, and clean extraction only. No Git push to `candidate`, hosted GitHub Actions run, GitHub Pages deployment, installed-PWA cache propagation, or physical-device QA is claimed.
