# 59. Spiral Matrix II
# https://leetcode.com/problems/spiral-matrix-ii/
# Medium

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n1(self):
        self.assertEqual(self.solution.generateMatrix(1), [[1]])

    def test_n2(self):
        self.assertEqual(self.solution.generateMatrix(2), [[1, 2], [4, 3]])

    def test_n3(self):
        self.assertEqual(
            self.solution.generateMatrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        )

    def test_n4(self):
        self.assertEqual(
            self.solution.generateMatrix(4),
            [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]],
        )

    def test_n5(self):
        expected = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9],
        ]
        self.assertEqual(self.solution.generateMatrix(5), expected)

    def test_n20_max_constraint(self):
        result = self.solution.generateMatrix(20)
        self.assertEqual(len(result), 20)
        for row in result:
            self.assertEqual(len(row), 20)
        self.assertEqual(sorted(v for row in result for v in row), list(range(1, 401)))
        self.assertEqual(result[0], list(range(1, 21)))
        self.assertEqual(result[19][19], 39)
        self.assertEqual(result[10][9], 400)

    def test_values_cover_range(self):
        for n in (6, 7, 10):
            result = self.solution.generateMatrix(n)
            self.assertEqual(
                sorted(v for row in result for v in row), list(range(1, n * n + 1))
            )

    def test_corners_n6(self):
        result = self.solution.generateMatrix(6)
        self.assertEqual(result[0][0], 1)
        self.assertEqual(result[0][5], 6)
        self.assertEqual(result[5][5], 11)
        self.assertEqual(result[5][0], 16)
        self.assertEqual(result[2][2], 33)

    def test_center_n3(self):
        self.assertEqual(self.solution.generateMatrix(3)[1][1], 9)

    def test_center_n5(self):
        self.assertEqual(self.solution.generateMatrix(5)[2][2], 25)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Matrix, Simulation
