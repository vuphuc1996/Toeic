# Package Verification — TOEIC Dictionary v2.95.70

## Baseline

- Exact predecessor: `TOEIC_Dictionary_v2.95.69_FullSource.zip`
- SHA-256: `4ec559a2117a1b1b38ef95d4a0d6955431b46e701cf208bd939bd38db232e853`
- Baseline source files: 847
- Baseline ZIP CRC: verified before extraction.

## Candidate contents

- Target release: `2.95.70`
- Target FullSource file count: 864 (excluding transient `__pycache__`, bytecode and test-runner output).
- Patch source-path operations: 32 total — 17 added, 15 modified, 0 deleted.
- FullSource root folder: `Toeic_Dictionary_v2.95.70/`.
- Patch is generated from the single verified `.69` baseline, not used as an input source.

## Replay contract

The final Patch is replayed onto a second clean extraction of the exact `.69` FullSource. The replayed tree is recursively compared against the final FullSource file-by-file and byte-for-byte. Acceptance requires equal path inventories, equal file counts, 0 extra paths, 0 missing paths and 0 byte-different files. Final measured replay results and archive SHA-256 values are also recorded in the external `.sha256` sidecars and delivery summary.

## Integrity and exclusion rules

- Both archives must pass `zipfile.testzip()`/CRC validation.
- ZIP SHA-256 values are recorded in adjacent sidecar files and external `SHA256SUMS.txt`; hashes are not embedded here to avoid a self-referential package checksum.
- No `.git`, `__pycache__`, `.pyc`, `.pyo`, `.pytest_cache`, checkpoint, local runner log or generated ZIP is included in FullSource.
- No files are deleted by this release Patch.

## Acceptance boundary

A successful clean replay verifies package reconstruction only. It does not prove hosted GitHub Actions, GitHub Pages deployment, Service Worker propagation on an installed PWA, offline/reconnect behavior or physical-device behavior. Those remain unverified until performed against a deployed build.
