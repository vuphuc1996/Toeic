## v2.95.66 — PWA release coherence and Batch 022 CI repair (2026-11-25)

- Reproduced the reported `app.js:2135:170` failure against repository history: the referenced `$('#modalBackdrop').addEventListener` call exists at that line/column in v2.95.64, while v2.95.65 HTML has only `modalLayer`. The browser was receiving stale cached app.js with the newer HTML shell.
- Added release query parameters to the app CSS, design-system CSS and app.js URLs in HTML. The same versioned URLs are included in Service Worker REQUIRED and APP_SHELL, preventing older worker cache entries from matching the previous app.js URL.
- Service Worker registration keeps the stable `./sw.js` URL and retains `updateViaCache: 'none'`; the versioned CSS/JS requests isolate app-shell cache keys without changing registration URL each release.
- Added a startup HTML/app release guard. When the meta release and JS release marker differ, the app displays a reload notice and returns before `bindEvents()`; this turns a future mixed-shell failure into an explicit release-coherence diagnostic.
- Fixed Batch 022's CI test: it now validates the actual `unittest discover` selector rather than requiring a source-path literal absent from the workflow.
- Updated PWA readiness and vocabulary validator SW001/SW002 checks to strip query parameters only for physical file lookup, preserving versioned cache keys. Added regressions proving existing versioned files pass and missing versioned paths still fail. Added a release-asset-coherence Node regression and registered it in GitHub Actions.
- No learning content, vocabulary IDs, canonical relations, question/choice/answer-key data, Mock eligibility or learner storage changed. UI layout and GitHub Pages-only architecture remain unchanged.
- Hosted Actions, exact package replay and physical-device cache/update acceptance remain pending the candidate PR run and post-merge testing.

- Hosted CI acceptance: 130/130 workflow steps PASS, 762/762 full Python tests PASS, and 44/44 Node regression scripts PASS. Data validator retained all 1,141 IDs with zero errors and zero new warnings. FullSource/Patch verification and real-device PWA acceptance remain separate pending gates.

## v2.95.65 — Batch 035 Cambridge historical tests and single modal overlay (2026-11-25)

- Replaced the stale split Cambridge Batch 035 test module that was present in the GitHub runner but absent from v2.95.64 FullSource. The compatibility suite now reconstructs the historical Batch 035 state from the current 567-row Related Glossary by reversing later additions/corrections and validates the original eight records, their exact source ledger, relation anchors and pre-batch file hash. It does not freeze the current glossary at 553 rows or compare the corrected `article` row with an obsolete pre-correction value.
- Preserved both Batch 035 test modules under the existing `test_related_glossary_batch_035*.py` selector. The exact GitHub Actions discovery command now selects 10 tests and passes locally.
- Removed the duplicate `modalBackdrop` full-screen element and `.modal-backdrop` styling. The existing `learningFocusBackdrop` is now the only dimming/blur surface; `modalLayer` is a transparent panel layer nested inside it. Modal-only mode hides the focus dialog, while a modal opened during focused learning leaves the active workspace intact.
- Unified modal show/hide/ARIA/body-scroll handling. Closing an ordinary modal hides the shared root; closing a nested modal preserves the active learning session. Modal layer `[hidden]` states use selector specificity instead of unnecessary `!important` declarations.
- Added a dedicated shared-overlay contract test and a fast GitHub Actions step. The modal-dismissal simulation verifies modal-only and active-focus modes, safe close behavior and no duplicate backdrop element. The design-token baseline identity was reconciled with the selector migration; the intentionally removed duplicate backdrop-background finding was retired.
- No glossary content, vocabulary IDs/headwords/relations, question/choice IDs, answer keys, learner IndexedDB records/schema, mock eligibility or Robot Buddy data boundaries changed. UI layout was not redesigned; no Cloudflare/backend or external data service was introduced.
- Local verification and known limitations are documented in `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.65.md`. Hosted GitHub Actions, Pages deployment, installed-PWA cache/offline and physical-device behavior remain unverified until a real repository push and device acceptance.

## v2.95.64 — GitHub commit-readiness and CI reliability hardening (2026-11-25)

- Added a dependency-free Git commit-readiness audit and a dedicated integration test suite. The check validates staged/clean Git state, case-insensitive path collisions, Windows-reserved names and characters, symlinks, large files, accidental release ZIP/checksum artifacts, expected `.gitignore` coverage, LF attributes and whitespace in the current commit/staged diff. It does not stage, commit or mutate Git state.
- Added `.gitattributes` rules to normalize text files to LF and preserve media as binary. Expanded `.gitignore` for Python/test caches, local virtual environments, logs, editor/OS files and generated release archives/checksums. Added workflow path filters for both Git hygiene files.
- Pinned `actions/checkout`, `actions/setup-python` and `actions/setup-node` to verified full commit SHAs (`v7.0.1`, `v7.1.0`, `v7.1.0`) and set checkout depth to 2 so CI can verify the current commit diff without scanning legacy history.
- Repaired repository-integrity discovery logic to include the documented default `unittest discover` pattern `test*.py`; new test modules are no longer falsely reported as uncovered when the workflow's full discovery step selects them. CI coverage now detects duplicate Python test selectors and duplicate step labels.
- Removed two duplicate Python test executions (Batch 021 and safe missing-IPA backfill) without reducing module coverage. Replaced the hand-maintained `py_compile` file list with `compileall -q tools` so future helper/test modules are syntax-checked automatically.
- No vocabulary, Related Glossary, question/choice IDs, answer keys, learner data/IndexedDB schema, UI layout, PWA runtime behavior, service worker cache or GitHub Pages architecture changed.
- Local focused tests and commit-preflight results are documented in `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.64.md`. Hosted GitHub Actions and actual Windows/macOS client commit behavior remain unverified.

## v2.95.63 — CI test discovery and safe answer-result modal lifecycle (2026-11-25)

- Fixed the GitHub Actions Batch 035 unittest discovery contract by changing its selector to `test_related_glossary_batch_035*.py`. The wildcard selects both the existing Batch 035 module and a split Cambridge module such as `test_related_glossary_batch_035_cambridge.py`; the repository preflight and CI coverage regression both verify this.
- Fixed the answer-result modal close lifecycle. Result, explanation-review and auto-advance-wait states now expose a visible close control and share one state-aware close dispatcher for the X button and Escape key. A result-modal close commits the pending result through the existing confirmation path; closing explanation review preserves the saved answer and leaves inline feedback available; closing the wait modal cancels auto-advance while keeping the current question.
- Added keyboard focus to the result and auto-advance close controls, clears stale modal classes/type/content on close, and serializes pending confirmation actions to prevent duplicate commits. Backdrop clicks remain conservative while a result is pending; explicit X/Escape remain available.
- Retained the existing completion modal and its three statistics (Đúng / Chưa đúng / Tổng câu), with the existing confirmation gate before answers and explanations are revealed. No new modal design or navigation was introduced.
- Added the modal-dismissal regression suite and CI registration; expanded CI coverage tests to match `unittest discover` glob semantics and prove the Batch 035 Cambridge split module is selected.
- No vocabulary/Related Glossary content, canonical IDs/headwords/relations, question IDs, choice IDs/order, answer keys, Mock eligibility, learner IndexedDB schema/data or Robot Buddy boundary changed. No service-worker storage schema or backend was added.
- UI layout remains frozen. Product remains GitHub Pages/GitHub-only; Cloudflare and backend services remain out of scope. Local checks are in `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.63.md`; hosted Actions, deployed Pages, real PWA cache/offline behavior and physical devices remain unverified.

## v2.95.62 — Related Glossary Batch 043: twenty-one sourced existing relation targets (2026-11-25)

- Enriched 21 existing Related Glossary rows with paraphrased English definitions, POS and Cambridge Dictionary provenance, selected only where a current vocabulary synonym/antonym relation provided a defensible sense anchor. No glossary rows or canonical vocabulary headwords were added or removed.
- Added guarded patch `patches-related-terms/v2.95.62/related-terms-043.json`, a source/provenance ledger, six dedicated regression tests and historical reconstruction updates so Batch 038–042 tests reverse Batch 043 before restoring earlier snapshots.
- Quality audit improved from 178 to 157 flagged rows (−21); missing definitions 111→103, placeholders 63→50, missing POS 174→153, and missing provenance 65→52. Duplicate normalized-term groups remain zero. Relation coverage remains 556/804.
- Preserved all 567 glossary term identities and Vietnamese meanings. Existing canonical vocabulary IDs/headwords/senses/relations, question and choice IDs, answer keys, Mock eligibility, learner IndexedDB data/schema and Robot Buddy boundary were not changed.
- Cambridge definitions are paraphrased from indexed entry excerpts reviewed 2026-11-25. Direct page fetch status was not asserted, and independent editorial review remains pending; no IPA or example sentences were invented or added.
- GitHub Pages/GitHub-only architecture and frozen UI remain. Local validators and tests are documented in `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.62.md`; hosted Actions, actual Pages deployment, offline/cache propagation and physical-device tests remain unverified.

## v2.95.61 — Related Glossary Batch 042: twenty sourced existing targets (2026-11-25)

- Enriched 20 existing Related Glossary targets with English definitions and POS: 16 Cambridge Dictionary paraphrases aligned to their existing relation anchors, plus 4 exact multi-sense definition sets copied from current canonical vocabulary entries (`guarantee`, `monthly`, `schedule`, `weekly`).
- Added exact-old-value and file-SHA-guarded patch `related-terms-042.json`, provenance/sense-alignment ledger, and five regression tests. Historical glossary reconstruction tests now reverse Batch 042 before replaying older batches; assertions are preserved.
- Quality audit improved from 198 to 178 flagged rows, 131 to 111 missing definitions, and 190 to 174 missing POS. Placeholder count remains 63; no unsupported placeholder was converted. Relation coverage remains 556/804, with 248 distinct missing relation terms.
- Preserved all 567 term identities and Vietnamese meanings; no canonical headword/ID/relation array, question/choice ID, answer key, Mock eligibility, learner data/IndexedDB, Robot Buddy privacy boundary, UI layout or hosting architecture changed.
- Cambridge entry excerpts were reviewed on 2026-11-25; direct fetch was unavailable for some pages (HTTP 403), and independent editorial review remains pending. No example sentences or IPA were copied or invented.
- Local validators, focused Python/Node tests, source/package integrity and exact Patch replay are recorded in the v2.95.61 reports. Hosted GitHub Actions/Pages and physical-device acceptance remain unverified.

## v2.95.60 — consolidated IPA and Related Glossary review queues (2026-11-24)

- Consolidated a deterministic, read-only missing-US-IPA queue from exact-headword CMUdict matching. The queue records 79 missing-IPA entries: 5 single-pronunciation candidates, 49 multiple-variant review cases and 25 with no exact dictionary key. No IPA was converted, approved or applied automatically.
- Added a Markdown renderer for the IPA queue, preserving ARPABET variants and clearly distinguishing candidate evidence from editorial approval.
- Regenerated the Related Glossary quality audit and enrichment queue: 567 entries scanned, 198 flagged, 0 duplicate normalized-term groups; the queue prioritizes definition blockers using existing relation frequency and source-headword references.
- Reconciled the candidate audit, missing-IPA report and glossary reports as versioned artifacts. All tools are read-only with respect to canonical learning content.
- Added regression coverage for IPA queue rendering, variant retention, count reconciliation and no-auto-apply policy.
- No vocabulary definitions, IPA, POS, translations, provenance, IDs, relations, questions, answer keys, learner data, IndexedDB schema, Mock eligibility, UI or deployment architecture changed.

## v2.95.59 — transparent item-complexity review queue (2026-11-24)

- Added a deterministic, read-only inventory of observable Listening/Reading item features: source length, prompt length, answer-option length spread, inference/purpose wording and multi-document indicators.
- The report is explicitly non-calibrated: it does not assign CEFR/ETS difficulty, estimate psychometric parameters, certify answer keys or approve Mock eligibility. Existing `level` labels are displayed as supplied and are not reinterpreted.
- Every current Listening/Reading question is indexed once; reserve-pending items are explicitly labelled not Mock eligible. No content, question IDs, choice IDs/order, answer keys, reserve state, learner records or IndexedDB schema changed.
- Added regression coverage and GitHub Actions syntax/test/report-generation steps. This work completes the structural triage component of Stage 2 item 9; independent review and psychometric calibration remain open.

## v2.95.58 — first-attempt learning outcome evidence (2026-11-24)

