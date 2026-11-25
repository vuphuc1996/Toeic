# Test Report — TOEIC Dictionary v2.95.53

## Release summary

**Local source validation: PASS WITH SKIPS. Production acceptance: NOT YET VERIFIED.**

## Dynamic Python suite

- Approved root: `tools/tests`.
- Baseline inventory: v2.95.45 (88 modules); current inventory: 91 modules.
- Discovered / terminal: **91 / 91 modules**.
- Test cases: **707 collected / 706 passed / 1 accepted skip / 0 failed / 0 errors**.
- Module outcomes: **90 PASS + 1 PASS WITH SKIPS**.
- Timed out / not run / deselected: **0 / 0 / 0**.
- Accepted skip: `test_patch_data.PatchDataTests.test_repository_gitignore_excludes_audit_logs`; reason: `source archive has no Git metadata; gitignore assertion requires a clone`. The exact reason is allowlisted in `tools/test-inventory-policy.json`; the skipped case is not counted as PASS.
- `test_validator.py`: 38/38 methods passed in four disjoint `unittest discover -k` groups because the complete module exceeded the single-command execution window. The module has per-test `setUp` and no class-level fixtures. All methods were run exactly once.
- After the generated-evidence fingerprint-scope correction, affected modules were rerun: `test_test_fingerprints.py` 10/10, `test_python_test_shard_runner.py` 19/19 and `test_release_acceptance_runner.py` 10/10 PASS. The added fingerprint regression raises the final aggregate case count from 706 to 707.
- Inventory delta: 3 added test modules, 0 removed, 0 suspected renames.
- Machine-readable evidence: `PYTHON_TEST_SHARDS_v2.95.53.json` and `.md`.

## JavaScript syntax and runtime regression

- `node --check sw.js`: PASS.
- Every `assets/js/*.js` file was copied to a temporary `.mjs` path and passed `node --check`.
- **40/40 Node runtime/regression scripts PASS**, including runtime render/migration, listening/TTS pacing, Mock exam engine, guided flow, choice identity, flashcards, objective evidence, Foundation Reading/Listening, Robot Buddy privacy/data boundaries, service-worker update lifecycle and legacy Google AI handoff.
- Node version in this environment: v22.16.0; hosted workflow targets Node 24.

## Responsive / design-system regression

| Test | Result |
|---|---:|
| `test_responsive_layout.py` | 8/8 PASS |
| `test_design_system.py` | 19/19 PASS |
| `test_design_profile.py` | 6/6 PASS |
| `test_audit_design_tokens.py` | 8/8 PASS |
| `audit-design-tokens.py` | 0 new violations |
| `sync-design-profile.py --check` | PASS — 54 tokens / 406 legacy font-floor selector groups |
| Browser viewport matrix | 5 profiles PASS |
| All-page overflow matrix | 44/44 checks; 0 horizontal overflows |

Visual browser evidence is in `visual-evidence/v2.95.53/`. It is rendered from the source HTML and source CSS; scripts were omitted for deterministic CSS/DOM geometry. This is not a physical iPad Safari acceptance test.

## Data and repository audits

- `validate-data.py`: **PASS**, 1,141 vocabulary records; 0 ID additions/removals; 0 ERROR / 0 WARNING. ID-set SHA-256 prefix `adccbdb4c9887220`.
- `validate-learning-content.py`: **PASS**, 0 errors / 0 warnings.
- `validate-part1-photo-assets.py`: **PASS**, 9/9 files valid; 0 missing-photo warnings.
- `audit-repository-integrity.py`: **PASS**, 429 references/data files inspected; 0 errors / 0 optional warnings.
- `audit-objective-resources.py`: **PASS**, 379/379 resource records linked.
- `audit-learning-outcomes.py`: **PASS**, 11 objectives / 33 criteria; 6 criteria have evidence-collection paths. The 27 uninstrumented criteria remain unmeasured.
- Related Glossary quality: 567 entries; 198 flagged; 131 missing definitions; 63 placeholders; 190 missing POS; 65 missing provenance; counts overlap.
- Relation-target coverage: 556/804; 248 unique targets / 249 occurrences remain uncovered.
- Vocabulary relationship graph: 1,037 references; 0 malformed items; 0 self-references; 0 duplicate normalized headwords; 248 non-reciprocal references are review flags.
- Full cross-module debt and interpretation: `CROSS_MODULE_AUDIT_v2.95.53.md`.

## Protected-data checks

- Canonical vocabulary identity SHA-256 prefix remains `adccbdb4c9887220`; no IDs added or removed.
- No vocabulary headword/sense/meaning/relation array, question ID, choice ID, answer key or Mock eligibility was modified.
- IndexedDB schema and learner records were not modified.
- Only the release version in `data/manifest.json` and registered version/cache markers changed for v2.95.53.

## Hosted / physical acceptance boundary

- Local source tests and viewport simulation: PASS WITH SKIPS.
- Hosted GitHub Actions: **UNVERIFIED**.
- GitHub Pages deployed artifact/commit identity: **UNVERIFIED**.
- Service Worker propagation on a real installation: **UNVERIFIED**.
- Offline/reconnect behavior after deployment: **UNVERIFIED**.
- Physical iPad Pro 11-inch M1 Safari and Home Screen PWA: **UNVERIFIED**.

A passing source archive or simulated viewport must not be represented as proof of hosted deployment or physical-device acceptance.
