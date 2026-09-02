# 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/
# Easy

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.thirdMax([3, 2, 1]), 1)

    def test_example2(self):
        self.assertEqual(self.solution.thirdMax([1, 2]), 2)

    def test_example3(self):
        self.assertEqual(self.solution.thirdMax([2, 2, 3, 1]), 1)

    def test_single_element(self):
        self.assertEqual(self.solution.thirdMax([42]), 42)

    def test_two_elements(self):
        self.assertEqual(self.solution.thirdMax([5, 10]), 10)

    def test_all_duplicates(self):
        self.assertEqual(self.solution.thirdMax([7, 7, 7, 7]), 7)

    def test_two_distinct_values(self):
        self.assertEqual(self.solution.thirdMax([1, 1, 2, 2]), 2)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.thirdMax([-1, -2, -3]), -3)

    def test_mixed_positive_negative(self):
        self.assertEqual(self.solution.thirdMax([3, -1, 0, 2]), 0)

    def test_zero_values(self):
        self.assertEqual(self.solution.thirdMax([0, 0, -1, 1]), -1)

    def test_duplicates_with_three_distinct(self):
        self.assertEqual(self.solution.thirdMax([5, 5, 5, 4, 4, 3]), 3)

    def test_unordered_input(self):
        self.assertEqual(self.solution.thirdMax([10, 3, 5, 1, 7]), 5)

    def test_extreme_values(self):
        self.assertEqual(self.solution.thirdMax([2**31 - 1, -(2**31), 0]), -(2**31))

    def test_negative_extreme(self):
        self.assertEqual(
            self.solution.thirdMax([-(2**31), -(2**31) + 1, -(2**31) + 2]),
            -(2**31),
        )

    def test_two_distinct_with_negatives(self):
        self.assertEqual(self.solution.thirdMax([-5, -5, -2]), -2)

    def test_duplicates_and_order(self):
        self.assertEqual(self.solution.thirdMax([2, 2, -3, -2, 0, 0, 3, 3]), 0)

    def test_four_distinct_values(self):
        self.assertEqual(self.solution.thirdMax([2, 2, -3, -2, 3, 3]), -2)

    def test_long_input(self):
        nums = list(range(10000, 0, -1))
        self.assertEqual(self.solution.thirdMax(nums), 9998)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Sorting