- Added separate first-attempt accuracy metrics to the read-only learning-outcome summary, alongside the existing latest-attempt metric. The first-attempt denominator includes only unique items with a valid recorded first attempt; retry attempts never overwrite that initial result.
- Added `firstAttemptItems`, `firstAttemptCorrect`, `firstAttemptAccuracy` and `firstAttemptAccuracyPercent` to the summary API. No new storage fields or IndexedDB schema changes are required because the existing attempt history is the source.
- Legacy or malformed item records without a usable attempt history are excluded from first-attempt calculations rather than having the latest result misrepresented as an initial result.
- Added runtime regressions proving first-attempt and latest-attempt accuracy can diverge after a retry and that repeated attempts do not inflate the unique-item denominator.
- Reconfirmed that answer-position shuffle certificates and stable choice identity already exist in the v2.95.57 baseline; no duplicate reorder or answer-key mutation was performed.
- No UI redesign, learner data migration, vocabulary/question content, IDs, answer keys, Mock eligibility, reserve status or Robot Buddy access changes.

## v2.95.57 — answer leakage and distractor-overlap diagnostics (2026-11-24)

- Added a deterministic, read-only diagnostic for question-stem lexical cueing, correct-answer/distractor token overlap, and keyed-answer length imbalance across 177 Mock-eligible Listening Part 3/4 and Reading Part 7 questions; both Listening and Reading reserve queues are excluded.
- Current triage flags 6/177 questions: 2 Part 3, 1 Part 4 and 3 Part 7. These are review signals only; long answers and lexical overlap can be legitimate.
- Added six focused Python tests and dedicated GitHub Actions steps for syntax, tests and report generation.
- No question text, answer keys, choice order/IDs, source evidence, Mock eligibility, reserve status, learner data/schema, UI or Robot Buddy scope changed. Listening reserve questions remain excluded.
- The audit is lexical/length triage only; it cannot prove semantic uniqueness, identify paraphrase errors or provide psychometric/ETS calibration.

## v2.95.56 — Listening Mock form-diversity gate (2026-11-24)

- Listening trend readiness now verifies distinct Listening question-ID sets across the three most recent completed Full Mock attempts; repeated attempts using the same Listening form no longer unlock a Listening trend.
- Reading trend calculation remains independent and unchanged. Listening history without question IDs fails closed rather than being assumed to represent an independent form.
- Distinct forms disclose their question overlap; overlap of 90% or more triggers an explicit caution so a nominally different form is not presented as strong independent evidence.
- Existing attempt question IDs are reused as evidence. No new learner-history schema, vocabulary/question content, answer key, choice order, Mock eligibility or IndexedDB change.
- Added regression cases for repeated forms, two distinct forms with 98% overlap, legacy records, Reading independence and Full Mock filtering.

## v2.95.55 — complete learner data backup and restore (2026-11-24)

- Added a separate full learner-data backup alongside the existing vocabulary-only JSON/CSV export. It enumerates every record in the existing IndexedDB `workspace` store and every `toeic:` localStorage key, including future/legacy app keys.
- Added SHA-256 integrity verification and strict backup type/schema/storage validation before restore. Unsupported versions, malformed records, duplicate keys, out-of-namespace localStorage keys and modified payloads are rejected before any write.
- Restore merges matching keys without clearing keys absent from the backup, downloads a pre-restore snapshot first, writes IndexedDB in one transaction, rolls back localStorage and attempts an IndexedDB rollback if cross-store restore fails, then reloads the app to hydrate runtime state.
- Requests `navigator.storage.persist()` when supported and records whether the browser granted persistent storage; this remains a browser-managed best-effort request.
- Added focused runtime and integration tests and registered both in GitHub Actions. Existing IndexedDB database/store/version and vocabulary-only import/export remain unchanged.
- No vocabulary/question content, IDs, answer keys, Mock eligibility or Robot Buddy data access changed. Physical Safari/iOS, browser quota behavior and hosted GitHub Actions remain unverified.



## v2.95.54 — independent audit Stage 1 remediation (2026-11-24)

- Applied guarded patch corrections: `appliance-n.verb_forms` is now `null`; eight inconsistent headword-level CEFR values now equal the highest CEFR level among their senses. The ninth reviewed item (`package-nv`) already followed this rule and was preserved.
- Added structural validator rule VF003 to reject empty/whitespace-only verb-form strings and CE004 to enforce the aggregate CEFR policy (A1 < A2 < B1 < B2 < C1). Added regression tests; existing rules and baselines were not relaxed.
- Confirmed the Listening reserve queue check is already data-driven in the v2.95.53 baseline and passes against 193 reserve questions; no duplicate change was made.
- Moved the two root-level v2.95.45/v2.95.46 update-note files into `docs/versions/legacy/`; added a full Python `unittest discover` step to CI.
- No IDs, headwords, topics, Vietnamese meanings, relations, question IDs, answer keys, Mock eligibility, UI features or Robot Buddy features changed.
- Independent audit remediation logs and test results are recorded in `docs/reports/INDEPENDENT_AUDIT_STAGE_1_v2.95.54.md`.

## v2.95.53 — iPad portrait responsive navigation + cross-module audit (2026-11-24)

- Fixed iPad/tablet portrait navigation: portrait tablet viewports from 641–850 CSS px now use the existing phone-style bottom navigation and mobile content flow; the sidebar is hidden.
- Preserved desktop navigation for landscape iPad Pro 11-inch M1 (approximately 1194 CSS px wide) and larger desktop/tablet landscape viewports.
- Added safe-area-aware bottom navigation, Robot Buddy positioning, modal sizing, and regression coverage for portrait/landscape breakpoint behavior.
- Corrected source/test fingerprint scope for generated Python shard, cross-module/iPad, glossary audit/queue and rendered visual evidence; generated evidence remains packaged and archive-hashed, while governance documents remain fingerprinted.
- No learner data, IndexedDB schema, vocabulary IDs, relation arrays, question IDs, answer keys, or Mock eligibility changed.
- Full cross-module audit and package evidence are recorded in the v2.95.53 release reports.

## v2.95.52 — Related Glossary Batch 041 and research-priority refresh (2026-11-24)

- Enriched eleven existing relation-target rows (`present`, `associate`, `contender`, `daily`, `deal`, `deny`, `direction`, `endpoint`, `fee`, `legitimate`, `occupation`) with Cambridge Dictionary-sourced paraphrases, POS and sense-alignment notes. Exact old-value guards and source-file SHA-256 protect every update.
- Preserved Vietnamese meanings, term identities and relation arrays. No canonical headwords, vocabulary IDs, question/answer content, learner records, IndexedDB, Mock eligibility, UI layout or hosting architecture changed.
- Updated the read-only quality audit and frequency-ranked research queue. Independent editorial review remains pending; no automatic definition invention or missing-term import was performed.
- Local full-suite, workflow replay, data validation and package acceptance results are recorded in the v2.95.52 reports. Hosted Actions, Pages, PWA cache/offline and physical-device acceptance remain unverified.

## v2.95.51 — Related Glossary Batch 040 and frequency-ranked enrichment queue (2026-11-24)

- Enriched six existing relation-target glossary entries (`charge`, `move`, `leave`, `opening`, `suggestion`, `location`) with Cambridge Dictionary-sourced paraphrases, POS and explicit sense-alignment/provenance notes. All changes use exact old-value guards and are independently review-pending.
- Added a deterministic, read-only enrichment queue ranking incomplete glossary entries by relation-reference frequency, distinct source headwords and quality priority. The report does not infer definitions or authorize automatic imports.
- Added queue contract tests and registered the queue audit in GitHub Actions syntax/test/replay workflow.
- No new glossary identities, vocabulary IDs/headwords/relations, question IDs/choices/answer keys, IndexedDB schema, learner records, Mock eligibility, UI layout or hosting architecture changed.
- Local focused tests and data/package checks are recorded in the v2.95.51 test and release-acceptance reports; hosted Actions, Pages and physical-device acceptance remain unverified.

## v2.95.49 — related glossary display safety (2026-11-24)

- Added a shared display-safety filter for related-glossary English definitions. Known editorial placeholders (including “Reference gloss for practice distractors.”) are no longer rendered as real English meanings in learner answer explanations.
- Valid definitions remain visible; Vietnamese gloss and part-of-speech metadata are preserved. This is a presentation guard only: it does not rewrite or delete glossary records.
- Added Node runtime coverage for placeholder families, valid definitions, empty/malformed values and application integration; registered the check in GitHub Actions.
- Re-audited Related Glossary: 567 entries; 227 flagged for review (223 high, 2 medium, 2 low); 150 missing definitions and 73 placeholder definitions. Coverage remains 556/804 references, with 248 unique missing terms. Missing terms are not auto-created because they lack canonical headwords and require sourced editorial review.
- No vocabulary IDs/headwords/relations, question IDs/choices/answer keys, IndexedDB schema, learner progress, Mock eligibility, UI layout or deployment architecture changed.
- Local validation and full-suite status are recorded in the v2.95.49 test report; hosted GitHub Actions, Pages and physical-device acceptance remain unverified.

## v2.95.48 — defensive learner evidence ledger (2026-11-24)

- Hardened objective resource indexing and read-only summaries against malformed resource maps, null records, invalid nested containers and malformed attempt/rubric history. Invalid nested branches are ignored by summaries and remain visible to the explicit integrity audit.
- Write paths now reject negative/non-finite timestamps and deduplicate objective IDs before storing attempts or explanation rubrics.
- The integrity audit reports latest-attempt/current-summary disagreement as a warning; it never repairs learner history. Recall-check and rubric timestamps are checked for non-negative finite values.
- Added runtime regression coverage for malformed ledgers, safe summaries, invalid timestamp rejection, duplicate objective IDs and latest-attempt mismatch reporting.
- No vocabulary/question content, learner history, IndexedDB schema, answer keys, Mock eligibility, UI layout or hosting architecture changed.
- Focused verification: Node runtime PASS; 83 Python cases PASS across 8 focused modules; real-source data validator PASS (1,141 records; 0 errors / 0 warnings). Full 89-module strict suite and hosted GitHub Actions remain unverified.

## v2.95.47 — read-only learner evidence queries (2026-11-24)

- Removed unintended write-side initialization from objective summaries and due-recall listing. These read paths now consume a safe empty view for absent/malformed containers and never add `schemaVersion` or `objectives` to learner data.
- Added frozen-ledger and empty-ledger regression coverage for objective summaries, aggregate summaries and due-recall queries.
- Explicit write operations retain their existing initializer; no IndexedDB schema, learner history migration, vocabulary/question content, answer keys, UI, or deployment changes.

## v2.95.46 — optimized-source CI and release hardening (2026-11-24)

- Continued from the user-supplied optimized v2.95.46 candidate; the prior assistant-generated ZIP was comparison-only and did not replace the user's source.
- Fixed checkpoint resume fingerprint drift by removing the operational `--resume` toggle from execution identity; added regression coverage.
- Added explicit generated-audit report patterns to the fingerprint policy so pre-test audits do not invalidate a compatible test checkpoint. Generated reports remain packaged and covered by FullSource SHA-256; governance docs remain fingerprinted.
- Replaced four Toast close-control CSS literals with existing design-system tokens; CSS token ratchet now reports 0 new violations. No UI redesign.
- Added regression coverage for fingerprint scope and Toast token compliance.
- Strict Python suite: 89 modules / 692 cases / 691 PASS / 1 accepted environment SKIP / 0 FAIL / 0 ERROR / 0 TIMEOUT / 0 NOT RUN.
- Exact local replay of `.github/workflows/validate-data.yml`: 110/110 shell run steps PASS. Local runtime (Python 3.13.5 / Node 22.16.0) differs from the workflow target (Python 3.12 / Node 24); hosted GitHub Actions and Pages remain unverified.
- All 12 local Release Acceptance gates PASS. Production deployment, browser/PWA/offline/cache and physical-device acceptance remain unverified.

## v2.95.46 — Governance consolidation and source-derived editorial inventory (candidate)

