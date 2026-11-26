# Change Manifest — TOEIC Dictionary v2.95.68

## Source chain

- Sole base release: `2.95.67`.
- Base FullSource: `TOEIC_Dictionary_v2.95.67_FullSource(1).zip`.
- Base FullSource SHA-256: `1f262ac4d67d8d244facf397b9ea1d179c6a741f50e561b3d3e9805efef31754`.
- Output release: `2.95.68`.

## Runtime changes

- `assets/js/app.js`: close any prior shared modal, then route assessment-result rendering to the existing active Learning Focus dialog; temporarily preserve and hide the prior focus children; restore header/close-button/ARIA state after result closure; share existing confirmation dispatch for inline and modal result surfaces.
- `assets/css/design-system.css`: extend completion confetti animation from 1.65 s to 2.4 s; existing stagger remains, with roughly 2.88 s maximum visible sequence; `prefers-reduced-motion` remains honored.
- `index.html`, `sw.js`, `assets/js/app.js`, `assets/js/mock-engine.js`, `data/manifest.json`: advance synchronized release markers and release-keyed cache/import URLs to `2.95.68`.

## Regression and tooling changes

- `tools/tests/assessment-result-focus-workflow.mjs`: added behavioral simulation for active Learning Focus result reuse, safe confirmation, and restoring pre-result content.
- `.github/workflows/validate-data.yml`: register the new Node regression and update the versioned Word Family audit report output path.
- `tools/tests/test_single_overlay_contract.py`: assert result reuse and longer confetti duration.
- `tools/tests/glossary_test_helpers.py`: restore Batch 025 Word Family fields to their exact `before: []` snapshots when reconstructing the historical Batch 036 canonical vocabulary checksum.
- `tools/audit-word-family-graph.py`: derive report version from `data/manifest.json` instead of a hardcoded release number.
- `tools/tests/test_word_family_graph_audit.py`: assert that generated audit heading matches the manifest release.

## Documentation and generated reports

- Updated `docs/MASTER_STATUS.md`, `docs/README.md`, `docs/versions/CURRENT_VERSION.md`, `docs/versions/PREVIOUS_VERSION.md`, root and docs changelogs.
- Added release test report, data comparison, command log, and package verification reports.
- Generated versioned Word Family graph audit Markdown and JSON for v2.95.68.

## Data and compatibility boundary

- 68/68 `data/` paths match the sole predecessor; after normalizing only the manifest release marker, data-tree composite SHA is unchanged.
- Canonical vocabulary: 1,141 IDs, +0 / -0; no headword, sense, definition, IPA, example, relation, or learner-facing content was changed.
- Question IDs, choice IDs/order, answer keys, Mock eligibility, and all protected learning-bank files remain unchanged.
- No IndexedDB migration, learner-data rewrite, UI redesign, Robot Buddy change, Cloudflare runtime or backend was added.
