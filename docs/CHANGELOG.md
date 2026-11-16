## v2.83.0 — Robot Buddy, progress-aware support and Service Worker validation repair

- Replaced the helper launcher with an animated robot icon and a responsive Robot Buddy panel. The usage guide and Quick Help vocabulary prefix/masked-letter search are removed.
- A first-time visitor is asked whether to complete the existing Placement Diagnostic or skip. The local onboarding choice is remembered; returning learners are identified from existing local learning evidence.
- Robot Buddy uses the device's existing study records to congratulate, summarize vocabulary/review activity, identify Reading/Listening areas for additional practice only after at least three unique answered questions, surface Foundation recall due, summarize A2 writing history and open existing practice destinations.
- Milestone notifications are tied to completed learner actions (practice streak, Flashcard quiz, Placement, Mock Exam, A2 writing revision). No generic AI-generated claims or invented mastery percentages are used.
- `assets/js/learning-assistant.js` is a deterministic local read-only summary module; it does not call Google, an API, a model or a backend. Legacy v2.79 feature-level Google AI actions and their preview/explicit external handoff remain unchanged and separate.
- `assets/js/quick-help.js` is a no-op compatibility tombstone. Both it and `learning-assistant.js` are listed in Service Worker `REQUIRED` and `APP_SHELL`, resolving SW002 for the two asset paths while safely overwriting stale files in older GitHub checkouts.
- Added only `toeic:robot-companion-onboarding:v1`; no IndexedDB migration, vocabulary/question changes, old progress reset or A2 portfolio schema changes.
- Preserved the accepted v2.80 Mock Exam icons (clipboard/check, bolt, stopwatch, trophy). Updated Master and archive documentation to keep one authoritative AI product contract and remove inaccurate feature claims.

## v2.82.1 — Quick Help cleanup

- Removed Quick Help prefix search, suggestions and masked-letter completion.
- Preserved the original v2.79 feature-level Google AI controls, A2 writing portfolio and Mock Exam SVG icons.

## v2.82.0 — restore existing feature-level actions

- Restored the original v2.79 feature-level Google AI controls after a temporary implementation regression in v2.81.0.
- No new shared assistant, contextual AI prompt or copy/transfer integration was introduced.
- Preserved the A2 writing portfolio, response revision history and Mock Exam SVG icons.

## v2.81.0 — A2 writing portfolio

- Added the local A2 writing portfolio and first-to-latest self-rating view using the existing Foundation progress store.
- A temporary regression hid some existing Google AI controls; the original v2.79 behavior was restored in v2.82.0.

## v2.80.0 — Mock Exam icon refresh

- Replaced the old clock glyph with the accepted Mock Exam SVG icon family: clipboard/check, bolt, stopwatch and trophy.
- The only Google AI functionality in the product remains the original feature-level controls from v2.79; no shared assistant/contextual AI handoff is part of the accepted product scope.

## v2.79.0 — A2 guided writing revision and response history

- Added a task-specific guided revision workspace to all 13 A2 contextual production tasks. Each lesson has three review checks and a tailored revision hint; learners compare the prior response, confirm each requirement was reviewed, write a distinct revision and self-rate the existing three criteria.
- New production attempts retain their response text. Each guided revision stores `basedOnResponse`, revised `response`, three review confirmations, three learner self-ratings, word count and timestamp. A revision must meet the eight-word minimum, differ from the prior text and include all required review and self-rating fields.
- First responses and successive versions remain in the existing `productionEvidence` map and `toeic:foundation-progress:v1` localStorage key. Existing `::produce1` and legacy `::apply1` IDs remain unchanged and isolated.
- Historical v2.78.0 attempt rows did not store response text. They are preserved as-is; no missing historical response is fabricated. The last currently stored response is used as the starting point for the next revision.
- Added an immutable SHA-256 baseline for all 13 revision guides and regression tests for task-specific guidance, first-response capture, multiple revisions, response-chain linkage, validation gates and legacy-data isolation.
- No automatic AI/grammar grading, server upload, new dependency, IndexedDB migration, learner-progress reset, vocabulary change or Reading/Listening bank change. Revision ratings are learner self-reports, not a proficiency or mastery certificate.
- Local test and validator results are recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.79.0.md`. Remote GitHub Actions, GitHub Pages deployment and physical-device QA remain unverified.

## v2.78.0 — A2 contextual writing tasks and separate production evidence

- Added 13 original, lesson-specific learner-authored writing tasks across the 13 guided A2 lessons. Every task includes a workplace scenario, instruction, three content requirements, a sentence frame, three tailored self-check criteria and one collapsed model-answer example.
- Set an eight-word minimum for A2 contextual production responses and added a live word counter. Pre-A1/A1 production retains its existing three-word minimum and generic self-report rubric.
- Added the `productionTask` resource contract and new stable task IDs (`<lesson-id>::produce1`). These use the existing `productionEvidence` map inside `toeic:foundation-progress:v1`; no new localStorage key or server endpoint is introduced.
- Preserved the earlier A2 production records under their old `applicationTask` IDs (`::apply1`). They are not deleted or overwritten, but are no longer counted as completion of the new contextual writing task; the UI explains this distinction. The current A2 production outcome now reads only the dedicated `::produce1` records.
- Added an immutable SHA-256 content baseline for all 13 A2 production tasks and regression coverage for task structure, min-word validation, customized rubrics, collapsed model answers, evidence isolation and preservation of legacy records.
- No IndexedDB database/store/version migration, no Foundation localStorage key change, no vocabulary or Reading/Listening question change, no learner profile reset, and no TOEIC Mock-pool change.
- Local regression and validator counts are recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.78.0.md`. Remote GitHub Actions, Pages deployment, real-device QA and independent second-person linguistic review remain unverified.
- Production evidence remains learner self-report. The application does not automatically grade grammar or writing quality and does not certify CEFR level or mastery.

