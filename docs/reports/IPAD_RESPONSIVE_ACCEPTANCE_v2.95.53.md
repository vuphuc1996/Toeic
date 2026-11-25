# iPad/tablet responsive acceptance — v2.95.53

## Implemented behavior

The 11-inch iPad Pro M1 uses an approximately 834 × 1194 CSS-pixel portrait viewport and 1194 × 834 CSS-pixel landscape viewport in the standard browser layout. The new CSS rule is viewport/orientation based, not a physical-inch device sniff.

| Viewport | Sidebar | Main left margin | Bottom navigation | Layout |
|---|---|---:|---|---|
| iPad Pro 11 M1 portrait · 834 × 1194 | Hidden | 0px | Fixed, five columns | Phone-style navigation and mobile content flow |
| iPad Pro 11 M1 landscape · 1194 × 834 | Visible, 216px | 216px | Hidden | Web/tablet landscape layout |
| Tablet portrait · 768 × 1024 | Hidden | 0px | Fixed, five columns | Phone-style navigation |
| iPhone · 390 × 844 | Hidden | 0px | Fixed, five columns | Existing phone layout |
| Desktop · 1440 × 900 | Visible, 264px | 264px | Hidden | Existing desktop layout |

## Interaction contract retained

- Three direct destinations remain on the bottom bar: Trang chủ, Từ vựng, Ôn tập.
- Học tập and Cấu hình continue to open their existing grouped sheet menus; the source JS event listeners are unchanged.
- Landscape continues to expose the complete left navigation, including the full wordmark, local-data status and version label.
- Safe-area padding remains enabled for the bottom bar and page content; Robot Buddy is lifted above the bar in portrait mode.
- No page content, navigation destination IDs, learner records, IndexedDB schema or data-module contract changed.

## Verification evidence

- Chromium layout simulation at five profiles: iPad portrait, iPad landscape, iPhone, desktop and 768px tablet portrait.
- All 11 `.page` sections were activated and checked at four viewport profiles: **44 checks; 0 page-level horizontal overflows**.
- `test_responsive_layout.py`: 8/8 PASS.
- `test_design_system.py`: 19/19 PASS, including the updated portrait-vs-landscape tablet navigation contract.
- `audit-design-tokens.py`: 0 new violations.
- Visual evidence (actual source HTML + source CSS, scripts omitted for deterministic layout geometry):
  - `visual-evidence/v2.95.53/ipad-pro-11-m1-portrait.jpg`
  - `visual-evidence/v2.95.53/ipad-pro-11-m1-landscape.jpg`
  - `visual-evidence/v2.95.53/viewport-matrix.json`
  - `visual-evidence/v2.95.53/all-pages-overflow-matrix.json`

## Acceptance limitation

This is a source-level browser viewport simulation, not a physical iPad test. Before production acceptance, verify on the user's iPad Pro 11 M1 in Safari and in the installed PWA:

1. Open the deployed app and allow the v2.95.53 service worker to activate; reload once after the update is available.
2. Portrait: confirm the left sidebar is absent, the five bottom tabs are visible, and Học tập/Cấu hình open their grouped sheets.
3. Tap each tab and one item inside each grouped sheet; confirm page navigation and active-tab highlighting.
4. Rotate to landscape: confirm the full left sidebar appears and the bottom bar disappears.
5. Rotate back to portrait and repeat; confirm no clipped menu text, horizontal scrolling, or Robot Buddy overlap.
6. Repeat in Safari and the Home Screen PWA, because their safe-area and installed-display behavior can differ.

**Status: viewport simulation PASS; physical-device / hosted deployment acceptance NOT YET VERIFIED.**
