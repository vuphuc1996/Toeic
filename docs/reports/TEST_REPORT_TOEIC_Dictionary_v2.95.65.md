# Test Report — TOEIC Dictionary v2.95.65

## Baseline

- Exact predecessor: v2.95.64 FullSource.
- SHA-256: `03ec4c80e88bc76e435cfc0782e933474be882a4f271318a23375a35e9242673`.
- ZIP CRC: PASS.

## Verified in this run

| Test/validation | Result |
|---|---:|
| Batch 035 wildcard discovery (both test modules) | 10/10 PASS |
| Single shared overlay contract | 2/2 PASS |
| CI coverage contract | 8/8 PASS |
| Repository integrity tests | 2/2 PASS |
| Git commit-readiness integration | 10/10 PASS |
| Design system | 19/19 PASS |
| Practice mode fallback | 6/6 PASS |
| Version synchronization unit tests | 12/12 PASS |
| Release acceptance runner tests | 10/10 PASS |
| Test fingerprint tests | 10/10 PASS |
| Source package tests | 3/3 PASS |
| Python test shard runner tests | 19/19 PASS |
| Node regression scripts (`tools/tests/*.mjs`) | 43/43 PASS |
| Python compileall (`tools/`) | PASS |
| Repository integrity preflight | 363 local references/data files; 0 errors, 0 optional warnings |
| Data validator | 1,141 records; 0 errors, 0 warnings; 0 IDs added/removed |
| Learning-content validator | 0 errors, 0 warnings |
| Part 1 photo validation | 9/9 PASS |
| Version sync check (pre-bump baseline) | PASS; all 13 markers aligned |
| Design-token audit | 0 new violations; 2,773 historical findings remain as warnings |
| GitHub Actions YAML | 125 unique steps; YAML parse PASS |

Python tests total **111/111 across 13 modules** (the Batch 035 wildcard covers two modules). Counts are from the exact workflow-style discovery invocations. The initial attempt to import `test_sync_version` as a package failed because that module intentionally imports `helpers` from the `tools/tests` discovery path; it was rerun using the exact `unittest discover -s tools/tests -p ...` invocation and passed 12/12. The failed package-import invocation is not counted as a test failure or pass.

## Full suite / external acceptance

- Full 97-module Python unittest discovery has not been executed to completion in this run. Do not interpret the focused tests as the full suite.
- GitHub-hosted Actions is not executed by this local environment.
- GitHub Pages deployment, service-worker cache propagation, offline behavior on an installed PWA, and actual Windows/macOS/iOS/iPadOS/Android device behavior remain unverified.

## Data preservation

No vocabulary/Related Glossary content, canonical word IDs/headwords/relations, question IDs, choice IDs/order, answer keys, Mock eligibility, learner IndexedDB records/schema or Robot Buddy access boundary changed. Only the version marker under `data/manifest.json` is expected to change during the final version synchronization.
