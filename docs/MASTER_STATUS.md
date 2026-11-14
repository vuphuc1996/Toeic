# TOEIC DICTIONARY — MASTER STATUS

> **Nguồn trạng thái và lộ trình duy nhất.** Mọi release cập nhật trực tiếp file này. `CHANGELOG.md` là log phát hành; `archive/PROJECT_HISTORY.md` là chỉ mục tài liệu đã nghỉ hưu; `COMPATIBILITY.md` là sổ tương thích duy nhất.

- **Ngày kiểm kê:** 2026-11-14.
- **Phiên bản mã nguồn đang kiểm kê:** v2.39.0 (TOEIC Part 5 Grammar and Structure Expansion; local candidate).
- **Current candidate:** v2.39.0 — TOEIC Part 5 Grammar and Structure Expansion.
- **Previous baseline:** v2.38.0 — TOEIC Part 5 Sentence Completion Practice.
- **Base:** v2.38.0; app remains GitHub Pages + static PWA, no backend/GAS/iframe/Cloudflare.
- **Release state:** local candidate. Remote GitHub Actions, Pages deployment and physical-device behavior are not verified from this workspace.
- **Development rule:** finish the internal product/content backlog first. Do not issue acceptance reminders or a broad acceptance checklist while development is active. The eventual test plan should focus on high-risk user flows rather than repeat a 100% inventory sweep.

## 1. v2.39.0 changes

### TOEIC Part 5 · Grammar and Structure Expansion

- Expanded the separate adaptive sentence-completion practice bank from 35 to **80 original questions**: 35 initial questions plus 45 new Batch 016 questions (`p5-sc-036`–`p5-sc-080`).
- Tagged all 80 questions with a grammar category. Coverage spans 14 groups: adjectives/adverbs (10), articles/determiners (3), conjunctions/clauses (3), gerunds/infinitives (3), imperatives/verb forms (1), infinitives/verb patterns (13), linking verbs (1), modal verbs (2), participles/reduced relative clauses (1), passive voice (5), prepositions/collocations (13), subject–verb agreement (7), verb tense/aspect (8), and word forms/nouns (10).
- Balanced the authored answer key positions A/B/C/D at 20/20/20/20. Runtime answer shuffling still preserves the corresponding option explanations.
- The Focus Workspace now shows the question's grammar group above the sentence and repeats it in the answer-review explanation. No separate screen or new storage system was added.
- Kept a unique `question ID` history for Part 5 and the existing canonical vocabulary `wordId` progress weighting. All 80 question targets resolve to distinct pre-existing vocabulary IDs; no headwords were added and no ID was changed.
- Added batch metadata (`editorialBatch=016`, `contentBatch=batch-016-part5-grammar-expansion`) and validation for grammar tags, group totals, option feedback prefixes and review status.
- Improved distractor wording in several preposition items to remove accepted alternative constructions (including `beneficial for`, `notify about`, and agent/beneficiary readings of `by/for`).
- All 80 items remain `reserve-pending-independent-review`. This release includes an internal author re-check and automated structural/runtime checks, not an independent second-person review. The bank remains practice-only and is excluded from Reading Mock inventory/scoring.

### Compatibility and unchanged areas

- Vocabulary remains 992 headwords; the v2.37 word-family relationships remain unchanged.
- Official Reading remains 200 questions (Part 5=60, Part 6=32, Part 7=108). The separate 80-question Part 5 practice bank is not included in those counts or Mock.
- Listening remains 200 questions, Grammar remains 33 lessons/86 exercises, and Mock blueprints/eligibility, TTS, stable resource/question/choice IDs and other study modes are unchanged.
- IndexedDB remains `toeic-vocabulary-phase1`, version 1, store `workspace`. Existing `sentenceCompletionSeenIds` and `studyProgress` behavior are preserved; no database version bump, reset or migration is introduced.
- Service Worker already lists the Part 5 module and data bank in `REQUIRED` and `APP_SHELL`; their updated files remain covered without adding a new runtime path.

## 2. Baseline inventory

| Area | Current inventory | Current development status |
|---|---:|---|
| Vocabulary | 992 headwords | 207 records with word-family links; 292 total links; US IPA on 642 records |
| Listening | **200 questions / 106 units** | 102 Mock-eligible; 98 reserve-pending-independent-review |
| Reading | **200 questions / 51 resources** | Two Full Reading forms can be selected without repeated eligible question IDs |
| Grammar | **33 lessons / 86 exercises** | Retry and shared Focus Workspace preserved |
| Separate TOEIC Part 5 practice | **80 sentence-completion questions** | 14 grammar groups; A–D positions 20/20/20/20; practice-only, all pending independent review |
| Mock formats | 15m/25Q · 60m/100Q · 120m/200Q | Blueprint and indivisible passage/conversation blocks preserved |

## 3. Content readiness and known limits