## v2.77.0 — A2 assessment quality and source-evidence pass

- Reviewed the 13 A2 Reading passages and 13 A2 Listening dialogues for repeated q2/q3 information. Reworked five question prompts/answer tasks across quantities, comparisons, visitor obligations and process sequencing so each resource tests distinct information.
- Added exact `evidenceText` source pointers to five reviewed questions. The new audit checks these strings against the actual passage or spoken segment, and verifies four unique choices, valid answer indices, non-empty prompts/rationales, distinct q2/q3 answer keys, stable IDs and full-bank answer-position balance.
- Kept all existing A2 q1/q2 question objects unchanged against the canonical v2.75.0 hash baseline; preserved existing lesson/resource/question IDs, progress stores, answer positions (A/B/C/D = 15/15/15/14), TTS behavior and 67% A2 practice threshold.
- Added `tools/audit-foundation-a2-assessment.py`, its focused review registry and eight Python regression tests; CI now runs both the tests and standalone audit.
- This is a focused internal single-author quality pass, not full semantic approval of all distractors, second-person language review, psychometric validation, CEFR certification or ETS equivalence. Remote CI, Pages deployment and physical-device QA remain unverified.

## v2.76.0 — A2 Reading & Listening depth expansion

- Expanded all 13 A2 Reading passages to 69–80 words and added one distinct third comprehension question per passage. The previous q1/q2 IDs, choices, answer keys and rationales are preserved byte-for-byte at the canonical question-object level; all 10 Pre-A1/A1 passages remain unchanged.
- Expanded all 13 A2 Listening scripts into four-turn dialogues (two female and two male speaker turns) and added a third comprehension question per dialogue. Playback uses the learner's saved/configured male and female device voices, retains the configured inter-speaker pause, exposes a Stop action and reports playback status. Legacy Pre-A1/A1 scripts without explicit speaker segments continue to play through sentence-splitting fallback.
- Foundation Reading and Listening now each contain 23 resources / 59 questions: 20 questions for the 10 Pre-A1/A1 resources and 39 questions for the 13 A2 resources. A2 requires 3 unique questions and uses a 67% local practice threshold; Pre-A1/A1 remains at 2 questions and 80%. These thresholds are not CEFR certification or mastery.
- Added an exact v2.75.0 question-pair baseline and regression checks proving all pre-existing A2 q1/q2 content and all Pre-A1/A1 records remain intact. Answer positions across each Foundation Reading/Listening bank are balanced A/B/C/D = 15/15/15/14.
- No vocabulary records, Foundation lesson/application IDs, learner progress key, IndexedDB v1 schema/store, personal vocabulary, settings or TOEIC L&R Mock pools were reset or migrated. No new dependency or audio asset was added; Listening audio remains device SpeechSynthesis, not ETS or recorded native-speaker audio.
- Local validation and exact test counts are recorded in `archive/PROJECT_HISTORY.md` (tài liệu release cũ đã được gom vào lịch sử). Remote GitHub Actions, Pages deployment, independent language review and physical-device audio/visual QA remain unverified.

## v2.75.0 — A2 core grammar expansion

- Added Present Perfect, basic Passive Voice and defining Relative Clauses as three A2 guided lessons; each includes teaching notes, bilingual examples, three recognition checks and a contextual-application task.
- Added three matching short Reading passages (6 questions) and three matching device-TTS Listening scripts (6 questions). Foundation totals: 23 lessons, 23 Reading passages/46 questions and 23 Listening scripts/46 questions.
- Expanded `foundation-a2` mapping to 13/13; objective-resource map now 294/294 across 11 objectives.
- Preserved all previous content IDs, answer keys, vocabulary, Foundation progress keys, IndexedDB v1 and existing learner data. Only new A2 records were added; comparison against v2.74.0 passed 52/52 prior-data preservation checks.
- Local validation: **131 selected Python tests across 19 modules and 22/22 JavaScript regression suites PASS**; vocabulary data 1,137 records / 0 errors / 0 warnings; learning-content 0 errors / 0 warnings; Part 1 photos 9/9; objective-resource links 294/294; outcome audit 11/11 objectives / 33 criteria; design-profile and version sync PASS.
- Local candidate only; independent A2 language review, remote CI, Pages deployment and physical-device QA remain pending. See `archive/PROJECT_HISTORY.md` (tài liệu release cũ đã được gom vào lịch sử).

## v2.74.0 — Foundation Outcome Instrumentation

- Instrumented Foundation recognition on stable per-question evidence without changing the unique-question denominator.
- Added 24-hour first recall scheduling and 1-day / 3-day retry intervals. Due recall is separate from recognition and cannot be recorded early.
- Added learner-authored sentence production with three explicit self-report checks; responses are stored locally and are not automatically graded.
- Added separate Pre-A1/A1 and A2 outcome dashboards. Foundation instrumentation coverage is 6/6; the complete outcome registry has 6/33 criteria with evidence paths (18.2%). No mastery or CEFR/ETS claim is made.
- Preserved the existing Foundation localStorage key and IndexedDB v1. No learner progress reset, schema migration, stable question ID change or vocabulary content change.
- Re-synchronized the canonical design profile and release markers.
- Validation: 22/22 JavaScript suites; 129 selected Python tests across 19 executed modules; all current structural, learning-content, strict Part 1 media, resource-map, outcome, design-profile and version checks pass. Remote CI/Pages/device QA remain unverified.

