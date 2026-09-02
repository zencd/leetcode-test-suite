# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/
# Medium

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestMinPathSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(
            self.solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]),
            7,
        )

    def test_example2(self):
        self.assertEqual(
            self.solution.minPathSum([[1, 2, 3], [4, 5, 6]]),
            12,
        )

    def test_single_cell(self):
        self.assertEqual(self.solution.minPathSum([[5]]), 5)

    def test_single_cell_zero(self):
        self.assertEqual(self.solution.minPathSum([[0]]), 0)

    def test_single_row(self):
        self.assertEqual(self.solution.minPathSum([[1, 2, 3, 4]]), 10)

    def test_single_column(self):
        self.assertEqual(self.solution.minPathSum([[1], [2], [3], [4]]), 10)

    def test_single_row_zeros(self):
        self.assertEqual(self.solution.minPathSum([[0, 0, 0]]), 0)

    def test_single_column_zeros(self):
        self.assertEqual(self.solution.minPathSum([[0], [0], [0]]), 0)

    def test_all_zeros(self):
        self.assertEqual(
            self.solution.minPathSum([[0, 0], [0, 0]]),
            0,
        )

    def test_2x2(self):
        self.assertEqual(self.solution.minPathSum([[1, 2], [3, 4]]), 7)

    def test_path_along_right_then_down(self):
        self.assertEqual(
            self.solution.minPathSum([[1, 2, 100], [100, 100, 1]]),
            104,
        )

    def test_path_along_down_then_right(self):
        self.assertEqual(
            self.solution.minPathSum([[1, 100, 100], [1, 1, 1]]),
            4,
        )

    def test_max_values(self):
        grid = [[200] * 200 for _ in range(200)]
        expected = (200 + 200 - 1) * 200
        self.assertEqual(self.solution.minPathSum(grid), expected)

    def test_rectangular_wide(self):
        self.assertEqual(
            self.solution.minPathSum([[1, 1, 1, 1], [5, 5, 5, 5]]),
            9,
        )

    def test_rectangular_tall(self):
        self.assertEqual(
            self.solution.minPathSum([[1, 5], [1, 5], [1, 5]]),
            8,
        )

    def test_grid_not_mutated(self):
        grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        expected = [row[:] for row in grid]
        self.solution.minPathSum(grid)
        self.assertEqual(grid, expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Matrix
