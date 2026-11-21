# Test Report — TOEIC Dictionary v2.95.30


## New work
- Added non-mutating CMUdict missing-US-IPA review queue builder.
- Added 8 unit tests for exact matching, alternate pronunciation preservation, no-match handling, empty entries, deduplication, sorting, and blank IPA detection.
- Generated queue for 80 canonical records missing US IPA: 6 single-pronunciation candidates, 49 multiple-pronunciation review, 25 no exact CMUdict entry.

## Checks
- New unit tests: 8/8 PASS.
- Python compile: PASS.
- CMUdict review queue generation: PASS (80 records).
- No IPA or other canonical data automatically applied.
- Full source package: 494 files. Update patch: 20 changed files, 0 deletions. Patch replay matches full source byte-for-byte (494/494). ZIP CRC and SHA-256 verification PASS.
- JavaScript regression: 39/39 PASS.
- Data validation: 1,141 records, 0 errors / 0 warnings.
- Learning-content validation: 0 errors / 0 warnings.
- Repository integrity: 403 references/files, 0 errors / 0 optional warnings.
- Version sync: PASS.
- Full Python discovery was attempted but exceeded the session timeout while running a repository-dependent patch rollback test; one observed test fails in the extracted non-Git source because `git check-ignore` requires Git metadata. Remaining discovery results are incomplete and are not claimed PASS.
- Remote CI, Pages deployment and device QA: not performed.
