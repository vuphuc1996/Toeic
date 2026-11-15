# Current Version — v2.61.0

- **Status:** local source candidate — deployment hold until the strict Part 1 photo validator passes (8 original licensed JPG binaries are missing from the inherited source archive); remote CI/Pages and physical-device QA are not verified.
- **Base:** v2.60.0.
- **Test correction:** `test_learning_detail_scope` now isolates a single top-level function and is resilient to helper functions inserted later in the file. The actual `openGrammarLesson()` scope remains free of out-of-scope `item.` references.
- **Editorial fingerprint trace:** all eight reviewed Listening Part 1 unit hashes were refreshed only after the old hashes matched when removing `photoSourceType: "licensed-stock"`; all eight question hashes remain unchanged. The registry contains a `fingerprintRefreshLog` with old/new digests and explicit conditions.
- **Recall queue UI:** reuses the app's standard panel/header, learning-card, badge/count and button patterns. Human-readable content omits the internal stable question ID while preserving it in the action data attribute.
- **Learning path UI:** reuses the same page heading, panel, learning-card grid, category/level labels and standard actions. Typography has readable minimums and fluid sizing; layout adapts to available CSS width rather than device-inch classes.
- **Data/progress preservation:** no vocabulary data, stable learning IDs, localStorage keys, IndexedDB stores/schema, or learner progress were reset or migrated.
- **Local regression results:** 130 selected Python tests pass (not a full-suite claim); 17/17 JavaScript scripts pass; vocabulary validation 992/992 with zero errors/warnings; learning-content validation zero errors with eight known missing-JPG warnings; objective resources 281/281 and outcome criteria 30/30 pass. Local version synchronization passes.
- **Verification boundary:** Chromium localhost preview is blocked in this environment. The strict Part 1 image validator currently fails 8 missing JPG files; exact Pexels restoration links are recorded in `../reports/PART1_PHOTO_ASSET_RECOVERY_v2.61.0.md`. Remote CI/Pages and physical-device QA are not verified.
- **Verification:** see `../reports/TEST_REPORT_TOEIC_Dictionary_v2.61.0.md` and `../reports/PROJECT_PROGRESS_BASELINE_v2.61.0.md`.
