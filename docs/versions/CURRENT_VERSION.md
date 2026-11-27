# Current Version — TOEIC Dictionary v2.95.73

- Current source: **v2.95.73** — Word Family Batch 027 reciprocity and self-reference repair.
- Release package: `TOEIC_Dictionary_v2.95.73_FullSource.zip` (not generated in this GitHub-first candidate workflow; the GitHub `candidate` branch is the source of record).
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.73.md`.
- **Sole development baseline:** GitHub `vuphuc1996/Toeic` `candidate` commit `d068526864ccaf1ef4e3f3fca33466239890b387` (v2.95.72, 1,181 headwords).
- Batch 027 adds 10 reciprocal Word Family links and removes 2 self-referential links. No vocabulary records or canonical IDs are added, removed, or renamed.
- Resulting graph: 428 directed links, 331 linked headwords, 0 target-POS mismatches, 0 non-reciprocal links, 0 self-references; 50 missing targets and 70 Vietnamese sense-anchor flags remain open.
- The app version and Service Worker cache keys are synchronized to v2.95.73.
- **Acceptance boundary:** candidate-source validation and Pages deployment are pending for the current commit; production `main` has not been changed. Installed-PWA update/offline and physical-device acceptance remain unverified.
