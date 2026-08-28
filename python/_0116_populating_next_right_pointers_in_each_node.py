# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Medium

from typing import List, Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        raise Exception("Not solved yet")


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        raise Exception("Not solved yet")


def build_tree(values: List[int]) -> Optional[Node]:
    if not values:
        return None
    nodes = [Node(v) for v in values]
    for i, node in enumerate(nodes):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < len(nodes):
            node.left = nodes[left_idx]
        if right_idx < len(nodes):
            node.right = nodes[right_idx]
    return nodes[0]


def levels_with_next(root: Optional[Node]) -> List[List[int]]:
    if root is None:
        return []
    levels = []
    level_head = root
    while level_head:
        level = []
        node = level_head
        while node:
            level.append(node.val)
            node = node.next
        levels.append(level)
        level_head = level_head.left if level_head.left else None
    return levels


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_tree(self):
        self.assertIsNone(self.sol.connect(None))

    def test_single_node(self):
        root = Node(1)
        result = self.sol.connect(root)
        self.assertIs(result, root)
        self.assertIsNone(result.next)

    def test_two_levels(self):
        root = build_tree([1, 2, 3])
        self.sol.connect(root)
        self.assertIs(root.left.next, root.right)
        self.assertIs(root.right.next, None)
        self.assertIsNone(root.next)

    def test_three_levels_example(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.sol.connect(root)
        expected = [[1], [2, 3], [4, 5, 6, 7]]
        self.assertEqual(levels_with_next(root), expected)

    def test_four_levels(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.sol.connect(root)
        expected = [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15]]
        self.assertEqual(levels_with_next(root), expected)

    def test_max_level_count(self):
        n_levels = 12
        n_nodes = 2**n_levels - 1
        values = list(range(1, n_nodes + 1))
        root = build_tree(values)
        self.sol.connect(root)
        levels = levels_with_next(root)
        self.assertEqual(len(levels), n_levels)
        for i, level in enumerate(levels):
            self.assertEqual(len(level), 2**i)
            start = (2**i) - 1
            self.assertEqual(level, values[start : start + (2**i)])

    def test_negative_values(self):
        root = build_tree([-5, -1000, 1000, -1, 0, 1, -1000])
        self.sol.connect(root)
        expected = [[-5], [-1000, 1000], [-1, 0, 1, -1000]]
        self.assertEqual(levels_with_next(root), expected)

    def test_extreme_values(self):
        root = build_tree([-1000, 1000, -1000])
        self.sol.connect(root)
        self.assertIs(root.left.next, root.right)

    def test_duplicates_values(self):
        root = build_tree([7, 7, 7, 7, 7, 7, 7])
        self.sol.connect(root)
        self.assertIs(root.left.left.next, root.left.right)
        self.assertIs(root.left.right.next, root.right.left)
        self.assertIs(root.right.left.next, root.right.right)
        self.assertIsNone(root.right.right.next)

    def test_original_nodes_preserved(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.sol.connect(root)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.left.left.val, 4)
        self.assertEqual(root.left.right.val, 5)
        self.assertEqual(root.right.left.val, 6)
        self.assertEqual(root.right.right.val, 7)

    def test_idempotent(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.sol.connect(root)
        first = levels_with_next(root)
        self.sol.connect(root)
        self.assertEqual(levels_with_next(root), first)

    def test_returns_root(self):
        root = Node(1)
        self.assertIs(self.sol.connect(root), root)


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree
