# TOEIC Dictionary — Design System & UI Governance

**Effective candidate:** v2.64.0  
**Profile:** `Calm Study Blue` (`design/design-profile.json`)  
**Status:** implemented as the shared default; visual preferences awaiting owner selection  
**Runtime stylesheet:** `assets/css/design-system.css` (loaded after `assets/css/app.css`)

## 1. Product design direction

The application uses one calm, professional learning workspace. The visual language is based on navy/blue for navigation and primary actions, neutral white surfaces for study content, and green only for positive learning feedback. Feature modules may differ in information architecture, but must not invent a separate font, color palette, card shape, button style, shadow system or spacing scale.

The design priorities are:

1. **Reading clarity:** instructions, question stems, answer options and learning explanations must be comfortably readable before any density optimization.
2. **One hierarchy:** page title → section title → card title → body copy → supporting metadata. A component's role, not its feature name, determines its typography.
3. **Consistent surfaces:** panels, cards, controls and dialogs use the shared border, radius, spacing and shadow tokens.
4. **Content-first responsive layout:** cards reflow when space is insufficient. Do not shrink type to preserve a fixed number of columns.
5. **Native accessibility:** local system font stack, keyboard focus ring, 44 px touch targets, readable contrast and reduced-motion support.

## 2. Canonical design profile — source of truth

`design/design-profile.json` is the canonical parameter file. Do not edit the generated token block in `assets/css/design-system.css` by hand.

```bash
python tools/sync-design-profile.py --apply   # regenerate JSON tokens and legacy font floor
python tools/sync-design-profile.py --check   # CI / local drift check
```

The synchronizer updates two generated regions in `design-system.css`: the `DESIGN_PROFILE_TOKENS` block and the `DESIGN_LEGACY_FONT_FLOOR` block. The latter is built by auditing every fixed `px`/`rem` text size below the caption floor in feature CSS and the legacy prefix of `design-system.css`; the corresponding selectors are lifted to the shared caption token. This prevents old module-level microtype from silently remaining visible. CI runs `--check`, so adding a new sub-caption rule causes a clear failure until it is removed, assigned a semantic token, or intentionally reviewed. Shared component rules remain in `design-system.css`; feature CSS in `app.css` is responsible for layout/behavior, not for creating new visual scales.

### Default visual palette

| Role | Token | Default | Use |
|---|---|---|---|
| Canvas | `--ds-color-canvas` | `#F4F7FB` | Main application background |
| Surface | `--ds-color-surface` | `#FFFFFF` | Cards, panels and dialogs |
| Subtle surface | `--ds-color-surface-subtle` | `#F8FAFD` | Secondary containers |
| Soft brand surface | `--ds-color-brand-soft` | `#EAF2FC` | Selected/active states |
| Primary text | `--ds-color-ink` | `#1B2F49` | Headings and important content |
| Secondary text | `--ds-color-muted` | `#63758C` | Supporting copy |
| Border | `--ds-color-border` | `#E0E7F0` | Card and control boundaries |
| Primary brand | `--ds-color-brand` | `#1D568F` | Primary actions and highlights |
| Deep brand | `--ds-color-brand-deep` | `#153C70` | Navigation and strong emphasis |
| Accent | `--ds-color-accent` | `#16876C` | Positive progress and confirmation |
| Warning / danger | `--ds-color-warning` / `--ds-color-danger` | `#A96A19` / `#C64D4D` | Semantic status only |

Do not introduce a new feature color for decoration. A new semantic color must be added to the profile with usage guidance and contrast verification.

## 3. Typography contract

Use the native system font stack from `--ds-font-family`. It avoids an external font dependency and follows the platform's Vietnamese glyph rendering. No module may load a separate font family.

| Semantic role | Token | Baseline |
|---|---|---:|
| Page title | `--ds-font-page-title` | Fluid 25–34 px |
| Section title | `--ds-font-section-title` | Fluid 20–23 px |
| Card title | `--ds-font-card-title` | Fluid 17–19 px |
| Main reading copy | `--ds-font-body` | Fluid 15–16 px |
| Supporting copy / card description | `--ds-font-support` | 14 px |
| Form label | `--ds-font-label` | 13 px |
| Caption / metadata | `--ds-font-caption` | 12.5 px |
| Input / button | `--ds-font-control` / `--ds-font-button` | 14.5 px |
| Long reading passage | `--ds-font-passage` | 15 px |

**Rules:**

- Essential instructions, answer options, passage text, explanation and card descriptions must never be reduced to microtext to fit a layout.
- 12.5 px is the enforced lower limit for visible text in the current baseline. The generated legacy floor audits all fixed `px`/`rem` declarations in `app.css` and the legacy prefix of `design-system.css` below that size and raises them to the shared caption token. New features must use the semantic tokens; do not introduce sub-12.5 px exceptions. Larger page, section, card and body roles are reasserted after the legacy floor so the floor does not flatten the hierarchy.
- Numeric score, word headword and test timer may use a dedicated larger display size, but must keep the same font family and weight logic.
- Never use arbitrary `font-size` values in a new feature. Choose a semantic role token. If no role fits, propose a token in `design-profile.json` and document its use.
- Prefer line-height 1.55–1.7 for reading and 1.3–1.45 for headings.

## 4. Spacing, geometry and elevation

| Element | Token | Value |
|---|---|---:|
| Spacing scale | `--ds-space-1` to `--ds-space-10` | 4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 px |
| Control radius | `--ds-radius-control` | 10 px |
| Card radius | `--ds-radius-card` | 16 px |
| Panel radius | `--ds-radius-panel` | 18 px |
| Pill radius | `--ds-radius-pill` | 999 px |
| Touch target | `--ds-touch-target` | 44 px minimum |
| Content maximum | `--ds-content-max` | 1600 px |

