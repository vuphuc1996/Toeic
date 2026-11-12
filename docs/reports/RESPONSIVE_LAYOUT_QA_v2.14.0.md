# Responsive Layout QA — v2.14.0

**Date:** 10 November 2026  
**Build:** TOEIC Dictionary v2.14.0  
**QA type:** automated/static regression and browser-attempt record; not physical-device certification.

## 1. Cross-device rules checked

| CSS viewport width | Intended device class | Navigation/layout behavior | QA evidence in this build |
|---:|---|---|---|
| 320–640 px | Android/iPhone | Sidebar hidden; five-item bottom navigation; safe-area bottom inset; one-column dense workspaces; 16 px input text | Static breakpoint and safe-area regression tests PASS; no screenshot/interaction run |
| 641–850 px | Compact tablet / iPad portrait | 76 px icon rail; phone bottom navigation hidden; fluid gutters and compact two-column dashboard | Static breakpoint and no-phone-nav tests PASS; no screenshot/interaction run |
| 851–1199 px | Tablet landscape / compact laptop | Compact full sidebar; no phone bottom navigation; flexible two-column dashboard | CSS/static breakpoint rules inspected; no screenshot/interaction run |
| ≥1200 px | Laptop / desktop / wide monitor | Full desktop navigation; content max width; flexible grid columns and large viewport gutters | Desktop uses base layout; no screenshot/interaction run |

## 2. Required viewport regression matrix

The release checklist defines the following target widths: **320, 360, 390, 430, 641, 768, 820, 1024, 1280, 1440 and 1920 CSS px**. This build contains automated checks for the breakpoint definitions, shared scale, safe-area behavior, touch sizing, stylesheet inclusion and PWA caching. It does **not** claim that each target width was visually rendered and inspected.

## 3. Typography and control audit

- Platform system font stack: iOS/macOS `-apple-system`/system UI, Windows `Segoe UI`, Android `Roboto` with `Noto Sans` fallback. No remote font download was added.
- Body: 15–16 px; page titles fluid 23–34 px; supporting/helper text target 12–14 px; eyebrow labels 11 px. A shared readability floor raises legacy 7–10 px micro-labels to at least 11 px.
- Primary/secondary and text buttons: minimum 44 px height; button copy normally 14–15 px. Inputs are 44 px minimum and 46 px on phones; mobile input text is 16 px.
- Icons normally 18–22 px; icon-only controls retain accessible names. Coarse-pointer icon actions, alphabet chips and row actions target 44 × 44 px.
- Focus-visible ring, disabled control state, tap feedback and high-contrast preference are present.

## 4. Motion and accessibility

- Page entry, button press, fine-pointer hover, card surface feedback, and progress changes have short transitions.
- Hover feedback is only enabled for fine pointers; touch users do not need hover to discover or use an action.
- `prefers-reduced-motion: reduce` suppresses non-essential transitions/animations and disables smooth scrolling.
- `prefers-contrast: more` increases border and muted-text contrast.

## 5. Automated/static evidence

- `tools/tests/test_design_system.py`: **13/13 PASS**.
- `tools/tests/test_dashboard_layout.py`: **6/6 PASS**.
- Design-system stylesheet is linked after feature CSS and is included in `REQUIRED`/`APP_SHELL` service-worker lists; all 73 APP_SHELL paths exist.
- CSS parser: 0 parse errors. HTML: 206 IDs, 206 unique, 0 duplicates.
- No project Markdown files are outside `docs/`.

## 6. Browser/device limitation

A headless Chromium 144 preview was attempted against both the local preview route and a local file. The sandbox blocked local navigation/render execution (`ERR_BLOCKED_BY_ADMINISTRATOR` / Chromium renderer termination); no trustworthy screenshot or computed-layout measurements were produced. Therefore this report does not claim browser screenshot QA, tap/keyboard interaction QA, text-clipping verification or no-overflow verification on a running browser.

Still pending: physical iPhone Safari, Android Chrome, iPadOS Safari, Windows/macOS desktop browsers, remote GitHub Actions and GitHub Pages deployment/cache QA. The 320–1920 CSS-pixel matrix must be captured in a functioning browser before calling cross-device visual QA complete.
