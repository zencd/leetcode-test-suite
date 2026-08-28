# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Easy

from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        raise Exception("Not solved yet")


def level_order(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def is_bst(
    node: Optional[TreeNode], lo: Optional[int] = None, hi: Optional[int] = None
) -> bool:
    if node is None:
        return True
    if lo is not None and node.val <= lo:
        return False
    if hi is not None and node.val >= hi:
        return False
    return is_bst(node.left, lo, node.val) and is_bst(node.right, node.val, hi)


def height(node: Optional[TreeNode]) -> int:
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def count_nodes(node: Optional[TreeNode]) -> int:
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_element(self):
        root = self.sol.sortedArrayToBST([1])
        self.assertIsNotNone(root)
        self.assertEqual(root.val, 1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_two_elements_left_root(self):
        root = self.sol.sortedArrayToBST([1, 3])
        self.assertIsNotNone(root)
        self.assertEqual(root.val, 3)
        self.assertIsNotNone(root.left)
        self.assertEqual(root.left.val, 1)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
        self.assertIsNone(root.right)

    def test_two_elements_right_root(self):
        root = self.sol.sortedArrayToBST([-2, -1])
        self.assertIsNotNone(root)
        self.assertEqual(root.val, -1)
        self.assertEqual(root.left.val, -2)
        self.assertIsNone(root.right)

    def test_example_1(self):
        root = self.sol.sortedArrayToBST([-10, -3, 0, 5, 9])
        self.assertEqual(level_order(root), [0, -3, 9, -10, None, 5])

    def test_example_2(self):
        root = self.sol.sortedArrayToBST([1, 3])
        self.assertEqual(level_order(root), [3, 1])

    def test_three_elements(self):
        root = self.sol.sortedArrayToBST([1, 2, 3])
        self.assertEqual(root.val, 2)
        self.assertEqual(root.left.val, 1)
        self.assertEqual(root.right.val, 3)

    def test_even_length_array(self):
        root = self.sol.sortedArrayToBST([1, 2, 3, 4])
        self.assertEqual(root.val, 3)
        self.assertEqual(level_order(root), [3, 2, 4, 1])

    def test_larger_sorted_array(self):
        nums = list(range(1, 11))
        root = self.sol.sortedArrayToBST(nums)
        self.assertEqual(level_order(root), [6, 3, 9, 2, 5, 8, 10, 1, None, 4, None, 7])
        self.assertTrue(is_bst(root))
        self.assertEqual(count_nodes(root), len(nums))

    def test_negative_values(self):
        root = self.sol.sortedArrayToBST([-4, -3, -2, -1])
        self.assertTrue(is_bst(root))
        self.assertEqual(count_nodes(root), 4)

    def test_all_same_sign_mixed(self):
        nums = [0, 1, 2]
        root = self.sol.sortedArrayToBST(nums)
        self.assertTrue(is_bst(root))
        self.assertEqual(root.val, 1)

    def test_produces_valid_bst(self):
        nums = [1, 3, 5, 7, 9, 12, 15, 20, 35, 100]
        root = self.sol.sortedArrayToBST(nums)
        self.assertTrue(is_bst(root))

    def test_height_balanced(self):
        nums = list(range(1, 16))
        root = self.sol.sortedArrayToBST(nums)
        self.assertEqual(abs(height(root) - height(root.left)), 1)
        self.assertEqual(abs(height(root) - height(root.right)), 1)
        self.assertEqual(height(root), 4)
        self.assertEqual(height(root.left), height(root.right))

    def test_inorder_traversal_restores_sorted_order(self):
        nums = [-15, -11, -7, -4, 0, 3, 8, 9]
        root = self.sol.sortedArrayToBST(nums)
        inorder = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        dfs(root)
        self.assertEqual(inorder, nums)

    def test_node_count_preserved(self):
        nums = [-5000, 0, 5000]
        root = self.sol.sortedArrayToBST(nums)
        self.assertEqual(count_nodes(root), 3)

    def test_large_array_balanced_and_valid(self):
        nums = list(range(-5000, 5001, 2))
        root = self.sol.sortedArrayToBST(nums)
        self.assertTrue(is_bst(root))
        self.assertEqual(count_nodes(root), len(nums))
        self.assertEqual(height(root), 13)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree
