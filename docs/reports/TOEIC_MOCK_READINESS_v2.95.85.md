# TOEIC Full-Mock Readiness Consolidation — v2.95.85

Read-only readiness audit built strictly from `APPROVED_FOR_MOCK` pools (`editorialStatus` empty or `internal-editorial-reviewed`). Reserve items (`reserve-pending-independent-review`) and Separate Part 5 (`80` practice-only questions) are **never** sampled in Mock.

## 1. Approved Mock Pool vs Reserve Pool by Part

| Sub-pool | `APPROVED_FOR_MOCK` (Q) | `HUMAN_REVIEW_REQUIRED` Reserve (Q) | Full-Mock Quota (200Q) | Disjoint Full-Form Capacity | Primary Bottleneck |
|---|---:|---:|---:|---:|---|
| Listening Part 1 | 8 | 1 | 6 | 1x | Needs >=12Q for 2 disjoint Full forms; even post-review cap is 9Q (hard photo bottleneck). |
| Listening Part 2 | 25 | 36 | 25 | 1x | 1 exact form (0 surplus); 2nd Full form reuses 25/25 until 36 reserve units pass review. |
| Listening Part 3 | 39 | 84 | 39 | 1x | 1 exact form (0 surplus); 2nd Full form reuses 39/39 until 28 reserve units pass review. |
| Listening Part 4 | 30 | 72 | 30 | 1x | 1 exact form (0 surplus); 2nd Full form reuses 30/30 until 24 reserve units pass review. |
| Reading Part 5 | 60 | 0 | 30 | 2x | Supports 2 disjoint Full forms (60Q approved); Separate 80Q P5 remains excluded. |
| Reading Part 6 | 32 | 0 | 16 | 2x | Supports 2 disjoint Full forms (32Q approved in indivisible blocks). |
| Reading Part 7 Single | 58 | 52 | 29 | 2x | Supports 2 disjoint Full forms (58Q approved in indivisible blocks). |
| Reading Part 7 Multiple | 50 | 35 | 25 | 2x | Supports 2 disjoint Full forms (50Q approved in indivisible blocks). |
| **Listening Total** | **102** | **193** | **100** | **1x** (2 surplus P1 Qs) | Reuses minimum **98/100** Qs on 2nd Full form |
| **Reading Total** | **200** | **87** | **100** | **2x** (exact DP block-packed: PASS) | Separate 80Q P5 & 87Q P7 reserve excluded |

## 2. Mode-by-Mode Operational Readiness

| Mode | Questions | Duration | 1st Form Valid | Disjoint Listening Forms | Disjoint Reading Forms | Disjoint Combined Forms | Notes |
|---|---:|---:|:---:|---:|---:|---:|---|
| `full` (Thi TOEIC đầy đủ) | 200 | 120 min | YES | 1 | 2 | 1 | Gated against repeated Listening forms in mock-score-readiness.js |
| `half` (Thi thử rút gọn) | 100 | 60 min | YES | 2 | 3 | 2 | Practice / diagnostic simulation only |
| `quick` (Test nhanh) | 25 | 15 min | YES | 6 | 8 | 6 | Practice / diagnostic simulation only |
| Part Practice (Library + Separate P5 + Grammar) | All eligible/practice | Untimed / timed P5 | YES | — | — | — | 169 Grammar + 80 Separate P5 + full Reading/Listening libraries (Listening reserves excluded from `objectiveProgress`) |

## 3. Exact Listening Bottleneck & Readiness Guardrails

- **Current Full-Mock Listening pool**: **102 questions** (Part 1 = 8, Part 2 = 25, Part 3 = 39, Part 4 = 30).
- **Minimum overlap on 2nd Full Listening form**: **98%** (`98/100` reused: 4 Part 1 + 25 Part 2 + 39 Part 3 + 30 Part 4; only 2 unused Part 1 questions remain).
- **Post-review ceiling if all 193 Listening reserves were approved**: Part 1 = 9/12, Part 2 = 61/50, Part 3 = 123/78, Part 4 = 102/60. Combined disjoint 100Q Listening forms remain **1** because **Listening Part 1 only has 9 total photographs (3 short of the 12 needed for 2 disjoint Full forms)**.
- **Reading independence**: Approved Reading (`200Q`) packs into **2 completely disjoint 100Q Full forms** preserving indivisible Part 6 and Part 7 single/multi-passage blocks (`readingTwoDisjointFullFormsVerified = true`).
- **Zero ETS scaled score claims**: `mock-engine.js` and `mock-score-readiness.js` report raw accuracy percentages only; no `/495` or `/990` ETS conversion exists, and `buildMockScoreReadiness()` suppresses Listening trends until >=2 distinct Listening forms are recorded (with >=90% overlap warnings).
