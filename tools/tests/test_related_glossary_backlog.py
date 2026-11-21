import json
import subprocess
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class RelatedGlossaryBacklogTests(unittest.TestCase):
    def test_report_is_generated_and_counts_are_consistent(self):
        subprocess.run([sys.executable,str(ROOT/'tools/build-related-glossary-backlog.py')],check=True,capture_output=True,text=True)
        report=json.loads((ROOT/'docs/reports/related-glossary-backlog.json').read_text(encoding='utf-8'))
        rows=report['terms']
        self.assertEqual(report['uniqueUnglossedTerms'],len(rows))
        self.assertEqual(report['uncoveredReferenceCount'],sum(x['references'] for x in rows))
        self.assertEqual(rows,sorted(rows,key=lambda x:(-x['references'],-x['sourceHeadwordCount'],-x['synonymReferences'],x['term'].casefold())))
        self.assertTrue((ROOT/'docs/reports/RELATED_GLOSSARY_BACKLOG.md').exists())
        self.assertTrue(all(len(x['sourceHeadwords']) == x['sourceHeadwordCount'] for x in rows))
        self.assertTrue(all(x['synonymReferences'] + x['antonymReferences'] == x['references'] for x in rows))
    def test_queue_exposes_source_headwords_and_reference_type(self):
        report=json.loads((ROOT/'docs/reports/related-glossary-backlog.json').read_text(encoding='utf-8'))
        row=next(x for x in report['terms'] if x['term'].casefold() == 'disorganize')
        self.assertEqual(row['sourceHeadwords'], ['arrange', 'organize'])
        self.assertEqual((row['references'],row['synonymReferences'],row['antonymReferences']), (2,0,2))
        self.assertEqual(report['schemaVersion'],2)
    def test_report_does_not_include_glossed_terms(self):
        subprocess.run([sys.executable,str(ROOT/'tools/build-related-glossary-backlog.py')],check=True,capture_output=True,text=True)
        gloss=json.loads((ROOT/'data/related-terms.json').read_text(encoding='utf-8'))['terms']
        known={x['term'].strip().casefold() for x in gloss}
        report=json.loads((ROOT/'docs/reports/related-glossary-backlog.json').read_text(encoding='utf-8'))
        self.assertTrue(all(x['term'].casefold() not in known for x in report['terms']))
if __name__=='__main__': unittest.main()
