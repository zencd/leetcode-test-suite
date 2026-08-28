# 398. Random Pick Index
# https://leetcode.com/problems/random-pick-index/
# Medium

from typing import List
import random


class Solution:
    def __init__(self, nums: List[int]):
        raise Exception("Not solved yet")

    def pick(self, target: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_single_element(self):
        sol = Solution([1])
        for _ in range(10):
            self.assertEqual(sol.pick(1), 0)

    def test_unique_target(self):
        sol = Solution([1, 2, 3, 4])
        for t, expected in [(1, 0), (2, 1), (3, 2), (4, 3)]:
            for _ in range(10):
                self.assertEqual(sol.pick(t), expected)

    def test_all_same(self):
        sol = Solution([7, 7, 7, 7])
        for _ in range(100):
            idx = sol.pick(7)
            self.assertIn(idx, (0, 1, 2, 3))

    def test_returns_valid_index(self):
        sol = Solution([1, 2, 3, 3, 3])
        for _ in range(200):
            idx = sol.pick(3)
            self.assertIn(idx, (2, 3, 4))
        for _ in range(100):
            self.assertEqual(sol.pick(1), 0)

    def test_negative_numbers(self):
        sol = Solution([-5, 3, -5, 0, -5])
        for _ in range(300):
            self.assertIn(sol.pick(-5), (0, 2, 4))
        self.assertEqual(sol.pick(3), 1)
        self.assertEqual(sol.pick(0), 3)

    def test_extreme_values(self):
        lo = -(2**31)
        hi = 2**31 - 1
        sol = Solution([lo, hi, lo, hi])
        for _ in range(100):
            self.assertIn(sol.pick(lo), (0, 2))
            self.assertIn(sol.pick(hi), (1, 3))

    def test_zero_as_value(self):
        sol = Solution([0, 0])
        for _ in range(50):
            self.assertIn(sol.pick(0), (0, 1))

    def test_distribution_uniformity(self):
        random.seed(42)
        m = 100
        nums = [9] * m
        sol = Solution(nums)
        counts = {i: 0 for i in range(m)}
        trials = 20000
        for _ in range(trials):
            counts[sol.pick(9)] += 1
        expected = trials / m
        for i, c in counts.items():
            self.assertGreater(c, expected * 0.6)
            self.assertLess(c, expected * 1.4)

    def test_distribution_two_candidates(self):
        random.seed(123)
        sol = Solution([4, 8, 4])
        counts = {0: 0, 2: 0}
        trials = 20000
        for _ in range(trials):
            counts[sol.pick(4)] += 1
        self.assertGreater(counts[0], trials / 2 - trials * 0.1)
        self.assertGreater(counts[2], trials / 2 - trials * 0.1)
        self.assertLess(counts[0], trials / 2 + trials * 0.1)
        self.assertLess(counts[2], trials / 2 + trials * 0.1)

    def test_mixed_targets(self):
        sol = Solution([1, 2, 2, 3, 3, 3])
        for _ in range(1000):
            self.assertIn(sol.pick(3), (3, 4, 5))
            self.assertIn(sol.pick(2), (1, 2))
            self.assertIn(sol.pick(1), (0,))

    def test_large_array(self):
        n = 20000
        nums = [i % 7 for i in range(n)]
        random.seed(7)
        sol = Solution(nums)
        for _ in range(200):
            t = random.randrange(7)
            self.assertEqual(nums[sol.pick(t)], t)

    def test_duplicates_adjacent(self):
        sol = Solution([5, 5, 6, 6, 5])
        for _ in range(200):
            self.assertIn(sol.pick(5), (0, 1, 4))
            self.assertIn(sol.pick(6), (2, 3))


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Math, Reservoir Sampling, Randomized
