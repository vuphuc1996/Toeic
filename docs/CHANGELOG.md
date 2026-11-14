## v2.39.0 — TOEIC Part 5 Grammar and Structure Expansion (2026-11-14)

- Expanded the separate adaptive TOEIC Part 5 sentence-completion practice bank from 35 to 80 original questions by adding 45 Batch 016 items (`p5-sc-036`–`p5-sc-080`).
- Added grammar-group metadata across 14 categories and surfaced the group in the question workspace and answer review; answer positions are balanced A/B/C/D=20/20/20/20.
- Tightened several potentially ambiguous distractor sets (`beneficial to`, `notify someone of`, `purpose of + V-ing`, `keep available for`) and added regression coverage for those constructions.
- Preserved canonical vocabulary IDs, distinct Part 5 question history, existing progress weighting, Focus Workspace, shuffle/explanation alignment and IndexedDB v1. All 80 items remain pending independent second-person review and excluded from Mock.
- Local checks: Part 5 Python 12/12, PWA readiness 3/3, CI coverage 2/2, Part 5/Focus Workspace/Practice Progress JavaScript regressions, data validator 0 errors/0 warnings, learning-content validator 0 errors/8 pre-existing Part 1 JPG warnings, source syntax checks and release overlay simulation.
- Remote GitHub Actions/Pages deployment, browser offline/reconnect and physical-device QA are not claimed.
- Detailed record: `batches/TOEIC_PART5_GRAMMAR_EXPANSION_BATCH_016_v2.39.0.md`; verification: `reports/TEST_REPORT_TOEIC_Dictionary_v2.39.0.md`.

# TOEIC Dictionary — consolidated release changelog

## v2.38.0 — TOEIC Part 5 Sentence Completion Practice (2026-11-14)

- Added a separate Part 5 incomplete-sentence practice mode with 35 original TOEIC-style questions linked to existing vocabulary records. Each item has one blank, four shuffled A–D choices, one keyed answer, a Vietnamese translation, grammar focus, answer rationale and option-specific explanations.
- Reuses the existing Focus Workspace, progress scheduler, feedback modal, Retry-compatible study progress and auto-next flow. A separate optional `sentenceCompletionSeenIds` field tracks Part 5 question IDs so vocabulary-mode history cannot suppress unattempted Part 5 questions.
- Added the runtime selector and question bank to the Service Worker app shell for offline precache; added focused Python/Node tests and CI wiring. IndexedDB remains v1; no learner profile reset or migration.
- The 35 items are original practice content, not ETS questions and not part of the 200-question Reading Mock bank. All remain reserve-pending-independent-review until a second reviewer records approval.
- Local targeted checks cover bank integrity, unique blanks/choices/keys, option-explanation alignment, question cycling, Focus Workspace integration, progress persistence and PWA app-shell paths. Eight pre-existing missing Part 1 JPG warnings remain. Remote GitHub Actions/Pages and physical-device QA are not claimed.
- Detailed record: `batches/TOEIC_PART5_SENTENCE_COMPLETION_v2.38.0.md`; verification: `reports/TEST_REPORT_TOEIC_Dictionary_v2.38.0.md`.

## v2.37.0 — Vocabulary Family Link Expansion (2026-11-14)

- Added 39 curated derivational relationships between existing TOEIC headwords, creating 77 new reciprocal/sense-linked family references while preserving the pre-existing reservation→reserve/reserved links.
- Expanded non-empty `word_family` coverage from 131 to 207 of 992 headwords (13.2% → 20.9%); the dictionary now contains 292 family links. The 992-headword inventory and all stable IDs remain unchanged.
- POS labels and Vietnamese glosses are drawn from the linked headword's matching sense. A focused regression suite checks bidirectional links, POS/gloss consistency, no duplicate family terms and preservation of existing links.
- Updated the coverage report to expose both family-record coverage and total family-link count. CI now invokes the new family-link regression module.
- No Listening/Reading/Grammar, Mock blueprint, TTS, PWA cache, IndexedDB or learner-profile behavior changed. This is a targeted vocabulary metadata improvement, not a full independent lexical review.
- Detailed record: `batches/TOEIC_VOCABULARY_FAMILY_LINKS_v2.37.0.md`; local checks: `reports/TEST_REPORT_TOEIC_Dictionary_v2.37.0.md`.

## v2.36.0 — Listening Reserve Author Pass & Evidence Refinement (2026-11-14)

