# 486. Predict the Winner
# https://leetcode.com/problems/predict-the-winner/
# Medium

from functools import lru_cache
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_element(self):
        self.assertTrue(self.sol.predictTheWinner([1]))

    def test_single_zero(self):
        self.assertTrue(self.sol.predictTheWinner([0]))

    def test_single_large(self):
        self.assertTrue(self.sol.predictTheWinner([10**7]))

    def test_two_equal(self):
        self.assertTrue(self.sol.predictTheWinner([1, 1]))

    def test_two_unequal(self):
        self.assertTrue(self.sol.predictTheWinner([5, 3]))

    def test_two_zero(self):
        self.assertTrue(self.sol.predictTheWinner([0, 0]))

    def test_two_equal_zero(self):
        self.assertTrue(self.sol.predictTheWinner([0, 0]))

    def test_example1(self):
        self.assertFalse(self.sol.predictTheWinner([1, 5, 2]))

    def test_example2(self):
        self.assertTrue(self.sol.predictTheWinner([1, 5, 233, 7]))

    def test_three_uneven(self):
        self.assertTrue(self.sol.predictTheWinner([1, 2, 3]))

    def test_three_player1_wins(self):
        self.assertTrue(self.sol.predictTheWinner([2, 1, 3]))

    def test_three_middle_dominant(self):
        self.assertFalse(self.sol.predictTheWinner([1, 100, 1]))

    def test_all_equal_single(self):
        self.assertTrue(self.sol.predictTheWinner([7]))

    def test_all_equal_three(self):
        self.assertTrue(self.sol.predictTheWinner([5, 5, 5]))

    def test_even_length_equal_pairs(self):
        self.assertTrue(self.sol.predictTheWinner([1, 2, 2, 1]))

    def test_odd_length_middle(self):
        self.assertFalse(self.sol.predictTheWinner([1, 10, 1]))

    def test_alternating(self):
        self.assertFalse(self.sol.predictTheWinner([1, 100, 1, 100, 1]))

    def test_max_length_losing(self):
        nums = [1] * 19
        self.assertTrue(self.sol.predictTheWinner(nums))

    def test_max_length_dominant_middle(self):
        nums = [0] * 9 + [10**7] + [0] * 9
        self.assertEqual(
            self.sol.predictTheWinner(nums),
            self._brute(nums),
        )

    def test_zero_and_positive(self):
        self.assertFalse(self.sol.predictTheWinner([0, 5, 0]))

    def test_zero_and_positive_win(self):
        self.assertTrue(self.sol.predictTheWinner([5, 0]))

    def test_large_values(self):
        self.assertTrue(self.sol.predictTheWinner([10**7, 10**7]))

    def test_mixed(self):
        self.assertEqual(
            self.sol.predictTheWinner([11, 85, 52, 62, 75, 19, 75, 94, 8, 92, 18, 70, 77, 17, 23, 36, 6, 76, 53, 67]),
            self._brute([11, 85, 52, 62, 75, 19, 75, 94, 8, 92, 18, 70, 77, 17, 23, 36, 6, 76, 53, 67]),
        )

    def _brute(self, nums):
        import sys

        sys.setrecursionlimit(10000)

        def solve(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            return max(nums[i] - solve(i + 1, j), nums[j] - solve(i, j - 1))

        return solve(0, len(nums) - 1) >= 0

    def test_random_small_vs_brute(self):
        import random

        random.seed(42)
        for _ in range(200):
            n = random.randint(1, 8)
            nums = [random.randint(0, 15) for _ in range(n)]
            self.assertEqual(
                self.sol.predictTheWinner(nums),
                self._brute(nums),
                f"Mismatch for {nums}",
            )


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Math, Dynamic Programming, Recursion, Minimax, Game Theory, Zero-Sum Game
