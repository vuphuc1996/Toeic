# Repository Integrity Preflight — v2.94.0

## Purpose

Prevent the recurring class of CI failures where a changed/removed/added file is no longer referenced correctly, a Service Worker asset list becomes stale, a test is omitted from GitHub Actions, or a source data file becomes invalid JSON.

## Automated coverage

`tools/audit-repository-integrity.py` is now a required GitHub Actions step. It checks:

1. Required control files (`sw.js`, workflow, `index.html`, application CSS) exist.
2. Service Worker `REQUIRED`, `APP_SHELL` and `OPTIONAL` file paths resolve; every required asset also appears in the app shell.
3. Local `href`, `src` and `poster` references in `index.html` resolve.
4. Local CSS `url(...)` references resolve relative to their stylesheet.
5. Static relative JavaScript imports and literal `releaseDataUrl()` references resolve.
6. Explicit scripts/files referenced by workflow commands exist.
7. Every `tools/tests/test_*.py` file is selected by a Python unittest pattern in the workflow.
8. Every `tools/tests/*.mjs` regression suite is invoked by the workflow.
9. Every JSON file under `data/` parses successfully.

## v2.94.0 result

- Local references and data files inspected: **361**.
- Errors: **0**.
- Optional warnings: **0**.
- `test_repository_integrity.py`: PASS.
- `test_ci_coverage.py`: PASS; all Python and JavaScript test files are registered in the workflow.

## Boundary

This is a structural preflight, not a proof that software has no defects. It cannot emulate GitHub-hosted runner behavior, remote deployment, physical device APIs, browser rendering or audible speaker output. The full CI workflow and user acceptance round remain required. Automated test/audit files are intentionally retained in source and are not exposed as learner-facing test content.
