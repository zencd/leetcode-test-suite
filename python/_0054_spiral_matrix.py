# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Medium

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_3x3(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.solution.spiralOrder(matrix), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_example_3x4(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        self.assertEqual(
            self.solution.spiralOrder(matrix), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        )

    def test_one_element(self):
        self.assertEqual(self.solution.spiralOrder([[7]]), [7])

    def test_single_row(self):
        self.assertEqual(self.solution.spiralOrder([[1, 2, 3, 4]]), [1, 2, 3, 4])

    def test_single_column(self):
        self.assertEqual(self.solution.spiralOrder([[1], [2], [3], [4]]), [1, 2, 3, 4])

    def test_two_rows_three_cols(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(self.solution.spiralOrder(matrix), [1, 2, 3, 6, 5, 4])

    def test_two_columns_three_rows(self):
        matrix = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(self.solution.spiralOrder(matrix), [1, 2, 4, 6, 5, 3])

    def test_two_by_two(self):
        self.assertEqual(self.solution.spiralOrder([[1, 2], [3, 4]]), [1, 2, 4, 3])

    def test_square_4x4(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
        expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_negative_values(self):
        matrix = [[-1, -2], [-3, -4]]
        self.assertEqual(self.solution.spiralOrder(matrix), [-1, -2, -4, -3])

    def test_max_boundary_values(self):
        matrix = [[100, -100], [-100, 100]]
        self.assertEqual(self.solution.spiralOrder(matrix), [100, -100, 100, -100])

    def test_5x2(self):
        matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        expected = [1, 2, 4, 6, 8, 10, 9, 7, 5, 3]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_2x5(self):
        matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        expected = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_duplicated_values(self):
        matrix = [[5, 5], [5, 5]]
        self.assertEqual(self.solution.spiralOrder(matrix), [5, 5, 5, 5])

    def test_result_length_matches_matrix_size(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        result = self.solution.spiralOrder(matrix)
        self.assertEqual(len(result), 6)
        self.assertEqual(sorted(result), sorted([1, 2, 3, 4, 5, 6]))

    def test_original_matrix_not_modified(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        original = [row[:] for row in matrix]
        self.solution.spiralOrder(matrix)
        self.assertEqual(matrix, original)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Matrix, Simulation
