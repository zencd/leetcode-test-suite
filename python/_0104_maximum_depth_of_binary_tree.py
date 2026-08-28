# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Easy

import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        raise Exception("Not solved yet")


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.maxDepth(None), 0)

    def test_single_node(self):
        self.assertEqual(self.solution.maxDepth(TreeNode(1)), 1)

    def test_root_with_left_only(self):
        root = build_tree([1, 2])
        self.assertEqual(self.solution.maxDepth(root), 2)

    def test_root_with_right_only(self):
        root = build_tree([1, None, 2])
        self.assertEqual(self.solution.maxDepth(root), 2)

    def test_root_with_both_children(self):
        root = build_tree([1, 2, 3])
        self.assertEqual(self.solution.maxDepth(root), 2)

    def test_example_1(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(self.solution.maxDepth(root), 3)

    def test_example_2(self):
        root = build_tree([1, None, 2])
        self.assertEqual(self.solution.maxDepth(root), 2)

    def test_left_skewed(self):
        root = build_tree([1, 2, None, 3, None, 4])
        self.assertEqual(self.solution.maxDepth(root), 4)

    def test_right_skewed(self):
        root = build_tree([1, None, 2, None, 3, None, 4])
        self.assertEqual(self.solution.maxDepth(root), 4)

    def test_perfect_tree_depth_3(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.solution.maxDepth(root), 3)

    def test_perfect_tree_depth_4(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(self.solution.maxDepth(root), 4)

    def test_uneven_tree(self):
        root = build_tree([1, 2, 3, None, None, 4, 5, None, None, 6])
        self.assertEqual(self.solution.maxDepth(root), 4)

    def test_negative_and_zero_values(self):
        root = build_tree([0, -1, 100, -100, 0])
        self.assertEqual(self.solution.maxDepth(root), 3)

    def test_duplicate_values(self):
        root = build_tree([5, 5, 5, 5, 5, 5, 5])
        self.assertEqual(self.solution.maxDepth(root), 3)

    def test_deep_left_chain_with_right_leaves(self):
        root = build_tree([1, 2, 10, 3, None, 11, None, None, 4])
        self.assertEqual(self.solution.maxDepth(root), 4)


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
