# Current Version — TOEIC Dictionary v2.95.82

- Current source: **v2.95.82** — Part 2 Lexical Distractor Evidence Instrumentation.
- Sole predecessor baseline: candidate HEAD `4d1eead800e3378cf91b5b83ddb14bc3c8fb8737` (v2.95.81).
- Target branch: `candidate`; `main` remains at `256ca21461e78a7685bed773ddd622a64050e33a`.
- Release package: `TOEIC_Dictionary_v2.95.82_FullSource.zip`.
- Package status: **NOT GENERATED OR VERIFIED**; the filename is a release target, not proof of an archive.
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.82.md`.
- Change manifest: `reports/CHANGE_MANIFEST_v2.95.82.md`.
- Canonical version source: `data/manifest.json`; top-level `package.json` is an exact-one checked marker.
- Part 2 distractor-resistance: **16** exact stable question mappings with prompt, wrong-choice, whole-word cue and response-mismatch evidence. All selected resources are non-reserve; no answer key or choice is changed.
- Criterion map: **1,119** mapping links / **638** unique stable question IDs. TOEIC instrumentation **23/27**; Foundation **6/6**; total **29/33**. Four TOEIC criteria remain deliberately uninstrumented.
- Part 2 audit requires exact prompt-to-segment match, exact incorrect choice at a non-answer index, whole lexical cue in prompt and distractor, and non-empty mismatch rationale.
- Existing multi-criterion questionKey indexing and the learner-local objectiveProgress ledger are reused; no IndexedDB schema migration.
- Version/cache inventory: 19 single-instance markers; app **17**, Service Worker **42**, mock-engine **1** release-keyed references, all synchronized to v2.95.82.
- GitHub Validate, focused evidence tests, canonical mapping audit, version synchronization, full Python suite and Pages build/deploy for this exact candidate commit: **PENDING**.
- Candidate only; no merge to `main` or Production Deployment Accepted decision.
- FullSource ZIP, installed-PWA/offline propagation and physical-device QA: **UNVERIFIED**.
