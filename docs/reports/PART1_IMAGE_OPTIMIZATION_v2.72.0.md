# Part 1 Image Optimization — v2.72.0

- Source: user-provided `Picture.zip`; all nine expected filenames were present. No image-generation step was used.
- Method: no AI generation. Eight licensed Pexels originals were resized/re-encoded; the existing project-owned `part1-office-cleaning.jpg` was preserved byte-for-byte.
- Shared output canvas: **1448×1086 px (4:3 landscape)**.
- JPEG: progressive, optimized, quality 84 (lowered only if needed to meet ceiling).
- Size ceiling: **400,000 bytes per image**.
- Part 1 photocopier: portrait original was cropped to a 4:3 landscape composition using the full source width and a reviewed vertical crop starting at 58% of the removable vertical area; the crop keeps the hand operating the copier and the control panel visible.
- Other landscape photos: centered 4:3 crop. No stretching or non-uniform scaling.
- Attribution rows, source URLs, photographers, license references, item IDs, question IDs, answer keys and explanations were not changed.

| File | Original dimensions | Original size | Packaged dimensions | Packaged size | Reduction |
|---|---:|---:|---:|---:|---:|
| `part1-meeting-documents.jpg` | 6000×4000 | 1,778,174 B | 1448×1086 | 165,454 B | 90.7% |
| `part1-warehouse-box.jpg` | 6000×4000 | 4,057,665 B | 1448×1086 | 204,939 B | 94.9% |
| `part1-technician-inspection.jpg` | 5293×3760 | 2,455,649 B | 1448×1086 | 371,874 B | 84.9% |
| `part1-airport-suitcase.jpg` | 6720×4480 | 7,048,197 B | 1448×1086 | 195,016 B | 97.2% |
| `part1-presentation-room.jpg` | 5473×3654 | 3,351,783 B | 1448×1086 | 217,789 B | 93.5% |
| `part1-reception-plant.jpg` | 5120×3413 | 1,329,143 B | 1448×1086 | 204,150 B | 84.6% |
| `part1-restaurant-setting.jpg` | 7360×4912 | 3,788,633 B | 1448×1086 | 219,055 B | 94.2% |
| `part1-photocopier.jpg` | 3923×5885 | 1,057,552 B | 1448×1086 | 86,632 B | 91.8% |
| `part1-office-cleaning.jpg` | 1448×1086 | 398,363 B | 1448×1086 | 398,363 B | 0.0% (kept) |

- Combined original image bytes: **25,265,159 bytes**.
- Combined packaged image bytes: **2,063,272 bytes**.
- Combined image payload reduction: **91.8%**.
- The strict asset validator now also checks common 4:3 landscape geometry and the 400,000-byte per-file ceiling.
- `restore-part1-photos.bat` and its download-only Python helper were retired from the current release. They downloaded large original Pexels files and did not optimize them. The new full-source archive already embeds the optimized assets; no photo download step is required.
