# Compatibility & Retirement Register

> One active register for release support, storage/data contracts and retirement decisions.

## Current support window — 2026-11-16

| Role | Version | Policy |
|---|---|---|
| Previous release | v2.82.1 | Preserves v2.79 feature-level Google AI and Mock Exam icons; removes Quick Help prefix/masked-letter search. |
| Current product source | v2.83.0 | Adds local Robot Buddy onboarding/progress feedback, removes the usage guide and all Quick Help word search, retains the entire v2.79 Google AI scope and Mock Exam icons. |
| Older releases | ≤ v2.82.0 | Historical; prototype behavior and scope corrections are consolidated in `archive/PROJECT_HISTORY.md` and `CHANGELOG.md`. |

- **SW002 repair:** `assets/js/learning-assistant.js` (active local Robot Buddy summary) and `assets/js/quick-help.js` (no-op compatibility tombstone) are present in both Service Worker `REQUIRED` and `APP_SHELL`. This directly addresses SW002 for these asset paths in an overlay update. Cache version is synced to `data/manifest.json`.
- **CI contract:** `tools/tests/learning-assistant.mjs`, `tools/tests/quick-help.mjs` and `tools/tests/legacy-google-ai.mjs` are all invoked in `.github/workflows/validate-data.yml`; the CI coverage test enforces every JavaScript regression file is called.

## Runtime/data contracts

- **Legacy Google AI from v2.79:** preserve the original user-triggered Google AI feature actions for vocabulary detail/unknown-term lookup, practice answer and review analysis, Grammar, Reading and Listening. The existing shared preview is opened by each feature's own control; the user explicitly confirms before the external Google Search AI Mode handoff (`udm=50`, `hl=vi`). This is not a documented stable API. Google controls the external experience. No embedded model, API key or server-side AI exists.
- **AI boundary:** only the original v2.79 feature-level Google AI actions are supported. There is no shared contextual AI assistant, assistant follow-up, copy/transfer flow or Google AI action inside Quick Help.
- **Robot Buddy v2.83:** `assets/js/learning-assistant.js` reads the existing local progress state and derives restrained summaries/milestone messages. It is deterministic local code, not a generative model, not an external AI API and not a free-form answer engine. It does not send learning history outside the device. The first-run question reuses the existing Placement Diagnostic; the choice is stored under `toeic:robot-companion-onboarding:v1`.
- **Quick Help retirement:** no usage guide, prefix lookup, suggestion list, masked vocabulary headword, missing-letter input or exact-match vocabulary shortcut remains. The Robot launcher/panel replaces the previous Quick Help UI. `assets/js/quick-help.js` is intentionally a no-op tombstone to overwrite stale copies from older GitHub checkouts; it has no runtime behavior.
- **Robot progress thresholds:** the weakest Reading/Listening Part is suggested only after at least three unique answered questions in that Part. The snapshot reads latest answer per question, not retry counts as separate questions. A2 writing is reported from learner self-assessment within each task; different rubrics are not combined into a fake overall score. These summaries are guidance, not mastery or CEFR/ETS certification.
- **Local milestone behavior:** Robot feedback is published after existing completed actions (e.g. three correct vocabulary answers in a row, Flashcard completion, Placement completion, Mock completion and A2 writing revision). It does not make unsupported AI claims.
- **Mock Exam icons:** retain `icon-clipboard-check`, `icon-bolt`, `icon-stopwatch`, `icon-trophy`; do not revert to the old `◷` glyph.
- **Source attribution exception:** `ai-generated` strings in Part 1 image attribution/audit files are provenance metadata only; they do not execute or activate AI features.

