# 240. Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/
# Medium

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1_target_found(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ]
        self.assertTrue(self.solution.searchMatrix(matrix, 5))

    def test_example2_target_not_found(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ]
        self.assertFalse(self.solution.searchMatrix(matrix, 20))

    def test_target_at_top_left(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertTrue(self.solution.searchMatrix(matrix, 1))

    def test_target_at_bottom_right(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertTrue(self.solution.searchMatrix(matrix, 9))

    def test_target_in_middle(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertTrue(self.solution.searchMatrix(matrix, 5))

    def test_target_absent_between_values(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertFalse(self.solution.searchMatrix(matrix, 10))

    def test_target_below_all_values(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertFalse(self.solution.searchMatrix(matrix, 0))

    def test_single_element_found(self):
        self.assertTrue(self.solution.searchMatrix([[7]], 7))

    def test_single_element_not_found(self):
        self.assertFalse(self.solution.searchMatrix([[7]], 8))

    def test_single_row_found(self):
        self.assertTrue(self.solution.searchMatrix([[1, 3, 5, 7]], 5))

    def test_single_row_not_found(self):
        self.assertFalse(self.solution.searchMatrix([[1, 3, 5, 7]], 4))

    def test_single_column_found(self):
        self.assertTrue(self.solution.searchMatrix([[2], [4], [6]], 4))

    def test_single_column_not_found(self):
        self.assertFalse(self.solution.searchMatrix([[2], [4], [6]], 5))

    def test_negative_values_found(self):
        matrix = [
            [-5, -3, -1],
            [-4, 0, 2],
            [-2, 1, 4],
        ]
        self.assertTrue(self.solution.searchMatrix(matrix, -4))

    def test_negative_values_not_found(self):
        matrix = [
            [-5, -3, -1],
            [-4, 0, 2],
            [-2, 1, 4],
        ]
        self.assertFalse(self.solution.searchMatrix(matrix, -6))

    def test_duplicate_values_found(self):
        matrix = [[1, 1, 3], [1, 3, 5], [3, 5, 7]]
        self.assertTrue(self.solution.searchMatrix(matrix, 1))

    def test_duplicate_values_not_found(self):
        matrix = [[1, 1, 3], [1, 3, 5], [3, 5, 7]]
        self.assertFalse(self.solution.searchMatrix(matrix, 2))

    def test_large_values(self):
        matrix = [[-(10**9), 0], [0, 10**9]]
        self.assertTrue(self.solution.searchMatrix(matrix, 10**9))
        self.assertTrue(self.solution.searchMatrix(matrix, -(10**9)))
        self.assertFalse(self.solution.searchMatrix(matrix, 999999999))

    def test_wide_matrix(self):
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8]]
        self.assertTrue(self.solution.searchMatrix(matrix, 8))
        self.assertFalse(self.solution.searchMatrix(matrix, 9))

    def test_tall_matrix(self):
        matrix = [[1], [2], [3], [4], [5]]
        self.assertTrue(self.solution.searchMatrix(matrix, 3))
        self.assertFalse(self.solution.searchMatrix(matrix, 6))

    def test_empty_matrix(self):
        self.assertFalse(self.solution.searchMatrix([], 5))

    def test_matrix_with_empty_row(self):
        self.assertFalse(self.solution.searchMatrix([[]], 5))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search, Divide and Conquer, Matrix
