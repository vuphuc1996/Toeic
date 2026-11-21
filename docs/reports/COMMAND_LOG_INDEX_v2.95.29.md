# Command Log Index — v2.95.29

- Baseline: `TOEIC_Dictionary_v2.95.28_FullSource.zip`.
- `python tools/enrich-related-glossary-from-canonical.py --apply` — applied 89 exact canonical bilingual entries.
- `python tools/enrich-related-glossary-from-canonical.py` — audit-only after apply: 0 remaining candidates.
- `python -m unittest ...` — 32 focused related-glossary/graph tests PASS.
- `node --test tools/tests/*.mjs` — 39/39 PASS.
- `python tools/validate-data.py` — PASS, 1,141 records, 0 errors / 0 warnings.
- `python tools/validate-learning-content.py` — PASS, 0 errors / 0 warnings.
- `python tools/audit-repository-integrity.py` — PASS, 403 files, 0 errors / 0 optional warnings.
- `python tools/sync-version.py --check` — PASS.
- FullSource ZIP: 485 files, one root; Update Patch: 25 changed/added files, no deletions; ZIP CRC PASS.
- Patch replay against v2.95.28: 485/485 byte-exact PASS. SHA-256 recorded in `TOEIC_Dictionary_v2.95.29_SHA256SUMS.txt`.
- Remote CI, Pages deployment and real-device QA are not verified.
