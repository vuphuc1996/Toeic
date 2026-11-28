# Current Version — TOEIC Dictionary v2.95.77

- Current source: **v2.95.77** — Migration Compatibility & CI Recovery.
- Release package: `TOEIC_Dictionary_v2.95.77_FullSource.zip`.
- Package location & verification: generated in `/tmp` outside repository root; SHA-256 recorded in `reports/PACKAGE_VERIFICATION_v2.95.77.md`.
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.77.md`.
- **Predecessor baseline:** `v2.95.76` candidate commit `035dd6e2001b3b049407f71acd21f9c33f33e776`.
- **Migration Profiles Reconciled:** Extended all 7 existing historical migration repair profiles (`979`, `992`, `1026`, `1063`, `1100`, `1137`, `1141`) with the 40 Batch 028 IDs, and added a new exact profile for the 1,181-word v2.95.75 snapshot (`1181`).
- **CI Recovery & Integrity:** Resolved the vocabulary release integrity test failure (`1221 !== 1181`), ensuring full compatibility with the 1,221-word inventory.
- **Protected Boundaries:** Maintained all 1,221 canonical words, all 831 question/support items, Mock eligibility rules, learner IndexedDB schema, and UI/UX layout unchanged. `main` branch remains untouched.
- **Acceptance boundary:** Source Release Accepted (local workspace). Candidate CI, Pages deployment, installed-PWA propagation, and physical-device QA remain unverified.
