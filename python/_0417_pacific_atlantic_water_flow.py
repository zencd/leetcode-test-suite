# 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Medium

from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def example1(self, res):
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        self.assertEqual(sorted(res), sorted(expected))

    def test_example1(self):
        heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
        self.example1(self.sol.pacificAtlantic(heights))

    def test_example2_single_cell(self):
        self.assertEqual(self.sol.pacificAtlantic([[1]]), [[0, 0]])

    def test_single_cell_zero_height(self):
        self.assertEqual(self.sol.pacificAtlantic([[0]]), [[0, 0]])

    def test_single_row(self):
        heights = [[1, 2, 3, 4, 1]]
        expected = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
        self.assertEqual(sorted(self.sol.pacificAtlantic(heights)), expected)

    def test_single_column(self):
        heights = [[1], [2], [3], [4]]
        expected = [[0, 0], [1, 0], [2, 0], [3, 0]]
        self.assertEqual(sorted(self.sol.pacificAtlantic(heights)), expected)

    def test_all_equal_cells(self):
        heights = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        expected = [[r, c] for r in range(3) for c in range(3)]
        self.assertEqual(sorted(self.sol.pacificAtlantic(heights)), expected)

    def test_1x1_min_max_height(self):
        for h in (0, 100000):
            self.assertEqual(self.sol.pacificAtlantic([[h]]), [[0, 0]])

    def test_pacific_only_barrier(self):
        heights = [[1, 3, 2], [3, 1, 1], [1, 2, 3]]
        res = self.sol.pacificAtlantic(heights)
        brute = self.brute_force(heights)
        self.assertEqual(sorted(res), sorted(brute))

    def test_no_common_cells(self):
        heights = [[1, 2, 99], [1, 1, 98], [1, 1, 97]]
        res = self.sol.pacificAtlantic(heights)
        self.assertEqual(sorted(res), sorted(self.brute_force(heights)))

    def test_monotone_increasing_to_atlantic(self):
        heights = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        res = self.sol.pacificAtlantic(heights)
        self.assertEqual(sorted(res), sorted(self.brute_force(heights)))

    def test_wide_1x200_row(self):
        heights = [[i % 7 for i in range(200)]]
        res = self.sol.pacificAtlantic(heights)
        self.assertEqual(len(res), 200)
        self.assertTrue(all(r == 0 for r, c in res))

    def test_tall_200x1_column(self):
        heights = [[i % 5] for i in range(200)]
        res = self.sol.pacificAtlantic(heights)
        self.assertEqual(len(res), 200)
        self.assertTrue(all(c == 0 for r, c in res))

    def test_random_consistency_brute_force(self):
        import random

        random.seed(42)
        for _ in range(30):
            m = random.randint(1, 6)
            n = random.randint(1, 6)
            heights = [[random.randint(0, 10) for _ in range(n)] for _ in range(m)]
            got = sorted(self.sol.pacificAtlantic(heights))
            want = sorted(self.brute_force(heights))
            self.assertEqual(got, want, f"mismatch on {heights}")

    def brute_force(self, heights):
        m, n = len(heights), len(heights[0])
        result = []
        for sr in range(m):
            for sc in range(n):
                if self._can_reach(heights, sr, sc, "P") and self._can_reach(heights, sr, sc, "A"):
                    result.append([sr, sc])
        return result

    def _can_reach(self, heights, sr, sc, ocean):
        m, n = len(heights), len(heights[0])
        visited = set()
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if (ocean == "P" and (r == 0 or c == 0)) or (ocean == "A" and (r == m - 1 or c == n - 1)):
                return True
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] <= heights[r][c] and (nr, nc) not in visited:
                    stack.append((nr, nc))
        return False


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Depth-First Search, Breadth-First Search, Matrix
