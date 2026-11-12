# TOEIC sources and editorial method — v2.12.0

## Official exam blueprint references

The following public references are used to confirm the TOEIC Listening & Reading section lengths and question distribution. They are not sources from which practice questions, passages or audio are copied.

- **ETS — TOEIC Listening and Reading FAQ:** describes a 200-question test, 100 Listening questions (approximately 45 minutes) and 100 Reading questions (75 minutes). https://www.ets.org/toeic/about/faq/product-specific-faq/toeic-listening-reading.html
- **IIBC — TOEIC Listening & Reading Test (English):** official test overview and section structure, including 45-minute Listening and 75-minute Reading. https://www.iibc-global.org/english/toeic/test/lr/about.html
- **Official TOEIC Korea — Test composition:** Part-level distribution Listening P1/P2/P3/P4 = 6/25/39/30; Reading P5/P6/P7 = 30/16/54, with Part 7 split 29 single-passage and 25 multiple-passage questions. It also describes accents used in listening. https://exam.toeic.co.kr/common/template/viewContents.php?contentsCode=19

## v2.12.0 original editorial content

All new material in this batch is authored as original TOEIC-style practice for workplace and everyday contexts. No ETS official question, official sample passage, test-form scan, or ETS audio is embedded. The official sources above are used for blueprint metadata only.

- Listening Part 2: short original prompts with three plausible response choices and one best answer.
- Listening Part 3: original multi-speaker workplace conversations with three linked questions per set. Speaker identities are explicit in segments.
- Listening Part 4: original short talks/announcements with three linked questions per set.
- Reading Part 5/6: original incomplete-sentence and text-completion practice.
- Reading Part 7: original email/order/reimbursement/meeting/facility documents; double/triple records expose each source document separately for cross-document reasoning.

## Content validation boundary

`tools/validate-learning-content.py` checks unique resource IDs, valid question choice counts and answer indexes, non-empty prompts/rationales, part distributions, Part 2/3/4 structural rules, Part 3 speaker count, image existence/labels, Part 6 blank counts, and structured Part 7 double/triple documents. Passing it does **not** prove that every answer is semantically correct or that distractors are sufficiently difficult. Manual editorial review is still required.

## Media provenance

- Part 1 SVG artwork is original vector illustration. It must be shown as illustration, not described as a photograph.
- Browser SpeechSynthesis is generated on-device/browser and depends on installed voices; it is not a recording and not official ETS audio.
- Any future licensed photograph or recorded audio must carry source/permission metadata and pass offline resource verification before inclusion.

## TOEIC vocabulary provenance

The 928-headword vocabulary and verified lexical fields are carried over unchanged from v2.11.0. v2.12.0 does not add headwords or alter IPA/CEFR/word-family/verb-form/synonym/antonym/collocation values. See `TOEIC_SOURCES_v2.11.0.md` for prior IPA source entries and editorial policy.
