# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Medium

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> Optional["TreeNode"]:
        raise Exception("Not solved yet")


def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
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


def find_node(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left is not None:
        return left
    return find_node(root.right, val)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def lca(self, root_vals, p_val, q_val):
        root = build_tree(root_vals)
        p = find_node(root, p_val)
        q = find_node(root, q_val)
        return self.solution.lowestCommonAncestor(root, p, q)

    def test_p_and_q_on_opposite_sides(self):
        result = self.lca([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 6)

    def test_p_is_ancestor_of_q(self):
        result = self.lca([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 2)

    def test_q_is_ancestor_of_p(self):
        result = self.lca([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 4, 2)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 2)

    def test_root_is_lca(self):
        result = self.lca([2, 1], 2, 1)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 2)

    def test_two_node_tree_children_of_root(self):
        result = self.lca([2, 1, 3], 1, 3)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 2)

    def test_deep_left_chain(self):
        result = self.lca([5, 3, None, 2, None, 1], 1, 5)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 5)

    def test_deep_right_chain(self):
        result = self.lca([5, None, 8, None, 10, None, 12], 5, 12)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 5)

    def test_leaves_in_different_subtrees(self):
        result = self.lca([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15], 1, 15)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 8)

    def test_leaves_sharing_nearest_ancestor(self):
        result = self.lca([8, 4, 12, 2, 6], 2, 6)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 4)

    def test_negative_values(self):
        result = self.lca([-10, -20, 0, -25, -15, -5, 5], -25, 5)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, -10)

    def test_all_negative_values_ancestor(self):
        result = self.lca([-10, -20, -5], -20, -10)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, -10)

    def test_large_values(self):
        small = 10**9 - 1
        result = self.lca([10**9, small], small, 10**9)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 10**9)

    def test_result_is_actual_node(self):
        root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 4)
        q = find_node(root, 3)
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertIs(result, p)

    def test_same_branch_ancestor_of_both(self):
        result = self.lca([10, 5, 15, 3, 6], 3, 6)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 5)

    def test_swapped_arguments(self):
        first = self.lca([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 8, 2)
        second = self.lca([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8)
        self.assertEqual(first.val, second.val)


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree, Binary Lifting, Lowest Common Ancestor
