# Test Report — v2.95.25 audit follow-up

## PASS
- 78 focused Python tests across 11 modules (including major-release audit, outcome evidence, glossary backlog/backfill, packaging, CI coverage, integrity, version sync, content and data validation test groups).
- 39 JavaScript regression suites.
- `tools/validate-data.py`: PASS, 0 errors and 0 warnings.
- `tools/validate-learning-content.py`: PASS, 0 errors and 0 warnings.
- `tools/sync-version.py --check`: PASS.
- Major release audit: PASS; 33 criteria detailed; 6 instrumented; 27 not yet instrumented.

## Incomplete / not run
- Full `unittest discover` timed out.
- `test_validator.py` timed out partway through and is not counted in focused total.
- Remote GitHub CI, live GitHub Pages, browser/device, offline/reconnect acceptance and deployment not run.

## Interpretation
Instrumentation status describes evidence collection wiring only. It is not completion, learner mastery, independent assessment or CEFR/ETS certification.
