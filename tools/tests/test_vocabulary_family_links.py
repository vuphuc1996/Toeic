"""Regression tests for sense-matched derivational vocabulary links in v2.37.0."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Base and derived headwords already existed in the dictionary. POS labels are
# deliberately explicit to avoid treating merely similar-looking words as a family.
PAIRS = [
    ('accrue', 'accrual', 'v', 'n'),
    ('amend', 'amendment', 'v', 'n'),
    ('appoint', 'appointment', 'v', 'n'),
    ('appraise', 'appraisal', 'v', 'n'),
    ('assess', 'assessment', 'v', 'n'),
    ('automate', 'automated', 'v', 'adj'),
    ('disburse', 'disbursement', 'v', 'n'),
    ('distribute', 'distributor', 'v', 'n'),
    ('endorse', 'endorsement', 'v', 'n'),
    ('enroll', 'enrollment', 'v', 'n'),
    ('extend', 'extension', 'v', 'n'),
    ('facilitate', 'facilitator', 'v', 'n'),
    ('fulfill', 'fulfillment', 'v', 'n'),
    ('handle', 'handling', 'v', 'n'),
    ('invoice', 'invoicing', 'v', 'n'),
    ('mobilize', 'mobilization', 'v', 'n'),
    ('notarize', 'notarized', 'v', 'adj'),
    ('outsource', 'outsourcing', 'v', 'n'),
    ('postpone', 'postponement', 'v', 'n'),
    ('quote', 'quotation', 'v', 'n'),
    ('reimburse', 'reimbursement', 'v', 'n'),
    ('replace', 'replacement', 'v', 'n'),
    ('require', 'requirement', 'v', 'n'),
    ('retire', 'retirement', 'v', 'n'),
    ('suspend', 'suspension', 'v', 'n'),
    ('undertake', 'undertaking', 'v', 'n'),
    ('underwrite', 'underwriting', 'v', 'n'),
    ('value', 'valuable', 'n', 'adj'),
    ('apprentice', 'apprenticeship', 'n', 'n'),
    ('participate', 'participant', 'v', 'n'),
    ('reserve', 'reservation', 'v', 'n'),
    ('complete', 'completion', 'v', 'n'),
    ('renew', 'renewal', 'v', 'n'),
    ('renew', 'renewable', 'v', 'adj'),
    ('implement', 'implementation', 'v', 'n'),
    ('perform', 'performance', 'v', 'n'),
    ('promote', 'promotion', 'v', 'n'),
    ('register', 'registration', 'v', 'n'),
    ('withdraw', 'withdrawal', 'v', 'n'),
]


def load_records():
    manifest = json.loads((ROOT / 'data/manifest.json').read_text(encoding='utf-8'))
    records = {}
    for letter in manifest['letters']:
        path = ROOT / letter['file'].replace('./', '', 1)
        data = json.loads(path.read_text(encoding='utf-8'))
        for record in data['words']:
            records[record['word'].casefold()] = record
    return records


def sense_meaning(record, pos):
    exact = [s for s in record['senses'] if s.get('pos') == pos]
    if not exact:
        exact = [s for s in record['senses'] if pos in str(s.get('pos', '')).split('/')]
    if not exact:
        raise AssertionError(f"No {pos} sense for {record['id']}")
    return exact[0]['meaning_vi']


class VocabularyFamilyLinkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_records()

    def family_member(self, owner, target_word):
        matches = [item for item in owner.get('word_family', [])
                   if item.get('word', '').casefold() == target_word.casefold()]
        self.assertEqual(len(matches), 1, f"{owner['id']} -> {target_word}: expected one link")
        return matches[0]

    def test_all_curated_pairs_exist_in_both_directions(self):
        self.assertEqual(len(PAIRS), 39)
        for base, derivative, base_pos, derivative_pos in PAIRS:
            self.assertIn(base, self.records)
            self.assertIn(derivative, self.records)
            self.family_member(self.records[base], derivative)
            self.family_member(self.records[derivative], base)

    def test_family_pos_and_vietnamese_gloss_match_target_sense(self):
        for base, derivative, base_pos, derivative_pos in PAIRS:
            a = self.records[base]
            b = self.records[derivative]
            a_link = self.family_member(a, derivative)
            b_link = self.family_member(b, base)
            self.assertEqual(a_link['pos'], derivative_pos, (base, derivative))
            self.assertEqual(b_link['pos'], base_pos, (derivative, base))
            self.assertEqual(a_link['meaning_vi'], sense_meaning(b, derivative_pos), (base, derivative))
            self.assertEqual(b_link['meaning_vi'], sense_meaning(a, base_pos), (derivative, base))

    def test_family_arrays_have_no_duplicate_terms(self):
        for record in self.records.values():
            items = record.get('word_family', [])
            terms = [item.get('word', '').casefold() for item in items]
            self.assertEqual(len(terms), len(set(terms)), record['id'])

    def test_family_coverage_clears_two_hundred_headwords(self):
        count = sum(bool(record.get('word_family')) for record in self.records.values())
        self.assertGreaterEqual(count, 200)

    def test_existing_reservation_links_are_preserved(self):
        reservation = self.records['reservation']
        reserve = self.records['reserve']
        self.family_member(reservation, 'reserve')
        self.family_member(reserve, 'reservation')
        self.assertTrue(any(item.get('word') == 'reserved' for item in reservation['word_family']))


if __name__ == '__main__':
    unittest.main()
