# Change Manifest — v2.95.24

- Baseline: v2.95.23 FullSource.
- Changed: `tools/build-related-glossary-backlog.py`, `tools/tests/test_related_glossary_backlog.py`, generated backlog JSON/Markdown, release/version docs.
- Fix: merge case variants by normalized term key; combine synonym/antonym counts and references; deduplicate source-headword anchors; deterministic display casing.
- Current dataset has no case-variant duplicate terms, so 423 glossary entries, 412/804 coverage and 392/393 uncovered totals remain unchanged.
- No canonical vocabulary headwords, stable IDs, relations, learning content, learner data, UI, CSS or runtime changed.
- Local focused checks only; no remote CI, deployment or browser/device QA.
