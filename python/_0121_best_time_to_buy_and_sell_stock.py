# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Easy

from typing import List
import unittest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        raise Exception("Not solved yet")


solution = Solution()


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_example_2_no_profit(self):
        self.assertEqual(solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_single_element(self):
        self.assertEqual(solution.maxProfit([1]), 0)

    def test_single_element_zero(self):
        self.assertEqual(solution.maxProfit([0]), 0)

    def test_two_elements_increasing(self):
        self.assertEqual(solution.maxProfit([1, 2]), 1)

    def test_two_elements_decreasing(self):
        self.assertEqual(solution.maxProfit([2, 1]), 0)

    def test_two_elements_equal(self):
        self.assertEqual(solution.maxProfit([5, 5]), 0)

    def test_three_elements_peak_in_middle(self):
        self.assertEqual(solution.maxProfit([1, 3, 1]), 2)

    def test_monotonically_increasing(self):
        self.assertEqual(solution.maxProfit([1, 2, 3, 4, 5]), 4)

    def test_monotonically_decreasing(self):
        self.assertEqual(solution.maxProfit([5, 4, 3, 2, 1]), 0)

    def test_all_equal(self):
        self.assertEqual(solution.maxProfit([3, 3, 3, 3]), 0)

    def test_sell_not_on_last_day(self):
        self.assertEqual(solution.maxProfit([3, 2, 6, 5, 0, 3]), 4)

    def test_zero_prices(self):
        self.assertEqual(solution.maxProfit([0, 0, 0]), 0)

    def test_start_from_zero(self):
        self.assertEqual(solution.maxProfit([0, 1]), 1)

    def test_max_profit_ends_on_last_day(self):
        self.assertEqual(solution.maxProfit([2, 4, 1]), 2)

    def test_dip_then_recover_to_new_high(self):
        self.assertEqual(solution.maxProfit([2, 5, 1, 7, 3, 9]), 8)

    def test_dip_and_overshoot(self):
        self.assertEqual(solution.maxProfit([8, 1, 3, 2, 9, 7, 2, 1, 8, 2]), 8)

    def test_consecutive_pairs(self):
        self.assertEqual(solution.maxProfit([1, 2, 1, 2, 1]), 1)

    def test_consecutive_dips(self):
        self.assertEqual(solution.maxProfit([2, 1, 2, 1, 2]), 1)

    def test_boundary_values_max_price(self):
        self.assertEqual(solution.maxProfit([0, 10000]), 10000)

    def test_boundary_values_zero_and_max(self):
        self.assertEqual(solution.maxProfit([10000, 0]), 0)

    def test_large_array_alternating(self):
        prices = [5000, 0] * 50000
        self.assertEqual(solution.maxProfit(prices), 5000)

    def test_large_array_increasing(self):
        prices = list(range(100000))
        self.assertEqual(solution.maxProfit(prices), 99999)

    def test_large_array_decreasing(self):
        prices = list(range(100000, 0, -1))
        self.assertEqual(solution.maxProfit(prices), 0)

    def test_result_type(self):
        self.assertIsInstance(solution.maxProfit([1, 2]), int)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming
