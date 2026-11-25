# Package Verification — TOEIC Dictionary v2.95.64

**Release:** `TOEIC_Dictionary_v2.95.64_FullSource.zip`
**Exact predecessor:** `TOEIC_Dictionary_v2.95.63_FullSource.zip`
**Predecessor SHA-256:** `6d43a7f44e1cc84d6ad7f3ee9dae660cceb83c792668d0966ce1060f4aa9ea80`
**Base commit in the local release-verification repository:** `7c1dab05334fbb0fff5ed40d8c329cd1131cb70e`

## FullSource verification

- Built using `python tools/package_source.py 2.95.64 ... --repo <clean-release-repository>` from the committed Git tree.
- The package contains **772 files** under exactly one root, `Toeic_Dictionary_v2.95.64/`.
- ZIP CRC/integrity check: PASS.
- Every packaged path and SHA-256 was compared with the final tracked Git tree: **772/772 identical**; no missing, extra or mismatched files.
- The FullSource SHA-256 is recorded in the detached `.zip.sha256` sidecar delivered beside the archive. The archive does not embed its own checksum.

## Patch verification

- Patch: `TOEIC_Dictionary_v2.95.64_Patch_From_v2.95.63.zip`.
- Created from the exact v2.95.63 baseline commit to the final v2.95.64 release commit; no other release, branch or source snapshot was used.
- Patch includes the source diff, base archive SHA-256 and a manifest identifying both versions.
- A new extraction of the exact v2.95.63 FullSource was initialized as a clean Git baseline. `git apply --check` and `git apply` both passed.
- Replayed tree compared byte-for-byte with the v2.95.64 FullSource: **772/772 identical**; missing=0, extra=0, changed=0.
- ZIP CRC/integrity check: PASS. Patch SHA-256 is recorded in its detached `.zip.sha256` sidecar.

## Commit-readiness verification

- 27 implementation/report files passed the staged pre-commit audit with 0 errors and 0 warnings; a final package-verification record was then added and the same staged audit rerun before the final local release commit.
- Final local release commit has a clean worktree; `audit-git-commit-readiness.py --require-clean` reports 772 indexed paths, 0 errors and 0 warnings.
- The local repository was created from the verified FullSource for deterministic commit/replay testing. This is **not** a push to the user's remote GitHub repository.
- Hosted GitHub Actions, actual remote commit/push, Windows/macOS client behavior, GitHub Pages deployment and installed-PWA device checks remain unverified.

## Output checksum handling

FullSource and Patch output hashes are supplied as detached checksum sidecars. They are deliberately not embedded in this document or the source archive, avoiding self-referential archive checksums.
