# TOEIC Dictionary — Project Progress Snapshot v2.95.15

- Candidate source: v2.95.15; baseline v2.95.14 (`e269173`).
- Release type: sourced related-term glossary addition plus CI/regression maintenance; local-only candidate.
- Claude's v2.95.13 review remains pending and will be reconciled when the owner shares the result.

## Inventory and status

| Area | Current value | Status |
|---|---:|---|
| Canonical vocabulary | 1,141 headwords | Stable IDs preserved; no new headword in this release |
| Related-term glossary | 387 entries | 4 new glosses in batch 022; independent lexical review pending |
| Synonym/antonym exact join | 376/804 | 428 distinct terms / 465 occurrences remain unglossed |
| Listening | 121 units / 239 questions | 102 eligible / 137 reserve pending independent review |
| Reading | 65 resources / 263 questions | Part 7 second-review gate remains |
| Grammar | 50 lessons / 137 exercises | Retained |
| Separate Part 5 practice | 80 questions | Practice-only; independent review pending |
| Foundation pathway | 23 lessons | Core and supplementary A2 scope unchanged |

## v2.95.15 completed

- Added `aim`, `avoid`, `cause` and `conceal` with POS-scoped, Cambridge-linked glosses.
- Applied an absent-only SHA-256-guarded patch and verified rollback against the exact baseline file hash.
- Added batch 022 provenance, 9 dedicated Python tests, CI execution and JS release-integrity assertions.
- Local verification: 36/36 focused Python cases, 38/38 JavaScript suites, all source syntax checks and three data/repository validators PASS.

## Open gates

- Independent lexical review for all glossary additions remains pending.
- 22 owner-run manual acceptance rows remain Chưa kiểm.
- Remote Actions/Pages and browser/device acceptance remain unverified.
- Full Python aggregate was not completed.

## Recommended next focus

Continue glossary completion only where frequency and contextual need justify it; the next remaining terms each have at most two current relationship references. In parallel, prioritize review of the 93 missing US IPA entries and the existing word-family/verb-form backlog. Do not inflate data counts by adding low-value one-off synonyms.
