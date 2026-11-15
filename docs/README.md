# TOEIC Dictionary v2.70.0 — Documentation

- Current candidate: `v2.70.0` — `versions/CURRENT_VERSION.md`.
- Previous release: `v2.69.0` — `versions/PREVIOUS_VERSION.md`.
- Master status: `MASTER_STATUS.md`.
- Release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.70.0.md`.
- Progress baseline: `reports/PROJECT_PROGRESS_BASELINE_v2.70.0.md`.
- Generated progress snapshot: `reports/PROJECT_PROGRESS_SNAPSHOT_v2.70.0.md`.
- TOEIC curriculum remains the primary track; Writing/Speaking and IELTS are kept separate from the current L&R completion denominator.
- Assessment flow: selection drafts stay ungraded until a full set is completed and explicitly confirmed.
- Mock Exam: timed schedule, visible current location, automatic focus transitions, spoken lead-ins, and no repeated audio within the same Listening group.
- Listening Part 1: fixed TTS preparation and spoken A–D sequence; media remains JPG-only with no SVG fallback.
- Dashboard and design governance: adaptive responsive layout with `design/design-profile.json` as the canonical token source.
- Vocabulary: **1,100 stable headwords**; v2.70.0 adds Batch 011 (+37) for Customer Service and Travel. Quantity progress is 36.7% of the 3,000 minimum and 22.0% of the 5,000 planning ceiling.
- US IPA: 1,009/1,100 (91.7%) with 298 cumulative source-linked CMUdict entries; the 91 unresolved entries remain blank rather than guessed. Word-family coverage: 267/1,100 (24.3%), 365 directed links.
- Existing IndexedDB schema, question IDs, answer keys, learner progress, personal vocabulary and study settings are preserved. No learning-content inventory is reclassified as editorially approved merely because automated checks pass.
- Release hold: strict Part 1 photo validation still fails because eight original repository-owned JPG binaries are missing from this source snapshot. Remote GitHub Actions, Pages deployment and physical-device QA have not been verified.
