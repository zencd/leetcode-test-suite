# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/
# Medium

import unittest
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        raise Exception("Not solved yet")


class TestSetMatrixZeroes(unittest.TestCase):
    def test_single_zero_in_center(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    def test_example_two(self):
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])

    def test_no_zeros(self):
        matrix = [[1, 2], [3, 4]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[1, 2], [3, 4]])

    def test_all_zeros(self):
        matrix = [[0, 0], [0, 0]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[0, 0], [0, 0]])

    def test_single_element_zero(self):
        matrix = [[0]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[0]])

    def test_single_element_nonzero(self):
        matrix = [[5]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[5]])

    def test_zero_in_first_row(self):
        matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[0, 0, 0], [0, 4, 5], [0, 7, 8]])

    def test_zero_in_first_column(self):
        matrix = [[1, 2], [0, 4], [6, 8]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[0, 2], [0, 0], [0, 8]])

    def test_zero_in_last_row_last_col(self):
        matrix = [[1, 2], [3, 0]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[1, 0], [0, 0]])

    def test_entire_first_row_zero(self):
        matrix = [[0, 0], [1, 2], [3, 4]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[0, 0], [0, 0], [0, 0]])

    def test_entire_column_zero(self):
        matrix = [[1, 0, 2], [3, 0, 5], [6, 0, 8]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_single_row_multiple_zeros(self):
        matrix = [[1, 0, 0, 2]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[0, 0, 0, 0]])

    def test_single_column_multiple_zeros(self):
        matrix = [[1], [0], [3], [0]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[0], [0], [0], [0]])

    def test_negative_values(self):
        matrix = [[-1, 0], [2, -3]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[0, 0], [2, 0]])

    def test_diagonal_zeros(self):
        matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[1, 0, 3], [0, 0, 0], [7, 0, 9]])

    def test_in_place_modification(self):
        matrix = [[1, 2], [3, 0]]
        result = Solution().setZeroes(matrix)
        self.assertIsNone(result)
        self.assertEqual(matrix, [[1, 0], [0, 0]])

    def test_large_zero_spread(self):
        matrix = [[2, 1, 0], [0, 1, 2], [4, 3, 2]]
        Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[0, 0, 0], [0, 0, 0], [0, 3, 0]])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Matrix
