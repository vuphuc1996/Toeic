## v2.95.45 — Merge alternate-source QA infrastructure + glossary sense reconciliation

- **Source comparison:** compared the user-uploaded alternate v2.95.44 FullSource (683 files) against the released v2.95.44 FullSource (664 files): 46 upload-only paths, 27 release-only paths, 43 changed common files and 594 byte-identical common files. The upload is a distinct branch, not a drop-in replacement.
- **Adopted engineering improvements:** imported `tools/run-python-tests-sharded.py` and its 12 tests, plus `tools/run-release-acceptance.py` and its 10 tests. Sharded execution isolates modules, kills descendant process groups on timeout, writes a version/inventory-bound checkpoint, resumes only modules already proven PASS, and preserves failed/timeout output. Release Acceptance runs ordered local gates, resolves the version from `data/manifest.json`, writes consistent JSON/Markdown version metadata and terminates timed-out child process groups through the shared sharder helper.
- **Batch 038 content:** adds five Cambridge-sourced terms already used by existing relations: `ask for` (request), `change` (transition), `comments` (feedback), `communicate with` (contact) and `connection` (network). Each record has POS, a paraphrased English definition, Vietnamese lookup meaning and Cambridge URL. Independent editorial approval remains pending.
- **Sense corrections:** `caller` now selects the visitor sense to match canonical anchor `visitor`; `article` selects the object sense to match `item`; `assume` selects responsibility/control to match `undertake`. These are exact-guarded field updates with old/new provenance retained in the Batch 038 ledger. Cambridge also lists other senses for these words; those senses are deliberately not mixed into the relationship-aligned lookup record.
- **Glossary:** 567 rows / 567 normalized unique / 0 duplicates; exact coverage 556/804 (69.2%); 248 unique terms / 249 relation occurrences remain uncovered. `consideration` was not imported because it is a noun derived from linked verb `consider`; it remains an editorial candidate rather than being presented as a synonym.
- **Protected content:** canonical A–Z vocabulary files, IDs and relationships; Grammar/Listening/Reading/Part 5 banks; question/choice IDs and answer keys; learner IndexedDB schema/progress and Mock eligibility remained unchanged. No UI redesign or backend/Cloudflare runtime added.
- **Tests:** new merge suite 8/8, sharded-runner suite 12/12, release-acceptance suite 10/10, CI coverage 3/3, Batch 034 6/6, Batch 027 5/5, Batch 037 7/7, Batch 036 6/6 and Batch 035 5/5 passed. Broader Python shard and local release acceptance outcomes are documented separately; no aggregate status is inferred from partial runs.
- **External gates:** remote GitHub Actions, GitHub Pages deployment/cache, browser/device acceptance and independent editorial review are not claimed unless the current report contains direct verification.
- **Artifacts:** Full Source/Patch v2.95.45, replay comparison, SHA-256 and package verification recorded in `reports/CHANGE_MANIFEST_v2.95.45.md` and `reports/PACKAGE_VERIFICATION_v2.95.45.md`.

## v2.95.43 — Related Glossary batch 036

- **Implemented:** 11 new sourced glosses for uncovered synonym/antonym targets: able, accuracy, actual, assume, business, caller, capable, car, carry, choice and company. Related Glossary **535 → 546**; exact unique coverage **524/804 → 535/804**; uncovered unique terms **280 → 269**; occurrences **281 → 270**. No duplicates.
- **Research/provenance:** Cambridge Dictionary search-index excerpts reviewed 2026-11-23; definitions paraphrased and Vietnamese glosses curated; direct Cambridge page fetches returned 403. Independent review remains pending; sources linked in records.
- **Integrity:** Batch 036 adds six tests including canonical vocabulary and protected learning-bank SHA-256 guards. Batch 035 historical base reconstruction now removes later additive ledgers dynamically. CI registers Batch 036 and syntax checks.
- **Preservation:** A–Z vocabulary file bytes and learning bank bytes were hash-verified unchanged; no headword IDs/relations, questions, choice IDs/answer keys, learner IndexedDB, UI, Mock eligibility or Robot Buddy permissions changed.
- **Local validation:** Batch 036 6/6; Batch 035 5/5; patch updater 11/11; CI coverage 3/3 (after CI-step correction). Remaining release checks are recorded in v2.95.43 report.
- **External gates:** remote GitHub Actions, GitHub Pages deployment, browser/device QA and independent editorial review not verified.
- **Artifacts:** batch ledger and guarded patch under `patches-related-terms/v2.95.43/`; report `reports/TOEIC_GLOSSARY_BATCH_036_v2.95.43.md`. Full Source 641 files; Patch 39 files (18 modified + 21 added, 0 deletions); actual replay 641/641 exact; ZIP CRC/root/exclusions and SHA-256 sidecars verified.


## v2.95.42 — Related Glossary coverage expansion (Batch 035)

- **Implemented:** 8 new sourced glosses for relation targets: administer, alert, alike, appeal, article, assist, backer, bargaining.
- **Source/provenance:** Cambridge Dictionary indexed entry excerpts reviewed 2026-11-22; direct entry pages returned HTTP 403; definitions paraphrased; direct source URLs retained per record. Editorial review pending.
- **Impact:** Related Glossary grows 527 → 535 entries; normalized duplicates remain 0; the 8 added terms are relation targets not canonical A–Z headwords.
- **Preservation:** no canonical vocabulary, IDs, relations, learner records/IndexedDB, learning question/answer keys, Mock eligibility, UI or deployment configuration changed.
- **Verification:** Batch 035 data/provenance regression and current coverage/audit tests; broader validators and package replay are listed in the release report.
- **External limits:** GitHub Actions, Pages deployment, browser/device QA and independent editorial approval not verified.
- **Coverage change:** 516/804 (64.2%) → 524/804 (65.2%); 280 unique / 281 occurrences remain uncovered; 73 placeholder English definitions remain.
- **Current reports:** `reports/TOEIC_GLOSSARY_BATCH_035_v2.95.42.md`, `reports/RELATED_GLOSSARY_CANDIDATE_AUDIT_v2.95.42.md`, `reports/RELATED_GLOSSARY_QUALITY_FLAGS_v2.95.42.md`, `reports/VOCABULARY_RELATIONSHIP_GRAPH_AUDIT_v2.95.42.md`, `reports/PROJECT_PROGRESS_SNAPSHOT_v2.95.42.md`.
- **Package:** Full Source 620 files; Patch 40 overlay files (17 modified + 23 added, 0 deletions); CRC/root/exclusion PASS; actual patch replay 620/620 exact; SHA-256 sidecars verified.

## v2.95.41 — Listening reserve inventory regression correction

- **Current canonical Listening inventory:** 145 units / 295 questions: 102 eligible for Mock and 193 reserve-pending independent review. By Part, eligible = P1 8 / P2 25 / P3 39 / P4 30; pending = P1 1 / P2 36 / P3 84 / P4 72.
- **Root cause:** `test_answer_position_balance.py` retained the 161 reserve / 263 total values from before v2.95.37 Batch 027. Batch 027 added 16 reserve resources / 32 original-editorial questions (P2=8, P3=12, P4=12), now included in the canonical 295-question pool.
- **Fix:** the test now asserts per-Part eligible and pending counts, total 295, Batch 027's 32 questions and its fail-closed reserve status. Existing 27-key move / stable choice identity checks and choice-ID uniqueness checks remain in place.
- **CI:** existing GitHub Actions test step for `test_answer_position_balance.py` is retained; CI coverage regression confirms all Python test modules remain registered.
- **Reports regenerated:** Listening Readiness, Editorial Evidence, Distractor Audit, Content Coverage and Project Progress for v2.95.41.
- **Data safety:** no question/choice text, question order, answer key/index, choice ID, resource ID, editorial status, learner progress, IndexedDB, UI or Mock eligibility changed. Reserve questions remain excluded from Mock pending independent approval.
- **Focused verification:** answer-position 4/4; listening expansion 8/8; question evidence 7/7; distractor quality 6/6; Batch 027 6/6; CI coverage 3/3; version sync 12/12. Further command-level and release checks are recorded in `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.41.md`.
- **Package:** `TOEIC_Dictionary_v2.95.41_FullSource.zip`, 597 files; CRC/root/exclusion checks PASS; exact comparison 597/597; SHA-256 sidecar verified.
- **External gates:** remote GitHub Actions, GitHub Pages deployment/cache, browser/device acceptance and second-person review are not claimed.

## v2.95.40 — Major Release Quality Audit 025 metric reconciliation

- **Root cause closed:** the v2.95.25 audit test retained the historical glossary expectation of 519 rows from before Batch 033. v2.95.39 Batch 033 added eight legitimate Cambridge-sourced terms (ability, acceptable, action, accusation, advertise, advise, allow, announce), bringing the canonical glossary to 527 rows.
- **Verified source count:** `data/related-terms.json` contains 527 rows, 527 NFKC/whitespace/case-folded unique terms and 0 duplicate normalized terms. The 519 value was a stale pre-Batch-033 test literal, not evidence of eight invalid rows.
- **Audit contract strengthened:** `relatedGlossary.entries` is explicitly the canonical raw-row count; the audit now also reports `uniqueEntries` and `duplicateEntries`. Relationship joins use the same NFKC/whitespace/case-folding normalization used by the glossary quality audit.
- **Regression corrected:** `test_major_release_quality_audit_025.py` now checks metrics against the canonical glossary file, asserts the v2.95.39 527-row inventory and confirms 0 duplicate normalized terms. The CI workflow continues to run this suite.
- **Batch 034 correction:** one existing glossary definition (`revision`) had drifted from its current exact single-sense canonical headword after the historical Batch 030 snapshot. Its English definition now matches the current canonical sense; Vietnamese meaning, POS, term identity and original source provenance remain unchanged. A hash-guarded update patch and atomic updater were added.
- **Historical-test hardening:** Batch 030 regression now loads only manifest-listed A–Z canonical files (not editorial batch snapshots) and checks current glossary text against current canonical senses, while preserving the historical patch ledger.
- **Reports refreshed:** current Major Release Quality Audit, Learning Outcome Evidence Matrix, candidate glossary audit, glossary backlog and quality flags are regenerated from the v2.95.40 source.
- **Preservation:** no headword or relation array, learner record, IndexedDB schema, question/answer key, UI or Mock eligibility changed. One existing related-glossary English definition was corrected to its current canonical source.
- **Local release gates:** Audit 025 8/8; Batch 030 4/4; Batch 034 6/6; 137/137 focused Python tests across 23 modules; JavaScript 39/39; compileall, validators, version sync, design profile, repository integrity and content audits PASS. Full Python discovery is not claimed because the full `test_validator.py` module exceeded the execution limit.
- **Packaging:** Full Source **587 files**; ZIP CRC/root/exclusion checks PASS; exact source comparison **587/587**; SHA-256 sidecar verified.
- **External gates:** Remote GitHub Actions, GitHub Pages deployment/cache, browser/device acceptance and independent lexical review remain pending.

## v2.95.39 — Related Glossary research batch 033

- Added 8 Cambridge-sourced glosses for previously uncovered relation terms: ability, acceptable, action, accusation, advertise, advise, allow and announce.
- Each addition has POS, English definition, Vietnamese meaning and direct Cambridge Dictionary URL; independent editorial review remains pending.
- No canonical vocabulary IDs, relation arrays, question/answer keys, learner progress, IndexedDB schema or UI layout changed.
- See batch ledger: `patches-related-terms/v2.95.39/batch-033-glossary-ledger.json`.
- Packaging: FullSource 569 files; Patch 28 files (10 added + 18 modified, 0 deletions); exact replay 569/569; CRC/root/exclusions/SHA PASS.

## v2.95.38 — Context-aware related-term explanations

- Fixed learning feedback context so synonym questions only show synonym references and antonym questions only show antonym references; prevents cross-relation evidence from misleading learners.
- Related Glossary fallback explanations now display available POS and English definition in addition to Vietnamese meaning. Missing metadata remains omitted.
- Added 3 regression tests and CI registration.
- Validation: 76 focused Python tests across related-glossary batches, choice history/identity, practice fallback, CI coverage, repository integrity and this change PASS; JavaScript 39/39 PASS; vocabulary and learning-content validators PASS; repository integrity 408 files, 0 errors; version sync PASS. Full Python discovery, remote CI, deployment and physical device QA are not verified.
- No canonical vocabulary, relation arrays, questions/answers, learner progress, IndexedDB schema or UI layout changed.
- Package: FullSource **559 files**; Patch **12 files (9 changed + 3 added)**, no deletions; replay exact **559/559**, CRC/root/SHA PASS.

## v2.95.37 — Listening content expansion batch 027

- Added 16 original-editorial Listening resources / 32 questions (Part 2=8; Part 3=12; Part 4=12). All new content remains independent-review-pending and excluded from Mock.
- Mapped new resources to learning objectives (379/379); listening inventory 145 units / 295 questions; eligible 102, pending 193.
- Updated stale audit/reserve counts and progress reports.
- Verification previously recorded: 121 focused Python tests PASS; 39/39 JavaScript suites PASS; data/content validators PASS. Full Python discovery, remote CI, Pages and device QA not verified.
- No UI redesign, vocabulary IDs, glossary, learner progress, IndexedDB or answer history changed.

## v2.95.35 — Related Glossary provenance recovery (batch 031)

- Recovered canonical sense index 0 for 155 exact single-sense rows; sourceHeadword/sourceRelease for 37 rows; POS for 6 rows. 165 unique glossary rows changed.
- All canonical transfers are exact-headword; multi-sense rows are not assigned a sense index and definitions are not automatically joined. Existing definitions and Vietnamese glosses remain intact.
- Added idempotent exact-match enrichment helper, 5 regression tests and CI registration. Batch 021/022/023/026/027 regression tests now compare original fields while permitting later provenance fields.
- Audit snapshot: 519 entries; missing definitions 156; placeholders 73; missing POS 223; missing source labels 75; normalized duplicates 0.

## v2.95.34 — canonical glossary remediation batch 030

- **Implemented:** 73 related-glossary terms now have English definitions and POS copied exactly from their exact canonical vocabulary headword, only where the canonical entry contains one unambiguous sense.
- **Safety:** Vietnamese meaning unchanged; 519 glossary term rows and normalized identities preserved. Multi-sense matches and unmatched terms deliberately remain pending.
- **Quality:** Full Python discovery 592 PASS / 1 SKIP; JavaScript 39/39 PASS; vocabulary and learning validators 0 errors/warnings; repository integrity 406 files, 0 errors/warnings; version sync PASS. FullSource 527 files; Patch 24 entries / 0 deletions; exact replay 527/527; CRC/SHA PASS.
- **Scope:** no UI, learner profile/progress/IndexedDB, Mock eligibility, or answer data changes.

## v2.95.33 — Related Glossary QC triage

- Quality audit now assigns deterministic review priority: High (definition/placeholder/malformed/duplicate/echo risks), Medium (missing POS, Vietnamese meaning, provenance), Low (short-definition review).
- Read-only report sorted by priority; glossary source data untouched.
- Related glossary quality audit tests: 11/11 PASS.
- Current audit snapshot: 519 entries; 305 flagged (302 High, 2 Medium, 1 Low); duplicate groups 0. Flag counts overlap by entry; priority counts are mutually exclusive.

## v2.95.31 — missing US IPA review queue

- Added source-linked, non-mutating CMUdict review queue for all 80 canonical records missing US IPA: 6 single pronunciation candidates, 49 multi-variant reviews, 25 no exact entry.
- All ARPABET variants are retained; no IPA is automatically applied. 8 focused tests PASS.
- No UI, vocabulary meaning, relations, learner data, or answer keys changed.
- Source package: 494 files; patch replay exact 494/494; CRC and SHA-256 PASS.
- Full Python discovery incomplete due timeout/non-Git extracted package environment. Remote CI, Pages deployment and real-device QA not verified.

## v2.95.30 — missing US IPA research queue

**Phiên bản mã nguồn đang kiểm kê:** v2.95.45

