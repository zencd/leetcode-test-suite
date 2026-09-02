# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Easy

import unittest
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        raise Exception("Not solved yet")

    def preorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        raise Exception("Not solved yet")


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.left = TreeNode(v)
                queue.append(node.left)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.right = TreeNode(v)
                queue.append(node.right)
    return root


def build_skewed(depth, side):
    root = TreeNode(1)
    node = root
    for v in range(2, depth + 1):
        child = TreeNode(v)
        if side == "left":
            node.left = child
        else:
            node.right = child
        node = child
    return root


SOLUTIONS = (
    ("recursive", Solution().preorderTraversal),
    ("iterative", Solution().preorderTraversalIterative),
)


class TestSolution(unittest.TestCase):
    def _check(self, values, expected):
        for name, fn in SOLUTIONS:
            with self.subTest(values=values, impl=name):
                self.assertEqual(fn(build_tree(values)), expected)

    def test_empty_tree(self):
        self._check([], [])

    def test_single_node(self):
        self._check([1], [1])

    def test_example1(self):
        self._check([1, None, 2, 3], [1, 2, 3])

    def test_example2(self):
        self._check(
            [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [1, 2, 4, 5, 6, 7, 3, 8, 9]
        )

    def test_left_chain(self):
        self._check([1, 2, None, 3, None, 4, None, 5, None], [1, 2, 3, 4, 5])

    def test_right_chain(self):
        self._check([1, None, 2, None, 3, None, 4, None, 5], [1, 2, 3, 4, 5])

    def test_full_binary_tree(self):
        self._check([1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 3, 6, 7])

    def test_negative_values(self):
        self._check([-1, -2, -3, -100, 100], [-1, -2, -100, 100, -3])

    def test_duplicate_values(self):
        self._check([5, 5, 5, 5], [5, 5, 5, 5])

    def test_left_only_children(self):
        self._check([1, 2, None, 3, None, 4, None, 5, None], [1, 2, 3, 4, 5])

    def test_right_only_children(self):
        self._check([1, None, 2, None, 3, None, 4, None, 5], [1, 2, 3, 4, 5])

    def test_unbalanced_tree(self):
        self._check(
            [1, 2, 3, None, 4, 5, None, None, None, 6, 7, 9], [1, 2, 4, 3, 5, 6, 9, 7]
        )

    def test_zero_value(self):
        self._check([0, 0, 0], [0, 0, 0])

    def test_deep_left_skewed_tree(self):
        for name, fn in SOLUTIONS:
            with self.subTest(impl=name):
                self.assertEqual(fn(build_skewed(100, "left")), list(range(1, 101)))

    def test_deep_right_skewed_tree(self):
        for name, fn in SOLUTIONS:
            with self.subTest(impl=name):
                self.assertEqual(fn(build_skewed(100, "right")), list(range(1, 101)))

    def test_returns_new_list_each_call(self):
        fn = Solution().preorderTraversal
        root = build_tree([1, 2, 3])
        first = fn(root)
        first.append(99)
        self.assertEqual(fn(root), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()

# Tags: Stack, Tree, Depth-First Search, Binary Tree
