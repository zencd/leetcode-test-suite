# 403. Frog Jump
# https://leetcode.com/problems/frog-jump/
# Hard

from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1_true(self):
        self.assertTrue(self.sol.canCross([0, 1, 3, 5, 6, 8, 12, 17]))

    def test_example2_false(self):
        self.assertFalse(self.sol.canCross([0, 1, 2, 3, 4, 8, 9, 11]))

    def test_two_stones_adjacent(self):
        self.assertTrue(self.sol.canCross([0, 1]))

    def test_two_stones_gap_too_large(self):
        self.assertFalse(self.sol.canCross([0, 2]))

    def test_second_stone_not_one(self):
        self.assertFalse(self.sol.canCross([0, 3]))

    def test_single_stone(self):
        self.assertFalse(self.sol.canCross([0]))

    def test_three_stones(self):
        self.assertTrue(self.sol.canCross([0, 1, 2]))
        self.assertTrue(self.sol.canCross([0, 1, 3]))

    def test_consecutive_stones(self):
        self.assertTrue(self.sol.canCross([0, 1, 2, 3, 4, 5, 6, 7]))

    def test_need_k_plus_one(self):
        self.assertTrue(self.sol.canCross([0, 1, 2, 4, 7]))

    def test_need_k_minus_one(self):
        self.assertTrue(self.sol.canCross([0, 1, 2, 4, 7, 9]))

    def test_long_gap_breaks(self):
        self.assertFalse(self.sol.canCross([0, 1, 3, 5, 9, 12]))

    def test_large_positions(self):
        stones = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
        self.assertTrue(self.sol.canCross(stones))

    def test_alternating_paths(self):
        self.assertTrue(self.sol.canCross([0, 1, 2, 3, 5, 6, 8]))
        self.assertTrue(self.sol.canCross([0, 1, 2, 3, 5, 7, 8]))

    def test_branching_required(self):
        self.assertTrue(self.sol.canCross([0, 1, 3, 4, 6, 7, 9, 12]))

    def test_impossible_branch(self):
        self.assertFalse(self.sol.canCross([0, 1, 2, 4, 7, 8]))

    def test_large_stone_values(self):
        big = 10**9
        stones = [0, 1, 3, big]
        self.assertFalse(self.sol.canCross(stones))

    def test_long_feasible_chain(self):
        stones = [0, 1]
        k = 1
        for i in range(50):
            k += 1
            stones.append(stones[-1] + k)
        self.assertTrue(self.sol.canCross(stones))

    def test_input_not_mutated(self):
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        snapshot = list(stones)
        self.sol.canCross(stones)
        self.assertEqual(stones, snapshot)

    def test_duplicate_free_guarantee(self):
        self.assertTrue(self.sol.canCross([0, 1, 2]))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming
