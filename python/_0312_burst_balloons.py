# 312. Burst Balloons
# https://leetcode.com/problems/burst-balloons/
# Hard

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.maxCoins([3, 1, 5, 8]), 167)

    def test_example_2(self):
        self.assertEqual(self.sol.maxCoins([1, 5]), 10)

    def test_single_balloon(self):
        self.assertEqual(self.sol.maxCoins([5]), 5)

    def test_single_one(self):
        self.assertEqual(self.sol.maxCoins([1]), 1)

    def test_two_ones(self):
        self.assertEqual(self.sol.maxCoins([1, 1]), 2)

    def test_two_equal(self):
        self.assertEqual(self.sol.maxCoins([10, 10]), 110)

    def test_three_ones(self):
        self.assertEqual(self.sol.maxCoins([1, 1, 1]), 3)

    def test_three(self):
        self.assertEqual(self.sol.maxCoins([2, 3, 4]), 36)

    def test_zero_values(self):
        self.assertEqual(self.sol.maxCoins([0, 1]), 1)

    def test_all_zeros(self):
        self.assertEqual(self.sol.maxCoins([0, 0, 0]), 0)

    def test_empty_list(self):
        self.assertEqual(self.sol.maxCoins([]), 0)

    def test_max_values(self):
        nums = [100] * 6
        expected = self._brute_max_coins(nums)
        self.assertEqual(self.sol.maxCoins(nums), expected)

    def test_max_length(self):
        self.assertEqual(self.sol.maxCoins([1] * 300), 300)

    def test_random_small_cases(self):
        import random

        random.seed(42)
        for _ in range(20):
            n = random.randint(1, 6)
            nums = [random.randint(1, 10) for _ in range(n)]
            self.assertEqual(
                self.sol.maxCoins(nums),
                self._brute_max_coins(nums),
                f"mismatch for {nums}",
            )

    @staticmethod
    def _brute_max_coins(nums: List[int]) -> int:
        from itertools import permutations

        best = 0
        for perm in permutations(range(len(nums))):
            coins = 0
            remaining = list(range(len(nums)))
            for idx in perm:
                pos = remaining.index(idx)
                left = nums[remaining[pos - 1]] if pos > 0 else 1
                right = nums[remaining[pos + 1]] if pos + 1 < len(remaining) else 1
                coins += left * nums[idx] * right
                remaining.pop(pos)
            best = max(best, coins)
        return best


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming
