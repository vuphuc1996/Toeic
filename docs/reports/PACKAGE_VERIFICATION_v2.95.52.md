# Package Verification — TOEIC Dictionary v2.95.52

## Canonical base

- Base archive: `TOEIC_Dictionary_v2.95.51_FullSource.zip`
- Base SHA-256: `4b3e2fcf937fc44c11cfd83ba722d694306bfd156d4b8eefe35d75bcb3237952`
- Base files: 588

## Target package

- FullSource: `TOEIC_Dictionary_v2.95.52_FullSource.zip`
- Patch: `TOEIC_Dictionary_v2.95.52_Patch_From_v2.95.51.zip`
- Target root: `Toeic_Dictionary_v2.95.52/`
- Target files: **616**
- Patch operations: **28 adds, 19 modifies, 0 deletes**.

## Verification

FullSource CRC/root/content verification, Patch base preconditions, exact replay and byte-for-byte comparison are performed during package construction. SHA-256 sidecars accompany both artifacts.

## Test and acceptance boundary

- Python suite: 91/91 modules terminal; 704 PASS / 1 accepted environment SKIP / 0 FAIL / 0 ERROR / 0 TIMEOUT / 0 NOT RUN.
- Related Glossary regression family: 131/131 PASS.
- Local workflow shell replay: 113/113 run steps PASS; this is not hosted GitHub Actions.
- Data validator: 1,141 records; 0 ID additions/removals; 0 ERROR / 0 WARNING.
- Independent editorial review of eleven Batch 041 paraphrases remains pending.
- Hosted GitHub Actions, Pages deployment, PWA update/cache propagation, offline behavior and physical-device acceptance remain unverified.
