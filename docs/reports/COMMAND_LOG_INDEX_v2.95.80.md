# Command Log Index — TOEIC Dictionary v2.95.80

**Branch:** `candidate`
**Predecessor baseline:** `5bbdc5e05e396380d17d5a65f108d73aa8ee172a` (v2.95.79)
**Verified candidate HEAD:** `84a6b55b53c5d07a6f127c06234605efc0098edd`
**GitHub Validate:** [run 46107947688](https://github.com/vuphuc1996/Toeic/actions/runs/46107947688) — PASS (151/151 steps, 850 Python tests).
**GitHub Pages:** [run 46107947573](https://github.com/vuphuc1996/Toeic/actions/runs/46107947573) — PASS (build 7/7, status 3/3, deploy 3/3).

| Order | Command / CI action | Purpose | Evidence status |
|---:|---|---|---|
| 1 | `python tools/audit-objective-criterion-map.py` | Verify canonical question IDs, indexes, mapping totals, Part 7 source quotes and reserve gates | **PASS** |
| 2 | `python -m unittest discover -s tools/tests -p 'test_objective_criterion_map.py' -v` | New mapping coverage and cross-document fail-closed regression tests | **PENDING CI** |
| 3 | `python -m unittest discover -s tools/tests -p 'test_learning_outcomes.py' -v` | Full 33-criterion outcome/report reconciliation | **PENDING CI** |
| 4 | `python tools/audit-learning-outcome-evidence.py` | Generate the current criterion matrix from canonical outcome/resource/question maps | **PENDING CI** |
| 5 | `python tools/sync-version.py --check` | Verify release markers and app/Service Worker/mock cache keys | **PENDING CI** |
| 6 | Full Python test discovery | Complete discovered Python suite | **PENDING CI** |
| 7 | GitHub Validate | Exact-commit source acceptance | **PASS** |
| 8 | GitHub Pages build/deploy | Exact-commit Pages acceptance, distinct from production approval | **PENDING** |

## Exact-commit acceptance evidence

All v2.95.80 hosted run IDs above refer to exact source/test HEAD `84a6b55b53c5d07a6f127c06234605efc0098edd`. Mapping audit PASS: 1,103/1,103 links, 638 unique stable IDs, 0 Listening reserve links, and 2/2 Part 7 cross-document sources verified. Version sync PASS: 19 markers and all app/Service Worker/mock-engine cache-key groups match v2.95.80.

## Expected post-change inventory

- 1,103 mapping links across 638 unique stable question keys.
- 22/27 TOEIC criteria mapped; five deliberately uninstrumented.
- Foundation 6/6; total outcome pathways 28/33.
- Listening reserve remains excluded; Part 7 second-review and Separate Part 5 independent-review remain active.
