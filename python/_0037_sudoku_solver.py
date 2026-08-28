# 37. Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/
# Hard

from typing import List
import unittest


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        raise Exception("Not solved yet")


def make_board(rows: List[str]) -> List[List[str]]:
    return [list(r) for r in rows]


SOLVED = [
    "123456789",
    "456789123",
    "789123456",
    "234567891",
    "567891234",
    "891234567",
    "345678912",
    "678912345",
    "912345678",
]


class TestSolveSudoku(unittest.TestCase):
    def solve_and_get(self, rows: List[str]) -> List[List[str]]:
        self.assertEqual(len(rows), 9)
        for r in rows:
            self.assertEqual(len(r), 9)
        board = make_board(rows)
        Solution().solveSudoku(board)
        return board

    def assert_valid_board(self, board: List[List[str]]) -> None:
        full = set("123456789")
        for i in range(9):
            self.assertEqual(len(board[i]), 9)
            self.assertNotIn(".", board[i], f"cell row {i} still empty")
            self.assertEqual(set(board[i]), full, f"row {i} invalid")
            self.assertEqual({board[r][i] for r in range(9)}, full, f"col {i} invalid")
        for br in range(3):
            for bc in range(3):
                vals = {
                    board[br * 3 + r][bc * 3 + c] for r in range(3) for c in range(3)
                }
                self.assertEqual(vals, full, f"box {br},{bc} invalid")

    def test_leetcode_example(self):
        board = self.solve_and_get(
            [
                "53..7....",
                "6..195...",
                ".98....6.",
                "8...6...3",
                "4..8.3..1",
                "7...2...6",
                ".6....28.",
                "...419..5",
                "....8..79",
            ]
        )
        self.assert_valid_board(board)
        self.assertEqual(
            board,
            make_board(
                [
                    "534678912",
                    "672195348",
                    "198342567",
                    "859761423",
                    "426853791",
                    "713924856",
                    "961537284",
                    "287419635",
                    "345286179",
                ]
            ),
        )

    def test_already_solved_board(self):
        board = self.solve_and_get(list(SOLVED))
        self.assert_valid_board(board)
        self.assertEqual(board, make_board(SOLVED))

    def test_all_empty_board(self):
        board = self.solve_and_get(["........."] * 9)
        self.assert_valid_board(board)
        counts = [sum(row.count(d) for row in board) for d in "123456789"]
        self.assertEqual(counts, [9] * 9)

    def test_single_empty_cell(self):
        rows = list(SOLVED)
        rows[4] = rows[4][:4] + "." + rows[4][5:]
        board = self.solve_and_get(rows)
        self.assert_valid_board(board)
        self.assertEqual(board, make_board(SOLVED))

    def test_missing_last_column(self):
        rows = [
            "12345678.",
            "45678912.",
            "78912345.",
            "234567891",
            "567891234",
            "891234567",
            "34567891.",
            "67891234.",
            "91234567.",
        ]
        board = self.solve_and_get(rows)
        self.assert_valid_board(board)
        self.assertEqual(board, make_board(SOLVED))

    def test_several_cells_removed(self):
        rows = [
            "....5....",
            "456789123",
            "789123456",
            "23456789.",
            "567891234",
            ".91234567",
            "345678912",
            "6789..345",
            "912345678",
        ]
        board = self.solve_and_get(rows)
        self.assert_valid_board(board)
        self.assertEqual(board, make_board(SOLVED))

    def test_heavily_removed_board(self):
        empties_per_row = {0: 6, 1: 7, 2: 7, 3: 6, 4: 7, 5: 7, 6: 6, 7: 7, 8: 6}
        rows = []
        for i, row in enumerate(SOLVED):
            n = empties_per_row[i]
            cols = sorted(range(9), key=lambda c: (i + c) % 9)
            drop = set(cols[:n])
            rows.append("".join(c if j not in drop else "." for j, c in enumerate(row)))
        board = self.solve_and_get(rows)
        self.assert_valid_board(board)

    def test_one_cell_per_row_and_column_removed(self):
        rows = [
            "".join("." if k == i else c for k, c in enumerate(row))
            for i, row in enumerate(SOLVED)
        ]
        board = self.solve_and_get(rows)
        self.assert_valid_board(board)
        self.assertEqual(board, make_board(SOLVED))

    def test_solution_modified_in_place(self):
        rows = [
            "53..7....",
            "6..195...",
            ".98....6.",
            "8...6...3",
            "4..8.3..1",
            "7...2...6",
            ".6....28.",
            "...419..5",
            "....8..79",
        ]
        board = make_board(rows)
        result = Solution().solveSudoku(board)
        self.assertIsNone(result)
        self.assert_valid_board(board)

    def test_givens_preserved(self):
        rows = [
            "53..7....",
            "6..195...",
            ".98..6...",
            "8...6...3",
            "4..8.3..1",
            "7...2...6",
            ".6....28.",
            "...419..5",
            "....8..79",
        ]
        board = make_board(rows)
        Solution().solveSudoku(board)
        for i in range(9):
            for j in range(9):
                if rows[i][j] != ".":
                    self.assertEqual(board[i][j], rows[i][j])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Backtracking, Matrix, Algorithm X, Dancing Links
