# 453. Minimum Moves to Equal Array Elements
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# Medium

from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.minMoves([1, 2, 3]), 3)

    def test_example_2(self):
        self.assertEqual(self.sol.minMoves([1, 1, 1]), 0)

    def test_single_element(self):
        self.assertEqual(self.sol.minMoves([5]), 0)

    def test_two_elements_equal(self):
        self.assertEqual(self.sol.minMoves([7, 7]), 0)

    def test_two_elements_unequal(self):
        self.assertEqual(self.sol.minMoves([1, 5]), 4)

    def test_decreasing(self):
        self.assertEqual(self.sol.minMoves([3, 2, 1]), 3)

    def test_negatives(self):
        self.assertEqual(self.sol.minMoves([-1, 0, 1]), 3)

    def test_all_negatives(self):
        self.assertEqual(self.sol.minMoves([-5, -3, -8]), 8)

    def test_mixed_negatives(self):
        self.assertEqual(self.sol.minMoves([-10, 3, -2, 7]), 38)

    def test_large_values(self):
        nums = [10**9, -(10**9), 0]
        self.assertEqual(self.sol.minMoves(nums), 3 * 10**9)

    def test_many_elements(self):
        nums = [1] * 99999 + [2]
        self.assertEqual(self.sol.minMoves(nums), 1)

    def test_zeroes(self):
        self.assertEqual(self.sol.minMoves([0, 0, 0]), 0)

    def test_zeros_and_positive(self):
        self.assertEqual(self.sol.minMoves([0, 1]), 1)

    def test_ascending(self):
        self.assertEqual(self.sol.minMoves([1, 2, 3, 4]), 6)

    def test_repeats(self):
        self.assertEqual(self.sol.minMoves([2, 1, 2, 1, 2]), 3)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Math
