# Robot Buddy v2.84.1 — Learning Insights & Knowledge Expansion

## Product identity

Robot Buddy is a head-only animated companion for TOEIC Dictionary, created by developer **Vũ Nguyễn Hoàng Phúc**. It uses a bundled, offline scripted dialogue library and local keyword intent matching. It is not a generative AI chatbot and does not claim unrestricted natural-language understanding.

## Content coverage

- 500 unique authored dialogue variants across seven groups: greeting 60, encouragement 100, caring 60, learning 80, help 100, reaction 60, rest 40.
- 59 feature-help messages for 12 destinations: Trang chủ, Lộ trình học, Từ vựng, Ôn tập, Thi thử TOEIC, Flashcard từ vựng, Ngữ pháp, Đọc hiểu, Nghe, Cấu hình, Quản lý dữ liệu and Placement.
- Six local FAQs and 16 quick prompts.
- The Trang chủ guide explains that overview statistics and learning shortcuts are presented on the dashboard; Statistics is not a separate navigation item in this release.

## Learning Insights

The app passes an in-memory snapshot of its already-loaded local stores to `assets/js/robot-learning-insights.js`. The module is pure/read-only: it does not open IndexedDB, read LocalStorage, write records or migrate data.

| Category | Evidence rule |
|---|---|
| Cần học | Vocabulary/Flashcard words with no recorded study repetition; learning units with no recorded completion evidence |
| Cần luyện | Vocabulary with at least 3 recorded reviews and weak accuracy/negative balance; Flashcard only after at least 3 quiz answers and weak accuracy; Grammar/Reading/Listening after at least 5 answered questions and accuracy below 70%; Foundation after at least 3 unique evidence items and accuracy below 80%; completed Mock results below the internal 75% practice threshold |
| Cần ôn | Vocabulary and Flashcard due dates have passed; Objective recall or Foundation recall timestamps are due |

Robot returns up to five concrete item names per category so the learner can see examples, not only totals. Small samples are not labelled as weak skills. For Grammar/Reading/Listening, fewer than five answered questions are reported as insufficient evidence. Internal thresholds are practice guidance, not ETS score, CEFR certification or proof of mastery.

## Privacy and control

- Progress analysis is enabled by default for this release and can be switched off in the Robot header.
- When disabled, Robot still supports greetings, FAQ, menu guidance and feature navigation.
- No learner progress is sent to an API, backend, server, Google AI or third party.
- Robot does not open IndexedDB or LocalStorage itself. Existing local stores are read by the main app as before and passed as object references for in-memory analysis only.
- Conversation history is not persisted. Robot preferences are stored only under `toeic:robot-buddy-settings:v1`.

## Preservation and runtime

- IndexedDB schema remains version 1.
- Existing progress keys and record formats remain unchanged.
- Service Worker `REQUIRED` and `APP_SHELL` include `robot-learning-insights.js`.
- Idle prompts retain the existing safeguards; when insights are enabled, an idle prompt may mention due-review or practice counts derived from local evidence.
- No changes to vocabulary content, learning banks, TTS, Placement scoring, Mock Exam engine or legacy user-triggered Google AI entry points.
