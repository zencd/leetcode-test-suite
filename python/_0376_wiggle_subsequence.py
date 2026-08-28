# 376. Wiggle Subsequence
# https://leetcode.com/problems/wiggle-subsequence/
# Medium

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.wiggleMaxLength([]), 0)

    def test_single_element(self):
        self.assertEqual(self.sol.wiggleMaxLength([1]), 1)

    def test_two_equal(self):
        self.assertEqual(self.sol.wiggleMaxLength([1, 1]), 1)

    def test_two_distinct(self):
        self.assertEqual(self.sol.wiggleMaxLength([1, 2]), 2)
        self.assertEqual(self.sol.wiggleMaxLength([2, 1]), 2)

    def test_example1(self):
        self.assertEqual(self.sol.wiggleMaxLength([1, 7, 4, 9, 2, 5]), 6)

    def test_example2(self):
        self.assertEqual(
            self.sol.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]), 7
        )

    def test_example3(self):
        self.assertEqual(self.sol.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2)

    def test_all_equal(self):
        self.assertEqual(self.sol.wiggleMaxLength([3, 3, 3, 3]), 1)

    def test_monotonic_decreasing(self):
        self.assertEqual(self.sol.wiggleMaxLength([9, 8, 7, 6, 5]), 2)

    def test_all_zeros(self):
        self.assertEqual(self.sol.wiggleMaxLength([0, 0, 0]), 1)

    def test_with_equal_adjacent(self):
        self.assertEqual(self.sol.wiggleMaxLength([1, 7, 7, 4, 9, 1]), 5)

    def test_trailing_equal(self):
        self.assertEqual(self.sol.wiggleMaxLength([1, 7, 4, 9, 2, 5, 5]), 6)

    def test_leading_equal(self):
        self.assertEqual(self.sol.wiggleMaxLength([1, 1, 7, 4, 9]), 4)

    def test_alternating_with_duplicates_inside(self):
        self.assertEqual(self.sol.wiggleMaxLength([1, 1, 1, 2, 2, 1, 2]), 4)

    def test_two_elements_max_constraint(self):
        self.assertEqual(self.sol.wiggleMaxLength([1000, 0]), 2)

    def test_repeated_pattern(self):
        self.assertEqual(self.sol.wiggleMaxLength([1, 2, 1, 2, 1, 2]), 6)

    def test_long_oscillation(self):
        nums = [1, 1000, 0, 999, 1, 998, 2]
        self.assertEqual(self.sol.wiggleMaxLength(nums), 7)

    def test_small_values(self):
        self.assertEqual(self.sol.wiggleMaxLength([0, 1, 0]), 3)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Greedy
