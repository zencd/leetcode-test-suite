# 63. Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/
# Medium

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(
            self.s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2
        )

    def test_example2(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[0, 1], [0, 0]]), 1)

    def test_single_cell_no_obstacle(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[0]]), 1)

    def test_single_cell_obstacle(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[1]]), 0)

    def test_start_obstacle(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[1, 0], [0, 0]]), 0)

    def test_end_obstacle(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[0, 0], [0, 1]]), 0)

    def test_first_row_blocked(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[1, 1], [1, 1]]), 0)

    def test_full_block_cross(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[0, 1], [1, 0]]), 0)

    def test_one_dimension_row(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[0, 0, 0]]), 1)

    def test_one_dimension_row_blocked(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[0, 1, 0]]), 0)

    def test_one_dimension_col(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[0], [0], [0]]), 1)

    def test_one_dimension_col_blocked(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[0], [1], [0]]), 0)

    def test_no_obstacles_2x2(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[0, 0], [0, 0]]), 2)

    def test_no_obstacles_3x3(self):
        self.assertEqual(
            self.s.uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 6
        )

    def test_no_obstacles_3x7(self):
        self.assertEqual(
            self.s.uniquePathsWithObstacles([[0] * 7 for _ in range(3)]), 28
        )

    def test_all_obstacles(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[1, 1], [1, 1]]), 0)

    def test_blocked_first_row_partial(self):
        self.assertEqual(
            self.s.uniquePathsWithObstacles([[0, 1, 0], [0, 0, 0], [0, 0, 0]]), 3
        )

    def test_blocked_first_col_partial(self):
        self.assertEqual(
            self.s.uniquePathsWithObstacles([[0, 0, 0], [1, 0, 0], [1, 0, 0]]), 3
        )

    def test_obstacle_corner_bottom_left(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[0, 0], [1, 0]]), 1)

    def test_wide_grid(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[0] * 101]), 1)

    def test_tall_grid(self):
        self.assertEqual(self.s.uniquePathsWithObstacles([[0] for _ in range(101)]), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Matrix
