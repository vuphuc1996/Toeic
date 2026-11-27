"""Safety and coverage tests for the v2.95.25 glossary backfill tool."""
from __future__ import annotations
import importlib.util, json, unittest
from pathlib import Path
from glossary_test_helpers import restore_batch_044
ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'tools/backfill-related-glossary-from-vocabulary.py'
spec = importlib.util.spec_from_file_location('glossary_backfill_025', SCRIPT)
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
class GlossaryBackfill025Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vocabulary = mod.load_vocabulary()
        cls.glossary = json.loads((ROOT/'data/related-terms.json').read_text(encoding='utf-8'))
        cls.current = [dict(r) for r in cls.glossary['terms']]
        # Recreate the eligible baseline rows as isolated fixtures; this avoids
        # testing against live source already changed by the backfill release.
        cls.fixture_rows = []
        for term, word in cls.vocabulary.items():
            senses = [s for s in word.get('senses',[]) if s.get('meaning_vi') and s.get('definition_en')]
            if senses and term in {r['term'].casefold() for r in cls.glossary['terms']}:
                current = next(r for r in cls.glossary['terms'] if r['term'].casefold()==term)
                if current.get('source') == mod.SOURCE:
                    clone = dict(current); clone['definition_en'] = mod.PLACEHOLDER; clone.pop('source',None); clone.pop('sourceHeadword',None); clone.pop('sourceRelease',None)
                    cls.fixture_rows.append(clone)
    def test_current_source_has_expected_remaining_placeholder_and_backfill_counts(self):
        placeholders=[r for r in self.current if mod.PLACEHOLDER in r.get('definition_en','').casefold()]
        backfilled=[r for r in self.current if r.get('source')==mod.SOURCE]
        self.assertEqual(len(placeholders),1)
        self.assertEqual(len(backfilled),205)
    def test_baseline_audit_identifies_exact_candidates(self):
        baseline=restore_batch_044({'terms':[dict(r) for r in self.current]}, ROOT)['terms']
        # Restore Batch 043's predecessor values before reconstructing the
        # historical Batch 025 input; otherwise later Cambridge repairs hide
        # placeholders that were present in that old snapshot.
        batch_043=json.loads((ROOT/'patches-related-terms/v2.95.62/related-terms-043.json').read_text(encoding='utf-8'))
        baseline_by={r['term'].casefold():r for r in baseline}
        for operation in batch_043['operations']:
            row=baseline_by[operation['term'].casefold()]
            for field,old_value in operation['expect'].items():
                if field=='term': continue
                if old_value is None: row.pop(field,None)
                else: row[field]=old_value
        for row in baseline:
            if row.get('source')==mod.SOURCE:
                row['definition_en']=mod.PLACEHOLDER
                row.pop('source',None); row.pop('sourceHeadword',None); row.pop('sourceRelease',None)
        placeholders=[r for r in baseline if mod.PLACEHOLDER in r.get('definition_en','').casefold()]
        candidates=[r for r in placeholders if mod.eligible(r,self.vocabulary)]
        self.assertEqual(len(placeholders),268)
        self.assertEqual(len(candidates),205)
        self.assertEqual(mod.audit(baseline,self.vocabulary,write_report=False),(268,205))
    def test_candidate_replacement_uses_canonical_bilingual_sense_and_provenance(self):
        row={'term':'accept','meaning_vi':'chấp nhận','definition_en':mod.PLACEHOLDER}
        word,senses=mod.eligible(row,self.vocabulary)
        updated=mod.replacement(row,word,senses)
        self.assertEqual(updated['meaning_vi'],row['meaning_vi'])
        self.assertNotIn('Reference gloss',updated['definition_en'])
        self.assertEqual(updated['source'],mod.SOURCE)
        self.assertEqual(updated['sourceHeadword'],'accept')
        self.assertEqual(updated['sourceRelease'],'2.95.24')
        self.assertEqual(updated['pos'],'v')
    def test_apply_only_replaces_eligible_fixture_rows(self):
        rows=[dict(r) for r in self.fixture_rows]
        before_terms=[r['term'] for r in rows]
        self.assertEqual(len(rows),205)
        count=mod.apply(rows,self.vocabulary)
        self.assertEqual(count,205)
        self.assertEqual(before_terms,[r['term'] for r in rows])
        self.assertEqual(sum(mod.PLACEHOLDER in r.get('definition_en','').casefold() for r in rows),0)
        self.assertEqual(sum(r.get('source')==mod.SOURCE for r in rows),205)
    def test_apply_is_idempotent(self):
        rows=[dict(r) for r in self.fixture_rows]
        self.assertEqual(mod.apply(rows,self.vocabulary),205)
        self.assertEqual(mod.apply(rows,self.vocabulary),0)
    def test_multi_sense_entry_retains_all_unique_definitions(self):
        row={'term':'record','meaning_vi':'hồ sơ; bản ghi','definition_en':mod.PLACEHOLDER}
        word,senses=mod.eligible(row,self.vocabulary)
        updated=mod.replacement(row,word,senses)
        self.assertGreaterEqual(updated['definition_en'].count(' / '),1)
        self.assertEqual(updated['pos'],'n/v')
if __name__=='__main__': unittest.main()
