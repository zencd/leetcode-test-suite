# 289. Game of Life
# https://leetcode.com/problems/game-of-life/
# Medium

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        raise Exception("Not solved yet")


def reference_step(state: List[List[int]]) -> List[List[int]]:
    rows, cols = len(state), len(state[0])
    out = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            neighbors = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and state[ni][nj] == 1:
                        neighbors += 1
            if state[i][j] == 1:
                out[i][j] = 1 if neighbors in (2, 3) else 0
            else:
                out[i][j] = 1 if neighbors == 3 else 0
    return out


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def _step(self, board: List[List[int]]) -> List[List[int]]:
        result = [row[:] for row in board]
        self.solution.gameOfLife(result)
        return result

    def test_example1(self) -> None:
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        self.assertEqual(self._step(board), expected)

    def test_example2(self) -> None:
        board = [[1, 1], [1, 0]]
        expected = [[1, 1], [1, 1]]
        self.assertEqual(self._step(board), expected)

    def test_1x1_dead_stays_dead(self) -> None:
        self.assertEqual(self._step([[0]]), [[0]])

    def test_1x1_live_dies(self) -> None:
        self.assertEqual(self._step([[1]]), [[0]])

    def test_all_dead_board(self) -> None:
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(self._step(board), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_single_live_cell_dies(self) -> None:
        board = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(self._step(board), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_isolated_adjacent_pair_dies(self) -> None:
        board = [[1, 1], [0, 0], [0, 0]]
        self.assertEqual(self._step(board), [[0, 0], [0, 0], [0, 0]])

    def test_line_of_three(self) -> None:
        self.assertEqual(self._step([[1, 1, 1]]), [[0, 1, 0]])
        self.assertEqual(self._step([[0, 1, 0]]), [[0, 0, 0]])

    def test_block_is_still_life(self) -> None:
        self.assertEqual(self._step([[1, 1], [1, 1]]), [[1, 1], [1, 1]])

    def test_beehive_is_still_life(self) -> None:
        board = [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(self._step(board), board)

    def test_blinker_oscillator(self) -> None:
        horizontal = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        vertical = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        self.assertEqual(self._step(horizontal), vertical)
        self.assertEqual(self._step(vertical), horizontal)

    def test_toad_oscillator(self) -> None:
        phase_a = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
        phase_b = [[1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1]]
        self.assertEqual(self._step(phase_a), phase_b)
        self.assertEqual(self._step(phase_b), phase_a)

    def test_glider_first_step(self) -> None:
        glider = [
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        expected = [
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(self._step(glider), expected)

    def test_two_and_three_neighbor_cells_survive(self) -> None:
        board = [
            [1, 1, 1],
            [0, 1, 0],
            [0, 0, 0],
        ]
        expected = [
            [1, 1, 1],
            [1, 1, 1],
            [0, 0, 0],
        ]
        self.assertEqual(self._step(board), expected)

    def test_overpopulation_3x3(self) -> None:
        board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        self.assertEqual(self._step(board), expected)

    def test_replication_requires_exactly_three(self) -> None:
        born = [[1, 0, 1], [0, 0, 0], [1, 0, 0], [0, 0, 0]]
        self.assertEqual(self._step(born), [[0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 0]])
        not_born = [[1, 0, 1], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(self._step(not_born), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        four = [[1, 1], [1, 1]]
        self.assertEqual(self._step(four), [[1, 1], [1, 1]])
        dead_with_four = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        self.assertEqual(self._step(dead_with_four), [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    def test_inplace_without_clobbering(self) -> None:
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        self.solution.gameOfLife(board)
        self.assertEqual(board, [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])

    def test_random_board_against_reference(self) -> None:
        import random

        random.seed(42)
        for _ in range(20):
            rows = random.randint(1, 7)
            cols = random.randint(1, 7)
            board = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
            expected = reference_step(board)
            applied = [row[:] for row in board]
            self.solution.gameOfLife(applied)
            self.assertEqual(applied, expected, f"mismatch on board {board}")

    def test_max_size_board_against_reference(self) -> None:
        board = [
            [1 if (i * 31 + j * 17) % 5 == 0 else 0 for j in range(25)]
            for i in range(25)
        ]
        expected = reference_step(board)
        self.solution.gameOfLife(board)
        self.assertEqual(board, expected)

    def test_multiple_successive_steps_against_reference(self) -> None:
        board = [
            [0, 0, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
        ]
        current = [row[:] for row in board]
        for _ in range(3):
            expected = reference_step(current)
            applied = [row[:] for row in current]
            self.solution.gameOfLife(applied)
            self.assertEqual(applied, expected)
            current = expected


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Matrix, Simulation
