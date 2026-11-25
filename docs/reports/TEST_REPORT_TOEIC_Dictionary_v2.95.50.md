# Test Report — TOEIC Dictionary v2.95.50

## Focused regression results

| Module / check | Result |
|---|---:|
| Related Glossary batch 039 | 4/4 PASS |
| Related Glossary quality audit | 11/11 PASS |
| Related Glossary candidate audit | 4/4 PASS |
| Batch 038 historical reconstruction | 8/8 PASS |
| Canonical glossary backfill history | 6/6 PASS |
| Batch 034 historical reconstruction | 6/6 PASS |
| Batch 035 historical reconstruction | 5/5 PASS |
| Batch 036 historical reconstruction | 6/6 PASS |
| Batch 037 historical reconstruction | 7/7 PASS |
| Version sync check | PASS |
| Data validator | PASS — 1,141 records, 0 ID changes, 0 ERROR, 0 WARNING |
| Objective audit | PASS — 11 objectives / 33 criteria; 6 evidence paths |
| Resource audit | PASS — 379/379 linked |

## Full suite status

The 90-module dynamic Python suite was started with the sharded runner, but repeated outer execution timeouts interrupted the run before all modules reached terminal states. The earlier run exposed five historical-test expectation failures caused by batch 039 changing the live glossary; those tests were corrected to reverse batch 039 during historical reconstruction, and each affected module was rerun directly and passed. **The complete v2.95.50 suite remains INCOMPLETE; no full-suite PASS is claimed.**

The single known environment-dependent skip in `test_patch_data.py` remains: Git metadata is absent in a source archive, so the `.gitignore` assertion requires a clone. It is distinct from a passed test.

## Production verification

Hosted GitHub Actions, GitHub Pages deployment, PWA cache propagation, offline use and physical iOS/Android/tablet/desktop acceptance remain unverified.
