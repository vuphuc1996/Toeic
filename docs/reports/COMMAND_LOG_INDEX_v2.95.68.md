# Command Log Index — TOEIC Dictionary v2.95.68

## Source integrity

| Command / action | Result |
|---|---|
| `sha256sum TOEIC_Dictionary_v2.95.67_FullSource(1).zip` | `1f262ac4d67d8d244facf397b9ea1d179c6a741f50e561b3d3e9805efef31754` |
| `unzip -t TOEIC_Dictionary_v2.95.67_FullSource(1).zip` | PASS; 807 archive entries, no CRC error |
| Extract source and inspect `data/manifest.json` | PASS; sole source version `2.95.67` |

## Validators / syntax

| Command | Result |
|---|---|
| `python tools/validate-data.py` | PASS; 1,141 canonical records; IDs +0 / -0; 0 errors / 0 warnings |
| `python tools/validate-learning-content.py` | PASS; 0 errors / 0 warnings |
| `python tools/validate-part1-photo-assets.py` | PASS; 9/9 |
| `python tools/sync-version.py --check` | PASS; 18/18 release markers |
| `python tools/audit-repository-integrity.py` | PASS; 408 references/data files; 0 errors / 0 warnings |
| `python tools/audit-git-commit-readiness.py` | PASS; 816 indexed paths; 0 errors / 0 warnings |
| `python tools/audit-design-tokens.py` | PASS; 0 new violations; 2,773 legacy warnings |
| `python -m compileall -q tools` | PASS |
| `node --check sw.js` and ES-module syntax check of all `assets/js/*.js` | PASS |
| `python tools/audit-word-family-graph.py --output docs/reports/WORD_FAMILY_GRAPH_AUDIT_v2.95.68.md --json-output docs/reports/WORD_FAMILY_GRAPH_AUDIT_v2.95.68.json` | PASS; report heading reads v2.95.68 |

## Focused Python regression commands

| Selector | Result |
|---|---:|
| `test_vocabulary_family_batch_025.py` | 5/5 PASS |
| `test_related_glossary_batch_036.py` | 6/6 PASS |
| `test_related_glossary_batch_037.py` | 7/7 PASS |
| `test_related_glossary_merge_038.py` | 8/8 PASS |
| `test_single_overlay_contract.py` | 3/3 PASS |
| `test_baseline_ids.py` | 13/13 PASS |
| `test_word_family_graph_audit.py` | 1/1 PASS |
| `test_choice_identity.py` | 9/9 PASS |
| `test_choice_history.py` | 5/5 PASS |
| `test_answer_position_balance.py` | 4/4 PASS |
| `test_learning_content.py` | 34/34 PASS |
| **Total** | **95/95 PASS** |

## Node regression

- Command: loop over every `tools/tests/*.mjs` with `node`.
- Result: **44 scripts PASS, 0 failed**.
- New `assessment-result-focus-workflow.mjs` is registered in GitHub Actions workflow.

## Full Python discovery

- Command attempted: `python -m unittest discover -s tools/tests -v`.
- Result: execution window elapsed before the final unittest summary was produced. Full discovery status is INCOMPLETE; do not treat partial output as a pass.

## Data comparison

- Compared every file under `data/` in the uploaded v2.95.67 ZIP with the v2.95.68 working source.
- Result: all 68 paths match after normalizing only `data/manifest.json.version` from 2.95.68 to 2.95.67. No other data file differs.
- Canonical IDs: 1,141 / 1,141; +0 / -0; duplicate headwords 0.
- Four protected learning-bank composite SHA-256: matches the Batch 036 ledger.
