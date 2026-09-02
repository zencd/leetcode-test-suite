# 498. Diagonal Traverse
# https://leetcode.com/problems/diagonal-traverse/
# Medium

from typing import List
import unittest


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1_3x3(self):
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.sol.findDiagonalOrder(mat), [1, 2, 4, 7, 5, 3, 6, 8, 9])

    def test_example_2_2x2(self):
        mat = [[1, 2], [3, 4]]
        self.assertEqual(self.sol.findDiagonalOrder(mat), [1, 2, 3, 4])

    def test_single_element(self):
        self.assertEqual(self.sol.findDiagonalOrder([[42]]), [42])

    def test_single_row(self):
        mat = [[1, 2, 3, 4]]
        self.assertEqual(self.sol.findDiagonalOrder(mat), [1, 2, 3, 4])

    def test_single_column(self):
        mat = [[1], [2], [3], [4]]
        self.assertEqual(self.sol.findDiagonalOrder(mat), [1, 2, 3, 4])

    def test_2x3(self):
        mat = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(self.sol.findDiagonalOrder(mat), [1, 2, 4, 5, 3, 6])

    def test_3x2(self):
        mat = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(self.sol.findDiagonalOrder(mat), [1, 2, 3, 5, 4, 6])

    def test_negative_values(self):
        mat = [[-1, -2], [-3, -4]]
        self.assertEqual(self.sol.findDiagonalOrder(mat), [-1, -2, -3, -4])

    def test_4x4(self):
        mat = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
        expected = [
            1,
            2,
            5,
            9,
            6,
            3,
            4,
            7,
            10,
            13,
            14,
            11,
            8,
            12,
            15,
            16,
        ]
        self.assertEqual(self.sol.findDiagonalOrder(mat), expected)

    def test_2x4(self):
        mat = [[1, 2, 3, 4], [5, 6, 7, 8]]
        self.assertEqual(self.sol.findDiagonalOrder(mat), [1, 2, 5, 6, 3, 4, 7, 8])

    def test_preserves_all_elements(self):
        mat = [
            [100000, -100000, 0],
            [7, 8, 9],
        ]
        res = self.sol.findDiagonalOrder(mat)
        self.assertEqual(len(res), len(mat) * len(mat[0]))
        self.assertEqual(sorted(res), sorted([v for row in mat for v in row]))

    def test_larger_matrix_shape(self):
        mat = [[i * 1000 + j for j in range(7)] for i in range(5)]
        res = self.sol.findDiagonalOrder(mat)
        self.assertEqual(len(res), 35)
        self.assertEqual(sorted(res), sorted([v for row in mat for v in row]))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Matrix, Simulation
