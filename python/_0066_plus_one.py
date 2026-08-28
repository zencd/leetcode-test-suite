# 66. Plus One
# https://leetcode.com/problems/plus-one/
# Easy

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_simple(self):
        self.assertEqual(self.solver.plusOne([1, 2, 3]), [1, 2, 4])

    def test_simple_4(self):
        self.assertEqual(self.solver.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_single_zero(self):
        self.assertEqual(self.solver.plusOne([0]), [1])

    def test_single_eight(self):
        self.assertEqual(self.solver.plusOne([8]), [9])

    def test_single_nine(self):
        self.assertEqual(self.solver.plusOne([9]), [1, 0])

    def test_trailing_nine(self):
        self.assertEqual(self.solver.plusOne([1, 9]), [2, 0])

    def test_trailing_nines(self):
        self.assertEqual(self.solver.plusOne([1, 2, 9, 9]), [1, 3, 0, 0])

    def test_all_nines(self):
        self.assertEqual(self.solver.plusOne([9, 9, 9]), [1, 0, 0, 0])

    def test_all_nines_long(self):
        self.assertEqual(self.solver.plusOne([9] * 100), [1] + [0] * 100)

    def test_inner_nine(self):
        self.assertEqual(self.solver.plusOne([9, 1, 7]), [9, 1, 8])

    def test_zero_in_middle(self):
        self.assertEqual(self.solver.plusOne([1, 0, 0]), [1, 0, 1])

    def test_nine_at_start(self):
        self.assertEqual(self.solver.plusOne([9, 0]), [9, 1])

    def test_large_number(self):
        self.assertEqual(self.solver.plusOne([1, 9, 9, 9, 9]), [2, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Math
