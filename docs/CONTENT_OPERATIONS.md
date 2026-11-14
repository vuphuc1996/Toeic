# TOEIC Content Operations — governed update workflow

## 1. Scope

Only TOEIC Listening & Reading content is in active development. Do not add IELTS/Academic materials, filters, data tags or lessons until the Master acceptance gates are satisfied and the user approves the scope change.

## 2. Source-of-truth files

| Content | Canonical path | Rule |
|---|---|---|
| Vocabulary | `data/vocabulary/[A-Z].json` | 26 alphabet files are runtime source; preserve record IDs; UI treats base data as read-only. |
| Topic list | `data/categories.json` | Do not invent topic IDs in a vocabulary patch. |
| Related gloss | `data/related-terms.json` | Only add a gloss when the relation and Vietnamese meaning are supportable. |
| Listening | `data/listening/listening-library.json` | Every unit needs Part, type, title, topic, level, source status, segments, question(s), answer and explanation. |
| Reading | `data/readings/reading-library.json` | Every unit needs Part 5/6/7, documentType, topic, level, passage/documents, questions, answer and explanation. |
| Grammar | `data/grammar/lessons.json` | Every exercise needs unique id, four choices, answerIndex and explanation. |

## 3. Vocabulary record quality

For each headword, review stable `id`, spelling/lemma, POS by sense, Vietnamese meaning, English definition, CEFR estimate, US/UK IPA, examples + translations, topics, word family, verb forms, collocations and lexical relations. Fields are conditional: do not force verb forms onto nouns, antonyms onto words without a clear antonym, or IPA values without a source. Keep multi-sense meaning distinct. CEFR is an editorial estimate unless independently verified per sense.

Use source notes and patch operations. Each data patch must pin `baseDataVersion`, `targetDataVersion`, `idSetSha256`, stable ID, JSON Pointer and `expect.old`. Run dry-run before apply. Do not edit production A–Z JSON by hand when a patch is applicable.

## 4. Listening content quality

- Part 1: one image prompt, four short spoken descriptions, exactly one correct answer; answer keys distributed across A–D; no text transcript printed as a hint before answer. Label vector artwork as illustrations; the prompt must say “illustration” (or neutral “image”), never “photograph” when the asset is an SVG.
- Part 2: short question/prompt and three natural response options; one best response.
- Part 3: multi-turn conversation with realistic workplace context, speaker identity continuity, multiple questions per conversation, detail/inference/purpose questions.
- Part 4: one short talk/announcement with multiple linked questions; use natural announcement/report/briefing discourse.
- Include transcript and Vietnamese explanation in review mode. Explanations must state the supporting clue and reasoning, not only repeat the correct option. A locale check must not accept an English token with an accent (for example, “résumé”) as proof of Vietnamese text. Browser TTS is synthesized audio and must not be presented as official or recorded ETS audio. Use accent variation in content where the voice is available; keep manual user voice choice higher priority than defaults.

## 5. Reading content quality

- Part 5: incomplete sentence, one blank, four parallel choices; explain grammar/meaning/discourse cues.
- Part 6: text completion with blank markers matching question count; include word/phrase and sentence-insertion item types where meaningful.
- Part 7: single, double and triple documents; connect questions to information across documents; include purpose, detail, inference, reference, vocabulary and insert-sentence questions.
- Each passage/document needs a documentType label (EMAIL, NOTICE, MEMO, ADVERTISEMENT, ARTICLE, SCHEDULE, POLICY, INVOICE/ORDER, etc.) and workplace/real-life context.
- Explanations must justify the right answer and explain why distractors fail, not just repeat the answer.

## 6.1 Dashboard content presentation

- The TOEIC Learning Diagnostics section uses an open section heading and short explanatory copy, not a second generic `.panel` card surrounding all metrics.
- Keep Listening and Reading as clearly separated groups. Frame only the seven interactive Part tiles; keep priority guidance as a light note below the groups.
- Preserve the statement that the figures are internal learning indicators, not an ETS score conversion. Do not introduce an estimated official score without a separate validated model.
- Maintain responsive layouts at desktop, tablet and narrow mobile widths; every Part tile must remain keyboard-focusable and the live priority status must be announced to assistive technology.

## 6. Content lifecycle

`Draft → source check → editorial review → schema validation → patch dry-run → apply → automated content QA → coverage report → version sync → unit tests → ZIP integrity → extracted-package recheck → Master/Changelog update`.

Any item whose source or answer is uncertain stays `draft-review` and must not be mixed into a production-ready test form. Keep original authoring provenance; do not copy ETS copyrighted sample questions/audio without explicit permission/licence. Official format facts may be referenced with citations, but must not be reproduced as proprietary item content.

## 7. Required release commands

```bash
python -m py_compile tools/validate-data.py tools/validate-learning-content.py tools/audit-toeic-coverage.py tools/sync-version.py tools/patch-data.py
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/audit-toeic-coverage.py
python tools/sync-version.py --check
node --check assets/js/app.js
node --check sw.js
```

Run unit tests separately by module: `test_baseline_ids.py`, `test_patch_data.py`, `test_sync_version.py`, `test_validator.py`, `test_learning_content.py` and `test_dashboard_layout.py`. After packaging, unzip into a clean directory and run data validator, content validator, sync-version, JS syntax and ZIP CRC again.

## 8. Coverage report and release record

Every release updates the same central documents:
- `docs/MASTER_STATUS.md`: current totals, Part coverage, blockers, acceptance gate and next action.
- `docs/CHANGELOG.md`: one concise release entry; the only detailed chronological release log.
- `docs/COMPATIBILITY.md`: only when support, storage, route, cache or data contracts change.
- `docs/DESIGN_SYSTEM.md`: only when shared interaction/layout rules change.
- `docs/batches/` and `docs/reports/`: keep one detailed record for the previous release and one for the current release only. The current file supersedes the older one when the next version is published.
- Source links and editorial method are recorded inside the current batch document; do not create one source Markdown file per batch.

All Markdown stays inside `docs/`. Keep one Master only. State clearly what has not been tested on target devices/remote GitHub.

## 9. One-form question-pool gate

The v2.12.0 minimum needed to select one TOEIC L&R form is: Listening P1≥6, P2=25, P3=39, P4=30; Reading P5=30, P6=16, P7≥29 single-passage questions + 25 multiple-passage questions (double/triple). These are blueprint minima for one form, not a guarantee of multiple non-repeating forms.

- Each Part 2 record contains exactly one question and three response options.
- Each Part 3 conversation and Part 4 talk contains exactly three linked questions. Part 3 must identify at least two distinct speakers.
- Each Part 7 DOUBLE PASSAGE record must contain exactly two `documents[]` items; TRIPLE PASSAGE must contain exactly three. Each document requires a non-empty `label` and `content`. Retain `passage` where current UI compatibility still depends on it.
- Extend existing sets by appending questions only. Never reorder or replace an existing question index because learners may already have local progress keyed to that item. New sets get unique stable resource IDs.
- Keep visual and audio provenance explicit: licensed Part 1 photographs use `visualType: photograph` and record creator/source/license in `assets/listening/ATTRIBUTION.csv`; SVG fallback artwork remains `visualType: illustration` when used as the primary asset. Browser SpeechSynthesis is synthesized audio, not a recorded native-speaker asset or ETS audio. Cache user-facing photo files locally and keep SVG fallback assets in the required app shell.
- Passing automated checks confirms structural integrity only. Before Full Mock, manually review every item's transcript/passage grounding, correct answer, distractors and Vietnamese rationale.


## 10. Documentation consolidation and two-release rotation

The active documentation set is deliberately small: `MASTER_STATUS.md`, `COMPATIBILITY.md`, `CHANGELOG.md`, `DESIGN_SYSTEM.md`, `CONTENT_OPERATIONS.md`, `README.md`, one archive index, and the previous/current release batch + test report. `reference/` is reserved for one-off external research that is still actively used.

When a new release is prepared:
1. Copy the previous current release batch/test record forward as the previous release file; add one new batch file and one new test report for the current release.
2. Update the Master, Changelog and Compatibility only where facts changed.
3. Run `python tools/rotate-release-files.py` and review every planned retirement.
4. Run `python tools/rotate-release-files.py --apply` only after verifying the two files retained in each release-specific folder. Old batch/report/source documents are converted into short index entries in `archive/PROJECT_HISTORY.md`; complete old copies are not duplicated.
5. Never create separate roadmap, Master, design-system, compatibility, or per-feature UI guide files. Put each decision in its existing central document.

The rotator is restricted to Markdown under `docs/batches/`, `docs/reports/`, `docs/sources/` and root `V*_UPDATE_NOTES.txt`. It must never touch application source, canonical JSON, `assets/`, PWA resources, patches or local learner profiles.
