# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
# Medium

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        raise Exception("Not solved yet")


def build_tree(values):
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    root = nodes[0]
    j = 1
    for i, node in enumerate(nodes):
        if node is None:
            continue
        if j < len(nodes):
            node.left = nodes[j]
            j += 1
        if j < len(nodes):
            node.right = nodes[j]
            j += 1
    return root


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.rightSideView(build_tree([])), [])

    def test_single_node(self):
        self.assertEqual(self.solution.rightSideView(build_tree([1])), [1])

    def test_example1(self):
        self.assertEqual(
            self.solution.rightSideView(build_tree([1, 2, 3, None, 5, None, 4])),
            [1, 3, 4],
        )

    def test_example2(self):
        self.assertEqual(
            self.solution.rightSideView(build_tree([1, 2, 3, 4, None, None, None, 5])),
            [1, 3, 4, 5],
        )

    def test_example3(self):
        self.assertEqual(self.solution.rightSideView(build_tree([1, None, 3])), [1, 3])

    def test_left_branch_only(self):
        self.assertEqual(
            self.solution.rightSideView(build_tree([1, 2, None, 3])), [1, 2, 3]
        )

    def test_right_branch_only(self):
        self.assertEqual(
            self.solution.rightSideView(build_tree([1, None, 2, None, 3])), [1, 2, 3]
        )

    def test_two_level_full(self):
        self.assertEqual(self.solution.rightSideView(build_tree([1, 2, 3])), [1, 3])

    def test_two_level_incomplete(self):
        self.assertEqual(self.solution.rightSideView(build_tree([1, 2, None])), [1, 2])

    def test_three_level_full(self):
        self.assertEqual(
            self.solution.rightSideView(build_tree([1, 2, 3, 4, 5, 6, 7])), [1, 3, 7]
        )

    def test_left_heavy_tree(self):
        self.assertEqual(
            self.solution.rightSideView(build_tree([1, 2, 3, None, 4])), [1, 3, 4]
        )

    def test_right_deeper_than_left(self):
        self.assertEqual(
            self.solution.rightSideView(build_tree([1, 2, 3, 4])), [1, 3, 4]
        )

    def test_negative_values(self):
        self.assertEqual(
            self.solution.rightSideView(build_tree([-1, -2, -3])), [-1, -3]
        )

    def test_zero_values(self):
        self.assertEqual(self.solution.rightSideView(build_tree([0, 0, 0])), [0, 0])

    def test_duplicate_values(self):
        self.assertEqual(
            self.solution.rightSideView(build_tree([5, 5, 5, 5])), [5, 5, 5]
        )

    def test_deep_left_chain(self):
        self.assertEqual(
            self.solution.rightSideView(build_tree([1, 2, None, 3, None, 4])),
            [1, 2, 3, 4],
        )

    def test_unbalanced_right(self):
        self.assertEqual(
            self.solution.rightSideView(build_tree([1, None, 2, 3])), [1, 2, 3]
        )

    def test_single_left_child(self):
        self.assertEqual(
            self.solution.rightSideView(build_tree([1, 2, None, None, 3])), [1, 2, 3]
        )

    def test_mixed_width(self):
        self.assertEqual(
            self.solution.rightSideView(build_tree([10, 5, 15, 3, 7, 12, 20])),
            [10, 15, 20],
        )

    def test_node_bound_values(self):
        self.assertEqual(
            self.solution.rightSideView(build_tree([-100, 100, -100])), [-100, -100]
        )

    def test_large_width(self):
        tree = build_tree([1] + [2] * 98)
        result = self.solution.rightSideView(tree)
        self.assertEqual(result[0], 1)
        self.assertEqual(len(result), 7)


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
