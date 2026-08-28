# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Easy

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        raise Exception("Not solved yet")


def build_tree(values: Optional[List[Optional[int]]]) -> Optional[TreeNode]:
    if values is None or values == []:
        return None
    root = TreeNode(values[0])
    queue = [root]
    index = 1
    while queue and index < len(values):
        node = queue.pop(0)
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.postorderTraversal(None), [])

    def test_single_node(self):
        root = build_tree([1])
        self.assertEqual(self.solution.postorderTraversal(root), [1])

    def test_root_with_left(self):
        root = build_tree([1, 2])
        self.assertEqual(self.solution.postorderTraversal(root), [2, 1])

    def test_root_with_right(self):
        root = build_tree([1, None, 2])
        self.assertEqual(self.solution.postorderTraversal(root), [2, 1])

    def test_example_1(self):
        root = build_tree([1, None, 2, 3])
        self.assertEqual(self.solution.postorderTraversal(root), [3, 2, 1])

    def test_example_2(self):
        root = build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
        self.assertEqual(
            self.solution.postorderTraversal(root), [4, 6, 7, 5, 2, 9, 8, 3, 1]
        )

    def test_full_binary_tree(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.solution.postorderTraversal(root), [4, 5, 2, 6, 7, 3, 1])

    def test_left_skewed(self):
        root = build_tree([1, 2, None, 3])
        self.assertEqual(self.solution.postorderTraversal(root), [3, 2, 1])

    def test_right_skewed(self):
        root = build_tree([1, None, 2, None, 3])
        self.assertEqual(self.solution.postorderTraversal(root), [3, 2, 1])

    def test_negative_and_zero_values(self):
        root = build_tree([-100, 0, 100, -50, 50, -1, 1])
        expected = [-50, 50, 0, -1, 1, 100, -100]
        self.assertEqual(self.solution.postorderTraversal(root), expected)

    def test_duplicate_values(self):
        root = build_tree([5, 5, 5, 5, 5, 5, 5])
        self.assertEqual(self.solution.postorderTraversal(root), [5, 5, 5, 5, 5, 5, 5])

    def test_deep_chain(self):
        root = TreeNode(1)
        current = root
        for value in range(2, 21):
            current.right = TreeNode(value)
            current = current.right
        self.assertEqual(self.solution.postorderTraversal(root), list(range(20, 0, -1)))

    def test_returns_list_types(self):
        result = self.solution.postorderTraversal(build_tree([1, 2, 3]))
        self.assertIsInstance(result, list)
        for value in result:
            self.assertIsInstance(value, int)


if __name__ == "__main__":
    unittest.main()

# Tags: Stack, Tree, Depth-First Search, Binary Tree
