# Test Report — TOEIC Dictionary v2.95.49

Date: 2026-11-24

## Scope

Suppress known Related Glossary editorial placeholder definitions from learner-facing synonym/antonym answer explanations. Preserve genuine definitions, Vietnamese meanings and POS metadata. Add the new JavaScript module to the required service-worker app shell and CI checks. No canonical glossary data or learner data was rewritten.

## Results actually observed

| Check | Cases / scope | Result |
|---|---:|---|
| `node tools/tests/related-glossary-quality.mjs` | 13 placeholder patterns; valid definitions; app integration; 73 canonical placeholder rows | PASS |
| `python -m unittest discover -s tools/tests -p test_related_term_explanation_context.py -v` | 4 | PASS 4/4 |
| Full dynamic Python sharded suite | 89 modules / 693 collected | **PASS WITH SKIPS**: 88 modules PASS; 1 module PASS WITH SKIPS; 692 passed / 1 accepted skip / 0 fail / 0 error / 0 timeout / 0 not run |
| `tools/tests/test_validator.py` within full suite | 38 | PASS 38/38 (63.62s) |
| `.github/workflows/validate-data.yml` local shell replay | 110 run steps | PASS 110/110; 0 fail / timeout / error / pending |
| `python tools/sync-version.py --check` | 13 markers + changelog | PASS |
| `python tools/validate-data.py` | 1,141 records | PASS; 0 errors / 0 legacy warnings; 0 IDs added / missing |
| `python tools/audit-learning-outcomes.py` | 11 objectives / 33 criteria | PASS; 6/33 criteria have evidence-collection paths; Foundation 6/6 |
| `python tools/audit-objective-resources.py` | 379 resource links | PASS; 379/379 |
| Related Glossary quality audit | 567 entries | PASS (read-only): 227 flagged for review; 223 high / 2 medium / 2 low; 150 missing definitions; 73 placeholder definitions |
| Related Glossary candidate audit | 804 references | PASS (read-only): 556 covered; 248 unique missing terms; 0 missing candidates with canonical vocabulary headword |
| JavaScript syntax check | all `assets/js/*.js` | PASS in local workflow replay |

## Accepted skip detail

- Module: `tools/tests/test_patch_data.py`
- Test: `test_repository_gitignore_excludes_audit_logs`
- Reason: `source archive has no Git metadata; gitignore assertion requires a clone`
- Policy: explicitly accepted by `tools/test-inventory-policy.json`; not counted as PASS.

## Incomplete / unverified

- Local replay executed every `run:` step in `.github/workflows/validate-data.yml` and all passed. This is not a remote GitHub-hosted Actions run.
- GitHub Pages deployment, live cache propagation, installed PWA update, offline behavior and physical iOS/Android/tablet/desktop acceptance remain UNVERIFIED.

## Data integrity and protected invariants

- `data/related-terms.json` was not modified; all 73 placeholder records remain in canonical source but are no longer displayed as English definitions.
- Vocabulary data: 1,141 records; no ID additions/removals; ID-set SHA-256 prefix `adccbdb4c9887220`.
- Question IDs, choices, answer keys, Mock eligibility, learner history and IndexedDB schema were not modified.
- `sw.js` includes `assets/js/related-glossary-quality.js` in both REQUIRED and APP_SHELL arrays to support installation/offline use.
- No UI layout redesign, backend, Cloudflare, GAS or iframe changes.

## Evidence files

- `PYTHON_TEST_SHARDS_v2.95.49.md` and `.json`
- `GITHUB_ACTIONS_SHELL_REPLAY_v2.95.49.md` and `.json`
- `RELATED_GLOSSARY_QUALITY_v2.95.49.md` and `.json`
- `RELATED_GLOSSARY_CANDIDATES_v2.95.49.md`