1. Listening totals by Part: P1=8, P2=51, P3=81, P4=60. The 98 pending questions are Batch 013=11, Batch 014=17 and Batch 015=70. They remain available for ordinary practice but excluded from Mock until a second independent reviewer records a decision.
2. Current eligible Listening pool: P1=8, P2=25, P3=39, P4=30. One 100-question Listening form can be assembled; a second currently reuses 98/100 question IDs.
3. Once all 98 reserves are approved, the eligible pool would become P1=8, P2=51, P3=81, P4=60. Two zero-repeat Full Listening forms still require four more distinct Part 1 photo-description items, taking the target P1 pool from 8 to 12.
4. Eight original Part 1 Pexels photographs have existing user-owned JPGs and attribution on the user's repository; the supplied source snapshot intentionally omits those eight JPG bytes. The eight SVG fallbacks are present. Do not overwrite or remove the user's original JPGs.
5. Part 1 strict-photo validation is therefore not certified by this source snapshot. SVG fallback availability is not equivalent to confirming all photograph binaries.
6. Reading's 200-question bank already supports two zero-overlap Full forms according to the local inventory audit. The 45 expanded Part 7 questions still need semantic second-person review of key/distractor quality.
7. All 80 Part 5 practice items are original practice material, not ETS items. The initial 35 plus Batch 016=45 have not received independent second-person approval; a well-formed single key and passing automated checks do not prove every distractor is semantically unique. Do not promote the bank to Mock.
8. Mock results are raw practice correct-count and accuracy indicators, not official ETS-equated Listening/Reading scores. No ETS questions or recordings are included.
9. Vocabulary has 992 headwords, below the internal 3,000–5,000 planning target. US IPA is present on 642/992 records; word-family links on 207/992. Remaining gaps in IPA, verb forms, collocations, synonyms/antonyms and definitions require sense-by-sense curation. CEFR assignments are editorial estimates unless individually marked with a verified basis.

## 4. Runtime and learning behavior

- Canonical vocabulary remains `data/vocabulary/A.json`–`Z.json`; `batch-*.json` is provenance only. Stable IDs are immutable.
- Keep stable Vocabulary/Listening/Reading/Grammar resource, question and choice IDs. Append new questions; do not reorder existing indexes linked to local progress.
- IndexedDB remains `toeic-vocabulary-phase1`, version 1, store `workspace`; no profile reset/import/export/inspection/migration in v2.39.0. The Part 5 seen-question list remains an optional additive field in the existing practice-session object.
- Retry and Attempt History remain device-local and preserve latest answer plus prior attempts.
- Flashcard images remain text-first; a word-specific image is shown only when its `imageStatus` is explicitly approved.
- TTS remains browser SpeechSynthesis. Voice availability and quality vary by OS/browser; the app can select and pace available voices but cannot supply missing native voice packs.
- Service Worker and app-shell validation remain static source checks. Actual GitHub Pages deployment, browser offline/reconnect and physical-device rendering are not verified here.

## 5. Active development backlog

| Priority | Workstream | Current state / next implementation |
|---|---|---|
| P0 | Listening reserve content | Complete source-grounded second-person review of 98 pending questions; correct key, evidence, distractors and naturalness before approval |
| P0 | Part 1 photo pool | Add four distinct photo-description items and local assets without touching the existing eight JPGs; target 12 distinct Part 1 items |
| P1 | Part 5 editorial review | Obtain an independent second-person review of all 80 questions; do not expand further or promote into Mock until key, distractor, grammar and naturalness decisions are recorded |
| P1 | Reading editorial quality | Complete semantic second review of the 45 expanded Part 7 questions; source-quote existence alone is not approval |
| P1 | Vocabulary | Continue sense-level work: IPA (350 currently missing), word families, verb forms, collocations, relation data, definitions and example accuracy; prioritize common TOEIC business/travel words |
| P1 | PWA/device behavior | Keep hardening high-risk display, offline cache, reconnect and asset-fallback behavior; reserve physical QA for the eventual final test plan |

IELTS remains deferred until the TOEIC development backlog is closed and the user explicitly approves the phase change.

## 6. Focused verification commands for this release

```bash
python -m unittest discover -s tools/tests -p 'test_sentence_completion.py' -v
python -m unittest discover -s tools/tests -p 'test_pwa_readiness.py' -v
python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v
node tools/tests/sentence-completion.mjs
node tools/tests/learning-focus-workspace.mjs
node tools/tests/practice-progress.mjs
python tools/validate-learning-content.py
python tools/validate-data.py
python tools/audit-toeic-coverage.py
python tools/sync-version.py --check
```

These checks target the new practice bank, Focus Workspace/session continuity, app-shell registration and core data integrity. They are not a declaration that remote deployment, browser offline/reconnect or physical-device behavior has been completed.

## 7. Two-generation documentation rotation

Current pair: v2.38.0 (previous) + v2.39.0 (current). When v2.40.0 is published, v2.38.0 will be summarized into `archive/PROJECT_HISTORY.md` and retired from active batch/report/root note/manifest files. Rotator must never touch app source, canonical JSON, assets, patches or learner profiles.
