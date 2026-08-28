# 354. Russian Doll Envelopes
# https://leetcode.com/problems/russian-doll-envelopes/
# Hard

from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]), 3)

    def test_example2(self):
        self.assertEqual(self.sol.maxEnvelopes([[1, 1], [1, 1], [1, 1]]), 1)

    def test_single_envelope(self):
        self.assertEqual(self.sol.maxEnvelopes([[1, 1]]), 1)

    def test_all_identical(self):
        self.assertEqual(self.sol.maxEnvelopes([[2, 2], [2, 2]]), 1)

    def test_duplicate_pairs(self):
        self.assertEqual(self.sol.maxEnvelopes([[2, 2], [2, 2], [3, 3], [3, 3]]), 2)

    def test_none_fit(self):
        self.assertEqual(self.sol.maxEnvelopes([[1, 2], [2, 1]]), 1)

    def test_all_fit(self):
        self.assertEqual(self.sol.maxEnvelopes([[1, 1], [2, 2], [3, 3], [4, 4]]), 4)

    def test_reverse_order(self):
        self.assertEqual(self.sol.maxEnvelopes([[4, 4], [3, 3], [2, 2], [1, 1]]), 4)

    def test_same_width_different_height(self):
        self.assertEqual(self.sol.maxEnvelopes([[3, 1], [3, 2], [3, 3]]), 1)

    def test_same_height_different_width(self):
        self.assertEqual(self.sol.maxEnvelopes([[1, 3], [2, 3], [3, 3]]), 1)

    def test_widths_fit_heights_do_not(self):
        self.assertEqual(self.sol.maxEnvelopes([[1, 10], [2, 5], [3, 3]]), 1)

    def test_heights_fit_widths_do_not(self):
        self.assertEqual(self.sol.maxEnvelopes([[10, 1], [5, 2], [3, 3]]), 1)

    def test_unsorted_input(self):
        self.assertEqual(self.sol.maxEnvelopes([[6, 4], [2, 3], [6, 7], [5, 4]]), 3)

    def test_equal_width_blocked(self):
        self.assertEqual(self.sol.maxEnvelopes([[1, 2], [1, 3], [2, 2], [2, 3]]), 2)

    def test_equal_height_blocked(self):
        self.assertEqual(self.sol.maxEnvelopes([[1, 1], [2, 2], [2, 1]]), 2)

    def test_diamond(self):
        self.assertEqual(self.sol.maxEnvelopes([[2, 3], [3, 4], [4, 2]]), 2)

    def test_mixed_larger_values(self):
        self.assertEqual(
            self.sol.maxEnvelopes([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 100]]), 6
        )

    def test_duplicate_pairs_mixed(self):
        self.assertEqual(
            self.sol.maxEnvelopes([[1, 1], [1, 1], [2, 2], [2, 2], [3, 3]]), 3
        )

    def test_width_increasing_height_decreasing(self):
        self.assertEqual(
            self.sol.maxEnvelopes([[1, 5], [2, 4], [3, 3], [4, 2], [5, 1]]), 1
        )

    def test_interleaved(self):
        self.assertEqual(self.sol.maxEnvelopes([[1, 1], [1, 2], [2, 1], [2, 2]]), 2)

    def test_returns_int(self):
        self.assertIsInstance(self.sol.maxEnvelopes([[1, 1]]), int)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search, Dynamic Programming, Sorting, Longest Increasing Subsequence
