# Release Acceptance & Evidence — TOEIC Dictionary v2.95.85

**Snapshot date:** 2026-11-28  
**Branch:** `candidate`  
**Verified source baseline:** `7b8d80f1eef1523b5c2f31f0361a51c90011da7e`  
**Production branch:** `main` was not changed by this candidate release.

## 1. Source-level verification

The project owner confirmed that the exact v2.95.85 source baseline above completed:

- **865/865 unit tests: PASS**
- Compilation/build checks: **PASS**
- JavaScript syntax/lint checks: **PASS**

This report records that supplied acceptance result. The raw local test logs and exact command output were not included with the repository snapshot available for this documentation repair, so those results are not represented as an independently replayed run in this report.

GitHub Actions status checks and GitHub Pages deployment for the exact baseline SHA were not independently established by this report. Hosted CI, Pages deployment, installed-PWA/offline propagation, FullSource ZIP generation, and physical-device testing remain separate evidence gates.

## 2. Release inventory

- Canonical vocabulary: **1,281 headwords**, including **60** additions in Batch 029; 32 topic groups.
- Learning outcomes: **11 objective groups / 33 criteria**.
- Criterion mapping: **1,163 links / 651 unique stable question IDs**.
- Instrumentation: **26/27 TOEIC criteria**, **6/6 Foundation criteria**, **32/33 overall**. The remaining TOEIC criterion is `listening-part-1-paraphrase-recognition`; it remains visible but uninstrumented because the current defensible Part 1 pool is below the 10-unique-item threshold.
- Listening: **145 resources / 308 questions**; **102** Mock-eligible, **193** reserve, and **13** Part 4 practice-only questions (`mockEligible: false`).
- Part 1: **9** resources, **8** currently eligible and **1** reserve-pending independent review.
- Reading: **200** Mock-eligible; **87** Part 7 reserve items remain excluded. Separate Part 5 has **80** review-only items.
- Grammar: **58** lessons. Reading resources: **73**.
- Provisional weighted curriculum-build index: **77.16%**. This is a content/evidence build indicator, not learner mastery, an official TOEIC score, or certification of exam readiness.

## 3. Protected data and release boundaries

The v2.95.85 candidate preserves canonical vocabulary IDs/headwords, assessment question and choice IDs, answer keys, learner IndexedDB v1 schema/data, Mock eligibility boundaries, and the existing UI/layout and Robot Buddy boundaries. No backend or Cloudflare dependency is introduced; the intended hosting architecture remains GitHub Pages.

Listening reserve, Reading Part 7 reserve, and Separate Part 5 review-only content are not promoted by this report. The outstanding human-review queue remains a review gate, not approved content.

## 4. Acceptance interpretation

**Source-level acceptance:** owner-confirmed for the exact baseline SHA listed above.  
**Production deployment acceptance:** not granted.  
**Merge to `main`:** not authorized by this report.

Any documentation-only commits made after the baseline SHA do not change the code/test result recorded above; they still require the repository's normal candidate validation workflow before being treated as a newly verified HEAD.
