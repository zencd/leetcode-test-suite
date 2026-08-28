# 188. Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# Hard

from typing import List
import unittest


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.maxProfit(2, [2, 4, 1]), 2)

    def test_example_2(self):
        self.assertEqual(self.sol.maxProfit(2, [3, 2, 6, 5, 0, 3]), 7)

    def test_single_element(self):
        self.assertEqual(self.sol.maxProfit(2, [1]), 0)

    def test_two_elements_increasing(self):
        self.assertEqual(self.sol.maxProfit(1, [1, 2]), 1)

    def test_two_elements_decreasing(self):
        self.assertEqual(self.sol.maxProfit(1, [2, 1]), 0)

    def test_equal_prices(self):
        self.assertEqual(self.sol.maxProfit(3, [5, 5, 5]), 0)

    def test_k_larger_than_holds(self):
        self.assertEqual(self.sol.maxProfit(10, [1, 2, 3, 4, 5]), 4)

    def test_k_one(self):
        self.assertEqual(self.sol.maxProfit(1, [3, 3, 5, 0, 0, 3, 1, 4]), 4)

    def test_k_one_alternating(self):
        self.assertEqual(self.sol.maxProfit(1, [1, 4, 2, 7]), 6)

    def test_all_decreasing(self):
        self.assertEqual(self.sol.maxProfit(3, [9, 8, 7, 6, 5, 4, 3, 2, 1]), 0)

    def test_all_increasing(self):
        self.assertEqual(self.sol.maxProfit(2, [1, 2, 3, 4, 5, 6, 7, 8]), 7)

    def test_multiple_dips(self):
        self.assertEqual(self.sol.maxProfit(3, [1, 2, 4, 2, 1, 3, 5]), 7)

    def test_zero_price_included(self):
        self.assertEqual(self.sol.maxProfit(1, [0, 1]), 1)

    def test_prices_zero(self):
        self.assertEqual(self.sol.maxProfit(2, [0, 0, 0]), 0)

    def test_large_prices(self):
        self.assertEqual(self.sol.maxProfit(2, [0, 1000, 0, 1000]), 2000)

    def test_k_zero(self):
        self.assertEqual(self.sol.maxProfit(0, [1, 2, 3]), 0)

    def test_repeated_pattern(self):
        self.assertEqual(self.sol.maxProfit(4, [2, 1, 2, 1, 2, 1, 2, 1, 2]), 4)

    def test_early_high_late_low(self):
        self.assertEqual(self.sol.maxProfit(2, [8, 7, 6, 5, 4, 3, 2, 1]), 0)

    def test_late_low_early_high(self):
        self.assertEqual(self.sol.maxProfit(2, [1, 2, 3, 4, 5, 6, 7, 8]), 7)

    def test_k_two_three_oscillations(self):
        self.assertEqual(self.sol.maxProfit(2, [1, 3, 1, 3, 1, 3]), 4)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming
