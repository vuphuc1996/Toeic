# Package Verification — TOEIC Dictionary v2.95.63

## Baseline and derivation

- Sole predecessor: `TOEIC_Dictionary_v2.95.62_FullSource.zip`.
- Predecessor SHA-256: `b9d56cd27d0d13c4c8781732ac72c17b526b2aa451fa1393c39fd30820260f96`.
- The final source tree was reconstructed from that exact archive. The v2.95.60 upload and all other old/intermediate sources were excluded.
- The FullSource is generated from the committed v2.95.63 Git tree using `tools/package_source.py`, not from an extracted working folder or an older Patch.
- The Patch is generated from the Git diff `v2.95.62 baseline commit → v2.95.63 release commit` only.

## FullSource verification

- ZIP integrity (`zipfile.testzip`) must pass and the archive must contain exactly one root directory: `Toeic_Dictionary_v2.95.63/`.
- Final archive: **758 files**, one root `Toeic_Dictionary_v2.95.63/`; ZIP CRC passed. The unpacked archive inventory and SHA-256 of every file match the exact tracked v2.95.63 source tree (758/758, zero differences).
- Runtime-only `__pycache__`/`.pyc`, Git metadata and generated local logs are excluded by the package contract.

## Patch verification

- Patch contains the binary Git diff and a manifest binding it to the v2.95.62 FullSource SHA-256 above.
- Patch diff SHA-256 and release commit are bound in the Patch manifest and are independently verified during replay.
- Patch replay was performed on a fresh extraction of the exact v2.95.62 archive. `git apply --check` and `git apply` both succeeded.
- The replayed tree matched the final FullSource file-by-file: **758/758**, zero missing, zero extra and zero byte-mismatched files. Patch ZIP CRC passed and it contains exactly four members (README, manifest, base checksum and binary diff).
- Detached `.sha256` sidecars are provided for both release ZIP files and checked with `sha256sum -c`. Output checksums are intentionally not embedded in this report because the report itself is part of FullSource and self-referential checksums are not meaningful.

## Release boundary

- Only `data/manifest.json` changes under `data/`, and only the release version value changes. All other data files remain byte-identical to v2.95.62.
- No vocabulary/question identities, relations, answer keys, learner storage schema/data, CSS redesign, or hosting/backend architecture changes are included.
- ZIP CRC, exact tree comparison and Patch replay results are verified in the release execution log before artifacts are delivered.
