# Test & Acceptance Report — TOEIC Dictionary v2.95.82

**Target branch:** `candidate`
**Sole predecessor baseline:** `4d1eead800e3378cf91b5b83ddb14bc3c8fb8737` (v2.95.81)
**Scope:** Part 2 distractor-resistance evidence and audit hardening; no learner-facing feature or content-bank edit.
**Verified source/test HEAD:** `ad6401282fdb6cf86e2321339ee4181d2fc2fb21`

## Required acceptance gates

| Gate | Required condition | Status |
|---|---|---|
| Part 2 lexical-distractor mappings | 16 unique existing question keys; all non-reserve | **PASS** |
| Exact source evidence | Prompt matches canonical segments; distractor matches selected wrong choice; repeated cue and mismatch rationale present | **PASS** |
| Answer-key safety | `distractorChoiceIndex` must differ from canonical `answerIndex` | **PASS** |
| Canonical map reconciliation | 1,119 links / 638 unique IDs / 23 mapped TOEIC criteria | **PASS** |
| Outcome reconciliation | Foundation 6/6; TOEIC 23/27; total 29/33; four remain uninstrumented | **PASS** |
| Reserve/review boundaries | 0 Listening reserve links; Part 7 and Separate Part 5 gates retained | **PASS** |
| Version/cache synchronization | 19 single-instance markers; 17 app, 42 SW and 1 mock-engine keys synchronized | **PASS** |
| Full Python discovery | Full discovered inventory on exact candidate SHA | **PASS** |
| GitHub Validate | Exact commit, all steps successful | **PASS** |
| GitHub Pages | Build, deploy and status-report jobs on exact commit | **PASS** |

## Exact-commit hosted acceptance

- GitHub Validate [run 46120842790](https://github.com/vuphuc1996/Toeic/actions/runs/46120842790): **PASS**, 151/151 steps, 0 failures, 0 skipped.
- Full Python discovery: **855 tests PASS**.
- Part 2 source-evidence guard and positive/negative regressions: **PASS**.
- Canonical mapping audit: **PASS**, 1,119 links / 638 unique stable question IDs; 23/27 TOEIC criteria; 0 Listening reserve mappings.
- Outcome and progress reconciliation: **PASS**, Foundation 6/6; TOEIC 23/27; total 29/33; weighted measurable build index 74.49%.
- Version/cache synchronization: **PASS**, 19 release markers; 17 app, 42 Service Worker and 1 mock-engine keys.
- GitHub Pages [run 46120842377](https://github.com/vuphuc1996/Toeic/actions/runs/46120842377): **PASS**, build, status-report and deploy jobs; environment URL https://vuphuc1996.github.io/Toeic/.
- `main` remains unchanged at `256ca21461e78a7685bed773ddd622a64050e33a`. FullSource ZIP generation, installed-PWA/offline propagation and physical-device QA remain separate unverified gates.
## Change contract

- New mapping rows must reference the canonical source question and existing stable question key.
- Exact wrong option must be a non-answer choice; no answer index or choice identity is changed.
- A mapping row must reproduce the canonical Part 2 spoken prompt and distractor choice; the repeated cue must be present in both.
- Available mapping inventory is not learner mastery. Practice threshold remains at least 10 unique items and 80% latest accuracy.
- No IndexedDB schema migration, learner data reset, UI redesign, Mock promotion, reserve promotion or `main` update is included.

FullSource ZIP creation, installed-PWA/offline propagation and physical-device QA remain separate acceptance gates.
