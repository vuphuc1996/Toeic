# Test Report — TOEIC Dictionary v2.95.27

## Scope
- Baseline: v2.95.26 FullSource.
- Duplicate term screening now uses Unicode NFKC normalization, collapsed whitespace, and casefolding to identify compatibility-equivalent term spellings.
- Audit handles invalid non-list input containers with an explicit `terms-not-list` marker instead of failing; empty lists are valid.
- Read-only only: no runtime vocabulary/glossary entries, relationship arrays, learning content, learner data, storage, UI or runtime logic were changed.

## Verification
- Related glossary quality audit tests: **9/9 PASS**.
- Python syntax compile for audit and test: **PASS**.
- JavaScript module suites: **39/39 PASS**.
- `tools/sync-version.py --check`: **PASS**, all markers v2.95.27.
- Vocabulary validation: **1,141 records, 0 errors, 0 warnings**; baseline ID/hash check PASS. Informational gaps remain: 80 missing IPA; 296 synonym/antonym references without meanings.
- Learning content validation: **0 errors / 0 warnings** (Listening 121/239, Reading 65/263, Grammar 50/137).
- Repository integrity: **399 inspected, 0 errors, 0 optional warnings**.
- FullSource/Patch ZIP integrity and patch replay: PASS; baseline replay verification performed against v2.95.26.

## Limits
- Full Python discovery not run.
- Remote GitHub Actions, Pages deployment, browser/device acceptance, offline and TTS remain unverified.
- This is a tooling/documentation release, not a content expansion.
