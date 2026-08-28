# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
# Easy

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_num_rows_1(self):
        self.assertEqual(self.solution.generate(1), [[1]])

    def test_num_rows_2(self):
        self.assertEqual(self.solution.generate(2), [[1], [1, 1]])

    def test_num_rows_3(self):
        self.assertEqual(self.solution.generate(3), [[1], [1, 1], [1, 2, 1]])

    def test_num_rows_4(self):
        self.assertEqual(
            self.solution.generate(4),
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]],
        )

    def test_num_rows_5(self):
        self.assertEqual(
            self.solution.generate(5),
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
        )

    def test_num_rows_6(self):
        self.assertEqual(
            self.solution.generate(6),
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
                [1, 5, 10, 10, 5, 1],
            ],
        )

    def test_num_rows_7(self):
        self.assertEqual(
            self.solution.generate(7),
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
                [1, 5, 10, 10, 5, 1],
                [1, 6, 15, 20, 15, 6, 1],
            ],
        )

    def test_num_rows_10(self):
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
            [1, 7, 21, 35, 35, 21, 7, 1],
            [1, 8, 28, 56, 70, 56, 28, 8, 1],
            [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
        ]
        self.assertEqual(self.solution.generate(10), expected)

    def test_num_rows_30_length(self):
        result = self.solution.generate(30)
        self.assertEqual(len(result), 30)

    def test_num_rows_30_row_lengths(self):
        result = self.solution.generate(30)
        for i, row in enumerate(result):
            self.assertEqual(len(row), i + 1)

    def test_edges_are_one(self):
        result = self.solution.generate(30)
        for row in result:
            self.assertEqual(row[0], 1)
            self.assertEqual(row[-1], 1)

    def test_symmetry(self):
        result = self.solution.generate(30)
        for row in result:
            self.assertEqual(row, row[::-1])

    def test_pascal_property(self):
        result = self.solution.generate(30)
        for i in range(2, len(result)):
            for j in range(1, i):
                self.assertEqual(result[i][j], result[i - 1][j - 1] + result[i - 1][j])

    def test_row_sums_are_powers_of_two(self):
        result = self.solution.generate(20)
        for i, row in enumerate(result):
            self.assertEqual(sum(row), 2**i)

    def test_num_rows_1_returns_list_of_lists(self):
        result = self.solution.generate(1)
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], list)
        self.assertIsInstance(result[0][0], int)

    def test_last_row_values(self):
        result = self.solution.generate(30)
        last_row = result[29]
        self.assertEqual(last_row[0], 1)
        self.assertEqual(last_row[1], 29)
        self.assertEqual(last_row[2], 406)
        self.assertEqual(last_row[-2], 29)
        self.assertEqual(last_row[-1], 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming
