import unittest
from array_count9 import array_count9

class TestArrayCount9(unittest.TestCase):
    def test_array_count9(self):
        self.assertEqual(array_count9([1, 2, 9]), 1)
        self.assertEqual(array_count9([1, 9, 9]), 2)
        self.assertEqual(array_count9([1, 9, 9, 3, 9]), 3)
        self.assertEqual(array_count9([1, 2, 3]), 0)
        self.assertEqual(array_count9([]), 0)
        self.assertEqual(array_count9([4, 2, 4, 3, 1]), 0)
        self.assertEqual(array_count9([9, 2, 4, 3, 1]), 1)
