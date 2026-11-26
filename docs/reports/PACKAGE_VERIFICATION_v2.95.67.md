# Package Verification — TOEIC Dictionary v2.95.67

## Baseline and derivation

- Sole predecessor: `TOEIC_Dictionary_v2.95.66_FullSource.zip`.
- Predecessor SHA-256: `30236500cfa2d8702a25cdca9c99f0eca58eaaa047928a6b12ce88b1b2a373c3`.
- The predecessor tree is reconstructed from that exact one-root FullSource archive before applying the release changes. No earlier archive, Patch, alternate branch or stale working directory is used.
- FullSource is generated from a committed Git tree using `tools/package_source.py`.
- Patch is generated from the exact Git diff between the v2.95.66 extracted baseline snapshot and the final v2.95.67 source commit.

## FullSource verification contract

- Expected archive root: exactly one directory, `Toeic_Dictionary_v2.95.67/`.
- Expected packaged inventory: **807 files** (795 predecessor files + 12 new source/data/report files; modified files do not change the count).
- ZIP CRC is checked with `ZipFile.testzip`; the extracted FullSource inventory and SHA-256 of every path are compared with the final committed source tree.
- Git metadata, Python bytecode/cache folders, local test logs and generated ZIP/checksum artifacts are excluded by the package-source contract.
- A detached `.sha256` sidecar is emitted for the archive; the sidecar is checked with `sha256sum -c`.

## Patch verification contract

- Patch contains exactly four members: `PATCH_README.md`, `PATCH_MANIFEST.json`, `BASE_SHA256.txt` and `patch.diff`.
- `PATCH_MANIFEST.json` binds the patch to the exact v2.95.66 FullSource SHA-256 and final v2.95.67 source snapshot, with file-level change counts.
- A clean extraction of the exact predecessor is initialized as the baseline Git snapshot. `git apply --check` and `git apply` are executed against that clean tree.
- The replayed result is compared with the release tree file-by-file: **807/807 identical**, with zero missing, extra or byte-mismatched paths.
- Patch ZIP CRC and detached `.sha256` sidecar are verified independently.

## Release and deployment boundary

- This is a locally packaged source candidate. The focused Python suite is 17 modules / 161 cases PASS plus two separately targeted validator methods PASS; the complete 102-module Python inventory remains incomplete.
- Data validation confirms 1,141 canonical IDs, no additions/removals, zero errors and zero warnings. The new Batch 025 modifies only three existing records' `word_family` arrays and adds a source ledger; the manifest version marker is also updated.
- No learner IndexedDB schema/records, Mock eligibility, question IDs, choice IDs/order, answer keys, UI layout or Robot Buddy privacy rules are changed.
- GitHub-hosted Actions, GitHub Pages deployment, service-worker update acceptance in a live browser, installed-PWA offline propagation and real device checks are separate gates and remain **UNVERIFIED** until executed against the hosted application.
