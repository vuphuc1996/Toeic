# Change Manifest — v2.95.12 candidate

## Version roles

- **Baseline to compare against:** v2.95.11, Git commit `daab38d`.
- **Candidate to review:** v2.95.12, local candidate source after the commits listed in Git History.
- Claude is asked to review the candidate and compare it with the baseline, not to treat v2.95.11 as the submission release.

## Candidate changes

### A. Vocabulary sense precision

- Nine existing headwords are expanded: `address`, `application`, `claim`, `draft`, `issue`, `order`, `record`, `position`, `term`.
- Twenty original English/Vietnamese examples are mapped to senses with `sense_index`.
- Multi-sense headwords: 30 → 39; examples attached to multi-sense records: 61 → 81.
- 22 related-term glossary entries gain Vietnamese meanings and Cambridge source URLs.
- `claimant → claim` is narrowed to the noun sense; `order` uses the procurement term `purchase order`.
- No new headword is created. All IDs, headwords and topic arrays are preserved.
- Editorial status remains provisional / pending independent review.

### B. Controlled data patching

- Four version-locked vocabulary patches under `patches/v2.95.12/`.
- One related-term patch under `patches-related-terms/v2.95.12/`.
- The related-term patcher checks exact Cambridge hostname/path, required data fields, duplicates, SHA-256 base-file precondition and safe rollback. It preserves file permissions and restores original bytes if audit output fails.
- Replay from the baseline Git archive reproduced the candidate's eight affected A–Z letter files plus `data/related-terms.json` byte-for-byte.

### C. Flashcard learning UX

- The maximum 10-card session rule from v2.95.10 is unchanged; the removed 5-card setting stays removed.
- Flashcard back now displays all non-primary meanings and the bilingual example linked to each extra sense.
- New helper: `assets/js/flashcard-senses.js`.
- Helper output escapes HTML, returns empty markup for single-sense terms and matches examples by exact `sense_index`.
- New helper is listed in both Service Worker `REQUIRED` and `APP_SHELL` caches for offline support.
- Automated browser-like rendering was not run; a Node unit test exercises actual helper output, and browser layout is an owner manual-acceptance item.

### D. Retained behavior

- Robot Buddy progressive local response stream and current-item context behavior remain unchanged.
- Learning Insights/dashboard, PWA user-consent update lifecycle, TTS timing, question banks and Mock eligibility are retained.

## Source/file groups

- `data/vocabulary/{A,C,D,I,O,P,R,T}.json`: existing records updated; identity/topic fields unchanged.
- `data/vocabulary/batch-014.json`, `batch-015.json`, `batch-016.json`: provenance snapshots.
- `data/related-terms.json`: 22 new gloss entries.
- `patches/v2.95.12/`, `patches-related-terms/v2.95.12/`: reproducible patch payloads.
- `tools/patch-related-terms.py`, `tools/tests/test_patch_related_terms.py`: safe glossary patching and tests.
- `assets/js/flashcard-senses.js`, `assets/js/app.js`, `assets/css/app.css`, `sw.js`: multi-sense Flashcard rendering, styling and precache.
- `tools/tests/flashcard-senses.mjs`, `flashcard-fixed-batch.mjs`, `service-worker-update.mjs`, `.github/workflows/validate-data.yml`: regression/CI coverage.
- `docs/`: Master, changelog, coverage, test, command, progress and 18-item manual-acceptance records.

## Out of scope / invariants

- No IELTS or Speaking/Writing expansion.
- No new vocabulary headwords, stable IDs, topic assignments or new question/answer data.
- No learner-storage schema/key changes, data clearing or migrations.
- No remote push, Actions execution or Pages deployment from this workspace.
- Calm Study Blue remains conditional pending owner approval; no bulk CSS redesign is included.
