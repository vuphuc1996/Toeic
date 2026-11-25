# TOEIC Dictionary — Master Status

**Phiên bản mã nguồn đang kiểm kê:** v2.95.66

**Current source:** v2.95.66 candidate — versioned PWA shell assets, runtime release-coherence guard, and Batch 022 unittest-discovery correction.

## Current candidate

- Exact predecessor FullSource: `TOEIC_Dictionary_v2.95.65_FullSource.zip`; SHA-256 `a1b95e807e08052bfa599a08ff88bc3237ae086688557ce3ae77b78e814814fb` (779 files). No older archive, Patch or alternate branch is used as the baseline.
- Candidate version markers: `data/manifest.json`, `assets/js/app.js`, `sw.js`, HTML title/sidebar/phase/footer and docs are synchronized to v2.95.66.
- Runtime fix: the app stylesheet, design-system stylesheet and app module use `?v=2.95.66` URLs. The Service Worker REQUIRED and APP_SHELL arrays precache those exact URLs; its registration URL stays stable at `./sw.js` with `updateViaCache: 'none'`.
- Startup guard: HTML `meta[name="toeic-release"]` must match `APP_RELEASE_VERSION`. A mismatch shows a reload notice and returns before `bindEvents()`, preventing the previous null-listener failure from surfacing as an opaque `addEventListener` exception.
- CI fix: Batch 022 validates the actual `unittest discover -p` selector with glob semantics. PWA readiness checks the local file path without treating the release query as part of the filesystem path.
- New `tools/tests/release-asset-coherence.mjs` is explicitly registered in the JavaScript regression step; it verifies manifest/HTML/app/SW version agreement, query-versioned app-shell resources, and bypass of the prior app.js cache key.
- Candidate branch: `fix/v2.95.66-pwa-release-coherence-ci-batch022`. GitHub Pages and full Actions acceptance are pending the pull-request run. Do not describe the candidate as accepted or fully tested until every CI job completes.
- No vocabulary/Related Glossary content, canonical IDs/headwords/relations, question/choice IDs, answer keys, Mock eligibility, learner IndexedDB data/schema, Robot Buddy boundary, visual layout or hosting architecture changed.

## Stage 2 progress

| Audit item | Status | Notes |
|---|---|---|
| 5. Full learner data export/import | Implemented in v2.95.55 | Full IndexedDB workspace + `toeic:` localStorage backup, integrity validation and guarded merge restore |
| 6. Listening reuse / trend integrity | Implemented in v2.95.56 | Listening trend requires two distinct question-ID forms; high overlap is disclosed; Reading remains independent |
| 7. Answer leakage / distractor overlap | Implemented in v2.95.57 | Read-only lexical/length triage; 6 review signals; no answer/content mutation |
| 8. Answer-position skew | Existing implementation verified | Historical controlled reorder certificates retain stable choice identity; 27 changes in v2.17.0 and 6 in v2.33.0 |
| 9. Evidence and difficulty | Structural triage implemented; independent review/calibration open | Source evidence + transparent complexity signals; no CEFR/ETS difficulty claims |
| 10. Learning outcome accuracy | Implemented in v2.95.58 | First-attempt and latest-attempt accuracy are reported separately from the same retained attempt history |

Stage 2: **6/6 workstreams implemented (100%)**; item 9 is structurally instrumented but independent review and psychometric calibration remain external acceptance gates, not marked complete.

## Non-negotiable data boundaries

- The 193 Listening reserve questions and 87 Reading reserve questions remain excluded from Mock until independent approval.
- Across v2.95.61–v2.95.66 candidate, no canonical vocabulary IDs/headwords/meanings/relations, question IDs/choices/answer keys, Mock eligibility, learner-history schema, or Robot Buddy access boundary changed. v2.95.65 modifies only Batch 035 historical test coverage, shared modal shell mechanics, CI registration, design-token selector identity and release documentation; learner IndexedDB stores/schema and records are untouched.
- The v2.95.55 complete learner-data backup and guarded restore remains intact. Existing attempt-history records are read without migration.
- UI layout and navigation were not redesigned.

## Acceptance boundary

For the v2.95.66 candidate, Batch 022 discovery, release asset coherence, PWA readiness and the complete Python/Node test suite are **PENDING hosted Actions**. No full-suite PASS is claimed. GitHub Pages deployment, installed-PWA update/cache propagation, offline startup and real Windows/macOS/iOS/iPadOS/Android behavior remain **UNVERIFIED** until the candidate is merged and device acceptance is recorded.

## Previous completed work

