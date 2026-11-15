import importlib.util, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('objective_audit',ROOT/'tools/audit-objective-resources.py')
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
class ObjectiveResourceMapTests(unittest.TestCase):
    def test_all_links_resolve_to_canonical_ids(self):
        objectives,rows,total,mapped=mod.audit()
        self.assertEqual(len(objectives),10)
        self.assertEqual(len(rows),10)
        self.assertEqual(mapped,281)
        self.assertEqual(total,281)
        self.assertGreater(total,0)
    def test_review_status_is_not_confused_with_availability(self):
        objectives,_,_,_=mod.audit()
        p5=next(x for x in objectives if x['id']=='part5-sentence-completion')
        self.assertEqual(p5['availability'],'available')
        self.assertEqual(p5['reviewState'],'pending_independent_review_practice_only_not_mock_eligible')
        listening=next(x for x in objectives if x['id']=='listening-part-3')
        self.assertEqual(listening['reviewState'],'mixed_or_pending_review_check_item_level')
if __name__=='__main__': unittest.main()
