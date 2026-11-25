# Cross-module consistency and data-quality audit — v2.95.53

Date: 2026-11-24  
Scope: complete static source tree, canonical data, module resource maps, question banks, relationship graph, design tokens and responsive layouts. This is an inventory/consistency audit; it does not claim editorial approval or learner mastery.

## Executive result

- **No structural data error or broken local reference was found by the current validators.**
- Vocabulary inventory: **1,141 records**; canonical ID set unchanged (`adccbdb4c9887220…`); 0 added IDs / 0 removed IDs; validator reports 0 ERROR / 0 WARNING.
- Related Glossary: **567 rows / 567 unique normalized terms**; 0 duplicate rows.
- Vocabulary relationship graph: **1,037 relation references**, 0 malformed items, 0 self-references, 0 duplicate normalized headwords.
- Repository integrity preflight: **429 local references/data files inspected; 0 errors; 0 optional warnings**.
- Learning content validation: **0 errors / 0 warnings**.
- Objective resource map: **379/379 records linked** across 11 objectives.
- Design-token ratchet: **0 new violations**; 2 legacy findings resolved during this audit. 2,776 existing legacy findings remain warnings and are not newly introduced by v2.95.53.

## Cross-module alignment

| Domain | Current inventory | Audit result | Interpretation |
|---|---:|---|---|
| Canonical vocabulary | 1,141 headwords | PASS | IDs and manifest count align; no duplicate normalized headwords |
| Related Glossary | 567 terms | PASS for identity | 567 unique normalized terms; no duplicate rows |
| Synonym/antonym graph | 1,037 edges | Review queue | 556/804 unique targets covered; 248 unique targets / 249 references remain uncovered |
| Listening | 145 units / 295 questions | PASS structure | 102 eligible; 193 reserve questions still await independent review |
| Reading | 73 units / 287 questions | PASS structure | 52 Part 7 resources; single/multiple passage mix 110/85 questions |
| Grammar | 58 lessons / 169 exercises | PASS structure | Part 5 tags 31 lessons / 108 exercises; Part 6 tags 16 lessons / 51 exercises |
| Separate Part 5 practice | 80 questions | PASS structure | Practice-only; pending independent editorial review; not counted as Mock eligibility |
| Question evidence | 582 Listening + Reading questions | Indexed | Every correct answer is mapped to transcript/passage or a review category; evidence mapping is not proof of distractor uniqueness |
| Learning outcomes | 11 objectives / 33 criteria | Partial instrumentation | 6/33 have evidence-collection paths; 27 remain criteria-only |
| Objective resources | 379 links | PASS | 379/379 resource records linked to objectives |

## Confirmed review debt (not structural validator errors)

### 1. Related Glossary quality

- 131 entries have no English definition.
- 63 entries still contain placeholder English definitions.
- 190 entries have no POS.
- 65 entries have no source provenance.
- 198 entries have one or more quality flags (194 high / 2 medium / 2 low). Counts overlap; they must not be added together as separate records.
- 248 unique relation targets (249 reference occurrences) are not represented in the Related Glossary. The graph audit reports 673 relation references absent from canonical headwords; 424 are covered by the glossary and 249 remain unresolved.
- Do not automatically create glossary rows or copy a canonical definition without sense-level editorial review.

### 2. Vocabulary definition and CEFR review

The validator reports four exact English-definition repeats across distinct headwords:

| Headwords | Shared definition | Audit interpretation |
|---|---|---|
| annual / yearly | happening once every year | Synonym pair; review whether shared paraphrase is acceptable |
| considerable / substantial | large in amount, size, or importance | Near-synonym pair; review sense alignment |
| personnel / staff | the people who work for an organization | Synonym pair; review whether shared paraphrase is acceptable |
| shareholder / stockholder | a person or organization that owns shares in a company | Variant/synonym pair; review sense alignment |

These are not duplicate vocabulary records or duplicate IDs. No row was deleted.

Nine headwords have a word-level CEFR value that differs from at least one sense-level value:

- `bill`: word A1; verb sense A2.
- `document`: word A2; verb sense B1.
- `experience`: word A2; one noun sense B1.
- `host`: word A2; noun/verb senses B2.
- `minute`: word A1; meeting-minutes noun sense B2.
- `offer`: word A1; one verb sense B1.
- `package`: word B1; noun sense A2.
- `supply`: word A2; noun/verb senses B2.
- `value`: word A2; verb senses B2.

These may be intentional aggregate-word versus sense-specific CEFR distinctions, but the project does not yet state a single policy that makes the relationship explicit. Keep the sense levels intact until the aggregate-level rule is approved; do not flatten them automatically.

