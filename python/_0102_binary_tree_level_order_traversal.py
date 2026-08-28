# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Medium

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        raise Exception("Not solved yet")


def build_tree(values: List) -> Optional[TreeNode]:
    if not values or values[0] is None:
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


import unittest


class TestSolution(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(Solution().levelOrder(None), [])

    def test_single_node(self):
        self.assertEqual(Solution().levelOrder(build_tree([1])), [[1]])

    def test_two_levels(self):
        self.assertEqual(Solution().levelOrder(build_tree([1, 2, 3])), [[1], [2, 3]])

    def test_example_one(self):
        self.assertEqual(
            Solution().levelOrder(build_tree([3, 9, 20, None, None, 15, 7])),
            [[3], [9, 20], [15, 7]],
        )

    def test_left_skew(self):
        self.assertEqual(
            Solution().levelOrder(build_tree([1, 2, None, 3])), [[1], [2], [3]]
        )

    def test_right_skew(self):
        self.assertEqual(
            Solution().levelOrder(build_tree([1, None, 2, None, 3])), [[1], [2], [3]]
        )

    def test_negative_values(self):
        self.assertEqual(
            Solution().levelOrder(build_tree([-1, -2, -3])), [[-1], [-2, -3]]
        )

    def test_duplicate_values(self):
        self.assertEqual(
            Solution().levelOrder(build_tree([2, 2, 2, 2])), [[2], [2, 2], [2]]
        )

    def test_missing_right_child(self):
        self.assertEqual(
            Solution().levelOrder(build_tree([1, 2, None, 3, 4])), [[1], [2], [3, 4]]
        )

    def test_deeply_imbalanced(self):
        values = [1, 2, None, 3, None, 4]
        self.assertEqual(
            Solution().levelOrder(build_tree(values)), [[1], [2], [3], [4]]
        )

    def test_full_tree(self):
        self.assertEqual(
            Solution().levelOrder(build_tree([1, 2, 3, 4, 5, 6, 7])),
            [[1], [2, 3], [4, 5, 6, 7]],
        )

    def test_result_does_not_mutate_tree(self):
        root = build_tree([1, 2, 3])
        before = (root.val, root.left.val, root.right.val)
        Solution().levelOrder(root)
        after = (root.val, root.left.val, root.right.val)
        self.assertEqual(before, after)

    def test_returns_list_of_lists(self):
        result = Solution().levelOrder(build_tree([1, 2, 3]))
        self.assertIsInstance(result, list)
        for level in result:
            self.assertIsInstance(level, list)


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Breadth-First Search, Binary Tree
