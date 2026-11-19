# TOEIC Dictionary v2.95.11 — Project Documentation

## Source of truth

- **Current source:** `versions/CURRENT_VERSION.md`.
- **Immediately previous source:** `versions/PREVIOUS_VERSION.md`.
- **Current project status and active backlog:** `MASTER_STATUS.md`.
- **Chronological release history:** `CHANGELOG.md`.
- **Storage, runtime and retirement contracts:** `COMPATIBILITY.md`.
- **Consolidated retired-document index:** `archive/PROJECT_HISTORY.md`.

## Current product

- GitHub Pages static PWA; GitHub-only. No app backend, GAS, iframe or Cloudflare runtime dependency.
- TOEIC Listening & Reading is the active exam-development track. B1 remains a blueprint only; TOEIC Speaking/Writing and IELTS are deferred. B1 blueprint: `reports/FOUNDATION_B1_CURRICULUM_BLUEPRINT_v2.92.0.md`.
- Flashcard sessions use a fixed maximum of 10 cards across all topic and mixed-learning paths; the retired 5-card setting is removed. Robot Buddy is a head-only offline companion. It streams replies progressively and composes varied local responses from its bundled dialogue/FAQ library, lightweight rules and current app/item context; optional read-only Learning Insights use an in-memory snapshot. It is not a generative chatbot and does not call AI/API services or send learner data externally.
- Speech uses device/browser SpeechSynthesis. It is not authentic ETS audio; available voices and audible timing depend on the device and browser.

## Canonical inventory

| Area | Current inventory |
|---|---:|
| Vocabulary | 1,141 headwords across A–Z |
| Grammar | 50 lessons / 137 exercises |
| TOEIC Listening | 121 units / 239 questions |
| TOEIC Reading | 65 resources / 263 questions |
| Separate Part 5 practice | 80 questions; practice-only and review-pending |
| Foundation | 23 lessons (10 Pre-A1/A1 + 13 A2); separate Reading and Listening evidence banks |

Counts describe source inventory, not editorial approval, learner completion, mastery or Mock eligibility. See the current progress snapshot for field coverage and review status. Active independent-review handoffs remain at `reports/TOEIC_BATCH_024_REVIEW_CHECKLIST_v2.92.0.md` and `reports/TOEIC_BATCH_025_REVIEW_CHECKLIST_v2.93.0.md`; their reserve content must not be promoted to Mock eligibility until review is recorded.

## Current release artifacts

- Current Claude audit assessment: `reports/CLAUDE_AUDIT_ASSESSMENT_v2.95.10.md`.
- Current command-log index: `reports/COMMAND_LOG_INDEX_v2.95.11.md`.
- Current Robot Buddy behavior report: `reports/ROBOT_BUDDY_v2.95.9.md`.
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.11.md`.
- Current manual acceptance checklist: `reports/MANUAL_ACCEPTANCE_CHECKLIST.md` (14 items; all start as Chưa kiểm).
- CSS design-token ratchet report: `reports/DESIGN_TOKEN_AUDIT_BASELINE_v2.95.11.md`.
- Current generated progress snapshot: `reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.10.md` (content inventory unchanged in the v2.95.11 tooling/governance update).
- Current editorial evidence audit: `reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.8.md`.
- Current distractor structural audit: `reports/TOEIC_DISTRACTOR_AUDIT_v2.95.8.md`.
- Current Foundation A2 assessment audit: `reports/FOUNDATION_A2_ASSESSMENT_QUALITY_v2.95.8.md`.
- Current Listening readiness audit: `reports/TOEIC_LISTENING_READINESS_v2.95.10.md`.
- Current content coverage audit: `reports/TOEIC_CONTENT_COVERAGE_v2.95.10.md`.
- Previous release report and acceptance checklist remain available for comparison under the v2.95.9 names.

## Documentation policy

Update `MASTER_STATUS.md` for current decisions and backlog; add one entry to `CHANGELOG.md` per release. Keep only current and immediately previous release-specific reports in the active reports folder. Retire older report files through `tools/rotate-release-files.py`; do not delete canonical data, assets, patch provenance or learner-storage contracts as part of documentation rotation.
