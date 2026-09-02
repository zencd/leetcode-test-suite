# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/
# Easy

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)

    def test_example2(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]), 2)

    def test_all_ones(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 1, 1, 1]), 4)

    def test_all_zeros(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0, 0, 0]), 0)

    def test_single_one(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1]), 1)

    def test_single_zero(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0]), 0)

    def test_leading_ones(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 1, 1, 0]), 3)

    def test_trailing_ones(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0, 1, 1, 1]), 3)

    def test_middle_ones(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0, 1, 1, 0]), 2)

    def test_isolated_ones(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0, 1, 0, 1, 0]), 1)

    def test_alternating(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 0, 1, 0, 1, 0]), 1)

    def test_max_at_end(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0, 0, 1, 1, 1, 1, 1]), 5)

    def test_multiple_runs_equal(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1]), 2)

    def test_max_in_middle(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 0, 1, 1, 1, 1, 0, 1]), 4)

    def test_long_arrays(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0] * 50000 + [1] * 50000), 50000)
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0] * 100000), 0)
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1] * 100000), 100000)

    def test_zeros_between_runs(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 1, 1, 0, 0, 0, 1, 1]), 3)


if __name__ == "__main__":
    unittest.main()

# Tags: Array
