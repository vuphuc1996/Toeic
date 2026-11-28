# Current Version — TOEIC Dictionary v2.95.84

- Current source: **v2.95.84** — Mock Pool Count Reconciliation & Listening Purpose Evidence Depth.
- Predecessor: stabilized v2.95.83 (`137160f08cd1ef2b2b505a8af1c9e7ba829b4297` + CI stabilization commit).
- Target branch: `candidate`; `main` remains `256ca21461e78a7685bed773ddd622a64050e33a`.
- Release package: `TOEIC_Dictionary_v2.95.84_FullSource.zip`. (Not generated or verified in this candidate snapshot.)
- Change manifest: `reports/CHANGE_MANIFEST_v2.95.84.md`.
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.84.md`.
- Criterion map: **1,148 links / 648 unique stable question IDs**. TOEIC **25/27**; Foundation **6/6**; total **31/33**. Two remain uninstrumented; `listening-part-3-conversation-purpose` advances **7 → 11** and `listening-part-4-talk-purpose` advances **2 → 7** (below 10-item minimum).
- Mock UI & Engine alignment: `assets/js/app.js` reuses `countMockPool` and `isQuestionMockEligible` from `assets/js/mock-engine.js`; displayed Mock pool stays at **102** Listening (**30** Part 4) and **200** Reading, excluding the 10 practice-only Part 4 questions (`mockEligible: false`).
- Part 1 photo visual review and Part 7 independent second-review handoff remain queued without promotion.
- Weighted measurable curriculum-build index: **76.00%** (provisional; not learner mastery or TOEIC score readiness).
- GitHub Validate, Pages deployment, FullSource ZIP, installed-PWA/offline propagation and physical-device QA: **PENDING / UNVERIFIED**.
- Candidate only; no merge to main or Production Deployment Accepted decision.
