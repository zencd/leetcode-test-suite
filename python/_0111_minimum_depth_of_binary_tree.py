# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Easy

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.minDepth(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.minDepth(root), 1)

    def test_example1(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(self.solution.minDepth(root), 2)

    def test_example2(self):
        root = build_tree([2, None, 3, None, 4, None, 5, None, 6])
        self.assertEqual(self.solution.minDepth(root), 5)

    def test_root_with_left_child_only(self):
        root = TreeNode(1, TreeNode(2), None)
        self.assertEqual(self.solution.minDepth(root), 2)

    def test_root_with_right_child_only(self):
        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(self.solution.minDepth(root), 2)

    def test_symmetric_two_levels(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.solution.minDepth(root), 3)

    def test_left_skewed_tree(self):
        root = build_tree([1, 2, None, 3, None, 4])
        self.assertEqual(self.solution.minDepth(root), 4)

    def test_right_skewed_tree(self):
        root = build_tree([1, None, 2, None, 3, None, 4])
        self.assertEqual(self.solution.minDepth(root), 4)

    def test_all_leaves_at_depth_3(self):
        root = build_tree([1, 2, 3, 4, None, 5, 6])
        self.assertEqual(self.solution.minDepth(root), 3)

    def test_only_leaves_on_inner_positions(self):
        root = build_tree([1, 2, 3, None, 4, 5, None])
        self.assertEqual(self.solution.minDepth(root), 3)

    def test_chain_through_right_children(self):
        root = build_tree([1, 2, None, None, 3, None, 4])
        self.assertEqual(self.solution.minDepth(root), 4)

    def test_values_not_matter(self):
        root = build_tree([1000, -1000, 0, None, None, -999, 500])
        self.assertEqual(self.solution.minDepth(root), 2)

    def test_wide_shallow_tree(self):
        values = [0] + [1] * 7 + [2] * 4
        root = build_tree(values)
        self.assertEqual(self.solution.minDepth(root), 3)

    def test_large_skewed_tree(self):
        n = 100000
        node = TreeNode(n)
        curr = node
        for i in range(n - 1, 0, -1):
            curr.right = TreeNode(i)
            curr = curr.right
        self.assertEqual(self.solution.minDepth(node), n)


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
