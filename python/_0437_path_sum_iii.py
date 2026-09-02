# 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/
# Medium

from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        raise Exception("Not solved yet")


import unittest


def build_tree(values):
    if not values or values[0] is None:
        return None
    from collections import deque

    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.left = TreeNode(v)
                q.append(node.left)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.right = TreeNode(v)
                q.append(node.right)
    return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        root = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
        self.assertEqual(self.sol.pathSum(root, 8), 3)

    def test_example_2(self):
        root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
        self.assertEqual(self.sol.pathSum(root, 22), 3)

    def test_empty_tree(self):
        self.assertEqual(self.sol.pathSum(None, 8), 0)

    def test_single_node_match(self):
        root = build_tree([8])
        self.assertEqual(self.sol.pathSum(root, 8), 1)

    def test_single_node_no_match(self):
        root = build_tree([8])
        self.assertEqual(self.sol.pathSum(root, 10), 0)

    def test_target_zero_single_node(self):
        root = build_tree([0])
        self.assertEqual(self.sol.pathSum(root, 0), 1)

    def test_negative_target(self):
        root = build_tree([5, -3, 11, -2, -25])
        self.assertEqual(self.sol.pathSum(root, -28), 1)

    def test_negative_nodes(self):
        root = build_tree([-2, -5, None, None, 1])
        self.assertEqual(self.sol.pathSum(root, -7), 1)
        self.assertEqual(self.sol.pathSum(root, -2), 1)
        self.assertEqual(self.sol.pathSum(root, -5), 1)
        self.assertEqual(self.sol.pathSum(root, 1), 1)
        self.assertEqual(self.sol.pathSum(root, -6), 1)
        self.assertEqual(self.sol.pathSum(root, -10), 0)

    def test_multiple_paths_same_sum(self):
        root = build_tree([1, 1, 1])
        self.assertEqual(self.sol.pathSum(root, 2), 2)

    def test_zero_valued_nodes(self):
        root = build_tree([0, 0, 0])
        self.assertEqual(self.sol.pathSum(root, 0), 5)

    def test_large_positive_values(self):
        root = build_tree([10**9, 10**9])
        self.assertEqual(self.sol.pathSum(root, 2 * 10**9), 1)

    def test_large_negative_values(self):
        root = build_tree([-(10**9), -(10**9)])
        self.assertEqual(self.sol.pathSum(root, -2 * 10**9), 1)

    def test_chain_tree(self):
        root = build_tree([5, 3])
        self.assertEqual(self.sol.pathSum(root, 8), 1)
        self.assertEqual(self.sol.pathSum(root, 5), 1)
        self.assertEqual(self.sol.pathSum(root, 3), 1)
        self.assertEqual(self.sol.pathSum(root, 7), 0)

    def test_no_path(self):
        root = build_tree([1, 2, 3])
        self.assertEqual(self.sol.pathSum(root, 100), 0)

    def test_root_only_path_negative(self):
        root = build_tree([1, -1, -4])
        self.assertEqual(self.sol.pathSum(root, -4), 1)
        self.assertEqual(self.sol.pathSum(root, -3), 1)
        self.assertEqual(self.sol.pathSum(root, 0), 1)
        self.assertEqual(self.sol.pathSum(root, -1), 1)
        self.assertEqual(self.sol.pathSum(root, -5), 0)

    def test_path_through_right_subtree(self):
        root = build_tree([0, 5, 23, None, None, None, 20])
        self.assertEqual(self.sol.pathSum(root, 43), 2)

    def test_diamond_of_twos(self):
        root = build_tree([2, 2, 2, 2, 2, 2, 2])
        self.assertEqual(self.sol.pathSum(root, 2), 7)

    def test_deep_tree(self):
        vals = [1] * 10
        root = TreeNode(vals[0])
        cur = root
        for v in vals[1:]:
            cur.left = TreeNode(v)
            cur = cur.left
        self.assertEqual(self.sol.pathSum(root, 10), 1)

    def test_degenerate_left_only(self):
        root = build_tree([5, 3, None, 2])
        self.assertEqual(self.sol.pathSum(root, 10), 1)
        self.assertEqual(self.sol.pathSum(root, 8), 1)
        self.assertEqual(self.sol.pathSum(root, 5), 2)

    def test_degenerate_right_only(self):
        root = build_tree([5, None, 3, None, 2])
        self.assertEqual(self.sol.pathSum(root, 10), 1)

    def test_cross_subtree_not_allowed(self):
        root = build_tree([1, 2, 3])
        self.assertEqual(self.sol.pathSum(root, 4), 1)
        self.assertEqual(self.sol.pathSum(root, 5), 0)
        self.assertEqual(self.sol.pathSum(root, 3), 2)

    def test_mixed_negative_positive(self):
        root = build_tree([3, -1, 4, -2, 8])
        self.assertEqual(self.sol.pathSum(root, 10), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Binary Tree
