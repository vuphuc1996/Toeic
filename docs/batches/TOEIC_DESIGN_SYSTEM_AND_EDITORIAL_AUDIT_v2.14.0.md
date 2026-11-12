# TOEIC Design System & Editorial Evidence Batch — v2.14.0

**Ngày:** 10/11/2026  
**Baseline:** v2.13.0  
**Scope:** TOEIC-only; shared responsive design system + editorial evidence mapping.

## 1. Shared design rules

- Added `assets/css/design-system.css` after feature CSS so all pages share a common font stack, fluid type, line-height, spacing, radii, card surface, button/input/icon scale, keyboard focus and disabled-state behavior.
- System font stack uses platform fonts on iOS/iPadOS, Android, Windows and macOS; no remote font download was introduced. Body type is 15–16 px; helper text is generally 12–14 px; uppercase eyebrow labels are 11 px.
- Primary/secondary buttons and input controls target at least 44 px; phone fields use 16 px text and 46 px height to avoid iOS Safari focus zoom. Icon-only controls have accessible names and shared sizing.
- Breakpoints: phone 320–640 CSS px; compact tablet/iPad portrait 641–850; tablet landscape/small laptop 851–1199; laptop/desktop 1200+. Tablet never displays the phone bottom bar.
- Phone navigation and main-area clearance respect bottom safe-area insets; app frame uses `100svh`/`100dvh` with fallback.
- Motion is restrained: page entry, button/card feedback and progress-fill transitions only. Hover is limited to fine pointers; `prefers-reduced-motion` disables non-essential movement.
- Added contrast preference support and visible `:focus-visible` feedback.

## 2. Editorial evidence pass

- Indexed 211 correct answers across Listening (102) and Reading (109) and linked each item to source text or an explicit review category.
- Listening: 32 direct-source matches, 34 lexical-evidence pointers, 3 paraphrase/inference cases manually checked, 8 Part 1 illustration/key comparisons checked, 25 Part 2 response-fit items checked.
- Reading: 32 direct-source matches, 28 lexical-evidence pointers, 3 paraphrase/inference cases manually checked, 30 Part 5 grammar items checked, 16 Part 6 context/cohesion items checked.
- The 6 low-overlap inference items are individually noted in `TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.14.0.md`.
- The 126 direct/lexical items still need a full distractor-plausibility/uniqueness pass; source overlap does not prove all alternative choices are wrong.

## 3. Listening corrections

- Replaced all 23 generic Part 2 translation placeholders with Vietnamese translations of their actual spoken lines.
- Standardized the supplier-samples response-selection prompt to match the actual task.
- Changed the room-unavailable negative-tag response to “That’s right…” to avoid a bare “Yes” that can confuse polarity interpretation.
- Added validator/tests for Part 2 prompt consistency and placeholder rejection.

## 4. Preservation

- Vocabulary remains 928 records / 928 stable IDs / 26 A–Z files.
- Listening and Reading remain 102/109 questions; no question IDs or question order changed. One reviewed Part 2 response choice was clarified without changing its correct answer index.
- Grammar remains 25 lessons / 54 exercises. No IndexedDB schema, personal vocabulary or study-progress migration was introduced.

- Unit test suites: **116/116 PASS** (the 33-case vocabulary validator regression suite completed across four groups).

## 5. Limitations

- Part 1 assets remain SVG illustrations, not ETS-style photographs. Audio remains browser SpeechSynthesis, not recorded/ETS audio.
- The editorial checks are internal and not independent two-person proofing, psychometric validation or ETS approval.
- Responsive CSS regression checks are automated/static. Browser preview was blocked by the sandbox; physical iPhone/iPad, Android, remote CI and GitHub Pages deployment are unverified.
- Full Mock remains gated on the remaining distractor audit, device QA and release signoff.
