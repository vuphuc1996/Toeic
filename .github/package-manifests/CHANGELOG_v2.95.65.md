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

## v2.95.57 — answer leakage and distractor-overlap diagnostics (2026-11-24)

- Added a deterministic, read-only diagnostic for question-stem lexical cueing, correct-answer/distractor token overlap, and keyed-answer length imbalance across 177 Mock-eligible Listening Part 3/4 and Reading Part 7 questions; both Listening and Reading reserve queues are excluded.
- Current triage flags 6/177 questions: 2 Part 3, 1 Part 4 and 3 Part 7. These are review signals only; long answers and lexical overlap can be legitimate.
- Added six focused Python tests and dedicated GitHub Actions steps for syntax, tests and report generation.
- No question text, answer keys, choice order/IDs, source evidence, Mock eligibility, reserve status, learner data/schema, UI or Robot Buddy scope changed. Listening reserve questions remain excluded.
- The audit is lexical/length triage only; it cannot prove semantic uniqueness, identify paraphrase errors or provide psychometric/ETS calibration.

## v2.95.54 — independent audit Stage 1 remediation (2026-11-24)

- Applied guarded patch corrections: `appliance-n.verb_forms` is now `null`; eight inconsistent headword-level CEFR values now equal the highest CEFR level among their senses. The ninth reviewed item (`package-nv`) already followed this rule and was preserved.
- Added structural validator rule VF003 to reject empty/whitespace-only verb-form strings and CE004 to enforce the aggregate CEFR policy (A1 < A2 < B1 < B2 < C1). Added regression tests; existing rules and baselines were not relaxed.
- Confirmed the Listening reserve queue check is already data-driven in the v2.95.53 baseline and passes against 193 reserve questions; no duplicate change was made.
- Moved the two root-level v2.95.45/v2.95.46 update-note files into `docs/versions/legacy/`; added a full Python `unittest discover` step to CI.
- No IDs, headwords, topics, Vietnamese meanings, relations, question IDs, answer keys, Mock eligibility, UI features or Robot Buddy features changed.
- Independent audit remediation logs and test results are recorded in `docs/reports/INDEPENDENT_AUDIT_STAGE_1_v2.95.54.md`.

# Changelog

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

## v2.95.53 — iPad portrait responsive navigation + cross-module audit (2026-11-24)

- Fixed iPad/tablet portrait navigation: portrait tablet viewports from 641–850 CSS px now use the existing phone-style bottom navigation and mobile content flow; the sidebar is hidden.
- Preserved desktop navigation for landscape iPad Pro 11-inch M1 (approximately 1194 CSS px wide) and larger desktop/tablet landscape viewports.
- Added safe-area-aware bottom navigation, Robot Buddy positioning, modal sizing, and regression coverage for portrait/landscape breakpoint behavior.
- Corrected source/test fingerprint scope for generated Python shard, cross-module/iPad, glossary audit/queue and rendered visual evidence; generated evidence remains packaged and archive-hashed, while governance documents remain fingerprinted.
- No learner data, IndexedDB schema, vocabulary IDs, relation arrays, question IDs, answer keys, or Mock eligibility changed.
- Full cross-module audit and package evidence are recorded in the v2.95.53 release reports.

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
- Validation status is recorded in the v2.95.47 test and package reports.

# Changelog

## v2.95.56 — Listening Mock form-diversity gate (2026-11-24)

- Listening trend readiness now verifies distinct Listening question-ID sets across the three most recent completed Full Mock attempts; repeated attempts using the same Listening form no longer unlock a Listening trend.
- Reading trend calculation remains independent and unchanged. Listening history without question IDs fails closed rather than being assumed to represent an independent form.
- Distinct forms disclose their question overlap; overlap of 90% or more triggers an explicit caution so a nominally different form is not presented as strong independent evidence.
- Existing attempt question IDs are reused as evidence. No new learner-history schema, vocabulary/question content, answer key, choice order, Mock eligibility or IndexedDB change.
- Added regression cases for repeated forms, two distinct forms with 98% overlap, legacy records, Reading independence and Full Mock filtering.


## v2.95.46 — development continuation (2026-11-24)

- Made delayed-recall due-count evaluation deterministic by accepting an optional evaluation timestamp in objective summary functions.
- Added boundary and fallback regression tests.
- No learner data, content IDs, answer keys, IndexedDB schema, UI layout, or deployment configuration changed.
- Validation: focused outcome tests 8/8 PASS; direct Node tests and syntax checks PASS; outcome/resource audits PASS. Full Python discovery timed out at the outer 300-second tool limit after 334 reported test cases; full-suite status remains INCOMPLETE.


## v2.95.46 — learner evidence integrity continuation (2026-11-24)

- Added a read-only objective progress ledger audit with stable issue codes and error/warning severity. It checks ledger shape, objective references, item/attempt timestamps, recall records and explanation rubric history.
- Unknown objectives are reported but retained; the audit never mutates or repairs learner progress. Added a serialization-based non-mutation regression.
- Added `docs/OBJECTIVE_PROGRESS_INTEGRITY.md`.
- No IndexedDB schema, learner data, vocabulary identity/relations, question/answer keys, Mock eligibility, UI or backend changes.
- Verification: focused Node runtime suite PASS; Python wrapper 3/3 PASS; strict Python inventory 89/89 modules (691 PASS, 1 accepted SKIP, no failures/errors/timeouts); local GitHub workflow replay 110/110 PASS. Remote GitHub-hosted CI remains unverified.
