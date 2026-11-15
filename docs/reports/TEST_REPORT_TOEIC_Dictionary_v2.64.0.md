# Test Report — TOEIC Dictionary v2.64.0

Date: 2026-11-15  
Candidate: v2.64.0 (local source only)

## Summary

| Check | Result | Scope / interpretation |
|---|---:|---|
| Selected Python regression tests | **94/94 PASS** | 16 targeted modules covering design, responsive composition, A–Z, Foundation, objective tracker and CI coverage |
| JavaScript regression suites | **19/19 PASS** | Every `tools/tests/*.mjs` suite |
| JavaScript syntax | **PASS** | `sw.js` and every `assets/js/*.js` checked with Node |
| Python syntax | **PASS** | Touched reporting, synchronization and test files compile with `py_compile` |
| CSS parse | **0 errors** | `assets/css/app.css` and `assets/css/design-system.css` parsed with tinycss2 |
| Design profile | **PASS** | 54 canonical tokens and 362 legacy font-floor selector groups synchronized |
| Version sync | **PASS** | Manifest, app, Service Worker, page title/sidebar/footer and project docs all use 2.64.0 |
| Vocabulary data | **992 records; 0 errors / 0 warnings** | Canonical vocabulary validator |
| Learning content | **0 errors / 8 warnings** | Warnings are the eight missing licensed Part 1 JPG binaries; SVG fallbacks remain |
| Part 1 photo validator (local permissive mode) | **1/9 present; 8 warnings** | Structural/attribution checks pass with explicit `--allow-missing` |
| Part 1 photo validator (strict CI mode) | **FAIL — 8 errors** | Eight original JPG binaries are absent from this workspace |

## Key regression coverage

- Both Listening Part 1 and TOEIC Mock Exam image frames share 4:3 aspect ratio, `object-fit: cover`, common caption treatment and the stable `data-photo-id` hook.
- The photocopier image uses a dedicated focal point (`50% 42%`) without modifying the licensed source bytes.
- Learning, Foundation, practice, mock-exam and objective cards share row height and footer baseline. Longer copy wraps and expands the row; it is not clipped to force a fixed height.
- Buttons wrap long labels and retain a minimum 44 px target.
- A–Z layout rules cover desktop/tablet/phone widths, including narrow-phone one-column fallback.
- CI explicitly invokes both the alphabet-sound and visual-composition test modules.
- A–Z sound bank contains all 26 letters; TTS play-button exposure counts use the separate `toeic:alphabet-sound-progress:v1` key. This is not a pronunciation accuracy or mastery measure.

## Data and compatibility

- Vocabulary remains 992 records; no stable vocabulary, lesson or question IDs were changed.
- No IndexedDB schema/store migration, personal vocabulary reset or previous learner-progress reset was introduced.
- A–Z interaction events are isolated to the new localStorage key `toeic:alphabet-sound-progress:v1`.
- Service Worker precache list includes the A–Z data and helper.

## Outstanding blockers and limits

1. **Deployment hold:** the source snapshot contains only `part1-office-cleaning.jpg` (1/9). The other eight licensed JPEGs are absent, including `part1-photocopier.jpg`. The user-supplied GitHub image URL could not be fetched in this environment; the binary was not silently replaced. Restore the original licensed binaries before release and require the strict validator to pass 9/9.
2. Chromium navigation to both localhost and a local file fixture returned `ERR_BLOCKED_BY_ADMINISTRATOR`. CSS/static tests passed, but rendered browser screenshots and physical iOS/Android visual checks were not possible here.
3. Remote GitHub Actions, GitHub Pages publication and offline PWA behavior have not been verified.
4. The 94 Python checks are the selected targeted regression groups, not a claim that the entire repository test suite or full discovery has passed.

## Run commands

```bash
python -m unittest \
  tools.tests.test_ci_coverage \
  tools.tests.test_alphabet_sound_lab \
  tools.tests.test_visual_composition \
  tools.tests.test_design_profile \
  tools.tests.test_design_system \
  tools.tests.test_responsive_layout \
  tools.tests.test_learning_surface_consistency \
  tools.tests.test_part1_photo_assets \
  tools.tests.test_foundation_pathway \
  tools.tests.test_foundation_reading \
  tools.tests.test_foundation_listening \
  tools.tests.test_learning_start_level \
  tools.tests.test_placement_diagnostic \
  tools.tests.test_learning_outcomes \
  tools.tests.test_learning_outcome_progress \
  tools.tests.test_project_progress -v

for f in tools/tests/*.mjs; do node "$f"; done
python tools/sync-design-profile.py --check
python tools/sync-version.py --check
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/validate-part1-photo-assets.py  # must pass after restoring 9/9 JPG files
```

## Status

**Local candidate verified with scoped tests; deployment hold remains.** Do not delete/replace the original JPG assets when merging the ZIP into the GitHub repository. Merge/overwrite changed source files while retaining the eight existing originals in the repository, then run the strict validator and remote CI.
