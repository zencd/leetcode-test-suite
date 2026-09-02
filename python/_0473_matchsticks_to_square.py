# 473. Matchsticks to Square
# https://leetcode.com/problems/matchsticks-to-square/
# Medium

from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertTrue(self.sol.makesquare([1, 1, 2, 2, 2]))

    def test_example2(self):
        self.assertFalse(self.sol.makesquare([3, 3, 3, 3, 4]))

    def test_perfect_square(self):
        self.assertTrue(self.sol.makesquare([1, 1, 1, 1]))

    def test_already_square(self):
        self.assertTrue(self.sol.makesquare([5, 5, 5, 5]))

    def test_single_stick(self):
        self.assertFalse(self.sol.makesquare([1]))

    def test_two_sticks(self):
        self.assertFalse(self.sol.makesquare([1, 1]))

    def test_three_sticks(self):
        self.assertFalse(self.sol.makesquare([1, 1, 1]))

    def test_too_few_sticks(self):
        self.assertFalse(self.sol.makesquare([2, 2]))

    def test_sum_not_divisible(self):
        self.assertFalse(self.sol.makesquare([1, 1, 1]))

    def test_stick_longer_than_side(self):
        self.assertFalse(self.sol.makesquare([2, 1, 1, 1, 1, 1]))

    def test_all_ones(self):
        self.assertTrue(self.sol.makesquare([1] * 8))

    def test_all_ones_odd(self):
        self.assertFalse(self.sol.makesquare([1] * 7))

    def test_all_ones_twelve(self):
        self.assertTrue(self.sol.makesquare([1] * 12))

    def test_two_sides_from_parts(self):
        self.assertTrue(self.sol.makesquare([1, 1, 1, 1, 2, 2, 2, 2]))

    def test_unorderable(self):
        self.assertFalse(self.sol.makesquare([1, 2, 3]))

    def test_max_length_single(self):
        self.assertFalse(self.sol.makesquare([10**8]))

    def test_large_equal_sticks(self):
        self.assertTrue(self.sol.makesquare([10**8] * 4))

    def test_large_mixed(self):
        self.assertFalse(self.sol.makesquare([10**8, 10**8, 10**8 - 1, 10**8 - 1, 2]))

    def test_mixed_lengths_true(self):
        self.assertTrue(self.sol.makesquare([15, 18, 21, 24, 27, 30, 33, 36]))

    def test_duplicate_sticks_false(self):
        self.assertFalse(self.sol.makesquare([1, 1, 1, 1, 2]))

    def test_fifteen_sticks(self):
        self.assertTrue(self.sol.makesquare([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))

    def test_order_independence(self):
        a = [1, 1, 2, 2, 2]
        b = list(reversed(a))
        self.assertEqual(self.sol.makesquare(a), self.sol.makesquare(b))

    def test_does_not_mutate_input(self):
        arr = [3, 1, 2, 1]
        original = list(arr)
        self.sol.makesquare(arr)
        self.assertEqual(arr, original)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask
