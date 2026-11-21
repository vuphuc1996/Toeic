# Test Report — TOEIC Dictionary v2.95.19

## Release scope

- Baseline: recovered v2.95.18 FullSource.
- Candidate: v2.95.19.
- UI, CSS, layout, navigation and runtime interaction are frozen. `app.js`, `index.html` and `sw.js` contain only synchronized version-marker changes.
- Listening evidence traceability and reviewer handoff tooling changed. No reserve question was promoted to Mock.

## Results

| Check | Result | Notes |
|---|---|---|
| Focused Python regression | **79/79 PASS** | 12 focused suites: Listening expansion 6; question evidence 7; editorial review queue 5; editorial review 6; sentence completion 12; content batch 024 8; content batch 025 7; distractor quality 6; CI coverage 3; project progress 4; package source 3; version sync 12. |
| JavaScript workflow regression | **38/38 PASS** | All `.mjs` test commands listed in `.github/workflows/validate-data.yml` completed successfully. |
| JavaScript syntax | PASS | `sw.js` and every `assets/js/*.js` module passed `node --check` using the workflow's `.mjs` check method. |
| Python compile | PASS | Changed audit/generator/test files compiled; workflow compile list also checked. |
| Vocabulary validator | PASS | 1,141 records; 0 ID additions / 0 missing; 0 errors / 0 warnings against retained legacy baseline. |
| Learning-content validator | PASS | Listening 121 units / 239 questions; Reading 65 / 263; Grammar 50 / 137; Part 5 practice 80; 0 errors / 0 warnings. |
| Repository integrity | PASS | 391 local references/data files; 0 errors; 0 optional warnings. |
| Part 1 photo validation | PASS | 9/9 assets valid; 0 missing-photo warnings. |
| Evidence audit | PASS | 502 indexed TOEIC questions; 137 Listening reserve items remain pending; no approval inferred. |
| Review queue generation | PASS | 137 Listening + 63 Reading Part 7 + 80 Part 5 = 280 item-level decisions. |
| Version synchronization | PASS | All release markers match 2.95.19. |
| Package contract tests | PASS | 3/3; one root, tracked files only, dirty-tree refusal and version validation. |

## Listening evidence closure

- 29 legacy Listening reserve questions that lacked `evidenceText` now have transcript-matching evidence pointers.
- All 137 reserve Listening questions have a matching transcript evidence pointer (checked by the new regression test).
- The Part 1 photo question has a separate internal visual-action note; this is traceability context, not independent approval.
- 16 older Listening units now explicitly state internal-author-check and independent-second-review-pending status.
- All 137 retain `reserve-pending-independent-review`; none was promoted to Mock.

## Remaining limitations and release gates

- `test_validator.py` full-module execution did **not** complete within the execution window. A focused full-suite attempt timed out during the aggregate run. Individual checks including `test_new_defect_not_hidden_by_equal_count` and `test_unknown_topic` passed when run separately; this does not substitute for the full 38-case module result.
- Full aggregate Python discovery was not completed. Do not interpret the 79 focused cases as all Python tests in the repository.
- No remote GitHub Actions result, GitHub Pages deployment, browser acceptance, Windows/iOS/Android device test, or physical TTS/audio quality check is claimed.
- The 280-question review packet is a reviewer handoff only. Independent human sign-off is still outstanding for Listening, Reading Part 7 and separate Part 5. Supplementary Foundation A2 review also remains open.
- No GitHub push or deployment was performed from this workspace.

## Reproduction commands

```bash
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/audit-repository-integrity.py
python tools/validate-part1-photo-assets.py
python tools/audit-question-evidence.py
python tools/build-editorial-review-queue.py
python tools/sync-version.py --check
python -m unittest discover -s tools/tests -p 'test_listening_expansion.py' -v
python -m unittest discover -s tools/tests -p 'test_question_evidence.py' -v
python -m unittest discover -s tools/tests -p 'test_editorial_review_queue.py' -v
```

Generated outputs and per-command notes are indexed in `COMMAND_LOG_INDEX_v2.95.19.md`.
