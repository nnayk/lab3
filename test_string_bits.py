import unittest
from string_bits import string_bits

class TestStringBits(unittest.TestCase):
    def test_string_bits(self):
        self.assertEqual(string_bits('Hello'), 'Hlo')
        self.assertEqual(string_bits('Hi'), 'H')
        self.assertEqual(string_bits('Heeololeo'), 'Hello')
        self.assertEqual(string_bits('HiHiHi'), 'HHH')
        self.assertEqual(string_bits(''), '')
        self.assertEqual(string_bits('Greetings'), 'Getns')
        self.assertEqual(string_bits('Chocoate'), 'Coot')
        self.assertEqual(string_bits('pi'), 'p')
        self.assertEqual(string_bits('Hello Kitten'), 'HloKte')
        self.assertEqual(string_bits('hxaxpxpxy'), 'happy')