- v2.95.56: Listening Mock form-diversity gate. See `reports/MOCK_LISTENING_FORM_DIVERSITY_v2.95.56.md`.

- v2.95.55: full learner-data backup and guarded restore. See `docs/reports/LEARNER_DATA_BACKUP_v2.95.55.md` and `docs/reports/RELEASE_ACCEPTANCE_v2.95.55.md`.
- v2.95.54: Stage 1 independent audit remediation and release evidence.

## v2.95.59 — item complexity review queue (2026-11-24)

- Added read-only complexity triage for the full Listening/Reading question inventory. Observable signals include source length, prompt length, answer-option length spread, inference/purpose wording and multi-document indicators.
- Does not infer difficulty or CEFR, does not use learner response statistics, and does not modify question content or Mock eligibility.
- Reserve-pending items remain excluded from Mock. Independent review, pilot response data and psychometric calibration remain open.

## v2.95.65 — Batch 035 Cambridge history and single shared modal overlay (2026-11-25)

- Baseline: exact `TOEIC_Dictionary_v2.95.64_FullSource.zip`; SHA-256 `03ec4c80e88bc76e435cfc0782e933474be882a4f271318a23375a35e9242673`.
- Replaced the stale hosted-only `test_related_glossary_batch_035_cambridge.py` with a checked-in historical test that reverses later Batch 036–038 additions and reviewed correction operations before asserting the Batch 035 snapshot/hash. Both modules are selected by `test_related_glossary_batch_035*.py`; 10/10 tests pass locally.
- Removed `modalBackdrop`/`.modal-backdrop`; the modal panel layer is nested within the existing `learningFocusBackdrop`, which is the sole full-screen overlay. Modal-only and active-focus cases preserve their distinct close behavior without duplicating the dimming layer.
- Added overlay contract regression tests and an explicit GitHub Actions test step. Modal dismissal simulation and all Node regression scripts pass. Design-token audit reports zero new violations after documented selector identity reconciliation.
- No learning content or learner IndexedDB data/schema changed. Hosted Actions, Pages deployment and device testing remain unverified.

## v2.95.64 — GitHub commit-readiness and CI reliability (2026-11-25)

- Baseline: exact `TOEIC_Dictionary_v2.95.63_FullSource.zip`; SHA-256 `6d43a7f44e1cc84d6ad7f3ee9dae660cceb83c792668d0966ce1060f4aa9ea80`.
- Added read-only Git commit readiness checks for clean/staged status, path portability/case collisions, symlinks, file size, release artifacts, ignored output paths, LF/binary attributes and whitespace in only the current commit/staged diff (legacy historical trailing whitespace is not mass-edited).
- Pinned official GitHub Actions at verified full SHAs; added `fetch-depth: 2` for the commit-diff preflight and trigger paths for `.gitignore`/`.gitattributes`.
- Repository-integrity audit now recognizes default `unittest discover` `test*.py`; CI coverage detects duplicate module selectors and duplicate workflow step labels. Two duplicate test executions were removed; full tools syntax check now uses `compileall`.
- No learning data or UI/runtime changes. Focused commit-preflight tests are recorded; complete 97-module Python suite started but the container execution window expired after 19 modules had passed. The full suite is therefore **INCOMPLETE**, not PASS. GitHub-hosted Actions and real Windows/macOS clone/commit checks remain unverified.

## v2.95.63 — CI discovery and modal lifecycle remediation (2026-11-25)

- Exact source baseline: v2.95.62 FullSource SHA-256 `b9d56cd27d0d13c4c8781732ac72c17b526b2aa451fa1393c39fd30820260f96`; the older uploaded v2.95.60 archive was excluded.
- Fixed unittest discovery pattern for Batch 035 to `test_related_glossary_batch_035*.py`, covering `test_related_glossary_batch_035_cambridge.py` if present in the CI checkout. Added explicit regression coverage for wildcard semantics and complete Python/Node test inventory registration.
- Repaired safe modal dismissal for result, answer explanation and auto-advance wait states. The result modal keeps the three requested stats; X/Escape commits or saves pending state safely. Closing explanation leaves inline answer feedback; closing the wait cancels auto-next and preserves the current question. Transient overlay state is cleared and focus returns to a visible close control.
- Added `tools/tests/modal-dismissal-workflow.mjs` and registered it in GitHub Actions. No CSS redesign, data change, ID migration or IndexedDB schema change.
- Local Node regression suite: 43/43 PASS. Focused Python suites: 42 test cases PASS across 8 modules (CI coverage 4, repository integrity 1, PWA 3, responsive 8, learning surface 5, practice fallback 6, sync-version 12, source package 3). Syntax and repository/data validators PASS. Complete Python suite and remote/physical deployment checks remain unverified.

