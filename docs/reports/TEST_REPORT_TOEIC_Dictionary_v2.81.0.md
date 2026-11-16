# TOEIC Dictionary v2.81.0 — Test & Verification Report

**Date:** 2026-11-16  
**Base:** v2.80.0 Full Source  
**Release:** v2.81.0 Runtime AI Removal & A2 Writing Portfolio Review

## 1. Python regression tests

**151/151 PASS across 21 selected modules.** These are explicitly selected modules, not a claim that every `test_*.py` file in the repository was run.

| Module | Tests | Status |
|---|---:|---|
| `test_foundation_production_revision.py` | 6 | PASS |
| `test_foundation_a2_production.py` | 7 | PASS |
| `test_ci_coverage.py` | 2 | PASS |
| `test_sync_version.py` | 12 | PASS |
| `test_design_profile.py` | 6 | PASS |
| `test_learning_content.py` | 34 | PASS |
| `test_foundation_pathway.py` | 10 | PASS |
| `test_foundation_reading.py` | 9 | PASS |
| `test_foundation_listening.py` | 13 | PASS |
| `test_foundation_outcome_evidence.py` | 2 | PASS |
| `test_learning_outcomes.py` | 3 | PASS |
| `test_learning_outcome_progress.py` | 3 | PASS |
| `test_project_progress.py` | 4 | PASS |
| `test_objective_resource_map.py` | 2 | PASS |
| `test_pwa_readiness.py` | 3 | PASS |
| `test_responsive_layout.py` | 5 | PASS |
| `test_learning_surface_consistency.py` | 5 | PASS |
| `test_part1_photo_assets.py` | 6 | PASS |
| `test_sentence_completion.py` | 12 | PASS |
| `test_vocabulary_batch_012.py` | 4 | PASS |
| `test_release_rotation.py` | 3 | PASS |

## 2. JavaScript regression suites

**25/25 PASS.** The complete `tools/tests/*.mjs` set was executed. `quick-help.mjs` verifies the local-only helper, true vocabulary masking/completion, no fabricated dictionary records, navigation/offline wiring, and absence of runtime AI/Google prompt-transfer UI. `foundation-production-revision.mjs` verifies revision chaining, task-level rubrics, review gates, legacy separation and portfolio aggregation.

- `alphabet-sound-progress.mjs` — PASS
- `assessment-deferred-workflow.mjs` — PASS
- `explanation-rubric-self-report.mjs` — PASS
- `flashcard-image-policy.mjs` — PASS
- `foundation-a2-production.mjs` — PASS
- `foundation-application-evidence.mjs` — PASS
- `foundation-evidence.mjs` — PASS
- `foundation-listening-evidence.mjs` — PASS
- `foundation-outcome-evidence.mjs` — PASS
- `foundation-production-revision.mjs` — PASS
- `foundation-reading-evidence.mjs` — PASS
- `learning-focus-workspace.mjs` — PASS
- `learning-outcome-progress.mjs` — PASS
- `listening-tts-regression.mjs` — PASS
- `mock-exam-engine.mjs` — PASS
- `mock-guided-flow.mjs` — PASS
- `mock-ui-integrity.mjs` — PASS
- `objective-recall-timing.mjs` — PASS
- `part5-timing-integration.mjs` — PASS
- `practice-progress.mjs` — PASS
- `quick-help.mjs` — PASS
- `recall-queue.mjs` — PASS
- `runtime-render-smoke.mjs` — PASS
- `sentence-completion.mjs` — PASS
- `vocabulary-release-integrity.mjs` — PASS

## 3. Syntax and static parsing

- Python: **66/66** files under `tools/` compiled with `py_compile`.
- JavaScript: **14/14** files (`assets/js/*.js` plus `sw.js`) passed `node --check`.
- `index.html`: Python HTMLParser PASS.
- CSS: 2 stylesheets parsed by `tinycss2`, **0 syntax errors** (1,891 top-level tokens).
- Design profile: **54 tokens** and **379** legacy font-floor selector groups synchronized.
- Version sync: all release markers report **2.81.0**.

## 4. Data and content validators

| Check | Result |
|---|---|
| Vocabulary data | 1,137 records; 0 errors; 0 warnings |
| Learning Content | Listening 107 units / 201 questions; Reading 51 / 200; Grammar 33 / 86; 0 errors / 0 warnings |
| Part 1 photos | 9/9 assets valid; attribution checked |
| Objective-resource links | 294/294; 11 objectives |
| Learning outcomes | 11/11 objectives; 33 criteria; 6/33 with an evidence collection path; Foundation 6/6 instrumented |
| CMUdict IPA | 333 source-linked records PASS |
| A2 assessment audit | Reading 13/13 and Listening 13/13; 39 questions each; 5/5 source evidence links; answer positions [15,15,15,14] |

## 5. Runtime AI removal check

- Removed Google AI links, prompt builders/previews/transfers, UI actions, modal markup/styles and stale event listeners from runtime files.
- No AI model/API/backend or network prompt service is loaded by the application.
- The local Quick Help component remains deterministic and device-local: app navigation, existing Placement Diagnostic entry and masked completion against canonical vocabulary records.
- The regression scans `index.html`, runtime JS/CSS, Service Worker and relevant workflow/test wiring for retired AI UI and handlers.
- Existing `ai-generated` attribution labels in the photo provenance ledger are retained as asset-source metadata only. They are not code, a model or a runtime integration; deleting them would make source attribution/audits inaccurate.
- Browser-installed TTS voices with provider names are still local OS/browser SpeechSynthesis and are not remote AI integration.

## 6. Release package verification

- Full Source ZIP and TAR.GZ each contain **256 files**.
- Both packages were independently extracted to separate directories.
- Source vs ZIP: **256/256 relative paths and per-file SHA-256 matched**.
- Source vs TAR.GZ: **256/256 relative paths and per-file SHA-256 matched**.
- ZIP vs TAR.GZ: **256/256 files matched**.
- Sidecar SHA-256 files for both archives were checked against the archive bytes and matched.
- The clean packages exclude Python bytecode/cache artifacts (`__pycache__`, `*.pyc`).

## 7. Limits

- Local tests do not prove that remote GitHub Actions passed.
- GitHub Pages production deployment/cache behavior has not been checked in this session.
- No physical-device QA on iOS/Android/tablets/laptops is claimed.
- Self-ratings are not automated language grading, TOEIC scoring, CEFR certification or proof of mastery.
