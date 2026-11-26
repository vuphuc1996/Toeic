# Data Difference Report — v2.95.69 → v2.95.70

The comparison uses the verified `TOEIC_Dictionary_v2.95.69_FullSource.zip` as the sole predecessor and an independent clean extraction. It does not compare against an earlier release or a Patch.

## `data/` directory

- Baseline files: 68
- Candidate files: 68
- Added: 0
- Removed: 0
- Byte-different paths: only `data/manifest.json`
- `manifest.json`: `version` changes from `2.95.69` to `2.95.70`. After normalizing only this field, the parsed JSON objects are identical.

All other 67 data files are byte-identical. Therefore this batch introduces no vocabulary or learning-content data edits.

## Protected data boundaries

- Canonical vocabulary inventory: 1,141 records; validator reports ID additions 0 and removals 0.
- Vocabulary IDs, headwords, meanings, IPA, word-family, verb forms, collocations, synonym/antonym relations: unchanged.
- Listening, Reading, Grammar and practice question banks: unchanged byte-for-byte.
- Question IDs, choice IDs, correct-answer keys and Mock eligibility: unchanged.
- Learner IndexedDB schema and records: no migration code or schema changes were introduced. Physical learner-device databases were not directly inspected.

## Runtime/source changes are separate

The v2.95.70 work changes assessment-result behavior, Foundation persistence ordering, tests, CI registration and documentation. Those are not edits to the `data/` records.
