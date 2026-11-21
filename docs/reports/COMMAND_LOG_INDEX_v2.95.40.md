# Command Log Index — TOEIC Dictionary v2.95.40

## Reproduction and focused fix

```bash
python -m unittest discover -s tools/tests -p 'test_major_release_quality_audit_025.py' -v
python tools/update-related-terms.py --patch patches-related-terms/v2.95.40/related-terms-034.json --dry-run
python tools/update-related-terms.py --patch patches-related-terms/v2.95.40/related-terms-034.json --apply
python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_030.py' -v
python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_034.py' -v
```

## Data and release gates

```bash
python -m compileall -q tools
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/validate-part1-photo-assets.py
python tools/sync-version.py --check
python tools/sync-design-profile.py --check
python tools/audit-repository-integrity.py
python tools/audit-major-release.py
python tools/audit-related-glossary-candidates.py --output docs/reports/RELATED_GLOSSARY_CANDIDATE_AUDIT_CURRENT.md
python tools/build-related-glossary-backlog.py
python tools/audit-related-glossary-quality.py --output docs/reports/RELATED_GLOSSARY_QUALITY_FLAGS_v2.95.40.md --json-output docs/reports/RELATED_GLOSSARY_QUALITY_FLAGS_v2.95.40.json
python tools/audit-toeic-coverage.py
python tools/audit-listening-readiness.py
python tools/audit-objective-resources.py
python tools/audit-learning-outcomes.py
python tools/audit-question-evidence.py
python tools/audit-distractors.py
python tools/audit-foundation-a2-assessment.py
```

## JavaScript

```bash
for file in sw.js assets/js/*.js; do node --check "$file"; done
for file in tools/tests/*.mjs; do node "$file"; done
```

## Execution boundaries

- Python focused regression: 137/137 across 23 named modules, as listed in `TEST_REPORT_TOEIC_Dictionary_v2.95.40.md`.
- JavaScript: 39/39 `.mjs` suites.
- Full aggregate Python discovery and the entire `test_validator.py` module are not claimed; the validator module attempt exceeded the execution time limit.
- Remote CI and live deployment were not run.

## Full Source package verification

- `tools/package_source.py 2.95.40`: **587 source/data/docs files**.
- CRC check: PASS; one root folder `Toeic_Dictionary_v2.95.40/`; exclusion policy PASS.
- Exact comparison to the release working tree after clean packaging: **587/587 byte-identical**.
- SHA-256 sidecar: `TOEIC_Dictionary_v2.95.40_FullSource.zip.sha256` — verified against the final archive.
- Full Python discovery and full `test_validator.py` remain unclaimed due to the execution time limit; remote CI and deployment were not run.
