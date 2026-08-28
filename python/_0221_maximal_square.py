# 221. Maximal Square
# https://leetcode.com/problems/maximal-square/
# Medium

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
        self.assertEqual(self.sol.maximalSquare(matrix), 4)

    def test_example2(self):
        matrix = [["0", "1"], ["1", "0"]]
        self.assertEqual(self.sol.maximalSquare(matrix), 1)

    def test_example3(self):
        matrix = [["0"]]
        self.assertEqual(self.sol.maximalSquare(matrix), 0)

    def test_single_one(self):
        matrix = [["1"]]
        self.assertEqual(self.sol.maximalSquare(matrix), 1)

    def test_all_zeros(self):
        matrix = [["0", "0", "0"], ["0", "0", "0"]]
        self.assertEqual(self.sol.maximalSquare(matrix), 0)

    def test_all_ones_square(self):
        matrix = [["1"] * 3 for _ in range(3)]
        self.assertEqual(self.sol.maximalSquare(matrix), 9)

    def test_all_ones_rect(self):
        matrix = [["1"] * 5 for _ in range(2)]
        self.assertEqual(self.sol.maximalSquare(matrix), 4)

    def test_reversed_rect(self):
        matrix = [["1"] * 2 for _ in range(5)]
        self.assertEqual(self.sol.maximalSquare(matrix), 4)

    def test_single_row(self):
        matrix = [["1", "0", "1", "1", "0", "1"]]
        self.assertEqual(self.sol.maximalSquare(matrix), 1)

    def test_single_col(self):
        matrix = [["1"], ["0"], ["1"], ["1"]]
        self.assertEqual(self.sol.maximalSquare(matrix), 1)

    def test_staircase_ones(self):
        matrix = [
            ["0", "0", "1", "1", "1"],
            ["0", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
        ]
        self.assertEqual(self.sol.maximalSquare(matrix), 16)

    def test_square_in_middle(self):
        matrix = [
            ["0", "0", "0", "0"],
            ["0", "1", "1", "0"],
            ["0", "1", "1", "0"],
            ["0", "0", "0", "0"],
        ]
        self.assertEqual(self.sol.maximalSquare(matrix), 4)

    def test_corner_square(self):
        matrix = [
            ["1", "1", "0"],
            ["1", "1", "0"],
            ["0", "0", "0"],
        ]
        self.assertEqual(self.sol.maximalSquare(matrix), 4)

    def test_broken_square(self):
        matrix = [
            ["1", "1", "1"],
            ["1", "0", "0"],
            ["1", "1", "1"],
        ]
        self.assertEqual(self.sol.maximalSquare(matrix), 1)

    def test_l_shape(self):
        matrix = [
            ["1", "1", "1"],
            ["0", "0", "1"],
            ["0", "0", "1"],
        ]
        self.assertEqual(self.sol.maximalSquare(matrix), 1)

    def test_noise(self):
        matrix = [
            ["1", "0", "1", "0", "1"],
            ["0", "1", "0", "1", "0"],
            ["1", "0", "1", "0", "1"],
        ]
        self.assertEqual(self.sol.maximalSquare(matrix), 1)

    def test_large_uniform(self):
        matrix = [["1"] * 300 for _ in range(300)]
        self.assertEqual(self.sol.maximalSquare(matrix), 90000)

    def test_large_stripe(self):
        matrix = [["1"] * 300 for _ in range(250)]
        self.assertEqual(self.sol.maximalSquare(matrix), 62500)

    def test_input_not_mutated(self):
        matrix = [
            ["1", "1"],
            ["1", "1"],
        ]
        original = [row[:] for row in matrix]
        self.assertEqual(self.sol.maximalSquare(matrix), 4)
        self.assertEqual(matrix, original)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Matrix
