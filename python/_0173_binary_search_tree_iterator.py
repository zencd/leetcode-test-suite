# 173. Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/
# Medium

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        raise Exception("Not solved yet")

    def next(self) -> int:
        raise Exception("Not solved yet")

    def hasNext(self) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_single_node(self):
        it = BSTIterator(TreeNode(5))
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 5)
        self.assertFalse(it.hasNext())

    def test_example_tree(self):
        root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
        it = BSTIterator(root)
        self.assertEqual(it.next(), 3)
        self.assertEqual(it.next(), 7)
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 9)
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 15)
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 20)
        self.assertFalse(it.hasNext())

    def test_all_sorted(self):
        root = TreeNode(
            8,
            TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
            TreeNode(10, TreeNode(9), TreeNode(14, None, TreeNode(15))),
        )
        it = BSTIterator(root)
        expected = [1, 3, 4, 6, 7, 8, 9, 10, 14, 15]
        out = []
        while it.hasNext():
            out.append(it.next())
        self.assertEqual(out, expected)

    def test_left_skewed(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1)))
        it = BSTIterator(root)
        self.assertEqual([it.next() for _ in range(3)], [1, 2, 4])
        self.assertFalse(it.hasNext())

    def test_right_skewed(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        it = BSTIterator(root)
        self.assertEqual([it.next() for _ in range(3)], [1, 2, 3])
        self.assertFalse(it.hasNext())

    def test_interleaving_next_and_hasnext(self):
        root = TreeNode(
            7,
            TreeNode(3, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(6))),
            TreeNode(15, TreeNode(9), TreeNode(20)),
        )
        it = BSTIterator(root)
        calls = ["next", "hasNext", "next", "hasNext", "next", "hasNext"]
        expected = [2, True, 3, True, 4, True]
        result = []
        for i, call in enumerate(calls):
            if call == "next":
                result.append(it.next())
            else:
                self.assertEqual(it.hasNext(), expected[i])
        self.assertEqual(result, [2, 3, 4])

    def test_hasnext_before_any_next(self):
        root = TreeNode(5, TreeNode(3), TreeNode(8))
        it = BSTIterator(root)
        self.assertTrue(it.hasNext())

    def test_zero_value_node(self):
        it = BSTIterator(TreeNode(0))
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 0)
        self.assertFalse(it.hasNext())

    def test_two_nodes(self):
        it = BSTIterator(TreeNode(2, TreeNode(1)))
        self.assertEqual(it.next(), 1)
        self.assertEqual(it.next(), 2)
        self.assertFalse(it.hasNext())

    def test_two_nodes_right_child(self):
        it = BSTIterator(TreeNode(1, None, TreeNode(2)))
        self.assertEqual(it.next(), 1)
        self.assertEqual(it.next(), 2)
        self.assertFalse(it.hasNext())

    def test_full_binary_tree_depth3(self):
        root = TreeNode(
            7,
            TreeNode(3, TreeNode(1), TreeNode(5, TreeNode(4), TreeNode(6))),
            TreeNode(15, TreeNode(9), TreeNode(25, TreeNode(20), TreeNode(30))),
        )
        it = BSTIterator(root)
        expected = [1, 3, 4, 5, 6, 7, 9, 15, 20, 25, 30]
        out = []
        while it.hasNext():
            out.append(it.next())
        self.assertEqual(out, expected)

    def test_large_tree_inorder(self):
        nodes = []

        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(mid)
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            nodes.append(node)
            return node

        root = build(0, 1022)
        it = BSTIterator(root)
        out = [it.next() for _ in range(len(nodes))]
        self.assertEqual(out, list(range(1023)))
        self.assertFalse(it.hasNext())

    def test_max_node_value(self):
        it = BSTIterator(TreeNode(10**6, None, None))
        self.assertEqual(it.next(), 10**6)

    def test_sequential_exhaustion(self):
        root = TreeNode(5, TreeNode(3), TreeNode(8))
        it = BSTIterator(root)
        self.assertEqual(it.next(), 3)
        self.assertEqual(it.next(), 5)
        self.assertEqual(it.next(), 8)
        self.assertFalse(it.hasNext())


if __name__ == "__main__":
    unittest.main()

# Tags: Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator
