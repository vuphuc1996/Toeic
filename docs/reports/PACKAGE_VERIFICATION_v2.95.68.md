# Package Verification — TOEIC Dictionary v2.95.68

## Exact source chain

- Base: `TOEIC_Dictionary_v2.95.67_FullSource(1).zip`.
- Base SHA-256: `1f262ac4d67d8d244facf397b9ea1d179c6a741f50e561b3d3e9805efef31754`.
- Target: `TOEIC_Dictionary_v2.95.68_FullSource.zip`.
- Patch: `TOEIC_Dictionary_v2.95.68_Patch_From_v2.95.67.zip`.

## FullSource archive

- Package builder: `tools/package_source.py` using `git archive` from the final committed source tree.
- Source files in archive: **816**.
- ZIP root: exactly `Toeic_Dictionary_v2.95.68/`.
- Duplicate archive paths: 0; ZIP CRC validation: **PASS**.
- SHA-256 is recorded in the detached `TOEIC_Dictionary_v2.95.68_FullSource.zip.sha256` sidecar, outside the archive to avoid a recursive self-checksum.

## Patch archive and replay

- Patch contains four entries under one root: `source.patch`, `PATCH_MANIFEST.json`, `BASE_SHA256.txt` and `README_PATCH.md`; ZIP CRC: **PASS**.
- Git diff is generated from the exact v2.95.67 baseline commit to the v2.95.68 target commit: 26 changed paths (9 added, 17 modified, 0 removed).
- `git apply --check source.patch`: **PASS** against a fresh extraction of the exact v2.95.67 FullSource.
- `git apply source.patch`: **PASS**.
- Replay tree vs extracted target FullSource: **816 files each; 0 added, 0 removed, 0 modified**; byte-for-byte identical.
- Patch manifest binds the exact predecessor SHA-256 and target FullSource SHA-256. Patch archive SHA-256 is recorded in its detached `.sha256` sidecar.

## Acceptance boundary

- Exact source ancestry, FullSource packaging, ZIP integrity and Patch replay are locally verified.
- Full Python discovery remains incomplete as documented in `TEST_REPORT_TOEIC_Dictionary_v2.95.68.md`; focused Python tests and all 44 Node regressions pass.
- This is source-package acceptance evidence only. It is not GitHub Actions, production deployment, installed-PWA/offline or physical-device acceptance.
