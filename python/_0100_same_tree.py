# 100. Same Tree
# https://leetcode.com/problems/same-tree/
# Easy

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        raise Exception("Not solved yet")


def build(values):
    if values is None:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    for i, node in enumerate(nodes):
        if node is None:
            continue
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < len(nodes):
            node.left = nodes[left_idx]
        if right_idx < len(nodes):
            node.right = nodes[right_idx]
    return nodes[0]


import unittest


class TestSameTree(unittest.TestCase):
    def test_both_empty(self):
        self.assertTrue(Solution().isSameTree(None, None))

    def test_one_empty(self):
        self.assertFalse(Solution().isSameTree(TreeNode(1), None))
        self.assertFalse(Solution().isSameTree(None, TreeNode(1)))

    def test_identical_single_nodes(self):
        self.assertTrue(Solution().isSameTree(TreeNode(1), TreeNode(1)))

    def test_different_single_nodes(self):
        self.assertFalse(Solution().isSameTree(TreeNode(1), TreeNode(2)))

    def test_same_trees_123(self):
        p = build([1, 2, 3])
        q = build([1, 2, 3])
        self.assertTrue(Solution().isSameTree(p, q))

    def test_different_structure(self):
        p = build([1, 2])
        q = build([1, None, 2])
        self.assertFalse(Solution().isSameTree(p, q))

    def test_swapped_children(self):
        p = build([1, 2, 1])
        q = build([1, 1, 2])
        self.assertFalse(Solution().isSameTree(p, q))

    def test_full_identical_tree(self):
        vals = [1, 2, 3, 4, 5, 6, 7]
        p = build(vals)
        q = build(vals)
        self.assertTrue(Solution().isSameTree(p, q))

    def test_negative_values(self):
        p = build([-1, -2, -3])
        q = build([-1, -2, -3])
        self.assertTrue(Solution().isSameTree(p, q))
        r = build([-1, -3, -2])
        self.assertFalse(Solution().isSameTree(p, r))

    def test_zero_values(self):
        self.assertTrue(Solution().isSameTree(build([0]), build([0])))

    def test_deep_left_chain(self):
        def chain(k):
            root = TreeNode(1)
            cur = root
            for _ in range(k):
                cur.left = TreeNode(1)
                cur = cur.left
            return root

        self.assertTrue(Solution().isSameTree(chain(49), chain(49)))

    def test_deep_left_chain_diff_depth(self):
        def chain(k):
            root = TreeNode(1)
            cur = root
            for _ in range(k):
                cur.left = TreeNode(1)
                cur = cur.left
            return root

        self.assertFalse(Solution().isSameTree(chain(5), chain(4)))

    def test_one_node_with_child_other_without(self):
        p = build([1, 2])
        q = build([1])
        self.assertFalse(Solution().isSameTree(p, q))

    def test_children_present_only_in_one(self):
        p = build([1, 2, 3])
        q = build([1, 2])
        self.assertFalse(Solution().isSameTree(p, q))

    def test_deep_mismatch_bottom(self):
        p = build([1, 1, 1, 1, 1, 1, 2])
        q = build([1, 1, 1, 1, 1, 1, 1])
        self.assertFalse(Solution().isSameTree(p, q))

    def test_non_increasing_values_identical(self):
        p = build([5, 4, 3, 2, 1])
        q = build([5, 4, 3, 2, 1])
        self.assertTrue(Solution().isSameTree(p, q))

    def test_100_nodes_identical(self):
        vals = list(range(1, 101))
        p = build(vals)
        q = build(vals)
        self.assertTrue(Solution().isSameTree(p, q))


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
