from alpha_seq import AlphaSequencer, numeric_alphabet_lookup, alphabet_numeral_lookup
import unittest

class TestSingles(unittest.TestCase):
    def setUp(self):
        self.steps = 500
        sequencer = AlphaSequencer(max_chars=1, seq_max=self.steps)
        self.seq = [c for c in sequencer.sequence_gen()]

    def test_counts_singles(self):
        self.assertEqual(self.seq.count('A'), 20, f"Should Have 20 A's after {self.steps} steps")
        self.assertEqual(self.seq.count('J'), 19, f"Should Have 19 J's after {self.steps} steps")

    def test_single_indexes(self):
        self.assertEqual(self.seq[1], 'B', "Should be letter 'B'")
        self.assertEqual(self.seq[27], 'B', "Should be letter 'B'")
        self.assertEqual(self.seq[53], 'B', "Should be letter 'B'")


class TestDoubles(unittest.TestCase):
    def setUp(self):
        self.steps = 1_409
        sequencer = AlphaSequencer(max_chars=2, seq_max=self.steps)
        self.seq = [c for c in sequencer.sequence_gen()]

    def test_counts_doubles(self):
        self.assertEqual(self.seq.count('A'), 3, f"Should Have 3 A's after {self.steps} steps")
        self.assertEqual(self.seq.count('J'), 2, f"Should Have 2 J's after {self.steps} steps")
        self.assertEqual(self.seq.count('AA'), 2, f"Should Have 2 AA's after {self.steps} steps")
        self.assertEqual(self.seq.count('ZZ'), 2, f"Should Have 2 ZZ's after {self.steps} steps")

    def test_double_indexes(self):
        self.assertEqual(self.seq[1], 'B', "Should be letter 'B'")
        self.assertEqual(self.seq[53], 'BB', "Should be letter 'BB'")
        self.assertEqual(self.seq[703], 'B', "Should be letter 'B'")

class TestTriples(unittest.TestCase):
    def setUp(self):
        self.steps = 18_982
        sequencer = AlphaSequencer(max_chars=3, seq_max=self.steps)
        self.seq = [c for c in sequencer.sequence_gen()]

    def test_counts_triples(self):
        self.assertEqual(self.seq.count('J'), 2, f"Should Have 2 J's after {self.steps} steps")
        self.assertEqual(self.seq.count('CZ'), 2, f"Should Have 2 CZ's after {self.steps} steps")
        self.assertEqual(self.seq.count('ADD'), 1, f"Should Have 1 ADD after {self.steps} steps")
        self.assertEqual(self.seq.count('AAB'), 2, f"Should Have 2 AAB after {self.steps} steps")

    def test_triples_indexes(self):
        self.assertEqual(self.seq[1], 'B', "Should be letter 'B'")
        self.assertEqual(self.seq[53], 'BB', "Should be letter 'BB'")
        self.assertEqual(self.seq[796], 'ADQ', "Should be letter 'ADQ'")
        self.assertEqual(self.seq[18_278], 'A', "Should be letter 'A'")
        self.assertEqual(self.seq[18_276], 'ZZY', "Should be letter 'ZZY'")

class TestQuad(unittest.TestCase):
    def setUp(self):
        self.steps = 493_542
        sequencer = AlphaSequencer(max_chars=4, seq_max=self.steps)
        self.seq = [c for c in sequencer.sequence_gen()]

    def test_counts_quad(self):
        self.assertEqual(self.seq.count('A'), 2, f"Should Have 2 A's after {self.steps} steps")
        self.assertEqual(self.seq.count('J'), 2, f"Should Have 2 J's after {self.steps} steps")
        self.assertEqual(self.seq.count('AA'), 2, f"Should Have 2 AA's after {self.steps} steps")
        self.assertEqual(self.seq.count('ZZ'), 2, f"Should Have 2 ZZ's after {self.steps} steps")
        self.assertEqual(self.seq.count('TEST'), 1, f"Should Have 1 TEST after {self.steps} steps")
        self.assertEqual(self.seq.count('AAAB'), 2, f"Should Have 2 AAAB's after {self.steps} steps")

    def test_double_quad(self):
        self.assertEqual(self.seq[1], 'B', "Should be letter 'B'")
        self.assertEqual(self.seq[53], 'BB', "Should be letter 'BB'")
        self.assertEqual(self.seq[18_276], 'ZZY', "Should be letter 'ZZY'")
        self.assertEqual(self.seq[18_278], 'AAAA', "Should be letter 'AAAA'")
        self.assertEqual(self.seq[475_250], 'ZZZW', "Should be letter 'ZZZW'")
        self.assertEqual(self.seq[493_534], 'AAAC', "Should be letter 'AAAC'")


class TestQuint(unittest.TestCase):
    def setUp(self):
        self.steps = 13_000_000
        sequencer = AlphaSequencer(max_chars=5, seq_max=self.steps)
        self.seq = [c for c in sequencer.sequence_gen()]

    def test_counts_quints(self):
        self.assertEqual(self.seq.count('A'), 2, f"Should Have 2 A's after {self.steps} steps")
        self.assertEqual(self.seq.count('J'), 2, f"Should Have 2 J's after {self.steps} steps")
        self.assertEqual(self.seq.count('AA'), 2, f"Should Have 2 AA's after {self.steps} steps")
        self.assertEqual(self.seq.count('DAMN'), 2, f"Should Have 2 DAMN's after {self.steps} steps")
        self.assertEqual(self.seq.count('LAUGH'), 1, f"Should Have 1 LAUGH after {self.steps} steps")
        self.assertEqual(self.seq.count('ADAPT'), 2, f"Should Have 1 ADAPT's after {self.steps} steps")

    def test_quints_indexes(self):
        self.assertEqual(self.seq[1], 'B', "Should be letter 'B'")
        self.assertEqual(self.seq[53], 'BB', "Should be letter 'BB'")
        self.assertEqual(self.seq[18_278], 'AAAA', "Should be letter 'AAAA'")
        self.assertEqual(self.seq[475_250], 'ZZZW', "Should be letter 'ZZZW'")
        self.assertEqual(self.seq[12_356_628], 'ZZZZY', "Should be letter 'ZZZZY'")
        self.assertEqual(self.seq[12_756_630], 'VSRQ', "Should be letter 'VSRQ'")
        self.assertEqual(self.seq[12_999_999], 'AJORZ', "Should be letter 'AJORZ'")

class TestLookupIntToChar(unittest.TestCase):
    def setUp(self):
        self.alpha_convert = numeric_alphabet_lookup()

    def test_get_letter_1(self):
        self.assertEqual(self.alpha_convert[2], "B", "B should be integer 2 key")

    def test_get_letter_2(self):
        self.assertEqual(self.alpha_convert[25], "Y", "Y should be integer 25 key")

    def test_get_letter_3(self):
        self.assertEqual(self.alpha_convert[0], " ", "Zero should be blank space ' '")

class TestLookupCharToInt(unittest.TestCase):
    def setUp(self):
        self.alpha_numeral = alphabet_numeral_lookup()

    def test_get_numeral_1(self):
        self.assertEqual(self.alpha_numeral["B"], 2, "B should be integer 2")

    def test_get_numeral_2(self):
        self.assertEqual(self.alpha_numeral["Y"], 25, "Y should be integer 25")

    def test_get_numeral_3(self):
        self.assertEqual(self.alpha_numeral[" "], 0, "Space ' ' should be zero")

if __name__ == '__main__':
    unittest.main()