# Package Verification — TOEIC Dictionary v2.95.49

## Canonical base

- Base archive: `TOEIC_Dictionary_v2.95.48_FullSource.zip`
- Base SHA-256: `0d6555bf768348bb18f231c8d41f54fa36711b1aa4769dcd68dbcd374d9eff3f`
- Base files: 510

## Target package

- FullSource: `TOEIC_Dictionary_v2.95.49_FullSource.zip`
- Patch: `TOEIC_Dictionary_v2.95.49_Patch_From_v2.95.48.zip`
- Target root: `Toeic_Dictionary_v2.95.49/`
- Target files: **539**
- Patch operations: **29 adds, 11 modifies, 0 deletes**.

## Patch safety

The patch manifest binds to the exact predecessor archive SHA-256 and contains per-file SHA-256 preconditions for every modified/deleted file, plus target hashes for every added/modified payload. Patch replay must be performed against the exact base archive; do not apply to another v2.95.48 build.

## Exclusions

FullSource excludes `.git`, logs, `__pycache__`, `.pyc`, `.zip`, temporary and generated runtime log artifacts. All project source, tests, canonical data and versioned reports remain included.

## Verification

FullSource CRC/root/content verification, Patch precondition verification, exact replay and byte-for-byte target comparison were performed successfully. Adjacent SHA-256 sidecars contain final artifact digests. Package integrity is distinct from production deployment acceptance.
