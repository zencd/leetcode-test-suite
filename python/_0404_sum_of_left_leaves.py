# 404. Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/
# Easy

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        raise Exception("Not solved yet")


def from_list(values):
    if not values or values[0] is None:
        return None
    nodes = [None] * len(values)
    nodes[0] = TreeNode(values[0])
    queue = [0]
    idx = 1
    while queue and idx < len(values):
        i = queue.pop(0)
        if idx < len(values) and values[idx] is not None:
            nodes[i].left = nodes[idx] = TreeNode(values[idx])
            queue.append(idx)
        idx += 1
        if idx < len(values) and values[idx] is not None:
            nodes[i].right = nodes[idx] = TreeNode(values[idx])
            queue.append(idx)
        idx += 1
    return nodes[0]


def to_list(root):
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


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        root = from_list([3, 9, 20, None, None, 15, 7])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 24)

    def test_example2_single_root(self):
        root = from_list([1])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 0)

    def test_only_left_leaf(self):
        root = from_list([1, 2])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 2)

    def test_only_right_leaf(self):
        root = from_list([1, None, 2])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 0)

    def test_two_leaves_both_sides(self):
        root = from_list([1, 2, 3])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 2)

    def test_left_child_with_children(self):
        root = from_list([1, 2, 3, 4, 5])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 4)

    def test_negative_values(self):
        root = from_list([0, -5, 10, None, None, -7, 3])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), -12)

    def test_deep_left_chain(self):
        root = from_list([1, 2, None, 3, None, 4])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 4)

    def test_deep_right_chain(self):
        root = from_list([1, None, 2, None, 3, None, 4])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 0)

    def test_multiple_left_leaves(self):
        root = from_list([3, 9, 20, None, None, 15, 7, 1, 2])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 10)

    def test_root_with_left_internal_and_leaf(self):
        root = from_list([5, 4, 6, 7, None, 8, 9])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 15)

    def test_zero_valued_nodes(self):
        root = from_list([0, 0, 0])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 0)

    def test_max_valued_nodes(self):
        root = from_list([1000, 1000, 1000])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 1000)

    def test_roundtrip_serialization(self):
        values = [3, 9, 20, None, None, 15, 7]
        root = from_list(values)
        serialized = to_list(root)
        expected = [3, 9, 20, None, None, 15, 7]
        i = 0
        j = 0
        self.assertTrue(len(serialized) >= len(expected))
        for ex in expected:
            self.assertEqual(serialized[i], ex, "mismatch at position " + str(i) + ": " + str(serialized))
            i += 1

    def test_helper_from_list_roundtrip(self):
        values = [1, 2, 3, 4, None, 6, 7, 8]
        root = from_list(values)
        self.assertEqual(to_list(root), values)

    def test_helper_from_list_empty(self):
        self.assertIsNone(from_list([]))
        self.assertIsNone(from_list([None]))

    def test_helper_from_list_single(self):
        root = from_list([5])
        self.assertEqual(root.val, 5)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_helper_to_list_empty(self):
        self.assertEqual(to_list(None), [])


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
