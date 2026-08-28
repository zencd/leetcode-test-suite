# 268. Missing Number
# https://leetcode.com/problems/missing-number/
# Easy

from typing import List
import unittest


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.missingNumber([3, 0, 1]), 2)

    def test_example2(self):
        self.assertEqual(self.solution.missingNumber([0, 1]), 2)

    def test_example3(self):
        self.assertEqual(self.solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    def test_missing_zero(self):
        self.assertEqual(self.solution.missingNumber([1, 2, 3, 4]), 0)

    def test_missing_last(self):
        self.assertEqual(self.solution.missingNumber([0, 1, 2, 3, 4, 5]), 6)

    def test_missing_middle(self):
        self.assertEqual(self.solution.missingNumber([0, 1, 3, 4, 5]), 2)

    def test_two_elements_zero_missing(self):
        self.assertEqual(self.solution.missingNumber([1, 2]), 0)

    def test_single_element_zero(self):
        self.assertEqual(self.solution.missingNumber([0]), 1)

    def test_single_element_one(self):
        self.assertEqual(self.solution.missingNumber([1]), 0)

    def test_sorted_input(self):
        self.assertEqual(self.solution.missingNumber([0, 1, 2, 4, 5]), 3)

    def test_reversed_input(self):
        self.assertEqual(self.solution.missingNumber([5, 4, 2, 1, 0]), 3)

    def test_larger_input(self):
        n = 100
        nums = list(range(n))
        for missing in (0, 1, 42, n):
            arr = [x for x in range(n + 1) if x != missing]
            self.assertEqual(self.solution.missingNumber(arr), missing)

    def test_returns_int(self):
        result = self.solution.missingNumber([3, 0, 1])
        self.assertIsInstance(result, int)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
