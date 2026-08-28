# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Medium

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_element(self):
        self.assertEqual(self.sol.maxProfit([1]), 0)

    def test_single_element_zero(self):
        self.assertEqual(self.sol.maxProfit([0]), 0)

    def test_single_element_large(self):
        self.assertEqual(self.sol.maxProfit([1000]), 0)

    def test_two_elements_increasing(self):
        self.assertEqual(self.sol.maxProfit([1, 2]), 1)

    def test_two_elements_decreasing(self):
        self.assertEqual(self.sol.maxProfit([2, 1]), 0)

    def test_two_elements_equal(self):
        self.assertEqual(self.sol.maxProfit([5, 5]), 0)

    def test_example_1(self):
        self.assertEqual(self.sol.maxProfit([1, 2, 3, 0, 2]), 3)

    def test_example_2(self):
        self.assertEqual(self.sol.maxProfit([1]), 0)

    def test_cooldown_prevents_buying_next_day(self):
        self.assertEqual(self.sol.maxProfit([2, 1, 4]), 3)

    def test_multiple_valid_transactions(self):
        self.assertEqual(self.sol.maxProfit([1, 2, 4, 3, 5]), 4)

    def test_all_ascending(self):
        self.assertEqual(self.sol.maxProfit([1, 2, 3, 4, 5]), 4)

    def test_all_descending(self):
        self.assertEqual(self.sol.maxProfit([5, 4, 3, 2, 1]), 0)

    def test_all_equal(self):
        self.assertEqual(self.sol.maxProfit([7, 7, 7, 7, 7]), 0)

    def test_all_zeros(self):
        self.assertEqual(self.sol.maxProfit([0, 0, 0, 0]), 0)

    def test_zigzag(self):
        self.assertEqual(self.sol.maxProfit([1, 2, 1, 2]), 1)

    def test_cooldown_costs_us_a_transaction(self):
        self.assertEqual(self.sol.maxProfit([3, 2, 6, 5, 0, 3]), 7)

    def test_buy_on_last_day_not_profitable(self):
        self.assertEqual(self.sol.maxProfit([5, 4]), 0)

    def test_sell_then_cooldown_then_nothing(self):
        self.assertEqual(self.sol.maxProfit([1, 2, 3]), 2)

    def test_best_is_single_transaction(self):
        self.assertEqual(self.sol.maxProfit([10, 1, 5]), 4)

    def test_negative_profit_never_chosen(self):
        self.assertEqual(self.sol.maxProfit([9, 8, 7]), 0)

    def test_long_flat_then_spike(self):
        self.assertEqual(self.sol.maxProfit([2, 2, 2, 100]), 98)

    def test_spike_then_flat(self):
        self.assertEqual(self.sol.maxProfit([100, 2, 2, 2]), 0)

    def test_many_oscillations(self):
        prices = [1, 2] * 50
        expected = 25
        self.assertEqual(self.sol.maxProfit(prices), expected)

    def test_max_length_input(self):
        prices = [i % 101 for i in range(5000)]
        self.assertGreaterEqual(self.sol.maxProfit(prices), 0)

    def test_max_price_values(self):
        self.assertEqual(self.sol.maxProfit([1000, 0, 1000]), 1000)

    def test_input_not_modified(self):
        prices = [1, 2, 3]
        original = list(prices)
        self.sol.maxProfit(prices)
        self.assertEqual(prices, original)

    def test_repeated_same_day_no_op(self):
        self.assertEqual(self.sol.maxProfit([1, 1, 2, 2, 1, 1, 3, 3]), 3)

    def test_empty_like_single_day_edge(self):
        self.assertEqual(self.sol.maxProfit([42]), 0)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming
