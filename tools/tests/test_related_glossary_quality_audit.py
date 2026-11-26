"""Contract tests for the read-only glossary quality flag audit."""
import importlib.util, json, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
from glossary_test_helpers import restore_batch_044
SPEC = importlib.util.spec_from_file_location('glossary_quality_audit', ROOT/'tools/audit-related-glossary-quality.py')
MODULE = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MODULE)

class RelatedGlossaryQualityAuditTests(unittest.TestCase):
    def test_missing_definition_meaning_pos_and_provenance_flags(self):
        row = {'term':'test', 'definition_en':'', 'meaning_vi':'', 'pos':'', 'source':''}
        self.assertEqual(MODULE.flags(row), ['missing-definition','missing-meaning-vi','missing-pos','missing-source-provenance'])
        row['definition_en'] = 'Reference gloss for practice distractors.'
        self.assertEqual(MODULE.flags(row), ['placeholder-definition','missing-meaning-vi','missing-pos','missing-source-provenance'])
    def test_short_definition_and_term_echo_flags(self):
        flags = MODULE.flags({'term':'run','definition_en':'run','meaning_vi':'chạy','pos':'verb','source':'x'})
        self.assertIn('short-definition-review', flags)
        self.assertIn('definition-equals-term', flags)
    def test_does_not_flag_normal_entry(self):
        row = {'term':'invoice', 'definition_en':'A document requesting payment for goods or services.', 'meaning_vi':'hóa đơn', 'pos':'noun', 'source':'editorial-reviewed'}
        self.assertEqual(MODULE.flags(row), [])
    def test_audit_reconciles_and_is_deterministic(self):
        rows = [{'term':'x','definition_en':'','meaning_vi':'','pos':'','source':''}, {'term':'y','definition_en':'A concise phrase used here.','meaning_vi':'ngắn','pos':'noun','source':'manual'}]
        a = MODULE.audit(rows); b = MODULE.audit(rows)
        self.assertEqual(a,b); self.assertEqual(a['entries'],2); self.assertEqual(a['flagged_entries'],1)
        self.assertEqual(sum(a['issue_counts'].values()),len(a['flagged'][0]['issues']))
        self.assertIn('read-only', MODULE.render(a))
    def test_duplicate_casefold_terms_are_flagged_without_merging(self):
        rows = [{'term':'Settle','definition_en':'Resolve an account.','meaning_vi':'giải quyết','pos':'v','source':'manual'},
                 {'term':' settle ','definition_en':'Pay an amount owed.','meaning_vi':'thanh toán','pos':'v','source':'manual'}]
        data = MODULE.audit(rows)
        self.assertEqual(data['duplicates'][0]['count'], 2)
        self.assertTrue(all('duplicate-normalized-term' in row['issues'] for row in data['flagged']))
        self.assertEqual(data['entries'], 2)
    def test_duplicate_normalization_uses_nfkc_and_collapsed_whitespace(self):
        rows = [{'term':'Ｆｏｒｍ  Ａ','definition_en':'A test form.','meaning_vi':'mẫu','pos':'noun','source':'manual'},
                 {'term':'form a','definition_en':'A form for a test.','meaning_vi':'biểu mẫu','pos':'noun','source':'manual'}]
        data = MODULE.audit(rows)
        self.assertEqual(len(data['duplicates']), 1)
        self.assertEqual(data['duplicates'][0]['term'], 'form a')
        self.assertEqual(data['duplicates'][0]['indices'], [0, 1])
    def test_non_list_container_is_reported_without_crashing(self):
        data = MODULE.audit({'terms': []})
        self.assertEqual(data['entries'], 0)
        self.assertEqual(data['container_issue'], 'terms-not-list')
        self.assertIn('Input container issue', MODULE.render(data))
    def test_review_priority_classifies_actionable_risk_levels(self):
        self.assertEqual(MODULE.review_priority(['missing-definition']), 'high')
        self.assertEqual(MODULE.review_priority(['placeholder-definition']), 'high')
        self.assertEqual(MODULE.review_priority(['missing-pos']), 'medium')
        self.assertEqual(MODULE.review_priority(['short-definition-review']), 'low')
        self.assertEqual(MODULE.review_priority([]), 'none')
    def test_audit_priority_counts_reconcile(self):
        rows = [
            {'term':'high','definition_en':'','meaning_vi':'','pos':'','source':''},
            {'term':'medium','definition_en':'A meaningful phrase here.','meaning_vi':'nghĩa','pos':'','source':'manual'},
            {'term':'low','definition_en':'run','meaning_vi':'chạy','pos':'v','source':'manual'},
        ]
        data = MODULE.audit(rows)
        self.assertEqual(data['priority_counts'], {'high':1,'medium':1,'low':1})
        self.assertEqual([x['priority'] for x in data['flagged']], ['high','medium','low'])
        self.assertIn('| Priority | Index | Term |', MODULE.render(data))
    def test_empty_list_is_valid_container(self):
        data = MODULE.audit([])
        self.assertEqual(data['entries'], 0)
        self.assertIsNone(data['container_issue'])
    def test_malformed_row_is_flagged_not_crashed(self):
        data = MODULE.audit([None])
        self.assertEqual(data['flagged'][0]['issues'], ['malformed-entry'])
        self.assertEqual(data['entries'], 1)
if __name__ == '__main__': unittest.main()

class RelatedGlossaryEnrichmentQueueTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import importlib.util
        path = ROOT / 'tools/build-related-glossary-enrichment-queue.py'
        spec = importlib.util.spec_from_file_location('related_glossary_enrichment_queue', path)
        cls.queue_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.queue_module)

    def test_queue_ranks_relation_frequency_before_alphabetical_order(self):
        rows = [
            {'term': 'alpha', 'definition_en': '', 'meaning_vi': 'a', 'pos': 'n', 'source': ''},
            {'term': 'zeta', 'definition_en': '', 'meaning_vi': 'z', 'pos': 'n', 'source': ''},
        ]
        data = self.queue_module.build(rows, {'alpha': 1, 'zeta': 4}, {'alpha': {'one'}, 'zeta': {'one', 'two'}})
        self.assertEqual([row['term'] for row in data['entries']], ['zeta', 'alpha'])
        self.assertEqual(data['entries'][0]['relationReferences'], 4)
        self.assertEqual(data['entries'][0]['distinctSourceHeadwords'], 2)

    def test_queue_tiers_separate_definition_blockers_from_metadata(self):
        rows = [
            {'term': 'missing', 'definition_en': '', 'meaning_vi': 'thiếu', 'pos': 'n', 'source': 'source'},
            {'term': 'pos-gap', 'definition_en': 'A complete definition with enough words.', 'meaning_vi': 'thiếu từ loại', 'pos': '', 'source': 'source'},
            {'term': 'short', 'definition_en': 'brief', 'meaning_vi': 'ngắn', 'pos': 'adj', 'source': 'source'},
        ]
        data = self.queue_module.build(rows, {}, {})
        tiers = {row['term']: row['tier'] for row in data['entries']}
        self.assertEqual(tiers['missing'], 'definition-blocker')
        self.assertEqual(tiers['pos-gap'], 'metadata-review')
        self.assertEqual(tiers['short'], 'editorial-review')

    def test_queue_is_read_only_and_render_explains_no_auto_import(self):
        rows = [{'term': 'x', 'definition_en': '', 'meaning_vi': 'x', 'pos': '', 'source': ''}]
        before = json.dumps(rows, ensure_ascii=False)
        data = self.queue_module.build(rows, {'x': 2}, {'x': {'headword'}})
        self.assertEqual(json.dumps(rows, ensure_ascii=False), before)
        self.assertTrue(data['readOnly'])
        self.assertIn('does not establish a definition', self.queue_module.render(data))

    def test_batch_040_guarded_patch_updates_only_existing_glossary_fields(self):
        import hashlib
        patch_path = ROOT / 'patches-related-terms/v2.95.51/related-terms-040.json'
        patch = json.loads(patch_path.read_text(encoding='utf-8'))
        glossary = json.loads((ROOT / 'data/related-terms.json').read_text(encoding='utf-8'))
        self.assertEqual(patch['batchId'], 'related-glossary-040-v2.95.51')
        # Reverse Batch 044 first, then the later historical batches, before
        # reconstructing the exact pre-040 snapshot.
        restored = restore_batch_044(glossary, ROOT)
        by_key = {row['term'].casefold(): row for row in restored['terms']}
        batch_043_path = ROOT / 'patches-related-terms/v2.95.62/related-terms-043.json'
        batch_043 = json.loads(batch_043_path.read_text(encoding='utf-8'))
        for operation in batch_043['operations']:
            row = by_key[operation['term'].casefold()]
            for field, old_value in operation['expect'].items():
                if field == 'term':
                    continue
                if old_value is None:
                    row.pop(field, None)
                else:
                    row[field] = old_value
        batch_042_path = ROOT / 'patches-related-terms/v2.95.61/related-terms-042.json'
        batch_042 = json.loads(batch_042_path.read_text(encoding='utf-8'))
        for operation in batch_042['operations']:
            row = by_key[operation['term'].casefold()]
            for field, old_value in operation['expect'].items():
                if field == 'term':
                    continue
                if old_value is None:
                    row.pop(field, None)
                else:
                    row[field] = old_value
        batch_041_path = ROOT / 'patches-related-terms/v2.95.52/related-terms-041.json'
        batch_041 = json.loads(batch_041_path.read_text(encoding='utf-8'))
        for operation in batch_041['operations']:
            row = by_key[operation['term'].casefold()]
            for field, old_value in operation['expect'].items():
                if field == 'term':
                    continue
                if old_value is None:
                    row.pop(field, None)
                else:
                    row[field] = old_value
        for operation in patch['operations']:
            row = by_key[operation['term'].casefold()]
            for field, old_value in operation['expect'].items():
                if field == 'term':
                    continue
                if old_value is None:
                    row.pop(field, None)
                else:
                    row[field] = old_value
        payload = (json.dumps(restored, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
        self.assertEqual(hashlib.sha256(payload).hexdigest(), patch['baseFileSha256'])
        self.assertEqual(len(patch['operations']), 6)
        self.assertEqual(len({op['term'].casefold() for op in patch['operations']}), 6)
        self.assertTrue(all(set(op['set']) == {'pos', 'definition_en', 'source', 'sourceUrls', 'sourceRelease'} for op in patch['operations']))
        self.assertTrue(all(op['expect'].get('term') == op['term'] for op in patch['operations']))
        self.assertEqual(len(glossary['terms']), 567)
        self.assertTrue(all(next(row for row in glossary['terms'] if row['term'] == op['term'])['sourceRelease'] == '2.95.51' for op in patch['operations']))
        self.assertTrue(all(op['set']['sourceUrls'][0].startswith('https://dictionary.cambridge.org/dictionary/english/') for op in patch['operations']))
