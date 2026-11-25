"""Read-only candidate audit contract and deterministic report tests."""
import importlib.util, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SPEC=importlib.util.spec_from_file_location('glossary_candidate_audit',ROOT/'tools/audit-related-glossary-candidates.py')
MODULE=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MODULE)
class RelatedGlossaryCandidateAuditTests(unittest.TestCase):
 def test_counts_reconcile(self):
  d=MODULE.collect(); self.assertEqual(d['vocabulary_count'],1141); self.assertEqual(d['glossary_count'],567); self.assertEqual(d['referenced_distinct'],804)
  self.assertEqual(d['covered']+d['missing_distinct'],d['referenced_distinct']); self.assertEqual(d['missing_occurrences'],249); self.assertEqual(d['missing_distinct'],248); self.assertEqual(d['canonical_candidates'],0)
 def test_missing_candidates_ranked_unique_and_tiered(self):
  d=MODULE.collect(); terms=[x['term'] for x in d['missing']]
  self.assertEqual(len(terms),d['missing_distinct']); self.assertEqual(len(terms),len(set(terms)))
  self.assertEqual(d['missing'],sorted(d['missing'],key=lambda x:(-x['references'],x['term'])))
  self.assertTrue(all(x['tier'] in {'single-sense-review','multi-sense-review','no-canonical-headword'} for x in d['missing']))
  self.assertTrue(all((x['preview'] is None) == (not x['canonical']) for x in d['missing']))
 def test_definition_categories_reconcile(self):
  d=MODULE.collect(); c=d['definition_category_counts']
  self.assertEqual(sum(c.values()),d['glossary_count']); self.assertEqual(c['missing'],131); self.assertEqual(c['placeholder'],63); self.assertEqual(c['present'],373)
 def test_audit_is_read_only_and_deterministic(self):
  a=MODULE.collect(); b=MODULE.collect(); self.assertEqual(a,b); report=MODULE.render(a)
  self.assertIn('Audit-only',report); self.assertIn('Review tier',report); self.assertIn('Definition audit',report)
if __name__=='__main__': unittest.main()
