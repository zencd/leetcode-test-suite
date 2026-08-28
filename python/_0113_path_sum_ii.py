# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/
# Medium

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        raise Exception("Not solved yet")


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


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertPathsEqual(self, expected, actual):
        self.assertEqual(sorted(map(tuple, expected)), sorted(map(tuple, actual)))

    def test_example1(self):
        root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
        self.assertPathsEqual(
            [[5, 4, 11, 2], [5, 8, 4, 5]], self.solution.pathSum(root, 22)
        )

    def test_example2(self):
        root = build_tree([1, 2, 3])
        self.assertEqual([], self.solution.pathSum(root, 5))

    def test_example3(self):
        root = build_tree([1, 2])
        self.assertEqual([], self.solution.pathSum(root, 0))

    def test_empty_tree(self):
        self.assertEqual([], self.solution.pathSum(None, 5))

    def test_single_node_matching(self):
        root = TreeNode(0)
        self.assertPathsEqual([[0]], self.solution.pathSum(root, 0))

    def test_single_node_not_matching(self):
        root = TreeNode(3)
        self.assertEqual([], self.solution.pathSum(root, 5))

    def test_negative_values(self):
        root = build_tree([-2, 1, -3, 0, None, -1, None, None, -2])
        self.assertPathsEqual([[-2, 1, 0, -2]], self.solution.pathSum(root, -3))
        self.assertPathsEqual([[-2, -3, -1]], self.solution.pathSum(root, -6))

    def test_no_path_found(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual([], self.solution.pathSum(root, 100))

    def test_target_zero_with_zero_sum_path(self):
        root = build_tree([1, -1, 0, 1, None, -1])
        self.assertPathsEqual([[1, 0, -1]], self.solution.pathSum(root, 0))

    def test_multiple_paths_same_sum(self):
        root = build_tree([10, 5, 5, 3, 3, 3, 3])
        self.assertPathsEqual(
            [[10, 5, 3], [10, 5, 3], [10, 5, 3], [10, 5, 3]],
            self.solution.pathSum(root, 18),
        )

    def test_deep_chain(self):
        root = TreeNode(1)
        node = root
        for _ in range(9):
            node.left = TreeNode(1)
            node = node.left
        self.assertPathsEqual([[1] * 10], self.solution.pathSum(root, 10))

    def test_root_only_leaf_with_negative_target(self):
        root = TreeNode(-1000)
        self.assertPathsEqual([[-1000]], self.solution.pathSum(root, -1000))

    def test_internal_nodes_excluded_when_wrong_sum(self):
        root = build_tree([5, 2, 3])
        self.assertEqual([], self.solution.pathSum(root, 5))

    def test_two_paths_distinct_lists(self):
        root = build_tree([1, 2, 2])
        actual = self.solution.pathSum(root, 3)
        self.assertPathsEqual([[1, 2], [1, 2]], actual)
        self.assertIsNot(actual[0], actual[1])


if __name__ == "__main__":
    unittest.main()

# Tags: Backtracking, Tree, Depth-First Search, Binary Tree
