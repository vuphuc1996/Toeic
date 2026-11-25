# Command Log Index — TOEIC Dictionary v2.95.52

| Command / activity | Result | Evidence / note |
|---|---|---|
| `tools/update-related-terms.py --dry-run` Batch 041 | PASS | 11 exact-guarded updates; no mutation during dry run |
| `tools/update-related-terms.py --apply` Batch 041 | PASS | Atomic update; audit record created |
| `tools/build-related-glossary-enrichment-queue.py` | PASS | Deterministic, read-only queue generated |
| `tools/audit-related-glossary-quality.py` | PASS | 567 rows; 198 flagged |
| `tools/audit-related-glossary-candidates.py` | PASS | 556/804 coverage; 248 missing unique targets |
| `tools/sync-version.py --set 2.95.52 --apply` | PASS | Registered version markers updated |
| `tools/sync-version.py --check` | PASS | All 13 markers and changelog aligned |
| `tools/validate-data.py` | PASS | 1,141 records; 0 ID changes; 0 errors / 0 warnings |
| Related Glossary Python regression discovery | PASS | 131/131 cases |
| Dynamic Python sharded suite | PASS WITH SKIPS | 91/91 modules; 704 pass / 1 accepted skip |
| Local workflow shell replay | See CI replay report | Local replay only; not hosted Actions |
| FullSource / Patch build and exact replay | See package verification | Exact v2.95.51 base required |
