# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/
# Easy

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        raise Exception("Not solved yet")


import unittest


def make_tree(values):
    if not values:
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


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_tree(self):
        self.assertTrue(self.sol.isBalanced(None))

    def test_single_node(self):
        self.assertTrue(self.sol.isBalanced(make_tree([1])))

    def test_two_nodes_left(self):
        self.assertTrue(self.sol.isBalanced(make_tree([1, 2])))

    def test_two_nodes_right(self):
        self.assertTrue(self.sol.isBalanced(make_tree([1, None, 2])))

    def test_balanced_three_nodes(self):
        self.assertTrue(self.sol.isBalanced(make_tree([1, 2, 3])))

    def test_example1(self):
        self.assertTrue(self.sol.isBalanced(make_tree([3, 9, 20, None, None, 15, 7])))

    def test_example2(self):
        self.assertFalse(
            self.sol.isBalanced(make_tree([1, 2, 2, 3, 3, None, None, 4, 4]))
        )

    def test_example3(self):
        self.assertTrue(self.sol.isBalanced(make_tree([])))

    def test_chain_of_three(self):
        self.assertFalse(self.sol.isBalanced(make_tree([1, 2, None, 3])))

    def test_right_heavy(self):
        self.assertFalse(self.sol.isBalanced(make_tree([1, None, 2, None, None, 3])))

    def test_balance_violation_in_subtree(self):
        tree = TreeNode(1)
        tree.left = TreeNode(2)
        tree.right = TreeNode(3)
        tree.right.left = TreeNode(4)
        tree.right.left.left = TreeNode(5)
        self.assertFalse(self.sol.isBalanced(tree))

    def test_deep_balanced(self):
        def build(d):
            if d == 0:
                return TreeNode(0)
            return TreeNode(0, build(d - 1), build(d - 1))

        self.assertTrue(self.sol.isBalanced(build(5)))

    def test_deep_unbalanced(self):
        node = TreeNode(0)
        current = node
        for v in range(1, 6):
            current.left = TreeNode(v)
            current = current.left
        self.assertFalse(self.sol.isBalanced(node))

    def test_all_left_chain_four(self):
        self.assertFalse(self.sol.isBalanced(make_tree([1, 2, None, 3, None, None, 4])))

    def test_mirror_of_example2(self):
        self.assertFalse(
            self.sol.isBalanced(make_tree([1, 2, 2, 3, 3, None, None, 4, 4]))
        )

    def test_symmetric_balanced(self):
        self.assertTrue(self.sol.isBalanced(make_tree([1, 2, 2, 3, 3, 3, 3])))

    def test_large_skewed_tree(self):
        root = TreeNode(0)
        current = root
        for v in range(1, 5000):
            current.left = TreeNode(v)
            current = current.left
        self.assertFalse(self.sol.isBalanced(root))


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Binary Tree
