# TOEIC Dictionary v2.15.1 — Runtime Hotfix Test Report

- **Release:** v2.15.1 — Reading/Grammar Runtime Hotfix & CI Runner Maintenance
- **Date:** 10/11/2026
- **Baseline:** v2.15.0 Distractor Quality Audit
- **Scope:** fix undefined-variable rendering in Reading and Grammar; harden Part 5 card word count where no passage exists; update GitHub Actions action majors and runner pin. No content or personal progress schema changes.

## 1. Defect analysis and fixes

### Reading `ReferenceError: item is not defined`

`openReadingDetail(id)` iterates `reading.questions` and `q.choices` but used `item.part` in the choice template. There is no `item` binding in that function. The choice template now renders `escapeHtml(choice)` directly; Reading options are no longer suppressed by a Part 1-only conditional copied from Listening.

### Grammar sibling defect

`openGrammarLesson(id)` had the same out-of-scope `item.part` reference while rendering Grammar choices. It now renders `escapeHtml(choice)` directly.

### Part 5 Reading card fallback

Part 5 resources intentionally use incomplete sentences and do not require a `passage` field. The old fallback expression called `item.passage.split()` when `wordCount` was `0`, which could throw. The card renderer now derives text from `passage` or `documents[]` safely, then calculates a fallback word count without dereferencing an absent string.

## 2. Regression tests

**129/129 test methods PASS** (126 existing v2.15.0 methods + 3 v2.15.1 runtime regression methods).

| Suite | Test methods | Result |
|---|---:|---|
| Baseline ID integrity | 13 | PASS |
| Guarded patch engine | 11 | PASS |
| Version synchronization | 12 | PASS |
| Vocabulary validator regression | 33 | PASS |
| Learning content | 24 | PASS |
| Dashboard layout | 6 | PASS |
| Shared design system | 13 | PASS |
| Answer-to-source evidence | 4 | PASS |
| Distractor quality / answer-index safety | 5 | PASS |
| Saved-choice history compatibility | 5 | PASS |
| Reading/Grammar runtime scope | 3 | PASS |
| **Total** | **129** | **PASS** |

The slow subprocess-based methods in the version-sync and validator suites were accounted for through independent test-method runs in the sandbox when grouped module execution exceeded the tool time limit. This report does not claim a single combined test-discovery process passed.

`tools/tests/test_learning_detail_scope.py`: **3/3 PASS**

- Grammar detail renderer contains no out-of-scope `item` reference.
- Reading detail renderer contains no out-of-scope `item` reference.
- Part 5 Reading card word count supports records without passage text.

`node --check assets/js/app.js`: PASS.

`node tools/tests/runtime-render-smoke.mjs`: PASS — thực thi renderer Reading Part 5 (không passage), Reading Part 7 (multi-document) và Grammar qua Node VM mocks; xác nhận choices được render và không có ReferenceError.

## 3. Validators

On v2.15.1 after the runtime-only changes:

- `python tools/validate-data.py`: PASS — 928 records, 0 errors, 12 known legacy warnings (DF005=3, EX006=1, FD001=8).
- `python tools/validate-learning-content.py`: PASS — 0 errors, 0 warnings; Listening 102, Reading 109, Grammar 25 lessons / 54 exercises.
- `python tools/audit-toeic-coverage.py`: PASS; report generated for v2.15.1.
- `python tools/audit-question-evidence.py`: PASS; all 211 question keys remain mapped.
- `python tools/audit-distractors.py`: PASS; 132 reviewed questions and 12 documented option-group edits remain unchanged.
- `python tools/sync-version.py --check`: PASS.
- JavaScript syntax: `node --check` passes for app.js, sw.js and the other application JS modules.
- Vocabulary JSON and learning content are untouched by v2.15.1.

## 4. CI workflow maintenance

- `actions/checkout@v7`
- `actions/setup-python@v7`, Python 3.12 retained
- `actions/setup-node@v7`, Node.js 24
- `runs-on: ubuntu-24.04` pinned for deterministic runner behavior during the `ubuntu-latest` migration to Ubuntu 26.04.
- Added the new scope regression suite to the workflow.

The historical Actions run supplied by the user shows a job exit code 1 and Node 20 / `ubuntu-latest` deprecation notices. Those notices are not sufficient to identify the failing command. Detailed step log output was not accessible in the current environment. `validate-data.py` passes locally on v2.15.1; therefore this report does not claim an unverified root cause for the historical remote failure. A new remote run is required to confirm the updated workflow on GitHub-hosted runners.

## 5. Static shell and package QA

- Workflow YAML parses successfully; 206 HTML IDs are unique; all 74/74 Service Worker `APP_SHELL` resources exist.
- All 52 Markdown documents are under `docs/`; none are at repository root.
- Final ZIP: 169 files; CRC PASS; clean extraction comparison 169/169 exact.
- All 31 JSON files under `data/vocabulary/` are byte-identical to v2.15.0.

## 6. Preservation and release boundary

- No vocabulary record or ID changed.
- No Listening/Reading/Grammar question, answer key, option text, question order or correct answer index changed.
- No IndexedDB schema/object store migration, progress reset or personal data rewrite.
- Remote CI, GitHub push, Pages deployment and physical-device/browser interaction QA remain pending.
