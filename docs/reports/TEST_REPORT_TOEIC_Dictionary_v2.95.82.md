# Test & Acceptance Report — TOEIC Dictionary v2.95.82

**Target branch:** `candidate`
**Sole predecessor baseline:** `4d1eead800e3378cf91b5b83ddb14bc3c8fb8737` (v2.95.81)
**Scope:** Part 2 distractor-resistance evidence and audit hardening; no learner-facing feature or content-bank edit.

## Required acceptance gates

| Gate | Required condition | Status |
|---|---|---|
| Part 2 lexical-distractor mappings | 16 unique existing question keys; all non-reserve | **PENDING CI** |
| Exact source evidence | Prompt matches canonical segments; distractor matches selected wrong choice; repeated cue and mismatch rationale present | **PENDING CI** |
| Answer-key safety | `distractorChoiceIndex` must differ from canonical `answerIndex` | **PENDING CI** |
| Canonical map reconciliation | 1,119 links / 638 unique IDs / 23 mapped TOEIC criteria | **PENDING CI** |
| Outcome reconciliation | Foundation 6/6; TOEIC 23/27; total 29/33; four remain uninstrumented | **PENDING CI** |
| Reserve/review boundaries | 0 Listening reserve links; Part 7 and Separate Part 5 gates retained | **PENDING CI** |
| Version/cache synchronization | 19 single-instance markers; 17 app, 42 SW and 1 mock-engine keys synchronized | **PENDING CI** |
| Full Python discovery | Full discovered inventory on exact candidate SHA | **PENDING CI** |
| GitHub Validate | Exact commit, all steps successful | **PENDING** |
| GitHub Pages | Build, deploy and status-report jobs on exact commit | **PENDING** |

## Change contract

- New mapping rows must reference the canonical source question and existing stable question key.
- Exact wrong option must be a non-answer choice; no answer index or choice identity is changed.
- A mapping row must reproduce the canonical Part 2 spoken prompt and distractor choice; the repeated cue must be present in both.
- Available mapping inventory is not learner mastery. Practice threshold remains at least 10 unique items and 80% latest accuracy.
- No IndexedDB schema migration, learner data reset, UI redesign, Mock promotion, reserve promotion or `main` update is included.

FullSource ZIP creation, installed-PWA/offline propagation and physical-device QA remain separate acceptance gates.
