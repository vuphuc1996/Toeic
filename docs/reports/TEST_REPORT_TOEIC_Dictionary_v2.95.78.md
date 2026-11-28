# Test & Hosted Acceptance Report — TOEIC Dictionary v2.95.78

**Verified candidate HEAD:** `0187b446123fca1a8708b496e971e18b19a46c57`
**Target branch:** `candidate`
**Main branch:** unchanged at `256ca21461e78a7685bed773ddd622a64050e33a`.

## Hosted verification

| Gate | Result | Evidence |
|---|---|---|
| GitHub Validate | **PASS** | [Run 46100106836](https://github.com/vuphuc1996/Toeic/actions/runs/46100106836) on the exact SHA above |
| GitHub Pages build and deploy | **PASS** | [Run 46100106757](https://github.com/vuphuc1996/Toeic/actions/runs/46100106757) on the same exact SHA |
| Validate workflow | **151 successful steps / 0 failed / 0 skipped** | Validate job completed successfully |
| Full Python test discovery | **846 tests PASS** | Final discovery output: `Ran 846 tests in 10.776s`; `OK` |
| Stable question-to-criterion map | **PASS** | 1,082 links verified; 638 unique stable question IDs; zero Listening reserve mappings |
| Criterion-level runtime tests | **PASS** | Accuracy, timed accuracy, optional self-report rubric, delayed recall, read-only summary and editorial review gates |
| CSS design-token ratchet | **PASS** | New criterion CSS uses canonical design-system tokens |
| Version synchronization | **PASS** | app.js, mock-engine.js, index.html, sw.js, docs and manifest at v2.95.78 |

## Source change under test

- Added `data/learning-path/objective-criterion-map.json`: 1,082 stable question-to-criterion links across 638 unique IDs.
- **22/27 TOEIC criteria** have explicit item-level evidence paths; **five remain uninstrumented** until suitable item-level evidence or rubric design exists.
- Six Foundation criteria retain their separate, existing evidence paths; **28/33 total criteria** have a local evidence-collection path.
- Criterion accuracy, timed accuracy, optional self-report explanation rubrics, delayed recall and exact source-question reopening use the existing `objectiveProgress` ledger.
- Grammar and Reading Part 5 explanation rubrics are learner self-reports, not automatic or independent grading.
- Separate Part 5 uses a 30-second internal practice target only; it is not an ETS timing standard or score conversion.

## Protected boundaries

- 1,221 vocabulary records and the 831-item assessment/support inventory are retained.
- Existing question/choice IDs, answer keys, Mock eligibility and editorial reserve gates remain unchanged.
- Listening reserve remains excluded from the criterion map.
- Reading Part 7 second-review and Separate Part 5 independent-review gates remain active.
- Existing IndexedDB v1 schema and learner-local data are preserved; no data reset or schema migration is introduced.
- UI layout, navigation, Robot Buddy access boundary and GitHub Pages-only architecture are retained.

## Acceptance boundary

**Source Release Accepted; Candidate CI Verified; Pages Deployment Verified.**

Installed-PWA cache/offline propagation and physical-device QA (iPhone/iPad portrait and landscape, laptop widths) remain **UNVERIFIED**. The v2.95.78 FullSource ZIP was not generated or CRC/byte-verified in this candidate. Production deployment to `main` is not approved; `main` remains unchanged.
