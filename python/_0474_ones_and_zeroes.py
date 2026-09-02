# 474. Ones and Zeroes
# https://leetcode.com/problems/ones-and-zeroes/
# Medium

from typing import List
import unittest


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.fx = self.solution.findMaxForm

    def test_example1(self):
        self.assertEqual(self.fx(["10", "0001", "111001", "1", "0"], 5, 3), 4)

    def test_example2(self):
        self.assertEqual(self.fx(["10", "0", "1"], 1, 1), 2)

    def test_single_zero_fits(self):
        self.assertEqual(self.fx(["0"], 1, 1), 1)

    def test_single_one_fits(self):
        self.assertEqual(self.fx(["1"], 1, 1), 1)

    def test_single_too_many_zeros(self):
        self.assertEqual(self.fx(["00"], 1, 1), 0)

    def test_single_too_many_ones(self):
        self.assertEqual(self.fx(["11"], 1, 1), 0)

    def test_all_fit(self):
        self.assertEqual(self.fx(["0", "1", "10", "11"], 5, 5), 4)

    def test_none_fit(self):
        self.assertEqual(self.fx(["1111", "0000"], 1, 1), 0)

    def test_larger_budget_than_needed(self):
        self.assertEqual(self.fx(["0", "1", "10"], 100, 100), 3)

    def test_all_zeros_tradeoff(self):
        self.assertEqual(self.fx(["0", "00", "000"], 3, 3), 2)

    def test_all_zeros_all_fit(self):
        self.assertEqual(self.fx(["0", "00", "000"], 6, 3), 3)

    def test_all_ones_tradeoff(self):
        self.assertEqual(self.fx(["1", "11", "111"], 3, 3), 2)

    def test_all_ones_all_fit(self):
        self.assertEqual(self.fx(["1", "11", "111"], 3, 6), 3)

    def test_must_choose(self):
        self.assertEqual(self.fx(["10", "0", "1", "0011"], 2, 2), 3)

    def test_zero_one_pair_better_than_split(self):
        self.assertEqual(self.fx(["00", "11", "10"], 2, 2), 2)

    def test_duplicate_items(self):
        self.assertEqual(self.fx(["10", "10"], 2, 2), 2)
        self.assertEqual(self.fx(["10", "10"], 1, 1), 1)

    def test_single_char_strings(self):
        self.assertEqual(self.fx(["0", "0", "0", "1", "1", "1"], 3, 3), 6)

    def test_one_dominates(self):
        self.assertEqual(self.fx(["1", "00"], 1, 1), 1)

    def test_zero_dominates(self):
        self.assertEqual(self.fx(["0", "11"], 1, 1), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, String, Dynamic Programming, Knapsack Problem, 0-1 Knapsack
