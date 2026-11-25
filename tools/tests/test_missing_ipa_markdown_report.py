import importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SPEC=importlib.util.spec_from_file_location('render_missing_ipa_review_queue', ROOT/'tools/render_missing_ipa_review_queue.py')
MODULE=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MODULE)
class MissingIpaMarkdownReportTests(unittest.TestCase):
    def test_report_reconciles_counts_and_preserves_review_boundary(self):
        payload={'canonicalMissingUsIpaCount':2,'source':'CMUdict','statusCounts':{'single_pronunciation_candidate':1,'multiple_pronunciations_review':1},'records':[{'id':'a','word':'alpha','status':'single_pronunciation_candidate','arpabet_variants':[['AE1','L','F','AH0']],'decision':'review_only_no_auto_apply'},{'id':'b','word':'beta','status':'multiple_pronunciations_review','arpabet_variants':[['B','EY1'],['B','IY1']],'decision':'review_only_no_auto_apply'}]}
        report=MODULE.render(payload)
        self.assertIn('Missing US IPA records: **2**',report)
        self.assertIn('| single_pronunciation_candidate | 1 |',report)
        self.assertIn('`B EY1`<br>`B IY1`',report)
        self.assertIn('no IPA values are applied automatically',report)
        self.assertIn('not an approved IPA transcription',report)
    def test_empty_queue_renders_without_failure(self):
        report=MODULE.render({'canonicalMissingUsIpaCount':0,'records':[],'statusCounts':{}})
        self.assertIn('Missing US IPA records: **0**',report)
        self.assertIn('Candidate and review records',report)
if __name__=='__main__': unittest.main()
