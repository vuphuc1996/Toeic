# Package Verification — TOEIC Dictionary v2.95.62

## Canonical source and exact predecessor

- Development baseline: `TOEIC_Dictionary_v2.95.61_FullSource.zip`.
- Verified predecessor SHA-256: `63bb04e7f9bbb15fa76ff00ab833b392bf6d48e71ecafd8740b05c2ff1cb56b7`.
- Predecessor archive passed ZIP CRC validation, matched its adjacent SHA-256 sidecar and contained the single root `Toeic_Dictionary_v2.95.61/` with 737 source files.
- The Git baseline commit was created only from that clean extracted archive: `28cefdf245343df15e4c712e151fc9858a108cdf`.
- The separately uploaded `v2.95.60_FullSource.zip` was not used as a source, fallback or patch base.

## Target FullSource

- FullSource: `TOEIC_Dictionary_v2.95.62_FullSource.zip`.
- Target root: `Toeic_Dictionary_v2.95.62/`.
- Expected final archive inventory: **753 files**, including this package-verification report.
- The project packager `tools/package_source.py` exports committed Git files only and enforces one versioned root plus the repository exclusion policy.
- Final ZIP CRC and SHA-256 sidecar are checked after final packaging. The SHA-256 sidecar is the source of truth for the actual archive checksum; it is not duplicated inside this report to avoid a self-referential checksum.

## Patch and exact replay

- Patch: `TOEIC_Dictionary_v2.95.62_Patch_From_v2.95.61.zip`.
- Bound to the exact predecessor archive SHA-256 above and baseline commit `28cefdf245343df15e4c712e151fc9858a108cdf`.
- Expected patch path inventory: **16 added / 20 modified / 0 deleted**; the added file includes this package verification report.
- Patch archive contains `PATCH_README.md`, `PATCH_MANIFEST.json`, `BASE_SHA256.txt` and `patch.diff`.
- Final replay procedure: extract the exact v2.95.61 FullSource into a clean directory; initialize a temporary Git index from that extraction; run `git apply --check patch.diff`, then `git apply patch.diff`; compare every eligible replay file SHA-256 with the final v2.95.62 FullSource tree.
- Acceptance requires exact file inventory and byte equality (**753/753**), with zero missing, extra or mismatched files. The final package command output and checksum sidecars are retained next to the release artifacts.

## Protected content and compatibility

- The only changed files below `data/` are `data/manifest.json` (version marker) and `data/related-terms.json` (21 guarded metadata updates). No `data/vocabulary/*.json`, Reading/Listening/Grammar/Part 5 bank, vocabulary ID/headword/sense/relation, question ID, choice ID/order or answer key changed.
- The Related Glossary remains 567 rows; exactly 21 existing entries were updated and 0 added/deleted. `term`, `meaning_vi` and synonym/antonym arrays are preserved.
- No learner IndexedDB data/schema, progress record, Robot Buddy data boundary, CSS/layout/navigation, API, Cloudflare service or backend changed. Version markers alone advance in the app shell/service worker/index.

## Verification boundary

- Focused Python: 160/160 PASS across 24 modules; the separate `test_validator.py` attempt timed out after 23 reported passes and is not counted. Full Python discovery across 96 modules was NOT RUN.
- Node regression: 42/42 PASS; JavaScript syntax: 21/21 PASS.
- Data and learning-content validators, repository-integrity audit, CI coverage test and 13/13 version-marker check: PASS.
- Hosted GitHub Actions, GitHub Pages deployment, PWA cache/offline propagation and physical-device acceptance remain UNVERIFIED.
- Independent editorial review of the 21 Cambridge Dictionary paraphrases remains PENDING.

A valid FullSource/ Patch replay proves archive consistency with this predecessor; it does not prove a remote deployment or physical-device acceptance.
