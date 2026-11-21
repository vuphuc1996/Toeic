# Change Manifest — v2.95.26


## Added/updated
- `tools/audit-related-glossary-quality.py`: missing Vietnamese gloss flag; malformed-row safe audit; normalized duplicate-term detection; Markdown + JSON output.
- `tools/tests/test_related_glossary_quality_audit.py`: expanded to six tests covering normal rows, missing fields, short/echo definitions, determinism, duplicate normalization and malformed input.
- CI compile/test registration for quality-audit tool and its test module.
- Generated Markdown and JSON quality audit reports.
- Release verification report records 6/6 focused Python tests, 39 JavaScript suites, validators and patch replay checks.
- Release documentation and version markers synchronized to 2.95.26.

## Not changed
- No canonical vocabulary headwords or vocabulary meanings.
- No glossary data entries or relation arrays.
- No learning questions, answer keys, profile storage or progress records.
- No UI/layout or PWA runtime behavior except version/cache markers required by release sync.
