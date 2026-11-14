# TOEIC Dictionary — concise release changelog

> Quick chronological index. v2.29.0 and v2.28.0 are the active/current handoff details. Older releases are intentionally summarized here; retired batch, report and source notes are indexed in `archive/PROJECT_HISTORY.md`. Do not append duplicate version headings.

## v2.29.0 — Shared Learning Workspace & Flashcard Single Scroll (2026-11-13)
- Refactored Flashcard into an upper vocabulary panel and an expanding lower meaning/example panel; removed the inner fixed-height scrolling face.
- Standardized Flashcard, Review, Grammar, Reading and Listening detail flows on the same `learningFocusBackdrop` shell. Grammar/Reading/Listening now mount content through `openLearningDetail()`.
- Made `.learning-focus-content` the single vertical scroll owner. Short content stays natural-height; long passage/transcript/explanation content scrolls once in the shared workspace.
- Updated responsive phone/tablet rules and reduced-motion behavior without changing question data, vocabulary IDs, TTS settings, Mock logic or IndexedDB schema.
- Removed 40 unused rules from the former fixed-height Flashcard flip-face and nested-scroll layout.
- Consolidated documentation around one Master, Compatibility, Design System, Content Operations, Changelog and compact Project History. Release-specific batch/report/update notes rotate as previous + current only.
- Local regression results and package verification: see `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.29.0.md`. Remote CI/Pages and physical-device QA remain pending.

## v2.28.0 — Vocabulary Batch 018 & two-version release rotation (2026-11-12)
- Added 8 new TOEIC headwords after checking the existing canonical bank for duplicates; canonical total is 979. New records have sense-linked POS, Vietnamese meaning, English definition, example/translation, US IPA, topic and collocations. CEFR remains an editorial estimate pending independent review.
- Added `data/vocabulary/batch-007.json` as the current editorial batch source; A–Z files remain the only canonical runtime vocabulary source. Existing stable IDs were preserved.
- Introduced a two-version handoff policy: immediate previous stable baseline + current candidate. Older release notes are not carried forward as separate active files.
- Consolidated superseded batch/test/coverage reports and the prior long Master snapshot into `docs/archive/PROJECT_HISTORY.md`; `docs/MASTER_STATUS.md` is now a concise active status/roadmap file, and `docs/COMPATIBILITY.md` is the only compatibility register. The competitor benchmark is in `docs/reference/`.
- No IndexedDB schema/profile changes, no image binaries added, and no user-owned Listening JPGs deleted. Remote Actions/Pages and physical-device QA remain pending.

