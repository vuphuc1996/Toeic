# Test & Hosted Acceptance Report — TOEIC Dictionary v2.95.79

**Target branch:** `candidate`
**Predecessor baseline:** `9a174778bcdfea7adca98f0abb1b17d3a050388e` (v2.95.78)
**Main baseline:** `256ca21461e78a7685bed773ddd622a64050e33a` (unchanged)

## Release scope

This is a source-maintenance release for release-version integrity. It does not add learner-facing features or change curriculum content.

- Register the top-level `package.json` version as a guarded marker in `tools/sync-version.py`.
- Require exactly one package version marker; missing or duplicate matches stop before writes.
- Add regression coverage for mismatch reporting, dry-run immutability, apply synchronization, and missing/duplicate marker safety.
- Synchronize the release shell and cache keys to v2.95.79.

## v2.95.79 acceptance status

| Gate | Status | Evidence |
|---|---|---|
| Package-version mismatch regression | **PENDING CI** | Added to `test_sync_version.py` |
| Missing/duplicate marker safety regression | **PENDING CI** | Added to `test_sync_version.py` |
| Version sync check | **PENDING CI** | `python tools/sync-version.py --check` |
| Full Python discovery | **PENDING CI** | Validate workflow on the exact new candidate commit |
| Vocabulary / learning-content validation | **PENDING CI** | Validate workflow on the exact new candidate commit |
| GitHub Pages build/deploy | **PENDING** | Must be inspected separately on the exact new commit |
| Installed-PWA/offline propagation | **UNVERIFIED** | Requires installed-device verification |
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

The previously observed GitHub-managed Pages dynamic workflow emitted Node.js 20 deprecation and dependency warnings while completing successfully. This batch does not modify hosting settings or replace the managed Pages workflow, so those warnings are **not claimed fixed**. A successful Pages run, when observed for v2.95.79, is recorded separately from production approval.

## Production boundary

This is a candidate-only source release. `main` remains unchanged at `256ca21461e78a7685bed773ddd622a64050e33a`. No merge, main deployment or Production Deployment Accepted decision is included.
