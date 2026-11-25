# Change Manifest — TOEIC Dictionary v2.95.65

## Source relationship

- Predecessor: `TOEIC_Dictionary_v2.95.64_FullSource.zip`
- Predecessor SHA-256: `03ec4c80e88bc76e435cfc0782e933474be882a4f271318a23375a35e9242673`
- Output: v2.95.65 FullSource and Patch generated only from this predecessor.

## Functional changes

1. Add/replace `tools/tests/test_related_glossary_batch_035_cambridge.py` with a historical reconstruction test for Batch 035. It reverses later glossary changes and correction records before validating the source ledger, relation anchors, expected 535-row historical checkpoint and exact pre-batch SHA. It does not alter current glossary data (currently 567 entries).
2. Remove the standalone `modalBackdrop` element and `.modal-backdrop` CSS identity. The existing `learningFocusBackdrop` becomes the only full-screen dimming/blur root; `modalLayer` is its transparent nested modal-panel layer.
3. Centralize overlay state/ARIA/body-scroll changes in `showModalLayer()` and `hideModalLayer()`; preserve active focus session when a nested modal closes.
4. Add `test_single_overlay_contract.py` and an explicit workflow step; keep the existing Batch 035 wildcard selector and add tests for both modules.
5. Reconcile design-token baseline selector identities with the modal-layer rename and retire the duplicate backdrop-background identity; design-token audit has zero new findings.
6. Update release/version records and bump synchronized version markers to 2.95.65.

## Protected data

No vocabulary, Related Glossary, question, choice, answer-key, Mock eligibility, learner IndexedDB record/schema or Robot Buddy privacy data was modified. The only expected file under `data/` to differ from the predecessor is `data/manifest.json` (version marker only).

## GitHub Actions changes

- Add a dedicated `test_single_overlay_contract.py` step adjacent to practice/modal contract tests.
- Existing `test_related_glossary_batch_035*.py` wildcard remains unchanged and selects the newly included Cambridge module.
- YAML is parsed locally; 125 unique step names, each step has exactly one `run` or `uses` action.
