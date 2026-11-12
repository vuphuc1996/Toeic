# Batch 012 — Licensed Part 1 photographs & photo-aware runtime (v2.22.0)

Date: 2026-11-11
Baseline: v2.21.0

## Scope
- Part 1 now prefers eight locally hosted Pexels photographs from `assets/listening/` using the filenames in `assets/listening/ATTRIBUTION.csv`.
- Existing SVG files remain as per-item fallbacks if a JPG is unavailable or fails to load.
- Service Worker pre-caches the eight JPGs as OPTIONAL assets; SVG fallback images remain REQUIRED. An unavailable JPG therefore cannot abort PWA installation.
- Image framing changes to 4:3 and uses `object-fit: cover`; the modal caption identifies photographs rather than illustrations.
- Correct spoken descriptions B/C/D are aligned with the reception plant, restaurant table-setting and photocopier photographs.

## Preservation
- All eight resource IDs, question IDs, `choiceIds`, answer positions, A–D ordering and progress keys remain unchanged.
- Answer indexes remain A/B/C/D = 0/1/2/3 for the eight Part 1 items.
- No IndexedDB schema/profile changes, imports, exports or resets.
- No Listening/Reading question-count changes.

## Asset delivery boundary
The source snapshot available during this patch contained the eight SVG fallbacks but not the JPG binaries that the user reports have already been uploaded to `assets/listening/` in the GitHub repository. The patch therefore references the exact eight `.jpg` filenames from the supplied Pexels manifest and does not replace those remote files. Before copying the patch, keep the existing JPG files in the repository. The app gracefully falls back to SVG if a photo path is missing.

## Sources and licensing
Photographer, Pexels page URL, direct download URL and Pexels license URL are recorded per item in `assets/listening/ATTRIBUTION.csv`. These are licensed practice photographs, not ETS test material.
