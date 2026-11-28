# Test & Acceptance Report — TOEIC Dictionary v2.95.84

**Target branch:** `candidate`
**Predecessor:** stabilized `v2.95.83` (`137160f08cd1ef2b2b505a8af1c9e7ba829b4297` + CI reconciliation commit)
**Scope:** Mock UI pool-count alignment (`mockEligible: false` exclusion), Listening Part 3/Part 4 purpose criterion depth, and release synchronization.

| Gate | Required condition | Status |
|---|---|---|
| Mock UI pool alignment | `app.js` uses `countMockPool` / `isQuestionMockEligible`; displayed Listening pool is 102 (Part 4 is 30), Reading 200 | **LOCAL PASS** |
| Part 3/4 purpose depth | `listening-part-3-conversation-purpose` 7 → 11; `listening-part-4-talk-purpose` 2 → 7 with verbatim non-reserve quotes | **LOCAL PASS** |
| Canonical map | 1,148 links / 648 unique stable IDs / 25 mapped TOEIC criteria / 0 Listening reserve | **LOCAL PASS** |
| Outcome reconciliation | Foundation 6/6; TOEIC 25/27; total 31/33; two remain uninstrumented | **LOCAL PASS** |
| Mock & readiness integrity | Part 4 approved pool remains 30; Listening approved pool remains 102; exact 25/100/200 Mock totals | **LOCAL PASS** |
| Reserve/review boundary | Listening reserve 193, Part 7 reserve 87, Part 5 review-only 80, Part 4 practice-only 10 remain excluded | **LOCAL PASS** |
| Release synchronization | manifest/package/HTML/app/Service Worker/mock-engine/docs all synchronized to 2.95.84 | **LOCAL PASS** |
| Full local Python + Node suites | All Python unit tests, validators, JS syntax checks, and 46 Node `.mjs` tests pass | **LOCAL PASS** |
| GitHub Validate / Pages | Hosted CI validation and GitHub Pages deployment | **PENDING** |

## Change contract

- All ten practice-only Part 4 items (`mockEligible: false`) remain excluded from Mock selection AND displayed Mock pool totals (`102` Listening / `30` Part 4).
- All 9 new Listening purpose mappings reuse existing non-reserve questions with verbatim transcript quotes; no question text, option, choice ID, or answer key is modified.
- Part 1 photo review and Part 7 independent second review are not bypassed; Listening reserve 193, Reading Part 7 reserve 87, and Separate Part 5 review-only 80 remain excluded.
- No IndexedDB schema migration, learner data reset, UI redesign or `main` modification.

FullSource ZIP, hosted GitHub CI/Pages, installed-PWA/offline and physical-device QA remain separate acceptance gates.