## v2.73.0 — A2 guided pathway starter expansion

- Extended the guided Foundation pathway from Pre-A1/A1 to a first A2 starter stage: 10 new A2 lessons with stable IDs, concise explanations, bilingual examples, three recognition checks and one separate contextual-application task per lesson.
- Added 10 A2 short-reading passages with two questions each and 10 A2 short-listening scripts with two questions each. Listening uses device SpeechSynthesis; it is not ETS audio or recorded native-speaker material. Reading/listening banks remain separate from TOEIC L&R Mock pools.
- Expanded the canonical objective-resource map to **11 objectives and 291/291 linked resource records**; the outcome registry now defines 33 criteria across 11 objectives. Foundation recognition/application progress remains separate from TOEIC objective evidence; production/retention outcomes are not yet instrumented.
- Added profile-safe, additive A2 IDs and preserved the prior Pre-A1/A1 lesson IDs, Reading/Listening IDs, answer keys, personal vocabulary, IndexedDB database/store/version and existing learner progress keys. No IndexedDB schema migration or data reset was introduced.
- Corrected an A2 suggestion example to the natural form “Why don't we meet after lunch?” and added a regression assertion for the accepted sentence and rationale. Balanced the A2 answer-key positions: recognition 8/8/7/7, contextual application 3/3/2/2, and Reading/Listening 5/5/5/5.
- Updated project progress reporting: 3/6 guided stages represented (**50.0%**), 291/291 objective-resource links and 33/33 outcome criteria defined. These are structural coverage measures, not full A2 completion, independent editorial approval or learner mastery.
- The 1,137-word vocabulary inventory and optimized 9/9 Part 1 4:3 JPEG assets remain unchanged. Part 1 strict validation continues to pass.
- Local verification: **306 Python tests passed across 42 fully executed modules**, **21/21 JavaScript regression suites**; vocabulary, learning-content, objective-resource and learning-outcome audits passed. The slow generic `test_validator.py` module was not counted because its full run did not finish within the execution window. Remote GitHub Actions, Pages deployment and physical-device QA remain unverified.
- The A2 content still requires independent linguistic/editorial review. The current A2 block is a starter stage, not the full A2 curriculum: present-perfect introduction, passive/relative clauses and wider four-skill assessment remain future work.

## v2.72.0 — embedded and optimized complete Listening Part 1 photo set

- Added all nine Part 1 JPG files directly to `assets/listening/` from the user-provided `Picture.zip`; no AI-generated or substitute images were created.
- Standardized every photo to **1448×1086 px (4:3 landscape)**, matching the shared design-system frame. `part1-photocopier.jpg` is now a landscape crop that keeps the employee's operating hand and the photocopier control panel in frame; no distortion is applied.
- Kept every image under **400,000 bytes**. The existing `part1-office-cleaning.jpg` remains byte-for-byte unchanged at 398,363 bytes. The other eight photos are optimized progressive JPEGs. Combined image payload is 2,063,272 bytes, down from 25,265,159 bytes (**91.8% smaller**).
- Extended strict Part 1 validation to enforce minimum 1280×960, 4:3 landscape ratio and the 400,000-byte ceiling. Strict validation now passes **9/9 photos**; Learning Content validation reports **0 errors / 0 warnings**.
- Removed the old `restore-part1-photos.bat` downloader shortcut and its helper/test from the current release. That utility previously downloaded full-resolution Pexels originals; it did not compress or attach photos. It is no longer needed because optimized images are embedded in this full-source archive.
- Question IDs, transcripts, answer choices, answer keys, explanations, image filenames and attribution/license records remain unchanged. Removed the per-image photocopier CSS focal override because the source asset is now prepared to the shared 4:3 frame.
- Local verification is recorded in `archive/PROJECT_HISTORY.md`. Remote GitHub Actions, Pages deployment and physical-device QA are not claimed unless separately confirmed.

## v2.71.0 — Contracts and Facilities vocabulary expansion; one-command original photo recovery

- Added Vocabulary Batch 012 with 37 original TOEIC headwords covering Contracts, Legal Procedures and Facilities Management. The canonical A–Z inventory increases from 1,100 to 1,137 stable headwords. Every new entry has an English definition, Vietnamese gloss, one bilingual context example, at least three collocations and a sense-level editorial CEFR estimate. Independent lexical/CEFR review remains pending; none is official ETS material.
- Added 35 conservative US IPA entries from exact single-pronunciation CMUdict matches. `ventilation` remains blank because CMUdict has multiple pronunciations. `dispute` is also withheld pending syllabification review instead of using a mechanically generated transcription with uncertain syllable division. Cumulative IPA ledger: 333 source-linked records; 93 vocabulary records remain without populated IPA (91 inherited unresolved records plus these two Batch 012 exceptions).
- Added five reciprocal word-family pairs: enforce/enforcement, janitor/janitorial, accessible/accessibility, occupy/occupant, and alter/alteration. Cumulative word-family records: 276; directed links: 374. No speculative synonyms or antonyms were added.
- Extended release-repair profiles so workspaces at 979, 992, 1,026, 1,063 and 1,100 base headwords can restore only the known cumulative release additions through Batch 012. Learner progress, personal vocabulary, study settings, question IDs, answer keys and IndexedDB stores remain untouched.
- Added `tools/restore_part1_photos.py` and `restore-part1-photos.bat`. They fetch all eight original licensed Pexels photos in one operation using the filenames and direct URLs already recorded in `assets/listening/ATTRIBUTION.csv`, validate JPEG signature/dimensions, and never generate substitute images or overwrite existing files. The current build environment still cannot access the Pexels CDN and the saved Library does not contain the eight original image bytes; therefore the eight JPGs are **not yet embedded** in this release archive. Strict photo validation remains blocked until the originals are available and restored.
- Vocabulary target coverage: 1,137/3,000 minimum = 37.9%; 1,137/5,000 planning ceiling = 22.7%. US IPA field coverage: 1,044/1,137 = 91.8%; word-family coverage: 276/1,137 = 24.3%. These are target/field coverage ratios, not a single overall product-completion percentage.
- Local verification is reported in `archive/PROJECT_HISTORY.md`. Remote GitHub Actions, Pages deployment and physical-device QA are not claimed unless separately confirmed.