### 3. Vocabulary field coverage

| Field | Records | Coverage |
|---|---:|---:|
| US IPA | 1,062 / 1,141 | 93.1% |
| Word family | 276 / 1,141 | 24.2% |
| Verb forms | 329 / 1,141 | 28.8% |
| Collocations | 971 / 1,141 | 85.1% |
| Synonyms | 405 / 1,141 | 35.5% |
| Antonyms | 210 / 1,141 | 18.4% |

79 vocabulary records still lack US IPA. Low word-family, verb-form, synonym and antonym coverage is a content-completeness opportunity, not proof of invalid records.

### 4. Relationship graph review

- Non-reciprocal references: 248. These are review flags, not automatic errors: sense-specific synonym/antonym relationships can intentionally be asymmetric.
- Self-references: 0.
- Malformed relation items: 0.
- Duplicate normalized canonical headwords: 0.
- Unresolved relation targets: 248 unique terms / 249 occurrences.

### 5. Learning outcome instrumentation

- 6/33 criteria are wired to evidence collection (2 practice evidence, 2 learner self-report, 2 delayed recall).
- 27/33 criteria are defined but not instrumented.
- Do not display these 27 criteria as measured skills or mastery. Resource linking is complete, but evidence collection is not.

### 6. Listening and question editorial status

- Listening readiness: 102 eligible; 193 reserve-pending-independent-review.
- The 193 reserve items have traceability pointers, but that does not approve answer uniqueness or Mock use.
- Distractor structural audit covers 264 questions (Listening Part 3/4 and Reading Part 7): four distinct options and valid answer keys pass. Twelve distractor revisions are recorded. Semantic uniqueness and second-person review remain separate gates.
- The separate 80-question Part 5 Sentence Completion set remains practice-only and pending independent review.

### 7. Design-system consistency

- New iPad portrait rules use the existing five-item mobile navigation and shared design tokens.
- Design-token ratchet reports 0 new violations. 2,776 existing legacy findings remain warnings; the current change did not add new raw font-size, font-weight, box-shadow, breakpoint or `!important` violations.
- Current profile adds the 834px iPad validation viewport and names the 850px tablet-portrait upper boundary. No separate mockup or image-only design was introduced: screenshots in `visual-evidence/v2.95.53/` are rendered from the actual source HTML and CSS.

### 8. Release-evidence fingerprint scope (fixed in this candidate)

The audit found that generated Python shard reports, cross-module/iPad acceptance reports and rendered viewport evidence were not all excluded from the source/test-input fingerprint. This could make a resumable test checkpoint appear stale after the runner wrote its own evidence, even though application source and tests had not changed.

- Added explicit generated-evidence patterns for Python shard reports, cross-module/iPad reports, Related Glossary audit/queue snapshots and rendered visual evidence.
- These files remain included in FullSource and are protected by ZIP CRC and archive SHA-256; they are excluded only from source/test-input fingerprints to prevent self-referential checkpoint invalidation.
- Governance/source documents remain fingerprinted; the regression test confirms an `EDITORIAL_POLICY.md` change still changes the fingerprint.
- Post-fix regressions: `test_test_fingerprints.py` 10/10 PASS; `test_python_test_shard_runner.py` 19/19 PASS; `test_release_acceptance_runner.py` 10/10 PASS.

## Responsive layout verification

- iPad Pro 11-inch M1 portrait simulation: 834 × 1194 CSS px; sidebar hidden; main margin-left 0; five-column fixed bottom nav visible; no horizontal document overflow.
- iPad Pro 11-inch M1 landscape simulation: 1194 × 834 CSS px; 216px desktop sidebar visible; bottom nav hidden; no horizontal document overflow.
- Additional viewports: iPhone 390 × 844, tablet portrait 768 × 1024, desktop 1440 × 900.
- All 11 page sections were activated in turn at four viewport profiles: **44/44 page-layout checks, 0 horizontal page overflows**.
- The browser simulation uses the real source HTML and both source stylesheets. Scripts were intentionally stripped for deterministic CSS/DOM geometry, so dynamic data loading and actual device touch behavior remain separate acceptance steps.

## Release decision

**Source/data consistency: PASS WITH REVIEW DEBT.** No structural data error, duplicate canonical identity, broken resource link, malformed relation, or new design-token violation was found. The review debt listed above remains explicit and must not be described as completed. Physical iPad Safari acceptance, hosted GitHub Actions, GitHub Pages deployment, PWA cache propagation and offline behavior remain unverified in this environment.
