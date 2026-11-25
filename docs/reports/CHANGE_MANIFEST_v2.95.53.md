# Change Manifest — TOEIC Dictionary v2.95.53

## User-approved scope

1. Fix iPad Pro 11-inch M1 portrait navigation so it uses the existing mobile layout; preserve desktop/web navigation in landscape.
2. Perform cross-module consistency and data-quality review; report mismatches and remaining debt without silently rewriting content.
3. Ensure visual proposals correspond to actual source CSS/HTML implementation and rendered evidence, not an unrelated mockup.

## Implementation

- `assets/css/design-system.css`: appended orientation-aware 641–850 CSS px portrait tablet rule. It hides the sidebar, resets main-area offset, uses existing five-item bottom navigation and existing menu sheet behavior, applies mobile content flow, safe-area spacing, Robot Buddy positioning and modal sizing. Uses shared design tokens and normal cascade (no added `!important`).
- `design/design-profile.json`: records 834px validation viewport and 850px tablet portrait upper boundary.
- `tools/tests/test_responsive_layout.py`: regression for iPad portrait/landscape breakpoint and mobile navigation contract.
- `tools/tests/test_design_system.py`: replaces the obsolete “tablet never uses phone navigation” expectation with orientation-specific portrait/landscape behavior.
- `tools/source-fingerprint-policy.json` and `tools/tests/test_test_fingerprints.py`: exclude generated test/audit/visual evidence from test-input fingerprints while retaining source/governance documents, preventing resumable checkpoints from invalidating themselves.
- `docs/MASTER_DEVELOPMENT_PROMPT.md`: adds owner-approved narrow tablet-orientation exception to the otherwise frozen UI contract.
- Reports: cross-module audit, iPad responsive acceptance, Python suite, test report and release acceptance.
- Visual evidence: source-rendered portrait/landscape screenshots and viewport JSON matrices.
- Version/cache markers synchronized to 2.95.53.

## Preserved data and runtime contracts

- No vocabulary record, headword, sense, Vietnamese meaning, POS, CEFR, IPA, synonym/antonym relation or vocabulary ID changed.
- No Listening/Reading/Grammar/Part 5 question, choice ID, answer key, source evidence or Mock eligibility changed.
- No IndexedDB schema, learner record, review history or Mock history changed.
- No app runtime JavaScript behavior, external backend, Cloudflare, GAS, iframe or hosting architecture changed.
- `data/manifest.json` changed only for release version synchronization.

## Review-only findings

Existing glossary coverage, POS/provenance, IPA, CEFR and Learning Outcome instrumentation debt is documented in `CROSS_MODULE_AUDIT_v2.95.53.md`; no unverified data was auto-enriched or deleted.
