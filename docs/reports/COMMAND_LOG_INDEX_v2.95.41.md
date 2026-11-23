# Command Log Index — TOEIC Dictionary v2.95.41

All commands below were run from the v2.95.41 source root unless noted.

## Python regression

- `python -m unittest discover -s tools/tests -p 'test_answer_position_balance.py' -v` — 4/4 PASS.
- `python -m unittest discover -s tools/tests -p 'test_listening_expansion.py' -v` — 8/8 PASS.
- `python -m unittest discover -s tools/tests -p 'test_question_evidence.py' -v` — 7/7 PASS.
- `python -m unittest discover -s tools/tests -p 'test_distractor_quality.py' -v` — 6/6 PASS.
- `python -m unittest discover -s tools/tests -p 'test_content_batch_027.py' -v` — 6/6 PASS.
- `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v` — 3/3 PASS.
- `python -m unittest discover -s tools/tests -p 'test_sync_version.py' -v` — 12/12 PASS.
- Total focused Python scope: 46/46 across 7 modules (not full project discovery).
- `python -m compileall -q tools` and `python -m py_compile tools/tests/test_answer_position_balance.py` — PASS.

## JavaScript regression and syntax

- Run each `tools/tests/*.mjs` with Node — 39/39 PASS.
- `node --check sw.js` — PASS.
- `node --check assets/js/*.js` (18 modules) — PASS.

## Validators / audits

- `python tools/validate-data.py` — PASS, 1,141 records, 0 errors / 0 warnings, no stable ID additions/removals.
- `python tools/validate-learning-content.py` — PASS, 0 errors / 0 warnings.
- `python tools/audit-repository-integrity.py` — PASS, 411 references/data files, 0 errors / 0 optional warnings.
- `python tools/sync-version.py --check` — PASS, all version markers v2.95.41.
- `python tools/sync-design-profile.py --check` — PASS, 54 tokens / 406 selector groups.
- `python tools/validate-part1-photo-assets.py` — PASS, 9/9.
- `python tools/audit-objective-resources.py` — PASS, 379/379.
- `python tools/audit-learning-outcomes.py` — PASS, 11 objectives / 33 criteria / 6 evidence paths.
- `python tools/audit-foundation-a2-assessment.py` — PASS, core and supplementary A2 checks.
- `python tools/audit-listening-readiness.py` — PASS, 102 eligible / 193 pending / 295 total.
- `python tools/audit-question-evidence.py` — PASS, 582 questions indexed and 193 Listening reserves traced.
- `python tools/audit-distractors.py` — PASS, 264-question structural scope.
- `python tools/audit-toeic-coverage.py` — PASS, current v2.95.41 coverage report generated.
- `python tools/report-project-progress.py` — PASS, current v2.95.41 progress snapshot generated.

## Full Source package verification

- `TOEIC_Dictionary_v2.95.41_FullSource.zip` — 597 files, one root `Toeic_Dictionary_v2.95.41/`.
- ZIP CRC check PASS; archive has no `.git`, caches, `__pycache__`, `.pyc`, `.pyo` or nested release ZIPs.
- Exact source comparison PASS — 597/597 archived files are byte-identical to the release tree.
- External SHA-256 sidecar generated and verified against the final archive.

## Release boundaries

- Remote GitHub Actions, production GitHub Pages deployment/cache, browser visual checks and physical-device audio/UI acceptance were not run here.
- Full aggregate Python discovery is not claimed.