- Established `docs/MASTER_DEVELOPMENT_PROMPT.md` as the single Sections 1–15 development contract, including source-of-truth/version governance, data preservation, large-batch priorities, provenance, dynamic test inventory, deterministic fingerprints, separate Source/Production acceptance and non-destructive production testing.
- Corrected stale compatibility/version documentation and expanded the manual acceptance checklist to 28 checks; all deployment/device checks remain unverified until performed.
- Added read-only `tools/editorial_inventory.py` and a reviewed v2.95.45 baseline snapshot. Editorial Review Queue counts are now computed from source data: Listening 102 eligible / 193 reserve / 295 total, Part 7 reserve 87, and separate Part 5 practice-only 80. Eligibility classifications are not altered.
- Updated Editorial Review Queue builder and regression tests to validate source-derived metrics, report agreement, disjoint Listening inventory and separate Part 7/Part 5 pools.
- Hardened release-document rotation to preserve active unversioned backlog and manual acceptance checklist. Retired 233 superseded versioned Markdown documents and 5 old root release notes after reference analysis; complete source text, original path, original byte size and SHA-256 marker were consolidated into `docs/archive/PROJECT_HISTORY.md`. A pre-cleanup scan found zero byte-identical Markdown duplicate groups; no report was deleted merely as a presumed duplicate. Canonical batch ledgers, provenance, tests, fixtures, content and user assets are retained.
- Implemented deterministic `SOURCE_RELEASE_FINGERPRINT` / `TEST_INPUT_FINGERPRINT` support, version-controlled scope policy, environment/dependency/command fingerprints, safe symlink/path handling, dynamic inventory comparison and explicit discovery-error evidence. Strict resume rejects missing or changed fingerprints; Release Acceptance runs complete modules without the former per-test case-splitting mode.
- Candidate inventory: 89 dynamically discovered modules against the 88-module v2.95.45 baseline (one added test module; zero removals; five existing test modules modified). The complete strict suite outcome must be read from `TEST_REPORT_TOEIC_Dictionary_v2.95.46.md`; module inventory and focused test results are not substitutes for its aggregate terminal-state summary. Remote GitHub Actions, Pages deployment/cache and physical browser/device acceptance remain unverified.
- No UI redesign, CSS/menu change, Cloudflare/backend, canonical headword/ID/relationship change, learning question/choice/answer-key change or learner IndexedDB migration is intended.

## v2.95.45 — alternate QA runner merge + relation-aligned glossary corrections

- Compared the alternate user-supplied v2.95.44 source with the released v2.95.44 source; preserved the newer Batch 037 glossary data and runtime as the baseline.
- Imported isolated Python test sharding with resumable, versioned checkpoints and process-group timeout cleanup, plus a reproducible Release Acceptance runner. It derives its version from `data/manifest.json`, stores the same value in JSON and Markdown, and terminates timed-out child process groups via the shared sharder helper.
- Added five Cambridge-verified Related Glossary relation targets (`ask for`, `change`, `comments`, `communicate with`, `connection`) and exact-guarded sense corrections for `caller`, `article` and `assume`, aligned to existing relationship anchors.
- Related Glossary: 562 → 567 records; exact coverage 551/804 → 556/804 (69.2%); remaining 248 unique targets / 249 occurrences. No canonical headwords, IDs, relation arrays or learner question/answer content changed.
- Focused Python regression: 283 PASS / 1 environment-dependent SKIP across 35 distinct modules; the sharder/acceptance-runner tests are 12/12 and 10/10 respectively; JavaScript 39/39; syntax 19/19; data, learning-content, repository and version validators PASS. Full 88-module Python discovery and aggregate Release Acceptance remain INCOMPLETE due the execution limit. Independent editorial review remains pending. Remote CI, Pages deployment/cache and device QA remain unverified.

## v2.95.44 — Related Glossary coverage batch 037

- Added 16 Cambridge Dictionary-sourced lookup glosses for existing relation targets: `begin`, `book`, `bring`, `characteristic`, `clothing`, `comparable`, `compute`, `consequence`, `currency`, `down payment`, `disturbance`, `development`, `declaration`, `eager`, `entire` and `eventuality`.
- Each record contains a selected POS, concise English paraphrase, Vietnamese lookup meaning, and exact Cambridge headword URL. Search-result entry content was retrieved on 2026-11-23; independent editorial review remains pending. No Cambridge example sentences, IPA or uncertain pronunciation variants were added.
- Related Glossary grows 546 → 562 entries. Exact unique relation-target coverage grows 535/804 (66.5%) → 551/804 (68.5%); 253 unique terms / 254 relation occurrences remain uncovered. Normalized duplicate count remains zero.
- Added seven Batch 037 regression checks; hardened Batch 036 historical hash reconstruction for subsequent additive batches; registered Batch 037 in Python CI compile and test steps. Regenerated backlog, candidate, quality, relationship graph, major release and progress audits.
- No canonical headwords/IDs, synonym/antonym arrays, questions, choices, answer keys, learner IndexedDB schema/data, Mock eligibility, UI layout, Robot Buddy data boundary or backend architecture changed. No Cloudflare/backend introduced.
- Independent editorial review, remote GitHub Actions, GitHub Pages deployment/cache and physical browser/device acceptance remain unverified.

## v2.95.43 — Related Glossary coverage batch 036

- Added 11 Cambridge-indexed Related Glossary entries for uncovered relation targets: able, accuracy, actual, assume, business, caller, capable, car, carry, choice and company. Each record has POS, concise English paraphrase, Vietnamese gloss and exact Cambridge Dictionary URL.
- Added a batch-specific regression contract with canonical A–Z vocabulary and protected Grammar/Listening/Reading/Part 5 bank SHA-256 fingerprints; registered test and compile checks in GitHub Actions. Batch 035 historical base-hash test now excludes later additive glossary batches dynamically.
- Related Glossary: 535 → 546 rows; 524/804 → 535/804 unique relation-target coverage (65.2% → 66.5%); 269 unique / 270 occurrences remain uncovered; placeholder definitions remain 73.
- Cambridge search excerpts reviewed 2026-11-23; direct entry fetches returned HTTP 403. Independent editorial review, remote GitHub Actions, Pages deployment and device acceptance remain unverified.
- No UI redesign, canonical vocabulary IDs/headwords, relation arrays, learning questions/answers, learner IndexedDB, Mock eligibility, Robot Buddy permission boundary or backend/deployment changes.

## v2.95.42 — Related Glossary coverage expansion (Batch 035)

- Added 8 source-linked English glosses for previously uncovered relationship targets: administer, alert, alike, appeal, article, assist, backer and bargaining.
- Definitions are concise Cambridge Dictionary sense paraphrases; Vietnamese meanings and part-of-speech labels were curated to match the relation target meaning. Independent editorial review remains pending.
- Updated candidate-coverage tests, batch-specific provenance/data tests, and the current glossary audit/backlog/progress reports.
- No canonical headwords, vocabulary IDs, relation arrays, learner data/IndexedDB, learning questions/answers, Mock eligibility, or UI were changed.
- Source patch: `patches-related-terms/v2.95.42/related-terms-035.json`; batch ledger: `batch-035-glossary-ledger.json`.
- Local regression and validation results are recorded in the v2.95.42 test report. Remote GitHub Actions, Pages deployment, and device QA remain unverified.
- Full Source 620 files; Patch 40 overlay files (17 modified + 23 added, 0 deletions); CRC/root/exclusion checks and actual patch replay 620/620 exact; SHA-256 sidecars verified.


## v2.95.41 — Listening reserve inventory regression correction

- Fixed the stale `test_answer_position_balance.py` inventory assertions: the prior 161-reserve / 263-total expectation predated v2.95.37 Listening Batch 027. Current canonical data has 102 Mock-eligible + 193 reserve-pending questions = 295 Listening questions.
- The regression now asserts per-Part eligible counts (8/25/39/30), pending counts (1/36/84/72), and the Batch 027 boundary (16 resources / 32 questions: Part 2=8, Part 3=12, Part 4=12). All Batch 027 items must remain reserve-pending and Mock-excluded until independent approval.
- Choice array lengths, unique `choiceIds`, valid answer indexes and the historic 27-key movement identity checks remain enforced. No Listening/Reading question, answer key, question order, choice ID or editorial status was changed.
- GitHub Actions already runs `test_answer_position_balance.py`; the existing CI step is retained. Updated listening readiness, question evidence and distractor audit reports are regenerated from canonical data.
- Local verification: answer-position suite 4/4 PASS; related listening expansion, question-evidence, distractor and mock-engine checks recorded in the v2.95.41 test report. Remote GitHub Actions, Pages deployment and physical-device QA remain unverified.

## v2.95.40 — Audit 025 glossary metric reconciliation

- Fixed the stale `test_major_release_quality_audit_025.py` expectation: 519 was the glossary count before Batch 033; the current canonical source correctly contains 527 entries after eight sourced additions.
- `relatedGlossary.entries` remains the raw canonical row count and now reports `uniqueEntries` and `duplicateEntries` separately. Normalized counting uses NFKC, collapsed whitespace and case-folding.
- Current source verification: **527 raw rows / 527 normalized unique terms / 0 duplicate groups**. No glossary data was removed or rewritten to force the metric.
- Added Batch 034: corrected the stale English definition for `revision` to match its current exact single-sense canonical vocabulary entry. Vietnamese meaning, POS, term identity and original source provenance remain unchanged. The guarded patch checks the original `related-terms.json` SHA-256 and all old field values before applying atomically.
- Fixed the Batch 030 regression harness to load only manifest-listed A–Z vocabulary files, not editorial batch snapshots. Current glossary definition/POS must match the current canonical single-sense entry.
- Added 6 guarded-update tests; regenerated the current major-release audit, Learning Outcome Evidence Matrix, glossary candidate audit, backlog and glossary quality reports.
- No application UI, vocabulary headword IDs/relations, questions/answers, learner progress, IndexedDB schema, Robot Buddy behavior or Mock eligibility changed.
- Focused verification: 137/137 Python tests across 23 modules; JavaScript 39/39; validators and integrity audits PASS. Full Python discovery is not claimed due to the test-validator execution limit.
- Packaging: Full Source **587 files**; CRC/root/exclusions PASS; exact comparison **587/587**; SHA-256 sidecar verified.
- Evidence: `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.40.md` and `docs/reports/COMMAND_LOG_INDEX_v2.95.40.md`. Remote CI, GitHub Pages deployment and physical-device acceptance remain unverified.

## v2.95.39 — Related Glossary research batch 033 (8 terms)

- Added 8 previously uncovered synonym/antonym terms: **ability, acceptable, action, accusation, advertise, advise, allow, announce**.
- Each entry now includes Vietnamese meaning, part of speech, a concise paraphrased English definition and a direct Cambridge Dictionary source URL.
- Source terms and relation arrays were not rewritten; canonical vocabulary, learner data, question keys, IndexedDB schema and UI layout remain unchanged.
- Added a dedicated 3-test regression suite and CI registration. Editorial review remains pending; dictionary-source research is not equivalent to independent pedagogical approval.
- Validation in this release is recorded in `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.39.md`.

## v2.95.38 — Context-aware synonym/antonym explanations

- Packaging: FullSource **559 files**; Update Patch **12 files (9 changed + 3 added)**, no deletions; replay on v2.95.37 exact **559/559**; CRC/root/SHA PASS.

- Corrected choice-review context lookup to filter relation sources by the active question type: synonym explanations only use synonym references; antonym explanations only use antonym references. Prevents misleading cross-relation evidence.
- Related Glossary alias explanations now include available POS and English definition alongside Vietnamese meaning. Missing metadata is omitted; no definitions or relations were invented.
- Added 3 focused regression tests and registered the suite in CI Python syntax and test steps.
- Validation: focused tests **3/3 PASS**; version sync check PASS. No vocabulary relations, canonical word records, question answers, learner data, IndexedDB schema, or UI layout changed.
- This release is a focused functional correctness patch, not a content-completion milestone.

## v2.95.37 — Listening expansion batch 027 (32 questions)

- Added 16 original-editorial Listening resources: 8 Part 2 response items, 4 Part 3 conversations and 4 Part 4 talks, totaling 32 questions.
- Added transcript evidence pointers for every question, Vietnamese explanations, stable choice IDs, review notes, and batch/source metadata. All 16 units are reserve-pending independent review and fail-closed excluded from Mock.
- Mapped all 16 new resources into the corresponding Listening objective resource groups; canonical objective-resource links are now **379/379**.
- Updated listening readiness and question-evidence audits, made the distractor structural audit version-aware/dynamic instead of retaining stale 240/171 totals, and refreshed mock-reserve count tests.
- Validation: learning content 0 errors/0 warnings; 104 focused Python tests PASS; 39/39 JavaScript suites PASS; objective resource mapping 379/379; distractor structural audit PASS; version sync PASS. Full Python discovery, remote CI, Pages deployment and physical-device QA not run.
- Listening inventory: **145 units / 295 questions**; 102 eligible and 193 pending review. Part 1 still has only 8 eligible questions; one pending item is retained. No Mock eligibility changed.
- No UI redesign, vocabulary IDs, glossary entries, learner progress, IndexedDB schema or answer-history records changed.

## v2.95.35 — canonical glossary provenance recovery batch 031

