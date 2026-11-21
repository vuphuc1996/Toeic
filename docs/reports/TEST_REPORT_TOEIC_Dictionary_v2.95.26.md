# Test Report — TOEIC Dictionary v2.95.26


## Scope

- Version advanced from v2.95.25 to v2.95.26.
- Hardened the read-only glossary audit: missing Vietnamese gloss, malformed rows, normalized duplicate detection, and structured JSON report output.
- Audit indices are stable per current input order; no merging or automatic corrections.
- No vocabulary/glossary runtime records, question content, answer keys, relations, IndexedDB, PWA runtime, or UI were intentionally changed beyond release version markers.

## Verification

- Glossary quality audit unit tests: **6/6 PASS**.
- Python compile check for audit tool and tests: **PASS**.
- Version sync check: **PASS**, all markers 2.95.26.
- Generated Markdown audit and JSON audit: **PASS** (both generated).

## Limits

- Full Python discovery was not run for this version.
- Remote GitHub Actions, Pages deployment, browser/device acceptance, mobile/desktop, offline and TTS are not verified.
- This release is a quality-tooling and documentation change, not a vocabulary-content release.

## Executed release checks
- Quality audit unit tests: **6/6 PASS**.
- JavaScript module test suites: **39/39 PASS**.
- `tools/sync-version.py --check`: **PASS**, all version markers 2.95.26.
- Vocabulary validation: **1,141 records; 0 errors, 0 warnings**; baseline ID/hash check PASS. Informational quality gaps remain (80 missing IPA, 296 synonym/antonym entries without meanings, etc.).
- Learning content validation: **0 errors / 0 warnings** (Listening 121 units/239 questions; Reading 65/263; Grammar 50/137).
- Repository integrity: **399 references/files inspected; 0 errors / 0 optional warnings**.
- ZIP integrity/root checks: FullSource and Patch **PASS**.
- Patch replay against v2.95.25 baseline: **PASS**, all 465 packaged source files byte-identical to FullSource after patch application.
- Full Python test discovery, remote CI, deployment and device/browser acceptance are not claimed.
