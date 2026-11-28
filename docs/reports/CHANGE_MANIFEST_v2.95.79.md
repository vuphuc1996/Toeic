# Change Manifest — TOEIC Dictionary v2.95.79

**Predecessor:** exact candidate HEAD `9a174778bcdfea7adca98f0abb1b17d3a050388e` (v2.95.78).
**Target:** v2.95.79 — Package Metadata Synchronization & Version Guard Hardening.
**Target branch:** `candidate`; `main` is not modified.

## Source changes

- `tools/sync-version.py`: add `package.json` top-level version as an exact-one release marker. Preserve preflight validation and the existing fail-closed behavior.
- `tools/tests/test_sync_version.py`: create a package fixture and test version mismatch detection, dry-run immutability, successful apply, and missing/duplicate marker rejection before any write.
- `data/manifest.json`, `package.json`, `assets/js/app.js`, `sw.js`, `assets/js/mock-engine.js`, and `index.html`: synchronize source release and cache keys to v2.95.79.
- `docs/README.md`, `docs/versions/CURRENT_VERSION.md`, `docs/MASTER_STATUS.md`, `docs/CHANGELOG.md`: set the active release ledger to v2.95.79; retain v2.95.78 history.
- Add release-scoped test report, command log and change manifest for v2.95.79.

## Verification strategy

The synchronizer must identify exactly one top-level package version marker. A version mismatch is a normal drift state (exit 1 on `--check`); a missing or duplicate marker is a structure error (exit 2) and must not write any file. `--dry-run` must remain read-only, and `--apply` must update only registered markers before the post-apply check.

**Exact source commit accepted:** `76ca52457929493a2a587f7673367bc29eeace49`. GitHub Validate [run 46105814708](https://github.com/vuphuc1996/Toeic/actions/runs/46105814708) PASS (151/151 steps, 848 Python tests); GitHub Pages [run 46105814298](https://github.com/vuphuc1996/Toeic/actions/runs/46105814298) PASS on the same exact SHA. Predecessor evidence is not substituted.

## Protected boundaries

No canonical vocabulary record or ID, sense/relationship, learning content, stable question/choice ID, answer key, Mock eligibility, editorial reserve, learner IndexedDB schema/data, user interface, navigation or Robot Buddy logic is intentionally changed. Hosting settings and workflows are not changed.
