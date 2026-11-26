# Package Verification — TOEIC Dictionary v2.95.69

## Source boundary

- Sole predecessor FullSource: `TOEIC_Dictionary_v2.95.68_FullSource.zip`
- Predecessor SHA-256: `2313f612e536c618b91fa1462611dffba7c9539f9e1a019a9b3ac4de79941c2a`
- Predecessor archive: 816 files; ZIP CRC verified before development. No older source, alternate archive or patch was used as an input.

## Final package contents

- FullSource: `TOEIC_Dictionary_v2.95.69_FullSource.zip` — **847 source files**, ZIP CRC valid.
- Patch: `TOEIC_Dictionary_v2.95.69_Patch_From_v2.95.68.zip` — **59 changed-path payloads** (31 added, 28 modified, 0 deleted), plus README and machine-readable manifest.
- Source comparison: 816 predecessor files → 847 target files; 31 added, 28 modified, 0 deleted.

## Exact clean Patch replay

The Patch was generated only from the source map of the exact predecessor ZIP and target `.69` working tree. It was then applied to a clean extraction of the predecessor FullSource. The replay result was compared against the complete target source path map and file bytes:

- Replayed files: **847**
- Extra files: **0**
- Missing files: **0**
- Byte-different files: **0**
- FullSource archive map vs target source: exact path and byte match; ZIP CRC valid.

The final package build is repeated after this report and Change Manifest are finalized. External `.sha256` sidecars hold the FullSource and Patch hashes; hashes are intentionally not embedded within the same package whose hash they describe.

## Data boundary

Only `data/manifest.json` (release marker `.68` → `.69`) and `data/related-terms.json` (15 existing metadata rows) differ under `data/`. All 1,141 canonical IDs match; protected learning-bank files are byte-identical. See `DATA_DIFF_v2.95.69.md` and `CHANGE_MANIFEST_v2.95.69.md` for detail.

## Acceptance boundary

Clean Patch replay establishes source-package reproducibility only. Hosted GitHub Actions, live GitHub Pages deployment, installed-PWA update/offline propagation and physical-device acceptance remain unverified. This is a locally verified release candidate, not a production-deployment acceptance.
