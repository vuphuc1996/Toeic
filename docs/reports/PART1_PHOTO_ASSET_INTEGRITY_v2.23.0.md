# Part 1 Pexels Photo Asset Integrity — v2.23.0

- **Date:** 2026-11-11
- **Expected assets:** 8 local JPEG files under `assets/listening/`
- **Attribution manifest:** `assets/listening/ATTRIBUTION.csv`
- **Runtime fallback:** the corresponding SVG remains required and is used when a JPG is absent or fails to load.

## Required filenames

1. `part1-meeting-documents.jpg`
2. `part1-warehouse-box.jpg`
3. `part1-technician-inspection.jpg`
4. `part1-airport-suitcase.jpg`
5. `part1-presentation-room.jpg`
6. `part1-reception-plant.jpg`
7. `part1-restaurant-setting.jpg`
8. `part1-photocopier.jpg`

## Asset requirements

- JPEG signature and valid decodable SOF dimensions.
- Minimum dimensions: 1280 × 960 pixels; the UI displays the image in a responsive 4:3 frame.
- Each Part 1 ID must map to exactly one attribution row with matching filename, Pexels source page, photographer and Pexels license URL.
- No remote CDN fetch at lesson time; images are local repository assets.
- JPG paths are in the Service Worker `OPTIONAL` list. The eight SVG fallbacks and core app resources remain in the required shell.
- Missing optional JPGs must not abort PWA installation. The strict photo asset validator remains a separate CI/release gate and must fail if any JPG is missing or invalid.

## Current working-snapshot result

<badge>Actual JPEG bytes not present in this snapshot</badge>

- JPG files found: **0/8**.
- SVG fallbacks found: **8/8**.
- Attribution rows: **8/8**.
- `python tools/validate-part1-photo-assets.py --allow-missing`: PASS with eight explicit missing-file warnings.
- `python tools/validate-part1-photo-assets.py` (strict): **not PASS** because the eight JPG binaries are absent.
- `python tools/validate-data.py`: PASS after the validator change that treats absent `OPTIONAL` resources as optional; missing required/app-shell assets still remain errors.
- `python tools/validate-learning-content.py`: 0 errors, 8 warnings corresponding only to the missing local JPG bytes; Part 1 remains runnable through SVG fallback.

The user reports that the images were uploaded to the GitHub repository, but this working session could not retrieve the remote repository bytes. Do not infer remote presence from the manifest or image URLs. Before release, verify the eight exact files in the target branch and run strict validation against the complete repository checkout.

## Release gate

The eight photos are not considered released until the strict validator reports 8/8 valid JPEGs and the actual images are visually checked against the keyed actions. Offline/browser/device photo checks remain pending. The Pexels source URLs and photographers are stored in `ATTRIBUTION.csv`; use is subject to the Pexels license and each source record.
