import unittest
from array_front9 import array_front9

class TestArrayFront9(unittest.TestCase):
    def test_array_front9(self):
        self.assertEqual(array_front9([1, 2, 3]), False)
        self.assertEqual(array_front9([1, 9, 9]), True)
        self.assertEqual(array_front9([1, 2, 9, 3, 4]), True)
        self.assertEqual(array_front9([1, 2, 3, 4, 9]), False)
        self.assertEqual(array_front9([1, 2, 3, 4, 5]), False)
        self.assertEqual(array_front9([9, 2, 3]), True)
        self.assertEqual(array_front9([1, 9]), True)
        self.assertEqual(array_front9([5, 5]), False)
        self.assertEqual(array_front9([2]), False)
        self.assertEqual(array_front9([9]), True)
        self.assertEqual(array_front9([]), False)
        self.assertEqual(array_front9([3, 9, 2, 3, 3]), True)
