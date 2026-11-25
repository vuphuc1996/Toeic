# Package Verification — TOEIC Dictionary v2.95.51

## Canonical base

- Base archive: `TOEIC_Dictionary_v2.95.50_FullSource.zip`
- Base SHA-256: `f1fe475725d218581ff4868a979ccba242b2b5a605ec4d94df390cf8a91fa849`
- Base files: 559

## Target package

- FullSource: `TOEIC_Dictionary_v2.95.51_FullSource.zip`
- Patch: `TOEIC_Dictionary_v2.95.51_Patch_From_v2.95.50.zip`
- Target root: `Toeic_Dictionary_v2.95.51/`
- Target files: **588**
- Patch operations: **29 adds, 18 modifies, 0 deletes**.
- Superseded local Python-suite scratch folders were intentionally excluded; final machine-readable suite evidence is retained outside the source package and summarized in the Test Report.

## Verification

FullSource CRC/root/content verification, Patch base preconditions, exact replay and byte-for-byte comparison are required and performed during package construction. SHA-256 sidecars accompany both artifacts.

## Test and acceptance boundary

- Python suite: 90/90 modules terminal; 700 PASS / 1 accepted environment SKIP / 0 FAIL / 0 ERROR / 0 TIMEOUT / 0 NOT RUN.
- Local workflow shell replay: 112/112 run steps PASS.
- Hosted GitHub Actions, GitHub Pages deployment, PWA update/cache propagation, offline behavior and physical-device acceptance remain unverified.
- Independent editorial review of six Batch 040 paraphrases remains pending.
