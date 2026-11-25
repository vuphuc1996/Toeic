# Package Verification — TOEIC Dictionary v2.95.59

## Canonical source

- Exact predecessor FullSource: `TOEIC_Dictionary_v2.95.58_FullSource.zip`
- Predecessor SHA-256: `67dd7d59a8f63bdb1307780dd95dd52e75f1b25af143ac0cef2a42e938b3d5cc`
- Target FullSource: `TOEIC_Dictionary_v2.95.59_FullSource.zip`
- Target Patch: `TOEIC_Dictionary_v2.95.59_Patch_From_v2.95.58.zip`
- Target archive hashes are recorded in adjacent `.sha256` sidecars and were checked with `sha256sum -c` after final packaging.

## Exact patch replay

- Patch was generated from the exact v2.95.58 extracted tree and v2.95.59 target tree.
- Replay was performed on a fresh extraction of the exact predecessor FullSource.
- `git apply --check` and `git apply` completed successfully.
- Replayed target files: 703; target FullSource files: 703.
- Replay-only paths: 0; target-only paths: 0; differing file hashes: 0.
- Result: **703/703 files byte-identical**.

## Archive integrity

- FullSource ZIP CRC: PASS; one versioned root.
- Patch ZIP CRC: PASS.
- FullSource and Patch SHA-256 sidecars: generated and verified against final archives.
- Generated caches, `.pyc`, `.zip`, `.log`, and `.git` are excluded from FullSource.

## Acceptance boundary

The local focused regression suite and Node regression scripts passed as recorded in `TEST_REPORT_TOEIC_Dictionary_v2.95.59.md`. Full Python discovery was not run. Hosted GitHub Actions, Pages, PWA cache propagation and physical-device acceptance remain UNVERIFIED.