## v2.70.0 — Customer Service and Travel vocabulary expansion; IPA coverage counter correction

- Added Vocabulary Batch 011 with 37 original TOEIC headwords across Customer Service and Travel, increasing the canonical dictionary from 1,063 to 1,100 entries. Each new record includes an English definition, Vietnamese gloss, a contextual bilingual example, at least three collocations, a sense-level editorial CEFR estimate, and one US IPA candidate sourced from a single exact-match CMUdict pronunciation.
- Added four reciprocal, POS/sense-checked word-family pairs: cancel/cancellation, resolve/resolution, responsive/responsiveness, and troubleshoot/troubleshooting. No speculative synonyms or antonyms were added.
- Cumulative CMUdict ledger now contains 298 source-linked entries. The original 91 unresolved IPA records from the v2.69 base remain blank; no IPA is guessed. Current US IPA population is 1,009/1,100 (91.7%).
- Vocabulary quantity coverage increases to 1,100/3,000 (36.7%) and 1,100/5,000 (22.0%). These are quantity ratios only, not quality, CEFR mastery, or an overall product-completion percentage.
- Fixed the validator's IPA missing counter so absent `phonetic` objects and missing/non-string `us` values count as missing. Added regression coverage for both forms.
- Extended migration-repair profiles to recognize the 1,063-word v2.69.0 snapshot and cumulatively restore the exact known release additions without changing unrelated local deletions or learner progress.
- No IndexedDB schema/store migration, learning-question IDs, answer keys, user progress, personal vocabulary, or study settings were reset. Independent lexical review remains pending; CMUdict-derived IPA is not independently pronunciation-certified.
- Strict Part 1 photo validation remains blocked by eight missing repository-owned original JPG binaries. Remote GitHub Actions, Pages deployment and physical-device QA are not claimed.

## v2.69.0 — US IPA coverage backfill and word-family quality pass

- Added **261 US IPA entries** for exact headword matches with a single CMUdict General American ARPABET pronunciation and a single primary stress. CMUdict provides ARPABET, not IPA; the project uses a documented, deterministic broad-GA conversion. The source warns that its entries may contain errors or inconsistencies, so these remain source-linked editorial candidates rather than independent pronunciation certification. Provenance, raw ARPABET, conversion rules and exclusions are recorded in `reports/CMUDICT_IPA_BACKFILL_v2.69.0.json`; the CMUdict data license is retained in `docs/licenses/CMUdict-DATA-LICENSE.txt`.
- Increased US IPA field coverage from 711/1,063 (66.9%) to **972/1,063 (91.4%)**, a gain of 261 records / 24.5 percentage points. The remaining 91 entries stay blank by design: 60 have multiple CMUdict pronunciations, 25 have no exact entry, and 6 have multiple primary-stress patterns. No IPA was guessed for excluded items.
- Expanded word-family metadata from 240 to **259 headwords** and from 338 to **357 directed links** (+19). Added reciprocal, POS/sense-aligned relationships; corrected the Vietnamese gloss for the `transaction → transact` link without changing IDs.
- Added deterministic `tools/cmudict_ipa.py`, an embedded source/provenance ledger, a license notice and five focused tests. CI now runs the IPA ledger check and test module. Progress reporting now includes word-family directed-link counts.
- Vocabulary remains **1,063/3,000 = 35.4%** of the minimum planning target and **1,063/5,000 = 21.3%** of the planning ceiling. This release improves metadata quality and does not add new headwords. Next planned content batch remains Customer Service, Travel, Contracts and Facilities after review of the 91 IPA exceptions.
- No vocabulary stable IDs, question IDs, answer keys, IndexedDB schema/stores, personal vocabulary, hidden-word state or learning progress were reset.
- **Local verification:** vocabulary validator 1,063 records / 0 errors / 0 warnings; CMUdict IPA ledger check PASS (261 source-linked records); focused CMUdict IPA tests 5/5; word-family-link tests 5/5; project-progress tests 4/4. Full test and asset status are recorded in `archive/PROJECT_HISTORY.md`.
- CMUdict is a source dictionary and may contain errors, omissions or inconsistencies; the conversion and single-pronunciation filter reduce ambiguity but do not constitute human independent lexical review. CEFR labels remain editorial estimates. Remote GitHub Actions, GitHub Pages and physical-device QA are not claimed. Strict Part 1 photo validation remains blocked by eight original JPG binaries absent from this source workspace.

## v2.68.0 — verified Part 1 fingerprint refresh and TOEIC Vocabulary Batch 010

