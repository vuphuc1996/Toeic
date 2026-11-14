# Compatibility & Retirement Register

> One active register for release support, storage/data contracts and retirement decisions.

## Current support window — 2026-11-14

| Role | Version | Policy |
|---|---|---|
| Previous baseline | v2.38.0 | Immediate overlay base and rollback reference for v2.39.0. |
| Current candidate | v2.39.0 | Expands separate TOEIC Part 5 practice to 80 questions with grammar-group metadata; no DB version bump or vocabulary ID change. |
| Older releases | ≤ v2.37.0 | Retired from active handoff; concise history remains in `archive/PROJECT_HISTORY.md` and `CHANGELOG.md`. |

## Runtime/data contracts

- Deployment remains GitHub Pages + static PWA; no backend/GAS/iframe/Cloudflare dependency.
- Canonical vocabulary is `data/vocabulary/A.json`–`Z.json`; batch JSON is editorial provenance only. Stable IDs remain immutable.
- Listening/Reading/Grammar resource, question and choice IDs stay stable. Listening Batch 013/014/015 reserve statuses remain unchanged.
- **Mock eligibility:** legacy status-less units and existing v2.33 `internal-editorial-reviewed` Reading records remain eligible for backwards compatibility; `approved-for-mock` is eligible; `reserve-pending-independent-review` and unknown statuses are excluded. New content must not receive an eligible status without the required review decision.
- Part 3/4 conversations/talks are indivisible three-question blocks. Part 6 is an indivisible four-question text; Part 7 single passages 2–4 questions and multiple passages 5 questions.
- Retry/attempt history: `answers` stores latest answer and `attemptHistory` stores prior attempts. Legacy progress without history remains readable.
- IndexedDB remains `toeic-vocabulary-phase1`, v1, store `workspace`; v2.38.0 performs no profile reset/import/export/inspection/migration; `sentenceCompletionSeenIds` is an optional additive field in the existing `practiceSession` object.
- Focus Workspace remains shared; `.learning-focus-content` is the only vertical scroll owner. The Part 5 Sentence Completion mode uses this shell and the existing answer-feedback/auto-next behavior.
- `data/practice/part5-sentence-completion.json` is a separate 35-question original practice bank; it is not part of the 200-question Reading Mock bank. All items remain pending independent review and are practice-only.
- Service Worker cache markers sync from `data/manifest.json`; `REQUIRED`/`APP_SHELL` include `assets/js/sentence-completion.js` and `data/practice/part5-sentence-completion.json`, with static integrity checked by `test_pwa_readiness.py`. This does not replace browser offline/reconnect QA.
- Preserve user-owned `assets/listening/*.jpg`, attribution and SVG fallbacks. Eight JPG binaries are intentionally absent from this source snapshot; never overwrite or delete the repository originals.
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
