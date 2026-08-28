# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Medium

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_single_node_zero(self):
        root = TreeNode(0)
        self.assertEqual(Solution().sumNumbers(root), 0)

    def test_single_node_digit(self):
        root = TreeNode(5)
        self.assertEqual(Solution().sumNumbers(root), 5)

    def test_example_1(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(Solution().sumNumbers(root), 25)

    def test_example_2(self):
        root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
        self.assertEqual(Solution().sumNumbers(root), 1026)

    def test_all_zeros(self):
        root = TreeNode(0, TreeNode(0), TreeNode(0))
        self.assertEqual(Solution().sumNumbers(root), 0)

    def test_left_only(self):
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(Solution().sumNumbers(root), 12)

    def test_right_only(self):
        root = TreeNode(1, None, TreeNode(3))
        self.assertEqual(Solution().sumNumbers(root), 13)

    def test_left_skew(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(Solution().sumNumbers(root), 123)

    def test_right_skew(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(Solution().sumNumbers(root), 123)

    def test_deep_chain(self):
        root = TreeNode(1)
        node = root
        for val in (2, 3, 4, 5, 6, 7, 8, 9):
            node.left = TreeNode(val)
            node = node.left
        self.assertEqual(Solution().sumNumbers(root), 123456789)

    def test_full_tree(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )
        self.assertEqual(Solution().sumNumbers(root), 522)

    def test_zero_internal(self):
        root = TreeNode(1, TreeNode(0, TreeNode(1), TreeNode(2)), TreeNode(3))
        self.assertEqual(Solution().sumNumbers(root), 101 + 102 + 13)

    def test_unbalanced(self):
        root = TreeNode(0, TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(9))
        self.assertEqual(Solution().sumNumbers(root), 12 + 13 + 9)


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Binary Tree
