# Test report — TOEIC Dictionary v2.95.31

- Safe missing-IPA pipeline tests: 8/8 PASS.
- CMUdict backfill regression: 6/6 PASS (includes converter-onset correction; cumulative ledger 334).
- CMUdict ledger check: PASS, 334 source-linked entries.
- Version sync check: PASS.
- Vocabulary validation: 1,141 records; 0 errors, 0 warnings (legacy). IPA coverage 1,062; 79 missing.
- Learning content validation: 0 errors, 0 warnings. Listening 121 units/239 questions; Reading 65/263; Grammar 50/137.
- Repository integrity: 405 files/references inspected; 0 errors, 0 optional warnings.

Not run: all JavaScript suites in this batch, full Python discovery, remote CI, GitHub Pages deployment, mobile/browser acceptance.
- JavaScript regression suites: 39/39 PASS.
- Focused Python tests: 14/14 PASS across the safe backfill and CMUdict converter modules.
- Full Python discovery attempted but exceeded this session's time limit; one selected test file (`test_validator.py`) did not finish within the batch. Standalone validation scripts above did complete successfully.
- FullSource package: 501 files; ZIP CRC/root/exclusion checks PASS.
- Update Patch: 22 changed/added files, 0 deleted. Replay against v2.95.30 baseline yielded 501/501 byte-exact files.
- SHA-256 checksum file generated and verified.
