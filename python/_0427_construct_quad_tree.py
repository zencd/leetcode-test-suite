# 427. Construct Quad Tree
# https://leetcode.com/problems/construct-quad-tree/
# Medium

import unittest
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        raise Exception("Not solved yet")


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        raise Exception("Not solved yet")


def serialize(root):
    if root is None:
        return None
    out = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
        else:
            out.append([1 if node.isLeaf else 0, 1 if node.val else 0])
            queue.extend([node.topLeft, node.topRight, node.bottomLeft, node.bottomRight])
    while out and out[-1] is None:
        out.pop()
    return out


class TestSolution(unittest.TestCase):
    def assert_serialized(self, grid, expected):
        root = Solution().construct(grid)
        self.assertIsInstance(root, Node)
        self.assertEqual(serialize(root), expected)

    def _assert_valid(self, node, grid, r, c, side):
        uniform = all(grid[i][j] == grid[r][c] for i in range(r, r + side) for j in range(c, c + side))
        if uniform:
            self.assertTrue(node.isLeaf, "uniform region must be a leaf")
            self.assertEqual(node.val, grid[r][c] == 1)
            self.assertIsNone(node.topLeft)
            self.assertIsNone(node.topRight)
            self.assertIsNone(node.bottomLeft)
            self.assertIsNone(node.bottomRight)
            return
        self.assertFalse(node.isLeaf, "mixed region must not be a leaf")
        self.assertIsNotNone(node.topLeft)
        self.assertIsNotNone(node.topRight)
        self.assertIsNotNone(node.bottomLeft)
        self.assertIsNotNone(node.bottomRight)
        half = side // 2
        self._assert_valid(node.topLeft, grid, r, c, half)
        self._assert_valid(node.topRight, grid, r, c + half, half)
        self._assert_valid(node.bottomLeft, grid, r + half, c, half)
        self._assert_valid(node.bottomRight, grid, r + half, c + half, half)

    def assert_structure_valid(self, grid):
        root = Solution().construct(grid)
        self._assert_valid(root, grid, 0, 0, len(grid))

    def test_single_zero(self):
        self.assert_serialized([[0]], [[1, 0]])

    def test_single_one(self):
        self.assert_serialized([[1]], [[1, 1]])

    def test_uniform_2x2_zeros(self):
        self.assert_serialized([[0, 0], [0, 0]], [[1, 0]])

    def test_uniform_2x2_ones(self):
        self.assert_serialized([[1, 1], [1, 1]], [[1, 1]])

    def test_uniform_4x4_ones(self):
        self.assert_serialized([[1] * 4 for _ in range(4)], [[1, 1]])

    def test_uniform_8x8_zeros(self):
        self.assert_serialized([[0] * 8 for _ in range(8)], [[1, 0]])

    def test_example1_mixed_2x2(self):
        self.assert_serialized(
            [[0, 1], [1, 0]],
            [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]],
        )

    def test_example2_mixed_8x8(self):
        grid = [
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
        ]
        self.assert_serialized(
            grid,
            [[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]],
        )

    def test_checkerboard_4x4(self):
        grid = [
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
        ]
        self.assert_serialized(
            grid,
            [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [1, 1], [1, 0], [1, 0], [1, 1], [1, 1], [1, 0], [1, 0], [1, 1], [1, 1], [1, 0], [1, 0], [1, 1], [1, 1], [1, 0], [1, 0], [1, 1]],
        )

    def test_vertical_split_4x4(self):
        grid = [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
        ]
        self.assert_serialized(grid, [[0, 1], [1, 1], [1, 0], [1, 1], [1, 0]])

    def test_horizontal_split_4x4(self):
        grid = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assert_serialized(grid, [[0, 1], [1, 1], [1, 1], [1, 0], [1, 0]])

    def test_single_zero_cell_4x4(self):
        grid = [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assert_structure_valid(grid)
        root = Solution().construct(grid)
        self.assertFalse(root.isLeaf)

    def test_structure_valid_mixed_8x8(self):
        grid = [
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
        ]
        self.assert_structure_valid(grid)

    def test_structure_valid_checkerboard_4x4(self):
        grid = [
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
        ]
        self.assert_structure_valid(grid)

    def test_structure_valid_all_ones_2x2(self):
        self.assert_structure_valid([[1, 1], [1, 1]])

    def test_root_attributes_single_cell(self):
        root = Solution().construct([[1]])
        self.assertTrue(root.val)
        self.assertTrue(root.isLeaf)
        self.assertIsNone(root.topLeft)
        self.assertIsNone(root.topRight)
        self.assertIsNone(root.bottomLeft)
        self.assertIsNone(root.bottomRight)

    def test_leaf_count_checkerboard_4x4(self):
        def count_leaves(node):
            if node.isLeaf:
                return 1
            return count_leaves(node.topLeft) + count_leaves(node.topRight) + count_leaves(node.bottomLeft) + count_leaves(node.bottomRight)

        grid = [
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
        ]
        root = Solution().construct(grid)
        self.assertEqual(count_leaves(root), 16)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Divide and Conquer, Tree, Matrix
