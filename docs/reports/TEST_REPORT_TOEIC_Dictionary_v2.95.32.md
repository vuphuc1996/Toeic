# Test Report — TOEIC Dictionary v2.95.32


## Quality-control closure before the major patch
- Python discovery after major patch: **587/587 PASS**. Baseline QC closure separately passed 580/580 on v2.95.31 after correcting stale assertions tied to glossary/IPA metrics.
- JavaScript regression suites: **39/39 PASS**.
- Vocabulary validator on v2.95.31: 1,141 canonical records; 0 errors, 0 warnings.
- Learning-content validator on baseline: 0 errors, 0 warnings.
- Repository-integrity preflight: 405 references inspected; 0 errors / 0 optional warnings.

## Major batch 026
- Grammar: 8 lessons / 32 exercises.
- Listening: 8 units / 24 questions (4 Part 3 conversations, 4 Part 4 talks).
- Reading: 8 single-passage Part 7 resources / 24 questions; passages 75–94 words.
- Total content addition: 24 resources / 80 exercises and questions.
- New answer-position distribution is balanced: Grammar 8 each A–D; Listening 6 each; Reading 6 each.
- Batch-specific tests: 6/6 PASS; exact transcript/passage evidence and batch file SHA-256s verified.
- Listening and Reading are original-editorial practice content; reserve-pending-independent-review and excluded from Mock eligibility.
- New content mapped to learning objectives; objective-resource audit: 363/363 links PASS.
- Mock engine regression: 161 Listening and 87 Reading Part 7 reserve questions excluded.

## Post-batch validators
- Learning content: 0 errors / 0 warnings; Listening 129 units / 263 questions; Reading 73 resources / 287 questions; Grammar 58 lessons / 169 exercises.
- Vocabulary validator: PASS (1,141 records; 0 errors / 0 warnings; legacy baseline marker retained).
- Repository integrity: 405 local references; 0 errors / 0 optional warnings.
- Question evidence report: 550 questions indexed; categories reflect current source.
- Independent-review queue: 328 item-level decisions (161 Listening + 87 Reading Part 7 + 80 Part 5).

## Release packaging verification
- FullSource: 512 files.
- Update Patch: 39 overlay files; 0 deletions.
- Patch replay on v2.95.31: 512/512 files byte-for-byte identical to v2.95.32 FullSource.
- ZIP CRC and SHA-256 checks: PASS.

## Not verified
- Remote GitHub Actions, Pages deployment, browser/device acceptance.
