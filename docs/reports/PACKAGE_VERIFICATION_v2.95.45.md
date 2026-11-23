# Package Verification — TOEIC Dictionary v2.95.45

## Exact source delta

Compared with the released v2.95.44 source tree (664 files), the final v2.95.45 source tree contains **698 packageable files**: **34 added**, **21 modified**, **0 deleted**, and **643 byte-identical common paths**. Local `logs/`, `.git`, caches, bytecode and transient files are excluded.

## Full Source contract

- ZIP: `TOEIC_Dictionary_v2.95.45_FullSource.zip`
- One root folder: `Toeic_Dictionary_v2.95.45/`
- 698 source files.
- CRC, one-root and exclusion checks must pass.

## Patch contract

- ZIP: `TOEIC_Dictionary_v2.95.45_Patch.zip`
- Base: released v2.95.44 FullSource.
- 55 overlay entries: 21 modified files + 34 added files; no deletion operations.
- Patch entries are rooted at `Toeic_Dictionary_v2.95.45_Patch/` and use the same relative source paths.

## Replay verification

The patch is applied to a fresh extraction of released v2.95.44. The replay tree is compared to the final v2.95.45 source using SHA-256 for every packageable relative path. Release is accepted only with 698/698 files byte-identical and zero missing/extra/mismatched paths.

The external release-folder `PACKAGE_VERIFICATION.json` records actual file counts, replay results, ZIP sizes and SHA-256 values. Adjacent `.sha256` files are generated from the final ZIP bytes.
