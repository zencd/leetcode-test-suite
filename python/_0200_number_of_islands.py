# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Medium

from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        raise Exception("Not solved yet")


import unittest


def make_grid(rows):
    return [list(row) for row in rows]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        grid = make_grid(
            [
                "11110",
                "11010",
                "11000",
                "00000",
            ]
        )
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_example_two(self):
        grid = make_grid(
            [
                "11000",
                "11000",
                "00100",
                "00011",
            ]
        )
        self.assertEqual(self.solution.numIslands(grid), 3)

    def test_all_water(self):
        grid = make_grid(
            [
                "000",
                "000",
                "000",
            ]
        )
        self.assertEqual(self.solution.numIslands(grid), 0)

    def test_all_land(self):
        grid = make_grid(
            [
                "111",
                "111",
                "111",
            ]
        )
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_single_land_cell(self):
        grid = make_grid(["1"])
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_single_water_cell(self):
        grid = make_grid(["0"])
        self.assertEqual(self.solution.numIslands(grid), 0)

    def test_isolated_diagonal_islands(self):
        grid = make_grid(
            [
                "101",
                "010",
                "101",
            ]
        )
        self.assertEqual(self.solution.numIslands(grid), 5)

    def test_checkerboard_two_islands(self):
        grid = make_grid(
            [
                "101",
                "010",
            ]
        )
        self.assertEqual(self.solution.numIslands(grid), 3)

    def test_single_row(self):
        grid = make_grid(["11010"])
        self.assertEqual(self.solution.numIslands(grid), 2)

    def test_single_column(self):
        grid = make_grid(
            [
                "1",
                "1",
                "0",
                "1",
            ]
        )
        self.assertEqual(self.solution.numIslands(grid), 2)

    def test_cross_shape(self):
        grid = make_grid(
            [
                "010",
                "111",
                "010",
            ]
        )
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_l_shape_island(self):
        grid = make_grid(
            [
                "10",
                "11",
            ]
        )
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_ring_shape_island(self):
        grid = make_grid(
            [
                "111",
                "101",
                "111",
            ]
        )
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_two_islands_same_row(self):
        grid = make_grid(
            [
                "101",
                "101",
            ]
        )
        self.assertEqual(self.solution.numIslands(grid), 2)

    def test_two_islands_same_column(self):
        grid = make_grid(
            [
                "10",
                "10",
                "01",
                "01",
            ]
        )
        self.assertEqual(self.solution.numIslands(grid), 2)

    def test_input_not_mutated(self):
        grid = make_grid(
            [
                "11110",
                "11010",
                "11000",
                "00000",
            ]
        )
        original = [row[:] for row in grid]
        self.solution.numIslands(grid)
        self.assertEqual(grid, original)

    def test_wide_grid(self):
        grid = make_grid(["10" * 150])
        self.assertEqual(self.solution.numIslands(grid), 150)

    def test_very_large_island(self):
        grid = [["1"] * 300 for _ in range(300)]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_all_land_large(self):
        grid = [["1"] for _ in range(300)]
        self.assertEqual(self.solution.numIslands(grid), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
