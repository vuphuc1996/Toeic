# TOEIC Dictionary — Project Progress Snapshot v2.95.14

## Current source

- Candidate: v2.95.14; predecessor: v2.95.13.
- Delivery architecture: GitHub Pages static PWA, GitHub-only; no runtime backend.
- Claude's review of v2.95.13 was submitted by the owner and is pending; this v2.95.14 work proceeds independently as a local candidate.

## Inventory

| Area | Current inventory | Status boundary |
|---|---:|---|
| Canonical vocabulary | 1,141 headwords | Stable ID set unchanged; 3,000 minimum target remains |
| Multi-sense vocabulary | 49 headwords / 105 linked examples | New lexical data remains provisional pending review |
| Related-term glossary | 383 records | Ten glossary additions in v2.95.14; independent review pending |
| Listening | 121 units / 239 questions | 102 eligible / 137 reserve pending independent review |
| Reading | 65 resources / 263 questions | Part 7 second-review gate remains |
| Grammar | 50 lessons / 137 exercises | No approved total target |
| Separate Part 5 practice | 80 questions | Practice-only; not Mock-eligible pending review |
| Foundation | 23 lessons | Pre-A1/A1/A2 pathway; separate from TOEIC exam evidence |

## v2.95.14 glossary delta

Ten existing synonym/antonym terms were given Vietnamese glosses: `requirement`, `pay`, `ignore`, `withhold`, `retain`, `earnings`, `duty`, `distribute`, `discourage`, `decline`. The canonical word inventory and relationship graph were not changed. Exact-term join coverage is 372/804 distinct referenced terms; 432 remain unglossed (477/1,037 link occurrences).

## Automated verification

- Focused Python: 43/43 cases across five modules.
- JavaScript regression: 38/38 `.mjs` suites.
- Vocabulary validator: 1,141 records, 0 ID additions/missing, 0 errors/warnings.
- Learning content validator: 0 errors/warnings.
- Repository integrity before report-file creation: 382 references/data files, 0 errors/warnings.
- Version markers and release integrity: PASS.

## Open gates

1. Review Claude's v2.95.13 result once provided and reconcile any findings.
2. Independently review the ten new glossary records and all inherited v2.95.13 editorial additions.
3. Run remote GitHub Actions and deploy Pages only after owner approval.
4. Complete 21 owner acceptance checks; all remain `Chưa kiểm`.
5. Continue unglossed synonyms/antonyms, missing IPA (93 entries) and broader vocabulary growth after editorial validation.

No GitHub push, remote Actions run, Pages deployment, manual device test or learner data migration was performed.
