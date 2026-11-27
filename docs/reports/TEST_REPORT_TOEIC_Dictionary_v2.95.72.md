# Test Report — TOEIC Dictionary v2.95.72

## Source baseline

- Sole predecessor: `TOEIC_Dictionary_v2.95.71_FullSource.zip` (derived from GitHub `vuphuc1996/Toeic` `main` commit `256ca21461e78a7685bed773ddd622a64050e33a`).
- Canonical records: 1,141 → 1,181 (+40 entries from Vocabulary Batch 026).
- Existing Related Glossary: 567 records (65 entries remediated in Batch 046).

## Node regression

- **45/45 scripts PASS**, terminal marker `NODE_SUITE_PASS`.
- JavaScript syntax check (`assets/js/app.js` and `sw.js`): PASS.
- Python compileall (`python -m compileall -q tools`): PASS.

## Other validations

| Check | Result |
|---|---|
| `validate-data.py` | PASS; 1,181 records; IDs +0/−0; 0 errors, 0 legacy warnings |
| `validate-learning-content.py` | PASS; 0 errors, 0 warnings |
| `audit-repository-integrity.py` | PASS; 411 references/data files inspected; 0 errors, 0 optional warnings |
| Part 1 local photo assets | PASS; 9/9 valid |
| `sync-version.py --check` | PASS; 18 release markers +17 app import keys +42 Service Worker precache keys |
| `sync-design-profile.py --check` | PASS; 54 design tokens and 406 typography selector groups synchronized |
| Design-token audit | 0 new violations; 2,773 legacy findings remain as warnings |
| Related Glossary quality audit | 567 entries; 54 flagged; 0 duplicate normalized groups |
| Word Family graph audit | 1,181 headwords; 322 with family; 420 links; 50 missing targets (−40); 1 POS mismatch; 72 Vietnamese sense-anchor mismatches; 10 non-reciprocal links; 0 duplicates/malformed |
| CI coverage contract | 10/10 PASS; Batch 026 and Batch 046 test modules registered |

## Implementation completed

1. Vocabulary Expansion — Batch 026: Added 40 high-frequency TOEIC canonical headwords addressing Word Family graph missing targets, complete with single-pronunciation CMUdict US IPA, collocations, TOEIC example sentences, and reciprocal word family links.
2. Word Family Graph Completion: Reduced missing canonical targets from 90 to 50, verifying reciprocal links and semantic correctness.
3. Related Glossary Remediation — Batch 046: Remediated 65 existing rows (36 placeholders, 2 missing provenance, 27 missing definitions), reducing flagged entries from 119 to 54 while protecting all 567 term identities and Vietnamese meanings.
4. Project progress dashboard: Calculated reproducible **55.88% provisional weighted measurable curriculum-build index** across 7 published workstreams.
5. Version synchronization: Updated all 18 markers, app imports, and Service Worker caches to `v2.95.72`.

## Unverified / not claimed

- GitHub-hosted Actions was not triggered or observed in this run.
- GitHub Pages deployment and live-site behavior were not verified.
- Installed PWA offline/update propagation and physical iOS/iPadOS/Android checks were not performed.
- No Git push or production deployment acceptance is claimed.
