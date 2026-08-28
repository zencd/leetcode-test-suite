# 85. Maximal Rectangle
# https://leetcode.com/problems/maximal-rectangle/
# Hard

from typing import List
import unittest


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        raise Exception("Not solved yet")


class TestMaximalRectangle(unittest.TestCase):
    def test_all_zeros(self):
        matrix = [["0"]]
        self.assertEqual(Solution().maximalRectangle(matrix), 0)

    def test_all_ones(self):
        matrix = [["1"]]
        self.assertEqual(Solution().maximalRectangle(matrix), 1)

    def test_example_1(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
        self.assertEqual(Solution().maximalRectangle(matrix), 6)

    def test_single_row(self):
        matrix = [["1", "1", "1", "1"]]
        self.assertEqual(Solution().maximalRectangle(matrix), 4)

    def test_single_row_with_zero(self):
        matrix = [["1", "0", "1", "1"]]
        self.assertEqual(Solution().maximalRectangle(matrix), 2)

    def test_single_row_all_zeros(self):
        matrix = [["0", "0", "0"]]
        self.assertEqual(Solution().maximalRectangle(matrix), 0)

    def test_single_column(self):
        matrix = [["1"], ["1"], ["1"]]
        self.assertEqual(Solution().maximalRectangle(matrix), 3)

    def test_single_column_with_zero(self):
        matrix = [["1"], ["0"], ["1"]]
        self.assertEqual(Solution().maximalRectangle(matrix), 1)

    def test_single_column_all_zeros(self):
        matrix = [["0"], ["0"]]
        self.assertEqual(Solution().maximalRectangle(matrix), 0)

    def test_full_square(self):
        matrix = [["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]]
        self.assertEqual(Solution().maximalRectangle(matrix), 9)

    def test_cross_pattern(self):
        matrix = [
            ["0", "1", "0"],
            ["1", "1", "1"],
            ["0", "1", "0"],
        ]
        self.assertEqual(Solution().maximalRectangle(matrix), 3)

    def test_diagonal(self):
        matrix = [
            ["1", "0", "0"],
            ["0", "1", "0"],
            ["0", "0", "1"],
        ]
        self.assertEqual(Solution().maximalRectangle(matrix), 1)

    def test_borders_of_ones(self):
        matrix = [
            ["1", "1", "1"],
            ["1", "0", "1"],
            ["1", "1", "1"],
        ]
        self.assertEqual(Solution().maximalRectangle(matrix), 3)

    def test_t_shape(self):
        matrix = [
            ["1", "1", "1"],
            ["0", "1", "0"],
            ["0", "1", "0"],
        ]
        self.assertEqual(Solution().maximalRectangle(matrix), 3)

    def test_ones_in_bottom(self):
        matrix = [
            ["0", "0", "0"],
            ["1", "1", "1"],
            ["1", "1", "1"],
        ]
        self.assertEqual(Solution().maximalRectangle(matrix), 6)

    def test_checkerboard(self):
        matrix = [
            ["1", "0", "1"],
            ["0", "1", "0"],
            ["1", "0", "1"],
        ]
        self.assertEqual(Solution().maximalRectangle(matrix), 1)

    def test_wide_rectangle_dominates(self):
        matrix = [
            ["0", "0", "1", "1", "1", "1", "1", "0"],
            ["0", "0", "1", "1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
        ]
        self.assertEqual(Solution().maximalRectangle(matrix), 15)

    def test_tall_rectangle_dominates(self):
        matrix = [
            ["0", "1", "0"],
            ["0", "1", "0"],
            ["0", "1", "0"],
            ["0", "1", "0"],
            ["0", "1", "0"],
        ]
        self.assertEqual(Solution().maximalRectangle(matrix), 5)

    def test_two_disjoint_blocks(self):
        matrix = [
            ["1", "1", "0", "1", "1"],
            ["1", "1", "0", "1", "1"],
            ["1", "1", "0", "1", "1"],
        ]
        self.assertEqual(Solution().maximalRectangle(matrix), 6)

    def test_mixed_with_zero_rows(self):
        matrix = [
            ["1", "1", "1"],
            ["0", "0", "0"],
            ["1", "1", "1"],
        ]
        self.assertEqual(Solution().maximalRectangle(matrix), 3)

    def test_asymmetric(self):
        matrix = [
            ["1", "0", "0", "1", "1"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "0"],
        ]
        self.assertEqual(Solution().maximalRectangle(matrix), 4)

    def test_numeric_values(self):
        matrix = [[0], [1], [1]]
        self.assertEqual(Solution().maximalRectangle(matrix), 2)

    def test_numeric_values_all_zero(self):
        matrix = [[0, 0], [0, 0]]
        self.assertEqual(Solution().maximalRectangle(matrix), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

# Tags: Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
