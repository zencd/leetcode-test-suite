# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# Medium

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_example2(self):
        self.assertEqual(self.solution.lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)

    def test_example3(self):
        self.assertEqual(self.solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1)

    def test_single_element(self):
        self.assertEqual(self.solution.lengthOfLIS([5]), 1)

    def test_already_increasing(self):
        self.assertEqual(self.solution.lengthOfLIS([1, 2, 3, 4, 5]), 5)

    def test_decreasing(self):
        self.assertEqual(self.solution.lengthOfLIS([5, 4, 3, 2, 1]), 1)

    def test_two_elements_increasing(self):
        self.assertEqual(self.solution.lengthOfLIS([1, 2]), 2)

    def test_two_elements_decreasing(self):
        self.assertEqual(self.solution.lengthOfLIS([2, 1]), 1)

    def test_two_elements_equal(self):
        self.assertEqual(self.solution.lengthOfLIS([3, 3]), 1)

    def test_negative_numbers(self):
        self.assertEqual(
            self.solution.lengthOfLIS([-10000, -5, -3, -1, 0, 5000, 9999, 10000]), 8
        )

    def test_all_negative_decreasing(self):
        self.assertEqual(self.solution.lengthOfLIS([-5, -4, -3, -2, -1]), 5)

    def test_mixed_negative_positive(self):
        self.assertEqual(self.solution.lengthOfLIS([-1, -2, -3, -4, -5, 6, 7, 8]), 4)

    def test_duplicates_scattered(self):
        self.assertEqual(self.solution.lengthOfLIS([1, 1, 1, 2, 2, 2, 3, 3, 3]), 3)

    def test_oscillating(self):
        self.assertEqual(self.solution.lengthOfLIS([1, 3, 5, 4, 7]), 4)

    def test_lis_not_suffix(self):
        self.assertEqual(self.solution.lengthOfLIS([4, 10, 4, 3, 2, 9, 5]), 2)

    def test_large_boundary_values(self):
        self.assertEqual(self.solution.lengthOfLIS([10000, 9999, -9999, -10000]), 1)

    def test_increase_then_dip_then_increase(self):
        self.assertEqual(
            self.solution.lengthOfLIS([2, 2, 3, 3, 1, 4, 7, 8, 2, 1, 2, 8, 1]), 5
        )

    def test_length_two_max(self):
        self.assertEqual(self.solution.lengthOfLIS([1, 3]), 2)

    def test_random_ish_sequence(self):
        self.assertEqual(
            self.solution.lengthOfLIS([1, 1, 2, 4, 6, 10, 9, 3, 8, 2, 7]), 5
        )

    def test_repeated_subsequences(self):
        self.assertEqual(self.solution.lengthOfLIS([1, 2, 1, 2, 1, 2]), 2)

    def test_strict_increasement_required(self):
        self.assertEqual(self.solution.lengthOfLIS([1, 2, 2, 2, 3, 3, 3, 4]), 4)

    def test_long_increasing_run(self):
        self.assertEqual(self.solution.lengthOfLIS(list(range(1, 101))), 100)

    def test_long_decreasing_run(self):
        self.assertEqual(self.solution.lengthOfLIS(list(range(100, 0, -1))), 1)

    def test_pattern_high_low(self):
        self.assertEqual(self.solution.lengthOfLIS([10, 1, 9, 2, 8, 3, 7, 4, 6, 5]), 5)

    def test_zero_and_positive(self):
        self.assertEqual(self.solution.lengthOfLIS([0, 0, 0, 1, 1, 1, 2]), 3)

    def test_zero_and_negative(self):
        self.assertEqual(self.solution.lengthOfLIS([-3, -2, -1, 0, 0, 0, 1]), 5)

    def test_alternating_negatives(self):
        self.assertEqual(self.solution.lengthOfLIS([-5, 3, -4, 2, -3, 1, -2, 0]), 5)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search, Dynamic Programming, Longest Increasing Subsequence