- Deployment remains GitHub Pages + static PWA; no backend/GAS/iframe/Cloudflare dependency.
- Canonical vocabulary is `data/vocabulary/A.json`–`Z.json`; batch JSON is editorial provenance only. Stable IDs remain immutable.
- Listening/Reading/Grammar resource, question and choice IDs stay stable. Listening Batch 013/014/015 reserve statuses remain unchanged.
- **Mock eligibility:** legacy status-less units and existing v2.33 `internal-editorial-reviewed` Reading records remain eligible for backwards compatibility; `approved-for-mock` is eligible; `reserve-pending-independent-review` and unknown statuses are excluded. New content must not receive an eligible status without the required review decision.
- Part 3/4 conversations/talks are indivisible three-question blocks. Part 6 is an indivisible four-question text; Part 7 single passages 2–4 questions and multiple passages 5 questions.
- Retry/attempt history: `answers` stores latest answer and `attemptHistory` stores prior attempts. Legacy progress without history remains readable.
- IndexedDB remains `toeic-vocabulary-phase1`, v1, store `workspace`; v2.38.0 performs no profile reset/import/export/inspection/migration; `sentenceCompletionSeenIds` is an optional additive field in the existing `practiceSession` object; v2.40.0 does not alter storage. v2.52.0 adds only the `objectiveProgress` key to the existing workspace store; no object-store/database-version migration or profile reset.
- Foundation progress remains in localStorage key `toeic:foundation-progress:v1`. v2.74.0 adds recall-check history under each stable question evidence record and a separate `productionEvidence` map for learner-authored responses/self-ratings. A first recognition attempt becomes due for recall after 24 hours; correct recall schedules 3 days and incorrect recall 1 day. Early recall is rejected. These are local practice/self-report signals, not automated assessment or mastery; no IndexedDB v1 schema migration is introduced.
- v2.75.0 adds only new A2 lesson, question, application, Reading passage and Listening script IDs to the existing Foundation JSON resources. It reuses the v2.74.0 evidence APIs and progress contract; there is no localStorage key change, IndexedDB migration, learner-data reset or overwrite of earlier lesson/resource IDs.
- v2.76.0 adds A2 Reading q3 and Listening q3 to existing A2 resources, extends A2 passages/dialogue scripts and adds four-turn `segments` for multi-speaker playback. The exact v2.75 question-pair baseline verifies the old q1/q2 objects remain unchanged. Pre-A1/A1 legacy Listening scripts remain compatible through sentence-splitting fallback. A2 uses 3 questions / 67% local practice threshold; older levels continue 2 / 80%. No storage schema, progress key, stable old ID or audio dependency changes.
- v2.77.0 revises five existing A2 question prompts/tasks to remove identified within-resource q2/q3 repetition and adds exact source-evidence metadata to five questions. The v2.75 canonical hash baseline still protects every prior A2 q1/q2 object. Question IDs, answer-position balance, progress keys, IndexedDB v1 and TTS contracts remain unchanged; the evidence fields are additive question metadata.
- v2.78.0 adds a `productionTask` contract to each of the 13 A2 lessons, with new stable IDs `::produce1`, custom task prompts/rubrics and an eight-word response minimum. The new learner-authored responses are additive entries in the existing `productionEvidence` object under `toeic:foundation-progress:v1`; no new key/database or IndexedDB migration is introduced. Prior A2 `::apply1` production responses remain preserved and are not used as evidence for the new prompts. Pre-A1/A1 continues to use the existing `::apply1` IDs and three-word default. New task definitions are protected by a versioned SHA-256 baseline.
- v2.79.0 extends the existing `productionEvidence` records with response text in newly captured attempts and `guided_revision` entries containing `basedOnResponse`, revised `response`, three learner-confirmed review checks and three self-ratings. No new localStorage key or database is added. Historical attempts from before v2.79.0 are preserved without reconstructing missing text; the last stored response is the revision starting point. `::produce1` and legacy `::apply1` evidence remain isolated. Revision data is device-local and not automatically graded; no IndexedDB v1 schema migration occurs.
- Focus Workspace remains shared; `.learning-focus-content` is the only vertical scroll owner. The Part 5 Sentence Completion mode uses this shell and the existing answer-feedback/auto-next behavior.
- `data/practice/part5-sentence-completion.json` is a separate 35-question original practice bank; it is not part of the 200-question Reading Mock bank. All items remain pending independent review and are practice-only.
- Service Worker cache markers sync from `data/manifest.json`; `REQUIRED`/`APP_SHELL` include `assets/js/sentence-completion.js` and `data/practice/part5-sentence-completion.json`, with static integrity checked by `test_pwa_readiness.py`. This does not replace browser offline/reconnect QA.
- Preserve `assets/listening/*.jpg` and mixed-source attribution. Listening Part 1 is photo-only: each record declares its JPG in `photo`; no per-item SVG fallback is declared, cached, referenced or retained. All nine optimized original/project-owned JPG assets are embedded in the current source, 1448×1086 (4:3 landscape), each below 400,000 bytes. Do not replace them with generated or unrelated stock images.
- Browser SpeechSynthesis is synthesized audio, not ETS/native recording. Multi-speaker voice differentiation is best-effort and depends on installed OS/browser voices.
- Mock metrics are practice correct-count/accuracy, not ETS-equated scores.

## CI test contract

- `.github/workflows/validate-data.yml` must invoke every `tools/tests/test_*.py` module and every `tools/tests/*.mjs` regression suite.
- `test_ci_coverage.py` enforces this wiring so future tests are not silently skipped.
- A passing local coverage guard confirms workflow declarations only; it does not prove a remote GitHub Actions run passed.

## Retirement / rotation

- Keep only the current and immediately previous release-specific batch/report/update notes/manifest files.
- Old docs are compacted into `archive/PROJECT_HISTORY.md`; do not clone old reports into new paths.
- Do not overlay a non-adjacent version blindly. Do not touch app source, canonical JSON, assets, PWA shell, patches or learner profiles during document rotation.

## Retired/incompatible references

- Legacy GAS/iframe/cloud-backend proposals remain historical.
- Do not create duplicate canonical runtime data, standalone roadmap/master or feature-specific design system copies.
