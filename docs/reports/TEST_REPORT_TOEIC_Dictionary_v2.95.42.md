# Test Report — TOEIC Dictionary v2.95.42


## 1. Release scope

- Base: exact v2.95.41 Full Source archive in the Library.
- Release: v2.95.42 — Related Glossary coverage expansion, Batch 035.
- Eight glossary-only additions: administer, alert, alike, appeal, article, assist, backer, bargaining.
- Test/audit/documentation changes; no UI redesign or learner-facing runtime feature change.

## 2. Implemented changes

- Added eight bilingual glossary rows with POS, paraphrased English definitions, exact Cambridge Dictionary URLs and source provenance. All terms are verified relationship targets and are absent from the canonical A–Z headword set.
- Added hash-guarded additive patch and batch ledger, using the existing atomic related-terms updater.
- Added 4 batch 035 regression tests for inventory, provenance, non-placeholder definitions, relation-target/canonical-headword constraints and ledger/data consistency.
- Registered Batch 035 regression in GitHub Actions and syntax-check list.
- Updated candidate-audit expectations from 527 to 535 entries and uncovered counts from 289/288 to 281/280; definition category present count 304 → 312.
- Hardened Batch 034 historical hash regression to reconstruct its v2.95.40 baseline without later Batch 035 additive rows.
- Regenerated current candidate, backlog, quality flags, relationship graph, major-release quality, progress and coverage reports.

## 3. Research evidence

- Cambridge Dictionary indexed entry excerpts reviewed **2026-11-22** for the eight entries.
- Direct dictionary page opens returned HTTP 403; no claim of direct full-page inspection is made.
- English definitions are paraphrased and example sentences were not copied. Direct URLs are retained per row.
- Independent editorial review remains pending.

## 4. Vocabulary/glossary inventory

| Metric | v2.95.41 | v2.95.42 |
|---|---:|---:|
| Canonical headwords | 1,141 | 1,141 |
| Related Glossary rows | 527 | 535 |
| Normalized unique glossary rows | 527 | 535 |
| Duplicate normalized rows | 0 | 0 |
| Exact referenced-term coverage | 516/804 (64.2%) | 524/804 (65.2%) |
| Uncovered unique terms | 288 | 280 |
| Uncovered relation occurrences | 289 | 281 |
| Placeholder English definitions | 73 | 73 |


## 5. Preservation contract

- No canonical headword IDs, canonical meanings, relation arrays, or vocabulary file contents changed.
- No learning questions, choices, IDs, answer keys, editorial status, Mock eligibility or question/resource IDs changed.
- No learner progress, IndexedDB schema, local storage contract, Robot Buddy data boundary, UI layout or backend/deployment configuration changed.

## 6. Focused Python regression

**74/74 tests PASS across 13 modules** (run individually):

| Module | Tests |
|---|---:|
| `test_related_glossary_batch_032.py` | 4 |
| `test_related_glossary_batch_033.py` | 3 |
| `test_related_glossary_batch_034.py` | 6 |
| `test_related_glossary_batch_035.py` | 5 |
| `test_patch_related_terms.py` | 11 |
| `test_related_glossary_candidate_audit.py` | 4 |
| `test_related_glossary_quality_audit.py` | 11 |
| `test_vocabulary_relationship_graph_audit.py` | 8 |
| `test_related_glossary_backlog.py` | 3 |
| `test_related_term_explanation_context.py` | 3 |
| `test_major_release_quality_audit_025.py` | 8 |
| `test_related_glossary_exact_match_enrichment_035.py` | 5 |
| `test_ci_coverage.py` | 3 |
| **Total** | **74** |


## 7. JavaScript regression and syntax

- All 39 `tools/tests/*.mjs` regression suites PASS.
- `node --check sw.js` PASS.
- All `assets/js/*.js` modules passed syntax check.
- `python -m compileall -q tools` PASS.


## 8. Validators and audits

| Check | Result |
|---|---|
| `tools/validate-data.py` | PASS — 1,141 records; 0 errors / 0 warnings; 0 ID additions/removals |
| `tools/validate-learning-content.py` | PASS — 0 errors / 0 warnings; all current inventory unchanged |
| Repository integrity | PASS — 412 references/data files; 0 errors / 0 optional warnings |
| Version synchronization | PASS — all markers v2.95.42 |
| Design profile | PASS — 54 tokens / 406 legacy selector groups |
| Part 1 assets | PASS — 9/9 |
| Objective resources | PASS — 379/379 |
| Learning outcomes | PASS — 11 objectives / 33 criteria / 6 evidence paths |
| Foundation A2 assessment | PASS — core Reading/Listening 13/13; supplementary Listening 13/13; evidence 5/5 |
| Listening readiness | PASS — 102 eligible / 193 reserve-pending / 295 total |
| Question evidence | PASS — 582 questions indexed; reserve scope 193 |
| Distractor structural audit | PASS — 264 in scope; valid choice identities and answer keys |
| Candidate/backlog/quality/graph audits | PASS — regenerated; 535 glossary rows, 0 normalized duplicates |
| Major-release audit | PASS — coverage and inventory reconciled to current canonical source |


## 9. Aggregate test limitation

Full Python unittest discovery was attempted but was interrupted by the environment execution limit while it was still progressing through the suite. The aggregate run is **not** claimed as a pass. The 73 targeted Python tests listed above are the completed, verified scope. During development, stale coverage assertions and the historical Batch 034 hash reconstruction initially failed; their expectations/fixture reconstruction were corrected, and the listed focused tests subsequently passed.


## 10. External acceptance not performed

- Remote GitHub Actions run
- GitHub Pages deployment/cache verification
- Browser UI, mobile/iOS/Android/iPad/desktop acceptance
- Real-device audio/pronunciation testing
- Independent lexical/translation approval


## 11. Package/replay verification

- Base: v2.95.41 Full Source archive (597 source files).
- Full Source: **620 source files**, single root `Toeic_Dictionary_v2.95.42/`; CRC/root/exclusions PASS; byte-for-byte comparison **620/620** against the release tree.
- Patch: **40 source overlay files** (17 modified + 23 added, 0 deletions) and 2 informational metadata files; ZIP CRC/root/exclusion checks PASS.
- Replay: actual Patch ZIP entries overlaid on the exact v2.95.41 baseline; replayed tree compared to release tree **620/620 files byte-identical**.
- SHA-256 sidecars for Full Source and Patch were generated and verified against the final archive bytes.
- Source packaging used the accessible extracted Full Source tree because this workspace is not a Git clone; `package_source.py`'s git-archive path was not used.
