# Data Difference Report — TOEIC Dictionary v2.95.68

## Exact comparison baseline

- Sole baseline: `TOEIC_Dictionary_v2.95.67_FullSource(1).zip`.
- Baseline ZIP SHA-256: `1f262ac4d67d8d244facf397b9ea1d179c6a741f50e561b3d3e9805efef31754`.
- ZIP was CRC-tested and contains 807 source entries before extraction.

## Full `data/` tree comparison

- Baseline data files: **68**; current data files: **68**; path sets identical: **True**.
- Baseline composite data-tree SHA-256: `4af97fe950714b2c44b5924e2cc0466e6ddbdc7f426995b7d3830c20334fb45f`.
- Current composite after normalizing only `data/manifest.json.version` back to `2.95.67`: `4af97fe950714b2c44b5924e2cc0466e6ddbdc7f426995b7d3830c20334fb45f`.
- Result: **all 68/68 data files are byte-identical after normalization of the single release marker**.
- The only data-file difference in v2.95.68 is `data/manifest.json`: `version` changed from `2.95.67` to `2.95.68`. No vocabulary or question-bank JSON was changed.

## Canonical vocabulary identity

- Canonical records/headwords: **1141**; unique IDs: **1141**; duplicate headwords: **0**.
- Pinned identity baseline: **1141 IDs**; additions: **0**; removals: **0**.
- ID-set SHA-256: `adccbdb4c98872207d2bede7bdc530e1c079bbd8b3679e7e4f6288054c7e404b` (matches the pinned baseline).

## Inherited Word Family data (not added by v2.95.68)

- Existing Batch 025 ledger (`release 2.95.67`) records **0 new headwords** and **6 reciprocal relation links** across three pairs. v2.95.68 adds **zero** vocabulary relations.
- The Batch 036 historical vocabulary assertion now restores those six links to their recorded `before: []` snapshots before reversing the earlier v2.95.54 operations; the existing ledger hash is reproduced. The canonical source data and ledger were not altered to force a match.

## Protected learning-bank hash comparison

| File | Bytes | SHA-256 |
|---|---:|---|
| `data/grammar/lessons.json` | 225,613 | `3e8169cc9e5bb29edc22c46e85732f350597ae73ebb2f7f5abfcfada4cfe7982` |
| `data/listening/listening-library.json` | 452,651 | `32fa347f500e3dbb241c183f48892572cbb529be6aa5a26c76d831bae7cf8111` |
| `data/practice/part5-sentence-completion.json` | 129,904 | `1af7f0e17522f4e5f341f1bd02a869b8b0bb3635552fa19147283f742be9ee8d` |
| `data/readings/reading-library.json` | 393,651 | `f7165c37af11e97333714b5b8c80ccd83332f5df22c7afef82555ba1f0372eba` |
- Composite SHA-256: `4c90ec8718784a8a73e8c357a279ceeabcc339a961fd78ca118f019a930141d9`.
- Existing Batch 036 ledger expected composite: `4c90ec8718784a8a73e8c357a279ceeabcc339a961fd78ca118f019a930141d9`.
- Result: **exact match**. The four protected banks (Grammar, Listening, Reading and Part 5 practice) are byte-identical to the historical protected snapshot. Regression suites additionally preserve question IDs, choice IDs and answer mapping.

## Scope note

- This report compares the uploaded v2.95.67 FullSource to the v2.95.68 candidate produced from it. It does not claim to reconstruct every content change made in releases before v2.95.67.
- Learner IndexedDB exists on each user device and is not stored in this source archive. No IndexedDB schema migration or learner-record rewrite was made in this batch.