- Fixed the remaining-content fingerprint CI failure by recording the approved removal of the legacy Part 1 SVG `image` metadata field. All eight historic unit hashes are reproducible by restoring the exact old SVG path; all question hashes remain unchanged. Added a second fingerprint refresh audit entry and fail-closed verification.
- Added 37 stable vocabulary headwords in Batch 010 for manufacturing, production operations, quality assurance/control, maintenance, warehouse operations and supply chain. Total rises 1,026 → **1,063** (+37; 35.4% of the 3,000 minimum target, 21.3% of the 5,000 planning ceiling).
- All 37 entries include definitions, Vietnamese glosses, original bilingual examples, at least three collocations and editorial US IPA. Added five reciprocal word-family pairs. CEFR is editorial-estimate; independent lexical review remains pending.
- Updated legacy hidden-word repair profiles: 979→84 known additions, 992→71, 1,026→37. Only exact matching historical snapshots can trigger a restore; no IndexedDB schema change or reset.
- Strict Part 1 photo validation remains blocked because this source snapshot contains only 1/9 original JPG binaries. Keep the eight repository-owned JPG originals when merging; deployment remains on hold until strict validation reaches 9/9.

## v2.67.0 — JPG-only Listening media and TOEIC Vocabulary Batch 009

- Removed the redundant public UI label “Nội dung bổ sung · đang chờ kiểm duyệt độc lập · chưa dùng trong Mock Exam”. The underlying `editorialStatus=reserve-pending-independent-review` metadata and fail-closed Mock exclusion remain intact; this is a presentation cleanup, not an approval or content-promotion change.
- Converted all nine Listening Part 1 records to a strict JPG-only contract: each unit uses `photo`, no unit declares the legacy `image` SVG fallback, runtime and Mock rendering no longer contain SVG fallback behavior, and the eight obsolete `assets/listening/part1-*.svg` files were removed from the source. Service Worker Part 1 entries are JPG-only; unrelated application/topic SVG icons remain untouched.
- Added Vocabulary Batch 009 with 34 stable headword IDs focused on finance, legal/compliance, procurement, HR and logistics. Canonical A–Z vocabulary grows from 992 to **1,026 headwords** (+34; 34.2% of the 3,000 lower-bound planning target). Each new entry includes an English definition, Vietnamese gloss, original TOEIC-context example and three collocations; all CEFR labels remain editorial estimates.
- Added 32 editorial US IPA transcriptions derived from CMUdict General American ARPABET where a stable single reading was selected; two entries remain blank pending dictionary-level confirmation. Added 11 reciprocal, POS/sense-matched word-family relationships to existing canonical headwords. No unsupported synonyms/antonyms or verb forms were invented.
- Added cumulative legacy migration repair profiles for devices whose old hidden-word snapshot was based on either 979 or 992 canonical headwords. The repair restores only the exact known additions for a matching historical fingerprint; unrelated user-hidden IDs and personal data remain untouched. No IndexedDB schema/store migration was added.
- Local validation: 117/117 selected Python tests and 21/21 JavaScript regression suites; vocabulary validator 1,026 records / 0 errors / 0 warnings; learning-content validator 0 errors / 8 warnings for missing original JPG bytes in this inherited workspace; focused JPG-only, PWA, learning-content, vocabulary family, example, progress and legacy-collocation suites passed. Strict photo validation remains blocked at 1/9 local JPG binaries; restore the eight repository-owned JPGs before deployment.
- Independent lexical review of Batch 009 remains pending. Automated checks and internal author review do not qualify as independent approval. Remote GitHub Actions, Pages deployment and real-device visual/audio QA are not claimed.

## v2.66.1 — fixed Listening Part 1 pacing and GitHub test correction

- Standardized every Speech Synthesis route on a fixed **2,000 ms** engine-preparation buffer after voice-catalog readiness and cleanup. The delay is no longer configurable, preventing different settings from making practice and exam audio behave differently.
- Listening Part 1 now speaks the topic header (`Part 1: [Topic]`, e.g. `Part 1: Warehouse & Shipping`), waits **1,000 ms**, speaks `Now, listen to the four statements.`, waits **1,000 ms**, then speaks each option label (`A.`, `B.`, `C.`, `D.`) as its own utterance. Each label is followed by a fixed **1,500 ms** pause before its description; descriptions are separated by **1,300 ms**.
- Practice and Mock Exam use the same Part 1 pipeline. The Mock Exam no longer speaks an extra generic transition before Part 1; the shared player owns the full topic → lead-in → A–D sequence. Parts 2–4 retain their existing segment/turn handling, with the new fixed 2-second startup readiness.
- The Practice transcript now includes the spoken topic header, lead-in and option labels. Mock audio guidance describes the same fixed timing. The timing controls were removed from Settings so users cannot accidentally create divergent schedules.
- Fixed the GitHub Actions failure in `test_distractor_quality.py`: an old assertion expected `recordPracticeAnswer()` to run immediately on selection. Since the v2.66.0 assessment contract intentionally stages choices and commits them only after the complete-set confirmation, the test now asserts `stagePracticeChoice()` on selection and `commitPracticeDraftSet()` after confirmation. No application scoring behavior was weakened or reverted.
- The long escaped `app.js` fragment in the Python traceback was the unittest representation of the source string in `AssertionError`, not escaped/corrupt JavaScript. The Google URL builder remains `new URL('https://www.google.com/search')`; Node syntax checks pass.
- Preserved Listening question text, answer keys, explanations, stable IDs, answer history, personal vocabulary, existing IndexedDB stores, voice selections, rate, pitch and volume. Legacy saved timing keys are ignored; no data reset or schema migration was added.
- Local verification: 21/21 JavaScript regression scripts PASS; 85/85 selected Python tests PASS across 10 modules; `test_tts_readiness.py` 13/13; `test_distractor_quality.py` 6/6; `test_ci_coverage.py` 2/2; version/design sync and syntax checks PASS; vocabulary validation 992 records / 0 errors / 0 warnings; learning-content validation 0 errors / 8 original JPG warnings. The strict Part 1 photo validator still fails because 8/9 original JPG binaries are present in the inherited source archive; keep the release hold.
- Real audible timing on Windows, iOS/iPadOS and Android, remote GitHub Actions, and GitHub Pages deployment remain unverified from this workspace.

