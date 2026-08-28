# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Medium

import random
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)

    dfs(root)
    return result


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        root = self.solution.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
        self.assertEqual(inorder_traversal(root), [9, 3, 15, 20, 7])
        self.assertEqual(postorder_traversal(root), [9, 15, 7, 20, 3])

    def test_example2_single_node(self):
        root = self.solution.buildTree([-1], [-1])
        self.assertEqual(root.val, -1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_single_node_zero(self):
        root = self.solution.buildTree([0], [0])
        self.assertEqual(root.val, 0)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_left_skewed(self):
        root = self.solution.buildTree([3, 2, 1], [3, 2, 1])
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.left.left.val, 3)
        self.assertIsNone(root.left.right)
        self.assertIsNone(root.right)

    def test_right_skewed(self):
        root = self.solution.buildTree([1, 2, 3], [3, 2, 1])
        self.assertEqual(root.val, 1)
        self.assertEqual(root.right.val, 2)
        self.assertEqual(root.right.right.val, 3)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right.left)

    def test_depth2_balanced(self):
        root = self.solution.buildTree([2, 1, 3], [2, 3, 1])
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.right.right)

    def test_negative_values(self):
        root = self.solution.buildTree([-5, -3, -2, -8, -1], [-5, -8, -2, -1, -3])
        self.assertEqual(root.val, -3)
        self.assertEqual(inorder_traversal(root), [-5, -3, -2, -8, -1])

    def test_two_nodes(self):
        root = self.solution.buildTree([2, 1], [2, 1])
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertIsNone(root.right)

    def test_mixed_structure(self):
        root = self.solution.buildTree([7, 2, 4, 1, 5, 3, 8], [7, 4, 2, 5, 8, 3, 1])
        self.assertEqual(root.val, 1)
        self.assertEqual(inorder_traversal(root), [7, 2, 4, 1, 5, 3, 8])
        self.assertEqual(postorder_traversal(root), [7, 4, 2, 5, 8, 3, 1])

    def test_many_left_children(self):
        n = 5
        inorder = list(range(5, 0, -1))
        postorder = list(range(5, 0, -1))
        root = self.solution.buildTree(inorder, postorder)
        self.assertEqual(inorder_traversal(root), inorder)
        current = root
        expected = 1
        while current:
            self.assertEqual(current.val, expected)
            expected += 1
            current = current.left
        self.assertIsNone(current)

    def test_mixed_positive_negative(self):
        base = TreeNode(
            0,
            TreeNode(-1000, TreeNode(2000), TreeNode(1500)),
            TreeNode(3000, TreeNode(-3000)),
        )
        inorder = inorder_traversal(base)
        postorder = postorder_traversal(base)
        rebuilt = self.solution.buildTree(inorder, postorder)
        self.assertEqual(inorder_traversal(rebuilt), inorder)
        self.assertEqual(postorder_traversal(rebuilt), postorder)

    def test_preorder_nodes_match_leetcode_form(self):
        root = self.solution.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
        result = []

        def dfs(node):
            if node is None:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        self.assertEqual(result, [3, 9, 20, 15, 7])

    def test_larger_random_tree(self):
        random.seed(42)
        root = self._random_tree(20)
        inorder = inorder_traversal(root)
        postorder = postorder_traversal(root)
        rebuilt = self.solution.buildTree(inorder, postorder)
        self.assertEqual(inorder_traversal(rebuilt), inorder)
        self.assertEqual(postorder_traversal(rebuilt), postorder)

    def _random_tree(self, n: int) -> Optional[TreeNode]:
        values = random.sample(range(-3000, 3001), n)
        return self._build_random(values)

    def _build_random(self, values: List[int]) -> Optional[TreeNode]:
        if not values:
            return None
        mid = len(values) // 2
        left = self._build_random(values[:mid])
        right = self._build_random(values[mid + 1 :])
        return TreeNode(values[mid], left, right)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Divide and Conquer, Tree, Binary Tree
