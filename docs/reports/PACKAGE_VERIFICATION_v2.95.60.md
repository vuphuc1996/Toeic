# Package Verification — TOEIC Dictionary v2.95.60

## Canonical base

- Exact base archive: `TOEIC_Dictionary_v2.95.59_FullSource.zip`.
- Base SHA-256: `b5dbb4e7c974814c8d59fc6bf653737f7208e7da2c2d49141078efff385d993c`.
- Base archive entries: 703.

## Target package

- FullSource: `TOEIC_Dictionary_v2.95.60_FullSource.zip`.
- Patch: `TOEIC_Dictionary_v2.95.60_Patch_From_v2.95.59.zip`.
- One versioned root; **720 files**; generated caches, bytecode, logs, nested ZIPs and temporary files excluded.
- FullSource SHA-256 and exact file count are recorded in adjacent sidecars and the final release handoff.

## Patch safety

- Patch generated from the exact v2.95.59 extracted tree after verifying its archive hash.
- Patch is a Git binary-capable unified diff and must be applied only to a fresh extraction of that exact base.
- Patch operations: **17 adds / 12 modifies / 0 deletes**.
- Exact patch replay was performed in an isolated copy: **720/720 files byte-identical** to FullSource.
- Final FullSource and Patch SHA-256 values are recorded in their adjacent `.sha256` sidecars; the sidecars are generated after the package contents are frozen.

## Verification boundary

- ZIP CRC/root/content, base SHA, patch application and byte-for-byte replay are separate from functional test completion.
- Python full-suite status is INCOMPLETE (17/94 modules, 126 cases passed, 77 not run); see the test report and shard report.
- Hosted GitHub Actions, GitHub Pages, PWA cache propagation/offline behavior and physical-device QA are UNVERIFIED.