## v2.66.0 — assessment summary-before-review and guided mock flow

- Balanced dashboard progress into full-width exam/skill rows; TOEIC Listening and Reading no longer compete in one uneven 4-Part/3-Part grid. The structure is extensible to Writing, Speaking and IELTS.
- Deferred correctness and explanations until a complete set is answered and the learner confirms the summary. Applied to Grammar, Reading, Listening, Foundation, Placement, Flash Quiz and single-question Smart Review/Part 5.
- Added a shared completion modal with correct/incorrect/total counts and a restrained bottom-up confetti animation. Existing answers, explanations and history are committed/opened only after confirmation.
- Mock Exam shows no correct/wrong feedback while in progress. Manual submission or timeout moves to a persisted pending summary; confirming opens the detailed answers, transcripts and explanations. Pending summaries survive reload and do not enter completed history until confirmed.
- Timed Mock Exam now reserves lead-in time within the overall 15/60/120-minute schedule and automatically advances focus across all Listening/Reading questions. A spoken transition identifies the current Part/question; Listening audio is replayed only when entering a new group, not on every sub-question in the same dialogue.
- Added `assessment-deferred-workflow.mjs`; updated mock guided-flow tests for section-local question numbering. Added `mock-flow.js` to the Service Worker required/app-shell cache.
- Preserved prior progress and IndexedDB schema. Validation is local only; physical device playback/visual rendering and remote GitHub Actions/Pages are not verified. Eight inherited Part 1 JPG binaries remain absent from this workspace, so strict media validation continues to block deployment.

## v2.65.2 — TOEIC Part 1 lead-in and spoken A–D option sequence

- Added a shared Part 1 lead-in: “Now, listen to the four statements.” The lead-in is spoken after voice preparation and before option A.
- Listening Part 1 options are now spoken as separate, explicitly labeled utterances: “A. [description]”, “B. [description]”, “C. [description]”, and “D. [description]”. Existing source descriptions stay clean and are labeled at playback time; already-prefixed source text is normalized to avoid duplicated labels.
- Added a configurable pause after the lead-in and before A (default 1,000 ms; 800–1,800 ms). The existing 1,300 ms default pause between A/B/C/D remains independently configurable.
- Practice Listening and Mock Exam use the same `playListeningAudio()` pipeline, so lead-in, spoken labels, voice selection, startup readiness and A–D pacing are identical in both modes. The Mock Exam audio hint and practice transcript now expose the same order and labels.
- Part 1 clips with anything other than four descriptions are blocked with a clear message rather than silently reading an incomplete A–D sequence.
- Added regression tests for the lead-in, spoken A–D labels, transition gaps, stop-during-lead-in, transcript labels, configuration persistence, the nine current Part 1 units, and shared Practice/Mock playback.
- Existing question text, answer keys, explanation text, stable IDs, personal vocabulary, IndexedDB stores, learner progress and existing TTS voice/rate/pitch/volume settings remain unchanged. `part1LeadInPauseMs` is additive to `appSettings.tts`.
- Local source verification only. Device-specific audio pronunciation and timing still require real browser/device listening. The inherited strict Part 1 photo validator remains blocked by eight missing original JPG binaries in this archive; do not remove existing GitHub image assets when applying this update.

# TOEIC Dictionary — Changelog

## v2.65.1 — TTS voice-selector startup hotfix

- Fixed the v2.65.0 initialization crash `ReferenceError: refreshSpeechVoiceSelectors is not defined`. The helper was still invoked by `bindTtsSettings()` and `syncSettingsUI()` but its function declaration had been dropped during the TTS readiness refactor.
- Restored the shared voice-selector refresh helper. It repopulates English voice choices when the device exposes its voice catalog, keeps the learner's manually saved male/female voice URI, preserves a saved URI that is unavailable on the current device with a clear option label, and disables selectors while no English voice is available.
- The `voiceschanged` listener and manual refresh button continue to use the same helper. TTS playback readiness, startup delay, Part 1 A–D pause, saved settings and learner progress are otherwise unchanged.
- Added a source-level regression assertion and expanded the JavaScript TTS regression to execute the helper with an empty catalog, a populated catalog, a saved voice, and an unavailable saved voice.
- Local hotfix verification: 10/10 TTS Python checks and the Listening/TTS JavaScript regression pass after the fix. Full syntax/runtime and data checks are recorded in `archive/PROJECT_HISTORY.md`.
- No vocabulary content, stable IDs, IndexedDB schema/stores, local progress keys, or TTS preferences were reset or migrated. Existing saved voice URIs remain preserved.
- Deployment remains on hold until the eight inherited original Part 1 JPG binaries are restored and the strict photo validator passes. Real-device audio QA and remote GitHub Actions/Pages remain unverified.

## v2.65.0 — speech engine readiness, protected audio starts and Reading read-aloud

- Centralized every browser Speech Synthesis path behind one readiness sequence: wait briefly for the device voice catalog, clear residual pending/speaking work after cancellation, then apply a configurable pre-play buffer before the first real utterance. This is intended to reduce clipped initial phonemes/words when a voice engine is cold or an utterance has just been canceled; browser/OS behavior still needs physical-device verification.
- Listening playback now prepares the voice catalog before the first segment. TOEIC Listening Part 1 has a dedicated configurable 1.3-second default gap between answer descriptions A–D; other conversation/short-talk content retains the configurable turn pause. Per-lesson playback rate and manual voice selection are preserved.
- Vocabulary slow playback, flashcards, alphabet sound lab, Foundation Listening and word-pronunciation buttons now inherit the same startup preparation and safe cancellation logic through `speakText` / the shared utterance queue.
- Added Reading read-aloud for passage/document content and Part 5 question-choice sets. It uses the same prepared voice path, status announcements and Stop action; no reading or learner-progress records are changed.
- Added settings for startup preparation delay (default 750 ms) and Part 1 A–D option gap (default 1,300 ms). Legacy `appSettings.tts` objects receive these defaults additively; existing voice, rate, pitch, volume and pause settings remain intact.
- Added regression coverage for initially empty voice catalogs, delay-before-first-speech, Part 1 A–D spacing, reading passage playback, status updates, and the single guarded `speechSynthesis.speak()` call. The new Python design/integration checks are included in CI.
- No vocabulary, listening/reading content, stable question IDs, IndexedDB stores/schema, learner history or personal progress are reset. Only two additive TTS preference fields are introduced.
- Local source verification only. Device TTS output and iOS/Android PWA behavior are not guaranteed by mocked tests. The inherited strict Part 1 asset validator remains blocked by eight missing original JPG binaries; deployment remains on hold until those original assets are restored and strict validation passes.

## v2.64.0 — responsive composition, Part 1 media normalization and A–Z sound lab

- Standardized all Listening Part 1 images to a common 4:3 frame with `object-fit: cover`, consistent radius, frame width and caption. `part1-photocopier` now has a stable focal-point adjustment so the portrait source fills the same visual area as the other illustrations. The licensed JPG binary itself is not rewritten; the existing SVG fallback remains in the same shared frame.
- Balanced learning, Foundation, practice-mode, mock-exam and objective cards: equal grid-row height, title/copy baseline, common footer alignment, safe wrapping, minimum-width reset and non-clipping content. Long copy can expand a card/row; button labels wrap without overlap.
- Refined device-width behavior: alphabet sound lab uses 4 desktop / 3 tablet-landscape / 2 tablet-portrait-and-phone / 1 very narrow phone columns. Other learning cards keep two columns where space allows and one column at phone width. All breakpoints are CSS viewport based.
- Extended the existing Pre-A1 alphabet lesson into a 26-letter A–Z sound lab with letter names, example words, IPA, Vietnamese meanings, common focus sounds and two TTS actions per letter. Playback requests are recorded under the additive localStorage key `toeic:alphabet-sound-progress:v1`; this is exposure/interaction evidence only, not pronunciation accuracy, mastery, or free-speaking ability.
- Added the new alphabet data/helper to Service Worker REQUIRED and APP_SHELL; added Python and JavaScript tests. Added both Python test modules to CI execution after the coverage test exposed that they were only being syntax-checked, not run.
- Preserved every existing vocabulary/question/lesson stable ID, existing localStorage/IndexedDB schemas and learner progress. No destructive migration or data reset.
- Local verification only. The inherited archive still lacks eight licensed Part 1 JPG binaries; the strict photo validator remains enabled and blocks deployment until original files are restored. Browser/physical-device QA, remote GitHub Actions and GitHub Pages deployment are not claimed.

## v2.63.0 — Unified Design System & Design Profile

- Added canonical `design/design-profile.json` with 51 tokens and `tools/sync-design-profile.py` to synchronize both the token block and the generated legacy typography floor; CI checks drift in both.
- Consolidated cross-module typography roles, colors, component surfaces, buttons, controls, spacing, radii and shadows into a single visual contract. A 362-selector audit now raises every legacy fixed `px`/`rem` text rule below 12.5px across feature CSS and the old design-system prefix to the shared caption token; semantic content and control sizes are reasserted after the floor.
- Aligned Dashboard, Objective Tracker, Spaced Recall, Foundation, practice modes and the full TOEIC mock-test flow with the shared type and component hierarchy.
- Replaced the stale design guide with explicit rules, a new-module checklist and `docs/DESIGN_BRIEF_TEMPLATE.md` for owner preference selection.
- No vocabulary, IndexedDB or learner-progress data migration. Deployment remains held by eight inherited missing Part 1 JPG assets; remote CI/Pages/device QA pending.

## v2.62.0 — application-wide typography and Foundation Listening

