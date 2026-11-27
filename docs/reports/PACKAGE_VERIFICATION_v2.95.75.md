# Package Verification — TOEIC Dictionary v2.95.75

## Predecessor & target inventory

- Preserved baseline: local completed `v2.95.74` snapshot (ahead of GitHub `candidate` `cfae6ce`, which was at `v2.95.73`).
- Target FullSource archive: `/tmp/TOEIC_Dictionary_v2.95.75_FullSource.zip` (generated outside `/app/applet` to keep the source tree clean of release artifacts).
- Sidecar checksum: `/tmp/TOEIC_Dictionary_v2.95.75_FullSource.zip.sha256` (external sidecar prevents self-referential hash recursion inside the source tree).
- Commit-ready Phase A patch against `candidate` (`c7a2f445589aa2a248dddbe7bf9d2dbef2d1c483`): `/tmp/v2.95.75_phaseA_ci_recovery.patch` + `.sha256`.
- Single archive root folder: `Toeic_Dictionary_v2.95.75/`
- Target packagable file inventory: **1,552** files (`data/`: 70 files; `docs/`: 1,101 files; `tools/`: 236 files; `assets/`: 59 files; `patches-related-terms/`: 47 files; `patches/`: 27 files; root & `.github/`/`design/`: 12 files).

## Exclusion & cleanliness policy

- Built using the exact exclusion rules defined in `tools/package_source.py` and `.gitignore`:
  - Excluded directories: `.git/`, `node_modules/`, `logs/`, `__pycache__/`, `.pytest_cache/`, `release/`, `releases/`, `archive/`, `release_*`.
  - Excluded suffixes: `.zip`, `.bundle`, `.log`, `.pyc`, `.tmp`, `.sha256`, `.tar`, `.tar.gz`.
- Verified zero `.zip`, `.patch`, or `.sha256` archives exist inside `/app/applet`.

## Verification checks

- `zipfile.ZipFile.testzip()` CRC integrity check: **PASS** (0 corrupted entries).
- Single root prefix check (`Toeic_Dictionary_v2.95.75/`): **PASS**.
- Exclusion audit against archived entry paths: **PASS** (0 excluded auxiliary/build/log paths included).
- Clean temp extraction check (`/tmp/extract_v29575_check/`): **PASS** (`1,552` extracted files; `package.json` and `data/manifest.json` both read `2.95.75` and match `/app/applet` byte-for-byte).
- Patch archive note: `/tmp/v2.95.75_phaseA_ci_recovery.patch` provides the exact `git diff` against `candidate` `c7a2f445589aa2a248dddbe7bf9d2dbef2d1c483` for commit/push where remote credentials are available.

## Deployment boundary

This confirms local FullSource ZIP packaging, CRC integrity, exclusion compliance, clean extraction, and patch generation only. No Git push to `candidate`, hosted GitHub Actions run, GitHub Pages deployment, installed-PWA cache propagation, or physical-device QA is claimed.
