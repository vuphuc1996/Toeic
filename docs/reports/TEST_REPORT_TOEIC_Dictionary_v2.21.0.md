# Test Report — TOEIC Dictionary v2.21.0

- Date: 11/11/2026
- Base: v2.20.0
- Scope: Batch 011 — cleanup of eight legacy collocation warnings across seven vocabulary records.
- Release state: local release candidate; remote GitHub Actions / Pages deployment not verified.

## Change summary

- Replaced 7 collocation arrays using a guarded patch, resolving 8 known FD001 legacy violations.
- Tightened `tools/quality-baseline.json` by removing exactly those 8 resolved entries; no new debt was added.
- Preserved 928 stable vocabulary IDs and the ID-set SHA-256.
- No IndexedDB database/store/schema migration; no personal profile import/export, inspection or reset.

## Validation results

| Gate | Result |
|---|---|
| Patch dry-run | PASS |
| Patch apply | PASS — 7 operations / 6 files |
| Vocabulary validator before tightening | PASS — 0 ERROR; 8 resolved FD001 |
| Baseline tightening | PASS — removed 8 resolved entries, added 0 |
| Final vocabulary validator | PASS — 0 ERROR / 0 WARNING (legacy) |
| New collocation regression tests | PASS — 3/3 |
| Learning validator | PASS — 0 errors / 0 warnings |
| Version sync | PASS — all 7 markers synchronized |
| Targeted unit groups | PASS — 54/54 methods: baseline IDs 13/13; patch data 11/11; version sync 12/12; choice history 5/5; vocabulary detail/examples 10/10; new collocation cleanup 3/3. The complete validator unit module stalled in grouped sandbox execution; no full-suite total is claimed. |
| ZIP CRC / clean extraction comparison | PASS — 212 files; ZIP CRC PASS; clean extraction 212/212 byte-identical; validators and version sync rerun from extracted package PASS |

## Release archive

- Archive: `TOEIC_Dictionary_v2.21.0_Legacy_Collocation_Cleanup.zip`
- Files: 212. ZIP CRC: PASS. Clean extraction byte comparison: 212/212 PASS.
- SHA-256 được ghi trong sidecar bên ngoài archive: `TOEIC_Dictionary_v2.21.0_Legacy_Collocation_Cleanup.zip.sha256`.
- Vocabulary validator, learning-content validator and version-sync check were rerun against the extracted archive and all passed.

## Remote / physical QA boundary

The user supplied GitHub Actions run `42981524564` / job `130392820806` with a generic `Process completed with exit code 1` annotation. The exact remote failed command, commit SHA and workflow revision are not available yet. The local V2.20 workflow mapping shows step 14 is `choice_history`, which passes locally 5/5; the V2.21 local `validate-data.py` passes 0 errors / 0 warnings; this does not prove the remote checkout is identical. See `docs/reports/GITHUB_ACTIONS_CI_INVESTIGATION_2026-11-11.md`. GitHub connector is not yet connected, so the remote failed command remains unverified.

No browser/physical-device QA, commit/push, remote Actions pass or Pages deploy is claimed.
