# Command Log Index — TOEIC Dictionary v2.95.80

**Branch:** `candidate`
**Predecessor baseline:** `5bbdc5e05e396380d17d5a65f108d73aa8ee172a` (v2.95.79)
**v2.95.80 exact-commit hosted evidence:** pending CI.

| Order | Command / CI action | Purpose | Evidence status |
|---:|---|---|---|
| 1 | `python tools/audit-objective-criterion-map.py` | Verify canonical question IDs, indexes, mapping totals, Part 7 source quotes and reserve gates | **PENDING CI** |
| 2 | `python -m unittest discover -s tools/tests -p 'test_objective_criterion_map.py' -v` | New mapping coverage and cross-document fail-closed regression tests | **PENDING CI** |
| 3 | `python -m unittest discover -s tools/tests -p 'test_learning_outcomes.py' -v` | Full 33-criterion outcome/report reconciliation | **PENDING CI** |
| 4 | `python tools/audit-learning-outcome-evidence.py` | Generate the current criterion matrix from canonical outcome/resource/question maps | **PENDING CI** |
| 5 | `python tools/sync-version.py --check` | Verify release markers and app/Service Worker/mock cache keys | **PENDING CI** |
| 6 | Full Python test discovery | Complete discovered Python suite | **PENDING CI** |
| 7 | GitHub Validate | Exact-commit source acceptance | **PENDING** |
| 8 | GitHub Pages build/deploy | Exact-commit Pages acceptance, distinct from production approval | **PENDING** |

## Expected post-change inventory

- 1,103 mapping links across 638 unique stable question keys.
- 22/27 TOEIC criteria mapped; five deliberately uninstrumented.
- Foundation 6/6; total outcome pathways 28/33.
- Listening reserve remains excluded; Part 7 second-review and Separate Part 5 independent-review remain active.
