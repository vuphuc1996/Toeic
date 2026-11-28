# Test & Hosted Acceptance Report — TOEIC Dictionary v2.95.79

**Target branch:** `candidate`
**Predecessor baseline:** `9a174778bcdfea7adca98f0abb1b17d3a050388e` (v2.95.78)
**Main baseline:** `256ca21461e78a7685bed773ddd622a64050e33a` (unchanged)
**Verified source commit:** `76ca52457929493a2a587f7673367bc29eeace49`
**Validate run:** [46105814708](https://github.com/vuphuc1996/Toeic/actions/runs/46105814708) — PASS
**Pages run:** [46105814298](https://github.com/vuphuc1996/Toeic/actions/runs/46105814298) — PASS

## Release scope

This is a source-maintenance release for release-version integrity. It does not add learner-facing features or change curriculum content.

- Register the top-level `package.json` version as a guarded marker in `tools/sync-version.py`.
- Require exactly one package version marker; missing or duplicate matches stop before writes.
- Add regression coverage for mismatch reporting, dry-run immutability, apply synchronization, and missing/duplicate marker safety.
- Synchronize the release shell and cache keys to v2.95.79.

## v2.95.79 acceptance status

| Gate | Status | Evidence |
|---|---|---|
| Package-version mismatch regression | **PASS** | `test_sync_version.py` — 16/16 tests passed, including package drift/apply case |
| Missing/duplicate marker safety regression | **PASS** | Missing and duplicate package markers stop before writes |
| Version sync check | **PASS** | 19 release markers; 17 app, 42 SW, 1 mock-engine cache keys synchronized |
| Full Python discovery | **PASS** | 848 tests; `Ran 848 tests in 10.732s; OK` |
| Vocabulary / learning-content validation | **PASS** | Vocabulary release integrity: 26 files, 1,221 records |
| GitHub Validate | **PASS** | 151/151 steps successful; 0 failed, 0 skipped on the exact verified source commit |
| GitHub Pages build/deploy | **PASS** | Build, upload, deploy and status-report jobs all succeeded on the same exact SHA |\n| Installed-PWA/offline propagation | **UNVERIFIED** | Requires installed-device verification |
| Physical-device layout QA | **UNVERIFIED** | iPhone/iPad portrait & landscape and laptop widths |
| FullSource ZIP generation / CRC verification | **NOT DONE** | No ZIP artifact is claimed |

## Predecessor evidence — not v2.95.79 evidence

The exact predecessor candidate HEAD `9a174778bcdfea7adca98f0abb1b17d3a050388e` (v2.95.78) passed:
- GitHub Validate: [run 46100602552](https://github.com/vuphuc1996/Toeic/actions/runs/46100602552).
- GitHub Pages build and deployment: [run 46100602152](https://github.com/vuphuc1996/Toeic/actions/runs/46100602152).

These runs validate the predecessor only. They must not be reported as passing evidence for v2.95.79.

## Protected boundaries

No vocabulary headword/ID/sense/relationship, Listening/Reading/Grammar content, stable question/choice identity, answer key, Mock eligibility, editorial reserve, learner IndexedDB v1 schema or learner data is changed. UI/UX layout, navigation, Robot Buddy behavior and GitHub Pages-only architecture are unchanged. No backend or Cloudflare service is introduced.

## Known Pages warning boundary

The successful v2.95.79 Pages run still emitted the GitHub-managed Node.js 20 deprecation warning plus dependency warnings `DEP0040` (`punycode`) and `DEP0169` (`url.parse()`). They did not fail the deploy. This batch does not alter hosting settings or the managed Pages workflow; those warnings are **not fixed or claimed fixed**.

## Production boundary

This is a candidate-only source release. The acceptance evidence above applies to source commit `76ca52457929493a2a587f7673367bc29eeace49`; the evidence-ledger follow-up changes documentation only and does not change app/runtime/data files. `main` remains unchanged at `256ca21461e78a7685bed773ddd622a64050e33a`. No merge, main deployment or Production Deployment Accepted decision is included.
