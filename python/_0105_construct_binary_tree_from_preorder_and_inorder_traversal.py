# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Medium

from typing import List, Optional, Dict
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result


def to_level_order_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    result = []
    level = [root]
    while any(node is not None for node in level):
        for node in level:
            result.append(node.val if node is not None else None)
        level = [
            child
            for node in level
            if node is not None
            for child in (node.left, node.right)
        ]
    while result and result[-1] is None:
        result.pop()
    return result


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_node(self):
        self.assertListEqual(
            to_level_order_list(self.solution.buildTree([-1], [-1])), [-1]
        )

    def test_single_node_zero(self):
        self.assertListEqual(
            to_level_order_list(self.solution.buildTree([0], [0])), [0]
        )

    def test_example1(self):
        root = self.solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        self.assertListEqual(to_level_order_list(root), [3, 9, 20, None, None, 15, 7])
        self.assertListEqual(preorder_traversal(root), [3, 9, 20, 15, 7])
        self.assertListEqual(inorder_traversal(root), [9, 3, 15, 20, 7])

    def test_two_nodes_left_only(self):
        root = self.solution.buildTree([1, 2], [2, 1])
        self.assertListEqual(to_level_order_list(root), [1, 2])
        self.assertListEqual(preorder_traversal(root), [1, 2])
        self.assertListEqual(inorder_traversal(root), [2, 1])

    def test_two_nodes_right_only(self):
        root = self.solution.buildTree([1, 2], [1, 2])
        self.assertListEqual(to_level_order_list(root), [1, None, 2])
        self.assertListEqual(preorder_traversal(root), [1, 2])
        self.assertListEqual(inorder_traversal(root), [1, 2])

    def test_full_binary_tree(self):
        root = self.solution.buildTree([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])
        self.assertListEqual(to_level_order_list(root), [1, 2, 3, 4, 5, 6, 7])
        self.assertListEqual(preorder_traversal(root), [1, 2, 4, 5, 3, 6, 7])
        self.assertListEqual(inorder_traversal(root), [4, 2, 5, 1, 6, 3, 7])

    def test_left_skewed(self):
        root = self.solution.buildTree([4, 3, 2, 1], [1, 2, 3, 4])
        self.assertListEqual(to_level_order_list(root), [4, 3, None, 2, None, 1])
        self.assertListEqual(preorder_traversal(root), [4, 3, 2, 1])
        self.assertListEqual(inorder_traversal(root), [1, 2, 3, 4])

    def test_right_skewed(self):
        root = self.solution.buildTree([1, 2, 3, 4], [1, 2, 3, 4])
        self.assertListEqual(to_level_order_list(root), [1, None, 2, None, 3, None, 4])
        self.assertListEqual(preorder_traversal(root), [1, 2, 3, 4])
        self.assertListEqual(inorder_traversal(root), [1, 2, 3, 4])

    def test_left_skewed_alt(self):
        root = self.solution.buildTree([1, 2, 3, 4], [4, 3, 2, 1])
        self.assertListEqual(to_level_order_list(root), [1, 2, None, 3, None, 4])
        self.assertListEqual(inorder_traversal(root), [4, 3, 2, 1])

    def test_negative_and_zero_values(self):
        root = self.solution.buildTree([-2, 0, -3], [0, -2, -3])
        self.assertListEqual(to_level_order_list(root), [-2, 0, -3])
        self.assertListEqual(preorder_traversal(root), [-2, 0, -3])
        self.assertListEqual(inorder_traversal(root), [0, -2, -3])

    def test_large_left_skewed(self):
        n = 500
        preorder = list(range(n, 0, -1))
        inorder = list(range(1, n + 1))
        root = self.solution.buildTree(preorder, inorder)
        self.assertListEqual(preorder_traversal(root), preorder)
        self.assertListEqual(inorder_traversal(root), inorder)

    def test_large_right_skewed(self):
        n = 800
        preorder = list(range(1, n + 1))
        inorder = list(range(n, 0, -1))
        root = self.solution.buildTree(preorder, inorder)
        self.assertListEqual(preorder_traversal(root), preorder)
        self.assertListEqual(inorder_traversal(root), inorder)

    def test_balanced_14_nodes(self):
        pre = [10, 5, 2, 1, 3, 7, 6, 8, 15, 12, 17, 20, 23, 25]
        ino = [1, 2, 3, 5, 6, 7, 8, 10, 12, 15, 17, 20, 23, 25]
        root = self.solution.buildTree(pre, ino)
        self.assertListEqual(preorder_traversal(root), pre)
        self.assertListEqual(inorder_traversal(root), ino)

    def test_root_first_in_inorder_right_subtree(self):
        root = self.solution.buildTree([2, 1], [2, 1])
        self.assertIsNone(root.left)
        self.assertEqual(root.val, 2)
        self.assertEqual(root.right.val, 1)

    def test_max_val_boundaries(self):
        root = self.solution.buildTree([3000, -3000], [-3000, 3000])
        self.assertListEqual(to_level_order_list(root), [3000, -3000])
        self.assertListEqual(inorder_traversal(root), [-3000, 3000])

    def test_mixed_structure(self):
        root = self.solution.buildTree(
            [1, 2, 3, 4, 5],
            [3, 2, 4, 1, 5],
        )
        self.assertListEqual(preorder_traversal(root), [1, 2, 3, 4, 5])
        self.assertListEqual(inorder_traversal(root), [3, 2, 4, 1, 5])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Divide and Conquer, Tree, Binary Tree
