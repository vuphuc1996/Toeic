# TOEIC Dictionary — Design System

**Current implementation:** v2.30.0  
**Scope:** every learning page, shared controls, responsive shell and PWA navigation.

## 1. Design principles

1. **One system, not per-page styling islands.** Shared typography, spacing, radii, buttons, icons, focus states and breakpoints live in `assets/css/design-system.css`. Feature-specific layout and behavior stay in `assets/css/app.css`.
2. **Readable before compact.** Body text targets 15–16 px; normal helper text should generally stay at 12–14 px; meaningful instructions, options and passage text must not be compressed into microtext. Uppercase eyebrow labels are 11 px; navigation labels may be 10–11 px only where width is constrained.
3. **Fluid sizing.** Prefer `clamp()`, `minmax(0, 1fr)`, `min-width: 0`, `max-width: 100%` and flexible wrapping rather than fixed widths. Prevent page-level horizontal scrolling; allow horizontal scrolling only inside intentionally scrollable components such as tables and topic rails.
4. **Touch and keyboard parity.** Primary actions and form controls should be at least 44 px high where practical. Preserve visible `:focus-visible` rings and clear disabled states.
5. **Platform-native readability.** Use the local system font stack rather than downloading fonts. This allows iOS/iPadOS, Android, Windows and macOS to use their familiar glyph rendering and Vietnamese diacritics.
6. **Quiet visual hierarchy.** Use whitespace and typography first. Cards are reserved for distinct content or actions; avoid wrapping an entire section in a card when its content already contains sub-cards.

## 2. Responsive behavior

| CSS viewport | Target form factor | Navigation/layout rule |
|---|---|---|
| 320–640 px | Android/iPhone phones | Hide sidebar, use five-item bottom navigation, one-column page layouts where content requires it, safe-area padding at the bottom |
| 641–850 px | Small tablet / iPad portrait / compact window | Keep the 76 px icon rail; hide phone bottom navigation; use fluid page gutters and compact two-column dashboard where space permits |
| 851–1199 px | Tablet landscape / small laptop | Retain a compact full sidebar; no phone bottom navigation; collapse dense multi-column learning layouts when needed |
| 1200 px and above | Laptop / desktop / wide monitor | Full navigation and comfortable page width; content remains capped rather than stretching indefinitely |

These are CSS viewport widths, not physical pixels. Device pixel ratio, browser zoom, split-screen and accessibility text scaling can change the effective layout width. Do not hard-code a layout for a named model of phone/tablet.

### Mobile platform requirements

- Respect `env(safe-area-inset-top)` and `env(safe-area-inset-bottom)` for fixed UI.
- Keep input text at 16 px on phone to avoid automatic focus zoom in iOS Safari.
- Use `100svh`/`100dvh` fallbacks for dynamic browser chrome.
- Keep scrollable passage/document content readable and avoid fixed-height text containers.
- Bottom navigation is phone-only; iPad/tablet keeps the sidebar rail.

## 3. Shared type, controls and icons

| Element | Shared target |
|---|---|
| Body text | 15–16 px, line-height about 1.58 |
| Page heading | Fluid 23–34 px depending on width |
| Section heading | Usually 18–24 px |
| Supporting/helper text | 12–14 px; legacy labels raised to at least 11 px |
| Uppercase eyebrow | 11 px, letter-spaced, metadata only |
| Main/secondary button | 44 px minimum across form factors |
| Text button / icon action | 44 px on touch devices; compact desktop row action may be 36 px |
| Input/select/textarea | 44 px minimum; 46 px on phone, 16 px phone input text |
| Icon | Usually 18–22 px; inherit current text color |
| Touch targets | Aim for 44 × 44 px; alphabet chips and compact row actions also use 44 × 44 px on coarse pointers |

Avoid mixing emoji and SVG icons for the same functional control where a matching SVG symbol exists. Icons must remain decorative when adjacent text already provides the accessible name; icon-only actions require an `aria-label` or title.

## 4. Motion and visual effects

Allowed effects are short and informative: page fade/raise on navigation, modal fade/raise on open, button press feedback, hover lift on pointer devices, card border/shadow feedback and progress-fill transitions tied to real progress changes. Existing toast feedback remains brief. Progress animation must reflect an actual value change.

Do not add autoplaying backgrounds, parallax, persistent pulsing, confetti on every answer, or movement that delays a learning action. Every new animation must have a `prefers-reduced-motion: reduce` fallback. On touch devices, do not rely on hover for meaning or navigation.

## 5. Required validation matrix

Before a release that changes shared layout, test CSS viewport widths at **320, 360, 390, 430, 641, 768, 820, 1024, 1280, 1440 and 1920 px**. Check:

- no document-level horizontal overflow;
- heading, button and label wrapping;
- no clipped dialogs, passage text or question options;
- phone safe-area spacing and bottom-nav clearance;
- tablet does not show the phone bottom bar;
- focus visibility, disabled/loading states and tap targets;
- `prefers-reduced-motion` disables non-essential movement;
- navigation, quiz choices, Part filters and personal progress still work.

Automated Chromium screenshots are a regression aid, not a substitute for physical iPhone Safari, Android Chrome, iPadOS Safari and desktop testing. Record untested devices as pending; never claim actual-device QA from viewport emulation.

## 6. Change governance

- Shared sizing or breakpoint changes must be made in `assets/css/design-system.css`, not duplicated across feature styles.
- A feature-specific exception must be documented in the relevant CSS block and have a regression test if it can cause clipping/overflow. Do not reduce type or tap targets ad hoc to make a card fit; reflow the layout first.
- New shared controls should use the shared button/input/icon scale.
- Update this guide and `docs/MASTER_STATUS.md` whenever the global design rules change.


## 7. Shared learning workspace (baseline v2.29.0; retry/history extension v2.30.0)

Flashcard, Vocabulary Review, Grammar, Reading and Listening detail views use the same `#learningFocusBackdrop` / `#learningFocusDialog` shell and shared header/content regions. New learning detail views must enter through `openLearningDetail()`; do not create one modal/backdrop implementation per feature.

- The focus dialog header is fixed; `.learning-focus-content` is the only vertical scroll owner for learning detail content.
- Nested content such as `#modalContent`, Flashcard cards, passages, transcript and question lists must remain `overflow: visible` unless a separate horizontal-only scroller is required for a specific control.
- Flashcard uses a word panel on top and reveals a meaning/example panel beneath it. The expanded panel participates in the same outer scroll; it must not impose a fixed height or its own vertical scrollbar.
- Short learning sessions remain naturally sized and do not create a scrollbar. Long passages, explanation sets or review lists scroll once in the shared workspace.
- On phones and tablets, the same hierarchy stacks to one column and respects safe areas. Do not reintroduce sticky inner action bars that create nested scroll traps.
- The generic vocabulary editor/detail modal and focused Smart Review answer explanation remain separate utilities because their interaction purpose is not a learning-unit detail view; their overlays must preserve correct stacking above the focus shell when invoked.

Regression gate: `node tools/tests/learning-focus-workspace.mjs`, `node tools/tests/flashcard-image-policy.mjs`, `node tools/tests/runtime-render-smoke.mjs`; manually inspect 320–430px phone, tablet portrait/landscape and 1280–1920px desktop. Record actual device/browser separately from viewport simulation.
