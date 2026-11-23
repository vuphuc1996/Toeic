# Current Version — TOEIC Dictionary v2.95.45

- Current source: **v2.95.45** (alternate QA infrastructure merge + Related Glossary Batch 038).
- Release package: `TOEIC_Dictionary_v2.95.45_FullSource.zip`.
- Full Source contains 698 packaged source files; Patch contains 55 overlay entries (21 modified + 34 added).
- Patch package: `TOEIC_Dictionary_v2.95.45_Patch.zip` (55 overlay entries: 21 modified + 34 added; base: released v2.95.44).
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.45.md`.
- Command log: `reports/COMMAND_LOG_INDEX_v2.95.45.md`.
- Change manifest: `reports/CHANGE_MANIFEST_v2.95.45.md`.
- Comparison report: `reports/COMPARE_MERGE_REVIEW_v2.95.45.md`.
- Batch 038 adds five relation-target terms and makes three exact-guarded, sense-aligned corrections; details and provenance are in `patches-related-terms/v2.95.45/`.
- Related Glossary: 567 rows / 567 normalized unique / 0 duplicates; 556/804 relation targets covered (69.2%); 248 unique / 249 occurrences remain unglossed.
- Added isolated Python test-shard and release acceptance runners. The latter uses the manifest version by default. Full-suite result and acceptance gates are reported with individual statuses; only proven PASS modules are reused on resume.
- No canonical headword/ID, synonym/antonym relation array, learning question/choice ID, answer key, learner IndexedDB schema/progress, Mock eligibility, Robot Buddy boundary or UI layout changed. No Cloudflare/backend added.
- Remote GitHub Actions, GitHub Pages deployment/cache, browser/device QA and independent editorial approval remain unverified/pending.

- Focused local validation: 283 Python PASS / 1 environment-dependent SKIP across 35 modules; JavaScript 39/39; syntax 19/19; data/content/repository/version checks PASS. Full Python discovery is INCOMPLETE, not PASS.
- Acceptance/deployment: combined acceptance run was interrupted by the execution limit; remote GitHub Actions, Pages deployment/cache and physical-device QA remain unverified.
