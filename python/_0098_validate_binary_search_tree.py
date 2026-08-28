# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Medium

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        raise Exception("Not solved yet")


import unittest


def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_simple_valid(self):
        self.assertTrue(self.sol.isValidBST(build_tree([2, 1, 3])))

    def test_simple_invalid(self):
        self.assertFalse(self.sol.isValidBST(build_tree([5, 1, 4, None, None, 3, 6])))

    def test_single_node(self):
        self.assertTrue(self.sol.isValidBST(build_tree([1])))

    def test_two_nodes_valid(self):
        self.assertTrue(self.sol.isValidBST(build_tree([2, 1])))
        self.assertTrue(self.sol.isValidBST(build_tree([1, None, 2])))

    def test_two_nodes_invalid(self):
        self.assertFalse(self.sol.isValidBST(build_tree([1, 2])))
        self.assertFalse(self.sol.isValidBST(build_tree([2, None, 1])))

    def test_equal_values_invalid(self):
        self.assertFalse(self.sol.isValidBST(build_tree([2, 2, 3])))
        self.assertFalse(self.sol.isValidBST(build_tree([2, 1, 2])))
        self.assertFalse(self.sol.isValidBST(build_tree([1, None, 1])))

    def test_deep_valid_chain(self):
        root = TreeNode(10, TreeNode(5, TreeNode(2)), None)
        root.right = TreeNode(15, None, TreeNode(20))
        self.assertTrue(self.sol.isValidBST(root))

    def test_deep_invalid_chain(self):
        root = TreeNode(10, TreeNode(5, None, TreeNode(7)), None)
        root.right = TreeNode(15, TreeNode(6), TreeNode(20))
        self.assertFalse(self.sol.isValidBST(root))

    def test_large_valid_tree(self):
        root = TreeNode(50)
        root.left = TreeNode(30)
        root.left.left = TreeNode(20)
        root.left.right = TreeNode(40)
        root.left.left.left = TreeNode(10)
        root.left.left.right = TreeNode(25)
        root.left.right.left = TreeNode(35)
        root.left.right.right = TreeNode(45)
        root.right = TreeNode(70)
        root.right.left = TreeNode(60)
        root.right.right = TreeNode(80)
        self.assertTrue(self.sol.isValidBST(root))

    def test_violation_in_left_subtree(self):
        root = TreeNode(50)
        root.left = TreeNode(30)
        root.left.left = TreeNode(20)
        root.left.right = TreeNode(40)
        root.left.right.left = TreeNode(45)
        root.right = TreeNode(70)
        self.assertFalse(self.sol.isValidBST(root))

    def test_violation_in_right_subtree(self):
        root = TreeNode(50)
        root.right = TreeNode(70)
        root.right.left = TreeNode(80)
        self.assertFalse(self.sol.isValidBST(root))

    def test_negative_values(self):
        root = TreeNode(0)
        root.left = TreeNode(-10, TreeNode(-20), TreeNode(-5))
        root.right = TreeNode(10)
        self.assertTrue(self.sol.isValidBST(root))

    def test_all_negative_valid(self):
        root = TreeNode(-2)
        root.left = TreeNode(-10)
        root.right = TreeNode(-1)
        self.assertTrue(self.sol.isValidBST(root))

    def test_all_negative_invalid(self):
        root = TreeNode(-2)
        root.left = TreeNode(-1)
        self.assertFalse(self.sol.isValidBST(root))

    def test_extreme_values(self):
        root = TreeNode(0, TreeNode(-(2**31)), TreeNode(2**31 - 1))
        self.assertTrue(self.sol.isValidBST(root))

    def test_extreme_values_invalid(self):
        root = TreeNode(2**31 - 1, TreeNode(2**31 - 2), TreeNode(2**31 - 2))
        self.assertFalse(self.sol.isValidBST(root))

    def test_skewed_left_valid(self):
        root = TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1))))
        self.assertTrue(self.sol.isValidBST(root))

    def test_skewed_right_valid(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        self.assertTrue(self.sol.isValidBST(root))

    def test_skewed_invalid(self):
        root = TreeNode(4, TreeNode(3, None, TreeNode(2)))
        self.assertFalse(self.sol.isValidBST(root))

    def test_leaf_violation(self):
        root = TreeNode(5, TreeNode(3), TreeNode(6, TreeNode(1), TreeNode(7)))
        self.assertFalse(self.sol.isValidBST(root))

    def test_in_order_boundary_values(self):
        root = TreeNode(
            4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(6))
        )
        self.assertTrue(self.sol.isValidBST(root))

    def test_duplicate_deep(self):
        root = TreeNode(4, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(6)))
        self.assertFalse(self.sol.isValidBST(root))


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree
