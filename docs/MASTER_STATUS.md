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

**Phiên bản mã nguồn đang kiểm kê:** v2.95.39

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
- Release v2.95.31 package: FullSource 501 files; Update Patch 22 files; patch replay exact 501/501; SHA-256 verified.

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
