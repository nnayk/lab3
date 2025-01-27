import unittest
from last2 import last2

class TestLast2(unittest.TestCase):
    def test_last2(self):
        self.assertEqual(last2('hixxhi'), 1)
        self.assertEqual(last2('xaxxaxaxx'), 1)
        self.assertEqual(last2('axxxaaxx'), 2)
        self.assertEqual(last2('xxaxxaxxaxx'), 3)
        self.assertEqual(last2('xaxaxaxx'), 0)
        self.assertEqual(last2('xxxx'), 2)
        self.assertEqual(last2('13121312'), 1)
        self.assertEqual(last2('11212'), 1)
        self.assertEqual(last2('13121311'), 0)
        self.assertEqual(last2('1717171'), 2)
        self.assertEqual(last2('hi'), 0)
        self.assertEqual(last2('h'), 0)
        self.assertEqual(last2(''), 0)

if __name__ == '__main__':
    unittest.main()
