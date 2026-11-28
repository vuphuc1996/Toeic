# Test & Acceptance Report — TOEIC Dictionary v2.95.83

**Target branch:** `candidate`
**Sole predecessor:** `5eb3b736c3252a38702438efbbbc75e74864189a` (v2.95.82)
**Scope:** Part 4 inference/action, Part 6 discourse-purpose, Mock eligibility preservation and independent-review handoff.

| Gate | Required condition | Status |
|---|---|---|
| Part 4 evidence | 10 new non-reserve questions with exact transcript, inference type, answer and rationale | **PENDING CI** |
| Part 6 evidence | 10 mappings to existing questions in four internal-editorial-reviewed resources | **PENDING CI** |
| Canonical map | 1,139 links / 648 unique stable IDs / 25 mapped TOEIC criteria | **PENDING CI** |
| Outcome reconciliation | Foundation 6/6; TOEIC 25/27; total 31/33; two remain uninstrumented | **PENDING CI** |
| Mock integrity | Part 4 approved pool remains 30; Listening approved pool remains 102; exact 25/100/200 Mock totals | **PENDING CI** |
| Practice-only exclusion | All ten new Part 4 items excluded from all Mock modes and pool counts | **PENDING CI** |
| Reserve/review boundary | Listening reserve 193, Part 7 reserve 87, Part 5 review-only 80 remain excluded | **PENDING CI** |
| Release synchronization | manifest/package/HTML/app/Service Worker/mock-engine all point to 2.95.83 | **PENDING CI** |
| Full Python discovery | All discovered Python tests on exact candidate SHA | **PENDING CI** |
| GitHub Validate / Pages | Exact candidate commit passes validation and deployment | **PENDING** |

## Change contract

- The ten new Part 4 questions are practice-only (`mockEligible: false`) and must not enter any Mock mode.
- Existing three-question Part 4 audio blocks, pre-existing questions, choice IDs and answer keys stay unchanged.
- Part 6 mappings reuse existing questions from internally reviewed resources; no source content is edited.
- Part 1 photo review and Part 7 independent second review are not bypassed.
- No Listening reserve, Reading Part 7 reserve or separate Part 5 review-only item is promoted.
- No IndexedDB schema migration, learner data reset, UI redesign or `main` modification.

FullSource ZIP, installed-PWA/offline and physical-device QA remain separate acceptance gates.
