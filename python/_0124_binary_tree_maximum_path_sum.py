# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Hard

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        raise Exception("Not solved yet")


import unittest


def build_tree(values):
    if not values:
        return None
    nodes = [None] * len(values)
    for i, v in enumerate(values):
        if v is not None:
            nodes[i] = TreeNode(v)
    for i, v in enumerate(values):
        if v is None:
            continue
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < len(values):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(values):
            nodes[i].right = nodes[right_idx]
    return nodes[0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_two_children(self):
        root = build_tree([1, 2, 3])
        self.assertEqual(self.solution.maxPathSum(root), 6)

    def test_negative_root_with_positive_branch(self):
        root = build_tree([-10, 9, 20, None, None, 15, 7])
        self.assertEqual(self.solution.maxPathSum(root), 42)

    def test_single_node_positive(self):
        root = build_tree([5])
        self.assertEqual(self.solution.maxPathSum(root), 5)

    def test_single_node_negative(self):
        root = build_tree([-3])
        self.assertEqual(self.solution.maxPathSum(root), -3)

    def test_all_negative_tree(self):
        root = build_tree([-2, -5, -1, None, None, -4, -3])
        self.assertEqual(self.solution.maxPathSum(root), -1)

    def test_left_chain(self):
        root = build_tree([1, 2, None, 3, None, None, None, 4])
        self.assertEqual(self.solution.maxPathSum(root), 10)

    def test_right_chain(self):
        root = build_tree([1, None, 2, None, None, 3, None, None, None, None, None, 4])
        self.assertEqual(self.solution.maxPathSum(root), 10)

    def test_path_not_through_root(self):
        root = build_tree([0, -1, -2, None, None, -3, -4])
        self.assertEqual(self.solution.maxPathSum(root), 0)

    def test_deep_left_branch_beats_root(self):
        root = build_tree([-1000, 1000, None, 1000])
        self.assertEqual(self.solution.maxPathSum(root), 2000)

    def test_both_branches_used(self):
        root = build_tree([10, 5, -1, None, -100, None, 2])
        self.assertEqual(self.solution.maxPathSum(root), 16)

    def test_negative_child_ignored(self):
        root = build_tree([5, -1, -2, None, None, -3, -4])
        self.assertEqual(self.solution.maxPathSum(root), 5)

    def test_mixed_values_multi_level(self):
        root = build_tree([4, -7, -3, None, None, -4, -1])
        self.assertEqual(self.solution.maxPathSum(root), 4)

    def test_long_skewed_all_positive(self):
        values = [
            1,
            2,
            None,
            3,
            None,
            None,
            None,
            4,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            5,
        ]
        root = build_tree(values)
        self.assertEqual(self.solution.maxPathSum(root), 15)

    def test_zero_values(self):
        root = build_tree([0, 0, 0])
        self.assertEqual(self.solution.maxPathSum(root), 0)

    def test_single_zero(self):
        root = build_tree([0])
        self.assertEqual(self.solution.maxPathSum(root), 0)

    def test_one_negative_child_beneficial(self):
        root = build_tree([-1, -2, -3])
        self.assertEqual(self.solution.maxPathSum(root), -1)

    def test_leaf_beats_everything(self):
        root = build_tree([-1000, -1000, -1000, None, None, -1000, 1000])
        self.assertEqual(self.solution.maxPathSum(root), 1000)

    def test_symmetric_positive(self):
        root = build_tree([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])
        self.assertEqual(self.solution.maxPathSum(root), 19)

    def test_null_children_explicit(self):
        root = build_tree([5, None, None])
        self.assertEqual(self.solution.maxPathSum(root), 5)


if __name__ == "__main__":
    unittest.main()

# Tags: Dynamic Programming, Tree, Depth-First Search, Binary Tree, DP on Trees
