# Test Report — TOEIC Dictionary v2.95.21

## Scope

- Baseline: v2.95.20 FullSource.
- Candidate: v2.95.21.
- Changes: 23 related-term glossary lookup records, provenance/patch tooling, one stale project-progress expectation, release docs and test/CI coverage.
- No UI/CSS/layout/navigation/runtime behavior change.

## Local verification results

| Check | Result | Detail |
|---|---|---|
| Batch 027 glossary regression | **5/5 PASS** | 23 terms, Cambridge source URLs, frequency priority, absent-only provenance patch, unchanged 1,141-word identity set and exact coverage. |
| Batch 026 regression | **5/5 PASS** | Existing previous batch remains compatible. |
| Related-term patch safety | **11/11 PASS** | Guarded patch, duplicate/absent checks and rollback/error handling. |
| Project-progress regression | **4/4 PASS** | Current 412/804 exact coverage and 392/393 missing-gap counts. |
| CI-coverage regression | **3/3 PASS** | New test and compile steps are registered in workflow. |
| Version-sync regression | **12/12 PASS** | Version markers and changelog/document pointers remain synchronized. |
| Focused Python total | **50/50 PASS** | Nine modules: the six main focused suites plus distractor-quality (6), repository-integrity (1) and package-source (3); not the entire Python inventory. |
| Python compilation | **PASS** | `python -m compileall -q tools`. |
| Package-source regression | **3/3 PASS** | One-root ZIP, tracked-only, dirty-tree refusal and version contract tests. |
| JavaScript regression | **38/38 PASS** | Every `tools/tests/*.mjs` suite executed independently. |
| JavaScript syntax | **PASS** | `sw.js` and every `assets/js/*.js` module checked via Node. |
| Vocabulary validator | **PASS** | 1,141 records; 0 IDs added / 0 missing; 0 errors / 0 warnings against the retained legacy baseline. |
| Learning-content validator | **PASS** | Listening 121 units /239 questions; Reading 65 /263; Grammar 50 /137; Part 5 practice 80; 0 errors / 0 warnings. |
| Repository integrity | **PASS** | 393 local references/data files; 0 errors; 0 optional warnings. |
| Listening/Reading evidence audit | **PASS** | 502 indexed questions; 137 Listening reserve items remain pending independent review. |
| Release-integrity Node test | **PASS** | 1,141 canonical headwords and current historical release/patch guards. |
| Version synchronization check | **PASS** | All current app/document version markers report 2.95.21. |

## Aggregate Python suite limitation

`python -m unittest discover -s tools/tests -p 'test_*.py' -v` was attempted with a 240-second execution limit. It did not complete before the limit and stopped while processing `test_patch_data.py`. This is an incomplete run, not a pass or a confirmed test failure. Do not treat the 50 focused cases as the full Python suite.

## Data and review status

- Vocabulary inventory remains 1,141 headwords; stable ID set adds 0 and loses 0 records.
- Related-term glossary: 423 entries; exact case-insensitive join 412/804 (51.2%); occurrence coverage 644/1,037 (62.1%). Remaining: 392 distinct referenced terms / 393 occurrences. Four source-verified two-reference terms were added in the final backlog scan; `disorganize` was deferred for insufficient direct definition evidence.
- The 23 new glosses are provisional lookup content and require independent lexical review.
- Independent review queue remains 280 items: 137 Listening + 63 Reading Part 7 + 80 separate Part 5. Queue inclusion is not approval or Mock eligibility.
- Full test logs and exact commands are indexed in `COMMAND_LOG_INDEX_v2.95.21.md`.

## Not verified / not claimed

- No remote GitHub Actions result, GitHub Pages deployment or production publication.
- No real-browser acceptance, offline/PWA acceptance, multi-tab test or physical iOS/Android/desktop device test.
- No physical TTS/audio-quality assessment.
- No owner manual acceptance; the existing 22-item manual checklist remains uncompleted.
- No independent lexical or exam-content reviewer sign-off.

## Packaging verification

- FullSource handoff: one-root ZIP, 412 project files; local logs, caches and nested archives excluded.
- Incremental update patch: 13 modified files + 12 new files, 0 deletions, compared against the v2.95.20 FullSource.
- Batch 027 was replayed from a clean v2.95.20 `data/related-terms.json` baseline; the resulting file matched the candidate byte-for-byte (SHA-256 `8c063e43e314e247c9fa2b26474afad8861eac1a066a759c787d8a866c0097bb`).
