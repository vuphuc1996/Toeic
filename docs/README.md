# TOEIC Dictionary v2.95.45 — Project Documentation

## Current candidate — v2.95.45

- Reconciles the owner-supplied alternate v2.95.44 FullSource with the released v2.95.44 source. The alternate source has 683 files versus 664 in the release; its 46 exclusive, 27 release-exclusive and 43 changed common paths were reviewed. It is not used as a wholesale replacement.
- Adopted the isolated Python test-shard runner and the reproducible release-acceptance runner from the alternate source. The acceptance runner now defaults its report version from `data/manifest.json`, rather than a stale hard-coded version. Checkpoints are versioned and inventory-guarded; timeout/failure/incomplete results are never treated as PASS.
- Related Glossary Batch 038 adds five verified existing relation targets: `ask for`, `change`, `comments`, `communicate with` and `connection`. Three existing entries were sense-corrected against their existing relation anchors: `caller` → visitor sense, `article` → object/item sense, `assume` → responsibility/control sense. The existing synonym/antonym arrays were not changed.
- Glossary: **567 entries / 567 normalized unique / 0 duplicates**; **556/804** exact relation targets covered (**69.2%**); **248 unique terms / 249 occurrences** remain uncovered. `consideration` from the alternate source was not merged because its noun POS does not directly match the linked verb `consider`; retain it for editorial review.
- No canonical vocabulary headwords/IDs, relation arrays, question/choice IDs, answer keys, learner IndexedDB data/schema, Mock eligibility, Robot Buddy boundary or UI layout changed. No Cloudflare/backend was added.
- Current reports: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.45.md`, `reports/COMMAND_LOG_INDEX_v2.95.45.md`, `reports/TOEIC_GLOSSARY_BATCH_038_v2.95.45.md`, `reports/COMPARE_MERGE_REVIEW_v2.95.45.md`, `reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.45.md` and `reports/RELEASE_ACCEPTANCE_v2.95.45.md`.
- Remote GitHub Actions, GitHub Pages deployment/cache and physical browser/device acceptance remain unverified; content is provisional pending independent editorial review.

## Previous release — v2.95.44

- Related Glossary Batch 037 added 16 Cambridge Dictionary-sourced relation-target glosses. See `reports/TOEIC_GLOSSARY_BATCH_037_v2.95.44.md` and the v2.95.44 FullSource/Patch release records.

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

## GitHub commit ZIP contract

- Commit ZIPs are generated from committed Git files only (`git archive`), not from the working folder.
- ZIP has one root folder: `Toeic_Dictionary_vX.Y.Z/`.
- Local logs, `.git`, bundles, nested ZIPs, caches, release artifacts and archive folders are not included.
- Use `python tools/package_source.py X.Y.Z output.zip`; tracked changes must be committed first.

## Canonical inventory

| Area | Current inventory |
|---|---:|
| Vocabulary | 1,141 headwords across A–Z |
| US IPA coverage | 1,062/1,141 headwords (93.1%; 79 still blank, independent phonetic review pending) |
| Related-term glossary | 567 entries (556/804 exact referenced-term join; 248 unique relation terms / 249 occurrences remain uncovered; 150 missing English definitions, 73 placeholders; independent lexical review pending) |
| Grammar | 58 lessons / 169 exercises |
| TOEIC Listening | 145 units / 295 questions |
| TOEIC Reading | 73 resources / 287 questions |
| Separate Part 5 practice | 80 questions; practice-only and review-pending |
| Foundation | 23 lessons (10 Pre-A1/A1 + 13 A2); separate Reading and Listening evidence banks |

Counts describe source inventory, not editorial approval, learner completion, mastery or Mock eligibility. See the current progress snapshot for field coverage and review status. Active independent-review handoffs remain at `reports/TOEIC_BATCH_024_REVIEW_CHECKLIST_v2.92.0.md` and `reports/TOEIC_BATCH_025_REVIEW_CHECKLIST_v2.93.0.md`; their reserve content must not be promoted to Mock eligibility until review is recorded.

## v2.95.21 candidate content update

- Continued Batch 027 in the related-term glossary: 23 Cambridge-referenced Vietnamese lookup glosses were added for terms already used by canonical synonym/antonym relations. The 23 records include the additional source-verified terms `maximum`, `different`, `determine` and `approach`; `disorganize` remains deferred because the direct dictionary-definition source requirement was not met.
- Glossary inventory increases from 400 to 423. Exact case-insensitive coverage rises from 389/804 (48.4%) to 412/804 (51.2%); occurrence coverage rises from 598/1,037 (57.7%) to 644/1,037 (62.1%). Remaining: 392 distinct terms / 393 occurrences.
- Canonical headwords and stable IDs, synonym/antonym relations, learning content, learner records and UI/layout are unchanged. New glossary entries remain provisional pending independent lexical review.
- Focused local checks and all 39 JavaScript suites pass; aggregate Python discovery remains incomplete due to the execution limit. Remote CI, deployment and browser/device acceptance are not claimed. See `reports/CHANGE_MANIFEST_v2.95.23.md`, `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.21.md` and `reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.42.md`.

## v2.95.18 candidate content update

- Added source-checked US IPA for 13 existing single-pronunciation headwords: `accountable`, `admission`, `backlog`, `carrier`, `confidentiality`, `creditor`, `credential`, `designation`, `documentation`, `duration`, `eligible`, `emerge` and `exemption`.
- US IPA coverage rises from 1,048/1,141 (91.8%) to 1,061/1,141 (93.0%). The remaining 80 blanks are not guessed; polysemous entries with POS-specific pronunciation variants require separate review.
- Only the existing `phonetic.us` field changed. No headword, ID, topic, learning content, answer key, learner data, or UI layout was changed. Independent phonetic review remains pending.
- See `reports/US_IPA_BACKFILL_v2.95.18.md`, `reports/CHANGE_MANIFEST_v2.95.18.md`, `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.18.md` and `reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.42.md`.

## v2.95.17 candidate content update

- Added nine Cambridge-sourced Vietnamese glosses for existing related terms: `choose`, `distribution`, `effect`, `estimate`, `former`, `inform`, `origin`, `possibility` and `responsibility`.
- All nine terms occur twice in current synonym/antonym relationships. Glossary entries rise from 387 to 396; the exact case-insensitive join rises from 376/804 to 385/804 (47.9%). Remaining gaps: 419 distinct terms / 447 occurrences.
- This is a lookup-only change; no headword, ID, topic, relationship, question, answer, learner data or runtime contract changed. The new translations/definitions remain provisional pending independent lexical review.
- See `reports/VOCABULARY_GLOSSARY_EXPANSION_v2.95.17.md`, `reports/CHANGE_MANIFEST_v2.95.17.md`, `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.17.md` and `reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.17.md`.

## v2.95.15 candidate content update

- Added four Cambridge-sourced Vietnamese glosses for frequently referenced existing synonym/antonym terms: `aim`, `avoid`, `cause` and `conceal`. Glossary inventory increases from 383 to 387 entries.
- POS scope is explicit: `aim` (n), `avoid` (v), `cause` (n/v), `conceal` (v). No canonical relationship, headword, stable ID or topic was changed.
- Exact-term coverage after the update: 376/804 distinct referenced terms have a glossary record; 428 distinct terms and 465 of 1,037 link occurrences remain without one. This exact join is separate from the validator's informational counter.
- New content is provisional and pending independent lexical review. See `reports/VOCABULARY_GLOSSARY_EXPANSION_v2.95.15.md`, `reports/CHANGE_MANIFEST_v2.95.15.md` and `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.15.md`.

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


## v2.95.32 — Major content batch 026

- Added 8 Grammar lessons / 32 exercises, 8 Listening units / 24 questions, and 8 Reading Part 7 passages / 24 questions (80 new practice items total).
- Original-editorial practice content with Vietnamese rationales, traceable transcript/passage quotes, stable IDs, balanced answer keys and SHA-256 batch inventory.
- New Listening and Reading are review-pending and excluded from Mock; all 24 resources are mapped to objectives.
- Batch manifest: `tools/content-batch-026-v2.95.32.json`; current progress snapshot and test report are in `reports/`.

## Current release artifacts

- Current release comparison: `reports/COMPARE_MERGE_REVIEW_v2.95.45.md`.
- Current release change manifest: `reports/CHANGE_MANIFEST_v2.95.45.md`.
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.45.md`.
- Current command-log index: `reports/COMMAND_LOG_INDEX_v2.95.45.md`.
- Current release acceptance status: `reports/RELEASE_ACCEPTANCE_v2.95.45.md` (full Python suite incomplete; do not infer aggregate PASS).
- Current project progress: `reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.45.md`.
- Current glossary batch report: `reports/TOEIC_GLOSSARY_BATCH_038_v2.95.45.md`.
- Current related-term candidate/backlog/quality audits: `reports/RELATED_GLOSSARY_CANDIDATE_AUDIT_v2.95.45.md`, `reports/RELATED_GLOSSARY_BACKLOG.md` and `reports/RELATED_GLOSSARY_QUALITY_FLAGS_v2.95.45.md`.
- Current relationship graph audit: `reports/VOCABULARY_RELATIONSHIP_GRAPH_AUDIT_v2.95.45.md`.
- Current content/listening/distractor audits: `reports/TOEIC_CONTENT_COVERAGE_v2.95.45.md`, `reports/TOEIC_LISTENING_READINESS_v2.95.45.md`, `reports/TOEIC_DISTRACTOR_AUDIT_v2.95.45.md`.
- Current Full Source and Patch: `TOEIC_Dictionary_v2.95.45_FullSource.zip` and `TOEIC_Dictionary_v2.95.45_Patch.zip` (the Patch is based on released v2.95.44).
- Current independent-review queue: `reports/TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.45.md` (360 pending decisions; Listening 193, Part 7 87, Part 5 80).
- Current manual acceptance checklist: `reports/MANUAL_ACCEPTANCE_CHECKLIST.md`; physical browser/device items remain unverified.
- CSS design-token baseline: `reports/DESIGN_TOKEN_AUDIT_BASELINE_v2.95.11.md`.
- Current editorial evidence audit: `reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.45.md`.
- Current Foundation A2 assessment audit: `reports/FOUNDATION_A2_ASSESSMENT_QUALITY_v2.95.45.md`.


## Documentation policy

Update `MASTER_STATUS.md` for current decisions and backlog; add one entry to `CHANGELOG.md` per release. Keep only current and immediately previous release-specific reports in the active reports folder. Retire older report files through `tools/rotate-release-files.py`; do not delete canonical data, assets, patch provenance or learner-storage contracts as part of documentation rotation.
