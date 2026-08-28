# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
# Medium

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        raise Exception("Not solved yet")


import unittest


def make_board(row_strings: List[str]) -> List[List[str]]:
    return [list(r) for r in row_strings]


def blank_board() -> List[List[str]]:
    return [["."] * 9 for _ in range(9)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1_valid(self):
        board = make_board(
            [
                "53..7....",
                "6..195...",
                ".98....6.",
                "8...6...3",
                "4..8.3..1",
                "7...2...6",
                ".6....28.",
                "...419..5",
                "....8...79",
            ]
        )
        self.assertTrue(self.solution.isValidSudoku(board))

    def test_example_2_invalid_duplicate_in_box(self):
        board = make_board(
            [
                "83..7....",
                "6..195...",
                ".98....6.",
                "8...6...3",
                "4..8.3..1",
                "7...2...6",
                ".6....28.",
                "...419..5",
                "....8...79",
            ]
        )
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_empty_board_is_valid(self):
        self.assertTrue(self.solution.isValidSudoku(blank_board()))

    def test_filled_valid_board(self):
        board = make_board(
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
        )
        self.assertTrue(self.solution.isValidSudoku(board))

    def test_duplicate_in_row(self):
        board = blank_board()
        board[0][0] = "5"
        board[0][8] = "5"
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_duplicate_in_col(self):
        board = blank_board()
        board[0][0] = "5"
        board[8][0] = "5"
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_same_digit_different_boxes_rows_cols_ok(self):
        board = blank_board()
        board[1][1] = "5"
        board[4][4] = "5"
        self.assertTrue(self.solution.isValidSudoku(board))

    def test_same_digit_different_boxes_same_row_invalid(self):
        board = blank_board()
        board[0][0] = "5"
        board[0][3] = "5"
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_same_digit_different_boxes_same_col_invalid(self):
        board = blank_board()
        board[0][0] = "5"
        board[3][0] = "5"
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_16_same_digits_invalid(self):
        board = blank_board()
        board[0][0] = "5"
        board[3][3] = "5"
        board[6][6] = "5"
        self.assertTrue(self.solution.isValidSudoku(board))
        board[4][4] = "5"
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_all_nines_invalid(self):
        board = [["9"] * 9 for _ in range(9)]
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_full_1_to_9_twice_invalid(self):
        rows = ["123456789", "123456789"]
        board = make_board(rows + ["." * 9] * 7)
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_two_identical_rows_invalid(self):
        board = [list("123456789"), list("123456789")] + [["."] * 9] * 7
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_corner_boxes_boundaries(self):
        board = blank_board()
        board[2][2] = "1"
        board[3][3] = "1"
        self.assertTrue(self.solution.isValidSudoku(board))
        board = blank_board()
        board[6][8] = "2"
        board[8][6] = "2"
        self.assertFalse(self.solution.isValidSudoku(board))

    def test_invalid_in_each_of_nine_boxes(self):
        for box_row in range(3):
            for box_col in range(3):
                board = blank_board()
                r = box_row * 3 + 1
                c = box_col * 3 + 1
                board[r][c] = "3"
                board[r][c + 1] = "3"
                self.assertFalse(
                    self.solution.isValidSudoku(board),
                    f"box ({box_row}, {box_col}) should be invalid",
                )

    def test_duplicate_in_every_column(self):
        for j in range(9):
            board = blank_board()
            board[1][j] = "4"
            board[2][j] = "4"
            self.assertFalse(self.solution.isValidSudoku(board))

    def test_row_of_1_to_9_is_valid(self):
        board = blank_board()
        board[0] = list("123456789")
        self.assertTrue(self.solution.isValidSudoku(board))
        board[0][4] = "1"
        self.assertFalse(self.solution.isValidSudoku(board))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Matrix
