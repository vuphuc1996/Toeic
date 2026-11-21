import importlib.util, unittest
from pathlib import Path
SPEC=importlib.util.spec_from_file_location('graph_audit',Path(__file__).resolve().parents[1]/'audit-vocabulary-relationship-graph.py')
M=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(M)
class GraphAuditTests(unittest.TestCase):
 def test_dangling_detected(self):
  d=M.audit_data([('A.json',self.file([self.word('alpha',['missing'])]))]); self.assertEqual([r['target'] for r in d['dangling_references']],['missing'])
 def test_reciprocal_review_flags_one_way(self):
  d=M.audit_data([('A.json',self.file([self.word('alpha',['beta'])])),('B.json',self.file([self.word('beta')]))]); self.assertEqual(len(d['nonreciprocal_references']),1)
 def test_reciprocal_relation_is_not_flagged(self):
  d=M.audit_data([('A.json',self.file([self.word('alpha',['beta'])])),('B.json',self.file([self.word('beta',['alpha'])]))]); self.assertEqual(d['nonreciprocal_references'],[])
 def test_duplicate_reference_and_self_reference_detected(self):
  d=M.audit_data([('A.json',self.file([self.word('alpha',['alpha',' ALPHA '])]))]); self.assertEqual(len(d['self_references']),1); self.assertEqual(len(d['malformed']),1)
 def test_nonlist_relation_flags_malformed(self):
  d=M.audit_data([('A.json',self.file([{'word':'alpha','senses':[{'synonyms':'beta'}]}]))]); self.assertEqual(d['malformed'][0]['issue'],'relation-not-list')
 def test_duplicate_normalized_headword_detected(self):
  d=M.audit_data([('A.json',self.file([self.word('alpha'),self.word(' ALPHA ')]))]); self.assertEqual(len(d['duplicate_headwords']),1)
 def test_glossary_covered_missing_headword_is_classified(self):
  d=M.audit_data([('A.json',self.file([self.word('alpha',['external-term'])]))],['external-term']); self.assertEqual(len(d['glossary_covered_references']),1); self.assertEqual(d['unresolved_references'],[])
 def test_empty_graph_is_safe(self):
  d=M.audit_data([]); self.assertEqual(d['relation_count'],0); self.assertEqual(d['dangling_references'],[])
 @staticmethod
 def word(word, synonyms=None, antonyms=None): return {'word':word,'senses':[{'synonyms':synonyms or [],'antonyms':antonyms or []}]}
 @staticmethod
 def file(words): return {'schemaVersion':1,'words':words}
if __name__=='__main__': unittest.main()
