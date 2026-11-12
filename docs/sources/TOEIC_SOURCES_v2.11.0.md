# v2.11.0 — TOEIC sources and editorial method

## Official TOEIC format references

- IIBC official English site: 200 questions; Listening approximately 45 minutes / 100 questions; Reading 75 minutes / 100 questions; Part 1 photographs = 6; Part 5 = 30; Part 6 = 16; Part 7 single passages = 29, multiple passages = 25. https://www.iibc-global.org/english/toeic/test/lr/about/format.html
- Official TOEIC Korea site: Listening P1/P2/P3/P4 = 6/25/39/30; Reading P5/P6/P7 = 30/16/54; includes accent sources US/UK/Canada/Australia/New Zealand. https://exam.toeic.co.kr/common/template/viewContents.php?contentsCode=19
- ETS TOEIC L&R description: receptive workplace English, workplace conversations, announcements, business documents and multiple-choice format. https://www.ets.org/toeic/about/faq/product-specific-faq/toeic-listening-reading.html

These format references are for blueprints and metadata only. The application does not copy ETS test questions, official sample passages, directions or ETS audio. All new v2.11.0 listening/reading/grammar content is original editorial practice material.

## IPA values added in Batch 001

| Headword / ID | US IPA | Reference |
|---|---|---|
| allowance / `allowance-n` | /əˈlaʊ.əns/ | https://dictionary.cambridge.org/dictionary/english/allowance |
| annually / `annually-adv` | /ˈæn.ju.ə.li/ | https://dictionary.cambridge.org/dictionary/english/annually |
| appoint / `appoint-v` | /əˈpɔɪnt/ | https://dictionary.cambridge.org/dictionary/english/appoint |
| approval / `approval-n` | /əˈpruː.vəl/ | https://dictionary.cambridge.org/dictionary/english/approval |
| asset / `asset-n` | /ˈæs.et/ | https://dictionary.cambridge.org/dictionary/english/asset |
| availability / `availability-n` | /əˌveɪ.ləˈbɪl.ə.t̬i/ | https://dictionary.cambridge.org/dictionary/english/availability |

The `annual` headword already had an IPA value and was not changed. IPA is stored for the US accent in this batch; do not infer UK IPA from the US field.

## New original learning content

- Listening Part 1 uses eight custom SVG illustrations. They are labelled as illustrations; they are not photographs and not ETS assets. Browser `SpeechSynthesis` supplies synthesized audio; voice availability depends on the user's operating system/browser.
- Listening P2–P4 additions and Reading P5–P7 additions are authored as original practice content in Vietnamese/English. No official ETS question, audio or sample passage has been embedded.
- Correct answer rationale and distractor explanation are stored with each question and checked by `tools/validate-learning-content.py`. This validator checks structure and presence, not full semantic correctness; editorial review is still required.

## Competitive research sources

See `docs/reports/TOEIC_APP_BENCHMARK_2026.md` for a feature-by-feature summary and the following public sources:
- ETS Global Super Prepa app update (Oct 2025): https://www.etsglobal.org/nc/en/blog/news/new-features-super-prepa-app
- ETS Global preparation page: https://www.etsglobal.org/pf/en/landing-page/preparation-for-the-toeic-test
- Migii TOEIC: https://migii.net/vi/toeic
- Toey: https://toey.app/about
- Vietnam National AI system registry — Prep: https://ai.dda.gov.vn/chi-tiet-he-thong-tri-tue-nhan-tao/VN-01-0000113-EDU-001-0
- ProTOEIC: https://protoeic.com/
- Voca Prep TOEIC Test 2026 App Store listing: https://apps.apple.com/vn/app/voca-prep-toeic-test-2026/id6745513706
- Quizlet Learn: https://quizlet.com/features/learn

Vendor pages describe their own features. They are not independent audits of question quality, score prediction validity or learner outcomes.
