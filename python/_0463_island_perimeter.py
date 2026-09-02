# 463. Island Perimeter
# https://leetcode.com/problems/island-perimeter/
# Easy

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        self.assertEqual(self.sol.islandPerimeter(grid), 16)

    def test_example_2_single_cell(self):
        grid = [[1]]
        self.assertEqual(self.sol.islandPerimeter(grid), 4)

    def test_example_3_two_cells_horizontal(self):
        grid = [[1, 0]]
        self.assertEqual(self.sol.islandPerimeter(grid), 4)

    def test_single_cell_land(self):
        grid = [[1]]
        self.assertEqual(self.sol.islandPerimeter(grid), 4)

    def test_two_horizontal(self):
        grid = [[1, 1]]
        self.assertEqual(self.sol.islandPerimeter(grid), 6)

    def test_two_vertical(self):
        grid = [[1], [1]]
        self.assertEqual(self.sol.islandPerimeter(grid), 6)

    def test_two_diagonal(self):
        grid = [[1, 0], [0, 1]]
        self.assertEqual(self.sol.islandPerimeter(grid), 8)

    def test_2x2_block(self):
        grid = [[1, 1], [1, 1]]
        self.assertEqual(self.sol.islandPerimeter(grid), 8)

    def test_line_horizontal(self):
        grid = [[1, 1, 1, 1]]
        self.assertEqual(self.sol.islandPerimeter(grid), 10)

    def test_line_vertical(self):
        grid = [[1], [1], [1], [1]]
        self.assertEqual(self.sol.islandPerimeter(grid), 10)

    def test_l_shape(self):
        grid = [[1, 1], [1, 0]]
        self.assertEqual(self.sol.islandPerimeter(grid), 8)

    def test_t_shape(self):
        grid = [[1, 1, 1], [0, 1, 0]]
        self.assertEqual(self.sol.islandPerimeter(grid), 10)

    def test_ring_with_corner(self):
        grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        self.assertEqual(self.sol.islandPerimeter(grid), 16)

    def test_single_in_corner(self):
        grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(self.sol.islandPerimeter(grid), 4)

    def test_island_at_edge(self):
        grid = [[1, 0], [1, 0], [0, 1]]
        self.assertEqual(self.sol.islandPerimeter(grid), 10)

    def test_single_row_mixed(self):
        grid = [[0, 1, 1, 0, 1]]
        self.assertEqual(self.sol.islandPerimeter(grid), 10)

    def test_single_col_mixed(self):
        grid = [[0], [1], [1], [0], [1]]
        self.assertEqual(self.sol.islandPerimeter(grid), 10)

    def test_full_grid(self):
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(self.sol.islandPerimeter(grid), 12)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Depth-First Search, Breadth-First Search, Matrix
