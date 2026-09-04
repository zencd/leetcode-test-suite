# 109. Convert Sorted List to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Medium

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        raise Exception("Not solved yet")


def build_list(values):
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def level_order(root):
    if not root:
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


def is_valid_bst(node, lo=float("-inf"), hi=float("inf")):
    if not node:
        return True
    if node.val <= lo or node.val >= hi:
        return False
    return is_valid_bst(node.left, lo, node.val) and is_valid_bst(node.right, node.val, hi)


def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))


def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def is_balanced(node):
    def bh(n):
        if not n:
            return 0
        lh = bh(n.left)
        if lh == -1:
            return -1
        rh = bh(n.right)
        if rh == -1:
            return -1
        if abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)

    return bh(node) != -1


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_list(self):
        self.assertIsNone(self.sol.sortedListToBST(None))

    def test_example_2(self):
        self.assertIsNone(self.sol.sortedListToBST(None))

    def test_single_node(self):
        head = build_list([5])
        root = self.sol.sortedListToBST(head)
        self.assertIsInstance(root, TreeNode)
        self.assertEqual(root.val, 5)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_two_nodes(self):
        head = build_list([1, 2])
        root = self.sol.sortedListToBST(head)
        self.assertTrue(is_valid_bst(root))
        self.assertEqual(inorder(root), [1, 2])
        self.assertTrue(is_balanced(root))

    def test_three_nodes(self):
        head = build_list([1, 2, 3])
        root = self.sol.sortedListToBST(head)
        self.assertEqual(level_order(root), [2, 1, 3])
        self.assertEqual(root.val, 2)
        self.assertTrue(is_valid_bst(root))

    def test_example_1(self):
        head = build_list([-10, -3, 0, 5, 9])
        root = self.sol.sortedListToBST(head)
        self.assertTrue(is_valid_bst(root))
        self.assertEqual(inorder(root), [-10, -3, 0, 5, 9])
        self.assertTrue(is_balanced(root))
        self.assertEqual(root.val, 0)

    def test_four_nodes(self):
        head = build_list([1, 2, 3, 4])
        root = self.sol.sortedListToBST(head)
        self.assertTrue(is_valid_bst(root))
        self.assertEqual(inorder(root), [1, 2, 3, 4])
        self.assertTrue(is_balanced(root))

    def test_five_nodes_root_is_middle(self):
        head = build_list([1, 2, 3, 4, 5])
        root = self.sol.sortedListToBST(head)
        self.assertEqual(root.val, 3)
        self.assertTrue(is_valid_bst(root))
        self.assertTrue(is_balanced(root))
        self.assertEqual(inorder(root), [1, 2, 3, 4, 5])

    def test_six_nodes(self):
        head = build_list([1, 2, 3, 4, 5, 6])
        root = self.sol.sortedListToBST(head)
        self.assertTrue(is_valid_bst(root))
        self.assertTrue(is_balanced(root))
        self.assertEqual(level_order(root), [4, 2, 6, 1, 3, 5])

    def test_seven_nodes(self):
        head = build_list([1, 2, 3, 4, 5, 6, 7])
        root = self.sol.sortedListToBST(head)
        self.assertEqual(root.val, 4)
        self.assertTrue(is_valid_bst(root))
        self.assertTrue(is_balanced(root))

    def test_negative_values(self):
        head = build_list([-5, -3, -1])
        root = self.sol.sortedListToBST(head)
        self.assertTrue(is_valid_bst(root))
        self.assertEqual(inorder(root), [-5, -3, -1])

    def test_zero_in_list(self):
        head = build_list([-1, 0, 1])
        root = self.sol.sortedListToBST(head)
        self.assertEqual(root.val, 0)
        self.assertTrue(is_valid_bst(root))

    def test_boundary_values(self):
        head = build_list([-100000, 0, 100000])
        root = self.sol.sortedListToBST(head)
        self.assertEqual(inorder(root), [-100000, 0, 100000])
        self.assertTrue(is_valid_bst(root))
        self.assertTrue(is_balanced(root))

    def test_duplicate_values(self):
        head = build_list([7, 7, 7])
        root = self.sol.sortedListToBST(head)
        self.assertEqual(inorder(root), [7, 7, 7])
        self.assertEqual(count_nodes(root), 3)

    def test_height_perfect_15(self):
        head = build_list(list(range(15)))
        root = self.sol.sortedListToBST(head)
        self.assertEqual(height(root), 4)
        self.assertTrue(is_balanced(root))
        self.assertTrue(is_valid_bst(root))

    def test_height_perfect_31(self):
        head = build_list(list(range(31)))
        root = self.sol.sortedListToBST(head)
        self.assertEqual(height(root), 5)
        self.assertTrue(is_balanced(root))

    def test_node_count_preserved_many_sizes(self):
        import sys

        sys.setrecursionlimit(10000)
        for n in (1, 2, 3, 4, 5, 6, 7, 8, 16, 32, 63, 100, 127):
            head = build_list(list(range(n)))
            root = self.sol.sortedListToBST(head)
            self.assertEqual(count_nodes(root), n, "n=%d" % n)
            self.assertTrue(is_balanced(root), "n=%d not balanced" % n)
            self.assertEqual(inorder(root), list(range(n)), "n=%d" % n)

    def test_many_nodes_1024(self):
        import sys

        sys.setrecursionlimit(10000)
        values = list(range(1024))
        head = build_list(values)
        root = self.sol.sortedListToBST(head)
        self.assertTrue(is_valid_bst(root))
        self.assertEqual(count_nodes(root), 1024)
        self.assertTrue(is_balanced(root))
        self.assertEqual(height(root), 11)
        self.assertEqual(inorder(root), values)

    def test_returns_tree_nodes(self):
        head = build_list([1, 2, 3])
        root = self.sol.sortedListToBST(head)
        self.assertIsInstance(root, TreeNode)
        self.assertIsInstance(root.left, TreeNode)
        self.assertIsInstance(root.right, TreeNode)


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Divide and Conquer, Tree, Binary Search Tree, Binary Tree
