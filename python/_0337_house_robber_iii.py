# 337. House Robber III
# https://leetcode.com/problems/house-robber-iii/
# Medium

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        raise Exception("Not solved yet")


def build_tree(values):
    if values is None:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
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


def build_chain(values):
    root = None
    cur = None
    for val in values:
        node = TreeNode(val)
        if root is None:
            root = node
        else:
            cur.left = node
        cur = node
    return root


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.rob(build_tree([3, 2, 3, None, 3, None, 1])), 7)

    def test_example_2(self):
        self.assertEqual(self.solution.rob(build_tree([3, 4, 5, 1, 3, None, 1])), 9)

    def test_single_node(self):
        self.assertEqual(self.solution.rob(build_tree([100])), 100)

    def test_single_node_zero(self):
        self.assertEqual(self.solution.rob(build_tree([0])), 0)

    def test_two_nodes_prefers_child(self):
        self.assertEqual(self.solution.rob(build_tree([1, 2])), 2)

    def test_two_nodes_prefers_root(self):
        self.assertEqual(self.solution.rob(build_tree([5, 2])), 5)

    def test_three_nodes_prefers_root(self):
        self.assertEqual(self.solution.rob(build_tree([10, 1, 1])), 10)

    def test_three_nodes_prefers_children(self):
        self.assertEqual(self.solution.rob(build_tree([1, 10, 10])), 20)

    def test_all_zeros(self):
        self.assertEqual(self.solution.rob(build_tree([0, 0, 0, 0, 0, 0, 0])), 0)

    def test_chain_left(self):
        self.assertEqual(self.solution.rob(build_chain([1, 2, 3, 4])), 6)

    def test_chain_left_odd(self):
        self.assertEqual(self.solution.rob(build_chain([5, 1, 5, 1, 5])), 15)

    def test_chain_right(self):
        self.assertEqual(self.solution.rob(build_chain([4, 3, 2, 1])), 6)

    def test_full_tree(self):
        self.assertEqual(self.solution.rob(build_tree([1, 2, 3, 4, 5, 6, 7])), 23)

    def test_deep_chain(self):
        self.assertEqual(self.solution.rob(build_chain(list(range(1, 11)))), 30)

    def test_large_values(self):
        self.assertEqual(self.solution.rob(build_tree([10000, 10000, 10000])), 20000)

    def test_only_left_subtree_with_grandchild(self):
        self.assertEqual(self.solution.rob(build_tree([1, 2, None, 3])), 4)


if __name__ == "__main__":
    unittest.main()

# Tags: Dynamic Programming, Tree, Depth-First Search, Binary Tree, DP on Trees
