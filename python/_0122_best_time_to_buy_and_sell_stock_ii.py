# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Medium

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.maxProfit([7, 1, 5, 3, 6, 4]), 7)

    def test_example_2(self):
        self.assertEqual(self.sol.maxProfit([1, 2, 3, 4, 5]), 4)

    def test_example_3(self):
        self.assertEqual(self.sol.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_single_element(self):
        self.assertEqual(self.sol.maxProfit([10]), 0)

    def test_two_elements_increasing(self):
        self.assertEqual(self.sol.maxProfit([1, 2]), 1)

    def test_two_elements_decreasing(self):
        self.assertEqual(self.sol.maxProfit([5, 2]), 0)

    def test_two_elements_equal(self):
        self.assertEqual(self.sol.maxProfit([4, 4]), 0)

    def test_flat_prices(self):
        self.assertEqual(self.sol.maxProfit([3, 3, 3, 3, 3]), 0)

    def test_zigzag(self):
        self.assertEqual(self.sol.maxProfit([1, 7, 1, 7, 1, 7]), 18)

    def test_multiple_dips_rises(self):
        self.assertEqual(self.sol.maxProfit([2, 4, 1, 7]), 8)

    def test_all_zeros(self):
        self.assertEqual(self.sol.maxProfit([0, 0, 0, 0]), 0)

    def test_zero_start_increase(self):
        self.assertEqual(self.sol.maxProfit([0, 1, 2]), 2)

    def test_equal_neighbours_mixed(self):
        self.assertEqual(self.sol.maxProfit([5, 5, 8, 8, 6, 9]), 6)

    def test_high_then_low_then_high(self):
        self.assertEqual(self.sol.maxProfit([100, 1, 500]), 499)

    def test_peak_valley_sequence(self):
        self.assertEqual(self.sol.maxProfit([6, 1, 7, 2, 9, 4, 11]), 20)

    def test_large_range(self):
        prices = list(range(30000))
        self.assertEqual(self.sol.maxProfit(prices), 29999)

    def test_large_range_decreasing(self):
        prices = list(range(30000, 0, -1))
        self.assertEqual(self.sol.maxProfit(prices), 0)

    def test_max_values_alternating(self):
        prices = [0, 10000] * 15000
        self.assertEqual(self.sol.maxProfit(prices), 150000000)

    def test_max_values_alternating_decreasing(self):
        prices = [10000, 0] * 15000
        self.assertEqual(self.sol.maxProfit(prices), 149990000)

    def test_two_level_wave(self):
        prices = [5, 5, 5, 7, 7, 7, 2, 2, 2, 9, 9, 9]
        self.assertEqual(self.sol.maxProfit(prices), 9)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Greedy
