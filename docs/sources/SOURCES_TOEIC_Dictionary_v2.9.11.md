# v2.9.11 — IPA and lexical relationship sources

Date: 2026-11-09. Primary pronunciation reference: Cambridge Dictionary US pronunciations. IPA was normalized only for spacing/format consistency; US rhotic symbols such as `ɚ`/`ɝ` and the flap mark `t̬` are retained.

## Corrected existing IPA values

| Headword | Stored US IPA | Source |
|---|---|---|
| buyer | `/ˈbaɪ.ɚ/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/buyer) |
| consider | `/kənˈsɪd.ɚ/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/consider) |
| deliver | `/dɪˈlɪv.ɚ/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/deliver) |
| difference | `/ˈdɪf.ɚ.əns/` | [Cambridge](https://dictionary.cambridge.org/pronunciation/english/difference) |
| employer | `/ɪmˈplɔɪ.ɚ/` | [Cambridge](https://dictionary.cambridge.org/pronunciation/english/employer) |
| estimate | `/ˈes.tə.mət/` (noun sense) | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/estimate) |
| transfer | `/ˈtræns.fɝː/` | [Cambridge](https://dictionary.cambridge.org/pronunciation/english/transfer) |

`estimate` is noun/verb with distinct US pronunciations (`/ˈes.tə.mət/` noun; `/ˈes.tə.meɪt/` verb). The current record schema stores only one `phonetic.us` string, so the noun form is stored because noun is the first sense. This limitation is recorded for a future POS-aware IPA schema/UI change; both forms are not concatenated into one invalid string.

## Newly populated IPA values

| Headword | Stored US IPA | Source |
|---|---|---|
| capacity | `/kəˈpæs.ə.t̬i/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/capacity) |
| catalogue | `/ˈkæt̬.ə.lɑːɡ/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/catalogue) |
| certificate | `/sɚˈtɪf.ə.kət/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/certificate) |
| certification | `/ˌsɝː.t̬ə.fɪˈkeɪ.ʃən/` | [Cambridge](https://dictionary.cambridge.org/pronunciation/english/certification) |
| certify | `/ˈsɝː.t̬ə.faɪ/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/certify) |
| circulate | `/ˈsɝː.kjə.leɪt/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/circulate) |
| clarify | `/ˈkler.ə.faɪ/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/clarify) |
| clerk | `/klɝːk/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/clerk) |
| commission | `/kəˈmɪʃ.ən/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/commission) |
| commodity | `/kəˈmɑː.də.t̬i/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/commodity) |
| compensation | `/ˌkɑːm.penˈseɪ.ʃən/` | [Cambridge](https://dictionary.cambridge.org/pronunciation/english/compensation) |
| competitive | `/kəmˈpet̬.ə.t̬ɪv/` | [Cambridge](https://dictionary.cambridge.org/pronunciation/english/competitive) |
| competitor | `/kəmˈpet̬.ə.t̬ɚ/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/competitor) |
| comply | `/kəmˈplaɪ/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/comply) |
| authorization | `/ˌɑː.θɚ.əˈzeɪ.ʃən/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/authorization) |
| arrangement | `/əˈreɪndʒ.mənt/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/arrangement) |
| consultant | `/kənˈsʌl.tənt/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/consultant) |
| consultation | `/ˌkɑːn.səlˈteɪ.ʃən/` | [Cambridge](https://dictionary.cambridge.org/pronunciation/english/consultation) |
| application | `/ˌæp.ləˈkeɪ.ʃən/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/application) |
| applicable | `/əˈplɪk.ə.bəl/` | [Cambridge](https://dictionary.cambridge.org/pronunciation/english/applicable) |
| attendance | `/əˈten.dəns/` | [Cambridge](https://dictionary.cambridge.org/pronunciation/english/attendance) |
| attendee | `/ə.tenˈdiː/` | [Cambridge](https://dictionary.cambridge.org/vi/pronunciation/english/attendee) |
| recruitment | `/rɪˈkruːt.mənt/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/recruitment) |
| manufacturer | `/ˌmæn.jəˈfæk.tʃɚ.ɚ/` | [Cambridge](https://dictionary.cambridge.org/us/pronunciation/english/manufacturer) |

## Synonyms and CEFR

- `competitor`: Cambridge's entry marks the word B1 and lists `challenger`, `contender`, and `rival` as synonyms: [Cambridge definition](https://dictionary.cambridge.org/us/dictionary/english/competitor). The record's sense and record-level CEFR were both changed from A2 to B1.
- `challenger` and `rival` glosses in `data/related-terms.json` are short editorial Vietnamese glosses; the synonym relationship itself comes from Cambridge. `contender` already had a glossary entry.

## Word-family editorial method

- 49 existing records were updated; no headword was added or removed. The links connect current dictionary headwords that are morphological derivatives/related parts of the same lexical family.
- Entries are not presented as synonyms. Each relation stores a target headword, POS label, and Vietnamese gloss; the learner should still use each form according to its own sense.
- The batch is a first curated pass, not a claim that all possible English word families or all 928 records are complete. Further family links require sense/POS review.
