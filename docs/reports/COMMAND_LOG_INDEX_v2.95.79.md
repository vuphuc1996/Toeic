# Command Log Index — TOEIC Dictionary v2.95.79

**Branch:** `candidate`
**Predecessor baseline:** `9a174778bcdfea7adca98f0abb1b17d3a050388e` (v2.95.78)
**Verified source commit:** `76ca52457929493a2a587f7673367bc29eeace49`
**GitHub Validate:** [run 46105814708](https://github.com/vuphuc1996/Toeic/actions/runs/46105814708) — PASS (151/151 steps; 848 Python tests).
**GitHub Pages:** [run 46105814298](https://github.com/vuphuc1996/Toeic/actions/runs/46105814298) — PASS on the same exact SHA.

| Order | Command / CI action | Purpose | Evidence status |
|---:|---|---|---|
| 1 | `python -m unittest discover -s tools/tests -p 'test_sync_version.py' -v` | Package drift, mismatch, dry-run, apply, missing/duplicate marker safety | **PASS** |
| 2 | `python tools/sync-version.py --check` | Manifest, package, app, HTML, Service Worker, docs and cache-key coherence | **PASS** |
| 3 | `--dry-run` regression cases in `test_sync_version.py` | Confirm dry-run is read-only for version drift | **PASS** |
| 4 | `python tools/validate-data.py` | Canonical vocabulary IDs, manifest and data constraints | **PASS** |
| 5 | `python tools/validate-learning-content.py` | Listening / Reading / Grammar content integrity | **PASS** |
| 6 | Full Python test discovery | Complete discovered Python suite | **PASS** |
| 7 | JavaScript syntax and Node regression checks | Runtime syntax and behavioral regression suite | **PASS** |
| 8 | GitHub Validate | Exact source commit; 151/151 steps, 848 Python tests | **PASS** |
| 9 | GitHub Pages build/deploy | Exact same source SHA; build/deploy/status jobs successful | **PASS** |

## Source acceptance evidence

All v2.95.79 Validate and Pages runs above are tied to exact source commit `76ca52457929493a2a587f7673367bc29eeace49`. The release evidence ledger is a documentation-only follow-up; it does not change tested application/runtime/data files.

## Predecessor evidence

v2.95.78 candidate HEAD `9a174778bcdfea7adca98f0abb1b17d3a050388e`: Validate [run 46100602552](https://github.com/vuphuc1996/Toeic/actions/runs/46100602552) and Pages build/deploy [run 46100602152](https://github.com/vuphuc1996/Toeic/actions/runs/46100602152) passed on that predecessor only.

Installed-PWA propagation, physical-device QA and production deployment are not inferred from source tests.