- Completed an internal author pass across all 34 Batch 015 Listening units (70 questions) and corrected three specific weaknesses in Part 2 response wording and Part 3 answer/evidence completeness.
- Updated the warehouse-label response to a complete status statement; expanded the Brightline quotation evidence to cover both delivery time and installation; clarified the customs-invoice transcript/key to include quantities for each product code.
- Kept all 34 Batch 015 units in `reserve-pending-independent-review`; the total 98-question Listening reserve pool remains excluded from Mock.
- Stable resource/question/choice IDs and option order are preserved. No content inventory, scoring or IndexedDB schema change.
- Carried forward v2.35.0 TTS multi-speaker fallback and CI test-coverage improvements.
- Detailed record: `batches/TOEIC_LISTENING_RESERVE_AUTHOR_PASS_v2.36.0.md`; local checks: `reports/TEST_REPORT_TOEIC_Dictionary_v2.36.0.md`.

## v2.35.0 — Runtime Quality & CI Coverage Hardening (2026-11-14)

- Fixed multi-speaker TTS voice selection so the preferred Daniel (en-GB) voice is not reused for a second male speaker when another male voice is available; explicit manual voice settings retain priority.
- Added a CI coverage guard that requires every Python regression module and JavaScript regression suite to be declared in the GitHub Actions workflow.
- Added the previously omitted Part 7 editorial regression module and Flashcard image-policy JavaScript suite to CI.
- CI wiring now covers all 24 Python test modules and 7 JavaScript regression suites. Local coverage checks do not equal a remote GitHub Actions run.
- No content-bank, stable ID, mock blueprint, IndexedDB schema or learner-profile changes.
- Detailed implementation: `batches/TOEIC_RUNTIME_QUALITY_HARDENING_v2.35.0.md`; local checks: `reports/TEST_REPORT_TOEIC_Dictionary_v2.35.0.md`.

## v2.34.0 — Listening Expansion & Final Learning Readiness (2026-11-14)

- Added 70 original reserve questions in Batch 015: Part 2 +16, Part 3 +11 conversations/33 questions, Part 4 +7 talks/21 questions. Listening library grows 130 → 200 questions / 106 units.
- The Mock-eligible pool remains 102; 98 questions (Batch 013=11, Batch 014=17, Batch 015=70) stay reserve-pending-independent-review until a second human reviewer approves them. They are available for normal Listening practice but excluded from Mock.
- Mock selector now allows established legacy status-less content, existing v2.33 `internal-editorial-reviewed` Reading resources and explicit `approved-for-mock`; reserve and unknown statuses fail closed. Whole Part 3/4 blocks remain indivisible.
- Mock landing page shows eligible, pending and projected Listening counts by Part plus the four-item Part 1 shortfall for two zero-repeat Full forms after all reserve approvals.
- Added Listening expansion/source-pointer tests, a static PWA app-shell audit and a generated Listening readiness report. Static PWA checks do not represent real-device offline QA.
- No vocabulary, Reading, Grammar, retry/attempt-history or IndexedDB schema changes. Preserve all user-owned Part 1 JPGs; this snapshot still lacks 8 JPG binaries.
- Detailed record: `batches/TOEIC_LISTENING_EXPANSION_BATCH_024_v2.34.0.md`; release gates: `reports/TEST_REPORT_TOEIC_Dictionary_v2.34.0.md`.


> The single chronological release log. Detailed implementation records live only for the previous/current release pair in `batches/` and `reports/`. Older releases are summarized here and in `archive/PROJECT_HISTORY.md`; do not create duplicate changelogs.

## v2.33.0 — Reading Expansion & Mock Exam Quality (2026-11-14)

