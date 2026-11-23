"""Regression tests for sense-linked TOEIC examples and vocabulary detail UX."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class VocabularyDetailAndExampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = load_json("data/manifest.json")
        cls.records = []
        for item in cls.manifest["letters"]:
            cls.records.extend(load_json(item["file"].replace("./", "", 1))["words"])
        cls.app_js = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
        cls.app_css = (ROOT / "assets/css/app.css").read_text(encoding="utf-8")

    def test_batch009_records_match_canonical_a_to_z_and_have_editorial_fields(self):
        batch = json.loads((ROOT / 'data/vocabulary/batch-009.json').read_text(encoding='utf-8'))
        self.assertEqual(batch['count'], 34)
        self.assertEqual(len(batch['words']), 34)
        self.assertIn('independent lexical review pending', batch['editorialStatus'])
        manifest = json.loads((ROOT / 'data/manifest.json').read_text(encoding='utf-8'))
        canonical = {}
        for item in manifest['letters']:
            path = ROOT / item['file'].replace('./', '', 1)
            for word in json.loads(path.read_text(encoding='utf-8'))['words']:
                canonical[word['id']] = word
        for entry in batch['words']:
            self.assertIn(entry['id'], canonical)
            current = canonical[entry['id']]
            self.assertEqual(current['word'], entry['word'])
            self.assertTrue(entry['senses'])
            self.assertTrue(all(s.get('meaning_vi') and s.get('definition_en') for s in entry['senses']))
            self.assertTrue(entry.get('examples'))
            self.assertTrue(all(e.get('en') and e.get('vi') for e in entry['examples']))
            self.assertGreaterEqual(len(entry.get('collocations', [])), 3)
        self.assertEqual(sum(bool(x.get('phonetic', {}).get('us')) for x in batch['words']), 32)

    def test_batch010_records_match_canonical_a_to_z_and_have_editorial_fields(self):
        batch = json.loads((ROOT / 'data/vocabulary/batch-010.json').read_text(encoding='utf-8'))
        self.assertEqual(batch['count'], 37)
        self.assertEqual(len(batch['words']), 37)
        self.assertIn('independent lexical review pending', batch['editorialStatus'])
        canonical = {record['id']: record for record in self.records}
        for entry in batch['words']:
            self.assertIn(entry['id'], canonical)
            current = canonical[entry['id']]
            self.assertEqual(current['word'], entry['word'])
            self.assertEqual(current['senses'], entry['senses'])
            self.assertTrue(entry['senses'])
            self.assertTrue(all(s.get('meaning_vi') and s.get('definition_en') for s in entry['senses']))
            self.assertEqual({e['sense_index'] for e in entry['examples']}, set(range(len(entry['senses']))))
            self.assertTrue(all(e.get('en') and e.get('vi') for e in entry['examples']))
            self.assertGreaterEqual(len(entry.get('collocations', [])), 3)
            self.assertTrue(entry.get('phonetic', {}).get('us'), entry['id'])
        self.assertEqual(sum(bool(x.get('phonetic', {}).get('us')) for x in batch['words']), 37)

    def test_batch011_records_match_canonical_a_to_z_and_have_editorial_fields(self):
        batch = load_json('data/vocabulary/batch-011.json')
        self.assertEqual(batch['count'], 37)
        self.assertEqual(len(batch['words']), 37)
        self.assertIn('independent lexical review pending', batch['editorialStatus'])
        canonical = {record['id']: record for record in self.records}
        for entry in batch['words']:
            self.assertIn(entry['id'], canonical)
            self.assertEqual(canonical[entry['id']]['word'], entry['word'])
            self.assertEqual(canonical[entry['id']]['senses'], entry['senses'])
            self.assertTrue(entry['examples'])
            self.assertEqual({e['sense_index'] for e in entry['examples']}, {0})
            self.assertTrue(all(e.get('en') and e.get('vi') for e in entry['examples']))
            self.assertGreaterEqual(len(entry.get('collocations', [])), 3)
            self.assertTrue(entry.get('phonetic', {}).get('us'), entry['id'])
        self.assertEqual(sum(bool(x.get('phonetic', {}).get('us')) for x in batch['words']), 37)

    def test_base_vocabulary_id_set_is_preserved_through_batch_012(self):
        ids = [record["id"] for record in self.records]
        baseline = set(load_json("tools/baseline-ids.json")["ids"])
        batch = load_json("data/vocabulary/batch-006.json")
        self.assertTrue(baseline.issubset(set(ids)))
        self.assertEqual(len(batch["words"]), 43)
        batch_018 = load_json("data/vocabulary/batch-007.json")
        self.assertEqual(len(batch_018["words"]), 8)
        self.assertTrue({w["id"] for w in batch_018["words"]}.issubset(set(ids)))
        batch_020 = load_json("data/vocabulary/batch-008.json")
        self.assertEqual(len(batch_020["words"]), 13)
        self.assertTrue({w["id"] for w in batch_020["words"]}.issubset(set(ids)))
        self.assertEqual(len(ids), self.manifest["totalWords"])
        self.assertEqual(len(ids), 1141)
        self.assertEqual(len(ids), len(set(ids)))
        batch_009 = load_json('data/vocabulary/batch-009.json')
        self.assertEqual(len(batch_009['words']), 34)
        self.assertTrue({w['id'] for w in batch_009['words']}.issubset(set(ids)))
        batch_010 = load_json('data/vocabulary/batch-010.json')
        self.assertEqual(len(batch_010['words']), 37)
        self.assertTrue({w['id'] for w in batch_010['words']}.issubset(set(ids)))
        batch_011 = load_json('data/vocabulary/batch-011.json')
        self.assertEqual(len(batch_011['words']), 37)
        self.assertTrue({w['id'] for w in batch_011['words']}.issubset(set(ids)))
        batch_012 = load_json('data/vocabulary/batch-012.json')
        self.assertEqual(len(batch_012['words']), 37)
        self.assertTrue({w['id'] for w in batch_012['words']}.issubset(set(ids)))

    def test_each_example_points_to_an_existing_sense(self):
        for record in self.records:
            for index, example in enumerate(record.get("examples", [])):
                sense_index = example.get("sense_index", 0)
                self.assertIs(type(sense_index), int, (record["id"], index))
                self.assertIn(sense_index, range(len(record["senses"])), (record["id"], index))

    def test_every_sense_has_at_least_one_dedicated_example(self):
        for record in self.records:
            covered = {example.get("sense_index", 0) for example in record.get("examples", [])}
            self.assertEqual(covered, set(range(len(record["senses"]))), record["id"])

    def test_example_sentences_and_translations_are_complete_and_not_duplicated(self):
        sentences = []
        for record in self.records:
            self.assertTrue(record.get("examples"), record["id"])
            for example in record["examples"]:
                en = example.get("en", "").strip()
                vi = example.get("vi", "").strip()
                self.assertGreaterEqual(len(en.split()), 5, (record["id"], en))
                self.assertRegex(en, r"^[A-Z].*[.!?]$", (record["id"], en))
                self.assertTrue(vi)
                self.assertNotEqual(en.casefold(), vi.casefold())
                sentences.append(en.casefold())
        self.assertEqual(len(sentences), len(set(sentences)))

    def test_batch014_sense_expansion_matches_canonical_records_and_sources(self):
        batch = load_json("data/vocabulary/batch-014.json")
        self.assertEqual(batch["batch"], "014")
        self.assertEqual(batch["release"], "2.95.12")
        self.assertEqual(batch["count"], 9)
        self.assertIn("independent lexical review pending", batch["editorialStatus"])
        canonical = {record["id"]: record for record in self.records}
        patch = load_json("patches/v2.95.12/batch-001.json")
        self.assertEqual(patch["allowedPaths"], ["/examples", "/senses"])
        self.assertTrue(all(op["path"] in {"/examples", "/senses"} for op in patch["operations"]))
        self.assertEqual({op["id"] for op in patch["operations"]}, {row["id"] for row in batch["records"]})
        self.assertEqual(patch["idSetSha256"], load_json("tools/baseline-ids.json")["idSetSha256"])
        self.assertEqual({entry["id"] for entry in patch["identityGuard"]}, {row["id"] for row in batch["records"]})
        self.assertTrue(all(entry["id"] and entry["word"] and isinstance(entry["topics"], list) for entry in patch["identityGuard"]))
        guarded = {entry["id"]: entry for entry in patch["identityGuard"]}
        for rid, identity in guarded.items():
            current = canonical[rid]
            self.assertEqual(current["id"], identity["id"])
            self.assertEqual(current["word"], identity["word"])
            self.assertEqual(current.get("topics", []), identity["topics"])
        evidence = {entry["id"]: set(entry["urls"]) for entry in patch["sourceEvidence"]}
        self.assertEqual(set(evidence), {row["id"] for row in batch["records"]})
        for url_set in evidence.values():
            self.assertTrue(url_set)
            self.assertTrue(all(url.startswith("https://dictionary.cambridge.org/") for url in url_set))
        for entry in batch["records"]:
            self.assertIn(entry["id"], canonical)
            current = canonical[entry["id"]]
            self.assertEqual(current["word"], entry["word"])
            self.assertEqual(current["senses"], entry["senses"])
            self.assertEqual(current["examples"], entry["examples"])
            self.assertTrue(entry["sourceUrls"])
            self.assertEqual({e["sense_index"] for e in entry["examples"]}, set(range(len(entry["senses"]))))

    def test_batch016_related_glossary_entries_cover_batch014_terms(self):
        glossary_batch = load_json("data/vocabulary/batch-016.json")
        self.assertEqual(glossary_batch["release"], "2.95.12")
        self.assertEqual(glossary_batch["count"], 22)
        self.assertIn("independent lexical review pending", glossary_batch["editorialStatus"])
        sense_terms = set()
        batch = load_json("data/vocabulary/batch-014.json")
        for entry in batch["records"]:
            for sense in entry["senses"]:
                sense_terms.update(sense.get("synonyms", []))
                sense_terms.update(sense.get("antonyms", []))
        glossary_terms = {entry["term"] for entry in glossary_batch["records"]}
        self.assertTrue(glossary_terms.issubset(sense_terms))
        for entry in glossary_batch["records"]:
            self.assertTrue(entry["meaning_vi"])
            self.assertTrue(entry["sourceUrls"])
            self.assertTrue(all(url.startswith("https://dictionary.cambridge.org/") for url in entry["sourceUrls"]))

    def test_batch017_sense_expansion_matches_canonical_records_and_sources(self):
        batch = load_json("data/vocabulary/batch-017.json")
        self.assertEqual(batch["batch"], "017")
        self.assertEqual(batch["release"], "2.95.13")
        self.assertEqual(batch["count"], 10)
        self.assertIn("independent lexical review pending", batch["editorialStatus"])
        canonical = {record["id"]: record for record in self.records}
        patch = load_json("patches/v2.95.13/batch-001.json")
        self.assertEqual(patch["allowedPaths"], ["/examples", "/senses"])
        self.assertEqual(len(patch["operations"]), 20)
        self.assertEqual(patch["idSetSha256"], load_json("tools/baseline-ids.json")["idSetSha256"])
        self.assertEqual({entry["id"] for entry in patch["identityGuard"]}, {row["id"] for row in batch["records"]})
        guarded = {entry["id"]: entry for entry in patch["identityGuard"]}
        evidence = {entry["id"]: set(entry["urls"]) for entry in patch["sourceEvidence"]}
        self.assertEqual(set(evidence), {row["id"] for row in batch["records"]})
        for entry in batch["records"]:
            current = canonical[entry["id"]]
            self.assertEqual(current["word"], entry["word"])
            self.assertEqual(current["senses"], entry["senses"])
            self.assertEqual(current["examples"], entry["examples"])
            self.assertEqual(current["id"], guarded[entry["id"]]["id"])
            self.assertEqual(current["word"], guarded[entry["id"]]["word"])
            self.assertEqual(current.get("topics", []), guarded[entry["id"]]["topics"])
            self.assertTrue(entry["sourceUrls"])
            self.assertEqual(set(entry["sourceUrls"]), evidence[entry["id"]])
            self.assertTrue(all(url.startswith("https://dictionary.cambridge.org/") for url in entry["sourceUrls"]))
            self.assertEqual({e["sense_index"] for e in entry["examples"]}, set(range(len(entry["senses"]))))

    def test_batch018_related_glosses_are_sourced_and_present(self):
        batch = load_json("data/vocabulary/batch-018.json")
        self.assertEqual(batch["batch"], "018")
        self.assertEqual(batch["release"], "2.95.13")
        self.assertEqual(batch["count"], 4)
        self.assertIn("independent lexical review pending", batch["editorialStatus"])
        related = {row["term"].casefold(): row for row in load_json("data/related-terms.json")["terms"]}
        patch = load_json("patches-related-terms/v2.95.13/related-terms-001.json")
        self.assertEqual(len(patch["operations"]), 4)
        for entry in batch["records"]:
            current = related[entry["term"].casefold()]
            # Later canonical-sense enrichment may add traceability metadata to an
            # existing related gloss without changing the original Batch 018 fields.
            for key, value in entry.items():
                self.assertEqual(current.get(key), value, f"{entry['term']}: {key}")
            extra = set(current) - set(entry)
            self.assertLessEqual(extra, {"sourceHeadword", "sourceRelease", "sourceSenseIndex"})
            self.assertTrue(entry["meaning_vi"])
            self.assertTrue(entry["sourceUrls"])
            self.assertTrue(all(url.startswith("https://dictionary.cambridge.org/") for url in entry["sourceUrls"]))

    def test_batch019_valuable_family_gloss_matches_value_noun_sense(self):
        batch = load_json("data/vocabulary/batch-019.json")
        self.assertEqual(batch["release"], "2.95.13")
        self.assertEqual(batch["count"], 1)
        entry = batch["records"][0]
        canonical = {record["id"]: record for record in self.records}[entry["id"]]
        self.assertEqual(canonical, entry)
        patch = load_json("patches/v2.95.13/batch-002-family-gloss.json")
        self.assertEqual(patch["allowedPaths"], ["/word_family/0"])
        self.assertEqual(patch["operations"][0]["expect"]["old"]["meaning_vi"], "giá trị; coi trọng")
        value = {record["word"]: record for record in self.records}["value"]
        noun = next(sense for sense in value["senses"] if sense["pos"] == "n")
        link = next(row for row in canonical["word_family"] if row["word"] == "value")
        self.assertEqual(link["pos"], "n")
        self.assertEqual(link["meaning_vi"], noun["meaning_vi"])

    def test_batch020_valuation_family_gloss_matches_value_verb_sense(self):
        batch = load_json("data/vocabulary/batch-020.json")
        self.assertEqual(batch["release"], "2.95.13")
        self.assertEqual(batch["count"], 1)
        entry = batch["records"][0]
        canonical = {record["id"]: record for record in self.records}[entry["id"]]
        self.assertEqual(canonical, entry)
        patch = load_json("patches/v2.95.13/batch-003-family-gloss.json")
        self.assertEqual(patch["allowedPaths"], ["/word_family/0"])
        value = {record["word"]: record for record in self.records}["value"]
        verb = next(sense for sense in value["senses"] if sense["pos"] == "v")
        link = next(row for row in canonical["word_family"] if row["word"] == "value")
        self.assertEqual(link["pos"], "v")
        self.assertEqual(link["meaning_vi"], verb["meaning_vi"])

    def test_multisense_entries_have_examples_for_all_senses(self):
        multi = [record for record in self.records if len(record["senses"]) > 1]
        self.assertEqual(len(multi), 49)
        self.assertEqual(sum(len(record["examples"]) for record in multi), 105)
        self.assertTrue(all(len({e.get("sense_index", 0) for e in record["examples"]}) == len(record["senses"]) for record in multi))

    def test_detail_modal_groups_meanings_by_pos_without_duplicate_pos_strip(self):
        self.assertIn("pos-detail-grid", self.app_js)
        self.assertIn("pos-detail-card", self.app_js)
        self.assertIn("posDisplayLabel", self.app_js)
        self.assertNotIn('<div class="detail-pos">${posMarkup(w)}</div>', self.app_js)

    def test_data_workspace_word_name_opens_detail_modal(self):
        handler = re.search(r"\$\('#dataTableBody'\)\.addEventListener\('click',e=>\{([^;]+(?:;[^;]+)*)\}\);", self.app_js)
        self.assertIsNotNone(handler)
        self.assertIn("closest('[data-detail]')", handler.group(1))
        self.assertIn("showDetail(detail.dataset.detail)", handler.group(1))

    def test_personal_copy_retains_sense_linked_examples(self):
        self.assertIn("old?.examples?.slice(1)", self.app_js)
        self.assertIn("sense_index:0", self.app_js)

    def test_vocabulary_example_typography_is_readable(self):
        self.assertRegex(self.app_css, r"\.pos-detail-card \.example-card strong\{[^}]*font-size:13(?:\.25)?px")
        self.assertRegex(self.app_css, r"\.pos-detail-card \.example-card span\{[^}]*font-size:12px")
        self.assertRegex(self.app_css, r"\.pos-detail-grid\{[^}]*grid-template-columns")

    def test_browser_normalizer_preserves_and_sorts_sense_index(self):
        self.assertIn("Number.isInteger(e.sense_index)", self.app_js)
        self.assertIn("Number.isInteger(e.sense_index)", self.app_js)
        self.assertIn("sort((a,b)=>a.sense_index-b.sense_index)", self.app_js)


if __name__ == "__main__":
    unittest.main()
