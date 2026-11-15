# Visual composition and Part 1 media report — v2.64.0

## Scope

This release addresses the user-reported portrait Part 1 photocopier image size mismatch, card/button/content overflow and visual density differences between desktop, laptop, tablet and phone widths.

## Implemented

- All Part 1 media is rendered in a 4:3 frame with shared responsive width, radius, crop and caption. `part1-photocopier` uses `object-position: 50% 42%` to place its subject within the common crop.
- CSS does not rewrite the licensed JPG. The source is still referenced by `data/listening/listening-library.json` and `assets/listening/ATTRIBUTION.csv`; the SVG fallback remains if the photo request fails.
- Learning/Foundation/listening/reading card grids share equal row sizing, card flex layout, consistent title and copy baselines, and footer alignment. Long copy wraps and expands the row rather than being clipped.
- Buttons can wrap, keep minimum touch height and have `min-width: 0`; text overflow uses `overflow-wrap: anywhere`.
- A–Z practice grid is four columns on desktop, three on tablet landscape, two on tablet portrait and phone, and one at 360px and below.

## Asset limitation

The supplied local v2.63.0 source archive does not contain the original `part1-photocopier.jpg` binary (or seven other licensed Part 1 JPGs); only the SVG fallback and attribution metadata are present in the workspace snapshot. The user supplied the repository URL for the original image, but this workspace could not retrieve the binary. Therefore this patch standardizes the presentation rule and crop focal point; it does not claim to have resampled or embedded the original photo. The strict asset validator remains enabled.

## Verification target

Run at 320, 360, 390, 430, 641, 768, 820, 1024, 1280, 1440 and 1920 CSS pixels. Expected: no horizontal page overflow; no overlapping text/buttons; Part 1 media frames share a 4:3 outer ratio; cards in each grid row share outer height/footer baseline; long content expands naturally. These checks are CSS/source regression checks; physical-device QA remains pending.
