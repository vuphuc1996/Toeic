# TOEIC App Benchmark — public feature comparison (2026-11-09)

## Method and limitations

This is a feature/positioning comparison based on official test-format pages and public product pages. Vendor feature descriptions are self-reported; they do not independently prove instructional quality, answer accuracy, audio quality or score validity. Prices and exact content counts can vary by country, subscription and app edition. This is not a hands-on usability review of every competitor.

## TOEIC format baseline

The IIBC official English site describes TOEIC Listening & Reading as 200 questions in approximately two hours: Listening about 45 minutes / 100 questions and Reading 75 minutes / 100 questions. The page specifies Part 1 photographs (6 questions), Part 5 incomplete sentences (30), Part 6 text completion (16), Part 7 single passages (29) and multiple passages (25). The Korean official TOEIC site lists Listening P1–P4 as 6/25/39/30 and Reading P5–P7 as 30/16/54. Use this as the management blueprint, and re-check before changing a test format. Sources: [IIBC — Test Format and Content](https://www.iibc-global.org/english/toeic/test/lr/about/format.html); [Official TOEIC Korea — test structure](https://exam.toeic.co.kr/common/template/viewContents.php?contentsCode=19).

## Public feature comparison

| Product | Publicly described strengths | Relative to this app | Evidence caveat |
|---|---|---|---|
| ETS / Super Prepa TOEIC official app | Official TOEIC questions and explanations; grammar lessons; ETS Global reported 600 official questions, 60 grammar lessons and 10 mock tests (5 full, 5 semi-real) in an Oct 2025 update. Another regional landing page advertises 700 questions and 80 grammar lessons. | Strongest authority for official-style question content and test-maker provenance. This app does not include ETS questions/audio and must not imply equivalence. | Official product; published counts differ across regional pages/editions, so the exact catalogue may vary. [ETS Global update](https://www.etsglobal.org/nc/en/blog/news/new-features-super-prepa-app); [ETS Global prep page](https://www.etsglobal.org/pf/en/landing-page/preparation-for-the-toeic-test). |
| Migii TOEIC | Personalized 30/60/90/160-day paths, entry assessment, vocabulary/grammar/listening/reading, mock tests, explanations and progress timeline. | This app has local/offline ownership and explicit source/patch control; Migii publicly describes a more mature guided study path and broader exercise flow. | Provider's own feature page, not independent benchmark. [Migii TOEIC](https://migii.net/vi/toeic). |
| Toey | Publicly describes TOEIC P1–4 / P5–7, 200-question mock tests, per-Part analysis, AI tutor, speaking/writing feedback, spaced-repetition flashcards and streaks. | This app now has all seven Part labels and per-Part local analytics, but its test bank is far smaller and has no AI tutor/server score analytics. | Toey's own product page; claims are not independently audited here. [Toey About](https://toey.app/about). |
| Prep / Prep AI | National AI-system registry describes TOEIC practice room, AI study plan, Teacher Bee assistant, virtual practice room and AI grading for speaking/writing. | This app is intentionally static/offline/local-first and currently has no server AI grading or personalized teacher assistant. | Registry and provider descriptions; do not compare learning outcomes directly. [Vietnam AI system registry — Prep](https://ai.dda.gov.vn/chi-tiet-he-thong-tri-tue-nhan-tao/VN-01-0000113-EDU-001-0). |
| ProTOEIC | Public site describes six modules, full 120-minute/200-question mock, predicted score, teacher Q&A, server-side answer reveal and FSRS review for wrong/bookmarked questions. | This app has a local static PWA and versioned content pipeline; ProTOEIC publicly describes more advanced mock/review/teacher features. | Provider's own claims; predicted score and FSRS quality not independently validated here. [ProTOEIC](https://protoeic.com/). |
| Voca Prep TOEIC Test 2026 | App Store listing describes timed mock tests, section practice, 30 grammar topics, daily dictation with 1,000+ lessons, accent/speed settings and wrong-answer review. | This app has voice selection and spacing controls, but lacks that breadth of dictation and full test content. | App Store developer description; catalogue/version may change. [App Store listing](https://apps.apple.com/vn/app/voca-prep-toeic-test-2026/id6745513706). |
| Quizlet Learn | Converts flashcard sets into adaptive multiple-choice, true/false and written questions; focuses practice based on past study behavior; syncs across devices. | This app has TOEIC-specific curated records and local flashcards; Quizlet has stronger general flashcard ecosystem and cross-device sync. | Official Quizlet feature page; not a TOEIC exam-format product. [Quizlet Learn](https://quizlet.com/features/learn). |

## Where the current app stands

### Competitive strengths

1. **Owner-controlled static PWA:** no app backend required for the current experience; content is local JSON; can be hosted under GitHub Pages and cached offline.
2. **Transparent data lineage:** stable word IDs, patch files, source notes, validators, quality baseline and a single Master are explicit. This is a maintainability advantage, not a claim of better pedagogy.
3. **Local privacy/control:** personal words, progress and preferences are designed to remain in IndexedDB/local storage with export/import; there is no remote learner profile service in this architecture.
4. **Custom listening voice settings:** selectable device voices, rate/pitch/volume and gaps support personal listening practice. It is still OS/browser TTS, not studio-recorded dialogue.
5. **Current TOEIC coverage:** all seven Parts are now represented, and per-Part progress/accuracy can direct the learner to weaker areas.

### Gaps versus leading specialist apps

1. **Content volume:** current library has 36 Listening questions and 77 Reading questions. This is not enough for a full 100+100 test bank; many practice repeats would appear quickly.
2. **Authenticity:** Part 1 art is original SVG illustration, not realistic photography; all synthesized listening is browser TTS, not recorded test audio. No ETS licensed questions/audio are present.
3. **Full mock engine:** no 200-question timed test, section timer, navigation/flag/review flow, multi-form test bank or validated score equating yet.
4. **Adaptive study:** per-Part local practice stats exist, but a mature spaced-repetition scheduler, daily study plan, robust wrong-answer queue and item-level weakness model remain to be completed.
5. **Cross-device sync / AI:** no server sync, AI tutor, AI speaking/writing grader or teacher/community layer. This is a deliberate consequence of static local-first architecture.
6. **Quality assurance:** data and content validators are now in CI, but remote GitHub Actions, deployed GitHub Pages, iPhone Safari, Android Chrome and real voice-pack QA still need explicit testing.

## Recommended roadmap to become a strong TOEIC L&R app

1. **Finish content integrity first:** complete sense-level vocabulary meanings, usage notes, IPA, word families and relation glosses; no synthetic fill values.
2. **Build genuine test depth:** move from 36/77 Listening/Reading questions toward complete, independently authored test forms; enforce the official per-Part blueprint.
3. **Improve Listening:** replace illustrative P1 art with photo-realistic licensed/original scenes; build broader P2–P4 conversations/talks with multiple speakers and varied accents; keep text/translations in review mode only.
4. **Improve Reading:** add realistic email/memo/notice/advertisement/schedule/order/policy/article single/double/triple passages, sentence-insertion, inference and cross-document questions.
5. **Adaptive revision:** schedule wrong answers/bookmarks with an explainable local spaced-repetition algorithm; add daily plan and mastery indicators while preserving local data export.
6. **Mock test and score reporting:** implement a 200-question timed practice test only when enough content exists. Score display must say “practice estimate”; do not claim ETS-equivalent scaling without validated equating.
7. **Release quality:** full desktop/mobile/offline/export-import test matrix; optionally consider sync/AI only as a separate architecture decision after TOEIC content gates.

## Bottom line

At v2.11.0 this app is best described as a **customizable, offline-first TOEIC study workspace with transparent content governance**, not yet a complete competitor to official or specialist TOEIC preparation platforms. Its strongest differentiator is control and traceability; its biggest gap is validated test-quality content at scale plus a full mock engine. The correct strategy is not to add IELTS now or imitate every competitor feature, but to finish TOEIC content depth, exam authenticity, adaptive revision and complete timed practice first.


## Updated public-page check (2026-11-09)

- The official IIBC format page confirms 200 questions, about 2 hours, Listening 45 minutes/100 questions and Reading 75 minutes/100 questions. Per-Part blueprint: Listening 6/25/39/30; Reading 30/16/54. ETS also states Listening audio is recorded English and Reading is self-paced within its section.
- ETS Global’s October 2025 Super Prepa update describes 600 official questions, 600 pedagogical explanations, 60 grammar lessons and 10 mock tests (5 full 2-hour/200-question and 5 semi-real). Its current regional landing page continues to advertise 10 tests.
- Toey currently advertises 3,200 ETS questions, full 200-question tests, per-Part analysis, AI tutor and adaptive study paths. Treat these as vendor statements, not verified independent quality claims.
- Voca Prep’s current App Store listing advertises 2,000+ practice questions, full timed tests, 30 grammar topics, 1,000+ dictation lessons and section-based wrong-answer review.
- Migii publicly presents 30/60/90/160-day learning paths and targeted vocabulary, grammar, listening and reading practice. ProTOEIC describes 120-minute/200-question mock tests and server-side score/answer workflows. Quizlet Learn offers adaptive formats and cross-device sync but is a general study platform, not a TOEIC exam simulator.

Sources: [IIBC official format](https://www.iibc-global.org/english/toeic/test/lr/about/format.html); [ETS L&R overview](https://www.ets.org/content/ets-org/ca/en/toeic/test-takers/about/listening-reading.html); [ETS Super Prepa update](https://www.etsglobal.org/nc/en/blog/news/new-features-super-prepa-app); [Toey](https://toey.app/en/toeic); [Voca Prep App Store](https://apps.apple.com/vn/app/voca-prep-toeic-test-2026/id6745513706); [Migii](https://migii.net/vi/toeic); [ProTOEIC](https://protoeic.com/); [Quizlet Learn](https://quizlet.com/features/learn).
