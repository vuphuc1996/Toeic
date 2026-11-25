# Package Verification — v2.95.57

- Exact baseline: `TOEIC_Dictionary_v2.95.56_FullSource.zip` (SHA-256 `8ec7435b810b8ebaae4dbe608491d5212c1f52ba5b3cde407e87ab0473dfdb7a`).
- FullSource: 684 source/data/docs files under exactly one root, `Toeic_Dictionary_v2.95.57/`.
- Patch: binary-safe Git diff from the exact v2.95.56 source baseline; clean `git apply --check` and `git apply` completed successfully.
- Clean replay verification: **684/684 files byte-identical**, 0 missing, 0 extra source files, 0 byte-different files (Git metadata excluded from comparison).
- FullSource ZIP and Patch ZIP integrity checks: PASS; SHA-256 sidecars are supplied beside the archives.
- Protected Listening/Reading question libraries and sampled vocabulary files were compared to v2.95.56 and are byte-identical.
- No canonical question content, answer keys, choices, IDs, reserve status, learner database/schema or UI changes are present.