- Expanded Reading from 35 resources / 109 questions to 51 resources / 200 questions: Part 5=60, Part 6=32, Part 7=108 (58 single-passage / 50 multiple-passage).
- Added six Part 5 sets (30 questions), four Part 6 texts (16 questions), four new Part 7 single passages (14 questions), one double-passage set (5) and one triple-passage set (5). Appended 21 questions to existing Part 7 resources without reordering or replacing old question indexes.
- Part 6 texts remain indivisible four-question blocks; Part 7 single passages remain complete 2–4 question blocks; all 10 double/triple resources contain exactly five questions and their required 2/3 documents.
- Added sourceLabels + exact source quotations to 45 new Part 7 questions. Evidence audit verifies every quote occurs in the document carrying its referenced label.
- Balanced six new Part 7 keyed positions with keyed-option swaps and stable `choiceIds`; new items A/B/C/D=11/11/11/12 and full Part 7=27/27/27/27. Mapping is `tools/answer-position-balance-v2.33.0.json`.
- Updated Mock sampling for complete Part 6/7 blocks. Quick/Half/Full modes remain 25/100/200 questions; regression verifies two consecutive non-overlapping 100-question Reading forms. Listening has only 102 eligible questions, so the second Full Listening section still reuses 98 questions; 28 reserves remain excluded pending independent review.
- No changes to 992 vocabulary records, 130 Listening questions, 33 Grammar lessons/86 exercises, retry/attempt-history semantics or IndexedDB v1. All Reading content is original project-authored material, not ETS questions.
- The 45 new Part 7 questions have explicit source references and structural checks; semantic distractor uniqueness still requires second-person review. No ETS/psychometric score equivalence is claimed.
- Local release checks: 67/67 targeted Python tests, six JavaScript runtime regression scripts, three syntax checks, data/content validators and version sync passed; eight missing Part 1 JPG warnings remain in the source snapshot. Remote CI/Pages and physical-device QA are unverified.
- Detailed record: `batches/TOEIC_READING_EXPANSION_BATCH_023_v2.33.0.md`; verification: `reports/TEST_REPORT_TOEIC_Dictionary_v2.33.0.md`.

## v2.32.0 — Listening Reserve Review & Expansion (2026-11-14)

- Completed internal source/key/rationale review of the 11 Batch 013 reserve questions; no key changes required. They remain reserve-pending-independent-review until a second human review occurs.
- Added 17 original Listening reserve questions in Batch 014: five Part 2 items, two Part 3 conversations (six questions) and two Part 4 talks (six questions).
- Listening grows from 113 to 130 questions: P1=8, P2=35, P3=48, P4=39. The active/mock-eligible pool remains 102; 28 reserves remain excluded from Mock.
- Release rotator keeps only previous/current UPDATE_NOTES and OVERLAY_MANIFEST files and consolidates history under one index heading. No Reading, Grammar, Vocabulary, IndexedDB or TTS behavior changed.
- Detailed record: `batches/TOEIC_LISTENING_RESERVE_BATCH_022_v2.32.0.md`; verification: `reports/TEST_REPORT_TOEIC_Dictionary_v2.32.0.md`.

## v2.31.0 — Grammar Expansion for TOEIC Part 5/6 (2026-11-14)

- Added eight original Grammar lessons and 32 exercises; library grows from 25 lessons / 54 exercises to 33 / 86.
- Added Part 5/Part 6 filters and shared Focus Workspace labels; preserved existing lesson/question/choice IDs and IndexedDB v1.
- Detailed record: `batches/TOEIC_GRAMMAR_EXPANSION_BATCH_021_v2.31.0.md`; verification: `reports/TEST_REPORT_TOEIC_Dictionary_v2.31.0.md`.

## v2.30.0 — Repeatable Practice & Vocabulary Batch 020 (2026-11-14)

- Added per-question/full-lesson retry for Reading, Listening and Grammar; history retains prior responses and latest analytics are separate from unique-question coverage.
- Added 13 headwords; vocabulary canonical total rises 979 → 992. IndexedDB v1 remains unchanged.
- Detailed record: `batches/TOEIC_VOCABULARY_BATCH_020_v2.30.0.md`; verification: `reports/TEST_REPORT_TOEIC_Dictionary_v2.30.0.md`.

## v2.29.0 — Shared Learning Workspace & Flashcard Single Scroll (2026-11-13)

- Standardized Flashcard, Review, Grammar, Reading and Listening details on one Focus Workspace and made it the only vertical scroll owner.
- Detailed record: `batches/TOEIC_SHARED_LEARNING_WORKSPACE_BATCH_019_v2.29.0.md`; verification: `reports/TEST_REPORT_TOEIC_Dictionary_v2.29.0.md`.

## Older release index

- **v2.28.0** — Vocabulary Batch 018; two-version rotation and history consolidation.
- **v2.27.0** — Focus learning workspace and Vocabulary Batch 017.
- **v2.26.0** — Flashcard image relevance and responsive card layout.
- **v2.25.0** — Timed TOEIC Mock Practice Beta.
- **v2.24.0** — Listening/TTS playback reliability hardening.
- **v2.23.0** — Part 1 photo QA and Listening reserve content.
- **v2.22.0** — Licensed Part 1 photo integration.
- **v2.21.0–v2.9.1** — See `archive/PROJECT_HISTORY.md` for the compact retired-document index.

The complete historical inventory and retired-note mapping is maintained in `archive/PROJECT_HISTORY.md`.
