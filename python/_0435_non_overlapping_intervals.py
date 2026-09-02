# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/
# Medium

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)

    def test_example2_identical(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]), 2)

    def test_example3_touching(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[1, 2], [2, 3]]), 0)

    def test_single_interval(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[1, 2]]), 0)

    def test_empty(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([]), 0)

    def test_all_overlapping(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]), 4)

    def test_already_sorted_disjoint(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[1, 2], [3, 4], [5, 6], [7, 8]]), 0)

    def test_unsorted_input(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[1, 10], [1, 3], [2, 4]]), 2)

    def test_negative_coordinates(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[-5, -1], [-2, 3], [0, 1]]), 1)

    def test_zigzag(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[0, 30], [5, 10], [15, 20]]), 1)

    def test_nested_within(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[1, 100], [2, 3], [4, 5], [6, 7]]), 1)

    def test_touching_chained(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [4, 5]]), 0)

    def test_partial_overlap_pair(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[1, 3], [2, 4]]), 1)

    def test_containing_pair(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[1, 10], [2, 3]]), 1)

    def test_min_max_constrains(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[-50000, 50000]] * 5), 4)

    def test_mixed_overlaps(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[1, 2], [3, 4], [5, 6], [7, 8]]), 0)

    def test_all_duplicate(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[5, 6], [5, 6], [5, 6], [5, 6]]), 3)

    def test_touching_overlapping_combination(self):
        self.assertEqual(self.sol.eraseOverlapIntervals([[1, 2], [2, 5], [3, 4]]), 1)

    def test_input_not_mutated_separately(self):
        original = [[1, 3], [2, 4]]
        copy = [list(x) for x in original]
        self.assertEqual(self.sol.eraseOverlapIntervals(original), 1)
        self.assertEqual(original, copy, "input list must not be mutated")


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Greedy, Sorting