- Added canonical sense-index (`sourceSenseIndex: 0`) for **155** exact-match single-sense glossary entries.
- Recovered missing source-headword/source-release fields for **37** entries and POS for **6** entries; total **165** glossary rows changed (some updates overlap).
- New policy: source sense index is assigned only for a single-sense canonical match. Multi-sense rows remain unindexed and missing definitions are not auto-joined. Existing English definitions and Vietnamese glosses are preserved.
- Added reusable idempotent enrichment tool and 5 regression tests; batch provenance tests were hardened to allow additional provenance fields while checking original batch values.
- Quality snapshot: 519 glossary rows; 156 missing definitions; 73 placeholders; 223 missing POS; 75 audit-flagged missing source labels; 0 duplicate normalized terms. (Flag counts overlap; priorities are exclusive.)
- Validation: 79/79 focused glossary tests, 3/3 CI coverage tests and 39/39 JavaScript suites PASS; data/content/integrity/version validators PASS. Full Python discovery remains incomplete due runtime timeout. FullSource 535 files; Patch 26 entries (18 changed + 8 added), 0 deletions; exact replay 535/535; CRC/SHA PASS.

## v2.95.34 — Related Glossary canonical definition backfill (73 terms)

- Backfilled English definitions and POS for 73 glossary terms with an exact canonical vocabulary headword and a single canonical sense; copied values verbatim, no external paraphrase or inference.
- Preserved every existing Vietnamese meaning and all 519 term identities. Ambiguous multi-sense exact matches and non-matching terms remain untouched.
- Added batch 030 ledger and 3 focused regression tests; registered the suite in CI and repository-integrity coverage.
- Verification: Python 592 PASS / 1 SKIP (Git metadata-dependent), JavaScript 39/39 PASS; vocabulary and learning validators PASS with 0 errors/warnings; repository integrity 406 files, 0 errors/warnings; version sync PASS. FullSource 527 files; patch 24 entries (15 changed + 9 added), 0 deletions; replay exact 527/527; CRC and SHA PASS. No UI, learner progress, IndexedDB, or question-answer content changed.

## v2.95.33 — Related Glossary QC triage

- Added deterministic High/Medium/Low review-priority classification to the read-only related-glossary audit. High priority includes missing/placeholder definitions, malformed rows, duplicate normalized terms and term-echo definitions; Medium flags missing POS, Vietnamese gloss or provenance; Low captures short-definition review.
- Report now sorts by actionable risk and emits reconciled priority counts. No glossary data was edited or definitions inferred.
- Added 2 regression tests for priority classification and count/order reconciliation.

## v2.95.32 — Major TOEIC content expansion and QC closure

- Closed baseline QC on v2.95.31: 580 Python tests and 39 JavaScript regression suites PASS after repairing stale test expectations for glossary/IPA metrics.
- Major content batch 026 adds 8 Grammar lessons / 32 exercises, 8 Listening units / 24 questions (four Part 3 conversations, four Part 4 talks), and 8 Reading Part 7 single passages / 24 questions. Total addition: 24 resources / 80 exercises and questions.
- All new content has Vietnamese explanations, exact transcript/passage evidence, stable IDs, source/batch metadata, balanced answer positions and source SHA-256 inventory.
- Listening/Reading are original-editorial practice content with reserve-pending-independent-review status, fail-closed Mock exclusion and reviewer notes. The new 24+24 questions remain excluded from Mock eligibility.
- All 24 batch resources are linked to learning objectives. Objective-resource map is now **363/363**.
- Independent review queue: **328** items (161 Listening + 87 Reading Part 7 + 80 Part 5). Question evidence audit indexes **550** current Listening/Reading questions.
- Post-batch learning-content validation: 0 errors / 0 warnings; vocabulary validation: 0 errors / 0 warnings; repository integrity: 405 references, 0 errors / 0 optional warnings. Final Python suite 587/587 PASS; JavaScript suites 39/39 PASS; batch 026 focused tests 6/6 PASS; mock-engine regression PASS.
- No UI redesign, canonical vocabulary, synonym/antonym relations, learner progress/history or IndexedDB schema changes.
- Packaging: FullSource 512 files; patch 39 entries / 0 deletions; exact replay 512/512; CRC and SHA-256 PASS.
- Remote GitHub Actions, Pages deployment and browser/device acceptance not run.

## v2.95.31 — safe CMUdict IPA backfill and syllable-onset correction

- Added a preview-first safe backfill tool that applies only exact-headword, unique-pronunciation CMUdict entries that pass the project IPA converter; ambiguous/missing/conversion-failing records remain review-only.
- Added 1 verified source-linked US IPA entry (`dispute`) to the cumulative ledger and canonical data (IPA `/dɪ.ˈspjut/`).
- Corrected the syllable-onset allowlist for the `spj` cluster, keeping the glide with the stressed syllable.
- Added 8 pipeline tests and 1 converter regression; registered both in CI and repository-integrity coverage.
- No UI, question/answer, learner progress, or relation data changed.

## v2.95.30 — missing US IPA research queue (non-mutating)


- Added CMUdict candidate review queue for the 80 canonical words without US IPA: 6 single-pronunciation candidates, 49 ambiguous pronunciation sets, 25 no exact dictionary match.
- Queue builder preserves alternate ARPABET pronunciations, deduplicates identical lines, sorts consistently, and never auto-applies IPA.
- Added 8 focused tests and CI registration. No canonical vocabulary, UI, learner progress, relations, or answer data changed.

## v2.95.29 — canonical related-glossary expansion (89 terms)

- Added 89 missing related-term entries only when each term had an exact canonical vocabulary headword match and every canonical sense contained both Vietnamese and English definitions. Multi-sense glosses preserve all canonical sense definitions joined for reference.
- Added provenance (`canonical-vocabulary-senses`, exact source headword, source release `2.95.28`) to every addition. No existing glossary row, vocabulary headword, synonym/antonym relationship, learning question/answer, learner record, or UI was overwritten.
- Added deterministic enrichment utility, 8 tests and CI registration. Exact eligible missing canonical candidates remaining: 0.
- Review note: this reduces glossary lookup gaps, but joined multi-sense terms may still need human sense-specific review; it does not claim to resolve relation meaning in every context.

## v2.95.28 — vocabulary relationship graph audit

- Added read-only cross-file audit of canonical synonym/antonym graph: dangling targets, related-glossary coverage, unresolved terms, duplicate headwords/references, self-links, non-reciprocal relations, and malformed records. Non-reciprocal flags are review-only; no relations or learner-facing data changed.
- Added focused tests and CI audit step.

## v2.95.27 — glossary quality audit robustness

- Duplicate detection now applies Unicode NFKC normalization and collapses internal whitespace before case-folding, improving detection of visually equivalent term variants.
- Audit input now reports a non-list `terms` container explicitly instead of crashing; empty lists remain valid.
- Added three robustness tests. The audit remains read-only; no runtime glossary, vocabulary, relationships, questions, learner data, or UI changed.

## v2.95.26 — glossary quality audit hardening

- Hardened the related-glossary quality audit with missing Vietnamese gloss checks, malformed row handling, normalized duplicate detection and JSON report output.
- Added tests and CI registration; no runtime data or UI changes.

# v2.95.25 — related glossary quality flag audit

- Added `tools/audit-related-glossary-quality.py`, a read-only screening tool for missing English definitions, placeholder definitions, short definitions, term-echo definitions, missing POS and missing source provenance.
- Generated `reports/RELATED_GLOSSARY_QUALITY_FLAGS_v2.95.25.md`: 430 entries scanned, 305 entries flagged for editorial review. Flags overlap; they are not unique issue totals and do not indicate all entries are wrong.
- Added 4 deterministic tests and CI registration. No glossary data, vocabulary, relation arrays, learner data or UI changed.

# v2.95.25 — read-only related glossary candidate audit

- Added `tools/audit-related-glossary-candidates.py`, a read-only candidate audit that ranks unglossed synonym/antonym references and flags placeholder definitions.
- Added deterministic reconciliation tests (3) and CI registration.
- No vocabulary, glossary runtime data, relation arrays, questions, learner data or UI changed.
- Focused verification: 3/3 candidate-audit tests PASS.

## v2.95.25 — related glossary canonical-sense batch 028

- Added seven previously unglossed related terms (`adherence`, `agreement`, `appraise`, `assign`, `assumption`, `authorization`, `breakdown`) using exact canonical headword senses, retaining English definitions, Vietnamese meanings and POS, with sourceHeadword provenance.
- Exact related-term coverage improved 412 → 419/804 (51.2% → 52.1%); unglossed terms 392 → 385; unglossed references 393 → 386.
- No vocabulary headwords or synonym/antonym relationship arrays changed. Batch ledger, absent-only patch, focused tests and CI registration added.
- Verification after this follow-up: 34 focused Python tests across seven modules PASS; all 39 JavaScript suites PASS; vocabulary, content, repository integrity and version-sync checks PASS. Full Python discovery, remote CI and device acceptance remain unverified.

## v2.95.25 — learning-outcome evidence matrix and audit detail

- Expanded the major-release audit with per-outcome criterion detail, evidence status distribution, metric, threshold and minimum item count.
- Added generated `LEARNING_OUTCOME_EVIDENCE_MATRIX_v2.95.25.md` so the 33 criteria can be reviewed individually; no learner progress or mastery is inferred.
- Added regression tests for status-count reconciliation and required criterion fields.
- Verification for this follow-up: 78 focused Python tests across 11 modules PASS, 39 JavaScript suites PASS, data/content validators PASS and version sync PASS. Full Python discovery and a slow validator unittest module remain incomplete/time-limited.
- No UI, vocabulary headwords, question bank, answer keys, learner storage or runtime learning behavior changed.

## v2.95.25 — canonical-sense glossary backfill and major quality audit
- Verification refresh: 66 focused Python tests across nine modules PASS; 39 JavaScript regression suites PASS; vocabulary/content validation and version synchronization PASS. Repository integrity 1/1 PASS. Full Python discovery was not completed within execution limits.
- Release packaging fix: preserve nested `docs/archive/` history while excluding only the repository-root archive and temporary `.tmp` files. Added regression checks for both boundaries.
- Robot Buddy privacy refinement: when the user turns progress analysis OFF, any rendered progress dashboard is immediately removed from the chat panel; other conversation messages remain. Analysis remains local, opt-in, and read-only.

- Robot Buddy progress analysis is explicitly opt-in: missing preference is treated as disabled. The welcome prompt explains that local analysis is optional; it only runs after enabling or asking for it while enabled. Existing contextual help, scripted conversation, navigation, placement-test flow and idle nudges based on current surface remain available without progress analysis. Aggregation uses already-loaded in-memory snapshots, does not directly open learner stores, does not mutate records and does not send data remotely.
- Added a CI regression for the Robot Buddy data boundary and explicit opt-in gate.

- Backfilled 43 existing related-glossary entries whose English definitions were placeholders, using exact canonical vocabulary headword senses. Existing Vietnamese meanings and relation graph remain unchanged; source provenance is recorded.
- Placeholder English definitions reduced from 116 to 73. No new glossary terms were added; no uncertain or unmatched entries were rewritten.
- Added an auditable baseline candidate report, cross-domain major-release audit, five-plus backfill safety tests and CI registration.
- Local targeted Python: 53 tests PASS plus version-sync 12/12; JavaScript: 38/38 PASS. Data/content validators and audits report PASS. Full Python discovery, remote CI, browser/device QA and deployment remain unverified.

## v2.95.24 — case-insensitive glossary backlog aggregation

- Fixed backlog aggregation so case variants of the same missing related-term merge into one row. Synonym/antonym counts combine, source-headword anchors deduplicate, and display spelling is deterministic.
- Added regression coverage for mixed-case duplicates. Existing canonical data has no such duplicates, so coverage totals remain unchanged.
- No vocabulary, relation, learning content, UI or runtime changes.

## v2.95.23 — glossary backlog traceability

- Upgraded the unglossed related-term backlog to schema v2: each missing term now lists its source headwords, distinct-headword count, synonym/antonym reference split, and deterministic review priority.
- This helps editorial review select terms with broader vocabulary impact without inventing definitions or automatically adding unsourced glosses. Existing missing-term and occurrence counts remain unchanged.
- Added regression coverage for provenance anchors, reference-type totals, schema and sort order. No vocabulary glosses, canonical headwords, relation arrays, questions, answer keys, learner data or UI/runtime behavior changed.
- Local candidate only; full repository suite, remote CI, deployment and device acceptance are not claimed.

## v2.95.22 — related-term backlog automation

- Added a deterministic, frequency-ranked report for unglossed synonym/antonym terms, including JSON data and a Markdown reviewer queue.
- Added two regression tests for report counts, ordering and glossary exclusion; registered the script/test in CI syntax and unit-test steps.
- No vocabulary definitions, headwords, stable IDs, relations, learning content, UI, progress storage or runtime behavior changed.
- Candidate is locally validated; full repository Python discovery and remote CI/deployment are not claimed.

## v2.95.21 — continue high-frequency glossary coverage and repair progress regression

- Added 23 Cambridge-referenced Vietnamese lookup glosses for the highest-frequency source-verified unglossed terms in canonical synonym/antonym relations. Each added term occurs exactly twice; the glossary grows from 400 to 423 entries.
- Exact case-insensitive relation join improves from 389/804 (48.4%) to 412/804 (51.2%). Occurrence coverage improves from 598/1,037 (57.7%) to 644/1,037 (62.1%); 392 distinct terms / 393 occurrences remain unglossed.
- Added a dedicated Batch 027 provenance ledger, absent-only SHA-256-guarded patch and five focused regression tests. Registered the new suite in GitHub Actions and the release-integrity Node test. Four additional two-reference terms were included after a second backlog scan. `disorganize` remains deferred because no direct Cambridge dictionary definition page met the source policy.
- Corrected the stale project-progress test that still expected the v2.95.17 coverage figure (385/804). Project-progress output remains generated from canonical data, and the v2.95.21 snapshot now reports the measured 412/804 value.
- No headword, stable vocabulary ID, synonym/antonym relation, question, answer key, learner record, storage key, UI layout, CSS, navigation or runtime behavior changed. Only release-version markers were synchronized.
- All new glosses remain provisional pending independent lexical review. The 280-item Listening/Reading/Part 5 review queue is unchanged and remains pending. Local candidate only; remote CI, deployment, browser/device QA and owner manual acceptance are not claimed.

## v2.95.20 — related-term glossary Batch 026

- Added four Cambridge Dictionary lookup glosses: `method`, `consume`, `function`, and `launch`.
- The related-term glossary increases from 396 to **400 entries**. Existing synonym/antonym relations, canonical headwords, stable IDs, learning content, answer keys and learner data remain unchanged.
- Added an absent-only SHA-256 guarded patch, provenance ledger, five regression checks, and a dedicated CI test step.
- The release source is reconstructed from the locally available v2.95.19 FullSource ZIP; earlier v2.95.20/21 claims from chat were not present as artifacts in this workspace. This candidate is based on the recovered v2.95.19 source and only the changes verified here.
- UI/layout is unchanged. Local checks only; remote CI, Pages deployment and device acceptance are not verified.

## v2.95.19 — clear Listening evidence gaps and consolidate independent review queue

- Added exact transcript evidence pointers to 29 legacy Listening reserve questions that previously lacked `evidenceText`; all 137 pending Listening questions now have a matching transcript pointer. Part 1's pending photo item also records a separate internal visual-action note.
- Added explicit `internal-author-check; transcript-evidence-linked-v2.95.19; independent-second-review-pending` notes to 16 legacy Listening units that had no review-state note. The `reserve-pending-independent-review` status is retained for all 137 questions; none is promoted to Mock.
- Added a generated, item-level independent review packet covering 137 Listening questions, 63 Reading Part 7 reserve questions and 80 separate Part 5 sentence-completion questions (280 total). The queue supplies transcript/passage context, answer keys and source pointers with per-question decisions and correction fields.
- Strengthened Listening regression tests to require a source-matching evidence pointer for every reserve question and a separate visual note for Part 1. The evidence report now distinguishes traceability from correctness/approval. CI runs the review-queue generator test. The generated progress snapshot now reports the 280-item independent-review queue from the canonical reserve statuses. The Part 1 reviewer packet includes the spoken A–D statement translation alongside generic answer labels, so the photo-action review can compare the image against all four statements.
- No UI/CSS/layout, vocabulary headword, stable ID, learner record, question key, or Mock eligibility changed. This release removes evidence-packet gaps and reduces reviewer handoff friction; independent reviewer sign-off, device QA and remote CI remain open.

## v2.95.18 — source-checked US IPA backfill batch 024

- Added US IPA transcriptions for 13 existing TOEIC headwords: `accountable`, `admission`, `backlog`, `carrier`, `confidentiality`, `creditor`, `credential`, `designation`, `documentation`, `duration`, `eligible`, `emerge` and `exemption`.
- US IPA coverage rises from 1,048/1,141 (91.8%) to **1,061/1,141 (93.0%)**; 80 canonical headwords still have no US IPA. Entries with POS-dependent pronunciation variants or no clearly verified Cambridge US form were intentionally left blank.
- Changes are limited to the existing `/phonetic/us` field. Stable IDs, headwords, meanings, examples, topics, word-family/relationship arrays, questions, answer keys, learner data and UI structure are unchanged.
- Added source ledger `data/vocabulary/batch-024.json`, an optimistic-lock patch `patches/v2.95.18/batch-001-ipa.json`, six focused Python regression tests, CI registration and JavaScript release-integrity assertions. New transcriptions remain pending independent phonetic review.
- Local candidate only. Remote GitHub Actions/Pages, deployment, browser/device QA and owner manual acceptance are not claimed.

## v2.95.17 — related-term glossary completion batch 023

- Added nine Cambridge-sourced Vietnamese lookup glosses: `choose`, `distribution`, `effect`, `estimate`, `former`, `inform`, `origin`, `possibility` and `responsibility`. The related-term glossary rises from 387 to 396 entries.
- Each new term already appears exactly twice in existing canonical synonym/antonym references. Exact case-insensitive coverage rises from 376/804 to 385/804 referenced terms; remaining gaps fall from 428 terms / 465 occurrences to 419 terms / 447 occurrences.
- The change adds explanatory lookup records only. No canonical headword, ID, topic, synonym/antonym relationship, question, answer, learner record or runtime data contract was changed. All nine additions remain provisional pending independent lexical review.
- Added batch provenance, an absent-only SHA-256-guarded patch, nine focused regression tests and a dedicated CI step. Historical glossary tests now use non-regressive minimum-size assertions rather than failing when future batches add entries. JavaScript release-integrity assertions cover Batch 023.
- Local checks: focused Python suites 46/46 passed; JavaScript release-integrity check passed; vocabulary, learning-content, repository-integrity and version-sync validators passed. Remote GitHub Actions/Pages and browser/device acceptance remain unverified. Remote GitHub Actions/Pages and browser/device acceptance are not claimed.

## v2.95.16 — lightweight Git-tracked commit package

- Added `tools/package_source.py` to create the GitHub commit ZIP from `git archive`, using exactly one root folder `Toeic_Dictionary_vX.Y.Z/`.
- Package output contains committed files only; untracked local logs and release artifacts are excluded. Tracked edits must be committed first. Nested ZIPs, bundles, logs, `.git`, cache and release/archive paths are rejected.
- Added package contract tests for one root folder, exclusion of untracked logs, dirty tracked-tree refusal and version format.
- Packaging-tool release only. No vocabulary records, learner data, application runtime behavior or exam content changed.
- Local verification: package tests 3/3 PASS; version synchronization is being checked. Remote GitHub CI, Pages and browser/device acceptance remain unverified.

## v2.95.15 — close the highest-frequency related-term glossary gaps

- Added four Cambridge-sourced Vietnamese glosses for the remaining synonym/antonym terms with at least three references: `aim`, `avoid`, `cause` and `conceal`. The related-term glossary rises from 383 to 387 entries.
- POS/sense scope: `aim` is noun-only in the current relationship graph; `avoid` and `conceal` are verbs; `cause` covers noun and verb usage. Glosses explain referenced terms without changing the underlying synonym/antonym arrays.
- Added provenance ledger `data/vocabulary/batch-022.json`, an absent-only patch with base-file SHA-256 guard, dedicated Python tests, workflow registration and JavaScript release-integrity assertions.
- Canonical dictionary remains 1,141 headwords. No vocabulary ID, headword, topic, question, answer key, learner record, IndexedDB schema, localStorage key or runtime data contract was changed.
- Exact-term audit moves from 372/804 to 376/804 referenced terms with glossary entries; 428 distinct terms and 465 of 1,037 link occurrences remain without a glossary entry. These figures use the exact case-insensitive term join, not the validator's separate informational counter.
- Local candidate only. All four new glosses remain provisional pending independent lexical review; remote GitHub Actions/Pages, browser/PWA/device acceptance and deployment are not claimed.

## v2.95.14 — sourced related-term glossary backfill

- Added ten Cambridge-sourced Vietnamese glosses for frequently referenced synonym/antonym terms: `requirement`, `pay`, `ignore`, `withhold`, `retain`, `earnings`, `duty`, `distribute`, `discourage` and `decline`. The related-term glossary rises from 373 to 383 entries.
- The ten terms already occurred in canonical synonym/antonym fields; this release adds explanations only. It does not add headwords, alter synonym/antonym relationships, or change vocabulary identities, topics, questions, answers or learner records.
- Glossary coverage audit after the patch: 804 distinct referenced terms; 372 have a matching glossary entry and 432 remain unglossed. At occurrence level, 477 of 1,037 synonym/antonym links still point to terms without a glossary entry. These are separate measures and are not a count of missing dictionary headwords.
- Added a provenance ledger, absent-only patch, a dedicated six-case Python regression module and aggregate JavaScript release-integrity assertions. CI now triggers on `patches-related-terms/**` for both pushes and pull requests. All new editorial glosses remain provisional pending independent lexical review.
- Local source checks only; remote GitHub Actions/Pages, browser/device acceptance and Claude's independent review of v2.95.13 are not being represented as complete.

## v2.95.13 — additional TOEIC sense coverage and family-link precision

- Expanded ten existing workplace/business headwords with clearer part-of-speech and usage distinctions: `bill`, `charge`, `document`, `experience`, `function`, `host`, `minute`, `offer`, `supply` and `value`. Added 24 original bilingual examples with explicit `sense_index` coverage. The project-wide multi-sense count rises 39 → 49; examples attached to multi-sense records rise 81 → 105.
- Added four Cambridge-sourced Vietnamese related-term glosses: `demand`, `guest`, `inexperience` and `refund`; the related-term glossary rises 369 → 373 entries.
- Aligned two reverse word-family links after splitting `value`: `valuable → value (n)` now maps to the monetary-worth noun sense; `valuation → value (v)` now maps to the assess-worth verb sense. These checks exposed and prevented ambiguous `n/v` cross-links from surviving a sense split.
- All canonical changes use separate patch files with `expect.old`, `allowedPaths`, stable-ID-set SHA-256 and identity guards. Data provenance is recorded in `batch-017.json` through `batch-020.json`. Editorial changes remain provisional and pending independent lexical review.
- Canonical inventory remains 1,141 headwords. No `id`, `word`, `topics`, question, answer key, learner data, IndexedDB schema or localStorage learner key was changed. Existing Flashcard sense rendering is exercised against the newly expanded records; no new runtime API or backend was added.
- Candidate is local only. Remote GitHub Actions, GitHub Pages, browser/device acceptance and independent human lexical review are not claimed.
- Focused verification: 17 Python modules / 175 cases and 38/38 JavaScript suites passed; data and learning-content validators report 0 errors / 0 warnings; clean-baseline patch replay matched all 10 changed A–Z files and `related-terms.json` byte-for-byte. Full Python aggregate, `test_validator.py`, remote CI/Pages and device acceptance are not claimed. See `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.13.md` and `reports/COMMAND_LOG_INDEX_v2.95.13.md`.

## v2.95.12 — sense-linked vocabulary expansion and sourced related-term glosses

- Split nine existing workplace/TOEIC headwords into distinct meanings by part of speech or usage: `address`, `application`, `claim`, `draft`, `issue`, `order`, `record`, `position` and `term`. Added 20 original example sentences/translations with explicit `sense_index` links; multi-sense headwords increase from 30 to 39 and their linked examples from 61 to 81.
- Added 22 Cambridge-sourced Vietnamese glosses for related terms used by the new senses, so the newly introduced synonym/antonym terms are not left as English-only entries. The missing related-term glossary occurrence count across the complete vocabulary decreases from 546 to 528 despite the added links (custom exact-term comparison against v2.95.11).
- Corrected `order`'s goods-order noun synonym from `purchase request` to the procurement term `purchase order`, using the Cambridge purchase-order definition. Corrected the reverse word-family relation `claimant → claim` to the specific compensation/request noun sense (`n`) instead of the former mixed `n/v` link.
- All data updates used version-locked patches with `expect.old`/absent preconditions, narrow allowlists, dry-run, apply and operation audit logs. A dedicated related-term patcher supports dry-run/apply/rollback, exact-base-file SHA-256 checking, exact Cambridge hostname/path validation, required-field and duplicate validation, file-mode preservation and byte-exact restoration if audit logging fails.
- Added provenance snapshots `batch-014.json`, `batch-015.json` and `batch-016.json`; new definitions, examples and glossary entries are marked provisional and pending independent lexical review. No new canonical headwords were added. All 1,141 stable IDs, headwords and topic arrays remain unchanged.
- Added regression coverage for sense/example alignment, source evidence, identity guards, glossary links, specific word-family POS and safe related-term patch operations. Flashcard backs now show all additional meanings and the example linked to each `sense_index`; a dedicated helper escapes HTML, returns no empty panel for single-sense words and is included in both Service Worker required/app-shell caches. Robot Buddy streaming, fixed maximum 10-card Flashcard, Listening/Reading content, Mock eligibility, IndexedDB v1 and learner records remain unchanged.
- Local verification: 38/38 JavaScript suites PASS; 13 focused Python modules 147/147 PASS (including related-term patcher 11/11, vocabulary details 15/15, family links 6/6, baseline IDs 13/13, patch-data 20/20, CI coverage 3/3, design-token audit 8/8, design system 19/19, design profile 6/6 and learning-content 34/34). Vocabulary validator: 1,141 records, ID additions 0/missing 0, 0 errors/0 warnings; learning-content validator 0 errors/0 warnings; repository integrity 372 references, 0 errors/0 optional warnings. All four vocabulary data patches and the related-term patch were replayed from the v2.95.11 Git baseline into a clean temporary tree; the resulting eight A–Z letter files and `related-terms.json` matched the candidate byte-for-byte.
- The complete `test_validator.py` unit module did not finish within this execution environment and is not claimed as PASS; the actual `validate-data.py --verbose` CLI did pass. GitHub Actions/Pages, browser UI, offline, two-tab update, iOS/Android TTS and human independent lexical review remain unverified.

## v2.95.11 — patch audit-log classification, CSS token ratchet and manual acceptance

- `tools/patch-data.py` records an explicit `mode` (`dry-run`, `apply`, `rollback`) on every operation log row; `.gitignore` excludes `logs/` so local audit output is not accidentally committed.
- Added `tools/audit-design-tokens.py`, a canonical rule file and an identity-based ratchet baseline. Existing v2.95.10 CSS findings remain warnings; new identities/values, increased occurrences and policy-hash drift fail CI. The baseline was tightened only by removing three update-banner violations fixed in this change.
- Added the formal design specification: one system font, nine semantic text roles with line-height, five permitted font weights, tokenized radius/shadow/spacing/color roles, four responsive bands and shared recipes for button/input/card/modal/chip/tab/banner. `calm-study-blue` remains a conditional default awaiting owner approval.
- Migrated the PWA update banner to existing spacing, typography, surface, border, radius and shadow tokens. No bulk CSS migration was performed.
- Added `docs/reports/MANUAL_ACCEPTANCE_CHECKLIST.md` with 14 real-world GitHub/PWA/offline/update/two-tab/TTS/Flashcard/photo/path checks. All 14 begin as `Chưa kiểm`; no remote or device QA is claimed.
- Retained the user-requested Robot Buddy progressive local replies and the fixed maximum 10-card Flashcard behavior. No vocabulary IDs, words, topics, question content, learner records or IndexedDB schema changed.

## v2.95.10 — Flashcard fixed batch, vocabulary identity baseline, safe data patching and consent-based PWA updates

- Removed the inactive 5-word Flashcard option from the UI and runtime. Every Flashcard entry route (all topics, Học tổng hợp, continue/next batch and wrong-answer review) now uses one consistent maximum of 10 words; the wrong-answer flow prioritizes missed words and fills remaining slots with new words. This does not modify vocabulary records or learner progress.
- Expanded `tools/baseline-ids.json` from 928 to 1,141 canonical vocabulary IDs after confirming 213 additive IDs and zero missing IDs. The resulting baseline has 1,141 unique IDs; validation now reports `ID: thêm 0, mất 0`.
- Hardened `tools/patch-data.py`: `/id`, `/word` and `/topics` roots (including descendants) are immutable; every patch must declare exact `allowedPaths`; an out-of-allowlist operation rejects the entire batch; and each operation writes an audit record with timestamp, batch ID, ID, pointer, old/new values and result. If the final audit record cannot be written after data replacement, the tool restores every original file byte-for-byte before returning an error. Existing patch operation payloads were not changed; their path allowlists were added from the paths they already use.
- Changed the Service Worker lifecycle: first install can activate immediately, later updates wait for explicit user consent through the “Có bản mới – Tải lại” banner and `SKIP_WAITING` message. Failed installs preserve the old cache; optional asset failures do not block installation; cache cleanup remains TOEIC-prefix-scoped.
- The update banner now uses shared typography tokens; the design-profile typography-floor regression remains green without changing the proposed visual profile.
- Re-audited content: 1,141 vocabulary headwords; Listening 121 units / 239 questions (102 Mock-eligible, 137 pending independent review); Reading 65 resources / 263 questions; Grammar 50 lessons / 137 exercises; separate Part 5 practice 80 questions (practice-only, review pending). No pending item was promoted to Mock eligibility.
- Local verification: 37/37 JavaScript `.mjs` suites PASS. Focused Python modules: baseline IDs 13/13, patch data 17/17, practice fallback 6/6, PWA readiness 3/3, CI coverage 3/3, design profile 6/6, version sync 12/12 and release rotation 6/6 and repository integrity 1/1. These focused Python modules total 67 passing cases; the whole Python inventory is not claimed as complete. Vocabulary validator: 1,141 records, 0 errors/0 warnings, 0 missing IDs; learning-content validator: 0 errors/0 warnings; repository integrity: 366 references/data files, 0 errors/0 optional warnings.
- `test_validator.py` did not complete within the available execution window and is not claimed as PASS. A broad Python discovery run was also interrupted; only the individually completed modules above are counted. GitHub Actions, GitHub Pages, real-browser two-tab update behavior, PWA offline behavior and physical-device acceptance remain external gates.
- No vocabulary A–Z record, stable ID, headword, topic, question, answer key, learner record, IndexedDB schema, localStorage learner key, TTS cadence or Mock eligibility was modified. No backend, AI API or remote learner-data transfer was added.

## v2.95.9 — Robot Buddy progressive response streaming and context-aware local composition

- Replaced the 320 ms whole-message reveal in ordinary Robot Buddy chat with a progressive character/grapheme stream, a blinking response cursor, an initial thinking indicator and delayed action buttons that appear after the reply is complete.
- Added a safe stream-completion path: a new user turn finishes the previous partial response before appending the next turn; streamed text is rendered with `textContent`; reduced-motion preferences skip the character animation.
- Improved the local response engine: feature help, FAQ, contextual help, identity, encouragement and clarification replies are composed from varied openings, transitions, current-page/current-item details and next-step language. FAQ selection now scores phrase matches rather than accepting a weak first substring match.
- Unsupported questions now receive an honest, context-aware clarification prompt instead of repeating a rigid generic statement. The Buddy does not claim it can answer unrestricted questions.
- Updated the visible product disclosure: replies are composed locally from bundled support content, lightweight rules and in-memory app context; no generative model, external AI/API, backend or learner-data transmission is introduced.
- Added `robot-buddy-streaming.mjs` and registered it in CI. Existing Robot Buddy routing, Placement, Learning Insights, dashboard, privacy and idle safeguards remain in place.
- No learner data, vocabulary/question content, stable IDs, IndexedDB schema, localStorage keys, TTS timing or Mock eligibility changed. Remote Actions, deployed Pages, browser animation and physical-device acceptance remain external verification gates.

## v2.95.8 — Five-defect consolidation, Robot Buddy Learning Insights preservation and source cleanup

- Consolidated the five regression groups previously delivered across v2.95.1–v2.95.5: Buddy page-only routing; Part 7 editorial validation/CI guard; Guided Mock Listening lead-in handoff; exact A/B/C/D pause assertions; and single visual progress dashboard without duplicate prose.
- Reaffirmed the approved Robot Buddy behavior: retain opt-in, local read-only Learning Insights and dashboard. The app passes an in-memory snapshot to the pure aggregator; no direct storage access, writes, migrations or external transmission are added. The v2.95.7 privacy-only removal of this feature is intentionally not carried forward.
- Added context-aware Buddy guidance for the active page and current in-session word, Flashcard, practice question, Grammar lesson, Reading item, Listening item or Foundation lesson. Idle nudges use that current item first and only compute progress-derived reminders when no current item is open.
- Adopted v2.95.7's documentation consolidation policy and safe dry-run-first release rotation utility, while retaining the five-defect tests and learning-insight regressions.
- Removed generated Python bytecode/cache artifacts from the distributable source. Intentional compatibility tombstones remain documented and tested; they are not duplicate active modules.
- No vocabulary/question bank, answer key, stable ID, IndexedDB schema, localStorage learner key or learner record was reset or migrated.
- Local test and validation outcomes are recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.8.md`; remote CI, Pages deployment and physical-device acceptance remain separate gates.

## v2.95.5 — Robot Buddy duplicate progress output regression guard
- Added an executable DOM-level regression for both explicit progress analysis and natural-language insight requests.
- The test invokes the real dashboard renderer and both entry points, confirming each request creates exactly one visual dashboard, one set of three totals, and no second prose summary repeating the same progress.
- Registered the new JavaScript regression in GitHub Actions. No learner progress, Robot dialogue library, insight thresholds or dashboard calculations were changed.

## v2.95.4 — TTS A–D one-second cadence regression guard
- Hardened the Listening/Reading TTS regression to assert the exact 1,000 ms pauses before answer-option sets, after each spoken A/B/C/D label, and between an option and the next label across Listening Parts 2–4, Reading Parts 5–7 and Guided Mock playback.
- Kept the intentional Part 1 timing contract separate: 1,500 ms after each spoken label and 1,300 ms between descriptions.
- No TTS timing constants or runtime behavior needed changing; the existing one-second contract is now explicitly executable and protected against regression.

## v2.95.3 — Listening / Reading narration sequence correction
- Fixed the shared Listening player to honor `skipLeadIn` when Guided Mock has already spoken its Part transition and lead-in; Mock no longer repeats the Part heading/instruction before the conversation or talk.
- Expanded TTS sequence regression coverage for Reading Part 6 and the Guided Mock Listening handoff, while retaining Parts 1–4 and Reading Parts 5/7 checks.
- No question content, answer keys, voice settings, learner progress, IndexedDB schema or standalone practice sequence changed.

## v2.95.2 — Editorial review regression and CI guard
- Expanded Part 7 editorial unit coverage to reject blank/duplicate answer choices and invalid `answerIndex` types (including booleans and strings), in addition to existing structure and reviewed-scenario checks.
- Added a focused CI guard requiring exactly one dedicated `test_editorial_review.py` execution step and retained workflow path triggers for test/workflow changes.
- Scope is limited to editorial review tests and CI coverage; no learner content, answer keys, progress, IndexedDB, voice, Robot Buddy runtime or dashboard behavior changed.

## v2.95.1 — Robot Buddy page-only shortcut regression coverage

- Kept the existing page-only action implementation unchanged: the delegated Buddy click listener accepts `data-robot-page`, closes the Buddy panel, then navigates to the selected page.
- Strengthened `tools/tests/robot-buddy.mjs` to execute the actual delegated click-listener body and actual `handleRobotCommand()` handler with a page-only `data-robot-page` action. The regression now asserts the panel closes and the exact destination is opened; it no longer relies only on testing action generation or source text.
- Scope is limited to Robot Buddy page-only shortcut dispatch and its regression test. No changes to `editorial_review`, Listening/Reading narration, TTS pause timing, progress-dashboard wording, learning content, or learner storage.
- Release gate: Robot Buddy navigation regression, all registered JavaScript regression suites and repository-integrity preflight must pass locally. Remote GitHub Actions, Pages deployment and physical-device acceptance remain unverified until actually run.

## v2.95.0 — Review-mode recovery, flashcard confirmation layering and interaction regressions

- Fixed the Robot Buddy action delegation so buttons returned with a destination page are handled as well as command buttons. Page actions close the Buddy panel and navigate to the intended module; the progress-insight response continues to render one visual dashboard with its navigation actions inside the dashboard, without repeating a prose summary.
- Fixed Review question selection so built-in Part 5 items remain usable even when a learner has hidden a linked headword from their personal dictionary. The effective personal vocabulary is preferred, missing built-in Part 5 targets are resolved from the immutable release vocabulary, and unavailable selected modes retry through a smart/common practice mode instead of stopping with an empty-question error.
- Corrected the Part 5 recall route to pass an exact question ID only when it still exists in the current bank; stale recall IDs safely fall back to a valid question. The review header reflects the question mode actually opened.
- Fixed the Flashcard completion confirmation stacking context: the assessment-result modal now renders above the focused learning workspace, so the user can confirm a completed 5/10-word quiz without the prompt being obscured by the flashcard panel. Existing confirmation-before-progress-write behavior remains unchanged.
- Updated the Part 5 recall-queue regression to match the safe exact-ID/fallback contract, aligned Robot Buddy and TTS tests with the current UI/runtime behaviour, and added dedicated tests for Part 5 vocabulary resolution, all review-mode fallback routes and modal stacking. CI coverage verifies every Python test module and JavaScript regression suite is invoked by the workflow.
- Preserved vocabulary content, Mock eligibility boundaries, review/Flashcard evidence, existing learner data keys and IndexedDB v1. No learner progress is reset, migrated or uploaded. TOEIC L/R remains the active scope; B1 remains blueprint-only and Speaking/Writing and IELTS stay deferred.
- Local verification is recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.0.md`. Remote GitHub Actions, deployed GitHub Pages and device QA are only considered verified after the user pushes/deploys and reports the actual results.

## v2.94.0 — Voice reliability, Robot Buddy progress dashboard and repository-wide release preflight

- Fixed the `question_evidence` CI regression: stale 401-question assertions were replaced by source-derived inventory and reserve counts. The current audit indexes all 502 TOEIC questions (239 Listening / 263 Reading), and its six unit tests pass.
- Consolidated Text-to-Speech through one `speakText()` and one guarded `speakUtterance()` implementation. Removed duplicate legacy declarations that overrode the guarded path. Playback queues the first utterance synchronously in the tap/click call stack, checks the voice catalogue without a fixed startup delay, retries once with the system voice when a selected named voice fails, and reports start/end watchdog, permission, network and synthesis failures clearly. The retry path ignores stale callbacks from the failed utterance, does not cancel the new fallback queue, and safely handles a throwing voice catalogue or utterance constructor.
- Listening, Reading, Foundation and vocabulary playback use the same local browser SpeechSynthesis engine. Part 1 pacing and inter-speaker pauses are preserved. Regression coverage includes an empty or throwing voice catalogue, selected-voice failure/fallback, stale cancellation/end/error callbacks, a throwing utterance constructor, missing start/end events, cancellation and Reading playback. Actual speaker output still requires device-level acceptance.
- Prevented Robot Buddy input focus from triggering automatic mobile/tablet zoom by keeping the chat input at a minimum 16px font size and adding mobile-friendly tap targets. User pinch zoom remains available.
- Added a one-tap Robot Buddy progress-analysis action to the welcome message and intent flow. The local-only dashboard presents Cần học / Cần luyện / Cần ôn totals plus color-coded, accessible per-module study-coverage bars and evidence notes. Coverage is not course completion or ETS score readiness; no unsupported global percentage is shown.
- Completed bilingual example and sentence-analysis enrichment for 42 examples across the 17 newest Grammar lessons (batches 024 and 025). Earlier Grammar lessons remain on the progressive editorial backlog.
- Added a repository-integrity preflight to GitHub Actions. It checks Service Worker REQUIRED/APP_SHELL/OPTIONAL paths, HTML local references, CSS url() files, static JS imports and data URLs, workflow script/test references, Python test selection, Node suite registration and JSON validity. Current run: 361 local references/data items inspected, zero errors and zero optional warnings.
- Preserved original Batch 024/025 fingerprints as historical release hashes and added separate v2.94 current-source grammar-enrichment fingerprints. Updated the vocabulary identity regression to compare the baseline plus append-only batches 006–013 (1,141 unique canonical headwords), avoiding a stale hard-coded total.
- Corrected the obsolete TTS note claiming every play waits two seconds before audio. Automated test suites and audit tools remain developer/CI controls and are not learner-facing test content; no learner-facing test/debug module was added.
- Preserved IndexedDB v1, existing learner-progress keys and Mock review boundaries. No progress reset/overwrite, external data transfer, new server/API or change to TOEIC L/R-only roadmap scope. B1 remains blueprint-only; Speaking/Writing and IELTS remain deferred.
- Local verification: 33/33 JavaScript regression suites; impacted Python modules pass (question evidence 6/6, TTS readiness 14/14, Grammar example quality 4/4, responsive layout 7/7, Batch 024/025 + vocabulary identity 18/18, project progress 4/4, CI coverage 2/2, repository integrity 1/1); vocabulary and learning-content validators, objective links 339/339, distractor audit, Foundation A2 audit, Part 1 photos 9/9, design profile and repository preflight pass. Complete Python discovery, remote GitHub Actions, Pages deployment and physical-device QA are not claimed.

## v2.93.0 — TOEIC L&R coverage expansion and score-readiness evidence tracker

- Added 9 Grammar lessons / 27 exercises, 8 Listening units / 20 questions (2 Part 2, 3 Part 3, 3 Part 4), and 8 Reading Part 7 resources / 36 questions (4 single passages and 4 double passages).
- Added 4 source-linked vocabulary headwords; US IPA is populated only where a single CMUdict pronunciation is available.
- Added a local-only Full Mock trend tracker. It requires three completed 200-question Full Mocks before showing L/R averages and trend; it never converts raw accuracy into an ETS scaled score.
- Updated objective-resource mapping and added batch integrity/evidence tests. All new Listening and Reading items remain practice-only pending independent review and excluded from Mock eligibility.
- Preserved existing local progress keys and IndexedDB v1. B1 remains design-only; Speaking/Writing and IELTS are deferred.

## v2.92.0 — TOEIC content batch 024: Grammar, Listening and Reading expansion

- Added eight original Grammar lessons with 24 exercises covering business conditionals, reported speech, comparison structures, countability/quantifiers, gerund/infinitive patterns, passive voice, relative clauses and time/deadline prepositions. Lessons are tagged for TOEIC Parts 5/6 and use stable unique choice IDs.
- Added six TOEIC Listening units / 18 questions: three multi-speaker Part 3 conversations and three Part 4 announcements/talks. Each item includes transcript translation, Vietnamese answer rationale and exact transcript evidence. All remain reserve-pending-independent-review and are excluded from Mock eligibility.
- Added six TOEIC Reading Part 7 resources / 27 questions: three single passages (four questions each) and three double passages (five questions each) across HR, shipping, office administration, finance and quality assurance. Each includes Vietnamese translation, four-option questions and source-label/quote evidence. All remain reserve-pending-independent-review and are excluded from Mock eligibility.
- Added `tools/content-batch-024-v2.92.0.json` with SHA-256 fingerprints for all 20 new resources, batch regression tests, and CI registration. Existing baseline resources and question IDs remain unchanged.
- Added a 12-unit Foundation B1 curriculum blueprint defining four-skill outcomes and acceptance gates. B1 is not exposed as a completed or selectable pathway in this release.
- Updated inventory reporting: Grammar 41 lessons / 110 exercises; Listening 113 units / 219 questions; Reading 57 resources / 227 questions. No invented completion percentages are used where total targets are undefined.
- No learner progress reset, localStorage key change, IndexedDB v1 schema migration, vocabulary changes, Mock promotion, API/backend, or external learner-data transfer.
- Independent second-person review of new reserve content, learner validation, remote GitHub Actions, Pages deployment and physical-device QA remain pending.

## v2.91.0 — A2 extended Listening multi-turn and inference upgrade

- Reworked all 13 supplementary A2 Listening clips in place, preserving stable clip/question IDs and the existing `{lessonId}::listening2` progress scope. Each now has six alternating speaker turns and 75–100 spoken words, up from the earlier four-turn, shorter dialogue format.
- Rebuilt the 39 questions into a consistent progression: listening for detail, understanding purpose/context, and inferring the next action. Each question now carries an exact source-turn `evidenceText`; four choices remain unique and answer positions are balanced across the full Foundation Listening bank at A/B/C/D = 25/25/24/24.
- Updated the lesson panel to disclose the six-turn dialogue format. Expanded regression coverage and the A2 assessment audit to check turn count, script length, question-skill sequence, exact evidence snippets, hash registry and isolated progress scope.
- Added a project roadmap status report with defensible coverage figures and explicit review/deployment gates. It does not invent a single overall completion percentage because no approved total denominator or workstream weighting exists.
- Preserved the 23 core Foundation Listening clips / 59 questions, all existing learner progress scopes and localStorage keys, IndexedDB schema v1, 99 TOEIC Listening reserve questions and Mock eligibility. No new backend, API or data transfer.
- New supplementary material remains `pending-independent-review`, practice-only, device SpeechSynthesis (not authentic ETS audio), and excluded from official A2 outcome or Mock eligibility. Learner validation, independent editorial review, remote GitHub Actions, Pages and physical-device QA remain pending.

## v2.90.0 — Foundation A2 supplementary Listening expansion

- Added 13 supplementary A2 listening clips, one for each of the 13 A2 lessons, with 39 new questions. Formats include phone call, announcement, discussion, voicemail, workplace update, safety briefing, directions, invitation, process instructions, planning call, status call, notice and help-desk call. Each clip contains four alternating female/male TTS turns and 50–63 spoken words.
- Added a collapsed “Nghe hiểu mở rộng” panel to each A2 lesson. Playback uses the learner's configured on-device English voices and inter-speaker pause; transcript remains hidden until requested. The UI clearly identifies this as browser SpeechSynthesis, not authentic ETS audio.
- Supplementary attempts use the existing `toeic:foundation-listening-progress:v1` ledger under `{lessonId}::listening2`. Core Listening remains keyed by the original lesson ID. The two evidence streams, draft sets and completion results are separate; no new storage key or IndexedDB migration was introduced.
- Preserved all 23 core Foundation Listening clips, their 59 questions, the v2.75.0 A2 q1/q2 content baseline, and the 99 TOEIC Listening reserve items / Mock eligibility boundary. The Foundation Listening inventory is now 23 core clips / 59 questions plus 13 supplementary A2 clips / 39 questions.
- Added a SHA-256 registry for all 13 supplementary clips and regression coverage for content structure, question IDs, answer keys, format diversity, runtime rendering, scoped evidence, CI registration and project-progress reporting. Listening answer positions are balanced across the full Foundation bank at A/B/C/D = 25/25/24/24.
- All supplementary content remains `pending-independent-review`. It is optional TTS practice only, not an official A2 outcome, CEFR certification, authentic recorded listening or TOEIC Mock content. Independent linguistic review and learner validation remain open.
- No existing lesson/question IDs, localStorage key names, IndexedDB v1 schema, learner progress, vocabulary data, TOEIC Mock pool, APIs or server contracts were changed.

## v2.89.0 — canonical design-profile CI repair & Foundation A2 extended Reading

- Fixed the CI failure in **Validate canonical design profile**. The source `assets/css/app.css` had acquired five fixed small-text selectors whose generated legacy typography-floor list in `assets/css/design-system.css` had not been regenerated. Ran `tools/sync-design-profile.py --apply`; the generated selector block now matches the canonical profile (54 tokens / 400 legacy font-floor selector groups). The exact `--check` command and all six `test_design_profile.py` tests pass locally. No validator was skipped or weakened.
- Added 13 longer A2 extended Reading passages, one per A2 Foundation lesson, with 39 new comprehension questions. Formats include workplace email, memo, comparison note, incident report, team update, notice, directions, invitation, procedure and staff information. Each passage is 90–110 words, has three questions, four unique options, a keyed answer, rationale and an exact `evidenceText` pointer.
- Extended Reading uses distinct IDs `::reading2` and the existing `toeic:foundation-reading-progress:v1` ledger under a scoped lesson ID (`{lessonId}::reading2`). Original 23 Foundation reading passages and their 59 questions remain unchanged; original A2 Reading q1/q2 baselines are still verified. New evidence is shown separately and is not folded into the official/core A2 outcome summary.
- Added a collapsed “Đọc hiểu mở rộng” area in each A2 lesson. Its open/closed state is preserved when a learner selects an answer and the lesson re-renders. The progress label and in-panel note clearly state that this is supplementary practice pending independent editorial review, not A2 certification.
- Corrected the 67% practice-threshold edge case in `foundation-reading-evidence.js`: status comparison now uses the same rounded percentage shown to learners. Thus 2/3 is represented consistently as 67% and meets a configured 67% threshold; unique-question minimums still apply.
- Registered `foundation-reading-extended.json` in Service Worker `REQUIRED` and `APP_SHELL`; added Python content/hash/ID/evidence/integration tests and JavaScript evidence-isolation/UI-state tests to CI. SHA-256 registry protects the complete passage objects.
- Preserved all old Reading IDs, original answer baselines, learner progress, local storage keys, IndexedDB v1 and Mock eligibility. No new API/server, no upload, no migration or reset. All 13 extended passages and 39 questions remain `pending-independent-editorial-review`; their presence does not certify A2 or authorize addition to the TOEIC Mock pool.
- Remote GitHub Actions/Pages and physical-device QA are not claimed as passing until the user pushes this source and verifies the remote run.

