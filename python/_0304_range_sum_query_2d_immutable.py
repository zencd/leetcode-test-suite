# 304. Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/
# Medium

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        raise Exception("Not solved yet")

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_example_from_problem_statement(self):
        matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
        obj = NumMatrix(matrix)
        self.assertEqual(obj.sumRegion(2, 1, 4, 3), 8)
        self.assertEqual(obj.sumRegion(1, 1, 2, 2), 11)
        self.assertEqual(obj.sumRegion(1, 2, 2, 4), 12)

    def test_single_cell(self):
        obj = NumMatrix([[42]])
        self.assertEqual(obj.sumRegion(0, 0, 0, 0), 42)

    def test_single_row(self):
        obj = NumMatrix([[1, 2, 3, 4, 5]])
        self.assertEqual(obj.sumRegion(0, 0, 0, 4), 15)
        self.assertEqual(obj.sumRegion(0, 1, 0, 3), 9)
        self.assertEqual(obj.sumRegion(0, 2, 0, 2), 3)
        self.assertEqual(obj.sumRegion(0, 0, 0, 0), 1)
        self.assertEqual(obj.sumRegion(0, 4, 0, 4), 5)

    def test_single_column(self):
        obj = NumMatrix([[1], [2], [3], [4]])
        self.assertEqual(obj.sumRegion(0, 0, 3, 0), 10)
        self.assertEqual(obj.sumRegion(1, 0, 2, 0), 5)
        self.assertEqual(obj.sumRegion(0, 0, 0, 0), 1)
        self.assertEqual(obj.sumRegion(3, 0, 3, 0), 4)

    def test_full_matrix(self):
        matrix = [
            [1, 2],
            [3, 4],
        ]
        obj = NumMatrix(matrix)
        self.assertEqual(obj.sumRegion(0, 0, 1, 1), 10)

    def test_negative_numbers(self):
        matrix = [
            [-1, -2],
            [-3, -4],
        ]
        obj = NumMatrix(matrix)
        self.assertEqual(obj.sumRegion(0, 0, 1, 1), -10)
        self.assertEqual(obj.sumRegion(1, 1, 1, 1), -4)
        self.assertEqual(obj.sumRegion(0, 1, 1, 1), -6)
        self.assertEqual(obj.sumRegion(0, 0, 1, 0), -4)

    def test_mixed_signs(self):
        matrix = [
            [-1, 100],
            [100, -1],
        ]
        obj = NumMatrix(matrix)
        self.assertEqual(obj.sumRegion(0, 0, 1, 1), 198)
        self.assertEqual(obj.sumRegion(0, 0, 0, 0), -1)
        self.assertEqual(obj.sumRegion(1, 1, 1, 1), -1)

    def test_zeros(self):
        obj = NumMatrix([[0, 0], [0, 0]])
        self.assertEqual(obj.sumRegion(0, 0, 1, 1), 0)
        self.assertEqual(obj.sumRegion(0, 1, 1, 1), 0)

    def test_submatrix_not_from_origin(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
        ]
        obj = NumMatrix(matrix)
        self.assertEqual(obj.sumRegion(1, 1, 2, 2), 6 + 7 + 10 + 11)
        self.assertEqual(obj.sumRegion(1, 2, 2, 3), 7 + 8 + 11 + 12)
        self.assertEqual(obj.sumRegion(0, 2, 1, 3), 3 + 4 + 7 + 8)

    def test_single_row_queries_at_edges(self):
        obj = NumMatrix([[7]])
        self.assertEqual(obj.sumRegion(0, 0, 0, 0), 7)

    def test_larger_matrix(self):
        import random

        random.seed(0)
        rows, cols = 10, 15
        matrix = [
            [random.randint(-1000, 1000) for _ in range(cols)] for _ in range(rows)
        ]
        obj = NumMatrix(matrix)
        for _ in range(200):
            r1 = random.randint(0, rows - 1)
            c1 = random.randint(0, cols - 1)
            r2 = random.randint(r1, rows - 1)
            c2 = random.randint(c1, cols - 1)
            expected = sum(
                matrix[r][c] for r in range(r1, r2 + 1) for c in range(c1, c2 + 1)
            )
            self.assertEqual(
                obj.sumRegion(r1, c1, r2, c2),
                expected,
                msg=f"failed at r1={r1}, c1={c1}, r2={r2}, c2={c2}",
            )

    def test_extreme_constraint_values(self):
        matrix = [
            [10000, -10000],
            [-10000, 10000],
        ]
        obj = NumMatrix(matrix)
        self.assertEqual(obj.sumRegion(0, 0, 1, 1), 0)
        self.assertEqual(obj.sumRegion(0, 0, 0, 0), 10000)
        self.assertEqual(obj.sumRegion(1, 0, 1, 0), -10000)

    def test_max_dimension_matrix_sum_consistency(self):
        rows = cols = 50
        matrix = [[i * cols + j for j in range(cols)] for i in range(rows)]
        obj = NumMatrix(matrix)
        total = sum(sum(row) for row in matrix)
        self.assertEqual(obj.sumRegion(0, 0, rows - 1, cols - 1), total)

    def test_repeated_queries_consistent(self):
        matrix = [[1, 2], [3, 4]]
        obj = NumMatrix(matrix)
        results = [obj.sumRegion(0, 0, 1, 1) for _ in range(5)]
        self.assertEqual(results, [10] * 5)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Design, Matrix, Prefix Sum
