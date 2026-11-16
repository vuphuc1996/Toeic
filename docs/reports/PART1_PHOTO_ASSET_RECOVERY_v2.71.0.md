# Part 1 Original Photo Recovery — v2.71.0

## Current source-package status

- The project contract is JPG-only for Listening Part 1: each Part 1 item points to `./assets/listening/*.jpg`; no SVG fallback should be substituted.
- This workspace archive contains **1/9** JPG binaries: `part1-office-cleaning.jpg`.
- The eight missing licensed-stock originals are explicitly identified in `assets/listening/ATTRIBUTION.csv` with the expected local filename, Pexels photographer, official source page, direct-download URL, license and usage notes.
- Saved historical full-source archives examined from v2.36.0 onward were labelled `NO_PEXELS_JPG` or carried the same missing-binary state; the current Library contains only duplicate copies of `part1-office-cleaning.jpg`, not the eight missing Pexels originals.
- The Pexels CDN was not reachable from the build environment. No image files were generated, synthesized, replaced, or renamed to imitate the originals. Consequently, the eight original JPG byte streams are **not embedded** in this release ZIP/TAR.GZ.

## Included one-command recovery

- `tools/restore_part1_photos.py` loads the eight licensed-stock rows from `ATTRIBUTION.csv` and downloads all missing photos in one operation.
- It only accepts HTTPS URLs on `images.pexels.com`, checks JPEG signature and minimum dimensions (1280×960), writes atomically, and refuses to overwrite existing assets.
- The project-generated `part1-office-cleaning.jpg` is not part of the download list.
- Windows shortcut: `restore-part1-photos.bat`.
- After restoration, run `python tools/validate-part1-photo-assets.py` in strict mode. Do not use `--allow-missing` as a release gate.

## Eight missing original files

`part1-meeting-documents.jpg`, `part1-warehouse-box.jpg`, `part1-technician-inspection.jpg`, `part1-airport-suitcase.jpg`, `part1-presentation-room.jpg`, `part1-reception-plant.jpg`, `part1-restaurant-setting.jpg`, and `part1-photocopier.jpg`.

## Release gate

Strict Part 1 photo validation remains **BLOCKED** until all nine JPG files are present and pass signature, dimensions, attribution and item-path checks. Remote GitHub Actions/Pages deployment is not claimed.
