# Project Progress Baseline — v2.63.0

## Design-system workstream

| Measure | Completed | Target | Progress / status |
|---|---:|---:|---|
| Canonical design tokens | 51 | 51 | 100% — synchronized JSON → CSS |
| Design-system unit tests | 19 | 19 | 100% PASS |
| Design-profile tests | 6 | 6 | 100% PASS |
| Learning-surface consistency tests | 5 | 5 | 100% PASS |
| Responsive layout tests | 5 | 5 | 100% PASS |
| Selected Python regression tests | 82 | 82 | 100% PASS for selected groups only |
| JavaScript regression suites | 18 | 18 | 100% PASS |
| CSS parse errors | 0 | 0 | 100% clean parse |
| User aesthetic preferences | Pending | 1 completed design brief | Not yet measurable; ask owner to choose preferences |

## Current canonical source

- Profile: `design/design-profile.json`
- Generated CSS: `assets/css/design-system.css`
- Synchronizer: `tools/sync-design-profile.py`
- Governance: `docs/DESIGN_SYSTEM.md`
- Owner brief: `docs/DESIGN_BRIEF_TEMPLATE.md`

The current implemented default is `Calm Study Blue`: neutral white surfaces, navy/blue primary actions, green positive status, a 15–16 px body scale, 14 px supporting copy, 12.5 px captions, 16 px card radius, 18 px panel radius and 44 px control/touch targets. This is a design baseline, not a finalized owner preference.

## Product and data scope

The underlying product metrics remain unchanged from v2.62.0. The generated project progress snapshot is `PROJECT_PROGRESS_SNAPSHOT_v2.63.0.md`; it uses the canonical project data and does not imply learner mastery.

## Release status

Local candidate only. Strict Part 1 photo validation still fails because eight original JPG binaries are missing (1/9 present). No remote Actions, Pages or physical-device visual QA is claimed. Do not deploy until the licensed source binaries are restored and the strict validator passes.


### Typography governance addendum

- Canonical design tokens: 51/51 synchronized (100%).
- Legacy microtype selector groups audited and normalized: 362/362 (100% of current fixed sub-12.5px `px`/`rem` selectors across `app.css` and the legacy prefix of `design-system.css`).
- Selected test suite: 82/82 Python tests passed; JavaScript regression: 18/18 passed.
- CSS parsing: 0 syntax errors in `app.css` and `design-system.css`.
- Owner preference profile remains pending; implemented default is Calm Study Blue.
