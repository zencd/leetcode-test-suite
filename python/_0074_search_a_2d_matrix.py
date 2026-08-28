# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
# Medium

import unittest
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1_target_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(self.solution.searchMatrix(matrix, 3))

    def test_example_2_target_not_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertFalse(self.solution.searchMatrix(matrix, 13))

    def test_single_element_present(self):
        self.assertTrue(self.solution.searchMatrix([[5]], 5))

    def test_single_element_absent(self):
        self.assertFalse(self.solution.searchMatrix([[5]], 6))

    def test_first_element(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(self.solution.searchMatrix(matrix, 1))

    def test_last_element(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(self.solution.searchMatrix(matrix, 60))

    def test_element_on_row_boundary(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(self.solution.searchMatrix(matrix, 10))
        self.assertTrue(self.solution.searchMatrix(matrix, 23))

    def test_target_below_min(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertFalse(self.solution.searchMatrix(matrix, 0))

    def test_target_above_max(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertFalse(self.solution.searchMatrix(matrix, 61))

    def test_target_between_rows(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertFalse(self.solution.searchMatrix(matrix, 8))
        self.assertFalse(self.solution.searchMatrix(matrix, 19))
        self.assertFalse(self.solution.searchMatrix(matrix, 35))

    def test_single_row(self):
        matrix = [[1, 2, 3, 4, 5]]
        self.assertTrue(self.solution.searchMatrix(matrix, 4))
        self.assertFalse(self.solution.searchMatrix(matrix, 6))

    def test_single_column(self):
        matrix = [[1], [2], [3], [4]]
        self.assertTrue(self.solution.searchMatrix(matrix, 3))
        self.assertFalse(self.solution.searchMatrix(matrix, 5))

    def test_negative_values(self):
        matrix = [[-5, -3, -1], [2, 4, 6]]
        self.assertTrue(self.solution.searchMatrix(matrix, -3))
        self.assertTrue(self.solution.searchMatrix(matrix, 2))
        self.assertFalse(self.solution.searchMatrix(matrix, -4))

    def test_zero_target(self):
        matrix = [[-1, 0, 1], [2, 3, 4]]
        self.assertTrue(self.solution.searchMatrix(matrix, 0))
        self.assertFalse(self.solution.searchMatrix(matrix, -2))

    def test_boundary_extremes(self):
        matrix = [[-10000, -9999], [9999, 10000]]
        self.assertFalse(self.solution.searchMatrix(matrix, 0))

    def test_boundary_extremes_found(self):
        matrix = [[-10000, -9999], [9999, 10000]]
        self.assertTrue(self.solution.searchMatrix(matrix, -10000))
        self.assertTrue(self.solution.searchMatrix(matrix, 10000))

    def test_wide_matrix(self):
        matrix = [[i for i in range(100)]]
        self.assertTrue(self.solution.searchMatrix(matrix, 99))
        self.assertFalse(self.solution.searchMatrix(matrix, 100))

    def test_tall_matrix(self):
        matrix = [[i] for i in range(100)]
        self.assertTrue(self.solution.searchMatrix(matrix, 99))
        self.assertFalse(self.solution.searchMatrix(matrix, 100))

    def test_repeated_values_in_row(self):
        matrix = [[1, 1, 5, 7], [10, 11, 16, 20]]
        self.assertTrue(self.solution.searchMatrix(matrix, 1))
        self.assertTrue(self.solution.searchMatrix(matrix, 5))
        self.assertFalse(self.solution.searchMatrix(matrix, 2))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search, Matrix
