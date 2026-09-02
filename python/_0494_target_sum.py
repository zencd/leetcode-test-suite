# 494. Target Sum
# https://leetcode.com/problems/target-sum/
# Medium

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.findTargetSumWays([1, 1, 1, 1, 1], 3), 5)

    def test_example2(self):
        self.assertEqual(self.sol.findTargetSumWays([1], 1), 1)

    def test_single_zero(self):
        self.assertEqual(self.sol.findTargetSumWays([0], 0), 2)

    def test_target_impossible_too_large(self):
        self.assertEqual(self.sol.findTargetSumWays([1, 1], 3), 0)

    def test_negative_target(self):
        self.assertEqual(self.sol.findTargetSumWays([1], -1), 1)
        self.assertEqual(self.sol.findTargetSumWays([1, 1, 1, 1, 1], -3), 5)

    def test_target_zero(self):
        self.assertEqual(self.sol.findTargetSumWays([1, 1, 1], 0), 0)
        self.assertEqual(self.sol.findTargetSumWays([1, 1], 0), 2)
        self.assertEqual(self.sol.findTargetSumWays([0, 0, 1], 0), 0)

    def test_all_zeros(self):
        self.assertEqual(self.sol.findTargetSumWays([0, 0, 0, 0], 0), 16)
        self.assertEqual(self.sol.findTargetSumWays([0, 0], 1), 0)

    def test_mixed_zeros(self):
        self.assertEqual(self.sol.findTargetSumWays([0, 0, 1, 1, 1], 1), 12)

    def test_parity_mismatch(self):
        self.assertEqual(self.sol.findTargetSumWays([1, 1, 1], 2), 0)
        self.assertEqual(self.sol.findTargetSumWays([1, 1, 1], -2), 0)

    def test_larger_numbers(self):
        self.assertEqual(self.sol.findTargetSumWays([100, 100, 100], 100), 3)
        self.assertEqual(self.sol.findTargetSumWays([100, 100], 0), 2)
        self.assertEqual(self.sol.findTargetSumWays([100, 100, 100], 300), 1)

    def test_max_negative_target(self):
        self.assertEqual(self.sol.findTargetSumWays([200, 200], -400), 1)
        self.assertEqual(self.sol.findTargetSumWays([200, 200], 401), 0)

    def test_brute_force_cross_check(self):
        import itertools, random

        random.seed(42)

        def brute(nums, target):
            count = 0
            for signs in itertools.product((-1, 1), repeat=len(nums)):
                if sum(s * n for s, n in zip(signs, nums)) == target:
                    count += 1
            return count

        for _ in range(200):
            n = random.randint(1, 10)
            nums = [random.randint(0, 15) for _ in range(n)]
            target = random.randint(-20, 20)
            expected = brute(nums, target)
            got = self.sol.findTargetSumWays(nums, target)
            self.assertEqual(got, expected, f"nums={nums}, target={target}")


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Backtracking, Knapsack Problem, 0-1 Knapsack
