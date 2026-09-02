# 419. Battleships in a Board
# https://leetcode.com/problems/battleships-in-a-board/
# Medium

from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        board = [
            ["X", ".", ".", "X"],
            [".", ".", ".", "X"],
            [".", ".", ".", "X"],
        ]
        self.assertEqual(self.sol.countBattleships(board), 2)

    def test_example2_empty_board(self):
        board = [["."]]
        self.assertEqual(self.sol.countBattleships(board), 0)

    def test_single_ship(self):
        board = [["X"]]
        self.assertEqual(self.sol.countBattleships(board), 1)

    def test_horizontal_ship(self):
        board = [["X", "X", "X"]]
        self.assertEqual(self.sol.countBattleships(board), 1)

    def test_vertical_ship(self):
        board = [["X"], ["X"], ["X"]]
        self.assertEqual(self.sol.countBattleships(board), 1)

    def test_multiple_horizontal_ships(self):
        board = [
            ["X", "X", ".", "X", "X"],
            [".", ".", ".", ".", "."],
        ]
        self.assertEqual(self.sol.countBattleships(board), 2)

    def test_multiple_vertical_ships(self):
        board = [
            ["X", ".", "X"],
            ["X", ".", "X"],
            [".", ".", "."],
        ]
        self.assertEqual(self.sol.countBattleships(board), 2)

    def test_mixed_ships(self):
        board = [
            ["X", ".", "X"],
            ["X", ".", "X"],
            [".", ".", "."],
            ["X", "X", "X"],
        ]
        self.assertEqual(self.sol.countBattleships(board), 3)

    def test_adjacent_rows_no_adjacency_within_ships(self):
        board = [
            ["X", ".", "X"],
            [".", "X", "."],
            ["X", ".", "X"],
        ]
        self.assertEqual(self.sol.countBattleships(board), 5)

    def test_full_board_single_ship_rows(self):
        board = [["X", "X", "X", "X"]]
        self.assertEqual(self.sol.countBattleships(board), 1)

    def test_all_empty(self):
        board = [
            [".", ".", "."],
            [".", ".", "."],
        ]
        self.assertEqual(self.sol.countBattleships(board), 0)

    def test_ships_separated_by_one_cell(self):
        board = [
            ["X", ".", "X"],
            ["X", ".", "X"],
        ]
        self.assertEqual(self.sol.countBattleships(board), 2)

    def test_mixed_lengths(self):
        board = [
            ["X", ".", ".", "X"],
            [".", "X", "X", "."],
            [".", "X", ".", "."],
        ]
        self.assertEqual(self.sol.countBattleships(board), 3)

    def test_wide_board(self):
        row = ["X", "."] * 5
        board = [[row[j] for j in range(len(row))] for _ in range(3)]
        self.assertEqual(self.sol.countBattleships(board), 5)

    def test_board_not_modified(self):
        board = [
            ["X", ".", "X"],
            [".", "X", "."],
        ]
        original = [row[:] for row in board]
        self.sol.countBattleships(board)
        self.assertEqual(board, original)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Depth-First Search, Matrix
