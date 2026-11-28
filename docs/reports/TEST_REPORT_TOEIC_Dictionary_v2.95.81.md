# Test & Acceptance Report — TOEIC Dictionary v2.95.81

**Target branch:** `candidate`
**Predecessor baseline:** `a16a3e4a51917e687b92e404ab1c785a393dfb0f` (v2.95.80)
**Scope:** Part 7 evidence validator hardening; no learner-facing feature or bank content changes.

## Expected checks

| Gate | Required evidence | Status |
|---|---|---|
| Part 7 validator regressions | Duplicate document/source labels, invalid types, and whole-phrase matching | **PENDING CI** |
| Canonical mapping audit | 1,103/1,103 links; 638 stable IDs; 0 Listening reserve mappings | **PENDING CI** |
| Criterion reconciliation | 22/27 TOEIC; 28/33 total; five remain uninstrumented | **PENDING CI** |
| Version/cache synchronization | 19 single-instance markers; app/SW/mock release-key groups synchronized | **PENDING CI** |
| Full Python suite | Complete discovered inventory on exact candidate SHA | **PENDING CI** |
| GitHub Validate | Exact candidate SHA, all steps complete | **PENDING** |
| GitHub Pages | Build/status/deploy for the same candidate SHA | **PENDING** |

## Change contract

- Invalid or ambiguous Part 7 source evidence must fail closed.
- Existing two eligible Part 7 mappings must continue to pass.
- Existing mapping counts and review gates must not be inflated or relaxed.
- No reserve items may enter the mapping or Mock inventory.
- No canonical vocabulary IDs, question/choice IDs, answers, learner IndexedDB data/schema, UI layout, navigation or Robot Buddy behavior may change.

The v2.95.80 candidate had its own hosted acceptance; that evidence does not carry over to v2.95.81. Installed-PWA/offline propagation, physical-device QA and FullSource ZIP generation remain separate acceptance gates.
