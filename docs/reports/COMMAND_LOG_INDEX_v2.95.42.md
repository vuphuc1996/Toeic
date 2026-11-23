# Command Log Index — TOEIC Dictionary v2.95.42


## Source and patch

- Retrieved exact Library Full Source `TOEIC_Dictionary_v2.95.41_FullSource(1).zip` and extracted to the release workspace.
- `python tools/patch-related-terms.py --patch patches-related-terms/v2.95.42/related-terms-035.json --dry-run` — PASS; 8 absent terms, no data writes.
- `python tools/patch-related-terms.py --patch patches-related-terms/v2.95.42/related-terms-035.json --apply` — PASS; 8 additive glossary entries; operation audit recorded.
- `python tools/sync-version.py --set 2.95.42 --apply` — PASS; manifest and registered release markers synchronized.
- Historical Batch 034 hash test was adjusted to reconstruct its base release excluding later Batch 035 additions; test PASS.

## Focused Python tests

- `test_related_glossary_batch_032.py` — 4/4 PASS.
- `test_related_glossary_batch_033.py` — 3/3 PASS.
- `test_related_glossary_batch_034.py` — 6/6 PASS.
- `test_related_glossary_batch_035.py` — 5/5 PASS (including reconstruction of the pre-batch base hash).
- `test_patch_related_terms.py` — 11/11 PASS.
- `test_related_glossary_candidate_audit.py` — 4/4 PASS.
- `test_related_glossary_quality_audit.py` — 11/11 PASS.
- `test_vocabulary_relationship_graph_audit.py` — 8/8 PASS.
- `test_related_glossary_backlog.py` — 3/3 PASS.
- `test_related_term_explanation_context.py` — 3/3 PASS.
- `test_major_release_quality_audit_025.py` — 8/8 PASS.
- `test_related_glossary_exact_match_enrichment_035.py` — 5/5 PASS.
- `test_ci_coverage.py` — 3/3 PASS.
- **Focused Python total: 74/74 PASS across 13 modules.**
- `python -m compileall -q tools` — PASS.
- Full aggregate Python discovery was attempted but interrupted by the environment execution limit; no full-suite pass is claimed.

## JavaScript

- `node --check sw.js` — PASS.
- Syntax check for all `assets/js/*.js` modules — PASS.
- Every `tools/tests/*.mjs` suite — **39/39 PASS**.


## Validators/audits

- `python tools/validate-data.py` — PASS (1,141 records; IDs unchanged; 0 errors/warnings).
- `python tools/validate-learning-content.py` — PASS (0 errors/warnings).
- `python tools/audit-repository-integrity.py` — PASS (412 references/data files; 0 errors/warnings).
- `python tools/sync-version.py --check` — PASS (2.95.42).
- `python tools/sync-design-profile.py --check` — PASS (54 tokens/406 selector groups).
- `python tools/validate-part1-photo-assets.py` — PASS (9/9).
- `python tools/audit-objective-resources.py` — PASS (379/379).
- `python tools/audit-learning-outcomes.py` — PASS (11 objectives/33 criteria/6 evidence paths).
- `python tools/audit-foundation-a2-assessment.py` — PASS.
- `python tools/audit-listening-readiness.py` — PASS (102 eligible/193 pending/295 total).
- `python tools/audit-question-evidence.py` — PASS (582 indexed).
- `python tools/audit-distractors.py` — PASS (264 in scope; structurally valid).
- `python tools/audit-major-release.py` — PASS; current release reports regenerated.
- `python tools/audit-related-glossary-candidates.py --output docs/reports/RELATED_GLOSSARY_CANDIDATE_AUDIT_v2.95.42.md` — PASS.
- `python tools/build-related-glossary-backlog.py` — PASS.
- `python tools/audit-related-glossary-quality.py --output ... --json-output ...` — PASS.
- `python tools/audit-vocabulary-relationship-graph.py --output ... --json-output ...` — PASS.
- `python tools/report-project-progress.py > docs/reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.42.md` — PASS.
- `python tools/audit-toeic-coverage.py > docs/reports/TOEIC_CONTENT_COVERAGE_v2.95.42.md` — PASS.


## Release boundary

Remote Actions, Pages deployment/cache, UI/device acceptance, real TTS and independent editorial approval are not verified.


## Package/replay verification

- Base archive integrity/root checked: v2.95.41 Full Source, 597 files.
- `TOEIC_Dictionary_v2.95.42_FullSource.zip` — 620 source files, CRC/root/exclusions PASS, 620/620 byte-identical to release tree.
- `TOEIC_Dictionary_v2.95.42_Patch.zip` — 40 source overlay files (17 modified + 23 added, 0 deletions) plus 2 patch metadata files; CRC PASS.
- Patch ZIP entries were replayed over the exact base Full Source; exact release-tree comparison PASS, 620/620.
- SHA-256 sidecars generated and verified. Package files were created outside the source tree to avoid nested release archives.
