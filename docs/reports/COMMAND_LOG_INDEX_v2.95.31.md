# Command log — v2.95.31

1. `python tools/backfill_missing_ipa_from_cmudict.py` — preview; 80 examined, 1 safe, 5 unique conversion failures, 49 multi-variant, 25 missing exact entries.
2. `python tools/backfill_missing_ipa_from_cmudict.py --apply` — 1 record applied; cumulative ledger 334.
3. `python tools/cmudict_ipa.py --check` — PASS.
4. `python -m unittest tools.tests.test_missing_ipa_safe_backfill tools.tests.test_cmudict_ipa_backfill -v` — 14/14 PASS.
5. `python tools/sync-version.py --check` — PASS.
6. `python tools/validate-data.py` — PASS, 1,141 records.
7. `python tools/validate-learning-content.py` — PASS, 0 errors/warnings.
8. `python tools/audit-repository-integrity.py` — PASS, 405 checks.

Full JavaScript test suite, full Python discovery, external CI, Pages deploy and device acceptance not run.
9. `node tools/tests/*.mjs` (39 individual suites executed sequentially) — 39/39 PASS.
10. Focused additional Python module loop started; full validator unittest module exceeded the execution time limit. Standalone validation commands had already passed. This timeout is not reported as PASS.
11. FullSource/Update Patch package checks — PASS (501 source files; 22 patch files; patch replay 501/501 byte-exact).
12. SHA-256 verification — PASS.
