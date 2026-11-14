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

## Where the current app stands — v2.36.0 (internal inventory checked 2026-11-14)

### Competitive strengths

1. **Owner-controlled static PWA:** no app backend is needed for the current experience; canonical content is local JSON; GitHub Pages hosting and a versioned Service Worker provide the intended deployment model.
2. **Transparent content governance:** stable word/question/choice IDs, patch tooling, validators, editorial states, a quality baseline and a single Master make content changes traceable.
3. **Local-first learning data:** study progress, preferences and practice history are stored on the device in IndexedDB. The project does not provide server-side cross-device learner sync.
4. **Multi-module practice:** the app includes Vocabulary, Listening, Reading, Grammar and Flashcards, with Retry/Attempt History and a shared Focus Workspace.
5. **Mock exam workflow:** Quick 25-question, Half 100-question and Full 200-question modes have section timing, question navigation, flag/review and local results. Reading currently supports two Full forms without repeated eligible question IDs.
6. **Custom listening playback:** device voice selection, accent, rate, pitch, volume, word pauses and speaker-turn pauses are available. This is browser/OS SpeechSynthesis, not studio-recorded TOEIC audio.

### Current catalogue and limitations

| Area | Current inventory | Important qualification |
|---|---:|---|
| Vocabulary | 992 headwords | Quality-controlled growth remains in progress; 3,000–5,000 is an internal target, not a completion claim |
| Listening | 200 questions / 106 units | Only 102 are Mock-eligible; 98 remain reserve-pending-independent-review |
| Reading | 200 questions / 51 resources | Local inventory supports two non-overlapping Full forms; semantic second review remains separate |
| Grammar | 33 lessons / 86 exercises | Part metadata supports the TOEIC-focused Grammar library |
| Mock | 15m/25Q · 60m/100Q · 120m/200Q | Results show raw correct-count and accuracy, not ETS-equated 5–495 / 10–990 estimates |
| Part 1 photos | 8 referenced Pexels photos + 8 SVG fallbacks | The supplied source snapshot omits the 8 original user-owned JPG bytes; preserve the repository originals. Four more distinct photo items are required for two zero-repeat Full Listening forms after reserve approval. |

### Important quality boundaries

- The 98 Listening reserve questions remain practice-only until a second independent reviewer records a decision. Automated schema, evidence and distractor checks do not replace that review.
- Current eligible Listening inventory can form one Full Listening section. A second currently repeats 98/100 IDs. After the 98 reserves are approved, four new Part 1 photo-description items are still required to make two non-overlapping forms.
- Part 1 SVG fallbacks protect display when a photo is unavailable; they do not satisfy the strict photograph-binary gate.
- SpeechSynthesis voice quality depends on installed browser/OS voice packs. The app can prefer a clearer voice and adjust pacing, but cannot provide a missing voice or claim native/studio audio.
- The app has not been validated as an ETS-equivalent score predictor. ETS score conversion uses form-specific equating; this app deliberately reports raw practice accuracy only.
- Static PWA/source checks do not prove remote GitHub Pages deployment, offline/reconnect behavior or physical-device display/voice quality.

## Development roadmap — active work, not acceptance checklist

1. **Close Listening content quality:** complete the independent second-person review of Batch 013/014/015 and correct any answer, evidence or distractor issue before approving whole units for Mock.
2. **Build the second Listening form:** add four distinct Part 1 photo-description items with their own original/licensed photo assets, while preserving the eight user-owned existing JPGs.
3. **Improve Reading content reliability:** finish semantic review of the 200-question bank, focusing on Part 7 cross-document and inference items where distractor plausibility is most difficult.
4. **Scale Vocabulary with quality gates:** improve sense-level meanings, examples/translations, source-backed IPA, word families, verb forms and relation glosses before accelerating growth toward the internal 3,000–5,000 target.
5. **Strengthen revision loops:** continue developing weak-answer routing and explainable local review scheduling without resetting local progress or introducing duplicate learning stores.
6. **Maintain PWA/runtime reliability:** focus fixes on asset fallback, cache version changes, navigation, saved attempts and responsive layout when code changes affect those flows.
7. **Defer final acceptance planning:** after the development backlog is closed, create one risk-weighted test plan around the highest failure-impact paths instead of repeating a full manual sweep of every stable component.

## Bottom line

At v2.36.0 this is a substantial **offline-first TOEIC learning and practice PWA** with a local 200-question Listening library, a 200-question Reading bank, Grammar exercises and a timed Mock workflow. It is not equivalent to ETS official preparation content: Listening has 98 items held out of Mock pending independent review, two zero-repeat Full Listening forms still need four more Part 1 photo items, and real deployment/device behavior is not certified by local checks. The right strategy remains to finish TOEIC content quality and runtime reliability before IELTS or server-side features.

## Reference dates and sources

The competitor feature comparison above is a public-page snapshot last checked 2026-11-09; provider claims and catalogue counts may change. The internal app inventory was checked 2026-11-14. Official TOEIC structure sources: [IIBC — Test Format and Content](https://www.iibc-global.org/english/toeic/test/lr/about/format.html); [Official TOEIC Korea — test structure](https://exam.toeic.co.kr/common/template/viewContents.php?contentsCode=19). Vendor feature pages are self-reported and do not independently establish instructional quality, answer accuracy, audio quality or score validity.