- Added **89** related-term glosses from exact canonical vocabulary matches with complete bilingual senses; multi-sense definitions are joined for reference.
- Related glossary: **430 → 519**. Provenance on each addition: `canonical-vocabulary-senses`, exact source headword, source release `2.95.28`.
- Strict candidate enrichment remaining: **0** of 89. Other unresolved relation terms remain **296 unique** for research; no fabricated definitions added.
- New tool defaults to audit-only, explicit `--apply`; 8 dedicated tests.
- Tests: focused related-glossary/graph 32/32 PASS; JS 39/39 PASS; data/content/integrity/version checks PASS.
- Data validation: 1,141 records, 0 errors / 0 warnings; content validation 0 errors / 0 warnings; repository integrity 403 files, 0 errors / 0 optional warnings.
- No UI, questions, answer keys, learner data, canonical headwords or relation arrays changed. Remote CI, Pages deployment and device QA not verified.

## v2.95.28 verification

- Added read-only relationship graph audit and 8 focused tests; no learner-facing vocabulary/relations changed.
- Focused Python: 39/39 PASS across six suites; JS `.mjs`: 39/39 PASS.
- Data/content/repository/version checks PASS. Remote CI/deployment/device acceptance not verified.


## v2.95.31 — IPA backfill
- Added one source-linked exact CMUdict IPA record (`dispute`) after safe-converter validation.
- Missing IPA count decreased from 80 to 79.
- Safe backfill pipeline is preview-first; only single-variant entries that convert successfully can be applied. Five single-variant candidates still fail conversion and remain review-only; 49 multi-variant and 25 unmatched entries remain unresolved.
- No UI or learning-question data changes.
- Release v2.95.31 package: FullSource 501 files; Update Patch 22 files; patch replay exact 501/501; SHA-256 sidecar verified.

## v2.95.32 — Major content batch 026

- QC completed against v2.95.31: 580 Python tests pass after correcting stale glossary/IPA metric expectations; final post-integration suite 587/587 PASS and 39 JavaScript regression suites PASS.
- Major batch 026: +8 Grammar lessons / 32 exercises, +8 Listening units / 24 questions, +8 Reading Part 7 passages / 24 questions. Total +24 resources / +80 exercise-question items.
- New content is original-editorial practice content with transcript/passage evidence snippets, stable question/choice IDs, source labels and batch hashes. Listening/Reading remain independent-review-pending and excluded from Mock eligibility.
- Post-batch validators: learning-content 0 errors / 0 warnings; vocabulary validator 0 errors / 0 warnings; repository-integrity 405 references / 0 errors / 0 optional warnings; objective-resource audit 363/363; evidence audit 550 questions; review queue 328 items.
- No UI, canonical vocabulary, relation arrays, answer history, learner progress or storage schema changed.
- Packaging verified: FullSource 512 files; patch 39 entries / 0 deletions; replay exact 512/512; CRC and SHA-256 PASS. Remote CI/deployment/device QA not verified.

## Package verification — v2.95.37

- FullSource: **556 files**.
- Update Patch: **35 entries** (22 changed + 13 added), **0 deletions**.
- Patch replay on v2.95.36: **556/556 files byte-for-byte identical** to v2.95.37 FullSource.
- ZIP CRC, one-root structure, excluded-path policy and SHA-256 verification: PASS.

## v2.95.36 — Batch 032 Related Glossary Remediation
- Recovered English definition, POS, and source URLs for six existing terms: account, acknowledgment, acquire, adaptable, advance, advantage.
- Preserved Vietnamese meanings and term identity/order. Added ledger and focused regression tests.
- Cambridge dictionary excerpts/pages consulted; paraphrases added; independent editorial review pending.
- No UI, vocabulary headword IDs, relations, question/answer content, IndexedDB, or learning-progress data intentionally changed.

- v2.95.36 batch 032: sourced, paraphrased English definitions/POS recovered for six existing related glossary entries; Vietnamese meaning preserved. Quality flags: 227 entries (150 missing definitions, 73 placeholders, 217 missing POS, 75 source flags, 0 duplicates). Independent review pending.
- v2.95.36 focused tests 45/45 PASS, JS 39/39 PASS; validators PASS. Full Python discovery timed out and remains incomplete. FullSource 543 files; 19-file Patch replay exact.
