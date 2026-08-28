# 174. Dungeon Game
# https://leetcode.com/problems/dungeon-game/
# Hard

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 7)

    def test_example2_single_zero(self):
        self.assertEqual(self.sol.calculateMinimumHP([[0]]), 1)

    def test_single_negative(self):
        self.assertEqual(self.sol.calculateMinimumHP([[-5]]), 6)

    def test_single_positive(self):
        self.assertEqual(self.sol.calculateMinimumHP([[10]]), 1)

    def test_single_one(self):
        self.assertEqual(self.sol.calculateMinimumHP([[1]]), 1)

    def test_row_of_negatives(self):
        dungeon = [[-1, -2, -3]]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 7)

    def test_column_of_negatives(self):
        dungeon = [[-1], [-2], [-3]]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 7)

    def test_all_negatives(self):
        dungeon = [[-1, -1], [-1, -1]]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 4)

    def test_all_positive(self):
        dungeon = [[5, 5], [5, 5]]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 1)

    def test_mixed_path_choice_right(self):
        dungeon = [[-2, 3], [-5, -10]]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 10)

    def test_mixed_path_choice_down(self):
        dungeon = [[-2, -10], [3, -5]]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 5)

    def test_long_row(self):
        dungeon = [[-1] * 200]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 201)

    def test_long_column(self):
        dungeon = [[-1] for _ in range(200)]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 201)

    def test_orb_in_last_cell(self):
        dungeon = [[-3, -5], [-2, 4]]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 6)

    def test_max_negative_grid(self):
        dungeon = [[-1000, -1000], [-1000, -1000]]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 3001)

    def test_larger_mixed_grid(self):
        dungeon = [[7, 8, 9], [1, 2, 3], [1, 1, 1]]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 1)

    def test_boundary_optimal_route(self):
        dungeon = [[-1000, 1000, -1000], [-1000, 1000, -1000], [-1000, 1000, -1000]]
        expected = 1001
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), expected)

    def test_wide_grid(self):
        dungeon = [[-1, 0, -1, 0, -1]]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 4)

    def test_tall_grid(self):
        dungeon = [[1], [-2], [3], [-4]]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 3)

    def test_symmetric_negative_grid(self):
        dungeon = [[-2, -3], [-3, -2]]
        self.assertEqual(self.sol.calculateMinimumHP(dungeon), 8)

    def test_big_grid_stress(self):
        import random

        rng = random.Random(174)
        grid = [[rng.randint(-1000, 1000) for _ in range(50)] for _ in range(50)]
        self.assertGreaterEqual(self.sol.calculateMinimumHP(grid), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Matrix
