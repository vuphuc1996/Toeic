# Change Manifest — TOEIC Dictionary v2.95.17

## Release summary

A glossary-only content batch that fills nine repeated gaps in existing synonym/antonym references. Packaging remains governed by the one-root, committed-source-only ZIP tool introduced in v2.95.16.

## Canonical data delta

| Item | v2.95.16 | v2.95.17 | Delta |
|---|---:|---:|---:|
| Canonical vocabulary headwords | 1,141 | 1,141 | 0 |
| Related-term glossary entries | 387 | 396 | +9 |
| Distinct synonym/antonym terms with glossary entries | 376/804 | 385/804 | +9 |
| Unglossed distinct referenced terms | 428 | 419 | -9 |
| Unglossed reference occurrences | 465 | 447 | -18 |

New lookup terms: `choose`, `distribution`, `effect`, `estimate`, `former`, `inform`, `origin`, `possibility`, `responsibility`. Each is referenced exactly twice in the unchanged canonical synonym/antonym graph.

## Files changed / added

- `data/related-terms.json` — nine lookup records appended and sorted.
- `data/vocabulary/batch-023.json` — provenance ledger, POS scope, concise English paraphrases, Vietnamese glosses and Cambridge URLs.
- `patches-related-terms/v2.95.17/related-terms-001.json` — absent-only patch with exact base-file SHA-256.
- `tools/tests/test_related_glossary_batch_023.py` — nine regression checks for metadata, provenance, linkage, POS, reference frequency, uniqueness and CI registration.
- `tools/tests/test_related_glossary_batch_022.py` and `tools/tests/vocabulary-release-integrity.mjs` — historical release assertions remain valid after glossary expansion; JavaScript release check now includes Batch 023.
- `tools/report-project-progress.py` and `tools/tests/test_project_progress.py` — adds exact related-term join coverage as a measured progress metric.
- `.github/workflows/validate-data.yml` — registers Batch 023 and the package-source tests in syntax/unit steps.
- Version markers, changelog, master ledger, current/previous version docs, README, progress snapshot and release reports updated.

## Integrity boundary

No canonical headword, stable ID, topic array, synonym/antonym relationship, word-family link, exam question, answer key, learner record, IndexedDB schema, localStorage key or runtime data structure was changed. Only release-version markers changed in app/service-worker/UI shell metadata. All nine glosses remain provisional pending independent lexical review.

## Delivery boundary

Local candidate only. No GitHub push, GitHub Actions execution, GitHub Pages deployment or owner-run device acceptance was performed.
