import unittest
from tools.backfill_missing_ipa_from_cmudict import classify_missing

def converter(tokens):
    if tokens == ['BAD']: raise ValueError('bad pronunciation')
    return '/test/'

class SafeBackfillTests(unittest.TestCase):
    def records(self):
        return {'a':{'word':'alpha','phonetic':{}},'b':{'word':'beta','phonetic':{}},'c':{'word':'gamma','phonetic':{}},'d':{'word':'delta','phonetic':{'us':'/old/'}}}
    def test_exact_single_variant_is_safe(self):
        out=classify_missing(self.records(),{'alpha':[['A']]},converter)
        self.assertEqual(out[0]['status'],'single_variant'); self.assertEqual(out[0]['phoneticUs'],'/test/'); self.assertEqual(out[0]['action'],'apply_safe')
    def test_multiple_variants_are_review_only(self):
        out=classify_missing(self.records(),{'alpha':[['A'],['B']]},converter)
        self.assertEqual(out[0]['status'],'multiple_variants'); self.assertIsNone(out[0]['phoneticUs'])
    def test_duplicate_variant_lines_deduplicated(self):
        out=classify_missing(self.records(),{'alpha':[['A'],['A']]},converter)
        self.assertEqual(out[0]['status'],'single_variant')
    def test_casefold_headword_match(self):
        out=classify_missing(self.records(),{'ALPHA':[['A']]},converter)
        self.assertEqual(out[0]['status'],'single_variant')
    def test_missing_exact_entry_is_review_only(self):
        out=classify_missing(self.records(),{},converter)
        self.assertEqual(out[0]['status'],'no_exact_entry')
    def test_conversion_error_blocks_apply(self):
        out=classify_missing(self.records(),{'alpha':[['BAD']]},converter)
        self.assertEqual(out[0]['status'],'single_variant_conversion_failed'); self.assertEqual(out[0]['action'],'review_only')
    def test_existing_ipa_skipped(self):
        out=classify_missing(self.records(),{'delta':[['D']]},converter)
        self.assertNotIn('d',[x['id'] for x in out])
    def test_queue_stably_sorted(self):
        out=classify_missing(self.records(),{'alpha':[['A']],'gamma':[['G']]},converter)
        self.assertEqual([x['word'] for x in out],sorted([x['word'] for x in out],key=str.casefold))
if __name__=='__main__': unittest.main()
