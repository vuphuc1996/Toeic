# Package verification — TOEIC Dictionary v2.95.56

- Exact base: `TOEIC_Dictionary_v2.95.55_FullSource.zip`.
- Target FullSource: `TOEIC_Dictionary_v2.95.56_FullSource.zip`.
- Patch: `TOEIC_Dictionary_v2.95.56_Patch_From_v2.95.55.zip`.
- FullSource is a one-root ZIP containing source/data/docs only; `.git`, caches, bytecode and test logs are excluded.
- Patch contains `patch.diff` and `PATCH_README.md`; its base SHA-256 is embedded in the README and the sidecar verifies the patch archive.
- Patch was applied to a clean extraction of the exact v2.95.55 FullSource. The replay tree was compared file-by-file and SHA-256-by-SHA-256 against the v2.95.56 FullSource extraction: 674 files / 674 files, byte-identical.
- FullSource and Patch each have a `.sha256` sidecar; `sha256sum -c` passed for both.
- The final archive names, exact hashes and sizes are recorded in the release handoff outside the source ZIP.