Panels use the panel radius and low elevation. Cards use the card radius and subtle elevation. Inputs and buttons use the control radius. Avoid combining several shadow styles in one section. Use the spacing scale; do not introduce arbitrary 7 px / 13 px / 19 px spacing without a documented reason.

## 5. Component recipes

| Component role | Required shared pattern |
|---|---|
| Page heading | Eyebrow (optional) + page title + one supporting sentence; actions align to the heading only when width allows |
| Section panel | White surface, shared panel border/radius, panel header, body spacing from tokens |
| Content card | Shared card border/radius/shadow, card title, body copy and optional metadata footer |
| Selection card | Entire card is one clear action; title 17–19 px, description 14 px, visible selected/focus state |
| Primary button | Brand fill, white text, 44 px minimum, 14.5 px label |
| Secondary button | White surface, border, brand text, 44 px minimum |
| Form control | 44 px minimum; 16 px input text on iPhone where needed to avoid automatic Safari zoom |
| Question / answer | Question 15–16 px; options 14.5–15 px; adequate line spacing and 44–48 px target |
| Result / score | Score is prominent; explanation and recommendation remain 14 px or larger |
| Mobile navigation | Five destinations, safe-area aware, caption about 12–12.5 px; must not steal vertical room from content |

A feature can add a layout class, not a private theme. It should reuse `.panel`, `.panel-header`, `.learning-card`, `.primary-button`, `.secondary-button` and the semantic type tokens wherever possible.


### Media frames and card-content balance (v2.64.0)

- Listening Part 1 illustrations and photographs share the `--ds-image-ratio: 4 / 3` frame. Each local JPG is prepared to the matching 1448×1086 landscape canvas so the browser does not need image-specific portrait cropping.
- Part 1 uses local JPG sources only. All nine optimized JPGs are included in the full-source archive; strict validation requires a 4:3 landscape image, at least 1280×960 pixels and no more than 400,000 bytes. Keep attribution and original source type intact; do not introduce an SVG fallback or generated placeholder.
- New image units must use the same frame component and must declare a stable `data-photo-id` only when a reviewed crop focal point is necessary. Do not add unique width/height rules to an individual image.
- Cards in the same grid row have equal outer height and a common footer baseline. Titles reserve a two-line baseline; normal descriptions reserve three lines as a minimum but are never clipped or line-clamped. Longer copy expands the row naturally.
- Card buttons may wrap to multiple lines, keep a minimum 44 px touch target, and must not force `white-space: nowrap`. Internal content uses `min-width: 0` and `overflow-wrap: anywhere` where long labels or IDs could otherwise escape the card.
- Responsive alphabet-sound cards use four columns on desktop, three at 851–1100 px, two at 641–850 px and 320–640 px, and one at 360 px or less. Other card grids select columns from available content width and their documented breakpoints. Do not assume the CSS viewport equals the physical display diagonal.

## 6. Responsive layout contract

Breakpoints are CSS viewport widths, not physical device sizes or diagonal inches.

| Viewport width | Behavior |
|---|---|
| 320–640 px | Phone layout, one-column learning cards when required, safe-area-aware bottom navigation |
| 641–850 px | Compact tablet icon rail, no phone bottom bar, content can use two columns only when cards remain readable |
| 851–1199 px | Tablet landscape / small laptop, compact sidebar, content-first grids |
| 1200 px and above | Full sidebar, wider content capped at 1600 px; do not stretch paragraphs across the whole display |

Responsive validation widths: **320, 360, 390, 430, 641, 768, 820, 1024, 1280, 1440 and 1920 px**.

Required checks: no document horizontal overflow; no clipped title/control/dialog; grid reflow instead of font shrink; passage/answer readability; visible focus; touch target; phone safe-area clearance; tablet never shows phone bottom navigation; reduced-motion respected.

## 7. Visual governance — do not create design islands

Before implementing a new module:

1. Identify its semantic component roles (page title, section panel, card, body, metadata, control, status).
2. Reuse tokens and existing shared components. Do not create a private font scale or palette.
3. Set layout with grid/flex/minmax/auto-fit and fluid `clamp()` only where needed. Do not use fixed physical-device assumptions.
4. If a visual exception is unavoidable, record the selector, reason, viewport range and test in the feature's change note.
5. Add a regression test for typography roles, component reuse and responsive reflow.
6. Run the profile synchronizer and design-system test before packaging.

**Forbidden:** one-off font families; feature-specific brand colors; 8–11 px text for meaningful content; using a smaller font as the first solution to overflow; duplicate page-specific panel/button styles; decorative gradients on every card; unreviewed per-feature shadow/radius scales.

**Allowed exceptions:** large numeric scores, timers, vocabulary headwords, phonetic symbols, compact decorative eyebrow text and dense table controls. These exceptions may change display scale, not the underlying font family/color system.

## 8. Design brief — owner preferences to confirm

The current `Calm Study Blue` profile is a safe and readable default, not a claim that all aesthetic preferences have been finalized. Complete the design brief in the conversation (or edit `docs/DESIGN_BRIEF_TEMPLATE.md`). Once approved, update `design/design-profile.json`, regenerate CSS tokens and record the approved profile here.

## 9. Release gate

A release that changes shared design must pass:

```bash
python tools/sync-design-profile.py --check
python -m unittest discover -s tools/tests -p 'test_design_system.py' -v
python -m unittest discover -s tools/tests -p 'test_design_profile.py' -v
```

Also run `tools/tests/test_learning_surface_consistency.py`, `test_visual_composition.py`, `test_alphabet_sound_lab.py` and the responsive test group. Browser viewport simulation must be described as simulation; it is not proof of physical-device QA. Remote GitHub Actions, GitHub Pages and iOS/Android PWA QA must be reported separately.
