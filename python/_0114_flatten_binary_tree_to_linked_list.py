# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Medium

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        raise Exception("Not solved yet")


def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    root = nodes[0]
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        node = queue.pop(0)
        if i < len(nodes):
            node.left = nodes[i]
            if nodes[i] is not None:
                queue.append(nodes[i])
            i += 1
        if i < len(nodes):
            node.right = nodes[i]
            if nodes[i] is not None:
                queue.append(nodes[i])
            i += 1
    return root


def to_list(root):
    result = []
    node = root
    while node:
        result.append(node.val)
        if node.left is not None:
            raise AssertionError("left child is not None")
        node = node.right
    return result


def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_tree(self):
        self.sol.flatten(None)
        self.assertIsNone(None)

    def test_single_node(self):
        root = build_tree([0])
        self.sol.flatten(root)
        self.assertEqual(to_list(root), [0])

    def test_example1(self):
        root = build_tree([1, 2, 5, 3, 4, None, 6])
        self.sol.flatten(root)
        self.assertEqual(to_list(root), [1, 2, 3, 4, 5, 6])

    def test_right_spine_only(self):
        root = build_tree([1, None, 2, None, 3])
        self.sol.flatten(root)
        self.assertEqual(to_list(root), [1, 2, 3])

    def test_left_spine_only(self):
        root = build_tree([3, 2, None, 1])
        self.sol.flatten(root)
        self.assertEqual(to_list(root), [3, 2, 1])

    def test_two_children_of_root(self):
        root = build_tree([1, 2, 3])
        self.sol.flatten(root)
        self.assertEqual(to_list(root), [1, 2, 3])

    def test_left_subtree_chain(self):
        root = build_tree([4, 2, 6, None, 1, None, 3])
        self.sol.flatten(root)
        self.assertEqual(to_list(root), [4, 2, 1, 6, 3])

    def test_full_binary_tree(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.sol.flatten(root)
        self.assertEqual(to_list(root), [1, 2, 4, 5, 3, 6, 7])

    def test_perfect_tree_15(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.sol.flatten(root)
        self.assertEqual(
            to_list(root), [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]
        )

    def test_negative_values(self):
        root = build_tree([-1, -2, -3, -4])
        self.sol.flatten(root)
        self.assertEqual(to_list(root), [-1, -2, -4, -3])

    def test_zero_valued_nodes(self):
        root = build_tree([0, 0, 0, 0, 0])
        self.sol.flatten(root)
        self.assertEqual(to_list(root), [0, 0, 0, 0, 0])

    def test_extreme_values(self):
        root = build_tree([-100, 100])
        self.sol.flatten(root)
        self.assertEqual(to_list(root), [-100, 100])

    def test_duplicate_values_preserved(self):
        root = build_tree([5, 5, 5, 5, 5, 5, 5])
        self.sol.flatten(root)
        self.assertEqual(to_list(root), [5, 5, 5, 5, 5, 5, 5])

    def test_flatten_matches_preorder_random_shape(self):
        trees = [
            [1, None, 2, 3, None, 4, None, 5],
            [1, 2, None, 3, 4, None, 5],
            [1, None, 2, None, 3, None, 4, 5],
        ]
        for values in trees:
            root = build_tree(values)
            expected = preorder(root)
            self.sol.flatten(root)
            self.assertEqual(to_list(root), expected)

    def test_modified_in_place_return_none(self):
        root = build_tree([1, 2, 3])
        result = self.sol.flatten(root)
        self.assertIsNone(result)

    def test_left_pointers_cleared(self):
        root = build_tree([1, 2, 5, 3, 4, None, 6])
        self.sol.flatten(root)
        node = root
        while node:
            self.assertIsNone(node.left)
            node = node.right


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Stack, Tree, Depth-First Search, Binary Tree
