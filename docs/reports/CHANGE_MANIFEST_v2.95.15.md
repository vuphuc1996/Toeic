# Change Manifest — TOEIC Dictionary v2.95.15 candidate

## Release boundary

- Baseline: v2.95.14 at commit `e269173`.
- Candidate: v2.95.15 on local branch `work-v2.95.15`.
- Claude's independent review of v2.95.13 remains pending; this release does not replace that review or claim its approval.
- Release status: local candidate only; no push, remote Actions run or Pages deployment.

## In-scope changes

| Area | Files | Change |
|---|---|---|
| Related-term glossary | `data/related-terms.json` | Four new Vietnamese glosses: `aim`, `avoid`, `cause`, `conceal`; total 383 → 387. |
| Provenance | `data/vocabulary/batch-022.json` | Four sourced entries, POS, English definition, source URLs and provisional-review status. |
| Safe data patch | `patches-related-terms/v2.95.15/related-terms-001.json` | Four absent-only operations, exact base-file SHA-256, Cambridge Dictionary URL constraints. |
| Regression | `tools/tests/test_related_glossary_batch_022.py` | Verify release metadata, source, POS, existing references, frequency threshold, uniqueness and CI registration. |
| CI | `.github/workflows/validate-data.yml` | Register Python syntax check and dedicated batch 022 test; existing related-patch path filters retained. |
| Release integrity | `tools/tests/vocabulary-release-integrity.mjs` | Assert v2.95.15, batch 022 metadata, four patch operations and 387 glossary records. |
| Version metadata/docs | `data/manifest.json`, `assets/js/app.js`, `sw.js`, `index.html`, `docs/**` | Synchronize release version and update Master, Changelog, acceptance checklist and evidence reports. |

## Explicitly unchanged

- 1,141 canonical vocabulary headwords, stable IDs and topic arrays.
- Synonym/antonym relationship arrays; no relationship is added, deleted or rewritten.
- TOEIC Listening/Reading/Grammar question banks, stable question/choice IDs, answer keys and Mock eligibility.
- Robot Buddy, Flashcard 10-card cap, TTS timing, IndexedDB v1 schema, learner localStorage keys and records.
- Runtime APIs, backend dependencies and external learner-data transfer.

## Review requirements

1. Confirm each Vietnamese gloss and POS against the linked Cambridge entry and the contexts where the term is referenced.
2. Re-run patch dry-run/apply and inspect operation audit logs; rollback must restore the exact baseline file hash.
3. Re-run local data, learning-content, repository-integrity, Python and JavaScript checks.
4. Keep manual acceptance, remote CI/Pages and device checks open until the owner performs them.
5. Do not push or deploy this candidate without owner approval and resolution of Claude's v2.95.13 findings.
