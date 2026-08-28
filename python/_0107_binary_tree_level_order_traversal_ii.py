# 107. Binary Tree Level Order Traversal II
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Medium

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def build(self, values):
        return build_tree(values)

    def test_empty_tree(self):
        self.assertEqual(self.solution.levelOrderBottom(self.build(None)), [])

    def test_empty_list(self):
        self.assertEqual(self.solution.levelOrderBottom(self.build([])), [])

    def test_single_node(self):
        self.assertEqual(self.solution.levelOrderBottom(self.build([1])), [[1]])

    def test_node_with_left_child_only(self):
        self.assertEqual(self.solution.levelOrderBottom(self.build([1, 2])), [[2], [1]])

    def test_node_with_right_child_only(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([1, None, 3])), [[3], [1]]
        )

    def test_two_level_full(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([1, 2, 3])),
            [[2, 3], [1]],
        )

    def test_example_1(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([3, 9, 20, None, None, 15, 7])),
            [[15, 7], [9, 20], [3]],
        )

    def test_example_2(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([1])),
            [[1]],
        )

    def test_example_3(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([])),
            [],
        )

    def test_left_skew(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([1, 2, None, 3, None, 4])),
            [[4], [3], [2], [1]],
        )

    def test_right_skew(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([1, None, 2, None, 3, None, 4])),
            [[4], [3], [2], [1]],
        )

    def test_full_tree_depth_3(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([1, 2, 3, 4, 5, 6, 7])),
            [[4, 5, 6, 7], [2, 3], [1]],
        )

    def test_negative_values(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([-1, -2, -3, -4, -5])),
            [[-4, -5], [-2, -3], [-1]],
        )

    def test_duplicate_values(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([5, 5, 5, 5, 5, 5, 5])),
            [[5, 5, 5, 5], [5, 5], [5]],
        )

    def test_zero_values(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([0, 0, 0])),
            [[0, 0], [0]],
        )

    def test_gaps_in_tree(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([1, 2, None, None, 3, None, 4])),
            [[4], [3], [2], [1]],
        )

    def test_root_none(self):
        self.assertEqual(self.solution.levelOrderBottom(None), [])

    def test_left_child_of_left(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([1, 2, None, 3])),
            [[3], [2], [1]],
        )

    def test_left_child_of_right(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([1, None, 2, 3])),
            [[3], [2], [1]],
        )

    def test_right_child_of_left(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([1, 2, None, None, 3])),
            [[3], [2], [1]],
        )

    def test_mixed_nulls(self):
        self.assertEqual(
            self.solution.levelOrderBottom(self.build([1, 2, 3, None, 4, None, 5])),
            [[4, 5], [2, 3], [1]],
        )

    def test_result_type_and_content(self):
        result = self.solution.levelOrderBottom(self.build([1, 2, 3]))
        self.assertIsInstance(result, list)
        for level in result:
            self.assertIsInstance(level, list)
        self.assertEqual(result[0], [2, 3])
        self.assertEqual(result[1], [1])


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Breadth-First Search, Binary Tree
