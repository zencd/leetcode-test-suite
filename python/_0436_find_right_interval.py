# 436. Find Right Interval
# https://leetcode.com/problems/find-right-interval/
# Medium

from typing import List
import bisect


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_interval(self):
        self.assertEqual(
            self.sol.findRightInterval([[1, 2]]),
            [-1],
        )

    def test_example2(self):
        self.assertEqual(
            self.sol.findRightInterval([[3, 4], [2, 3], [1, 2]]),
            [-1, 0, 1],
        )

    def test_example3(self):
        self.assertEqual(
            self.sol.findRightInterval([[1, 4], [2, 3], [3, 4]]),
            [-1, 2, -1],
        )

    def test_single_interval_self_match(self):
        self.assertEqual(
            self.sol.findRightInterval([[1, 1]]),
            [0],
        )

    def test_all_no_match(self):
        self.assertEqual(
            self.sol.findRightInterval([[1, 10], [2, 20], [3, 30]]),
            [-1, -1, -1],
        )

    def test_all_match_to_later(self):
        self.assertEqual(
            self.sol.findRightInterval([[1, 2], [2, 3], [3, 4]]),
            [1, 2, -1],
        )

    def test_negative_starts(self):
        self.assertEqual(
            self.sol.findRightInterval([[-5, -1], [-3, 2], [0, 1]]),
            [2, -1, -1],
        )

    def test_negative_starts_and_ends(self):
        self.assertEqual(
            self.sol.findRightInterval([[-10, -5], [-3, -1]]),
            [1, -1],
        )

    def test_zero_values(self):
        self.assertEqual(
            self.sol.findRightInterval([[0, 0], [1, 2]]),
            [0, -1],
        )

    def test_exact_boundary_match_only(self):
        self.assertEqual(
            self.sol.findRightInterval([[1, 3], [2, 3], [3, 5]]),
            [2, 2, -1],
        )

    def test_minimize_start_even_with_larger_end(self):
        self.assertEqual(
            self.sol.findRightInterval([[1, 5], [2, 3], [6, 10]]),
            [2, 2, -1],
        )

    def test_unordered_input(self):
        self.assertEqual(
            self.sol.findRightInterval([[10, 20], [1, 5], [5, 8]]),
            [-1, 2, 0],
        )

    def test_large_values(self):
        self.assertEqual(
            self.sol.findRightInterval([[-(10**6), 10**6], [10**6, 10**6]]),
            [1, 1],
        )

    def test_large_input_performance(self):
        intervals = list(([[i, i + 1] for i in range(20000)])[::-1])
        expected = [i - 1 if i > 0 else -1 for i in range(len(intervals))]
        self.assertEqual(
            self.sol.findRightInterval(intervals),
            expected,
        )

    def test_starts_not_monotonic_ends(self):
        self.assertEqual(
            self.sol.findRightInterval([[1, 7], [2, 4], [4, 6]]),
            [-1, 2, -1],
        )

    def test_duplicate_ends_distinct_starts(self):
        self.assertEqual(
            self.sol.findRightInterval([[1, 5], [3, 5], [5, 9]]),
            [2, 2, -1],
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search, Sorting
