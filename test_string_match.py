import unittest	
from string_match import string_match

class TestStringMatch(unittest.TestCase):
    def test_string_match(self):
        self.assertEqual(string_match('xxcaazz', 'xxbaaz'), 3)
        self.assertEqual(string_match('abc', 'abc'), 2)
        self.assertEqual(string_match('abc', 'axc'), 0)
        self.assertEqual(string_match('hello', 'he'), 1)
        self.assertEqual(string_match('he', 'hello'), 1)
        self.assertEqual(string_match('h', 'hello'), 0)
        self.assertEqual(string_match('', 'hello'), 0)
        self.assertEqual(string_match('aabbccdd', 'abbbxxd'), 1)
        self.assertEqual(string_match('aaxxaaxx', 'iaxxai'), 3)
        self.assertEqual(string_match('iaxxai', 'aaxxaaxx'), 3)
