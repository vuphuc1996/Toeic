# Related Glossary Batch 036 — v2.95.43

## Scope

Add 11 previously unglossed synonym/antonym relation targets. They are lookup entries only, not canonical A–Z headwords. The batch is alphabetical A–C and has a guarded additive patch, ledger, six tests, CI registration, and refreshed glossary/progress audits.

| Term | Vietnamese gloss | POS | English paraphrase | Cambridge source |
|---|---|---|---|---|
| able | có thể; đủ khả năng hoặc điều kiện để làm việc gì | adj | having the strength, skill, time, money, or opportunity needed to do something; also skilled at what one does | [Cambridge](https://dictionary.cambridge.org/dictionary/english/able) |
| accuracy | độ chính xác; tính đúng đắn | n | the quality of being exact or correct, or the ability to do something without mistakes | [Cambridge](https://dictionary.cambridge.org/dictionary/english/accuracy) |
| actual | thực tế; có thật; đúng thực tế | adj | existing in fact or real, rather than imagined, expected, or planned | [Cambridge](https://dictionary.cambridge.org/dictionary/english/actual) |
| assume | cho rằng (chưa có chứng cứ); đảm nhận | v | to accept something as true without proof, or to take on responsibility or control | [Cambridge](https://dictionary.cambridge.org/dictionary/english/assume) |
| business | kinh doanh; hoạt động thương mại; doanh nghiệp | n | the activity of buying and selling goods or services, or an organization that does this | [Cambridge](https://dictionary.cambridge.org/dictionary/english/business) |
| caller | người gọi điện (đến) | n | a person who makes a telephone call | [Cambridge](https://dictionary.cambridge.org/dictionary/english/caller) |
| capable | có năng lực; có khả năng | adj | able to do something effectively and skillfully or to achieve results | [Cambridge](https://dictionary.cambridge.org/dictionary/english/capable) |
| car | xe ô tô | n | a road vehicle with an engine, usually four wheels, and seats for a small number of people | [Cambridge](https://dictionary.cambridge.org/dictionary/english/car) |
| carry | mang; vận chuyển; chở | v | to hold or move a person or thing from one place to another | [Cambridge](https://dictionary.cambridge.org/dictionary/english/carry) |
| choice | sự lựa chọn; quyền lựa chọn; các lựa chọn | n | the act or possibility of choosing, or a range of things available to choose from | [Cambridge](https://dictionary.cambridge.org/dictionary/english/choice) |
| company | công ty; doanh nghiệp | n | an organization that sells goods or services in order to make money | [Cambridge](https://dictionary.cambridge.org/dictionary/english/company) |

## Research and provenance

- Cambridge Dictionary indexed search-result excerpts were reviewed on **2026-11-23**.
- Direct fetches of all 11 Cambridge pages returned **HTTP 403** in this environment. This batch therefore records paraphrases of indexed excerpts and retained exact source URLs, not direct full-page inspection.
- No Cambridge examples copied. English definitions are concise paraphrases. Vietnamese glosses are curated for the relation-target context.
- Independent lexical/translation review is still pending; these entries are not marked editorially approved.

## Coverage impact

- Related Glossary rows: **535 → 546**.
- Normalized unique rows: **546**; duplicates: **0**.
- Exact relation target join: **524/804 → 535/804 (65.2% → 66.5%)**.
- Missing unique targets: **280 → 269**.
- Missing relation occurrences: **281 → 270**.
- English definitions: **312 → 323 present; 150 missing; 73 placeholder definitions unchanged**.
- All 11 terms were confirmed to appear in canonical synonym/antonym arrays and to be absent from canonical A–Z headwords.

## Integrity and regression changes

- Additive patch is base-hash guarded and refuses to overwrite existing glossary terms.
- Six Batch 036 tests check inventory/patch/ledger consistency, patch base reconstruction, row/provenance agreement, relation-target membership, Cambridge URLs and non-placeholder definitions, and SHA-256 protection for all canonical vocabulary files plus Grammar, Listening, Reading and separate Part 5 banks.
- GitHub Actions compiles and executes Batch 036; CI coverage test confirms all Python/JavaScript test files are registered.
- Batch 035 historical base-hash reconstruction now discovers later additive ledgers dynamically. Batch 027 coverage and Batch 034 historical patch tests were reconciled to the current glossary and later additive batches.

## Preservation

No canonical headword IDs/words, synonym/antonym arrays, questions, choice IDs, answer keys, Mock eligibility, learner IndexedDB records/schema, UI redesign, Robot Buddy permissions, backend or deployment configuration changed.

## Verification

- Batch 036: **6/6 PASS**.
- Batch 035: **5/5 PASS**.
- All related-glossary test modules: **104/104 PASS**.
- Related-term updater: **11/11 PASS**.
- CI coverage: **3/3 PASS**.
- Major release audit tests: **8/8 PASS**.
- Related-term explanation tests: **3/3 PASS**.
- Version synchronization tests: **12/12 PASS**.
- JavaScript regressions: **39/39 suites PASS**.
- Data/content/repository/version validation: PASS (details in the release test report).
- Full Python discovery was attempted but terminated by the execution-time limit before a final aggregate summary; no full-suite PASS is claimed.
- Remote GitHub Actions, Pages deployment/cache and browser/device acceptance remain unverified.
