"""Integrity and evidence checks for original-editorial content batch 026."""
from __future__ import annotations
import hashlib, json, re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def read(rel):
    return json.loads((ROOT/rel).read_text(encoding='utf-8'))
class ContentBatch026Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.batch=read('tools/content-batch-026-v2.95.32.json')
        cls.grammar=read('data/grammar/lessons.json')['lessons']
        cls.listening=read('data/listening/listening-library.json')['listening']
        cls.reading=read('data/readings/reading-library.json')['readings']
        cls.g={x['id']:x for x in cls.grammar}; cls.l={x['id']:x for x in cls.listening}; cls.r={x['id']:x for x in cls.reading}
    def test_batch_inventory_and_totals(self):
        self.assertEqual(self.batch['batch'],'026'); self.assertEqual(self.batch['version'],'2.95.32')
        self.assertEqual(len(self.batch['grammar']),8); self.assertEqual(len(self.batch['listening']),8); self.assertEqual(len(self.batch['reading']),8)
        self.assertEqual(self.batch['counts'],{'grammarLessons':8,'grammarExercises':32,'listeningUnits':8,'listeningQuestions':24,'readingResources':8,'readingQuestions':24})
    def test_source_hashes_match_canonical_content_files(self):
        for path,key in [('data/grammar/lessons.json','grammar_sha256'),('data/listening/listening-library.json','listening_sha256'),('data/readings/reading-library.json','reading_sha256')]:
            source = (ROOT/path).read_bytes()
            if key == 'listening_sha256':
                document = read(path)
                remediation_ids = {
                    'batch026-part3-vendor-call', 'batch026-part3-training-room',
                    'batch026-part3-invoice-correction', 'batch026-part3-access-card',
                    'batch026-part4-building-notice', 'batch026-part4-travel-update',
                    'batch026-part4-product-launch', 'batch026-part4-policy-reminder',
                }
                present = set()
                for unit in document['listening']:
                    if unit.get('id') in remediation_ids:
                        self.assertTrue(unit.get('transcriptTranslation', '').strip(), unit['id'])
                        present.add(unit['id'])
                        del unit['transcriptTranslation']
                self.assertEqual(present, remediation_ids)

                # v2.95.83 adds one practice-only inference item to each
                # allowlisted pre-existing Part 4 talk. Strip only these
                # exact items when rebuilding the historical bank fingerprint.
                practice_only_part4_ids = {
                    'part4-office-announcement', 'part4-conference-update',
                    'part4-safety-announcement', 'part4-product-launch',
                    'part4-quarterly-town-hall', 'part4-customer-voicemail',
                    'part4-warehouse-safety-briefing', 'part4-training-registration',
                    'part4-travel-service-update', 'part4-quarterly-inventory-report',
                }
                practice_only_part4_q5_ids = {
                    'part4-safety-announcement', 'part4-product-launch',
                    'part4-quarterly-inventory-report',
                }
                practice_seen = set()
                for unit in document['listening']:
                    unit_id = unit.get('id')
                    if unit_id not in practice_only_part4_ids:
                        continue
                    questions = unit.get('questions') or []
                    expected_len = 5 if unit_id in practice_only_part4_q5_ids else 4
                    if len(questions) != expected_len or any(q.get('mockEligible') is not False for q in questions[3:]):
                        raise AssertionError(f"Unexpected Part 4 practice-only addition: {unit_id}")
                    practice_seen.add(unit_id)
                    unit['questions'] = questions[:3]
                self.assertEqual(practice_seen, practice_only_part4_ids)

                # v2.95.86 adds three new Part 1 reserve resources. Validate
                # their exact reserve-only contract, then remove only these
                # allowlisted rows to reconstruct the historical Batch 026 bank.
                batch_018_part1_ids = {
                    'part1-construction-plans',
                    'part1-laboratory-bench',
                    'part1-supermarket-shelf',
                }
                batch_018_seen = set()
                restored_units = []
                for unit in document['listening']:
                    if unit.get('id') not in batch_018_part1_ids:
                        restored_units.append(unit)
                        continue
                    questions = unit.get('questions') or []
                    if (
                        unit.get('part') != 'Part 1'
                        or unit.get('editorialBatch') != '018'
                        or unit.get('editorialStatus') != 'reserve-pending-independent-review'
                        or len(questions) != 1
                        or 'mockEligible' in questions[0]
                    ):
                        raise AssertionError(f"Unexpected Batch 018 Part 1 reserve record: {unit.get('id')}")
                    batch_018_seen.add(unit['id'])
                self.assertEqual(batch_018_seen, batch_018_part1_ids)
                document['listening'] = restored_units
                source = (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode('utf-8')
            self.assertEqual(self.batch[key],hashlib.sha256(source).hexdigest())
    def test_grammar_exercises_are_valid_and_ids_unique(self):
        ids=set(); count=0
        for lesson_id in self.batch['grammar']:
            lesson=self.g[lesson_id]; self.assertTrue(lesson['summary']); self.assertTrue(lesson['explanation']); self.assertGreaterEqual(len(lesson['examples']),2)
            for item in lesson['exercises']:
                count+=1; self.assertEqual(len(item['choices']),4); self.assertIn(item['answerIndex'],range(4)); self.assertEqual(len(item['choiceIds']),4); self.assertEqual(len(set(item['choiceIds'])),4)
                for cid in item['choiceIds']: self.assertNotIn(cid,ids); ids.add(cid)
        self.assertEqual(count,32)
    def test_answer_positions_are_evenly_balanced(self):
        from collections import Counter
        grammar=Counter(q['answerIndex'] for lesson_id in self.batch['grammar'] for q in self.g[lesson_id]['exercises'])
        listening=Counter(q['answerIndex'] for unit_id in self.batch['listening'] for q in self.l[unit_id]['questions'])
        reading=Counter(q['answerIndex'] for item_id in self.batch['reading'] for q in self.r[item_id]['questions'])
        self.assertEqual(grammar,{0:8,1:8,2:8,3:8})
        self.assertEqual(listening,{0:6,1:6,2:6,3:6})
        self.assertEqual(reading,{0:6,1:6,2:6,3:6})
    def test_listening_questions_have_exact_transcript_evidence_and_unique_ids(self):
        ids=set(); count=0
        for unit_id in self.batch['listening']:
            unit=self.l[unit_id]; self.assertEqual(unit['contentSource'],'original-editorial'); self.assertEqual(unit['editorialStatus'],'reserve-pending-independent-review'); self.assertEqual(unit['editorialBatch'],'026'); self.assertEqual(unit['contentBatch'],'batch-026-major-expansion'); transcript=' '.join(x['text'] for x in unit['segments'])
            for q in unit['questions']:
                count+=1; self.assertIn(q['evidenceText'],transcript); self.assertEqual(len(q['choices']),4); self.assertIn(q['answerIndex'],range(4))
                for cid in q['choiceIds']: self.assertNotIn(cid,ids); ids.add(cid)
        self.assertEqual(count,24)
    def test_reading_questions_have_exact_passage_evidence_and_unique_ids(self):
        ids=set(); count=0
        for rid in self.batch['reading']:
            item=self.r[rid]; self.assertEqual(item['contentSource'],'original-editorial'); self.assertEqual(item['editorialStatus'],'reserve-pending-independent-review'); self.assertEqual(item['editorialBatch'],'026'); self.assertEqual(item['contentBatch'],'batch-026-major-expansion'); self.assertGreaterEqual(item['wordCount'],75); self.assertEqual(item['wordCount'],len(re.findall(r"\b[\w'-]+\b",item['passage'])))
            for q in item['questions']:
                count+=1; self.assertIn(q['evidenceText'],item['passage']); self.assertEqual(len(q['choices']),4); self.assertIn(q['answerIndex'],range(4))
                for cid in q['choiceIds']: self.assertNotIn(cid,ids); ids.add(cid)
        self.assertEqual(count,24)

    def test_v29583_part4_practice_additions_are_exact_and_mock_excluded(self):
        expected_ids = {
            'part4-office-announcement', 'part4-conference-update',
            'part4-safety-announcement', 'part4-product-launch',
            'part4-quarterly-town-hall', 'part4-customer-voicemail',
            'part4-warehouse-safety-briefing', 'part4-training-registration',
            'part4-travel-service-update', 'part4-quarterly-inventory-report',
        }
        q5_ids = {
            'part4-safety-announcement', 'part4-product-launch',
            'part4-quarterly-inventory-report',
        }
        for unit_id in expected_ids:
            unit = self.l[unit_id]
            expected_len = 5 if unit_id in q5_ids else 4
            self.assertEqual(len(unit['questions']), expected_len, unit_id)
            for q_num in range(4, expected_len + 1):
                added = unit['questions'][q_num - 1]
                self.assertIs(added.get('mockEligible'), False, unit_id)
                self.assertEqual(added['choiceIds'], [f'listening:{unit_id}:{q_num}:choice:{i}' for i in range(1, 5)])

if __name__=='__main__': unittest.main()
