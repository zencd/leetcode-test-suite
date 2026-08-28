# 322. Coin Change
# https://leetcode.com/problems/coin-change/
# Medium

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.coinChange([1, 2, 5], 11), 3)

    def test_example2(self):
        self.assertEqual(self.sol.coinChange([2], 3), -1)

    def test_example3(self):
        self.assertEqual(self.sol.coinChange([1], 0), 0)

    def test_amount_zero(self):
        self.assertEqual(self.sol.coinChange([3, 7], 0), 0)

    def test_single_coin_exact(self):
        self.assertEqual(self.sol.coinChange([5], 5), 1)

    def test_single_coin_multiple(self):
        self.assertEqual(self.sol.coinChange([5], 10), 2)

    def test_single_coin_impossible(self):
        self.assertEqual(self.sol.coinChange([7], 10), -1)

    def test_coin_equals_amount(self):
        self.assertEqual(self.sol.coinChange([2, 10], 10), 1)

    def test_greedy_fails(self):
        self.assertEqual(self.sol.coinChange([1, 5, 6, 8], 11), 2)

    def test_duplicate_coins(self):
        self.assertEqual(self.sol.coinChange([2, 2, 2], 8), 4)

    def test_unsorted_coins(self):
        self.assertEqual(self.sol.coinChange([5, 2, 1], 11), 3)

    def test_coin_larger_than_amount(self):
        self.assertEqual(self.sol.coinChange([10, 20], 5), -1)

    def test_one_coin_smaller_others_too_big(self):
        self.assertEqual(self.sol.coinChange([1, 100, 200], 3), 3)

    def test_big_amount_with_one(self):
        self.assertEqual(self.sol.coinChange([1, 50, 25, 5], 99), 10)

    def test_big_amount_impossible(self):
        self.assertEqual(self.sol.coinChange([4, 6], 7), -1)

    def test_max_amount(self):
        self.assertEqual(self.sol.coinChange([1] * 12, 10000), 10000)

    def test_all_twelve_coins(self):
        self.assertEqual(
            self.sol.coinChange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 30), 3
        )

    def test_only_big_denomination(self):
        self.assertEqual(self.sol.coinChange([10000], 10000), 1)

    def test_amount_one(self):
        self.assertEqual(self.sol.coinChange([1], 1), 1)
        self.assertEqual(self.sol.coinChange([2, 3], 1), -1)

    def test_powers_of_two(self):
        self.assertEqual(self.sol.coinChange([1, 2, 4, 8, 16], 31), 5)

    def test_impractical_composition(self):
        self.assertEqual(self.sol.coinChange([3, 7, 40, 43], 5), -1)
        self.assertEqual(self.sol.coinChange([3, 7, 40, 43], 6), 2)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Breadth-First Search, Knapsack Problem, Complete Knapsack
