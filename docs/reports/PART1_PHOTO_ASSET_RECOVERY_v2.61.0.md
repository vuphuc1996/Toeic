# Part 1 Photo Asset Recovery — v2.61.0

## Current status

- The source archive inherited from v2.60.0 contains only one of nine Part 1 JPG binaries (`part1-office-cleaning.jpg`). Eight licensed-stock JPGs are missing, while the matching SVG fallback files remain in `assets/listening/`.
- The eight existing `ATTRIBUTION.csv` rows already record the original Pexels photographer, source page, `direct_download` URL and Pexels license. The corresponding official photo pages and download links were opened and checked during this review.
- The container could not resolve `images.pexels.com`; therefore no original bytes could be restored in this run. No substitute or placeholder JPEG was created.
- `python tools/validate-part1-photo-assets.py` (strict mode, used by `.github/workflows/validate-data.yml`) currently fails with 8 missing-file errors. Deployment should remain on hold until the original files are restored and this strict validator passes.
- `python tools/validate-part1-photo-assets.py --allow-missing` is for local inspection only; it must not replace the strict CI gate.

## Exact assets to restore

| Learning unit | Expected file | Photographer / creator | Official page | Direct download |
|---|---|---|---|---|
| `part1-meeting-documents` | `part1-meeting-documents.jpg` | Mikhail Nilov | https://www.pexels.com/photo/coworkers-reading-documents-together-8297490/ | https://images.pexels.com/photos/8297490/pexels-photo-8297490.jpeg?cs=srgb&dl=pexels-mikhail-nilov-8297490.jpg&fm=jpg |
| `part1-warehouse-box` | `part1-warehouse-box.jpg` | cottonbro studio | https://www.pexels.com/photo/person-pulling-box-from-a-shelf-7019313/ | https://images.pexels.com/photos/7019313/pexels-photo-7019313.jpeg?cs=srgb&dl=pexels-cottonbro-7019313.jpg&fm=jpg |
| `part1-technician-inspection` | `part1-technician-inspection.jpg` | José Andrés Pacheco Cortes | https://www.pexels.com/photo/man-checking-an-air-conditioner-5463575/ | https://images.pexels.com/photos/5463575/pexels-photo-5463575.jpeg?cs=srgb&dl=pexels-jose-andres-pacheco-cortes-3641213-5463575.jpg&fm=jpg |
| `part1-airport-suitcase` | `part1-airport-suitcase.jpg` | Gustavo Fring | https://www.pexels.com/photo/woman-wearing-a-coat-holding-black-luggage-bag-3885497/ | https://images.pexels.com/photos/3885497/pexels-photo-3885497.jpeg?cs=srgb&dl=pexels-gustavo-fring-3885497.jpg&fm=jpg |
| `part1-presentation-room` | `part1-presentation-room.jpg` | Pavel Danilyuk | https://www.pexels.com/photo/chairs-arranged-inside-a-conference-room-8761316/ | https://images.pexels.com/photos/8761316/pexels-photo-8761316.jpeg?cs=srgb&dl=pexels-pavel-danilyuk-8761316.jpg&fm=jpg |
| `part1-reception-plant` | `part1-reception-plant.jpg` | Anastasiya Gepp | https://www.pexels.com/photo/woman-watering-plant-1462646/ | https://images.pexels.com/photos/1462646/pexels-photo-1462646.jpeg?cs=srgb&dl=pexels-anastasiya-gepp-654466-1462646.jpg&fm=jpg |
| `part1-restaurant-setting` | `part1-restaurant-setting.jpg` | Western Skyline Hotel | https://www.pexels.com/photo/elegant-waitress-preparing-table-for-guests-4873361/ | https://images.pexels.com/photos/4873361/pexels-photo-4873361.jpeg?cs=srgb&dl=pexels-westernhotel-4873361.jpg&fm=jpg |
| `part1-photocopier` | `part1-photocopier.jpg` | Mikhail Nilov | https://www.pexels.com/photo/a-man-operating-a-photocopier-9301897/ | https://images.pexels.com/photos/9301897/pexels-photo-9301897.jpeg?cs=srgb&dl=pexels-mikhail-nilov-9301897.jpg&fm=jpg |

## Restoration acceptance criteria

1. Place the exact original Pexels JPEG at the expected path under `assets/listening/`.
2. Do not replace the asset with a generated image while keeping `source_type=licensed-stock`.
3. Run `python tools/validate-part1-photo-assets.py`; expected result: `Part 1 photo files valid: 9/9` and `PASS`.
4. Run `python -m unittest discover -s tools/tests -p 'test_part1_photo_assets.py' -v`; expected result: 4/4 PASS.
5. Keep `ATTRIBUTION.csv` and the current `photoSourceType` values aligned with the true asset source.

## Source references

- Official Pexels photo pages are recorded in `assets/listening/ATTRIBUTION.csv` and linked in the table above.
- Pexels license: https://www.pexels.com/license/
