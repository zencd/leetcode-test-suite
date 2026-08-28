# 79. Word Search
# https://leetcode.com/problems/word-search/
# Medium

from typing import List
from collections import Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]

    def test_example1(self):
        self.assertTrue(Solution().exist(self.board, "ABCCED"))

    def test_example2(self):
        self.assertTrue(Solution().exist(self.board, "SEE"))

    def test_example3(self):
        self.assertFalse(Solution().exist(self.board, "ABCB"))

    def test_single_cell_match(self):
        self.assertTrue(Solution().exist([["A"]], "A"))

    def test_single_cell_mismatch(self):
        self.assertFalse(Solution().exist([["A"]], "B"))

    def test_single_cell_word_too_long(self):
        self.assertFalse(Solution().exist([["A"]], "AA"))

    def test_2x2_all_same_found(self):
        self.assertTrue(Solution().exist([["A", "A"], ["A", "A"]], "AAAA"))

    def test_2x2_all_same_too_long(self):
        self.assertFalse(Solution().exist([["A", "A"], ["A", "A"]], "AAAAA"))

    def test_vertical_2x1(self):
        self.assertTrue(Solution().exist([["A"], ["B"]], "AB"))

    def test_vertical_2x1_reverse(self):
        self.assertTrue(Solution().exist([["A"], ["B"]], "BA"))

    def test_char_absent(self):
        self.assertFalse(Solution().exist(self.board, "XYZ"))

    def test_uses_all_cells(self):
        self.assertTrue(Solution().exist([["A", "B"], ["C", "D"]], "ABDC"))
        self.assertFalse(Solution().exist([["A", "B"], ["C", "D"]], "ABCD"))

    def test_backtracking_needed(self):
        self.assertTrue(Solution().exist([["A", "A"], ["A", "B"]], "AAB"))

    def test_diagonal_not_allowed(self):
        self.assertFalse(Solution().exist([["A", "B"], ["C", "D"]], "AD"))

    def test_reuse_forbidden(self):
        self.assertFalse(Solution().exist([["A", "B"], ["C", "A"]], "AAA"))

    def test_snake_path_3x3(self):
        board = [
            ["a", "b", "c"],
            ["f", "e", "d"],
            ["g", "h", "i"],
        ]
        self.assertTrue(Solution().exist(board, "abcdefghi"))
        self.assertTrue(Solution().exist(board, "abcde"))
        self.assertFalse(Solution().exist(board, "abcz"))

    def test_case_sensitive(self):
        self.assertFalse(Solution().exist([["a", "b"], ["c", "d"]], "ABCD"))

    def test_max_word_length_found(self):
        self.assertTrue(Solution().exist([["a"] * 4 for _ in range(4)], "a" * 15))

    def test_board_not_mutated_on_true(self):
        board = [["A", "B"], ["C", "D"]]
        expected = [row[:] for row in board]
        Solution().exist(board, "ABCD")
        self.assertEqual(board, expected)

    def test_board_not_mutated_on_false(self):
        board = [["A", "B"], ["C", "D"]]
        expected = [row[:] for row in board]
        Solution().exist(board, "ABAC")
        self.assertEqual(board, expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, String, Backtracking, Depth-First Search, Matrix
