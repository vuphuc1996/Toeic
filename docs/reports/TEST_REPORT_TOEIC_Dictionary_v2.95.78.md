# Candidate Test Report — TOEIC Dictionary v2.95.78

**Status: PRE-CI SOURCE CANDIDATE — hosted verification pending.**

This report documents the intended verification scope for the v2.95.78 source change. It does not claim that local tests, GitHub Actions, Pages deployment, installed-PWA behavior or physical-device tests have already passed.

## Source change under test

- Candidate predecessor: `c1f9702579633aeb6cd372b29e17b143cb2868a1` (v2.95.77).
- Release target: `v2.95.78`.
- Main branch is outside scope and remains unchanged.
- Added stable question-to-criterion map: 1,082 links / 638 unique IDs / 22 of 27 TOEIC criteria.
- Added criterion ledger functions, optional self-report explanation rubrics, a criterion progress dashboard, and criterion-level due-recall routing.
- Existing `objectiveProgress` record, IndexedDB v1 schema, content banks, question/choice IDs, answer keys and Mock gates are protected.

## Verification gates

| Gate | Evidence expected | Status in this source report |
|---|---|---|
| Source integrity | Git tree diff and preserved canonical banks / IDs | Pending candidate commit review |
| Data mapping audit | 1,082 mapped links resolve exactly; zero Listening reserve mappings | Automated audit added; not yet run here |
| Learning outcome tests | 33 criteria, 22/27 TOEIC mapped, five intentionally uninstrumented | Regression tests added; not yet run here |
| Criterion runtime | Accuracy, timed accuracy, delayed recall, rubric, read-only audit | Node regression added; not yet run here |
| Python test suite | Full discovered test inventory, counts and skips | Pending GitHub Actions |
| Version / Service Worker | Manifest, app, HTML, package, cache keys and both precache lists at v2.95.78 | Source changes staged in this candidate |
| GitHub Validate | Must pass on the exact candidate commit | Pending |
| GitHub Pages | Build and deployment must pass on the same exact candidate commit | Pending |
| Installed PWA / offline | Cache update and offline reload on installed PWA | Unverified |
| Physical-device QA | iPhone/iPad portrait and landscape, common laptop widths | Unverified |
| Production on main | Separate approval and verification required | Not approved; main unchanged |

## Acceptance boundary

A passing mapping audit does not constitute learner mastery or editorial approval. A passing source test does not prove hosted deployment, installed-PWA cache propagation or physical-device behavior. Production acceptance on `main` is explicitly excluded from this candidate.
