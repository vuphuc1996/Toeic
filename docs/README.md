# TOEIC Dictionary v2.95.14 — Project Documentation

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

## v2.95.14 candidate content update

- Added ten Cambridge-sourced Vietnamese glosses for existing synonym/antonym terms: `requirement`, `pay`, `ignore`, `withhold`, `retain`, `earnings`, `duty`, `distribute`, `discourage` and `decline`. The related-term glossary increases from 373 to 383 entries.
- The terms already existed in canonical synonym/antonym fields. This patch adds explanatory glossary records only; it does not add headwords or alter any relationship.
- The exact-term coverage audit now finds 372/804 distinct referenced terms with a glossary record; 432 distinct terms and 477 of 1,037 link occurrences remain without a gloss. This is a separate audit from the validator's informational `323/804` line and must not be conflated with it.
- All ten entries are provisional and pending independent lexical review. See `reports/VOCABULARY_GLOSSARY_EXPANSION_v2.95.14.md`, `reports/CHANGE_MANIFEST_v2.95.14.md` and `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.14.md`.

## v2.95.13 candidate content update

- Ten existing headwords (`bill`, `charge`, `document`, `experience`, `function`, `host`, `minute`, `offer`, `supply`, `value`) gained clearer sense-specific meanings and 24 bilingual examples linked by sense index.
- Four new sourced Vietnamese glosses were added for `demand`, `guest`, `inexperience` and `refund`; two reverse family links now point to the correct noun/verb sense of `value`.
- Multi-sense coverage remains 49 headwords / 105 linked examples; the related-term glossary at the end of v2.95.13 had 373 entries. Canonical vocabulary remains 1,141 headwords; that release’s additions are provisional pending independent lexical review.
- See `reports/VOCABULARY_SENSE_EXPANSION_v2.95.13.md` and `reports/CHANGE_MANIFEST_v2.95.13.md` for patch and provenance detail.

## v2.95.12 candidate content update

- Nine existing headwords have additional sense distinctions and 20 sense-linked examples; 22 supporting related-term entries have sourced Vietnamese glosses. Flashcard backs display additional meanings and the example mapped to each extra sense, with the helper included in the Service Worker cache.
- Multi-sense coverage is 39 headwords with 81 linked examples. All additions remain pending independent lexical review.
- Stable identity/topic contract is unchanged; no new canonical headwords were added. See `reports/VOCABULARY_SENSE_EXPANSION_v2.95.12.md`.

## Current release artifacts

- Previous Claude review package manifest: `reports/CHANGE_MANIFEST_v2.95.13.md` (submitted by the owner; result pending). Current release change manifest: `reports/CHANGE_MANIFEST_v2.95.14.md`.
- Current command-log index: `reports/COMMAND_LOG_INDEX_v2.95.14.md`.
- Current Robot Buddy behavior report: `reports/ROBOT_BUDDY_v2.95.9.md`.
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.14.md`.
- Current manual acceptance checklist: `reports/MANUAL_ACCEPTANCE_CHECKLIST.md` (21 items; all remain Chưa kiểm).
- CSS design-token ratchet report: `reports/DESIGN_TOKEN_AUDIT_BASELINE_v2.95.11.md`.
- Current generated progress snapshot: `reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.14.md`.
- Current glossary expansion report: `reports/VOCABULARY_GLOSSARY_EXPANSION_v2.95.14.md`.
- Previous vocabulary sense-expansion report: `reports/VOCABULARY_SENSE_EXPANSION_v2.95.13.md`.
- Current distractor structural audit: `reports/TOEIC_DISTRACTOR_AUDIT_v2.95.8.md`.
- Current Foundation A2 assessment audit: `reports/FOUNDATION_A2_ASSESSMENT_QUALITY_v2.95.8.md`.
- Current Listening readiness audit: `reports/TOEIC_LISTENING_READINESS_v2.95.10.md`.
- Latest inherited content coverage audit: `reports/TOEIC_CONTENT_COVERAGE_v2.95.13.md` (the 2.95.14 change is glossary-only).
- Previous release report and acceptance checklist remain available for comparison under the v2.95.9 names.

## Documentation policy

Update `MASTER_STATUS.md` for current decisions and backlog; add one entry to `CHANGELOG.md` per release. Keep only current and immediately previous release-specific reports in the active reports folder. Retire older report files through `tools/rotate-release-files.py`; do not delete canonical data, assets, patch provenance or learner-storage contracts as part of documentation rotation.
