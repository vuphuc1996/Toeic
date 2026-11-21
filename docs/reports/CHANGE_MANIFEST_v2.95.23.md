# Change Manifest — v2.95.23

- Baseline: v2.95.22 FullSource
- Changed: `tools/build-related-glossary-backlog.py`, its Python regression test, generated JSON/Markdown backlog, release docs/version markers.
- Queue schema: v1 → v2. New fields: `sourceHeadwordCount`, `sourceHeadwords`, `synonymReferences`, `antonymReferences`.
- Priority order: total references descending, distinct source-headwords descending, synonym refs descending, term case-insensitive ascending.
- Data coverage unchanged: glossary 423; exact referenced terms 412/804; unglossed 392 terms / 393 occurrences.
- No learner data, vocabulary definitions, canonical word IDs, relation graph, questions, answer keys, UI, CSS or runtime changed.
- Validation: 8 focused Python tests passed; Robot Buddy Node regression passed.
