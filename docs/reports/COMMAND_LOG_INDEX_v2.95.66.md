# Command Log Index — TOEIC Dictionary v2.95.66 candidate

## Baseline

- Source: TOEIC_Dictionary_v2.95.65_FullSource.zip
- SHA-256: a1b95e807e08052bfa599a08ff88bc3237ae086688557ce3ae77b78e814814fb
- File inventory: 779
- Candidate base commit: bfb28d63669508dc8fd766802c1203f6a2e86087

## Required verification sequence

| Order | Area | Exact command / evidence | Current status |
|---:|---|---|---|
| 1 | Python syntax | python -m compileall -q tools | PENDING hosted Actions |
| 2 | Batch 022 | python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_022.py' -v | PASS — Actions run 45589650195 |
| 3 | PWA readiness | python -m unittest discover -s tools/tests -p 'test_pwa_readiness.py' -v | PASS |
| 4 | CI coverage | python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v | PASS |
| 5 | Release asset coherence | node tools/tests/release-asset-coherence.mjs | PASS |
| 6 | Service Worker lifecycle | node tools/tests/service-worker-update.mjs | PASS |
| 7 | Full JavaScript regression group | 44 Node regression scripts in the JavaScript syntax check step | PASS — 44/44 |
| 8 | Full Python discovery | python -m unittest discover -s tools/tests -v | PASS — 762/762 in 13.230s |
| 9 | Data / learning validators | python tools/validate-data.py and python tools/validate-learning-content.py | PASS — 1,141 IDs unchanged; 0 errors / 0 new warnings |
| 10 | Version synchronization | python tools/sync-version.py --check | PASS — all registered markers aligned |
| 11 | Source package | python tools/package_source.py 2.95.66 <output.zip> | PENDING — build from exact candidate commit |
| 12 | Patch replay | git apply --check, git apply, then file-by-file tree comparison against the exact v2.95.65 baseline | PENDING |
| 13 | Post-commit audit | python tools/audit-git-commit-readiness.py --require-clean | PENDING |
| 14 | Browser / installed PWA | Manual Acceptance Checklist rows 13–15 | PENDING real-device test |

Do not promote a pending command to PASS until its exact run completes and evidence is inspected. A workflow step skipped after an earlier failure is not a pass.


## Hosted Actions evidence

- Run: `45589650195` (candidate head `9fdfc39`)
- Workflow conclusion: **success**; 130/130 steps succeeded, 0 failed, 0 skipped.
- Full Python unittest discovery: 762 tests, all passed, 13.230 seconds.
- Node regression scripts: 44/44 passed. JavaScript syntax checks passed.
- Remaining tasks: build FullSource/Patch from the accepted commit; detached SHA-256, ZIP CRC, exact patch replay, Pages deployment and physical-device/PWA cache acceptance.
