# Vocabulary quality review — v2.9.11 Batch 001

**Base:** v2.9.10  
**Target:** v2.9.11  
**Date:** 2026-11-09  
**Data scope:** 928 fixed headwords; no new IDs.

## Changes delivered

| Area | Operations | Result |
|---|---:|---|
| US IPA | 31 | 7 malformed entries corrected; 24 missing IPA values populated from Cambridge Dictionary |
| Word families | 49 | Coverage 74 → 122 records |
| Competitor synonyms / CEFR | 4 | `challenger`, `contender`, `rival`; CEFR A2 → B1 |
| Related-term glossary | 2 new glossary entries | 345 → 347 terms |

### IPA quality

The 7 corrected records are `buyer-n`, `consider-v`, `deliver-v`, `difference-n`, `employer-n`, `estimate-nv`, and `transfer-nv`. The 24 new transcriptions are `capacity`, `catalogue`, `certificate`, `certification`, `certify`, `circulate`, `clarify`, `clerk`, `commission`, `commodity`, `compensation`, `competitive`, `competitor`, `comply`, `authorization`, `arrangement`, `consultant`, `consultation`, `application`, `applicable`, `attendance`, `attendee`, `recruitment`, and `manufacturer`. All source URLs are listed in `SOURCES_TOEIC_Dictionary_v2.9.11.md`.

`estimate` has distinct noun and verb pronunciations. As `phonetic.us` accepts one string, the noun pronunciation is stored for the first/primary sense; POS-specific IPA remains a known schema/UI limitation.

### Word-family review

The 49 affected records form these reviewed clusters where the corresponding headwords exist: apply/applicant/application/applicable; arrange/arrangement; attendance/attendee; benefit/beneficial/beneficiary; comply/compliance; consultancy/consultant/consultation; deliver/deliverable/delivery; employee/employer/employment; manage/manager; manufacture/manufacturer; produce/product/productivity; recruit/recruitment; respond/response; supply/supplier; authorize/authorization; confirm/confirmation; coordinate/coordinator; negotiate/negotiation/negotiator; approve/approval; inspect/inspection/inspector; supervise/supervision/supervisor; compensate/compensation; certify/certification/certificate. Existing family entries were retained; duplicate target words were not added.

### Synonym and CEFR case

Cambridge marks `competitor` as B1 and lists challenger/contender/rival as synonyms. Its record CEFR and sense CEFR were both updated from A2 to B1; `data/manifest.json` was updated to A1=64, A2=227, B1=276, B2=294, C1=67. No other CEFR labels were mass-changed.

## Automated verification

- All 3 `tools/patch-data.py` batches: dry-run PASS before apply.
- Data validator after batch and baseline tightening: 928 records, 0 ERROR, 12 legacy WARNING.
- Warnings remaining: DF005=3; EX006=1; FD001=8 violations across 7 records. No IPA warnings remain.
- Coverage: IPA=563/928 (61%); word_family=122/928 (13%); verb_forms=291/928; collocations=758/928; synonym-bearing records=361; antonym-bearing records=213. IPA remains blank on 365 records pending source review.
- CEFR word/sense mismatches: 0.
- ID count and ID-set SHA-256 remain 928 and `dd1705e64c8df4ad7ebca188a6ad856fff1d180d99730d2d77d2ba6fbdc12656`.

## Remaining work / caveats

- Continue IPA source work for the 365 remaining empty entries in small batches; do not auto-generate pronunciations.
- Continue synonym/antonym verification by sense and source; 312 of 763 unique lexical relations still lack a related-term gloss.
- Continue word-family coverage and targeted CEFR checking; do not mass-classify based solely on guessed level.
- Existing DF005/EX006/FD001 legacy warnings remain open for separate editorial correction.
- This batch does not change UI, Listening TTS, Smart Review, flashcard imagery, IndexedDB or personal learning data. Those requirements stay in v2.10.0.
- GitHub Actions, Pages deployment, iPhone Safari, Android Chrome and tablet/device QA are not verified by this local build.
