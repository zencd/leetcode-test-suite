# 407. Trapping Rain Water II
# https://leetcode.com/problems/trapping-rain-water-ii/
# Hard

from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.sol.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]),
            4,
        )

    def test_example_2(self):
        self.assertEqual(
            self.sol.trapRainWater(
                [
                    [3, 3, 3, 3, 3],
                    [3, 2, 2, 2, 3],
                    [3, 2, 1, 2, 3],
                    [3, 2, 2, 2, 3],
                    [3, 3, 3, 3, 3],
                ]
            ),
            10,
        )

    def test_single_row(self):
        self.assertEqual(self.sol.trapRainWater([[1, 2, 3, 0, 5]]), 0)

    def test_single_column(self):
        self.assertEqual(self.sol.trapRainWater([[1], [2], [3], [0]]), 0)

    def test_single_cell(self):
        self.assertEqual(self.sol.trapRainWater([[5]]), 0)

    def test_two_rows(self):
        self.assertEqual(self.sol.trapRainWater([[5, 1, 5], [5, 1, 5]]), 0)

    def test_two_cols(self):
        self.assertEqual(self.sol.trapRainWater([[5, 1], [5, 1], [5, 1]]), 0)

    def test_no_water_flat(self):
        self.assertEqual(self.sol.trapRainWater([[1, 1, 1], [1, 1, 1]]), 0)

    def test_no_water_monotonic(self):
        self.assertEqual(
            self.sol.trapRainWater([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]),
            0,
        )

    def test_zero_heights(self):
        self.assertEqual(
            self.sol.trapRainWater(
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                ]
            ),
            1,
        )

    def test_single_pit(self):
        grid = [[5, 5, 5], [5, 3, 5], [5, 5, 5]]
        self.assertEqual(self.sol.trapRainWater(grid), 2)

    def test_multiple_pits(self):
        grid = [
            [5, 5, 5, 5, 5, 5],
            [5, 2, 2, 2, 2, 5],
            [5, 2, 1, 2, 2, 5],
            [5, 2, 2, 1, 2, 5],
            [5, 2, 2, 2, 2, 5],
            [5, 5, 5, 5, 5, 5],
        ]
        self.assertEqual(self.sol.trapRainWater(grid), 50)

    def test_water_spilling_out(self):
        grid = [
            [1, 1, 1],
            [1, 5, 1],
            [1, 1, 1],
        ]
        self.assertEqual(self.sol.trapRainWater(grid), 0)

    def test_water_level_limited_by_opening(self):
        grid = [
            [3, 3, 3, 3],
            [3, 0, 1, 2],
            [3, 0, 2, 2],
            [3, 3, 3, 3],
        ]
        self.assertEqual(self.sol.trapRainWater(grid), 5)

    def test_large_heights(self):
        grid = [
            [20000, 20000, 20000],
            [20000, 0, 20000],
            [20000, 20000, 20000],
        ]
        self.assertEqual(self.sol.trapRainWater(grid), 20000)

    def test_non_square(self):
        grid = [
            [3, 3, 3, 3, 3, 3],
            [3, 1, 2, 1, 2, 3],
            [3, 0, 2, 2, 1, 3],
            [3, 3, 3, 3, 3, 3],
        ]
        self.assertEqual(self.sol.trapRainWater(grid), 13)

    def test_already_full_interior(self):
        grid = [
            [3, 3, 3],
            [3, 5, 3],
            [3, 3, 3],
        ]
        self.assertEqual(self.sol.trapRainWater(grid), 0)

    def test_interior_higher_than_walls(self):
        grid = [
            [2, 2, 2],
            [2, 7, 2],
            [2, 2, 2],
        ]
        self.assertEqual(self.sol.trapRainWater(grid), 0)

    def test_mixed_water_heights(self):
        grid = [
            [4, 4, 4, 4, 4],
            [4, 1, 2, 3, 4],
            [4, 3, 2, 1, 4],
            [4, 4, 4, 4, 4],
        ]
        self.assertEqual(self.sol.trapRainWater(grid), 12)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Breadth-First Search, Heap (Priority Queue), Matrix
