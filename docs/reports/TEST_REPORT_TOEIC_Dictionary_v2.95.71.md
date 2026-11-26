# Test Report — TOEIC Dictionary v2.95.71

## Source baseline

- Sole predecessor: `TOEIC_Dictionary_v2.95.70_FullSource.zip`
- SHA-256: `1a0df44d309d127df3d3fb5012e7a6654c93a450c591f1f67575f4d15822e672`
- 864 files; ZIP CRC verified before extraction and editing.

## Python full inventory

- Test modules discovered: **107**
- Modules completed: **107 / 107**
- Modules: 106 PASS, 1 PASS WITH SKIPS, 0 FAIL, 0 timeout, 0 import/setup/error, 0 unrun.
- Cases: **799** collected; **798 PASS**, 0 FAIL, 1 SKIP, 0 errors.
- The sole skip is a Git-metadata-dependent check: a FullSource ZIP intentionally contains no `.git` metadata. Its other 19 test cases passed.
- `test_validator.py`: 44/44 PASS in 63.27 seconds.
- Full sharded execution used 120-second per-module timeout and completed all modules; it was not split into partial test methods.
- Machine-readable and Markdown inventory: `PYTHON_TEST_SHARDS_v2.95.71.json/.md`.

## Node regression

- **45/45 scripts PASS**, terminal marker `NODE_SUITE_PASS`.
- JavaScript syntax: `assets/js/app.js` and `sw.js` PASS.
- Python compileall: `python -m compileall -q tools` PASS.

## Other validations

| Check | Result |
|---|---|
| `validate-data.py` | PASS; 1,141 records; IDs +0/−0; 0 errors, 0 legacy warnings |
| `validate-learning-content.py` | PASS; 0 errors, 0 warnings |
| `audit-repository-integrity.py` | PASS; 409 references/data files inspected; 0 errors, 0 optional warnings |
| Part 1 local photo assets | PASS; 9/9 valid |
| `sync-version.py --check` | PASS; 18 release markers +17 app import keys +42 Service Worker precache keys |
| `sync-design-profile.py --check` | PASS; 54 design tokens and 406 typography selector groups synchronized |
| Design-token audit | 0 new violations; 2,773 legacy findings remain as warnings |
| Related Glossary quality audit | 567 entries; 119 flagged; 0 duplicate normalized groups |
| Vocabulary relationship graph | Read-only audit; no mutation |
| Word Family graph | Read-only: 90 missing canonical targets, 1 POS mismatch, 72 Vietnamese sense-anchor mismatches, 10 non-reciprocal links; 0 duplicate links and 0 malformed records |
| CI coverage contract | 9/9 PASS; Word Family report path is derived from current manifest release |
| Word Family report contract | 1/1 PASS |

## Implementation completed

1. Related Glossary Batch 045 enriches metadata on 23 already existing relation-target entries, using Cambridge Dictionary indexed entry evidence and preserving Vietnamese meanings and all relation arrays.
2. Project progress dashboard calculates a reproducible **54.47% provisional weighted measurable curriculum-build index** using seven published workstreams and weights. It is not official total-system completion or TOEIC readiness.
3. CI's Word Family audit report path is now release-keyed from `data/manifest.json`, replacing a stale hard-coded `.68` destination.
4. The missing-US-IPA review queue had 79 candidates; zero were safe for auto-application, so no uncertain pronunciation was invented.

## Unverified / not claimed

- GitHub-hosted Actions was not triggered or observed in this run.
- GitHub Pages deployment and live-site behavior were not verified.
- Installed PWA offline/update propagation and physical iOS/iPadOS/Android checks were not performed.
- No Git push or production deployment acceptance is claimed.
