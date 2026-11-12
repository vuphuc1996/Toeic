# v2.10.2 — IPA & Word Family Sources

Date: 2026-11-09. Scope: Batch 002, source review for 11 US IPA entries and 9 word-family links. All IPA values were normalized to the project's slash-delimited, dot-separated style while retaining US rhotic and flap symbols.

## US IPA references

| Headword | Stored US IPA | Cambridge source | Editorial note |
|---|---|---|---|
| absence | `/ˈæb.səns/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/absence) | Normalized Cambridge syllable spacing. |
| absorb | `/əbˈsɔːrb/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/absorb) | Cambridge presents two US variants; schema has one `phonetic.us` field, so the first listed US variant is stored and the second is not concatenated. |
| accommodate | `/əˈkɑː.mə.deɪt/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/accommodate) | US form. |
| accountant | `/əˈkaʊn.t̬ənt/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/accountant) | Retains Cambridge flap mark. |
| accounting | `/əˈkaʊn.t̬ɪŋ/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/accounting) | Retains Cambridge flap mark. |
| accurate | `/ˈæk.jɚ.ət/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/accurate) | US rhotic vowel retained. |
| activate | `/ˈæk.tə.veɪt/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/activate) | US form. |
| additional | `/əˈdɪʃ.ə.nəl/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/additional) | Normalized source syllable spaces into dots. |
| adequate | `/ˈæd.ə.kwət/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/adequate) | UK and US forms match in Cambridge. |
| adjacent | `/əˈdʒeɪ.sənt/` | [Cambridge pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/adjacent) | Normalized source syllable spacing. |
| administration | `/ədˌmɪn.əˈstreɪ.ʃən/` | [Cambridge pronunciation](https://dictionary.cambridge.org/pronunciation/english/administration) | US form; retained stress markers. |

Cambridge pronunciation pages provide British/American phonetic transcriptions and audio. Project IPA is a transcription field, not audio. IPA should be rechecked per POS when a single headword contains multiple pronunciations; the current schema stores only one US value per record.

## Word-family sources and scope

- `accommodate` ↔ `accommodation`: [Cambridge accommodate](https://dictionary.cambridge.org/us/dictionary/english/accommodate), [Cambridge accommodation](https://dictionary.cambridge.org/us/dictionary/english/accommodation). Cambridge explicitly describes accommodation as a noun and uses it as a noun counterpart of accommodate.
- `accountant` ↔ `accounting`: [Cambridge accounting](https://dictionary.cambridge.org/us/dictionary/english/accounting) lists accountant among related terms and defines accounting as the activity/job associated with keeping financial records.
- `administration` / `administrative` / `administrator`: [Cambridge administration](https://dictionary.cambridge.org/us/dictionary/english/administration) presents the noun, adjective and noun derivatives together.
- `annual` ↔ `annually`: [Cambridge annual](https://dictionary.cambridge.org/us/dictionary/english/annual) and [Cambridge annually](https://dictionary.cambridge.org/us/dictionary/english/annually) confirm adjective/adverb forms and the same yearly meaning.

Word-family links were only added where both headwords already existed in the 928-record dictionary. These are morphological/derivational links, not synonyms. The Vietnamese glosses are concise editorial translations matched to the existing headword records; they are not quoted translations from Cambridge.
