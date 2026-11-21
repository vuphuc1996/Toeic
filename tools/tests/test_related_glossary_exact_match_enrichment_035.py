import unittest, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from enrich_related_glossary_exact_match import eligible, apply, norm

class ExactMatchGlossaryEnrichmentTests(unittest.TestCase):
    def setUp(self):
        self.vocab={'billing':{'word':'billing','senses':[{'pos':'n','meaning_vi':'vi','definition_en':'English'},{'pos':'v','meaning_vi':'vi2','definition_en':'English2'}]}}
    def test_exact_match_requires_complete_bilingual_senses(self):
        row={'term':'BILLING'}
        self.assertIsNotNone(eligible(row,self.vocab))
        bad={'billing':{'word':'billing','senses':[{'meaning_vi':'vi','definition_en':''}]}}
        self.assertIsNone(eligible(row,bad))
    def test_enrichment_fills_missing_fields_without_overwriting_existing(self):
        rows=[{'term':'billing','meaning_vi':'existing gloss','definition_en':'Keep this','pos':'n','sourceHeadword':'billing'}]
        self.assertEqual(apply(rows,self.vocab,'2.95.35'),1)
        self.assertEqual(rows[0]['definition_en'],'Keep this')
        self.assertEqual(rows[0]['pos'],'n')
        self.assertEqual(rows[0]['sourceRelease'],'2.95.35')
        self.assertEqual(rows[0]['source'],'canonical-vocabulary-senses')
    def test_multisense_definition_is_not_automatically_joined_and_is_idempotent(self):
        rows=[{'term':'billing','meaning_vi':'billing'}]
        self.assertEqual(apply(rows,self.vocab,'2.95.35'),1)
        self.assertNotIn('definition_en', rows[0])
        self.assertEqual(rows[0]['pos'],'n/v')
        self.assertEqual(rows[0]['pos'],'n/v')
        self.assertNotIn('sourceSenseIndex', rows[0])
        self.assertEqual(apply(rows,self.vocab,'2.95.35'),0)
    def test_single_sense_definition_can_be_copied(self):
        vocab={'billing':{'word':'billing','senses':[{'pos':'n','meaning_vi':'vi','definition_en':'English'}]}}
        rows=[{'term':'billing','meaning_vi':'billing'}]
        self.assertEqual(apply(rows,vocab,'2.95.35'),1)
        self.assertEqual(rows[0]['definition_en'],'English')
        self.assertEqual(rows[0]['sourceSenseIndex'],0)

    def test_normalization_is_stable(self):
        self.assertEqual(norm('  BILLING\u00a0 '), 'billing')

if __name__=='__main__': unittest.main()
