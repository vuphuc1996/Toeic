# Test Report — TOEIC Dictionary v2.95.40

## Release scope

- Base: exact user-supplied `TOEIC_Dictionary_v2.95.39_FullSource.zip` (569 ZIP entries, CRC valid).
- Release: v2.95.40 — Audit 025 metric reconciliation + Related Glossary Batch 034 correction.
- No visual redesign or new learning feature. Existing UX was kept frozen.

## Root cause and code changes

- Reproduced the user's original failure on v2.95.39: 7/8 pass; `relatedGlossary.entries` returned 527 while the test still expected 519.
- Confirmed 519 was the pre-Batch-033 inventory; Batch 033 contributed eight legitimate terms. Current data contains 527 raw rows, 527 normalized unique terms and zero duplicate terms.
- Updated the audit generator to expose raw, normalized-unique and duplicate counts. Updated the Audit 025 test to check canonical data rather than a historical literal.
- Corrected one stale `revision` English gloss to match the current exact single-sense canonical definition using a SHA-256 guarded, atomic update patch. Vietnamese meaning, POS and source provenance are preserved.
- Fixed Batch 030 test data loading to use only manifest-listed A–Z canonical files instead of globbing editorial batch snapshots.
- Added `tools/update-related-terms.py`, Batch 034 ledger/patch and six regression tests. CI syntax/test registration updated.

## Focused Python test results

**137/137 tests PASS across 23 modules** (individually executed):

| Module | Result |
|---|---:|
| `test_major_release_quality_audit_025.py` | 8/8 PASS |
| `test_related_glossary_batch_030.py` | 4/4 PASS |
| `test_related_glossary_batch_021.py` | 7/7 PASS |
| `test_related_glossary_batch_022.py` | 9/9 PASS |
| `test_related_glossary_batch_023.py` | 9/9 PASS |
| `test_related_glossary_batch_026.py` | 5/5 PASS |
| `test_related_glossary_batch_027.py` | 5/5 PASS |
| `test_related_glossary_batch_028.py` | 4/4 PASS |
| `test_related_glossary_canonical_enrichment_029.py` | 8/8 PASS |
| `test_related_glossary_backfill_025.py` | 6/6 PASS |
| `test_related_glossary_batch_032.py` | 4/4 PASS |
| `test_related_glossary_batch_033.py` | 3/3 PASS |
| `test_related_glossary_batch_034.py` | 6/6 PASS |
| `test_related_glossary_exact_match_enrichment_035.py` | 5/5 PASS |
| `test_related_glossary_candidate_audit.py` | 4/4 PASS |
| `test_related_glossary_quality_audit.py` | 11/11 PASS |
| `test_related_glossary_backlog.py` | 3/3 PASS |
| `test_patch_related_terms.py` | 11/11 PASS |
| `test_related_term_explanation_context.py` | 3/3 PASS |
| `test_practice_mode_fallback.py` | 6/6 PASS |
| `test_ci_coverage.py` | 3/3 PASS |
| `test_sync_version.py` | 12/12 PASS |
| `test_repository_integrity.py` | 1/1 PASS |

## JavaScript and syntax

- JavaScript regression suites: **39/39 PASS**.
- `node --check sw.js` and every `assets/js/*.js`: PASS.
- `python -m compileall -q tools`: PASS.
- CI coverage regression: 3/3 PASS, including the Batch 034 test registration.

## Data, content and cross-domain audits

| Check | Result |
|---|---|
| `tools/validate-data.py` | PASS — 1,141 records; 0 errors / 0 warnings; 0 IDs added or removed |
| `tools/validate-learning-content.py` | PASS — 0 errors / 0 warnings; Listening 145/295, Reading 73/287, Grammar 58/169; separate Part 5 practice 80 |
| Part 1 photo validation | PASS — 9/9 |
| Repository integrity preflight | PASS — 411 references/data files; 0 errors / 0 optional warnings |
| Version synchronization | PASS — all current markers v2.95.40 |
| Design profile | PASS — 54 tokens / 406 legacy font-floor groups |
| Objective resources | PASS — 379/379 across 11 objectives |
| Learning outcome instrumentation | PASS — 11 objectives / 33 criteria; 6/33 evidence paths; not claimed fully instrumented |
| Question evidence | PASS — 582 questions indexed |
| Distractor structural audit | PASS — 264 questions in scope; unique choices and valid answer keys |
| Foundation A2 assessment | PASS — core Reading/Listening 13/13; supplementary Listening 13/13; source evidence 5/5 |
| Listening readiness | PASS — 102 eligible / 193 reserve-pending-independent-review / 295 total |

## Glossary metrics after reconciliation

- Entries (raw rows): **527**
- Unique normalized entries: **527**
- Duplicate normalized entries: **0**
- Referenced unique terms: **804**
- Covered unique terms: **516 (64.2%)**
- Unglossed unique terms / occurrences: **288 / 289**
- Placeholder English definitions remaining: **73**
- Quality flags: **227 entries**; duplicate groups **0**.

## Not verified / limits

- Full aggregate Python discovery is **not claimed**. An attempt to run the full `test_validator.py` module exceeded the execution time limit; its entire module is not marked PASS. The direct `validate-data.py` executable completed successfully with 0 errors / 0 warnings.
- Remote GitHub Actions, actual GitHub Pages deployment/cache, browser visual acceptance and real iOS/Android/desktop audio QA were not run here.
- Independent editorial/second-person review of Batch 033 terms, remaining glossary flags and unreviewed TOEIC reserve content remains pending.
- No learner progress, IndexedDB v1 schema, answer history, canonical vocabulary ID set, question pool or Mock eligibility was changed.

## Package

- Full Source: **587 files**.
- ZIP CRC / single root / exclusion policy: **PASS**.
- Exact source comparison: **587/587 files byte-identical** after archive creation.
- SHA-256 sidecar: `TOEIC_Dictionary_v2.95.40_FullSource.zip.sha256` — verified against the final archive.
