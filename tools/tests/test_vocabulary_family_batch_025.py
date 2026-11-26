"""Regression tests for sourced reciprocal Word Family enrichment in v2.95.67."""
import importlib.util
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location('word_family_graph_audit', ROOT/'tools/audit-word-family-graph.py')
AUDIT = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(AUDIT)

PAIRS = [('apologize','apology','n','v'),('subscribe','subscription','n','v'),('transport','transportation','n','v')]

def load_records():
    manifest=json.loads((ROOT/'data/manifest.json').read_text(encoding='utf-8'))
    records={}
    for item in manifest['letters']:
        data=json.loads((ROOT/item['file'].replace('./','',1)).read_text(encoding='utf-8'))
        for word in data['words']: records[word['word'].casefold()]=word
    return records

def get_sense(record, pos):
    matches=[s for s in record['senses'] if pos in str(s.get('pos','')).split('/')]
    if not matches: raise AssertionError(f"No {pos} sense for {record['id']}")
    return matches[0]

class VocabularyFamilyBatch025Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records=load_records()
        cls.ledger=json.loads((ROOT/'data/vocabulary/batch-025.json').read_text(encoding='utf-8'))

    def test_all_three_new_pairs_are_canonical_and_reciprocal(self):
        for a,b,a_to_b_pos,b_to_a_pos in PAIRS:
            self.assertIn(a,self.records); self.assertIn(b,self.records)
            wa,wb=self.records[a],self.records[b]
            ab=[x for x in wa.get('word_family',[]) if x.get('word','').casefold()==b]
            ba=[x for x in wb.get('word_family',[]) if x.get('word','').casefold()==a]
            self.assertEqual(len(ab),1,(a,b)); self.assertEqual(len(ba),1,(b,a))
            self.assertEqual(ab[0],{'word':wb['word'],'pos':a_to_b_pos,'meaning_vi':get_sense(wb,a_to_b_pos)['meaning_vi']})
            self.assertEqual(ba[0],{'word':wa['word'],'pos':b_to_a_pos,'meaning_vi':get_sense(wa,b_to_a_pos)['meaning_vi']})

    def test_batch_ledger_is_source_linked_and_does_not_add_headwords(self):
        self.assertEqual(self.ledger['release'],'2.95.67')
        self.assertEqual(self.ledger['headwordsAdded'],0)
        self.assertEqual(self.ledger['linksAdded'],6)
        self.assertEqual(len(self.ledger['pairs']),3)
        self.assertTrue(all('dictionary.cambridge.org' in p['sourceUrl'] and 'dictionary.cambridge.org' in p['targetUrl'] for p in self.ledger['pairs']))
        self.assertEqual(len(self.ledger['records']),6)
        for row in self.ledger['records']:
            current=self.records[row['word']]
            self.assertEqual(row['after'],current['word_family'])
            self.assertEqual(row['id'],current['id'])

    def test_read_only_audit_classifies_synthetic_graph(self):
        data=[('A.json',{'words':[{'word':'alpha','senses':[{'pos':'n','meaning_vi':'một alpha'}],
            'word_family':[{'word':'beta','pos':'n','meaning_vi':'một beta'}, {'word':'missing','pos':'v','meaning_vi':'thiếu'}]}]}),
            ('B.json',{'words':[{'word':'beta','senses':[{'pos':'v','meaning_vi':'động từ beta'}],'word_family':[]} ]})]
        report=AUDIT.audit_data(data)
        self.assertEqual(report['link_count'],2)
        self.assertEqual(len(report['missing_targets']),1)
        self.assertEqual(len(report['pos_mismatches']),1)
        self.assertEqual(len(report['meaning_mismatches']),1)
        self.assertEqual(len(report['nonreciprocal_links']),1)
        self.assertEqual(report['malformed'],[])

    def test_duplicate_and_malformed_links_are_reported(self):
        data=[('A.json',{'words':[{'word':'alpha','senses':[{'pos':'n','meaning_vi':'x'}],
            'word_family':[{'word':'beta','pos':'n','meaning_vi':'y'},{'word':' BETA ','pos':'n','meaning_vi':'y'},'bad']} ]}),
            ('B.json',{'words':[{'word':'beta','senses':[{'pos':'n','meaning_vi':'y'}],'word_family':[]} ]})]
        report=AUDIT.audit_data(data)
        self.assertEqual(len(report['duplicate_links']),1)
        self.assertEqual(len(report['malformed']),1)

    def test_audit_does_not_mutate_input_records(self):
        original={'word':'alpha','senses':[{'pos':'n','meaning_vi':'x'}],'word_family':[]}
        before=json.dumps(original,sort_keys=True)
        AUDIT.audit_data([('A.json',{'words':[original]})])
        self.assertEqual(json.dumps(original,sort_keys=True),before)

if __name__=='__main__': unittest.main()
