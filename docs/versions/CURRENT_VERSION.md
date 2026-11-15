# Current Version — v2.62.0

- **Status:** local source candidate — deployment hold until the strict Part 1 photo validator passes (8 original licensed JPG binaries are missing from the inherited source archive); remote CI/Pages and physical-device QA are not verified.
- **Base:** v2.61.0.
- **Typography:** application-wide scale for ordinary copy, cards, metadata, forms, objective tracker, practice-mode choices, mock-test setup/results/review and mobile navigation. Ordinary reading content uses a 13.5px floor; controls use at least 14px; supporting metadata uses a 12px floor.
- **Foundation layout:** intro explicitly uses one column; card and option grids reflow by available viewport width.
- **Foundation Listening:** 10 scripts, one per existing Pre-A1/A1 lesson, and 20 stable comprehension questions. Uses device/browser Speech Synthesis; transcript is opt-in. This is synthesized practice, not ETS audio or official CEFR evidence.
- **Progress:** listening attempts use a separate localStorage key `toeic:foundation-listening-progress:v1`; existing Foundation recognition/application/reading keys, previous lesson IDs, IndexedDB schema and learner history remain unchanged.
- **Local regression:** 18/18 JavaScript scripts, focused Python tests listed in the v2.62.0 test report, JS syntax checks, vocabulary/data checks and version synchronization. Full Python discovery and actual browser/physical-device QA are not claimed.
- **Pre-deployment blocker:** strict `python tools/validate-part1-photo-assets.py` still reports 8 missing original JPG binaries. SVG fallbacks remain; restore the correct licensed assets before deployment and keep the CI validator strict.
- **Verification:** see `../reports/TEST_REPORT_TOEIC_Dictionary_v2.62.0.md` and `../reports/PROJECT_PROGRESS_BASELINE_v2.62.0.md`.
