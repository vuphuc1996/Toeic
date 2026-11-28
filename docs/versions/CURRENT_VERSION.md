# Current Version — TOEIC Dictionary v2.95.85

- Current source baseline: **v2.95.85**, candidate source HEAD `7b8d80f1eef1523b5c2f31f0361a51c90011da7e` — Vocabulary Batch 029, Part 4/Part 7 Criterion Instrumentation & Revision Priority Summary.
- Documentation reconciliation: release-acceptance evidence was added on the candidate branch after the source baseline; it does not change the recorded v2.95.85 application source SHA.
- Predecessor: `v2.95.84` (`19171e45f98ba55b0098b2ed3691e2672a59c5c0` on `candidate`).
- Target branch: `candidate`; `main` baseline remains `256ca21461e78a7685bed773ddd622a64050e33a`.
- Owner-confirmed source validation: **865/865 unit tests PASS**, build/compilation PASS and syntax/lint PASS on the exact source baseline above. This is owner-supplied evidence recorded in `reports/RELEASE_ACCEPTANCE_v2.95.85.md`; raw logs were not attached to the documentation repair and these results were not independently replayed here.
- Learning outcome evidence: `reports/TOEIC_LEARNING_OUTCOME_EVIDENCE_v2.95.85.md`.
- Major release quality audit: `reports/MAJOR_RELEASE_QUALITY_AUDIT_v2.95.85.md`.
- Independent-review handoff: `reports/OUTSTANDING_REVIEW_HANDOFF_v2.95.83.md`.
- Vocabulary inventory: **1,281** canonical headwords (**1,221 → 1,281** via Batch 029, +60 original workplace items, `1221` repair profile added and all historical profiles updated; no fabricated IPA).
- Criterion map: **1,163 links / 651 unique stable question IDs**. TOEIC **26/27**; Foundation **6/6**; total **32/33**. `listening-part-4-talk-purpose` advances **7 → 10** (`mockEligible: false` Part 4 Q5 items); `reading-part-7-paraphrase-inference` advances **0 → 12** verified non-reserve items; only `listening-part-1-paraphrase-recognition` remains uninstrumented.
- Runtime weakness summary: `summarizeCriterionWeaknesses` is exported from `assets/js/learning-outcome-progress.js` and rendered as a concise read-only priority indicator in `assets/js/app.js`.
- Mock pool & reserve boundaries preserved: **102** Listening approved (**30** Part 4), **200** Reading approved, **193** Listening reserve, **87** Part 7 reserve, **80** Separate Part 5 review-only, **13** Part 4 practice-only (`mockEligible: false`).
- Part 1: **9** items/resources exist, **8** approved for mapping/eligible use and **1** reserve-pending independent review. The paraphrase criterion remains uninstrumented; do not reuse generic visual-match mappings to claim paraphrase coverage.
- Weighted measurable curriculum-build index: **77.16%** (provisional; not learner mastery or TOEIC score readiness).
- GitHub Actions status, Pages deployment for the v2.95.85 exact source SHA, FullSource ZIP, installed-PWA/offline propagation and physical-device QA: **PENDING / UNVERIFIED** unless separate exact-SHA evidence is attached.
- Candidate only; no merge to `main` and no Production Deployment Accepted decision.
