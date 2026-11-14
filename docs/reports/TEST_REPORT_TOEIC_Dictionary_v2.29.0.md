# Test Report — TOEIC Dictionary v2.29.0

**Base:** v2.28.0  
**Scope:** shared learning workspace, Flashcard two-zone layout and one vertical scroll owner, release documentation consolidation.  
**Status:** local release candidate; remote deployment and physical-device QA are not claimed.

## Implemented scope

- Flashcard keeps the vocabulary, IPA/POS and topic in an upper panel. First activation reveals a natural-height meaning/example panel below; a following activation advances to the next word.
- The shared `.learning-focus-content` is the only vertical scroll owner. Flashcard panels and shared detail content do not create a second nested scrolling viewport.
- Grammar, Reading and Listening detail now enter through `openLearningDetail()` and use the same focus backdrop, header, close control, dialog and scroll container as Flashcard/Review.
- Responsive layout keeps the same hierarchy on desktop/tablet and stacks approved artwork and vocabulary content on narrower viewports. Phone safe-area behavior and reduced-motion support remain active. Removed 40 obsolete CSS rules from the previous independently scrolling Flashcard face and layout variants.
- Documentation was consolidated around one `MASTER_STATUS.md`, `COMPATIBILITY.md`, `DESIGN_SYSTEM.md`, `CONTENT_OPERATIONS.md`, `CHANGELOG.md` and `archive/PROJECT_HISTORY.md`.
- Release rotation applied: v2.28.0 (previous) and v2.29.0 (current) remain active. Nine old Markdown batch/report/source files were summarized in Project History and retired; the v2.27.0 root update note was retired. The release rotator has 2 dedicated regression tests.

## Verification results

| Check | Result | Notes |
|---|---|---|
| `node --check assets/js/app.js` | PASS | JavaScript syntax |
| `node --check sw.js` | PASS | Service worker syntax |
| `learning-focus-workspace.mjs` | PASS | Unique HTML IDs, Flashcard/Review flow, shared detail shell, responsive rules, IndexedDB v1 |
| `flashcard-image-policy.mjs` | PASS | 979 vocabulary records; word image policy preserved |
| `mock-ui-integrity.mjs` | PASS | Mock interface and local usage ledger preserved |
| `mock-exam-engine.mjs` | PASS | 15/60/120-minute modes and blueprint integrity |
| `listening-tts-regression.mjs` | PASS | Voice selection, pauses, rate and cancellation regressions |
| `runtime-render-smoke.mjs` | PASS | Reading/Listening/Grammar rendering and legacy choice-ID migration behavior |
| Targeted Python unit tests | PASS — 90/90 | Design System, Learning Detail Scope, Dashboard Layout, Version Sync, Learning Content, Vocabulary Examples, Patch Data and Release Rotation |
| `python tools/validate-data.py` | PASS | 979 canonical headwords; 0 errors / 0 validator warnings |
| `python tools/validate-learning-content.py` | PASS with 8 warnings | 0 errors; 8 Part 1 JPG binaries absent from this source snapshot; SVG fallbacks remain |
| `python tools/sync-version.py --check` | PASS | All registered version markers 2.29.0 |
| Release rotation | PASS | Dry-run reviewed, apply completed; two release generations remain active; 2 regression tests |
| ZIP CRC / clean extraction / overlay reconstruction | PASS | Full Source: 156 files; Overlay: 22 changed/added (6 added + 16 modified), no delete directives; clean merge simulation matches Full Source byte-for-byte |

## Not verified / release limitations

- Physical desktop, tablet, iPhone Safari and Android Chrome interaction remains pending. Automated CSS and runtime tests do not replace user-device QA.
- GitHub Actions and GitHub Pages deployment are pending; no remote commit or deploy is claimed.
- Strict Part 1 photo gate is NOT passed in this snapshot: all eight JPG files are absent. Preserve any user-owned copies on the live repository; SVG fallbacks remain present.
- No IndexedDB user data was imported, exported, inspected, reset or migrated.
- The complete Python test discovery was not used as a release claim; the report records only the eight targeted modules (90/90) listed above.

## Version and data integrity

- Canonical vocabulary remains 979 headwords; this release changes UI and documentation, not vocabulary content.
- Existing vocabulary, Listening, Reading and Grammar IDs/question pools remain unchanged.
- IndexedDB remains `toeic-vocabulary-phase1`, version 1, store `workspace`.

## Package inventory

- Full Source contains 156 files.
- Update Overlay contains 22 changed/added files (6 added, 16 modified); it contains no direct delete instructions.
- Both ZIPs passed CRC verification. Overlay was applied to an extracted v2.28.0 baseline, the documentation rotator was run, and the resulting inventory/content matched v2.29.0 Full Source byte-for-byte.
