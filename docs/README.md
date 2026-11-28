# TOEIC Dictionary v2.95.85 — Project Documentation

This documentation describes the current TOEIC-first GitHub Pages candidate. Source changes and release evidence are tracked separately from hosted CI, Pages deployment, installed-PWA behavior and physical-device acceptance.

- Current release: `2.95.85`.
- Owner-confirmed source acceptance: `reports/RELEASE_ACCEPTANCE_v2.95.85.md` — records the exact source baseline SHA, 865/865 unit-test result, build/syntax-lint result, source inventory and acceptance boundaries. The 865-test result is owner-supplied evidence; it is not presented as an independently rerun test log.
- Learning outcome evidence: `reports/TOEIC_LEARNING_OUTCOME_EVIDENCE_v2.95.85.md` — 26/27 TOEIC criteria instrumented across 1,163 stable question-to-criterion links and 651 unique stable question IDs; one criterion (`listening-part-1-paraphrase-recognition`) remains deliberately uninstrumented.
- Major release data-quality audit: `reports/MAJOR_RELEASE_QUALITY_AUDIT_v2.95.85.md` — vocabulary enrichment, morphology, glossary and resource coverage inventory. These measurements are not editorial approval or learner mastery.
- Outstanding human review: `reports/OUTSTANDING_REVIEW_HANDOFF_v2.95.83.md` — Part 1 photo verification and Part 7 independent second-review queue.
- v2.95.85 expands canonical vocabulary via Batch 029 (`+60` headwords → **1,281** total; `1221` migration repair profile added and all historical profiles updated), adds 3 `mockEligible: false` Part 4 talk-purpose items (`listening-part-4-talk-purpose` **7 → 10**, Mock Listening remains **102** / Part 4 **30**), instruments `reading-part-7-paraphrase-inference` with **12** verified non-reserve items (**1,163** links across **651** unique question IDs; **26/27** TOEIC and **32/33** overall criteria instrumented), and surfaces read-only criterion revision priorities in `assets/js/learning-outcome-progress.js` and `assets/js/app.js`.
- v2.95.84 fixed Mock UI pool/part counting (`mockPoolCount` and `eligibleByPart` in `assets/js/app.js` via `countMockPool` / `isQuestionMockEligible` in `assets/js/mock-engine.js`) so practice-only Part 4 questions (`mockEligible: false`) stay excluded from displayed Mock counts (102 Listening / 30 Part 4), and added 9 verbatim audio-backed purpose mappings (`listening-part-3-conversation-purpose` 7 → 11; `listening-part-4-talk-purpose` 2 → 7).
- Part 4/6 evidence batch (v2.95.83): `reports/PART4_PART6_EVIDENCE_BATCH_v2.95.83.md` — 10 new practice-only Part 4 questions and 10 reviewed Part 6 discourse mappings.
- Historical GitHub Validate / Pages evidence is listed below for its exact historical commit SHAs only. It must not be generalized to the v2.95.85 source SHA or subsequent commits:
  - Exact candidate source/test HEAD `ad6401282fdb6cf86e2321339ee4181d2fc2fb21`: GitHub Validate [run 46120842790](https://github.com/vuphuc1996/Toeic/actions/runs/46120842790) **PASS** (151/151 steps; 855 Python tests PASS); GitHub Pages [run 46120842377](https://github.com/vuphuc1996/Toeic/actions/runs/46120842377) **PASS**.
  - Exact candidate source/test HEAD `047781760d0c34788e9153cc402efdec605c3d5f`: GitHub Validate [run 46118675768](https://github.com/vuphuc1996/Toeic/actions/runs/46118675768) **PASS** (151/151 steps; 853 Python tests PASS); GitHub Pages [run 46118675714](https://github.com/vuphuc1996/Toeic/actions/runs/46118675714) **PASS**.
- Criterion map audit: `../tools/audit-objective-criterion-map.py` — checks exact question IDs, question indices, Listening reserve exclusion, Part 7 multi-document source quotes and review gates.
- Criterion mapping remediation: `reports/CRITERION_MAPPING_REMEDIATION_v2.95.80.md` — 21 additional links; explains why below-minimum criteria remain below 10.
- Project progress history v2.95.76: `reports/PROJECT_PROGRESS_v2.95.76.md` — prior weighted build index 57.07%.
- Current version ledger: `versions/CURRENT_VERSION.md`.
- Master project status: `MASTER_STATUS.md`.
- Assessment completion and draft/commit semantics: `ASSESSMENT_FLOW.md`.
- Changelog: `CHANGELOG.md`.

## Content and learner-data boundaries

- Batch 029's 60 new headwords are original editorial additions. IPA is left blank pending source verification; CEFR labels are editorial estimates; no Word Family links are inferred.
- Listening source, question and choice IDs, answer keys and question eligibility must remain stable unless a separately reviewed content change explicitly authorizes an update.
- Listening reserve (193), Reading Part 7 reserve (87) and Separate Part 5 review-only (80) remain excluded from Mock.
- Existing canonical vocabulary IDs/headwords/senses and learner IndexedDB v1 schema/records must be preserved.
- UI/UX layout, navigation, Robot Buddy access boundary and GitHub Pages-only/offline architecture remain unchanged. No backend or Cloudflare service is introduced.
- Criterion evidence is recorded in the existing learner-local `objectiveProgress` ledger without an IndexedDB schema migration. Grammar and Reading Part 5 explanation rubrics are optional learner self-reports.

## Acceptance boundary

Source release, candidate CI, Pages deployment, installed-PWA cache/offline propagation and physical-device QA are separate acceptance gates. Do not infer one from another. The v2.95.85 report records owner-supplied source-level verification; hosted CI and Pages results must be checked against the exact current commit SHA.
