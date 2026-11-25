# Release Acceptance — TOEIC Dictionary v2.95.53

## Decision

**Local source/package acceptance: PASS WITH SKIPS. Production acceptance: NOT GRANTED.**

## Mandatory source gates

| Gate | Result | Evidence |
|---|---|---|
| Version synchronization | PASS | `sync-version.py --check` |
| Design profile synchronization | PASS | `sync-design-profile.py --check` |
| Canonical vocabulary validator | PASS | 1,141 records; 0 ID changes; 0 ERROR / 0 WARNING |
| Learning-content validator | PASS | 0 errors / 0 warnings |
| Repository integrity | PASS | 429 inspected; 0 errors / 0 optional warnings |
| Part 1 photo validation | PASS | 9/9 valid; no missing-photo warning |
| Python suite | PASS WITH SKIPS | 91/91 modules terminal; 705 PASS / 1 accepted skip |
| JavaScript syntax | PASS | `sw.js` and all `assets/js/*.js` modules |
| Node runtime regressions | PASS | 40/40 scripts |
| Responsive/design-system tests | PASS | responsive 8/8; design system 19/19; profile 6/6; token tests 8/8 |
| Design-token ratchet | PASS | 0 new violations; 2 legacy findings resolved |
| Fingerprint scope | PASS | Generated release evidence excluded from test fingerprints; source/governance docs remain included; 10/10 fingerprint tests |
| All-page viewport matrix | PASS | 44/44 checks; 0 page-level horizontal overflows |
| Cross-module audit | PASS WITH REVIEW DEBT | no structural errors; outstanding content/evidence debt documented |
| FullSource/Patch package | PASS | 638 files; 22 adds / 15 modifies / 0 deletes; CRC, exact replay and byte-for-byte comparison PASS |

## Accepted skip

`test_patch_data.PatchDataTests.test_repository_gitignore_excludes_audit_logs` is skipped because the source archive has no Git metadata and the assertion requires a clone. The exact reason is allowlisted; it is not counted as PASS.

## Remaining review debt

- 248 unique relation targets / 249 occurrences remain uncovered.
- 131 glossary definitions missing; 63 placeholders; 190 POS gaps; 65 provenance gaps (overlapping flags).
- 79 vocabulary entries lack US IPA.
- 9 word-vs-sense CEFR differences and 4 repeated definition pairs require policy/editorial review.
- 27/33 Learning Outcome criteria do not yet have evidence-collection paths.
- 193 Listening reserve questions remain pending independent review.
- 2,776 legacy design-token findings remain warnings; no new violations were introduced.

## Production gates not verified

- Hosted GitHub Actions success.
- GitHub Pages deployment and deployed artifact/commit identity.
- Real PWA Service Worker activation/update/cache propagation.
- Offline and reconnect behavior after deployment.
- Physical iPad Pro 11-inch M1 Safari and installed-PWA portrait/landscape behavior.

## iPad manual acceptance required

Follow `IPAD_RESPONSIVE_ACCEPTANCE_v2.95.53.md`. The current evidence is a Chromium viewport simulation using the actual source HTML/CSS, not a physical-device test.