## v2.27.0 — Focus learning workspace & Vocabulary Batch 017 (2026-11-12)
- Added one shared fixed focus workspace with a dimmed/blurred backdrop, internal scrolling and a persistent close (×) control. Flashcard sessions and their follow-up vocabulary check now share the same workspace; the first card tap flips to meaning/examples and the next tap adv…
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.26.0 — Flashcard image relevance & responsive layout
- Removed the generic topic illustration from individual vocabulary flashcards. A word card is text-first by default so an unrelated office/travel/finance image can no longer imply the wrong meaning.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.25.0 — Full TOEIC Mock Practice Beta (2026-11-11)
- Added three timed test modes: 15-minute quick test (25 questions), 60-minute half test (100 questions) and 120-minute full test (200 questions), with Listening/Reading timers (5:22/9:38, 22:30/37:30 and 45:00/75:00 respectively).
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.24.0 — Listening/TTS playback reliability (2026-11-11)
- Hardened speech cancellation so the app resolves its active utterance immediately before calling the browser speech engine. The Listening playback sequence can no longer remain stuck waiting for a cancellation callback that some speech engines may omit.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.23.0 — Part 1 photo QA hardening & Listening reserve batch (2026-11-11)
- Re-audited all eight Part 1 photo/answer pairs against the Pexels source descriptions. Correct statements for the warehouse and air-conditioning items now describe the visible actions more precisely; answer indexes, option arrays, choice IDs and question IDs are unchanged.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.22.0 — Licensed Part 1 photographs & offline-safe image loading (2026-11-11)
- Replaced the primary Part 1 visual source with eight locally hosted Pexels JPG paths from the user's asset manifest; each item keeps its existing SVG fallback for missing/corrupt photo files.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.21.0 — Legacy collocation cleanup & CI diagnosis (2026-11-11)
- Corrected 8 baseline FD001 collocation violations across 7 stable vocabulary records using guarded Batch 011 operations. The revised phrases keep headword-level collocation patterns and are recorded with dictionary/occupational/budgeting sources.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.20.0 — Vocabulary example readability, sense-linked POS cards & data detail fix (2026-11-11)
- Enlarged vocabulary example typography to a balanced 13.25px English sentence and 12px Vietnamese translation, with clearer line spacing and responsive sizing; also improved example text in learning references.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.19.0 — Remaining Listening/Reading second-pass review (2026-11-11)
- Completed an internal second-pass review of the 148 Listening/Reading questions outside Part 7: Listening P1=8, P2=25, P3=39, P4=30; Reading P5=30 and P6=16. Part 7's 63-question review remains recorded in v2.18.0.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.18.0 — Sidebar height adaptation & Part 7 second-pass review (2026-11-11)
- Fixed the desktop sidebar vertical layout for short laptop viewports: the sidebar uses the dynamic viewport height, the navigation area scrolls independently when space is insufficient, and the local-data/version footer remains pinned and visible.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.17.0 — TOEIC answer-position balance & progress migration safety (2026-11-11)
- Evidence audit output now derives its report filename/version from `data/manifest.json`, so future releases no longer overwrite a file named for v2.15.0.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.16.0 — Stable choice identity & CI failure isolation (2026-11-10)
- Added persistent `choiceIds` arrays to all 109 Reading questions, 102 Listening questions and 54 Grammar exercises (265 question/exercise sets). IDs are scoped to the stable parent resource/question position and remain paired with their option when choices are deliberately reo…
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.15.1 — Reading/Grammar runtime hotfix & CI runner maintenance (2026-11-10)
- Fixed the `ReferenceError: item is not defined` in `openReadingDetail()` by rendering each Reading choice directly from the active question's `choice` value; the function no longer references an out-of-scope `item` variable.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.15.0 — TOEIC Distractor Quality Audit & Answer-Key Safety (2026-11-10)
- Completed a question-level distractor review of 132 items: Listening Part 3 (39), Part 4 (30) and Reading Part 7 (63), covering the 126 direct/lexical evidence mappings plus six paraphrase/inference items.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.14.0 — Cross-device design system & editorial evidence traceability (2026-11-10)
- Added `assets/css/design-system.css` as the shared authority for typography, spacing/radii, control sizing, icon scale, focus feedback, touch behavior and responsive guardrails; documented the rules in `docs/DESIGN_SYSTEM.md`.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.13.0 — Editorial rationale QA & balanced TOEIC diagnostics layout (2026-11-10)
- Reworked the TOEIC Learning Diagnostics dashboard into an unboxed section heading and description, with separate Listening/Reading groups, seven independently framed Part cards, a lighter priority note and responsive tablet/mobile rules. Added visible keyboard focus and an acc…
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.12.0 — TOEIC question-pool expansion & structural content QA (2026-11-10)
- Expanded Listening to 56 units / 102 questions: Part 2=25, Part 3=39 across 13 three-question multi-speaker conversations, Part 4=30 across 10 three-question talks; Part 1 remains 8 explicitly labeled SVG illustrations.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.11.0 — TOEIC-only coverage expansion & content operations (2026-11-09)
- Scope reset: focus 100% on TOEIC Listening & Reading (7 Parts); IELTS is deferred until the TOEIC acceptance gates in `MASTER_STATUS.md` are met and the user approves the transition.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.10.2 — Lexical Audit Batch 002 & Documentation Consolidation (2026-11-09)
- Continued lexical audit from v2.10.1: added 11 US IPA transcriptions checked against Cambridge Dictionary pronunciation entries.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.10.1 — Smart Review Wait Modal, Flashcard Layout & iPhone Male Voice Priority (2026-11-09)
- Moved the post-OK auto-next countdown into a dedicated blocking wait modal with a visible countdown ring, progress bar, loading state and a manual-cancel action. The manual Next button is enabled when auto-next is off or the wait is cancelled. Wait state is restored safely aft…
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.10.0 — Smart Review, Flashcard Layout & Natural TTS (2026-11-09)
- Added a dedicated answer-review modal with correctness, chosen answer, expected answer, vocabulary meaning, word family, verb forms, examples and per-choice explanations. The modal must be acknowledged with OK before moving on.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.9.11 — IPA, Word Family & Lexical Audit Batch 001 (2026-11-09)
- Corrected 7 invalid/ambiguous IPA values, including five US rhotic transcriptions and two dual-POS IPA strings.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.9.10 — Verb Forms & Collocations (2026-11-09)
- Added 122 verb-form sets to records with at least one verbal sense; all 291 records with a verbal sense now have forms. Existing 169 form sets were preserved.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.9.9 — Definition & Example Correction (2026-11-09)
- Corrected 160 English definitions across the 928-record TOEIC vocabulary dataset.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.9.8 — Data Quality & Release Integrity (2026-11-09)
- Added a ratcheting data validator with structural errors, legacy-debt warnings, and new-regression errors keyed by rule + record ID + JSON pointer.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.9.7 — TOEIC Batch 005
- Added 118 unique TOEIC-focused headwords; total 928.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.9.6 — TOEIC Batch 004
- Added 79 TOEIC-focused entries; total vocabulary records: 810.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.9.5 — Vocabulary Batch 002 (draft)
- Added 44 unique headwords to the 612-word v2.9.3 baseline; total is now 656.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.9.3 — Vocabulary Batch 001 (draft)
- Added 35 unique headwords extending the recovered 577-word baseline.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.9.2 – Natural multi-speaker Listening
- Cải thiện nhận diện voice nữ/nam từ danh sách voice tiếng Anh mà thiết bị cung cấp.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.

## v2.9.1 – Flashcard refinement
- Bổ sung tìm kiếm chủ đề trong Flashcard.
- Chi tiết cũ đã được rút gọn; tra cứu chỉ mục và dấu vết tài liệu trong `archive/PROJECT_HISTORY.md`.