## v2.95.62 — Related Glossary Batch 043 (2026-11-25)

- Exact source baseline: v2.95.61 FullSource SHA-256 `63bb04e7f9bbb15fa76ff00ab833b392bf6d48e71ecafd8740b05c2ff1cb56b7`; the uploaded v2.95.60 archive was not used.
- Added paraphrased Cambridge Dictionary definitions/POS/provenance to 21 existing relation-target rows selected via existing vocabulary synonym/antonym anchors. Batch report and per-term ledger record source URLs, sense notes and the independent-review gate.
- Quality audit: 567 rows; 157 flagged (153 high, 2 medium, 2 low); 103 missing definitions, 50 placeholders, 153 missing POS, 52 missing provenance; zero duplicate groups. Relation coverage remains 556/804.
- Preserved all term identities, Vietnamese meanings and relation arrays. No canonical vocabulary or question/choice/answer-key data, learner data/IndexedDB, Mock eligibility, Robot Buddy boundary, UI or hosting architecture changed.
- Definitions use indexed dictionary entry excerpts reviewed 2026-11-25, paraphrased; direct page fetch status was not asserted. Independent editorial review remains pending.
- Local test/validator/package results are in v2.95.62 reports. Hosted CI, Pages, installed-PWA cache/offline and physical-device acceptance remain unverified.

## v2.95.61 — Related Glossary Batch 042 (2026-11-25)

- Development base: exact `TOEIC_Dictionary_v2.95.60_FullSource.zip`; SHA-256 `b4e5404b824991208d99babb3f471b45e9e27fded1d31327854ae3a15ce58838`.
- Added sourced English definitions/POS to 20 existing relation-target rows. Sixteen are Cambridge Dictionary paraphrases; four copy every existing sense definition verbatim from the exact canonical headword in v2.95.60.
- The guarded patch binds to `data/related-terms.json` SHA-256 `dbc233b11ab0b8f351092bb404fe2010f9e54091e2590c5765b68cc1b8d3f97e`. The provenance ledger records exact URLs, source method, POS, sense alignment and relation anchors.
- Quality audit: 567 rows; 178 flagged (174 high, 2 medium, 2 low); 111 missing definitions, 63 placeholders, 174 missing POS, 65 missing provenance; zero normalized duplicate groups.
- Preserved all existing term identities and Vietnamese meanings. No canonical vocabulary/relationship arrays, question/choice IDs, answer keys, Mock eligibility, learner records, IndexedDB schema, Robot Buddy privacy boundary, UI layout or hosting architecture changed.
- Cambridge direct retrieval returned HTTP 403 for some entries; indexed dictionary excerpts were reviewed. Independent editorial review remains pending.
- Local validation and exact package replay are recorded in the v2.95.61 reports; remote CI, Pages and physical devices remain unverified.

## v2.95.60 — consolidated IPA and Related Glossary quality queues (2026-11-24)

- Development base: exact `TOEIC_Dictionary_v2.95.59_FullSource.zip`; SHA-256 `b5dbb4e7c974814c8d59fc6bf653737f7208e7da2c2d49141078efff385d993c`.
- Added a deterministic missing-US-IPA review inventory from exact-headword CMUdict lookup. 79 records: 5 single-pronunciation candidates, 49 multi-variant cases requiring review, 25 with no exact dictionary key. CMUdict package version is recorded; ARPABET remains the evidence format. No IPA was converted or inserted.
- Added a Markdown renderer and regression tests for queue counts, variant display and the no-auto-apply boundary.
- Rebuilt Related Glossary quality and relation-frequency queues: 567 entries; 198 flagged (194 high, 2 medium, 2 low); 131 missing definitions; 63 placeholders; 190 missing POS; 65 missing provenance; 0 normalized duplicate groups.
- Candidate coverage audit: 567 glossary entries, 804 distinct referenced terms, 248 distinct terms / 249 reference occurrences not covered; no canonical candidate was auto-imported.
- The v2.95.59 non-calibrated complexity inventory remains part of the baseline: 582 questions; 280 reserve-pending (193 Listening, 87 Reading); all reserve remain excluded from Mock.
- No canonical vocabulary fields, IDs, headwords, relation arrays, question content/IDs/choices/answer keys, learner data, IndexedDB schema, Mock eligibility, UI layout or hosting architecture changed. This release adds reports/tooling/tests and synchronized release markers only.
- Full hosted Actions, Pages deployment, cache propagation and physical-device acceptance remain unverified.
