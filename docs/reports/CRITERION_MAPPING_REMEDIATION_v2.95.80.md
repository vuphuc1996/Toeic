# Criterion Mapping Remediation — TOEIC Dictionary v2.95.80

**Predecessor:** candidate HEAD `5bbdc5e05e396380d17d5a65f108d73aa8ee172a` (v2.95.79).
**Target branch:** `candidate`; `main` remains unchanged at `256ca21461e78a7685bed773ddd622a64050e33a`.

## 1. Verified mapping delta

- Previous inventory: **1,082** criterion/question links across **638** unique stable question keys.
- Added in this batch: **21** links to questions that already exist in the canonical banks.
- Updated inventory: **1,103** links across the same **638** unique stable question keys.
- No new question, passage, resource, question ID, choice ID or answer key was created.

| Criterion | Before | Added | Current | Minimum | Inventory status |
|---|---:|---:|---:|---:|---|
| Grammar form recognition | 1 | +9 | **10** | 10 | Reaches the inventory minimum |
| Listening Part 3 conversation purpose | 5 | +2 | **7** | 10 | Below minimum; remains visible |
| Listening Part 3 speaker/action linking | 1 | +9 | **10** | 10 | Reaches the inventory minimum |
| Listening Part 4 talk purpose | 1 | +1 | **2** | 10 | Below minimum; remains visible |
| Reading Part 7 cross-document link | 2 | +0 | **2** | 10 | Below minimum; review gate retained |
| Listening Part 1 visual/audio match | 8 | +0 | **8** | 10 | Below minimum; no reserve promotion |
| Listening Part 1 detail retention | 8 | +0 | **8** | 10 | Below minimum; no reserve promotion |

## 2. Why some criteria remain below 10

- **Listening Part 1:** only eight existing photograph items are outside the reserve bucket. The ninth item remains `reserve-pending-independent-review`; it is not mapped to increase the count.
- **Listening Part 3 purpose:** two additional questions directly ask which problem prompted the call or was reported. Detail, schedule, location and next-action questions were not relabeled as purpose evidence.
- **Listening Part 4 purpose:** one additional question asks for the central subject of the chief operating officer's talk. Date, location and procedural-detail questions were not promoted to talk-purpose evidence.
- **Reading Part 7 cross-document:** the existing two mapped questions both cite two distinct source documents with matching quotes in resources marked `internal-editorial-reviewed`. The other multi-document resources do not currently supply additional questions that satisfy this exact evidence rule and review status.

## 3. Part 7 evidence guard strengthened

`tools/audit-objective-criterion-map.py` now rejects a Part 7 cross-document mapping unless:
1. The resource is marked `internal-editorial-reviewed`.
2. At least two distinct `sourceLabels` are supplied and each points to a declared document.
3. There is one corresponding quote per source label, and the quote is present in that document's canonical `content`.
4. The mapping's `evidenceBasis` names every cited source label.

The Reading Part 7 second-review gate remains active. This stricter mapping-evidence check does not waive that gate or independently certify a second review.

## 4. Outcome and learner-data boundaries

- TOEIC outcomes with an instrumented evidence path remain **22/27**.
- Foundation remains **6/6**; total instrumented criteria remain **28/33**.
- The same five TOEIC criteria remain deliberately uninstrumented.
- A mapping is content inventory coverage, not a learner attempt, correctness result, mastery, CEFR level, ETS score or official TOEIC readiness.
- No learner IndexedDB schema or record is migrated. No question text, answer, choice, stable identity, vocabulary record, Mock eligibility, reserve status, UI, navigation or Robot Buddy behavior is changed.
- The provisional weighted measurable curriculum-build index remains **73.73%**; this batch deepens mappings within already-instrumented criteria and does not increase the instrumented-criterion count.

## 5. Acceptance boundary

This is a candidate-only source release. GitHub Validate, the mapping tests, full Python discovery and GitHub Pages build/deployment must pass on the exact v2.95.80 candidate commit before acceptance is recorded. `main` remains unchanged.
