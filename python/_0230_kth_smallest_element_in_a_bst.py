# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Medium

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        raise Exception("Not solved yet")


def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    root = nodes[0]
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if i < len(nodes):
            current.left = nodes[i]
            if nodes[i] is not None:
                queue.append(nodes[i])
            i += 1
        if i < len(nodes):
            current.right = nodes[i]
            if nodes[i] is not None:
                queue.append(nodes[i])
            i += 1
    return root


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        root = build_tree([3, 1, 4, None, 2])
        self.assertEqual(self.solution.kthSmallest(root, 1), 1)

    def test_example_two(self):
        root = build_tree([5, 3, 6, 2, 4, None, None, 1])
        self.assertEqual(self.solution.kthSmallest(root, 3), 3)

    def test_single_node(self):
        root = build_tree([42])
        self.assertEqual(self.solution.kthSmallest(root, 1), 42)

    def test_left_skewed_tree(self):
        root = build_tree([4, 3, None, 2, None, 1])
        self.assertEqual(self.solution.kthSmallest(root, 1), 1)
        self.assertEqual(self.solution.kthSmallest(root, 2), 2)
        self.assertEqual(self.solution.kthSmallest(root, 3), 3)
        self.assertEqual(self.solution.kthSmallest(root, 4), 4)

    def test_right_skewed_tree(self):
        root = build_tree([1, None, 2, None, 3, None, 4, None, 5])
        self.assertEqual(self.solution.kthSmallest(root, 1), 1)
        self.assertEqual(self.solution.kthSmallest(root, 3), 3)
        self.assertEqual(self.solution.kthSmallest(root, 5), 5)

    def test_first_smallest(self):
        root = build_tree([5, 3, 7, 2, 4, 6, 8])
        self.assertEqual(self.solution.kthSmallest(root, 1), 2)

    def test_last_smallest(self):
        root = build_tree([5, 3, 7, 2, 4, 6, 8])
        self.assertEqual(self.solution.kthSmallest(root, 7), 8)

    def test_middle_smallest(self):
        root = build_tree([5, 3, 7, 2, 4, 6, 8])
        self.assertEqual(self.solution.kthSmallest(root, 4), 5)

    def test_k_equals_node_count(self):
        root = build_tree([10, 5, 15, None, None, 12, 20])
        self.assertEqual(self.solution.kthSmallest(root, 5), 20)

    def test_k_equals_one_on_small_tree(self):
        root = build_tree([3, 1, 2])
        self.assertEqual(self.solution.kthSmallest(root, 1), 1)

    def test_tree_with_zero_values(self):
        root = build_tree([2, 0, 3])
        self.assertEqual(self.solution.kthSmallest(root, 1), 0)

    def test_max_value_boundaries(self):
        root = build_tree([5000, 0, 10000])
        self.assertEqual(self.solution.kthSmallest(root, 1), 0)
        self.assertEqual(self.solution.kthSmallest(root, 2), 5000)
        self.assertEqual(self.solution.kthSmallest(root, 3), 10000)

    def test_deeper_bst_all_k(self):
        root = build_tree([11, 5, 17, 3, 7, 13, 21, 2, 4, 6, 8, 12, 14, 20, 22])
        sorted_vals = [2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 17, 20, 21, 22]
        for k, expected in enumerate(sorted_vals, start=1):
            self.assertEqual(self.solution.kthSmallest(root, k), expected)

    def test_all_k_values_on_balanced_tree(self):
        root = build_tree([8, 4, 12, 2, 6, 10, 14])
        for k, expected in enumerate(sorted([8, 4, 12, 2, 6, 10, 14]), start=1):
            self.assertEqual(self.solution.kthSmallest(root, k), expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree
