# Current Version — TOEIC Dictionary v2.95.39
- Current source: **v2.95.39**.
- Release package: `TOEIC_Dictionary_v2.95.39_FullSource.zip`.
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.39.md`.
- Batch 033: added 8 Cambridge-sourced related-term glosses (ability, acceptable, action, accusation, advertise, advise, allow, announce), each with POS, paraphrased definition and direct source URL. Independent editorial review remains pending.
- Batch 028: related-term explanation now filters reference context by synonym/antonym relation type and includes glossary alias POS/English definition where available.
- Batch 027: 16 original-editorial Listening resources / 32 questions (Part 2: 8 items; Part 3: 4 conversations / 12 questions; Part 4: 4 talks / 12 questions).
- Every new question has a transcript evidence pointer and stable choice IDs; each resource includes review notes and batch metadata. All remain pending independent review and fail-closed excluded from Mock.
- Objective-resource mapping: **379/379** canonical links.
- Listening inventory: 145 resources / 295 questions; Mock-eligible 102 / independent-review reserve 193. Part 1 still has 8 eligible + 1 pending, below the 10-item evidence threshold.
- Validation: **49 focused glossary regression tests PASS**, plus explanation-context, practice-fallback and CI-coverage suites PASS; **39/39 JavaScript regression suites PASS**; data and learning-content validators PASS with 0 errors/warnings; repository integrity 409 references / 0 errors / 0 optional warnings; objective-resource audit 379/379; distractor structural audit PASS; version sync PASS.
- Full Python unittest discovery was attempted but timed out; it is not counted as passed. Remote CI, GitHub Pages deployment, browser/device acceptance and independent review remain unverified.
- No UI redesign, vocabulary headword IDs, Glossary, learner progress, IndexedDB schema, or answer-history data changed.


- Packaging: FullSource **569 files**; Update Patch **28 files (10 added + 18 modified, 0 deleted)**; replay exact **569/569**; CRC/root/exclusions/SHA PASS.
