# 99. Recover Binary Search Tree
# https://leetcode.com/problems/recover-binary-search-tree/
# Medium

import collections
import unittest
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        raise Exception("Not solved yet")


def build_tree(values) -> Optional[TreeNode]:
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    root = nodes[0]
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        if i < len(nodes) and nodes[i] is not None:
            node.left = nodes[i]
            queue.append(nodes[i])
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = nodes[i]
            queue.append(nodes[i])
        i += 1
    return root


def to_list(root: Optional[TreeNode]) -> Optional[List[Optional[int]]]:
    if root is None:
        return None
    result = []
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def is_bst(node, lo=float("-inf"), hi=float("inf")) -> bool:
    if node is None:
        return True
    if not (lo < node.val < hi):
        return False
    return is_bst(node.left, lo, node.val) and is_bst(node.right, node.val, hi)


def inorder_values(node, acc=None):
    if acc is None:
        acc = []
    if node is not None:
        inorder_values(node.left, acc)
        acc.append(node.val)
        inorder_values(node.right, acc)
    return acc


def build_balanced(vals) -> Optional[TreeNode]:
    if not vals:
        return None
    mid = len(vals) // 2
    return TreeNode(
        vals[mid], build_balanced(vals[:mid]), build_balanced(vals[mid + 1 :])
    )


def find_node(root, val) -> Optional[TreeNode]:
    if root is None:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left is not None:
        return left
    return find_node(root.right, val)


class TestRecoverTree(unittest.TestCase):
    def run_and_check(self, broken, expected):
        self.assertFalse(is_bst(build_tree(broken)))
        root = build_tree(broken)
        Solution().recoverTree(root)
        self.assertEqual(to_list(root), expected)
        self.assertTrue(is_bst(root))

    def run_swap(self, base_vals, a, b):
        root = build_balanced(base_vals)
        self.assertTrue(is_bst(root))
        snapshot = to_list(root)
        na = find_node(root, a)
        nb = find_node(root, b)
        self.assertIsNotNone(na)
        self.assertIsNotNone(nb)
        na.val, nb.val = nb.val, na.val
        self.assertFalse(is_bst(root))
        Solution().recoverTree(root)
        self.assertEqual(to_list(root), snapshot)
        self.assertTrue(is_bst(root))

    def test_example_1(self):
        self.run_and_check([1, 3, None, None, 2], [3, 1, None, None, 2])

    def test_example_2(self):
        self.run_and_check([3, 1, 4, None, None, 2], [2, 1, 4, None, None, 3])

    def test_two_nodes_swapped(self):
        self.run_and_check([1, 3], [3, 1])

    def test_root_and_right_child_swapped(self):
        self.run_and_check([3, None, 1], [1, None, 3])

    def test_extreme_root_and_right(self):
        low = -(2**31)
        high = 2**31 - 1
        self.run_and_check([high, None, low], [low, None, high])

    def test_left_skewed_tree(self):
        self.run_and_check([4, 2, None, 3, None, 1], [4, 3, None, 2, None, 1])

    def test_right_skewed_tree(self):
        self.run_and_check([3, None, 2, None, 1], [1, None, 2, None, 3])

    def test_adjacent_values_in_inorder(self):
        vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.run_swap(vals, 3, 4)

    def test_distant_values_in_inorder(self):
        vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.run_swap(vals, 1, 15)

    def test_root_swapped_with_leaf(self):
        vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.run_swap(vals, 8, 14)

    def test_root_swapped_with_leftmost_leaf(self):
        vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.run_swap(vals, 8, 1)

    def test_all_negative_values(self):
        vals = list(range(-15, 0))
        self.run_swap(vals, -8, -2)

    def test_extreme_values(self):
        vals = [-(2**31), -1, 0, 1, 2**31 - 1]
        self.run_swap(vals, -(2**31), 2**31 - 1)

    def test_valid_tree_stays_unchanged(self):
        root = build_tree([5, 3, 8, 1, 4, 6, 9])
        before = to_list(root)
        Solution().recoverTree(root)
        self.assertEqual(to_list(root), before)

    def test_structure_not_changed(self):
        root = build_tree([1, 3, None, None, 2])
        left = root.left
        root_right = root.right
        left2 = left.right
        Solution().recoverTree(root)
        self.assertIs(root.left, left)
        self.assertIs(root.right, root_right)
        self.assertIs(left.right, left2)

    def test_inorder_values_preserved(self):
        root = build_tree([3, 1, 4, None, None, 2])
        before = inorder_values(root)
        Solution().recoverTree(root)
        self.assertEqual(sorted(inorder_values(root)), sorted(before))

    def test_large_tree_random_swap(self):
        vals = list(range(1, 300))
        root = build_balanced(vals)
        snapshot = to_list(root)
        self.assertTrue(is_bst(root))
        a = 37
        b = 251
        na = find_node(root, a)
        nb = find_node(root, b)
        na.val, nb.val = nb.val, na.val
        self.assertFalse(is_bst(root))
        Solution().recoverTree(root)
        self.assertEqual(to_list(root), snapshot)
        self.assertTrue(is_bst(root))
        self.assertEqual(inorder_values(root), vals)


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree
