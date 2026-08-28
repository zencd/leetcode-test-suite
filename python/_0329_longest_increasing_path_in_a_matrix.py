# 329. Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Hard

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def check(self, matrix, expected):
        self.assertEqual(self.s.longestIncreasingPath(matrix), expected)

    def test_example1(self):
        self.check([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4)

    def test_example2(self):
        self.check([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4)

    def test_example3(self):
        self.check([[1]], 1)

    def test_single_row(self):
        self.check([[1, 2, 3, 4]], 4)

    def test_single_row_decreasing(self):
        self.check([[4, 3, 2, 1]], 4)

    def test_single_column(self):
        self.check([[1], [2], [3]], 3)

    def test_single_column_decreasing(self):
        self.check([[5], [4], [3]], 3)

    def test_all_equal(self):
        self.check([[7, 7], [7, 7]], 1)

    def test_2x2_increasing_diagonal_blocked(self):
        self.check([[1, 2], [3, 4]], 3)

    def test_zigzag_grid(self):
        self.check(
            [
                [1, 5, 9, 13],
                [15, 14, 8, 7],
                [6, 10, 11, 12],
                [16, 17, 18, 19],
            ],
            5,
        )

    def test_zigzag_single(self):
        self.check([[3, 4, 2], [5, 4, 7], [9, 8, 11], [6, 2, 2]], 3)

    def test_path_requires_non_adjacent_moves(self):
        self.check([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5)

    def test_negative_values(self):
        self.check([[-1, -2], [-3, -4]], 3)

    def test_mixed_negative_positive(self):
        self.check([[-5, -1, -3], [0, -2, 4], [-7, 1, 8]], 3)

    def test_max_value_boundary(self):
        big = 2**31 - 1
        self.check([[big, 1], [0, big]], 2)

    def test_large_matrix_smoke(self):
        m, n = 50, 50
        matrix = [[(i * n + j) % 1000 for j in range(n)] for i in range(m)]
        self.assertGreaterEqual(self.s.longestIncreasingPath(matrix), 1)

    def test_empty_matrix(self):
        self.assertEqual(self.s.longestIncreasingPath([]), 0)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Memoization, Matrix, Directed Acyclic Graph
