# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Medium

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        raise Exception("Not solved yet")


import unittest


def make_tree(values):
    if values is None or len(values) == 0:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        root = make_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(self.sol.zigzagLevelOrder(root), [[3], [20, 9], [15, 7]])

    def test_example2_single_node(self):
        root = make_tree([1])
        self.assertEqual(self.sol.zigzagLevelOrder(root), [[1]])

    def test_example3_empty_tree(self):
        self.assertEqual(self.sol.zigzagLevelOrder(None), [])

    def test_two_level_left_only(self):
        root = make_tree([1, 2])
        self.assertEqual(self.sol.zigzagLevelOrder(root), [[1], [2]])

    def test_two_level_right_only(self):
        root = make_tree([1, None, 2])
        self.assertEqual(self.sol.zigzagLevelOrder(root), [[1], [2]])

    def test_two_level_both(self):
        root = make_tree([1, 2, 3])
        self.assertEqual(self.sol.zigzagLevelOrder(root), [[1], [3, 2]])

    def test_three_levels_full(self):
        root = make_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.sol.zigzagLevelOrder(root), [[1], [3, 2], [4, 5, 6, 7]])

    def test_unbalanced_chain_left(self):
        root = make_tree([1, 2, None, 3, None, 4])
        self.assertEqual(self.sol.zigzagLevelOrder(root), [[1], [2], [3], [4]])

    def test_unbalanced_chain_right(self):
        root = make_tree([1, None, 2, None, 3, None, 4])
        self.assertEqual(self.sol.zigzagLevelOrder(root), [[1], [2], [3], [4]])

    def test_duplicate_values(self):
        root = make_tree([5, 5, 5, 5, 5, 5, 5])
        self.assertEqual(self.sol.zigzagLevelOrder(root), [[5], [5, 5], [5, 5, 5, 5]])

    def test_negative_values(self):
        root = make_tree([-1, -2, -3, -4, -5, -6, -7])
        self.assertEqual(
            self.sol.zigzagLevelOrder(root), [[-1], [-3, -2], [-4, -5, -6, -7]]
        )

    def test_zero_value(self):
        root = make_tree([0, 0, 0])
        self.assertEqual(self.sol.zigzagLevelOrder(root), [[0], [0, 0]])

    def test_mixed_values(self):
        root = make_tree([1, -50, 100, None, 7, -3, 42, 99])
        self.assertEqual(
            self.sol.zigzagLevelOrder(root), [[1], [100, -50], [7, -3, 42], [99]]
        )

    def test_deep_left_skewed(self):
        root = make_tree([1, 2, None, 3, None, 4, None, 5])
        self.assertEqual(self.sol.zigzagLevelOrder(root), [[1], [2], [3], [4], [5]])

    def test_wide_level(self):
        root = make_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        result = self.sol.zigzagLevelOrder(root)
        self.assertEqual(
            result, [[1], [3, 2], [4, 5, 6, 7], [15, 14, 13, 12, 11, 10, 9, 8]]
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Breadth-First Search, Binary Tree
