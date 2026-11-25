# Change Manifest — v2.95.47

- Base: exact `TOEIC_Dictionary_v2.95.46_Integrity_Continuation_FullSource.zip` archive; this is a continuation overlay, not an official v2.95.46-to-v2.95.47 patch from a user-supplied release baseline.
- Functional change: objective summaries and due-recall queries now use a non-mutating read view rather than `ensureObjectiveProgress()`.
- Regression tests: deeply frozen learner ledger, empty ledger and null ledger; verifies no creation of `schemaVersion` / `objectives` and no nested history mutation.
- Explicit write functions retain existing initializer behavior.
- Version bump: manifest, app, service worker, title/sidebar/phase-note/footer, docs and changelog synchronized to 2.95.47.
- No intentional changes to vocabulary/content datasets, related terms, questions, answer keys, IndexedDB schema or learner history.
