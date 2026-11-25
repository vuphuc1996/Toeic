# Release Delta — v2.95.61 → v2.95.62

## User-visible data improvement

Twenty-one already-linked Related Glossary words now have explicit POS, paraphrased English definitions and source provenance. This fills gaps for entries that were already referenced by canonical vocabulary relations; it does not add new headwords or synonyms/antonyms.

The current glossary quality audit moves from 178 to 157 flagged entries. Placeholder definitions fall from 63 to 50, missing English definitions from 111 to 103, missing POS from 174 to 153, and missing provenance from 65 to 52. There are still 50 placeholders and 103 blank definitions; this batch does not claim the glossary is complete.

## Compatibility and retention

The patch updates only 21 existing Related Glossary metadata fields. Vietnamese meanings and all synonym/antonym arrays remain byte/value-stable for those rows; canonical vocabulary and learning banks are not modified. No learner IndexedDB migration or data rewrite is introduced.

## Interface and deployment

No UI redesign or layout change. Only registered application/service-worker/index release version strings advance to v2.95.62. Hosting remains static GitHub Pages; no Cloudflare, API or backend is added.

## Evidence boundary

Focused local tests/validators are recorded in the test report. Full Python discovery (96 modules), hosted GitHub Actions, GitHub Pages deployment, installed-PWA cache/offline behavior and physical device acceptance are not claimed as verified. Cambridge paraphrases await independent editorial review.
