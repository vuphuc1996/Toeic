# Test & Hosted Acceptance Report — TOEIC Dictionary v2.95.80

**Target branch:** `candidate`
**Predecessor baseline:** `5bbdc5e05e396380d17d5a65f108d73aa8ee172a` (v2.95.79)
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
| Mapping count and identity reconciliation | **PENDING CI** | Expected 1,103 links / 638 unique stable keys |
| Grammar and Listening mapping regression tests | **PENDING CI** | New criterion count assertions |
| Part 7 cross-document evidence guard | **PENDING CI** | Internal review, two source labels, one matching quote per source |
| Five deliberately uninstrumented criteria | **PENDING CI** | Must remain without question mappings |
| Listening reserve exclusion | **PENDING CI** | No reserve item added |
| Version marker/cache synchronization | **PENDING CI** | `tools/sync-version.py --check` |
| Full Python discovery | **PENDING CI** | Exact candidate commit |
| GitHub Validate | **PENDING** | Exact candidate commit |
| GitHub Pages build/deploy | **PENDING** | Exact candidate commit |

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

Part 7 cross-document mappings require an `internal-editorial-reviewed` resource, two distinct declared source labels and one matching quote per source. Reading Part 7 second-review and Separate Part 5 independent-review gates remain active. No Listening reserve question is promoted.

This is a candidate-only source release. `main` remains unchanged at `256ca21461e78a7685bed773ddd622a64050e33a`. Installed-PWA/offline propagation, physical-device QA and FullSource ZIP verification are separate, unverified gates.
