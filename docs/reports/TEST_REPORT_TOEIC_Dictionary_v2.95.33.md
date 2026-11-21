# Test Report — TOEIC Dictionary v2.95.33

## Scope
- Added priority tiers to the read-only Related Glossary quality audit.
- Regenerated priority-sorted Markdown and structured JSON reports.
- Glossary data itself was not modified.

## Results
- Related Glossary quality audit: 11/11 PASS.
- Related Glossary candidate audit + backlog tests: 7/7 PASS.
- Combined focused glossary tests: 18/18 PASS. Package-source tests: 3/3 PASS. Total focused Python tests: 21/21 PASS.
- JavaScript test files: 39/39 PASS (each `.mjs` executed separately).
- Vocabulary validation: 1,141 records; 0 errors / 0 warnings.
- Learning-content validation: 0 errors / 0 warnings.
- Repository-integrity preflight: 405 files; 0 errors / 0 optional warnings.
- Version sync: PASS.

## Current glossary quality snapshot
- Entries scanned: 519; flagged: 305.
- Review priority: 302 High / 2 Medium / 1 Low (mutually exclusive buckets).
- Issue counts overlap: missing English definition 229; missing POS 302; missing source provenance 75; placeholder English definition 73; short definition review 1.
- Duplicate normalized term groups: 0.

## Incomplete checks
- Full Python unittest discovery was attempted but timed out; one failure marker appeared before timeout, and its traceback was not captured. The full suite is NOT reported as passing. The focused suites and validators above completed.
- Remote GitHub Actions, Pages deployment, and real-device/browser acceptance were not run.
