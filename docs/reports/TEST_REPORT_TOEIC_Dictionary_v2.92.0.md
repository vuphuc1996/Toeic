# Test Report — TOEIC Dictionary v2.92.0

## Release scope

This is a consolidated content release built on v2.91.0. It adds 20 resources and 69 new questions/exercises:

1. **Grammar:** 8 lessons / 24 exercises covering conditionals, reported speech, comparisons, countability/quantifiers, gerunds/infinitives, passive voice, relative clauses and time/deadline prepositions.
2. **Listening:** 6 units / 18 questions (3 Part 3 conversations and 3 Part 4 talks), each with Vietnamese transcript translation, Vietnamese answer rationale, four unique options and exact transcript evidence.
3. **Reading:** 6 Part 7 resources / 27 questions: 3 single-passage resources with 4 questions each, plus 3 double-passage resources with 5 questions each. Each has a Vietnamese translation, Vietnamese rationales, four unique options and source-label/quote evidence.
4. **Foundation planning:** a 12-unit, four-skill B1 curriculum blueprint with measurable outcomes and review gates. B1 is not exposed as a selectable learner pathway in this release.
5. **Governance:** batch SHA-256 registry, expanded regression tests, CI registration, objective-resource mapping, item-level independent-review checklist and updated Master/roadmap/progress/coverage reports.

## Updated canonical inventory

| Library | Before v2.92.0 | After v2.92.0 | New in this release |
|---|---:|---:|---:|
| Grammar | 33 lessons / 86 exercises | 41 lessons / 110 exercises | 8 lessons / 24 exercises |
| Listening | 107 units / 201 questions | 113 units / 219 questions | 6 units / 18 questions |
| Reading | 51 resources / 200 questions | 57 resources / 227 questions | 6 resources / 27 questions |

No approved total target exists for these three libraries, so no completion percentage is claimed. Vocabulary remains unchanged at 1,137 headwords.

## Local verification results

| Check | Result | Notes |
|---|---|---|
| JavaScript regression suites | PASS 32/32 | Every `tools/tests/*.mjs` suite executed, including Mock eligibility checks for the new Reading reserve |
| Selected Python tests | PASS 93/93 | 12 focused modules: content batch 024, learning content, Reading expansion, Grammar expansion, objective map, project progress, CI coverage, answer-position balance, distractor quality, editorial review, Listening expansion and A2 assessment quality |
| Python syntax compilation | PASS 69/69 | All Python files under `tools/` compiled |
| JavaScript syntax | PASS | `sw.js`, `assets/js/app.js` and all `assets/js/*.js` modules |
| Vocabulary validator | PASS | 1,137 records; 0 new errors / 0 new warnings (legacy baseline remains documented) |
| Learning-content validator | PASS | Listening 113/219; Reading 57/227; Grammar 41/110; 0 errors / 0 warnings |
| Batch 024 SHA-256 registry | PASS | 8 Grammar, 6 Listening and 6 Reading resource objects match their registered fingerprints |
| Batch 024 content integrity | PASS | 24 Grammar exercises, 18 Listening questions, 27 Reading questions; stable IDs, four-choice keys, source evidence and translations validated |
| Reading Part 7 answer positions | PASS | Batch 024 A/B/C/D = 7/7/7/6; all three double-passage sets contain five questions |
| Mock exclusion boundary | PASS | 117 pending Listening questions and 27 pending Reading questions are excluded from Mock; the Full form remains exactly 100 Listening + 100 Reading questions |
| Objective-resource mapping | PASS | 314/314 canonical resource records linked across 11 objectives |
| Distractor structural audit | PASS | 204-question scope; 90 pending Listening Part 3/4 questions structurally checked separately; no duplicate options or invalid answer keys |
| Learning outcome audit | PASS | 11/11 objectives; 33 criteria; 6/33 evidence-collection paths. This is not learner mastery |
| Foundation A2 assessment audit | PASS | Existing A2 core and supplementary inventories remain intact; no A2 content or progress scope changed |
| Part 1 photo validation | PASS | 9/9 assets and attribution rows |
| Design profile | PASS | 54 tokens / 400 generated typography selector groups synchronized |
| Version synchronization | PASS | All registered version markers agree at 2.92.0 |

The full Python test discovery command was attempted but did not finish within the execution time window. It is not claimed as a full-suite pass. The 92 selected tests above completed successfully.

## Content and editorial boundary

- All six new Listening units and six new Reading resources are `reserve-pending-independent-review`. They remain available for normal practice but are excluded from Mock until a second reviewer records item-level approval.
- The original 99 pending Listening questions remain unchanged; v2.92.0 adds 18, bringing the pending Listening reserve inventory to 117. The 102-question Mock-eligible Listening pool is unchanged.
- The new 27 Reading questions remain pending and Mock-excluded; the pre-existing 200-question eligible Reading inventory is unchanged.
- The 24 Grammar exercises are newly authored practice content. Automated validation confirms structure and answer-key consistency, not independent linguistic quality or psychometric validity.
- The B1 blueprint is design documentation only. No B1 lesson content or selectable B1 pathway is shipped.
- The SHA-256 registry protects the complete objects in batch 024; it does not constitute editorial approval.

## Preservation

- No vocabulary record or stable legacy question ID was modified.
- No existing learner progress was reset, migrated, overwritten or deleted.
- IndexedDB remains schema v1. Existing localStorage keys, Foundation A2 scopes, Mock history and settings are unchanged.
- No backend, API, server-side learning store or learner-data transfer was added.
- Existing Service Worker data resources were already in `REQUIRED` and `APP_SHELL`; only the release cache version was advanced to 2.92.0.

## Not verified / acceptance still pending

- Remote GitHub Actions run, GitHub Pages deployment and production cache behavior.
- Live browser visual QA at desktop 15.6-inch / 100% zoom, mobile, iOS, Android and landscape.
- Physical-device TTS voice quality, pause perception, offline/reconnect and cache refresh.
- Independent second-person editorial review of new batch 024 content and existing reserve banks.
- Learner validation of the Foundation pathway and newly expanded TOEIC resources.
- Full Python test discovery.

A local source release is not a claim of production deployment or final academic acceptance.
