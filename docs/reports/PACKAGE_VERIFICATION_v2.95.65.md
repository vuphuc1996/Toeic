# Package Verification — TOEIC Dictionary v2.95.65

## Source relationship

- Exact predecessor: `TOEIC_Dictionary_v2.95.64_FullSource.zip`
- Predecessor SHA-256: `03ec4c80e88bc76e435cfc0782e933474be882a4f271318a23375a35e9242673`
- The predecessor ZIP passed CRC and SHA-256 verification before extraction. No older FullSource, Patch, alternate branch or stale extraction was used as a development source.

## FullSource verification — PASS

- Output: `TOEIC_Dictionary_v2.95.65_FullSource.zip`
- Inventory: **779 files**, one root folder (`Toeic_Dictionary_v2.95.65/`).
- Built by `tools/package_source.py` from the final clean Git commit, not from an uncommitted working directory.
- ZIP CRC: PASS.
- Every packaged path and file byte matches the final committed Git archive after the package exclusion rules are applied.
- No ignored logs, caches, temporary files or ZIP artifacts are included.
- Archive SHA-256 is recorded in the detached `.zip.sha256` sidecar (not embedded in the archive itself).

## Patch verification — PASS

- Output: `TOEIC_Dictionary_v2.95.65_Patch_From_v2.95.64.zip`
- Generated from the binary Git diff between the exact v2.95.64 baseline snapshot and final v2.95.65 release commit.
- Change inventory: 18 modified, 7 added, 0 deleted (25 paths total).
- Patch archive contains exactly four members: `PATCH_README.md`, `PATCH_MANIFEST.json`, `BASE_SHA256.txt`, and `patch.diff`.
- Replayed against a fresh extraction of the exact v2.95.64 FullSource. `git apply --check` and `git apply` both passed.
- Final replay comparison: **779/779 files byte-identical**, 0 missing, 0 extra and 0 changed files.
- Patch ZIP CRC: PASS; detached SHA-256 sidecar: PASS.

## Commit readiness — PASS

- Baseline commit preserves the exact raw bytes from the verified FullSource. Historical trailing whitespace in untouched baseline files was not mass-edited.
- Staged diff passed `git diff --cached --check` and `python tools/audit-git-commit-readiness.py --staged`: 779 indexed paths inspected, 0 errors and 0 warnings.
- Local release commit was created successfully. Post-commit `python tools/audit-git-commit-readiness.py --require-clean` passed with 779 indexed paths, 0 errors and 0 warnings; worktree is clean.
- Release artifacts are outside the repository and are not included in the commit.

## External boundary

Local Git commit simulation and archive replay do not publish to the user's GitHub repository. Hosted Actions, GitHub Pages deployment, browser cache/offline propagation and physical-device acceptance remain unverified until the repository owner commits/pushes the source and deployment/device checks complete.
