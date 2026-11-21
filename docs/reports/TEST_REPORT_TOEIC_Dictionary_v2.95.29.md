# Test Report — TOEIC Dictionary v2.95.29

## Major work delivered
- Canonical related glossary expanded **430 → 519 entries (+89)**, sourced only from exact canonical vocabulary headwords with complete Vietnamese and English senses. All 89 additions record source, source headword and source release `2.95.28`.
- Exact eligible missing canonical related-term candidates: **89 before / 0 after**. The other **296** missing unique related terms do not have an exact canonical bilingual headword match under this strict pipeline and remain queued for researched/editorial work.
- New deterministic tool `tools/enrich-related-glossary-from-canonical.py`: audit-only default, explicit `--apply`, blocks incomplete bilingual senses, deduplicates terms, and never overwrites existing glossary rows.
- Updated backlog and candidate audit expectations, plus glossary quality report for 519 entries.
- No UI, learner progress, assessment questions/answers, canonical headwords, or synonym/antonym arrays changed.

## Verification
- Dedicated canonical enrichment tests: **8/8 PASS**.
- Focused related-glossary + graph test modules: **32/32 PASS**.
- JavaScript regression suites: **39/39 PASS**.
- `tools/validate-data.py`: **1,141 records; 0 errors, 0 warnings** (legacy baseline warnings = 0).
- `tools/validate-learning-content.py`: **0 errors / 0 warnings**; Listening 121 units/239 questions, Reading 65/263, Grammar 50/137.
- `tools/audit-repository-integrity.py`: **403 local references/data files; 0 errors / 0 optional warnings**.
- `tools/sync-version.py --check`: PASS.
- Related glossary audit: **519 entries**; flags still remain for editorial review, not automatically judged incorrect.
- Graph audit: 1,037 relations; 673 absent canonical targets, of which 376 glossary-covered; 297 unresolved occurrences / 296 unique terms; 0 self references; 0 malformed relation records; 248 non-reciprocal review flags.

## Package verification
- FullSource: **485 source/data/docs files**, single root `TOEIC_Dictionary_v2.95.29/`, ZIP CRC PASS.
- Update Patch: **25 changed/added files**, **0 deletions**, ZIP CRC PASS.
- Patch replay against v2.95.28: **485/485 files byte-exact PASS**.
- SHA-256 stored in `TOEIC_Dictionary_v2.95.29_SHA256SUMS.txt`.

## Not verified
- Remote GitHub Actions CI, GitHub Pages deployment, browser acceptance, and actual mobile/desktop device acceptance were not run in this environment.

## Test correction
- A stale JS release-integrity assertion (glossary expected 430) was updated to 519 after expansion; the full JS suite then passed. Candidate-audit expected counts and a report-order-dependent backlog test were also updated to match the new data and deterministic test setup.
