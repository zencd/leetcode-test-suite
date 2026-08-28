# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/
# Medium

from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        expected = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ]
        self.sol.solve(board)
        self.assertEqual(board, expected)

    def test_example_single_x(self):
        board = [["X"]]
        self.sol.solve(board)
        self.assertEqual(board, [["X"]])

    def test_single_o_on_edge(self):
        board = [["O"]]
        self.sol.solve(board)
        self.assertEqual(board, [["O"]])

    def test_all_o(self):
        board = [["O", "O"], ["O", "O"]]
        self.sol.solve(board)
        self.assertEqual(board, [["O", "O"], ["O", "O"]])

    def test_all_x(self):
        board = [["X", "X"], ["X", "X"]]
        self.sol.solve(board)
        self.assertEqual(board, [["X", "X"], ["X", "X"]])

    def test_1x_row(self):
        board = [["O", "X", "O"]]
        self.sol.solve(board)
        self.assertEqual(board, [["O", "X", "O"]])

    def test_1x_col(self):
        board = [["O"], ["X"], ["O"]]
        self.sol.solve(board)
        self.assertEqual(board, [["O"], ["X"], ["O"]])

    def test_inner_o_single_cell(self):
        board = [
            ["X", "X", "X"],
            ["X", "O", "X"],
            ["X", "X", "X"],
        ]
        expected = [
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"],
        ]
        self.sol.solve(board)
        self.assertEqual(board, expected)

    def test_inner_2x2_region(self):
        board = [
            ["X", "X", "X", "X", "X"],
            ["X", "O", "O", "X", "X"],
            ["X", "O", "O", "X", "X"],
            ["X", "X", "X", "X", "X"],
        ]
        expected = [["X", "X", "X", "X", "X"] for _ in range(4)]
        self.sol.solve(board)
        self.assertEqual(board, expected)

    def test_inner_l_shape_region(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "O", "X", "X"],
            ["X", "X", "X", "X"],
        ]
        expected = [["X", "X", "X", "X"] for _ in range(4)]
        self.sol.solve(board)
        self.assertEqual(board, expected)

    def test_multiple_regions_mixed(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["O", "X", "X", "O"],
            ["X", "O", "O", "X"],
            ["X", "X", "X", "X"],
        ]
        expected = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["O", "X", "X", "O"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
        ]
        self.sol.solve(board)
        self.assertEqual(board, expected)

    def test_o_ring(self):
        board = [
            ["X", "O", "X"],
            ["O", "O", "O"],
            ["X", "O", "X"],
        ]
        self.sol.solve(board)
        self.assertEqual(
            board,
            [
                ["X", "O", "X"],
                ["O", "O", "O"],
                ["X", "O", "X"],
            ],
        )

    def test_o_islands_only_on_edges(self):
        board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["X", "O", "X"],
        ]
        self.sol.solve(board)
        self.assertEqual(
            board,
            [
                ["X", "O", "X"],
                ["O", "X", "O"],
                ["X", "O", "X"],
            ],
        )

    @staticmethod
    def _expected_diagonal(n=50):
        return [["X"] * n for _ in range(n)]

    def test_diagonal_chain_not_captured(self):
        n = 50
        board = [["X"] * n for _ in range(n)]
        for i in range(1, n - 1):
            board[i][i] = "O"
        self.sol.solve(board)
        self.assertEqual(board, self._expected_diagonal(n))

    def test_h_line_reaching_edge(self):
        board = [
            ["X", "X", "X", "X"],
            ["O", "O", "O", "X"],
            ["X", "X", "X", "X"],
        ]
        self.sol.solve(board)
        self.assertEqual(
            board,
            [
                ["X", "X", "X", "X"],
                ["O", "O", "O", "X"],
                ["X", "X", "X", "X"],
            ],
        )

    def test_v_line_reaching_edge(self):
        board = [
            ["X", "O", "X"],
            ["X", "O", "X"],
            ["X", "O", "X"],
        ]
        self.sol.solve(board)
        self.assertEqual(
            board,
            [
                ["X", "O", "X"],
                ["X", "O", "X"],
                ["X", "O", "X"],
            ],
        )

    def test_surrounded_region_with_branches(self):
        board = [
            ["X", "X", "X", "X", "X", "X"],
            ["X", "O", "O", "O", "X", "X"],
            ["X", "O", "X", "O", "X", "X"],
            ["X", "O", "O", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X"],
        ]
        expected = [["X", "X", "X", "X", "X", "X"] for _ in range(5)]
        self.sol.solve(board)
        self.assertEqual(board, expected)

    def test_o_near_edge_but_surrounded(self):
        board = [
            ["X", "X", "X"],
            ["X", "O", "X"],
            ["X", "X", "X"],
        ]
        board[1][1] = "O"
        expected = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]
        self.sol.solve(board)
        self.assertEqual(board, expected)

    def test_board_with_only_non_surrounded_o(self):
        board = [["X", "O", "X"], ["X", "X", "O"]]
        self.sol.solve(board)
        self.assertEqual(board, [["X", "O", "X"], ["X", "X", "O"]])

    def test_in_place_modification_no_return(self):
        board = [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]]
        result = self.sol.solve(board)
        self.assertIsNone(result)

    def test_large_board(self):
        n = 200
        board = [["X"] * n for _ in range(n)]
        for i in range(50, 150):
            for j in range(50, 150):
                board[i][j] = "O"
        self.sol.solve(board)
        for i in range(50, 150):
            for j in range(50, 150):
                self.assertEqual(board[i][j], "X", f"cell ({i},{j})")

    def test_large_board_edge_region_survives(self):
        n = 200
        board = [["X"] * n for _ in range(n)]
        for i in range(1, n - 1):
            board[i][i] = "O"
            board[i][i + 1] = "O"
        self.sol.solve(board)
        for i in range(1, n - 1):
            self.assertEqual(board[i][i], "O")
            self.assertEqual(board[i][i + 1], "O")


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
