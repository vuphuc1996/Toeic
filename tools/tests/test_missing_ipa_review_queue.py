import unittest
from tools.build_missing_ipa_review_queue import collect

class MissingIpaQueueTests(unittest.TestCase):
 def test_only_records_without_us_ipa_are_queued(self):
  rows={'a':{'word':'alpha','phonetic':{'us':'/a/'}},'b':{'word':'beta','phonetic':{'us':''}}}
  result=collect(rows,{'beta':[['B','EY1','T','AH0']]})
  self.assertEqual([r['id'] for r in result],['b'])
 def test_exact_dictionary_match_single_candidate(self):
  result=collect({'x':{'word':'exact'}},{'exact':[['EH1','G','Z','AE2','K','T']]})[0]
  self.assertEqual(result['status'],'single_pronunciation_candidate')
  self.assertEqual(result['arpabet_variants'],[['EH1','G','Z','AE2','K','T']])
 def test_alternate_pronunciations_retained_and_not_applied(self):
  result=collect({'x':{'word':'variant'}},{'variant':[['V','AE1','R'],['V','EH1','R']]})[0]
  self.assertEqual(result['status'],'multiple_pronunciations_review')
  self.assertEqual(len(result['arpabet_variants']),2)
  self.assertEqual(result['decision'],'review_only_no_auto_apply')
 def test_no_match_flagged(self):
  result=collect({'x':{'word':'unknown'}},{})[0]
  self.assertEqual(result['status'],'no_exact_dictionary_entry')
  self.assertEqual(result['arpabet_variants'],[])
 def test_duplicate_dictionary_variants_deduplicated(self):
  result=collect({'x':{'word':'repeat'}},{'repeat':[['R','IY1'],['R','IY1']]})[0]
  self.assertEqual(len(result['arpabet_variants']),1)
 def test_empty_entry_flagged(self):
  result=collect({'x':{'word':'empty'}},{'empty':[]})[0]
  self.assertEqual(result['status'],'empty_dictionary_entry')
 def test_queue_sorted_case_insensitively(self):
  rows={'z':{'word':'Zulu'},'a':{'word':'alpha'}}
  self.assertEqual([r['word'] for r in collect(rows,{})],['alpha','Zulu'])
 def test_blank_us_ipa_is_treated_as_missing(self):
  result=collect({'x':{'word':'word','phonetic':{'us':' '}}},{'word':[['W','ER1','D']]})
  self.assertEqual(len(result),1)
if __name__=='__main__': unittest.main()
