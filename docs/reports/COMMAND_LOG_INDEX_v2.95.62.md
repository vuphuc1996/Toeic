# Command Log Index — TOEIC Dictionary v2.95.62

All commands below were run from the exact v2.95.61-derived repository root. The v2.95.60 archive uploaded in this task was not used as a baseline or fallback.

## Source-of-truth verification and update

| Command / operation | Result |
|---|---|
| SHA-256 check of `TOEIC_Dictionary_v2.95.61_FullSource.zip` against its `.sha256` sidecar | PASS; `63bb04e7f9bbb15fa76ff00ab833b392bf6d48e71ecafd8740b05c2ff1cb56b7` |
| `unzip -tq TOEIC_Dictionary_v2.95.61_FullSource.zip` and single-root/inventory check | PASS; clean archive, exact root `Toeic_Dictionary_v2.95.61/` |
| `python tools/update-related-terms.py --root . --patch patches-related-terms/v2.95.62/related-terms-043.json --dry-run` | PASS; 21 guarded updates previewed; base glossary SHA matched |
| `python tools/update-related-terms.py --root . --patch patches-related-terms/v2.95.62/related-terms-043.json --apply` | PASS; 21 existing rows updated atomically; 0 additions / 0 deletions |
| `python tools/sync-version.py --set 2.95.62 --dry-run` | PASS; exact registered edits previewed |
| `python tools/sync-version.py --set 2.95.62 --apply` | PASS; 4 files updated (manifest, app.js, sw.js, index.html) |
| `python tools/sync-version.py --check` | PASS; 13/13 markers |

## Quality reports and validators

| Command | Result |
|---|---|
| `python tools/audit-related-glossary-quality.py --output docs/reports/RELATED_GLOSSARY_QUALITY_v2.95.62.md --json-output docs/reports/RELATED_GLOSSARY_QUALITY_v2.95.62.json` | PASS; 157 flagged of 567 |
| `python tools/build-related-glossary-enrichment-queue.py --output docs/reports/RELATED_GLOSSARY_ENRICHMENT_QUEUE_v2.95.62.md --json-output docs/reports/RELATED_GLOSSARY_ENRICHMENT_QUEUE_v2.95.62.json` | PASS; deterministic read-only queue |
| `python tools/validate-data.py --root . --json /tmp/validate-data-62.json` | PASS; 1,141 records, no IDs added/removed, 0 errors / 0 warnings |
| `python tools/validate-learning-content.py` | PASS; 0 errors / 0 warnings |
| `python tools/audit-toeic-coverage.py` | PASS; generated v2.95.62 coverage report |
| `python tools/audit-question-evidence.py` | PASS; generated v2.95.62 question-evidence report |
| `python tools/audit-distractors.py` | PASS; generated v2.95.62 distractor report |
| `python tools/audit-repository-integrity.py` | PASS; 442 references/data files, no errors/warnings |

## Focused Python regressions

Each module ran using `python -m unittest discover -s tools/tests -p '<module>' -v`. Final result: **160/160 PASS across 24 modules**. Exact per-module case counts are in `TEST_REPORT_TOEIC_Dictionary_v2.95.62.md`.

Covered current batch 043, historical glossary batches 025 and 029–042, guarded update tool, quality/backlog/candidate audits, relationship graph, repository integrity, test fingerprints, shard runner, release acceptance, package source and CI coverage.

## Node and syntax checks

| Command | Result |
|---|---|
| `for f in tools/tests/*.mjs; do node "$f"; done` | PASS; 42/42 scripts |
| `for f in sw.js assets/js/*.js; do node --check "$f"; done` | PASS; 21/21 files |
| `python -m py_compile` for new/modified regression/helper modules | PASS |

## Test-suite inventory boundary

- `python tools/run-python-tests-sharded.py --list`: 96 Python modules discovered; the historical 88-module inventory baseline reports 8 additions (from multiple recent releases).
- Full 96-module test execution: NOT RUN. Focused test result is not presented as a full-suite result. A separate `test_validator.py` attempt exceeded the 180-second limit after 23 `ok` results while test 24 was still executing; no aggregate summary was captured and this attempt is not counted as a pass.
- GitHub Actions workflow coverage: local `test_ci_coverage.py` PASS; remote hosted workflow NOT VERIFIED.

## Package and Patch

- Package command: `python tools/package_source.py 2.95.62 /mnt/data/TOEIC_Dictionary_v2.95.62_FullSource.zip --repo <committed-v2.95.62-root>`; output and final archive verification are recorded in `PACKAGE_VERIFICATION_v2.95.62.md`.
- Patch is generated from `git diff --binary <v2.95.61-baseline-commit> <v2.95.62-final-commit>` and is bound to the exact predecessor FullSource SHA-256.
- Replay procedure: clean extraction of the exact v2.95.61 FullSource, `git apply --check patch.diff`, `git apply patch.diff`, then complete tree hash comparison with the v2.95.62 FullSource. Final results are recorded in package verification.
