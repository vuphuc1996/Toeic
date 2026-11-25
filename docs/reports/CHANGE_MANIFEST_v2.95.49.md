# Change Manifest — TOEIC Dictionary v2.95.49

## Purpose

Prevent editorial placeholder strings in Related Glossary metadata from being displayed to learners as genuine English definitions, while preserving canonical data and all learner progress.

## Source changes

- `assets/js/related-glossary-quality.js`
  - Added a narrow, shared detector for known glossary placeholder-definition families.
  - Added `getLearnerFacingRelatedGlossaryDefinition()` to return a trimmed genuine definition or an empty value for placeholders/empty values.
- `assets/js/app.js`
  - Synonym/antonym answer explanations now filter `alias.definition_en` before adding an English-definition line. Existing Vietnamese meaning, POS and relation-specific context remain unchanged.
- `sw.js`
  - Added the new module to both required app-shell resources and the canonical app-shell cache list, so the module is available offline and SW002 validation remains clean.
- `tools/tests/related-glossary-quality.mjs`
  - Tests known placeholder families, valid definitions, malformed/empty values, app integration, and all 73 currently flagged canonical placeholder rows.
- `tools/tests/test_related_term_explanation_context.py`
  - Updated source-level contract tests for the shared display filter.
- `.github/workflows/validate-data.yml`
  - Registered the new Node regression test in the CI runtime test sequence.
- Version metadata and current release documentation synchronized to `2.95.49`.

## Data and protected invariants

- No Related Glossary record was rewritten, removed or auto-enriched.
- No vocabulary ID/headword/sense/relation, question ID/choice/answer key, Mock eligibility, learner record, IndexedDB schema or UI layout was changed.
- No backend, Cloudflare, GAS, iframe or external data service was introduced.

## Validation

See `TEST_REPORT_TOEIC_Dictionary_v2.95.49.md`. Full-suite and workflow evidence must be interpreted from their terminal-state reports; hosted GitHub Actions, Pages and physical-device acceptance are separate and remain unverified.
