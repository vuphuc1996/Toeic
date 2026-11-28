# Test & Hosted Acceptance Report — TOEIC Dictionary v2.95.80

**Target branch:** `candidate`
**Predecessor baseline:** `5bbdc5e05e396380d17d5a65f108d73aa8ee172a` (v2.95.79)
**Verified candidate HEAD:** `84a6b55b53c5d07a6f127c06234605efc0098edd`
**Validate:** [run 46107947688](https://github.com/vuphuc1996/Toeic/actions/runs/46107947688) — PASS
**Pages:** [run 46107947573](https://github.com/vuphuc1996/Toeic/actions/runs/46107947573) — PASS
**Main baseline:** `256ca21461e78a7685bed773ddd622a64050e33a` (unchanged)

## Release scope

This is a criterion-mapping and audit-hardening release. It adds no learner-facing questions, passages, vocabulary or UI behavior.

- Add 21 defensible mapping links to existing canonical questions.
- Keep 638 unique stable question keys; total mapping rows become 1,103.
- Strengthen Part 7 cross-document validation using internal review status, declared source labels and matching document quotes.
- Preserve the 10-unique-item / 80% local practice threshold and all editorial gates.

## v2.95.80 acceptance status

| Gate | Status | Evidence |
|---|---|---|
| Mapping count and identity reconciliation | **PASS** | Audit confirms 1,103/1,103 links and 638 unique stable question IDs |
| Grammar and Listening mapping regression tests | **PASS** | Mapping test module 4/4; outcome module 5/5 |
| Part 7 cross-document evidence guard | **PASS** | 2/2 mapped resources are internally reviewed with matching quotes from two declared sources; negative tests reject invalid evidence |
| Five deliberately uninstrumented criteria | **PASS** | Audit confirms 5 remain uninstrumented; outcome totals remain 22/27 TOEIC and 28/33 overall |
| Listening reserve exclusion | **PASS** | Audit reports 0 Listening reserve mappings |
| Version marker/cache synchronization | **PASS** | 19 release markers; 17 app, 42 SW and 1 mock-engine cache keys |
| Full Python discovery | **PASS** | 850 tests; `Ran 850 tests in 11.175s; OK` |
| GitHub Validate | **PASS** | 151/151 steps; 0 failures, 0 skipped on the exact verified HEAD |
| GitHub Pages build/deploy | **PASS** | Build 7/7, report status 3/3 and deploy 3/3 on the same exact SHA |

## Exact mapping delta

- Grammar form recognition: 1 → 10.
- Listening Part 3 conversation purpose: 5 → 7.
- Listening Part 3 speaker/action linking: 1 → 10.
- Listening Part 4 talk purpose: 1 → 2.
- Part 7 cross-document remains 2; both items have explicit evidence from two source documents in internally reviewed material.
- Listening Part 1 visual/audio match and detail retention remain 8 each.

## Protected boundaries

No question text, passage, answer, choice, stable question/choice ID, vocabulary record, Mock eligibility or editorial status is changed. No learner IndexedDB schema or local record is migrated. No UI, navigation or Robot Buddy behavior changes. The five unsupported TOEIC criteria remain uninstrumented. Mapping inventory is not learner evidence, mastery, CEFR/ETS certification or official TOEIC readiness.

The weighted measurable curriculum-build index remains **73.73%** because this batch does not increase the count of instrumented criteria.

## Review and release boundaries

The Part 7 cross-document audit passes for 2/2 mapped questions: each requires an `internal-editorial-reviewed` resource, two distinct declared source labels and one matching quote per source. Reading Part 7 second-review and Separate Part 5 independent-review gates remain active. No Listening reserve question is promoted.

The GitHub-managed Pages workflow still emits a Node.js 20 deprecation warning and a `DEP0040` (`punycode`) warning. These did not fail the build or deployment and are not fixed by this batch.

This is a candidate-only source release. The verified source/test HEAD is `84a6b55b53c5d07a6f127c06234605efc0098edd`; it includes two small test-only corrections to stale 1,082 mapping expectations, without changing runtime logic or the 73.73% weighted index. `main` remains unchanged at `256ca21461e78a7685bed773ddd622a64050e33a`. Installed-PWA/offline propagation, physical-device QA and FullSource ZIP verification are separate, unverified gates.
