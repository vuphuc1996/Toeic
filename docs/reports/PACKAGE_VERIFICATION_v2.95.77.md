# Package Verification — TOEIC Dictionary v2.95.77

## Predecessor & target inventory

- Baseline: commit `035dd6e2001b3b049407f71acd21f9c33f33e776` (`v2.95.76`).
- Target release: `v2.95.77`
- Target FullSource archive: `/tmp/TOEIC_Dictionary_v2.95.77_FullSource.zip` (generated outside `/app/applet` to keep source tree clean).
- Sidecar checksum: `/tmp/TOEIC_Dictionary_v2.95.77_FullSource.zip.sha256`.
- Single archive root folder: `Toeic_Dictionary_v2.95.77/`
- Target packagable file inventory: **1,557** files.

## Exclusion & cleanliness policy

- Built using exact rules defined in `tools/package_source.py` and `.gitignore`:
  - Excluded directories: `.git/`, `node_modules/`, `logs/`, `__pycache__/`, `.pytest_cache/`, `release/`, `releases/`, `archive/`, `release_*`.
  - Excluded suffixes: `.zip`, `.bundle`, `.log`, `.pyc`, `.tmp`, `.sha256`, `.tar`, `.tar.gz`.
- Verified zero `.zip`, `.patch`, or `.sha256` archives exist inside `/app/applet`.

## Verification checks

- `zipfile.ZipFile.testzip()` CRC integrity check: **PASS** (0 corrupted entries).
- Single root prefix check (`Toeic_Dictionary_v2.95.77/`): **PASS**.
- Clean temp extraction check (`/tmp/extract_v29577_check/`): **PASS** (`1,557` extracted files; `package.json` and `data/manifest.json` both read `2.95.77` and match `/app/applet` byte-for-byte).

## Deployment boundary

This confirms local FullSource ZIP packaging, CRC integrity, exclusion compliance, and clean extraction only. No Git push to `candidate`, hosted GitHub Actions run, GitHub Pages deployment, installed-PWA cache propagation, or physical-device QA is claimed.
