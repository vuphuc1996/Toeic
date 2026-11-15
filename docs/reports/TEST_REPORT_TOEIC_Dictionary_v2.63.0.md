# Test Report — TOEIC Dictionary v2.63.0

**Scope:** canonical design profile, design token synchronization, typography and responsive component consistency, plus regression protection for the existing TOEIC learning flows.

## Results

| Test group | Result |
|---|---:|
| `test_design_system.py` | 19/19 PASS |
| `test_design_profile.py` | 6/6 PASS |
| `test_learning_surface_consistency.py` | 5/5 PASS |
| `test_responsive_layout.py` | 5/5 PASS |
| `test_dashboard_layout.py` | 6/6 PASS |
| `test_sync_version.py` | 12/12 PASS |
| `test_pwa_readiness.py` | 3/3 PASS |
| `test_ci_coverage.py` | 2/2 PASS |
| `test_foundation_pathway.py` | 6/6 PASS |
| `test_foundation_reading.py` | 5/5 PASS |
| `test_foundation_listening.py` | 7/7 PASS |
| `test_learning_outcomes.py` | 3/3 PASS |
| `test_learning_outcome_progress.py` | 3/3 PASS |
| **Selected Python regression total** | **82/82 PASS** |
| JavaScript regression scripts | **18/18 PASS** |

Also passed:

- CSS parsing: `assets/css/app.css` (1,496 top-level rules) and `assets/css/design-system.css` (160 top-level rules); 0 parser errors in either file.
- JavaScript syntax: `sw.js` and all `assets/js/*.js` passed `node --check`.
- `python tools/sync-design-profile.py --check`: PASS; all 51 canonical tokens and the 362-selector legacy typography floor match their source rules.
- `python tools/sync-version.py --check`: PASS; manifest, app runtime, service worker, HTML, README, Master and Changelog all show v2.63.0.
- Data validation: 992 vocabulary records, 0 errors, 0 warnings.
- Learning content validation: 0 errors, 8 warnings for missing original Part 1 JPG binaries; SVG fallback remains.
- Objective resources: 281/281 records linked; learning outcome framework: 30/30 criteria defined.

## Known blocker / limits

- `python tools/validate-part1-photo-assets.py` fails 8 checks: only 1/9 original Part 1 JPGs exists in the inherited source. The strict validator is unchanged. This remains a deployment hold; do not disable it or replace the source photos with generated placeholders.
- Full Python test discovery was not run in this release; only the named groups above are claimed.
- Chromium/browser visual QA is not claimed because the environment blocked the local app URL. CSS parsing and automated source-level checks are not a substitute for a real rendered page.
- Remote GitHub Actions, GitHub Pages deployment, and physical iPhone/iPad/Android/desktop QA remain unverified.

## Design changes

- Consolidated superseded typography patches into one shared component contract, then generated the legacy selector floor from the current source audit. The profile is governed by 51 semantic tokens and 362 legacy selector groups.
- Canonical profile is `design/design-profile.json`; `tools/sync-design-profile.py` generates only the marked CSS token block.
- `docs/DESIGN_SYSTEM.md` specifies the visual direction, typography roles, palette, spacing, radii, shadows, component recipes, responsive widths, prohibited design patterns, and release gates.
- `docs/DESIGN_BRIEF_TEMPLATE.md` records owner preferences for the next design iteration. `Calm Study Blue` remains the implemented default pending those selections.

## Data preservation

No vocabulary IDs or canonical records changed. No IndexedDB store/schema migration, personal vocabulary reset, history reset, or learner-progress reset was made.


## Supplemental typography floor audit

- `tools/sync-design-profile.py --check` now verifies both the 51 canonical tokens and a generated legacy selector floor.
- Current source audit covers 362 selector groups across `assets/css/app.css` and the pre-profile legacy section of `assets/css/design-system.css` that previously declared fixed text sizes below 12.5px.
- A future feature that introduces another fixed `px`/`rem` text size below the caption floor changes the expected generated block; CI then fails until the feature is assigned a semantic role or consciously resolved.
- The semantic body/support/control styles are applied after the legacy floor, preserving the type hierarchy instead of forcing all content to a single size.
- This is a static CSS/source audit, not browser screenshot or physical-device visual verification.
