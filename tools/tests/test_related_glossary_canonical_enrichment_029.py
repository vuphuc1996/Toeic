import importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SPEC=importlib.util.spec_from_file_location('canonical_enrichment',ROOT/'tools/enrich-related-glossary-from-canonical.py')
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)
class EnrichmentTests(unittest.TestCase):
    def test_normalization_unicode_case_and_whitespace(self):
        self.assertEqual(MOD.norm('  Café  '),MOD.norm('café'))
        self.assertEqual(MOD.norm('  Work   Place '),'work place')
    def test_only_referenced_missing_terms_are_added(self):
        vocab={'alpha':{'word':'Alpha','senses':[{'pos':'n','meaning_vi':'một','definition_en':'a complete definition','synonyms':['beta']} ]},
                'beta':{'word':'Beta','senses':[{'pos':'n','meaning_vi':'hai','definition_en':'a complete Beta definition'}]},
                'gamma':{'word':'Gamma','senses':[{'pos':'n','meaning_vi':'ba','definition_en':'another complete meaning','synonyms':[]}]}}
        rows=[]
        result=MOD.candidate_rows(rows,vocab)
        self.assertEqual([r['term'] for r in result],['Beta'])
    def test_existing_terms_are_never_overwritten_or_added(self):
        vocab={'alpha':{'word':'Alpha','senses':[{'pos':'n','meaning_vi':'x','definition_en':'definition','synonyms':['beta']}]},'beta':{'word':'Beta','senses':[{'pos':'n','meaning_vi':'hai','definition_en':'definition'}]}}
        existing=[{'term':'Beta','meaning_vi':'existing gloss'}]
        self.assertEqual(MOD.candidate_rows(existing,vocab),[])
    def test_incomplete_bilingual_sense_blocks_entry(self):
        vocab={'alpha':{'word':'Alpha','senses':[{'pos':'n','meaning_vi':'x','definition_en':'ok','synonyms':['beta']}]},'beta':{'word':'Beta','senses':[{'pos':'n','meaning_vi':'hai','definition_en':'ok'},{'pos':'v','meaning_vi':'','definition_en':'missing Vietnamese'}]}}
        self.assertEqual(MOD.candidate_rows([],vocab),[])
    def test_multi_sense_fields_are_joined_and_provenance_set(self):
        vocab={'alpha':{'word':'Alpha','senses':[{'pos':'n','meaning_vi':'một','definition_en':'source sense','synonyms':['beta']}]},'beta':{'word':'Beta','senses':[{'pos':'n','meaning_vi':'một','definition_en':'sense one','synonyms':['beta']},{'pos':'v','meaning_vi':'hai','definition_en':'sense two','antonyms':['beta']}]}}
        row=MOD.candidate_rows([],vocab)[0]
        self.assertEqual(row['meaning_vi'],'một / hai'); self.assertEqual(row['definition_en'],'sense one / sense two')
        self.assertEqual(row['pos'],'n/v'); self.assertEqual(row['source'],MOD.SOURCE); self.assertEqual(row['sourceHeadword'],'Beta'); self.assertEqual(row['sourceRelease'],MOD.SOURCE_RELEASE)
    def test_duplicate_references_emit_one_term(self):
        vocab={'alpha':{'word':'Alpha','senses':[{'pos':'n','meaning_vi':'một','definition_en':'source','synonyms':['beta','BETA','beta']}]},'beta':{'word':'Beta','senses':[{'pos':'n','meaning_vi':'một','definition_en':'meaning'}]}}
        self.assertEqual(len(MOD.candidate_rows([],vocab)),1)
    def test_missing_pos_is_not_invented(self):
        vocab={'alpha':{'word':'Alpha','senses':[{'meaning_vi':'một','definition_en':'source','synonyms':['beta']}]},'beta':{'word':'Beta','senses':[{'meaning_vi':'một','definition_en':'meaning'}]}}
        self.assertEqual(MOD.candidate_rows([],vocab)[0]['pos'],'')
    def test_repo_candidates_have_complete_fields_and_unique_terms(self):
        glossary=json.loads((ROOT/'data/related-terms.json').read_text(encoding='utf-8'))['terms']
        vocab=MOD.load_vocab(); rows=MOD.candidate_rows(glossary,vocab)
        normalized=[MOD.norm(r['term']) for r in rows]
        self.assertEqual(len(normalized),len(set(normalized)))
        self.assertTrue(all(r['meaning_vi'] and r['definition_en'] and r['source'] and r['sourceHeadword'] for r in rows))
        self.assertEqual(len(rows),0) # all eligible terms are now covered after apply
if __name__=='__main__': unittest.main()