- Audited the existing CSS cascade and added a shared application-wide typography floor. Main reading copy, card descriptions, objective-tracker evidence, practice-mode options, mock-test setup/results/review, form controls, captions and mobile navigation now use a consistent readable scale; large scores/timers retain their data hierarchy.
- Fixed the Foundation introduction layout by explicitly keeping the intro panel in one column; its content controls reflow separately on narrow viewports. Practice-mode and mock-test cards use content-first grids (auto-fit / tablet two-column / phone one-column) instead of squeezed fixed columns.
- Added a consistent type scale for Objective Learning Tracker cards, practice selection and TOEIC mock-test cards. Supporting metadata no longer uses the inherited 6–11px microtype styles for the audited reading surfaces.
- Added Foundation Listening for all 10 existing Pre-A1/A1 lessons: 10 original short workplace/everyday scripts, 20 stable multiple-choice comprehension questions, and balanced answer positions (5 each across A–D).
- Listening playback uses the learner's current browser/device Speech Synthesis voice settings. Transcript is hidden until requested. The UI and content metadata explicitly state that this is synthesized practice, not authentic ETS audio or a recorded TOEIC test.
- Added a separate `toeic:foundation-listening-progress:v1` ledger with stable question IDs, latest result and attempt history. Listening evidence is not merged with recognition, contextual application or reading evidence; retries do not add new unique-question IDs. Existing lesson progress and local data are preserved.
- Added the listening data and evidence helper to Service Worker REQUIRED and APP_SHELL; added Python/JavaScript tests and CI coverage.
- No vocabulary records, existing learning IDs, answer keys, IndexedDB schema/stores or existing localStorage progress keys were reset or migrated. Existing user data remains additive and separate.
- Local source verification only. Browser visual QA, remote GitHub Actions, GitHub Pages deployment and physical iOS/Android PWA behavior are not verified in this workspace. The inherited strict Part 1 photo-asset blocker remains: 8 original licensed JPG binaries are absent; restore them before deployment. SVG fallbacks remain available and the strict validator must remain enabled.

## v2.61.0 — Learning UI consistency and test integrity

- Fixed the false-positive scope test by isolating one top-level function at a time; the check continues to catch an actual `item.` reference inside `openGrammarLesson()` while allowing local callback variables in separate helpers.
- Re-verified the eight reviewed Listening Part 1 units. The old unit hash for each matched exactly after removing only `photoSourceType: "licensed-stock"`; all eight question hashes still match. Refreshed the eight `unitContentSha256` values and added `fingerprintRefreshLog` with old/new digests, scope and precondition results.
- Rebuilt the dashboard Spaced Recall queue using shared `panel`, `panel-header`, `learning-card`, shared count label and button styles. The human-facing card no longer prints internal stable question IDs; the ID remains bound to the correct review action.
- Rebuilt the Foundation learning-path overview with the same shared panels/cards, standard heading hierarchy and controls; increased body/status type sizes and made progress meter accessible.
- Added viewport-first responsive rules for the intro, cards and recall queue; no device-inch breakpoints or fixed-width-only layouts were introduced.
- Added CI coverage for the new learning-surface consistency test and the fingerprint refresh guard; expanded version synchronization checks to include `APP_RELEASE_VERSION`.
- No canonical learning content, question answer, ordering, stable IDs, personal data, IndexedDB schema or learner progress was changed/reset.
- Local verification only. The source ZIP inherited from v2.60.0 is missing 8 of the 9 licensed Part 1 JPG binaries; the strict asset validator run by CI therefore fails until those original Pexels files are restored. Exact recovery links are in `archive/PROJECT_HISTORY.md`. Do not deploy this candidate before the strict validator reports 9/9. GitHub Pages deployment and physical iOS/Android PWA presentation are not verified in this workspace.

## v2.60.0 — Vocabulary release integrity and PWA cache synchronization

- Fixed release/data mismatch risk: versioned `__release` query keys are used for the manifest and all JSON data requests, so an older Service Worker cache cannot silently return previous vocabulary files.
- Added runtime integrity gates: manifest version, per-letter counts, total word count, unique IDs and unique headwords must agree before the dictionary is rendered.
- Added a visible dashboard integrity line showing the validated GitHub base-dictionary count versus the manifest total, release version and personal additions separately.
- Service Worker update checks bypass HTTP cache; when an already-controlled PWA receives a new controller, it reloads once so HTML/JS/data are from one release.
- Kept canonical cache keys in the current versioned cache so precached data remains available offline; query strings are normalized only inside the current release cache.
- Preserved all 992 vocabulary records and existing stable IDs, personal vocabulary, IndexedDB schema and learner progress. No content count was fabricated or manually adjusted.
- Local source verification only; GitHub Actions, Pages and physical-device behavior remain unverified until deployed.

## v2.58.0 — Foundation contextual application evidence

- Added one stable contextual-application task to each of the 10 Pre-A1/A1 lessons (10 tasks).
- Application results and retry history are stored separately from recognition-question evidence; retries do not inflate unique recognition-question counts.
- Lesson detail explains that these are contextual multiple-choice checks, not free production or spontaneous communication.
- Preserved existing lesson/question IDs, `toeic:foundation-progress:v1`, legacy fields and IndexedDB schema.
- Local verification only; remote CI, GitHub Pages and physical-device QA are not claimed.

## v2.57.0 — Foundation learning evidence (Pre-A1/A1)

- Added 30 stable recognition/understanding checks across 10 lessons.
- Added unique-question evidence with latest-result accuracy and retry history.

## v2.59.0 — Foundation short reading comprehension

- Added 10 short reading passages (one per existing Pre-A1/A1 lesson) and 20 stable comprehension questions.
- Question skills cover locating explicit details and understanding simple purpose/context; passages are short, beginner-level workplace/everyday texts.
- Added separate reading evidence ledger `toeic:foundation-reading-progress:v1`, keyed by stable question IDs with latest result and attempt history. Retries do not inflate unique-question coverage.
- Local practice threshold: 2 unique questions and 80% latest-result accuracy. This is not CEFR certification or a broad reading-mastery claim.
- Added reading progress line to Foundation lesson cards and responsive passage styling.
- Added module/data to Service Worker REQUIRED and APP_SHELL for offline availability.
- Preserved existing lesson, recognition-question and contextual-application IDs; no IndexedDB schema migration or learner-data reset.
