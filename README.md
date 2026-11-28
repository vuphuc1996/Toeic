# TOEIC Dictionary

An offline-first, TOEIC-focused English vocabulary and practice PWA. The project is hosted on GitHub Pages and is designed to keep learner progress in the browser rather than depend on a cloud account or application backend.

**Open the candidate app:** https://vuphuc1996.github.io/Toeic/

## What the app includes

- Searchable TOEIC vocabulary, word details, related terms and examples.
- Flashcards, grammar practice and guided learning paths for beginners.
- Listening and Reading practice organized around the seven TOEIC parts.
- TOEIC mock-exam modes with a final result and post-test review.
- Local learning-progress and objective-evidence tracking.
- Robot Buddy, which operates within the app's local/offline boundary.

## Architecture and data protection

- Static GitHub Pages delivery with a service worker for PWA caching.
- Learner records remain in browser IndexedDB; the current learner-data schema is IndexedDB v1.
- No Cloudflare Worker, D1 database, hosted AI chatbot or external API key is required for the GitHub Pages learning experience.
- Vocabulary identities, question/choice IDs and answer keys are treated as canonical data and must not be silently rewritten.
- Listening/Reading reserve and review-only pools remain excluded from Mock until their stated review gates are satisfied.

## Current candidate status

| Item | Current state |
| --- | --- |
| Application version | **v2.95.86** |
| Development branch | `candidate` |
| Latest candidate HEAD | `41b34ba73deb4178c413653027aeda9987f5941a` |
| Validated application/source snapshot | `d5cefa69610bc381a802127d5f9f000d88e48df8` |
| GitHub Validate on latest HEAD | **PASS** — [run 46137721113](https://github.com/vuphuc1996/Toeic/actions/runs/46137721113) |
| GitHub Pages build/deployment on latest HEAD | **PASS** — [run 46137720680](https://github.com/vuphuc1996/Toeic/actions/runs/46137720680) |
| Production promotion | **Not accepted** — `main` remains protected and has not been updated |

The v2.95.86 candidate contains Part 1 Batch 018 additions. The three newly added photo-description resources are still marked `reserve-pending-independent-review`; they are not approved for Mock. The release inventory reports 148 Listening resources / 311 questions, with 102 approved Listening questions and 196 reserve questions. Reading Mock-eligible content remains 200 questions, while the 87-question Part 7 reserve and 80-question separate Part 5 review-only pool remain excluded.

The provisional weighted curriculum-build index is **77.16%**. This is a content/instrumentation build indicator, not learner mastery, an estimated TOEIC score, or a claim that the entire product is complete.

## Verification boundaries

Candidate CI and the Pages build/deployment are passing for the current candidate revision. The following remain separate gates and must not be reported as complete until actually verified:

- FullSource ZIP generation, checksum and replay verification.
- Installed-PWA cache propagation and offline behavior after an update.
- Physical-device QA across supported phone, tablet and desktop sizes.
- Production acceptance and promotion from `candidate` to `main`.

## Project documentation

- [Project documentation](docs/README.md)
- [Master status and release history](docs/MASTER_STATUS.md)
- [Current version ledger](docs/versions/CURRENT_VERSION.md)
- [Changelog](docs/CHANGELOG.md)
- [Assessment and review semantics](docs/ASSESSMENT_FLOW.md)

## Local development

Node.js is required for the repository's local development and validation utilities.

```bash
npm install
npm run dev
```

The local development server is not required for the deployed GitHub Pages app. Do not add secrets or a Gemini API key for normal TOEIC Dictionary use.
