# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/
# Easy

from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        raise Exception("Not solved yet")


def build_tree(values):
    if not values:
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


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_node(self):
        self.assertEqual(self.sol.binaryTreePaths(TreeNode(1)), ["1"])

    def test_example_1(self):
        root = build_tree([1, 2, 3, None, 5])
        self.assertEqual(self.sol.binaryTreePaths(root), ["1->2->5", "1->3"])

    def test_left_child_only(self):
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(self.sol.binaryTreePaths(root), ["1->2"])

    def test_right_child_only(self):
        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(self.sol.binaryTreePaths(root), ["1->2"])

    def test_two_children(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(self.sol.binaryTreePaths(root), ["1->2", "1->3"])

    def test_skewed_left(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(self.sol.binaryTreePaths(root), ["1->2->3"])

    def test_skewed_right(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(self.sol.binaryTreePaths(root), ["1->2->3"])

    def test_negative_values(self):
        root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        self.assertEqual(self.sol.binaryTreePaths(root), ["-1->-2", "-1->-3"])

    def test_zero_value(self):
        self.assertEqual(self.sol.binaryTreePaths(TreeNode(0)), ["0"])

    def test_full_binary_tree_depth_3(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        expected = ["1->2->4", "1->2->5", "1->3->6", "1->3->7"]
        self.assertEqual(sorted(self.sol.binaryTreePaths(root)), expected)

    def test_mixed_nulls(self):
        root = build_tree([1, 2, None, 4, 5])
        self.assertEqual(self.sol.binaryTreePaths(root), ["1->2->4", "1->2->5"])

    def test_order_in_dependence(self):
        root = build_tree([1, 7, None, 12, 5, 7])
        paths = self.sol.binaryTreePaths(root)
        self.assertEqual(sorted(paths), ["1->7->12", "1->7->5"])

    def test_large_negative_and_positive(self):
        root = TreeNode(-100, TreeNode(100), TreeNode(-100))
        self.assertEqual(self.sol.binaryTreePaths(root), ["-100->100", "-100->-100"])

    def test_returns_list_of_strings(self):
        result = self.sol.binaryTreePaths(TreeNode(1))
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(p, str) for p in result))


if __name__ == "__main__":
    unittest.main()

# Tags: String, Backtracking, Tree, Depth-First Search, Binary Tree
