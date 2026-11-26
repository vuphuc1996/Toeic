# Package Verification — TOEIC Dictionary v2.95.66

## Baseline and derivation

- Sole predecessor: `TOEIC_Dictionary_v2.95.65_FullSource.zip`.
- Predecessor SHA-256: `a1b95e807e08052bfa599a08ff88bc3237ae086688557ce3ae77b78e814814fb`.
- The v2.95.65 source tree was restored from that exact archive before changes. The older v2.95.64 archive, earlier work folders and previous Patch files were not used as source.
- FullSource is generated from the final committed v2.95.66 Git tree using `tools/package_source.py`.
- Patch is generated from the exact Git diff `v2.95.65 baseline commit → v2.95.66 release commit` only.

## FullSource verification

- Expected archive root: exactly one directory, `Toeic_Dictionary_v2.95.66/`.
- Expected source inventory: **795 files** (the 779-file predecessor plus 16 release additions).
- ZIP integrity is checked with `zipfile.testzip`; the extracted archive inventory and SHA-256 of every file are compared against the exact tracked release tree.
- Git metadata, Python bytecode/cache folders and local test execution logs are excluded by the package-source contract.
- A detached `.sha256` sidecar is provided; the archive checksum is verified with `sha256sum -c`.

## Patch verification

- Patch contains exactly four members: `PATCH_README.md`, `PATCH_MANIFEST.json`, `BASE_SHA256.txt`, and `patch.diff`.
- Manifest binds the patch to the exact predecessor FullSource SHA-256 above and the final FullSource SHA-256.
- A fresh extraction of the exact v2.95.65 FullSource is used for `git apply --check` and `git apply`.
- The replayed tree must match the final FullSource file-by-file: **795/795**, zero missing, extra or byte-mismatched files.
- Patch ZIP CRC and detached `.sha256` sidecar are checked.

## Data / release boundary

- Only `data/manifest.json` changes under `data/`, and only the version value changes from 2.95.65 to 2.95.66.
- No vocabulary or Related Glossary content, canonical IDs/headwords/relations, question/choice/answer-key records, Mock eligibility, learner IndexedDB records/schema, or Robot Buddy privacy boundary changes.
- Hosted GitHub Actions, GitHub Pages deployment and real installed-PWA/device acceptance are separate gates; they are not inferred from local packaging success.
