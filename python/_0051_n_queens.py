# 51. N-Queens
# https://leetcode.com/problems/n-queens/
# Hard

import unittest
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        raise Exception("Not solved yet")


EXPECTED_COUNTS = {1: 1, 2: 0, 3: 0, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92, 9: 352}


class TestNQueens(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def sort_solutions(self, solutions):
        return sorted(solutions, key=lambda s: tuple(s))

    def validate_board(self, board):
        n = len(board)
        queens = []
        for r in range(n):
            row = board[r]
            self.assertEqual(len(row), n)
            self.assertIsInstance(row, str)
            self.assertTrue(set(row) <= {"Q", "."})
            queens += [(r, c) for c in range(n) if row[c] == "Q"]
        self.assertEqual(len(queens), n)
        for i in range(len(queens)):
            r1, c1 = queens[i]
            for j in range(i + 1, len(queens)):
                r2, c2 = queens[j]
                self.assertNotEqual(c1, c2)
                self.assertNotEqual(r1 - c1, r2 - c2)
                self.assertNotEqual(r1 + c1, r2 + c2)

    def test_n1(self):
        result = self.solution.solveNQueens(1)
        self.assertEqual(result, [["Q"]])

    def test_n2_no_solutions(self):
        self.assertEqual(self.solution.solveNQueens(2), [])

    def test_n3_no_solutions(self):
        self.assertEqual(self.solution.solveNQueens(3), [])

    def test_n4_count(self):
        result = self.solution.solveNQueens(4)
        self.assertEqual(len(result), 2)
        for board in result:
            self.validate_board(board)

    def test_n4_expected(self):
        expected = self.sort_solutions(
            [
                [".Q..", "...Q", "Q...", "..Q."],
                ["..Q.", "Q...", "...Q", ".Q.."],
            ]
        )
        self.assertEqual(self.sort_solutions(self.solution.solveNQueens(4)), expected)

    def test_expected_counts(self):
        for n, count in EXPECTED_COUNTS.items():
            with self.subTest(n=n):
                self.assertEqual(len(self.solution.solveNQueens(n)), count)

    def test_all_boards_valid(self):
        for n in range(1, 10):
            for board in self.solution.solveNQueens(n):
                with self.subTest(n=n, board=board):
                    self.validate_board(board)

    def test_result_types_and_shape(self):
        for n in (1, 4, 5, 8):
            result = self.solution.solveNQueens(n)
            self.assertIsInstance(result, list)
            for board in result:
                self.assertIsInstance(board, list)
                self.assertEqual(len(board), n)
                for row in board:
                    self.assertIsInstance(row, str)
                    self.assertEqual(len(row), n)

    def test_solutions_distinct(self):
        for n in (4, 5, 6):
            result = self.solution.solveNQueens(n)
            self.assertEqual(len(result), len({tuple(b) for b in result}))

    def test_each_row_has_one_queen(self):
        for n in (1, 4, 5, 7):
            for board in self.solution.solveNQueens(n):
                for row in board:
                    self.assertEqual(row.count("Q"), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Backtracking, Algorithm X
