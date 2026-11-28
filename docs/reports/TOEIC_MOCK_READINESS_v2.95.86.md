# TOEIC Full-Mock Readiness Consolidation — v2.95.86

Read-only readiness audit built strictly from `APPROVED_FOR_MOCK` pools (`editorialStatus` empty or `internal-editorial-reviewed`). Reserve items (`reserve-pending-independent-review`) and Separate Part 5 (**80** practice-only questions) are **never** sampled in Mock.

## 1. Approved Mock Pool vs Reserve Pool by Part

| Sub-pool | `APPROVED_FOR_MOCK` (Q) | `HUMAN_REVIEW_REQUIRED` Reserve (Q) | Full-Mock Quota (200Q) | Current Disjoint Full-Form Capacity | Primary Bottleneck |
|---|---:|---:|---:|---:|---|
| Listening Part 1 | 8 | 4 | 6 | 1x | Current pool supports one form; all four reserve items need independent review. If all are approved, Part 1 reaches 12 questions for two disjoint quotas. |
| Listening Part 2 | 25 | 36 | 25 | 1x | 1 exact form; additional questions remain under independent review. |
| Listening Part 3 | 39 | 84 | 39 | 1x | 1 exact form; additional passage blocks remain under independent review. |
| Listening Part 4 | 30 | 72 | 30 | 1x | 1 exact form; additional talk blocks remain under independent review. |
| Reading Part 5 | 60 | 0 | 30 | 2x | Supports two disjoint Full forms; Separate 80Q P5 remains excluded. |
| Reading Part 6 | 32 | 0 | 16 | 2x | Supports two disjoint Full forms in indivisible passage blocks. |
| Reading Part 7 Single | 58 | 52 | 29 | 2x | Supports two disjoint Full forms in indivisible passage blocks. |
| Reading Part 7 Multiple | 50 | 35 | 25 | 2x | Supports two disjoint Full forms in indivisible passage blocks. |
| **Listening Total** | **102** | **196** | **100** | **1x** | Current second Full Listening form still reuses at least **98/100** questions. |
| **Reading Total** | **200** | **87** | **100** | **2x** | Separate 80Q P5 and 87Q Part 7 reserve remain excluded. |

## 2. Mode-by-Mode Operational Readiness

| Mode | Questions | Duration | 1st Form Valid | Disjoint Listening Forms | Disjoint Reading Forms | Disjoint Combined Forms | Notes |
|---|---:|---:|:---:|---:|---:|---:|---|
| `full` | 200 | 120 min | YES | 1 | 2 | 1 | Current approved pool only |
| `half` | 100 | 60 min | YES | 2 | 3 | 2 | Practice / diagnostic simulation |
| `quick` | 25 | 15 min | YES | 6 | 8 | 6 | Practice / diagnostic simulation |

## 3. Listening Bottleneck and Review Gates

- **Current Full-Mock Listening pool:** **102 questions** (Part 1 = 8, Part 2 = 25, Part 3 = 39, Part 4 = 30).
- **Part 1 reserve change:** 9 → 12 total photo questions; current eligible stays at 8 and pending reserve becomes 4. The three Batch 018 additions have question-level `mockEligible: false`.
- **Current second Full Listening form:** minimum overlap remains **98/100**; Part 1 contributes only two approved surplus questions to a second form.
- **Post-review arithmetic ceiling:** if all **196** pending Listening questions were independently approved, partwise inventory would be Part 1 = **12/12**, Part 2 = **61/50**, Part 3 = **123/78**, and Part 4 = **102/60**. This reaches the two-form quota by counts only; it does not approve any reserve or replace a future exact block-packing and editorial audit.
- **Learning outcomes:** Part 1 visual/audio and delayed-retention mappings remain at **8** each. `listening-part-1-paraphrase-recognition` remains uninstrumented. Batch 018 is not added to the criterion map.
- **Reading independence:** Approved Reading (**200Q**) still packs into two completely disjoint 100Q Full forms while preserving indivisible Part 6 and Part 7 passage blocks.
- **No ETS scaled-score claims:** Mock readiness remains based on approved source inventory and raw practice accuracy; it is not an official ETS score estimate.

## 4. Protected Eligibility

Listening reserve **196**, Reading Part 7 reserve **87**, Separate Part 5 review-only **80**, and Part 4 practice-only **13** remain excluded from Mock. Only a documented independent review can change a resource-level review status; adding content or evidence pointers does not approve it.
