# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
# Easy

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        raise Exception("Not solved yet")


def build_tree(values: Optional[List[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    i = 1
    q = deque([root])
    while q and i < len(values):
        cur = q.popleft()
        if values[i] is not None:
            cur.left = TreeNode(values[i])
            q.append(cur.left)
        i += 1
        if i < len(values) and values[i] is not None:
            cur.right = TreeNode(values[i])
            q.append(cur.right)
        i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> Optional[List[int]]:
    if root is None:
        return []
    result = []
    q = deque([root])
    while q:
        cur = q.popleft()
        if cur is None:
            result.append(None)
        else:
            result.append(cur.val)
            q.append(cur.left)
            q.append(cur.right)
    while result and result[-1] is None:
        result.pop()
    return result


def invert_reference(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    stack = [root]
    while stack:
        cur = stack.pop()
        cur.left, cur.right = cur.right, cur.left
        if cur.left is not None:
            stack.append(cur.left)
        if cur.right is not None:
            stack.append(cur.right)
    return root


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        root = None
        self.assertIsNone(self.solution.invertTree(root))

    def test_example_1(self):
        root = build_tree([4, 2, 7, 1, 3, 6, 9])
        self.solution.invertTree(root)
        self.assertEqual(tree_to_list(root), [4, 7, 2, 9, 6, 3, 1])

    def test_example_2(self):
        root = build_tree([2, 1, 3])
        self.solution.invertTree(root)
        self.assertEqual(tree_to_list(root), [2, 3, 1])

    def test_example_3(self):
        root = build_tree([])
        self.assertIsNone(self.solution.invertTree(root))

    def test_single_node(self):
        root = build_tree([1])
        result = self.solution.invertTree(root)
        self.assertEqual(tree_to_list(result), [1])

    def test_single_node_zero(self):
        root = build_tree([0])
        result = self.solution.invertTree(root)
        self.assertEqual(tree_to_list(result), [0])

    def test_single_node_negative(self):
        root = build_tree([-5])
        result = self.solution.invertTree(root)
        self.assertEqual(tree_to_list(result), [-5])

    def test_two_nodes_left_only(self):
        root = build_tree([1, 2])
        self.solution.invertTree(root)
        self.assertEqual(tree_to_list(root), [1, None, 2])

    def test_two_nodes_right_only(self):
        root = build_tree([1, None, 2])
        self.solution.invertTree(root)
        self.assertEqual(tree_to_list(root), [1, 2])

    def test_three_nodes(self):
        root = build_tree([3, 1, 2])
        self.solution.invertTree(root)
        self.assertEqual(tree_to_list(root), [3, 2, 1])

    def test_left_skewed_tree(self):
        root = build_tree([1, 2, None, 3])
        self.solution.invertTree(root)
        self.assertEqual(tree_to_list(root), [1, None, 2, None, 3])

    def test_right_skewed_tree(self):
        root = build_tree([1, None, 2, None, 3])
        self.solution.invertTree(root)
        self.assertEqual(tree_to_list(root), [1, 2, None, 3])

    def test_symmetric_tree(self):
        root = build_tree([1, 2, 2, 3, 4, 4, 3])
        self.solution.invertTree(root)
        self.assertEqual(tree_to_list(root), [1, 2, 2, 3, 4, 4, 3])

    def test_values_not_modified(self):
        root = build_tree([10, 20, 30, 40])
        original_values = []
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur is None:
                continue
            original_values.append(cur.val)
            q.append(cur.left)
            q.append(cur.right)
        self.solution.invertTree(root)
        new_values = []
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur is None:
                continue
            new_values.append(cur.val)
            q.append(cur.left)
            q.append(cur.right)
        self.assertEqual(sorted(new_values), sorted(original_values))

    def test_returns_same_root(self):
        root = build_tree([1, 2, 3])
        result = self.solution.invertTree(root)
        self.assertIs(result, root)

    def test_mirror_property(self):
        root_a = build_tree([4, 2, 7, 1, 3, 6, 9])
        root_b = build_tree([4, 7, 2, 9, 6, 3, 1])
        self.solution.invertTree(root_a)
        self.assertEqual(tree_to_list(root_a), tree_to_list(root_b))

    def test_invert_twice_restores_original(self):
        original = [4, 2, 7, 1, 3, 6, 9]
        root = build_tree(original)
        self.solution.invertTree(root)
        self.solution.invertTree(root)
        self.assertEqual(tree_to_list(root), original)

    def test_deep_tree(self):
        values = list(range(50))
        root_a = build_tree(values)
        root_b = build_tree(values)
        self.solution.invertTree(root_a)
        invert_reference(root_b)
        self.assertEqual(tree_to_list(root_a), tree_to_list(root_b))

    def test_full_binary_tree(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.solution.invertTree(root)
        self.assertEqual(tree_to_list(root), [1, 3, 2, 7, 6, 5, 4])

    def test_negative_values(self):
        root = build_tree([-1, -2, -3, -4, -5])
        self.solution.invertTree(root)
        self.assertEqual(tree_to_list(root), [-1, -3, -2, None, None, -5, -4])

    def test_mixed_values(self):
        root = build_tree([0, -5, 5, -10, 10])
        self.solution.invertTree(root)
        self.assertEqual(tree_to_list(root), [0, 5, -5, None, None, 10, -10])

    def test_node_structure_preserved(self):
        root = build_tree([1, 2, 3, 4, 5])
        self.solution.invertTree(root)
        self.assertIsNotNone(root)
        self.assertIsNotNone(root.left)
        self.assertIsNotNone(root.right)
        self.assertEqual(root.left.val, 3)
        self.assertEqual(root.right.val, 2)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
        self.assertEqual(root.right.left.val, 5)
        self.assertEqual(root.right.right.val, 4)


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
