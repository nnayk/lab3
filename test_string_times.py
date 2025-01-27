import unittest
from string_times import string_times

class TestStringTimes(unittest.TestCase):
    def test_string_times(self):
        self.assertEqual(string_times('Hi', 2), 'HiHi')
        self.assertEqual(string_times('Hi', 3), 'HiHiHi')
        self.assertEqual(string_times('Hi', 1), 'Hi')
        self.assertEqual(string_times('Hi', 0), '')
        self.assertEqual(string_times('Hi', 5), 'HiHiHiHiHi')
        self.assertEqual(string_times('Oh Boy!', 2), 'Oh Boy!Oh Boy!')
        self.assertEqual(string_times('x', 4), 'xxxx')
        self.assertEqual(string_times('', 4), '')
        self.assertEqual(string_times('code', 2), 'codecode')
        self.assertEqual(string_times('code', 3), 'codecodecode')

if __name__ == '__main__':
    unittest.main()
