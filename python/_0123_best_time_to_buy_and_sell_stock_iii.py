# 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# Hard

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]), 6)

    def test_example2_increasing(self):
        self.assertEqual(self.solution.maxProfit([1, 2, 3, 4, 5]), 4)

    def test_example3_decreasing(self):
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.maxProfit([5]), 0)

    def test_two_elements_increasing(self):
        self.assertEqual(self.solution.maxProfit([1, 2]), 1)

    def test_two_elements_decreasing(self):
        self.assertEqual(self.solution.maxProfit([2, 1]), 0)

    def test_two_elements_equal(self):
        self.assertEqual(self.solution.maxProfit([3, 3]), 0)

    def test_one_transaction_enough(self):
        self.assertEqual(self.solution.maxProfit([10, 11, 10]), 1)

    def test_two_transactions_better(self):
        self.assertEqual(self.solution.maxProfit([2, 4, 1, 7]), 7 - 1 + 4 - 2)

    def test_flat_prices(self):
        self.assertEqual(self.solution.maxProfit([2, 2, 2, 2]), 0)

    def test_prices_with_zero(self):
        self.assertEqual(self.solution.maxProfit([0, 1, 0, 1]), 2)

    def test_buy_on_last_day_unprofitable(self):
        self.assertEqual(self.solution.maxProfit([1, 2, 3, 4, 0]), 3)

    def test_sell_on_last_day(self):
        self.assertEqual(self.solution.maxProfit([5, 1, 1, 2, 1, 6]), 6)

    def test_alternating_up_down(self):
        self.assertEqual(self.solution.maxProfit([1, 2, 1, 2, 1, 2]), 2)

    def test_large_profits(self):
        self.assertEqual(self.solution.maxProfit([0, 100000, 0, 100000]), 200000)

    def test_mixed_scenario(self):
        self.assertEqual(
            self.solution.maxProfit([1, 3, 2, 5, 4, 8, 3, 9]), (8 - 1) + (9 - 3)
        )

    def test_three_rises_but_only_two_allowed(self):
        self.assertEqual(self.solution.maxProfit([1, 2, 1, 3, 1, 4]), (3 - 1) + (4 - 1))

    def test_repeated_low_high(self):
        self.assertEqual(self.solution.maxProfit([2, 1, 2, 1, 2, 1, 2]), 2)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming
