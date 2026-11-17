# Test Report — TOEIC Dictionary v2.89.0

## Release scope

1. Repair the CI failure at **Validate canonical design profile** by regenerating `assets/css/design-system.css` from the canonical profile. The CI check remains strict and enabled.
2. Add 13 supplementary A2 Reading passages / 39 questions with scoped progress, independent review status, offline Service Worker caching and a dedicated regression suite.
3. Correct the displayed-vs-effective 67% threshold rounding edge case in Foundation Reading evidence.
4. Preserve all original Foundation Reading items, stable IDs, progress keys, IndexedDB v1 and Mock eligibility boundaries.

## Local verification results

| Check | Result | Notes |
|---|---|---|
| All JavaScript regression suites | PASS 32/32 | Every `tools/tests/*.mjs` suite was run |
| Selected Python regression tests | PASS 130/130 | 17 focused modules; not full-suite discovery |
| Python syntax compilation | PASS | All `tools/**/*.py` files compiled |
| `test_ci_coverage.py` | PASS 2/2 | All 48 Python test modules and 32 JavaScript suites are registered in GitHub Actions |
| `test_design_profile.py` | PASS 6/6 | Canonical source, generated selectors, typography floor and responsive width rules |
| `test_foundation_reading.py` | PASS 9/9 | Existing base resource and v2.75 question baseline preserved |
| `test_foundation_reading_extended.py` | PASS 7/7 | 13 passages, 39 questions, source evidence, ID map, hashes, app/SW integration and storage isolation |
| `foundation-reading-evidence.mjs` | PASS | Existing reading evidence plus 2/3 => displayed 67% threshold behavior |
| `foundation-reading-extended-evidence.mjs` | PASS | Retry semantics, `reading2` scope isolation and extension-open state contract |
| `node --check sw.js` and app.js | PASS | Service Worker and app module syntax |
| CSS parse (`tinycss2`) | PASS | `app.css`: 1,815 top-level nodes; `design-system.css`: 270; 0 parse errors |
| `tools/validate-data.py` | PASS | 1,137 canonical vocabulary records; 0 errors / 0 warnings (legacy baseline noted) |
| `tools/validate-learning-content.py` | PASS | Listening 107/201, Reading 51/200, Grammar 33/86; 0 errors / 0 warnings |
| `tools/validate-part1-photo-assets.py --allow-missing` | PASS | 9/9 Part 1 photo records/assets and attribution checked; 0 missing warnings |
| Canonical design profile | PASS | 54 tokens / 400 legacy font-floor selector groups synchronized |
| Version synchronization | PASS | All registered app, SW, HTML and documentation markers agree at v2.89.0 |
| Full archive integrity | PASS | Final ZIP tested and SHA-256 recorded in the companion checksum file |

The 130 Python tests are selected targeted modules, not the full Python test discovery suite.

## Canonical design-profile CI root cause

`tools/sync-design-profile.py --check` failed because the generated legacy font-floor selector list in `assets/css/design-system.css` was stale relative to the fixed font declarations in `assets/css/app.css`. Five selectors were missing from the generated block:

- `.foundation-portfolio-export .secondary-button`
- `.foundation-portfolio-export small`
- `.foundation-portfolio-export strong`
- `.foundation-production-extension>summary small`
- `.robot-header-title small`

The generated file was refreshed with `python tools/sync-design-profile.py --apply`. The check then passed at 54 design tokens and 400 legacy selector groups. No test was removed, weakened or bypassed.

## Remote / manual QA not claimed

- The GitHub Actions run that reported the failure has not been rerun remotely from this workspace. The source fix and exact validator passed locally; a pushed commit is required to confirm the remote workflow is green.
- GitHub Pages deployment, browser visual QA, desktop 15.6-inch at 100% zoom, mobile/tablet, iOS/Android and offline/reconnect are not claimed as verified.
- All 13 new A2 extended Reading passages remain pending independent editorial review and learner validation.

## Data preservation

- Original `data/learning-path/foundation-reading.json` remains unchanged.
- The new bank uses stable `::reading2` IDs and the existing `toeic:foundation-reading-progress:v1` storage key with a scoped child key.
- No new localStorage key, IndexedDB schema/store/version, migration, profile reset, progress overwrite, network upload or backend dependency is introduced.
- New extended Reading evidence is not merged into core A2 outcome evidence or TOEIC Mock pools.
