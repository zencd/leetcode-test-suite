# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
# Medium

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.maxProduct([2, 3, -2, 4]), 6)

    def test_example2(self):
        self.assertEqual(self.sol.maxProduct([-2, 0, -1]), 0)

    def test_single_positive(self):
        self.assertEqual(self.sol.maxProduct([5]), 5)

    def test_single_negative(self):
        self.assertEqual(self.sol.maxProduct([-5]), -5)

    def test_single_zero(self):
        self.assertEqual(self.sol.maxProduct([0]), 0)

    def test_all_positive(self):
        self.assertEqual(self.sol.maxProduct([1, 2, 3, 4, 5]), 120)

    def test_all_negative_even_count(self):
        self.assertEqual(self.sol.maxProduct([-1, -2, -3, -4]), 24)

    def test_all_negative_odd_count(self):
        self.assertEqual(self.sol.maxProduct([-1, -2, -3]), 6)

    def test_two_negatives_apart(self):
        self.assertEqual(self.sol.maxProduct([-2, -3, -4]), 12)

    def test_negative_pair_with_positives(self):
        self.assertEqual(self.sol.maxProduct([-2, 1, -3, 4, -5, 6]), 360)

    def test_zeros_reset(self):
        self.assertEqual(self.sol.maxProduct([2, 3, 0, 4, 5]), 20)

    def test_zeros_around_negatives(self):
        self.assertEqual(self.sol.maxProduct([-2, 0, -3, 0, -4]), 0)

    def test_all_zeros(self):
        self.assertEqual(self.sol.maxProduct([0, 0, 0]), 0)

    def test_zero_between_negative_extremes(self):
        self.assertEqual(self.sol.maxProduct([-10, 0, 10]), 10)

    def test_ones(self):
        self.assertEqual(self.sol.maxProduct([1, 1, 1, 1]), 1)

    def test_mixture_of_ones_and_negatives(self):
        self.assertEqual(self.sol.maxProduct([-1, 1, -1]), 1)

    def test_extreme_values(self):
        self.assertEqual(self.sol.maxProduct([-10, -10]), 100)

    def test_large_product_of_tens(self):
        self.assertEqual(self.sol.maxProduct([10, 10]), 100)

    def test_negative_then_zero_then_positive(self):
        self.assertEqual(self.sol.maxProduct([-2, 0, 7]), 7)

    def test_positive_then_zero_then_negative(self):
        self.assertEqual(self.sol.maxProduct([7, 0, -2]), 7)

    def test_alternating_signs(self):
        self.assertEqual(self.sol.maxProduct([2, -2, 2, -2]), 16)

    def test_single_negative_in_positive_run(self):
        self.assertEqual(self.sol.maxProduct([3, 4, -1, 5]), 12)

    def test_min_product_wins_via_pair_of_negatives(self):
        self.assertEqual(self.sol.maxProduct([1, -2, 3, -4, 5]), 120)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming
