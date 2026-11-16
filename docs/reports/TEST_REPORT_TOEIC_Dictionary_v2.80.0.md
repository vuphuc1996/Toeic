# Test Report — TOEIC Dictionary v2.80.0

- **Date:** 2026-11-16
- **Release:** v2.80.0
- **Base:** v2.79.0
- **Scope:** shared Learning Assistant, canonical vocabulary prefix completion, optional Google AI context handoff, mock-exam icon refresh, product documentation and PWA shell.
- **Execution:** local source and independently extracted release packages. Remote GitHub Actions, public GitHub Pages and physical-device behavior are not claimed.

## 1. Regression tests

### JavaScript

**25/25 JavaScript regression suites passed.** Every `tools/tests/*.mjs` script present in the source was executed after the final assistant UI and icon changes:

1. `alphabet-sound-progress.mjs`
2. `assessment-deferred-workflow.mjs`
3. `explanation-rubric-self-report.mjs`
4. `flashcard-image-policy.mjs`
5. `foundation-a2-production.mjs`
6. `foundation-application-evidence.mjs`
7. `foundation-evidence.mjs`
8. `foundation-listening-evidence.mjs`
9. `foundation-outcome-evidence.mjs`
10. `foundation-production-revision.mjs`
11. `foundation-reading-evidence.mjs`
12. `learning-assistant.mjs`
13. `learning-focus-workspace.mjs`
14. `learning-outcome-progress.mjs`
15. `listening-tts-regression.mjs`
16. `mock-exam-engine.mjs`
17. `mock-guided-flow.mjs`
18. `mock-ui-integrity.mjs`
19. `objective-recall-timing.mjs`
20. `part5-timing-integration.mjs`
21. `practice-progress.mjs`
22. `recall-queue.mjs`
23. `runtime-render-smoke.mjs`
24. `sentence-completion.mjs`
25. `vocabulary-release-integrity.mjs`

The assistant suite checks real-data prefix lookup, prefix normalization, hidden-letter masking, exact completion validation, no fabricated `house`/`horse`/`home`/`hold` entries, exact-word navigation, guide actions, contextual prompt handling, long-prompt copy fallback, mobile layout and Service Worker cache wiring.

### Python

**151/151 tests passed across 21 fully executed modules.** The selection is explicit; it is not represented as every Python test file in the repository having been executed.

| Module | Passed |
|---|---:|
| `test_foundation_production_revision.py` | 6 |
| `test_foundation_a2_production.py` | 7 |
| `test_ci_coverage.py` | 2 |
| `test_sync_version.py` | 12 |
| `test_design_profile.py` | 6 |
| `test_learning_content.py` | 34 |
| `test_foundation_pathway.py` | 10 |
| `test_foundation_reading.py` | 9 |
| `test_foundation_listening.py` | 13 |
| `test_foundation_outcome_evidence.py` | 2 |
| `test_learning_outcomes.py` | 3 |
| `test_learning_outcome_progress.py` | 3 |
| `test_project_progress.py` | 4 |
| `test_objective_resource_map.py` | 2 |
| `test_pwa_readiness.py` | 3 |
| `test_responsive_layout.py` | 5 |
| `test_learning_surface_consistency.py` | 5 |
| `test_part1_photo_assets.py` | 6 |
| `test_sentence_completion.py` | 12 |
| `test_vocabulary_batch_012.py` | 4 |
| `test_release_rotation.py` | 3 |
| **Total** | **151** |

A broader single-process test invocation previously exceeded the execution time limit. It is not counted. The selected 21 modules above were each completed and returned success.

## 2. Static checks and validators

- Python syntax compilation: **66/66** Python files under `tools/` compiled successfully.
- JavaScript syntax: **13/13** `assets/js/*.js` modules plus `sw.js` passed Node syntax checks.
- HTML: `index.html` parsed successfully with Python `HTMLParser`.
- CSS: `assets/css/app.css` (1,638 top-level nodes) and `assets/css/design-system.css` (270 nodes), **1,908 combined**, no `tinycss2` parse errors.
- Version sync: **PASS**, every marker reads v2.80.0.
- Design profile: **PASS**, 54 tokens and 387 legacy font-floor selector groups synchronized.
- CMUdict: **PASS**, 333 source-linked IPA records.
- Vocabulary validation: **1,137 records, 0 errors, 0 warnings**. 93 blank IPA records and other incomplete fields are retained where data is not verified; the validator does not claim full editorial completion.
- Learning-content validation: **0 errors, 0 warnings**; current inventory: Listening 107 units / 201 questions, Reading 51 units / 200 questions, Grammar 33 lessons / 86 exercises. The separate 80-question Part 5 practice bank remains practice-only and pending independent review.
- Part 1 photos: **9/9** valid assets.
- Objective-resource audit: **11 objectives, 294/294 resource links**.
- Learning outcomes audit: **11/11 objectives, 33 defined criteria, 6/33 with evidence-collection paths**. Foundation instrumentation 6/6 is data-collection wiring, not learner mastery.
- A2 assessment audit: **13/13 Reading passages, 13/13 Listening dialogues, 39/39 questions per skill, 5/5 source-evidence pointers**; answer-position counts across the bank [15, 15, 15, 14].
- Editorial evidence audit: 401 indexed questions.
- Distractor audit: 177 questions in audit scope, 72 structural reserve checks and 12 revisions; answer keys/options structurally valid across the review scope.
- CI coverage guard: PASS; current JavaScript and Python tests are wired in the workflow declarations.
- Project progress snapshot: generated from canonical data; vocabulary 1,137/3,000 minimum (37.9%), 1,137/5,000 planning ceiling (22.7%); stage representation 3/6; outcome instrumentation 6/33. These are inventory/collection metrics, not quality or mastery scores.

## 3. Product behavior boundaries

- Mock exam quick / half / full modes now use distinct SVG icons (bolt / stopwatch / trophy); the mock section uses the clipboard/check symbol.
- The assistant is an optional, dismissible shared shell component. It reuses existing guide navigation, placement diagnostic, dictionary detail renderer and prompt preview; no duplicate learning database or progress tracker was added.
- Prefix search uses the currently loaded canonical/local word records. `ho` returns the current exact matches `hospitality`, `host`, `hotline`, `hour` and `housekeeping`. `house`, `horse`, `home` and `hold` are not in the current canonical list and are not fabricated.
- Google AI is an external, user-initiated handoff, not an embedded AI model or API. The complete prompt is previewed; short prompts are transferred only after click. Oversized prompts are copied in full and opened for manual paste without truncation.
- No new localStorage key, IndexedDB migration, backend, API key or automatic content transfer was added. The assistant helper is included in the Service Worker offline app shell.
- No separate demo mode/temporary dataset was found in the shipped product UI. Legitimate TOEIC learning material containing “demo” or “demonstration” remains unchanged.

## 4. Release-package verification

The final ZIP and TAR.GZ were independently extracted. Their file paths and per-file SHA-256 digests were compared against the release source directory; totals and hashes are recorded in the release handoff. Package integrity and overall SHA-256 checks must pass before distribution.

## 5. Not verified in this session

- A remote GitHub Actions run.
- The public GitHub Pages deployment, service-worker cache refresh or browser cache invalidation after deployment.
- Physical UI/voice QA on Windows, Android, iOS or small tablets.
- Whether the external Google AI web experience remains unchanged; it is third-party UI and may evolve.
- Accuracy/quality of all vocabulary, distractors or AI-generated responses beyond the listed structural and focused audits.

## 6. Execution note

All “PASS” results above refer to local source/tool execution unless specifically stated otherwise. They do not imply that the current GitHub Pages site has already been updated.
