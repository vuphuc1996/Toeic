# Package verification — TOEIC Dictionary v2.95.55

Date: 2026-11-24

## Exact source lineage

- Base archive: `TOEIC_Dictionary_v2.95.54_FullSource.zip`
- Base archive SHA-256: `05912f844fb0cd6a9997cd99964ef4ef887325fdb7d7520445994ded625f28ce`
- The base ZIP contained no upstream `.git` metadata. A local Git baseline was reconstructed from its exact contents solely to enforce clean commits and generate a reproducible patch. These local commits are not GitHub commits.

## Package contents

- FullSource: `TOEIC_Dictionary_v2.95.55_FullSource.zip`
- Patch: `TOEIC_Dictionary_v2.95.55_Patch_From_v2.95.54.zip`
- FullSource contains **664 tracked source/data/docs files** under one root folder `Toeic_Dictionary_v2.95.55/`; `.git`, logs, caches and generated runtime artifacts are excluded.
- Patch delta from the exact v2.95.54 base: **14 added / 10 modified / 0 deleted files**.
- Patch is a binary-capable unified diff plus README and exact base SHA-256 precondition.
- Final SHA-256 values are recorded in the adjacent `.sha256` sidecars and must be checked before use.

## Replay verification

1. Extract the exact v2.95.54 FullSource archive.
2. Verify its SHA-256 against the base hash above.
3. Run `git apply --check patch.diff`, then `git apply patch.diff` on the extracted tree.
4. Compare the resulting tree recursively against the extracted v2.95.55 FullSource.

Result: **PASS — patch applies cleanly and every file is byte-for-byte identical to the FullSource tree.**

The patch contains no vocabulary/question identity or learner-history migrations. Existing IndexedDB database/version/store remain unchanged.
