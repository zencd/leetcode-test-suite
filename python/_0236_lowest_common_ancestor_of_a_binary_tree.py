# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
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
    ) -> "TreeNode":
        raise Exception("Not solved yet")


def build_tree(values, index=0):
    if index >= len(values) or values[index] is None:
        return None
    node = TreeNode(values[index])
    node.left = build_tree(values, index * 2 + 1)
    node.right = build_tree(values, index * 2 + 2)
    return node


def find_node(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    left = find_node(root.left, target)
    if left is not None:
        return left
    return find_node(root.right, target)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1_root_is_lca(self):
        tree = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        root = build_tree(tree)
        p = find_node(root, 5)
        q = find_node(root, 1)
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertIsNotNone(result)
        self.assertEqual(3, result.val)

    def test_example2_ancestor_is_p(self):
        tree = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        root = build_tree(tree)
        p = find_node(root, 5)
        q = find_node(root, 4)
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertIsNotNone(result)
        self.assertEqual(5, result.val)

    def test_example3_two_node_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        p, q = root, root.left
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertIs(root, result)

    def test_p_is_left_child_q_is_right_child(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        result = self.solution.lowestCommonAncestor(root, root.left, root.right)
        self.assertIs(root, result)

    def test_p_and_q_in_left_subtree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        result = self.solution.lowestCommonAncestor(
            root, root.left.left, root.left.right
        )
        self.assertIs(root.left, result)

    def test_p_and_q_in_right_subtree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        result = self.solution.lowestCommonAncestor(
            root, root.right.left, root.right.right
        )
        self.assertIs(root.right, result)

    def test_deeper_chain_p_ancestor_of_q(self):
        root = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        root.left = n2
        n2.right = n3
        n3.right = n4
        result = self.solution.lowestCommonAncestor(root, n2, n4)
        self.assertIs(n2, result)

    def test_q_ancestor_of_p(self):
        root = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        root.right = n2
        n2.left = n3
        result = self.solution.lowestCommonAncestor(root, n3, n2)
        self.assertIs(n2, result)

    def test_leaves_in_different_branches(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right = TreeNode(6)
        root.right.left = TreeNode(7)
        result = self.solution.lowestCommonAncestor(
            root, root.left.left, root.right.left
        )
        self.assertIs(root, result)

    def test_lca_not_root_deep(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(8)
        root.right = TreeNode(4)
        result = self.solution.lowestCommonAncestor(
            root, root.left.right.left, root.left.right.right
        )
        self.assertIs(root.left.right, result)

    def test_skewed_tree(self):
        root = TreeNode(1)
        a = TreeNode(2)
        b = TreeNode(3)
        c = TreeNode(4)
        root.right = a
        a.right = b
        b.right = c
        result = self.solution.lowestCommonAncestor(root, a, c)
        self.assertIs(a, result)

    def test_negative_values(self):
        root = TreeNode(-10)
        root.left = TreeNode(-20)
        root.right = TreeNode(-30)
        result = self.solution.lowestCommonAncestor(root, root.left, root.right)
        self.assertIs(root, result)

    def test_large_values(self):
        root = TreeNode(10**9)
        root.left = TreeNode(-(10**9))
        root.right = TreeNode(10**8)
        result = self.solution.lowestCommonAncestor(root, root.left, root.right)
        self.assertIs(root, result)

    def test_result_is_p_when_p_is_root(self):
        root = TreeNode(5)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        result = self.solution.lowestCommonAncestor(root, root, root.left)
        self.assertIs(root, result)

    def test_result_is_q_when_q_is_root(self):
        root = TreeNode(5)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        result = self.solution.lowestCommonAncestor(root, root.left, root)
        self.assertIs(root, result)

    def test_full_four_level_tree_lca_at_level_two(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)
        result = self.solution.lowestCommonAncestor(
            root, root.left.left.left, root.left.left.right
        )
        self.assertIs(root.left.left, result)

    def test_cross_subtree_leaves_deepest(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(4)
        root.left.right.left = TreeNode(6)
        root.right.left.right = TreeNode(7)
        result = self.solution.lowestCommonAncestor(
            root, root.left.right.left, root.right.left.right
        )
        self.assertIs(root, result)

    def test_siblings_directly(self):
        root = TreeNode(10)
        root.left = TreeNode(20)
        root.right = TreeNode(30)
        result = self.solution.lowestCommonAncestor(root, root.left, root.right)
        self.assertEqual(10, result.val)

    def test_p_is_only_node_path(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.left.right.right = TreeNode(4)
        result = self.solution.lowestCommonAncestor(
            root, root.left, root.left.right.right
        )
        self.assertIs(root.left, result)


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Binary Tree, Binary Lifting, Lowest Common Ancestor
