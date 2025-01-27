import unittest
from front_times import front_times

class TestFrontTimes(unittest.TestCase):
    def test_front_times(self):
        self.assertEqual(front_times('Chocolate', 2), 'ChoCho')
        self.assertEqual(front_times('Chocolate', 3), 'ChoChoCho')
        self.assertEqual(front_times('Abc', 3), 'AbcAbcAbc')
        self.assertEqual(front_times('Ab', 4), 'AbAbAbAb')
        self.assertEqual(front_times('A', 4), 'AAAA')
        self.assertEqual(front_times('', 4), '')
        self.assertEqual(front_times('Abc', 0), '')

if __name__ == '__main__':
    unittest.main()
