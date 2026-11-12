# Batch 016 — Flashcard image relevance & responsive layout (v2.26.0)

## User requirement
Remove misleading images from vocabulary flashcards, or show only an image that clearly represents that exact vocabulary item. Preserve useful topic-level illustrations separately. Make approved images fit phone/tablet/desktop frames without awkward cropping or overflow.

## Implemented
- Individual vocabulary cards are now text-first by default. They no longer take the first `topics[]` value and display its generic `assets/topics/*` artwork as if it represented the headword.
- Topic thumbnails remain on the topic-selection screen because they represent a category, not an individual vocabulary item.
- A future word-specific illustration is accepted only if all fields are present: `image` path under `./assets/vocabulary/`, meaningful `imageAlt`, and `imageStatus: "approved"`. Paths containing `..` and non-image extensions are rejected.
- Approved image cards use responsive 4:3 frames and `object-fit: contain`; very narrow phones use a compact square frame. Text-only cards use the full card width and do not reserve an empty image column.
- The CSS uses available viewport width, not nominal device-inch measurements. The same design therefore adapts to actual viewport sizes and orientation across 4.7–6.9-inch phones, tablets and desktop screens.

## Data and safety boundaries
- No new image files were downloaded or added. No image has been marked approved.
- All 928 canonical vocabulary records and stable IDs remain unchanged.
- No Listening, Reading, Grammar, Mock Test, TTS or IndexedDB schema/profile data changed.
- Personal IndexedDB import/export/inspection/reset/migration remains deferred.

## Acceptance
- `node tools/tests/flashcard-image-policy.mjs` verifies no generic topic image is rendered on a vocabulary card and enforces the explicit approved-image contract.
- JavaScript syntax, runtime smoke, Mock UI integrity, data validator and version synchronization are checked in the v2.26.0 test report.
