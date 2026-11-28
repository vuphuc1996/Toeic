# Command Log Index — TOEIC Dictionary v2.95.84

**Branch:** `candidate`
**Predecessor:** stabilized `v2.95.83` (`137160f08cd1ef2b2b505a8af1c9e7ba829b4297` + CI reconciliation commit)
**Scope:** Mock UI pool-count reconciliation (`mockEligible: false` exclusion), Listening Part 3/Part 4 purpose criterion depth, and full local validation.

| Order | Command / workflow | Purpose | Status |
|---:|---|---|---|
| 1 | `python3 tools/sync-version.py --check` | Verify canonical version, package, HTML, app, SW, and mock-engine release markers | **PASS** |
| 2 | `python3 tools/validate-data.py` | Verify canonical vocabulary, IDs, and ratchet baseline | **PASS** |
| 3 | `python3 tools/validate-learning-content.py` | Verify Listening/Reading/Grammar schema and Part 4 practice-only allowlist | **PASS** |
| 4 | `python3 tools/audit-objective-criterion-map.py` | Verify 1,148 links / 648 stable IDs / 25 TOEIC criteria / 0 Listening reserve | **PASS** |
| 5 | `python3 tools/audit-listening-readiness.py` | Verify Mock-eligible Listening 102, reserve 193, practice-only 10 | **PASS** |
| 6 | `python3 tools/audit-mock-readiness.py` | Verify Full-Mock readiness & 30 Part 4 / 102 Listening pool | **PASS** |
| 7 | `python3 tools/audit-distractors.py` | Verify distractor integrity & 30-question Part 4 Mock balance | **PASS** |
| 8 | `python3 tools/audit-seven-part-content.py` | Verify 841 questions, 302 Mock-approved, 360 review-required, 0 structural errors | **PASS** |
| 9 | `python3 tools/audit-repository-integrity.py && python3 tools/audit-design-tokens.py` | Verify repository integrity & CSS design-token ratchet | **PASS** |
| 10 | `node --check assets/js/*.js && node tools/tests/*.mjs` | Verify JS syntax and all 46 Node regression suites | **PASS** |
| 11 | `python3 -m unittest discover -s tools/tests -v` | Full Python discovery on v2.95.84 source | **PASS** |
| 12 | GitHub Validate + GitHub Pages + FullSource ZIP + physical-device QA | Hosted CI, Pages deployment, ZIP packaging, and device QA | **PENDING / UNVERIFIED** |
