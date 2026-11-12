# TOEIC Learning Diagnostics — Layout QA v2.13.0

- **Date:** 2026-11-10
- **Scope:** `#toeicProgressPanel` on the dashboard.
- **Status:** Static markup/CSS regression tests pass; real browser and physical-device visual QA remain pending.

## Layout changes

| Area | v2.12.0 issue | v2.13.0 treatment |
|---|---|---|
| Section wrapper | Generic `.panel` outer surface made the diagnostics block look like a nested boxed card | Removed exact `panel` class; section reads as an open content section |
| Header hierarchy | Eyebrow, main title and explanation crowded in a panel header | Separate eyebrow, H2 and short description |
| TOEIC scope | Listening and Reading content appeared as one large block | Two separately labeled groups with form question counts |
| Part tiles | Per-Part details were visually nested under the outer panel | Seven individually framed interactive cards remain the only framed metric tiles |
| Priority note | Recommendation looked like another content card | Lightweight left-accented note below both groups |

## Responsive and accessible behavior

- Two-column Listening/Reading layout at wide widths; stacked groups below 900px.
- Two-column Part card grid at narrow widths; min-width safeguards avoid grid overflow.
- Part tiles remain native buttons and retain `:focus-visible` outline.
- Priority recommendation retains `role="status"` and `aria-live="polite"`.
- Reduced-motion preference disables the card hover transition.
- Copy continues to identify diagnostics as internal learning indicators, not an ETS score conversion.

## Static test results

`tools/tests/test_dashboard_layout.py`: **6/6 PASS**. The tests assert that the wrapper is not a generic `.panel`, title hierarchy exists, Listening and Reading have separate mount points, priority status is accessible, tablet/mobile breakpoints exist, and Part tiles are keyboard-focusable with overflow safeguards.

## Visual QA limitation

A rendered screenshot and real browser interaction check could not be completed in the current sandbox because the headless browser navigation was blocked by the environment (`ERR_BLOCKED_BY_ADMINISTRATOR`). Therefore no claim is made for pixel-perfect appearance on Chrome, Safari, iOS or Android. The user should complete the manual viewport checks in the release test report before production deployment.
