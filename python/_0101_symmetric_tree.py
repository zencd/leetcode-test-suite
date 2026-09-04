# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
# Easy

import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
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


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        raise Exception("Not solved yet")

    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_single_node(self):
        self.assertTrue(self.s.isSymmetric(build_tree([1])))

    def test_symmetric(self):
        self.assertTrue(self.s.isSymmetric(build_tree([1, 2, 2, 3, 4, 4, 3])))

    def test_not_symmetric_example_2(self):
        self.assertFalse(self.s.isSymmetric(build_tree([1, 2, 2, None, 3, None, 3])))

    def test_not_symmetric_leaf_mismatch(self):
        self.assertFalse(self.s.isSymmetric(build_tree([1, 2, 2, 3, 4, 3, 4])))

    def test_not_symmetric_values_equal_structure_different(self):
        self.assertFalse(self.s.isSymmetric(build_tree([1, 2, 2, 3, None, None, 4])))

    def test_two_levels_one_side_only(self):
        self.assertFalse(self.s.isSymmetric(build_tree([1, None, 2])))
        self.assertFalse(self.s.isSymmetric(build_tree([1, 2, None])))

    def test_symmetric_two_levels(self):
        self.assertTrue(self.s.isSymmetric(build_tree([1, 2, 2])))

    def test_symmetric_three_levels(self):
        self.assertTrue(self.s.isSymmetric(build_tree([1, 2, 2, 3, 4, 4, 3])))

    def test_symmetric_deeper(self):
        self.assertTrue(
            self.s.isSymmetric(
                build_tree([1, 2, 2, 3, 4, 4, 3, None, None, 5, 6, 6, 5])
            )
        )

    def test_skewed_left_not_symmetric(self):
        self.assertFalse(self.s.isSymmetric(build_tree([1, 2, None, 3, None, 4])))

    def test_skewed_right_not_symmetric(self):
        self.assertFalse(self.s.isSymmetric(build_tree([1, None, 2, None, 3, None, 4])))

    def test_negative_values_symmetric(self):
        self.assertTrue(
            self.s.isSymmetric(build_tree([0, -100, -100, 100, -50, -50, 100]))
        )

    def test_boundary_values(self):
        self.assertTrue(
            self.s.isSymmetric(build_tree([100, -100, -100, -100, 100, 100, -100]))
        )

    def test_null_children_symmetric(self):
        self.assertTrue(self.s.isSymmetric(build_tree([1, 2, 2, None, 3, 3, None])))

    def test_both_children_null(self):
        self.assertTrue(self.s.isSymmetric(build_tree([1, None, None])))

    def test_deep_chain_not_symmetric(self):
        root = TreeNode(1)
        cur = root
        for i in range(2, 1001):
            cur.right = TreeNode(i)
            cur = cur.right
        self.assertFalse(self.s.isSymmetric(root))

    def test_deep_symmetric_not(self):
        left = TreeNode(1, TreeNode(2, TreeNode(3)), None)
        right = TreeNode(1, None, TreeNode(2))
        self.assertFalse(self.s.isSymmetric(TreeNode(0, left, right)))


class TestSolutionIterative(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_single_node(self):
        self.assertTrue(self.s.isSymmetricIterative(build_tree([1])))

    def test_symmetric(self):
        self.assertTrue(self.s.isSymmetricIterative(build_tree([1, 2, 2, 3, 4, 4, 3])))

    def test_not_symmetric_example_2(self):
        self.assertFalse(
            self.s.isSymmetricIterative(build_tree([1, 2, 2, None, 3, None, 3]))
        )

    def test_not_symmetric_leaf_mismatch(self):
        self.assertFalse(self.s.isSymmetricIterative(build_tree([1, 2, 2, 3, 4, 3, 4])))

    def test_one_side_child_only(self):
        self.assertFalse(self.s.isSymmetricIterative(build_tree([1, None, 2])))
        self.assertFalse(self.s.isSymmetricIterative(build_tree([1, 2, None])))

    def test_symmetric_two_levels(self):
        self.assertTrue(self.s.isSymmetricIterative(build_tree([1, 2, 2])))

    def test_null_children_symmetric(self):
        self.assertTrue(
            self.s.isSymmetricIterative(build_tree([1, 2, 2, None, 3, 3, None]))
        )

    def test_negative_values_symmetric(self):
        self.assertTrue(
            self.s.isSymmetricIterative(build_tree([0, -100, -100, 100, -50, -50, 100]))
        )

    def test_deep_chain_not_symmetric(self):
        root = TreeNode(1)
        cur = root
        for i in range(2, 1001):
            cur.right = TreeNode(i)
            cur = cur.right
        self.assertFalse(self.s.isSymmetricIterative(root))

    def test_skewed_left_not_symmetric(self):
        self.assertFalse(
            self.s.isSymmetricIterative(build_tree([1, 2, None, 3, None, 4]))
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
