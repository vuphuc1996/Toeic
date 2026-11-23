# Command Log Index — v2.95.44 / Batch 037

All commands below were run against the extracted v2.95.43 source tree after applying the guarded Batch 037 changes. Commands are listed with their actual completed status; the full test-discovery timeout is explicitly separated.

## Patch application

```bash
python tools/patch-related-terms.py --patch patches-related-terms/v2.95.44/related-terms-037.json --dry-run
python tools/patch-related-terms.py --patch patches-related-terms/v2.95.44/related-terms-037.json --apply
```

Result: dry-run PASS; apply PASS. Patch base SHA-256 was checked by the updater. Sixteen records were added; no existing glossary row was overwritten.

## Focused Python regression

Each suite was executed using `python -m unittest discover -s tools/tests -p '<test-file>.py' -v`.

- `test_related_glossary_batch_037.py` — 7/7 PASS
- `test_related_glossary_batch_036.py` — 6/6 PASS
- `test_related_glossary_batch_035.py` — 5/5 PASS
- `test_related_glossary_batch_034.py` — 6/6 PASS
- `test_related_glossary_batch_027.py` — 5/5 PASS
- `test_patch_related_terms.py` — 11/11 PASS
- `test_related_glossary_candidate_audit.py` — 4/4 PASS
- `test_related_glossary_backlog.py` — 3/3 PASS
- `test_related_glossary_quality_audit.py` — 11/11 PASS
- `test_vocabulary_relationship_graph_audit.py` — 8/8 PASS
- `test_major_release_quality_audit_025.py` — 8/8 PASS
- `test_project_progress.py` — 4/4 PASS
- `test_related_term_explanation_context.py` — 3/3 PASS
- `test_ci_coverage.py` — 3/3 PASS
- `test_vocabulary_detail_examples.py` — 19/19 PASS after a stale historical-field assertion was corrected
- `test_repository_integrity.py` — 1/1 PASS
- `test_package_source.py` — 3/3 PASS
- `test_responsive_layout.py` — 7/7 PASS
- `test_learning_surface_consistency.py` — 5/5 PASS
- `test_pwa_readiness.py` — 3/3 PASS
- `test_part1_photo_assets.py` — 6/6 PASS
- `test_release_rotation.py` — 6/6 PASS
- `test_editorial_review.py` — 6/6 PASS

Focused aggregate: **134 tests / 22 suites PASS**.

## Syntax, data and consistency checks

```bash
python -m compileall -q tools
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/sync-version.py --check
python tools/validate-part1-photo-assets.py
python tools/audit-repository-integrity.py
```

Result: all commands completed successfully. Validator details are in the Test Report.

JavaScript:

```bash
node --check sw.js
# Each assets/js/*.js copied to a temporary .mjs path, then:
node --check <temporary-module.mjs>
# All tools/tests/*.mjs:
node <test-file.mjs>
```

Result: Node v22.16.0; 18/18 JavaScript asset modules passed syntax check; `sw.js` passed; 39/39 `.mjs` test files passed.

## Regenerated audits/reports

```bash
python tools/audit-listening-readiness.py
python tools/audit-question-evidence.py
python tools/audit-distractors.py
python tools/audit-toeic-coverage.py
python tools/audit-learning-outcomes.py
python tools/audit-foundation-a2-assessment.py
python tools/build-editorial-review-queue.py
```

All completed and wrote the corresponding v2.95.44 reports under `docs/reports/`.

## Incomplete / external checks

- Full Python unittest discovery was attempted with a 115-second timeout. It did not finish before the environment timeout; the partial log stopped during `test_patch_data.py`. Do not treat this as PASS.
- Remote GitHub Actions, GitHub Pages deployment/cache and browser/device acceptance were not executed.
- No independent human editorial review was performed.

## Release packaging and replay

- Previous Full Source v2.95.43 was freshly extracted from its verified archive (base tree: 641 files).
- v2.95.44 source tree: 664 files after excluding runtime `logs/`, `__pycache__/` and `*.pyc`.
- Diff: 23 additions, 20 modifications, 0 deletions; Patch overlay: 43 files.
- Generated Full Source and Patch ZIPs; `ZipFile.testzip()` passed for both. Each archive has one root and no excluded runtime/cache files.
- Replayed the generated Patch onto a fresh v2.95.43 extraction and compared the resulting tree to v2.95.44: 664/664 files byte-identical; 0 missing / 0 extra / 0 mismatched.
- SHA-256 sidecar files created and verified against the ZIP bytes.
