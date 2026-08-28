# 112. Path Sum
# https://leetcode.com/problems/path-sum/
# Easy

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        raise Exception("Not solved yet")


def build(values):
    nodes = [None if v is None else TreeNode(v) for v in values]
    for i, node in enumerate(nodes):
        if node is None:
            continue
        li, ri = 2 * i + 1, 2 * i + 2
        if li < len(nodes):
            node.left = nodes[li]
        if ri < len(nodes):
            node.right = nodes[ri]
    return nodes[0] if nodes else None


import sys
import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        sys.setrecursionlimit(max(sys.getrecursionlimit(), 20000))
        self.sol = Solution()

    def test_example1(self):
        root = build([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
        self.assertTrue(self.sol.hasPathSum(root, 22))

    def test_example2(self):
        root = build([1, 2, 3])
        self.assertFalse(self.sol.hasPathSum(root, 5))

    def test_example3_empty_tree(self):
        self.assertFalse(self.sol.hasPathSum(None, 0))

    def test_single_node_matching(self):
        self.assertTrue(self.sol.hasPathSum(TreeNode(5), 5))

    def test_single_node_not_matching(self):
        self.assertFalse(self.sol.hasPathSum(TreeNode(5), 3))

    def test_single_node_zero_target(self):
        self.assertTrue(self.sol.hasPathSum(TreeNode(0), 0))

    def test_empty_tree_zero_nodes_target_negative(self):
        self.assertFalse(self.sol.hasPathSum(None, -1000))

    def test_negative_node_values(self):
        root = build([-2, None, None])
        self.assertTrue(self.sol.hasPathSum(root, -2))

    def test_negative_values_path(self):
        root = build([1, -2, 3, -1, None, None, -1])
        self.assertTrue(self.sol.hasPathSum(root, -2))
        self.assertTrue(self.sol.hasPathSum(root, 3))
        self.assertFalse(self.sol.hasPathSum(root, 0))

    def test_non_leaf_intermediate_sum_does_not_count(self):
        root = build([1, 0])
        self.assertTrue(self.sol.hasPathSum(root, 1))
        self.assertFalse(self.sol.hasPathSum(root, 0))

    def test_deep_left_spine(self):
        node = TreeNode(0)
        cur = node
        for _ in range(4999):
            cur.left = TreeNode(0)
            cur = cur.left
        self.assertTrue(self.sol.hasPathSum(node, 0))
        self.assertFalse(self.sol.hasPathSum(node, 1))

    def test_deep_right_spine(self):
        node = TreeNode(1)
        cur = node
        for _ in range(20):
            cur.right = TreeNode(1)
            cur = cur.right
        self.assertTrue(self.sol.hasPathSum(node, 21))
        self.assertFalse(self.sol.hasPathSum(node, 20))

    def test_wide_tree_only_right_leaf_matches(self):
        root = build([0, -1, 5, -1, -1, -1, -1])
        self.assertTrue(self.sol.hasPathSum(root, 4))
        self.assertFalse(self.sol.hasPathSum(root, 5))

    def test_all_paths_share_no_target(self):
        root = build([2, 4, 8, 11, 13, 4])
        sums = [2 + 4 + 11, 2 + 4 + 13, 2 + 8 + 4]
        for s in sums:
            self.assertTrue(self.sol.hasPathSum(root, s))
        self.assertFalse(self.sol.hasPathSum(root, sum(sums)))
        self.assertFalse(self.sol.hasPathSum(None, sum(sums)))

    def test_extreme_values(self):
        root = build([1000, -1000])
        self.assertTrue(self.sol.hasPathSum(root, 0))
        root2 = build([1000, 1000])
        self.assertTrue(self.sol.hasPathSum(root2, 2000))
        self.assertFalse(self.sol.hasPathSum(root2, 1000))


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