## v2.88.0 — Foundation A2 extended writing tasks and portfolio expansion

- Added 13 additional contextual A2 writing tasks, one for each of the 13 A2 lessons. The writing pathway now contains 26 distinct learner-authored production tasks: 13 original `::produce1` tasks and 13 extended `::produce2` tasks.
- Each extended task uses a separate stable ID and includes a workplace/daily-life scenario, 3–4 sentence-form instruction, three task requirements, a writing frame, minimum 20-word response, three task-specific self-review criteria, a model answer, three guided-revision checks and a topic-specific revision hint.
- Extended tasks are shown in a collapsed “Thử thách viết mở rộng” section so the existing lesson remains compact. Each task has independent response, self-rating and revision history in the existing `toeic:foundation-progress:v1` ledger.
- Updated the Foundation A2 writing portfolio, outcome evidence aggregation and Markdown export to recognize both original and extended task IDs. Export remains learner-triggered, local-only and read-only; each task and its revisions are listed independently.
- Added `tools/foundation-a2-extended-production-v2.88.0.json` with the 13 stable IDs, per-task SHA-256 fingerprints and editorial state. The original v2.78.0 and v2.87.0 scenario baselines remain unchanged.
- Updated the legacy revision regression to expect a 26-task A2 portfolio and test coexistence of original and extended tasks. The new content, registry hashes, minimum-word gate, export, aggregation, syntax, CI coverage and preservation rules are covered by tests.
- New extended prompts are explicitly marked `pending-independent-editorial-review`. The A2 pathway is not complete or CEFR-certified: varied Reading/Listening tasks, independent linguistic review and real-learner validation remain open.
- No IndexedDB schema/store/version migration, localStorage key change, existing task ID replacement, progress reset/overwrite, automated grammar grading, external transfer, vocabulary corpus change, TOEIC question-bank change or Listening reserve approval change.

## v2.87.0 — Foundation A2 writing portfolio export & task-direction quality repair

- Added a learner-initiated Markdown export to the local A2 writing portfolio. The export contains only saved A2 task context, learner-authored initial responses and revisions, task-specific self-ratings/revision checks, and the authored model answer for reference. It is generated entirely on-device and is not sent to any server or third party.
- The export preserves revision order, timestamps, word counts, self-assessment labels and the response used as the revision source. Embedded Markdown code fences in learner text are handled without breaking the exported document. The export builder is a pure function and does not mutate the progress ledger.
- Corrected the scenario direction in `a2-polite-requests`: the learner now needs the colleague to send the meeting notes, matching the task instruction, requirements, sentence frame and model answer. The task ID, legacy application task, question bank, learner progress and answer logic are unchanged. The v2.78.0 baseline remains intact; a v2.87.0 fingerprint refresh records the exact one-field change.
- Added a dedicated export regression suite and registered it in GitHub Actions. Strengthened A2 production-task checks for task requirements, rubric/checklist completeness, required model-answer features, minimum response length and the scenario/instruction alignment.
- No IndexedDB/localStorage schema or key changes, no progress migration/reset, no automatic grammar scoring, no TOEIC or CEFR mastery claim, no vocabulary/question-bank change, and no change to the Listening reserve-to-Mock approval boundary.
- Local verification: 31/31 JavaScript regression suites; 54/54 focused Python tests; CSS parse 0 errors; vocabulary validation 1,137 records / 0 errors / 0 warnings; learning-content validation 0 errors / 0 warnings; PWA readiness, CI coverage and version sync pass. Browser visual/device QA, remote GitHub Actions and Pages deployment are not claimed.

## v2.86.0 — Robot Buddy conversation layout isolation & persistent quick prompts

- Fixed the flex-layout regression where a growing conversation could compress the quick-prompt selection area. The message log now owns its own scroll region and may shrink within a bounded range; the quick-prompt menu, composer, typing indicator and privacy footer are non-shrinking siblings.
- Kept the quick-prompt menu visible and reusable throughout the current conversation instead of hiding it after the first sent message. The prompt area has its own maximum height and internal scroll so it cannot push the input or footer out of the panel.
- Reduced the privacy-note type from 7.5px to 6.5px and tightened its line-height/padding while preserving the offline, pre-authored-dialogue, local-only and no-external-transfer explanation.
- Added a dedicated Robot Buddy layout regression test and registered it in GitHub Actions coverage. Corrected an inherited malformed reduced-motion CSS rule for Listening cards so the preference is applied validly.
- Preserved the dialogue library, Learning Insights evidence thresholds, all learner content, stable IDs, IndexedDB v1, local progress keys and all existing onboarding/reminder settings. No new API, server or external transfer is introduced.
- Local source checks are documented in `reports/TEST_REPORT_TOEIC_Dictionary_v2.86.0.md`. Automated browser screenshots and physical-device validation could not be completed in this workspace; GitHub Actions and Pages deployment remain unverified.

## v2.85.0 — Robot Buddy polished layout & one-tap learning actions

- Rebuilt the Robot Buddy header as two clear rows: Robot name, TOEIC companion/offline status and close control remain together; the progress-analysis and reminder on/off controls sit below without pushing the title out of alignment.
- Enlarged the quick-prompt selection area and tap targets. Tightened the privacy footer while preserving the essential offline, local-only and non-generative-chatbot explanation.
- Robot replies now emphasize **Robot Buddy**, **TOEIC Dictionary** and **Vũ Nguyễn Hoàng Phúc** using safe DOM text nodes and `<strong>` elements; user messages and untrusted text remain plain text.
- Added up to four contextual navigation shortcuts after a progress analysis. Shortcuts are based only on categories and example areas actually returned by the local insight aggregator; they open existing app pages and do not alter learner records.
- Reminder and progress-analysis controls now present explicit Bật/Tắt states with accessible pressed state. Existing reminder preference semantics and `toeic:robot-buddy-settings:v1` are preserved.
- Preserved the offline dialogue library, all learning content, stable IDs, local storage keys, IndexedDB schema v1 and Service Worker shell. No learner progress is written, migrated, uploaded or reset.
- Local checks: Robot Buddy unit/regression suite, runtime render/migration smoke, JavaScript syntax and focused responsive/design/version checks are recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.85.0.md`. Browser visual QA, physical-device QA, GitHub Actions and Pages deployment remain pending.

## v2.84.1 — Robot Buddy Learning Insights & Knowledge Expansion

- Restored Robot Buddy learning-progress analysis using snapshots already loaded by the app from IndexedDB v1 and existing local progress stores. The Robot itself does not open IndexedDB or localStorage and receives only in-memory read-only snapshots.
- Added the three action buckets: **Cần học** (no completed evidence yet), **Cần luyện** (sufficient attempts with low/unstable accuracy), and **Cần ôn** (items whose existing review schedule is due). Sparse evidence is reported as insufficient rather than a weak-skill conclusion.
- Added a user-controlled progress-analysis toggle. Turning it off preserves normal dialogue, feature help and navigation.
- Updated “Bạn là ai?” with the developer introduction and a clear statement that Robot Buddy is scripted/offline, not a generative online chatbot. Learner progress is not sent to an API, server, Google AI or third party.
- Updated Robot's local privacy metadata, quick prompts and the in-app privacy explanation. Kept the 500 unique authored dialogue variants and the head-only SVG mascot.
- Registered `robot-learning-insights.js` in Service Worker `REQUIRED` and `APP_SHELL`; cache and release version moved to 2.84.1.
- Preserved IndexedDB schema version 1 and every existing learner-progress key. No progress migration, rewrite or deletion is performed by this release.
- Local test status is recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.84.1.md`. GitHub Actions, Pages deployment and physical-device checks remain pending until the user publishes and verifies the release.

## v2.84.0 — Head-only Robot Buddy & Offline Dialogue Library

- Replaced the former progress-aware Robot with a single head-only SVG mascot. Multiple expression states drive eye, pupil, eyebrow, mouth and antenna animations; reduced-motion preferences are respected.
- Added a bundled local content library with **500 unique messages** across greeting (60), encouragement (100), caring (60), learning (80), help (100), reaction (60) and rest (40), plus 55 feature-help messages for 11 app destinations, six FAQs and 12 quick prompts.
- Added offline keyword-intent recognition and feature navigation. Free-text replies are intentionally limited to authored topic groups; unknown questions receive a clear fallback rather than a false claim of open-ended AI understanding.
- Added quiet idle bubbles after 90 seconds, then 5- and 10-minute spacing, at most three notices per rolling hour, automatic dismissal, snooze and mute control. Idle prompts are suppressed during timed Mock Exams, active focus/modal dialogs, text entry, speech playback and hidden/unfocused tabs.
- First-run onboarding offers the existing Placement Diagnostic or skip. Robot stores only this choice and idle-mute preference in `toeic:robot-buddy-settings:v1`; a one-time migration reads only the v2.83 onboarding-choice key to avoid asking existing users again. It does not read the Placement result or any learner-progress store.
- Strict separation: no IndexedDB, vocabulary-progress, Flashcard, Grammar, Reading, Listening, Foundation, Mock score or personal vocabulary reads; no external API, Google AI or server; no persisted conversation transcript.
- Preserved the original v2.79 feature-level Google AI entry points outside Robot Buddy. Retired the v2.83 learner-progress assistant as a no-op compatibility tombstone.
- Added the runtime and dialogue JSON to Service Worker `REQUIRED` and `APP_SHELL`; cache version synchronized to v2.84.0.
- No vocabulary, question-bank, learning curriculum, TTS, Placement assessment logic, Mock engine, learner progress keys or IndexedDB v1 changes.
- Local validation and release status: see `reports/TEST_REPORT_TOEIC_Dictionary_v2.84.0.md`. Remote GitHub Actions, Pages deployment and physical-device QA remain unverified until tested after push.

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

### v2.95.25 — audit refinement continuation
- Enhanced the read-only related-glossary candidate audit with canonical-sense previews, single-/multi-sense review tiers, and reconciled glossary-definition categories.
- Candidate audit now separates 229 missing English definitions, 73 placeholder definitions, and 128 non-placeholder definitions (430 total entries); previews are review-only and do not copy definitions.
- Expanded focused tests from 3 to 4, including tier structure and definition-category reconciliation. No app UI/runtime or learning data changed.

## v2.95.26 — glossary quality audit hardening
- Quality audit now flags missing Vietnamese glosses, malformed rows and normalized duplicate terms without merging or editing records.
- Supports a structured JSON report alongside Markdown; deterministic index references help review entries without changing source data.
- Added regression tests for duplicate normalization and malformed input handling.

## Package verification — v2.95.37

- FullSource: **556 files**.
- Update Patch: **35 entries** (22 changed + 13 added), **0 deletions**.
- Patch replay on v2.95.36: **556/556 files byte-for-byte identical** to v2.95.37 FullSource.
- ZIP CRC, one-root structure, excluded-path policy and SHA-256 verification: PASS.

## v2.95.36 — Related Glossary Definition Recovery (Batch 032)
- Added Cambridge-sourced, paraphrased definitions and POS for six existing related-glossary terms: account, acknowledgment, acquire, adaptable, advance, advantage.
- Preserved all six Vietnamese meanings, term identities, glossary ordering, and vocabulary/question/progress data.
- Added Batch 032 ledger and regression tests. Independent review of these definitions remains pending; source excerpts/pages were inspected during preparation.

### v2.95.46 — Toast / CI diagnostic candidate (2026-11-24)
- Success/error toast notifications can now be dismissed manually; accessible roles, focus styling and text wrapping added.
- Toast regression test added. Local targeted checks pass; full test suite timed out, so this remains a candidate and is not production-accepted.

## v2.95.50 — Related Glossary sourced enrichment batch 039

- Enriched 12 existing relation-target glossary rows (`plan`, `neglect`, `amount`, `bill`, `customer`, `division`, `essential`, `file`, `gain`, `loss`, `meeting`, `refuse`) with Cambridge Dictionary-backed paraphrased definitions and reviewed POS labels.
- Each row now carries a Cambridge Dictionary source URL and source release provenance; sense-alignment notes are preserved in `patches-related-terms/v2.95.50/batch-039-glossary-ledger.json`.
- Updates use exact old-value guards and a base-file SHA-256. The regression reconstructs the original glossary byte representation and verifies the patch base hash.
- No vocabulary headwords, sense identities, synonym/antonym edges, questions, answer keys, Mock eligibility, learner records, IndexedDB schema, UI layout or hosting architecture changed.
- Independent editorial review remains pending; source lookup is not a substitute for final human approval.
