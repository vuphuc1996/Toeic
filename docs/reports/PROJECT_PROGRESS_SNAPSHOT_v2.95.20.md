# Project Progress Snapshot — v2.95.20


## Verified source state
- 1,141 canonical vocabulary headwords; ID baseline validator reports 0 additions and 0 missing IDs.
- Related-term glossary: 400 entries (recovered v2.95.19 baseline had 396; Batch 026 added 4).
- UI/layout remains frozen.
- Listening/Reading reserve review and independent sign-off are still pending; this release does not promote any reserve question into Mock.

## Glossary coverage from this glossary only
- Related-term options observed in canonical synonym/antonym references: 804 distinct term strings, 1,037 occurrences.
- Current related glossary matches 389/804 unique strings (48.4%) and 598/1,037 occurrences (57.7%). These are literal case-folded matches and do not count canonical headwords as glossary lookup records.

## Quality gates
- Vocabulary: 0 errors / 0 warnings (legacy baseline).
- Learning content: 0 errors / 0 warnings.
- Repository integrity: 392 references inspected, 0 errors / 0 optional warnings.
- Batch 026: 4 Cambridge sourced glosses, 5/5 focused tests PASS.
- Patch tool: 11/11 PASS; CI coverage: 3/3 PASS; release integrity: PASS; version synchronization: PASS.
- Full suites, remote CI, deployment, device QA and manual acceptance remain unverified.
