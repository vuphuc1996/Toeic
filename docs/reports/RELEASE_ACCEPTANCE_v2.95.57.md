# Release Acceptance — v2.95.57

- Baseline: exact v2.95.56 FullSource archive, SHA-256 `8ec7435b810b8ebaae4dbe608491d5212c1f52ba5b3cde407e87ab0473dfdb7a`.
- Release scope: Stage 2 item 7 read-only answer leakage / distractor-overlap diagnostic.
- Local acceptance: 42/42 Node regression scripts PASS; 36 focused Python tests PASS across 6 modules; repository integrity preflight PASS; data validator PASS; structural distractor audit PASS; answer leakage diagnostic PASS; version sync PASS.
- Question libraries and sampled vocabulary files are byte-identical to v2.95.56. No canonical content or answer data was modified.
- Listening reserve (193) and Reading reserve (87) remain excluded from Mock and from the Mock-eligible diagnostic.
- Full Python discovery was not run for this release. Hosted GitHub Actions, Pages deployment, installed PWA cache behavior and physical-device acceptance remain UNVERIFIED.
- This release does not claim ETS equivalence, psychometric calibration, or independent human approval of flagged items.
