# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Easy

import collections
import unittest
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        raise Exception("Not solved yet")


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = collections.deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if index < len(values):
            value = values[index]
            index += 1
            if value is not None:
                node.left = TreeNode(value)
                queue.append(node.left)
        if index < len(values):
            value = values[index]
            index += 1
            if value is not None:
                node.right = TreeNode(value)
                queue.append(node.right)
    return root


class InorderTraversalTest(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(Solution().inorderTraversal(None), [])

    def test_single_node(self):
        self.assertEqual(Solution().inorderTraversal(build_tree([1])), [1])

    def test_example_one(self):
        self.assertEqual(
            Solution().inorderTraversal(build_tree([1, None, 2, 3])), [1, 3, 2]
        )

    def test_example_two(self):
        values = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
        self.assertEqual(
            Solution().inorderTraversal(build_tree(values)), [4, 2, 6, 5, 7, 1, 3, 9, 8]
        )

    def test_left_skewed_tree(self):
        root = TreeNode(3, TreeNode(2, TreeNode(1)), None)
        self.assertEqual(Solution().inorderTraversal(root), [1, 2, 3])

    def test_right_skewed_tree(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(Solution().inorderTraversal(root), [1, 2, 3])

    def test_bst_inorder_is_sorted(self):
        values = [8, 3, 10, 1, 6, None, 14]
        self.assertEqual(
            Solution().inorderTraversal(build_tree(values)), [1, 3, 6, 8, 10, 14]
        )

    def test_negative_values(self):
        values = [-5, -10, -1, -15, -5, None, 0]
        self.assertEqual(
            Solution().inorderTraversal(build_tree(values)), [-15, -10, -5, -5, -1, 0]
        )

    def test_duplicate_values(self):
        values = [2, 2, 2, 2, 2, 2, 2]
        self.assertEqual(Solution().inorderTraversal(build_tree(values)), [2] * 7)

    def test_full_binary_tree(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(
            Solution().inorderTraversal(build_tree(values)), [4, 2, 5, 1, 6, 3, 7]
        )

    def test_node_with_only_left_child(self):
        self.assertEqual(Solution().inorderTraversal(build_tree([1, 2])), [2, 1])

    def test_node_with_only_right_child(self):
        self.assertEqual(Solution().inorderTraversal(build_tree([1, None, 2])), [1, 2])

    def test_deep_left_chain(self):
        root = TreeNode(1)
        node = root
        for value in range(2, 6):
            node.left = TreeNode(value)
            node = node.left
        self.assertEqual(Solution().inorderTraversal(root), [5, 4, 3, 2, 1])

    def test_result_is_list(self):
        result = Solution().inorderTraversal(build_tree([1, 2, 3]))
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()

# Tags: Stack, Tree, Depth-First Search, Binary Tree
