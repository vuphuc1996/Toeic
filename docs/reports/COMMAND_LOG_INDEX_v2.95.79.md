# Command Log Index — TOEIC Dictionary v2.95.79

**Branch:** `candidate`
**Predecessor baseline:** `9a174778bcdfea7adca98f0abb1b17d3a050388e` (v2.95.78)
**Current v2.95.79 hosted evidence:** pending the new exact-commit runs.

| Order | Command / CI action | Purpose | Evidence status |
|---:|---|---|---|
| 1 | `python -m unittest discover -s tools/tests -p 'test_sync_version.py' -v` | Package drift, mismatch, dry-run, apply, missing/duplicate marker safety | **PENDING CI** |
| 2 | `python tools/sync-version.py --check` | Manifest, package, app, HTML, Service Worker, docs and cache-key coherence | **PENDING CI** |
| 3 | `python tools/sync-version.py --dry-run` | Confirm a clean release tree produces no edits | **PENDING CI** |
| 4 | `python tools/validate-data.py` | Canonical vocabulary IDs, manifest and data constraints | **PENDING CI** |
| 5 | `python tools/validate-learning-content.py` | Listening / Reading / Grammar content integrity | **PENDING CI** |
| 6 | Full Python test discovery | Complete discovered Python suite | **PENDING CI** |
| 7 | JavaScript syntax and Node regression checks | Runtime syntax and behavioral regression suite | **PENDING CI** |
| 8 | GitHub Validate | Exact-commit hosted source acceptance | **PENDING** |
| 9 | GitHub Pages build/deploy | Exact-commit hosted Pages result; distinct from production approval | **PENDING** |

## Predecessor evidence

v2.95.78 candidate HEAD `9a174778bcdfea7adca98f0abb1b17d3a050388e`: Validate [run 46100602552](https://github.com/vuphuc1996/Toeic/actions/runs/46100602552) and Pages build/deploy [run 46100602152](https://github.com/vuphuc1996/Toeic/actions/runs/46100602152) passed on that predecessor only.

Installed-PWA propagation, physical-device QA and production deployment are not inferred from source tests.
