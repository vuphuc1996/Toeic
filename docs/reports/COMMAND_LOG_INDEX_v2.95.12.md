# Command Log Index — v2.95.12

Date: 2026-11-19 (Asia/Ho_Chi_Minh)

All commands below ran in the v2.95.12 local candidate checkout. Test logs are supplied in the one-shot handoff's `TEST_EVIDENCE/` folder. Exit codes are recorded from the command process, not inferred from output text.

## JavaScript regression

- **Command pattern:** `node tools/tests/<suite>.mjs` (each invoked individually from the exact suite list in `.github/workflows/validate-data.yml`).
- **Result:** 38/38 PASS; 0 FAIL; total runtime ~1.84 s.
- Full output: `javascript-final.log`.
- New tests include `flashcard-senses.mjs`; existing `flashcard-fixed-batch.mjs`, `robot-buddy-streaming.mjs` and `service-worker-update.mjs` also passed.

## Python unit modules

| Command pattern | Tests | Result | Elapsed reported by unittest |
|---|---:|---|---:|
| `python -m unittest discover -s tools/tests -p 'test_patch_related_terms.py' -v` | 11 | Exit 0 | 9.738 s |
| `python -m unittest discover -s tools/tests -p 'test_vocabulary_detail_examples.py' -v` | 15 | Exit 0 | 0.075 s |
| `python -m unittest discover -s tools/tests -p 'test_vocabulary_family_links.py' -v` | 6 | Exit 0 | 0.012 s |
| `python -m unittest discover -s tools/tests -p 'test_baseline_ids.py' -v` | 13 | Exit 0 | 20.310 s |
| `python -m unittest discover -s tools/tests -p 'test_patch_data.py' -v` | 20 | Exit 0 | 17.173 s |
| `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v` | 3 | Exit 0 | 0.002 s |
| `python -m unittest discover -s tools/tests -p 'test_audit_design_tokens.py' -v` | 8 | Exit 0 | 0.012 s |
| `python -m unittest discover -s tools/tests -p 'test_learning_content.py' -v` | 34 | Exit 0 | 0.027 s |
| `python -m unittest discover -s tools/tests -p 'test_repository_integrity.py' -v` | 1 | Exit 0 | 0.828 s |
| `python -m unittest discover -s tools/tests -p 'test_design_system.py' -v` | 19 | Exit 0 | 0.002 s |
| `python -m unittest discover -s tools/tests -p 'test_responsive_layout.py' -v` | 7 | Exit 0 | 0.006 s |
| `python -m unittest discover -s tools/tests -p 'test_vocabulary_batch_012.py' -v` | 4 | Exit 0 | 0.022 s |
| `python -m unittest discover -s tools/tests -p 'test_design_profile.py' -v` | 6 | Exit 0 | 1.538 s |
| **Total** | **147** | **13 modules PASS** | |

Logs: `python-targeted.log`, `test_patch_data.log`, `test_ci_coverage.py.log`, `test_audit_design_tokens.py.log`, `test_learning_content.py.log`, `test_repository_integrity.py.log`, `test_design_system.py.log`, `test_responsive_layout.py.log`, `test_vocabulary_batch_012.py.log`, `test_design_profile.log`.

## Validators / audits / sync

| Command | Exit | Result |
|---|---:|---|
| `python tools/validate-data.py` | 0 | 1,141 records; ID additions 0 / missing 0; 0 errors / 0 warnings |
| `python tools/validate-learning-content.py` | 0 | Listening/Reading/Grammar/Part 5 inventory valid; 0 errors / 0 warnings |
| `python tools/audit-toeic-coverage.py` | 0 | Generated `TOEIC_CONTENT_COVERAGE_v2.95.12.md` |
| `python tools/audit-repository-integrity.py` | 0 | 372 references; 0 errors / 0 optional warnings |
| `python tools/audit-design-tokens.py` | 0 | 2,778 known legacy warnings; 0 new violations |
| `python tools/sync-version.py --check` | 0 | All release markers synchronized |
| `node --check assets/js/*.js` and `node --check sw.js` | 0 | All JavaScript syntax checks passed |
| `python -m compileall -q tools` | 0 | Python tools compile |
| `git diff --check` | 0 | No whitespace errors |

Full outputs: `validate-data.timed.log`, `validate-learning-content.timed.log`, `audit-toeic-coverage.timed.log`, `audit-repository-integrity.timed.log`, `audit-design-tokens.timed.log`, `sync-version.timed.log`, `javascript-final.log`.

## Patch replay proof

- Start source: clean archive of Git HEAD v2.95.11 (`git archive HEAD`).
- Each of four vocabulary patches: `python tools/patch-data.py --root <temp> --patch <patch> --dry-run` then `--apply` (each exit 0).
- Related glossary patch: `python tools/patch-related-terms.py --root <temp> --patch patches-related-terms/v2.95.12/related-terms-001.json --dry-run` then `--apply` (each exit 0).
- Final `validate-data.py --root <temp>` exit 0.
- Rollback proof: related-term `--rollback` exit 0; output file matched baseline bytes exactly.
- Replayed eight affected A–Z files and `related-terms.json` were byte-identical to the v2.95.12 candidate.

## Incomplete / not run

- A combined Python test invocation hit the container time limit before the aggregate completed. The same 13 focused modules were then run individually and all 147 tests passed.
- The complete Python inventory and `test_validator.py` unit module are not claimed as run; actual validator CLI passed.
- No browser/device/manual checks, GitHub Actions remote run, Pages deploy or push were performed.
