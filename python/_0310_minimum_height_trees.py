# 310. Minimum Height Trees
# https://leetcode.com/problems/minimum-height-trees/
# Medium

from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_node(self):
        self.assertEqual(self.sol.findMinHeightTrees(1, []), [0])

    def test_two_nodes(self):
        self.assertEqual(sorted(self.sol.findMinHeightTrees(2, [[0, 1]])), [0, 1])

    def test_star_center(self):
        self.assertEqual(
            sorted(self.sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])), [1]
        )

    def test_two_centers(self):
        self.assertEqual(
            sorted(
                self.sol.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])
            ),
            [3, 4],
        )

    def test_path_five_nodes(self):
        self.assertEqual(
            self.sol.findMinHeightTrees(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), [2]
        )

    def test_path_six_nodes(self):
        self.assertEqual(
            sorted(
                self.sol.findMinHeightTrees(6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]])
            ),
            [2, 3],
        )

    def test_three_leaves_two_centers(self):
        self.assertEqual(
            sorted(self.sol.findMinHeightTrees(5, [[1, 0], [2, 1], [3, 2], [4, 3]])),
            [2],
        )

    def test_balanced_tree(self):
        self.assertEqual(
            sorted(
                self.sol.findMinHeightTrees(
                    7, [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [3, 6]]
                )
            ),
            [1, 3],
        )

    def test_lopsided_tree(self):
        self.assertEqual(
            sorted(self.sol.findMinHeightTrees(4, [[0, 1], [1, 2], [1, 3]])), [1]
        )

    def test_large_star(self):
        n = 1000
        edges = [[0, i] for i in range(1, n)]
        self.assertEqual(self.sol.findMinHeightTrees(n, edges), [0])

    def test_large_path(self):
        n = 10000
        edges = [[i, i + 1] for i in range(n - 1)]
        result = sorted(self.sol.findMinHeightTrees(n, edges))
        self.assertEqual(result, [4999, 5000])

    def test_edges_unordered(self):
        self.assertEqual(sorted(self.sol.findMinHeightTrees(3, [[2, 0], [2, 1]])), [2])

    def test_input_not_mutated(self):
        edges = [[1, 0], [1, 2], [1, 3]]
        snapshot = [list(e) for e in edges]
        self.sol.findMinHeightTrees(4, edges)
        self.assertEqual(edges, snapshot)


if __name__ == "__main__":
    unittest.main()

# Tags: Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort
