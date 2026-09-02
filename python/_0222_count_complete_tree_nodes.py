# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/
# Medium

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        raise Exception("Not solved yet")


def _node_count(node: Optional[TreeNode]) -> int:
    if node is None:
        return 0
    return 1 + _node_count(node.left) + _node_count(node.right)


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    index = 1
    while queue and index < len(values):
        node = queue.pop(0)
        if index < len(values):
            node.left = TreeNode(values[index])
            queue.append(node.left)
            index += 1
        if index < len(values):
            node.right = TreeNode(values[index])
            queue.append(node.right)
            index += 1
    return root


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.countNodes(None), 0)

    def test_single_node(self):
        self.assertEqual(self.solution.countNodes(build_tree([1])), 1)

    def test_two_nodes(self):
        self.assertEqual(self.solution.countNodes(build_tree([1, 2])), 2)

    def test_three_nodes_full(self):
        self.assertEqual(self.solution.countNodes(build_tree([1, 2, 3])), 3)

    def test_four_nodes(self):
        self.assertEqual(self.solution.countNodes(build_tree([1, 2, 3, 4])), 4)

    def test_five_nodes(self):
        self.assertEqual(self.solution.countNodes(build_tree([1, 2, 3, 4, 5])), 5)

    def test_six_nodes_example(self):
        self.assertEqual(self.solution.countNodes(build_tree([1, 2, 3, 4, 5, 6])), 6)

    def test_seven_nodes_full(self):
        self.assertEqual(self.solution.countNodes(build_tree([1, 2, 3, 4, 5, 6, 7])), 7)

    def test_eight_nodes(self):
        self.assertEqual(self.solution.countNodes(build_tree([1, 2, 3, 4, 5, 6, 7, 8])), 8)

    def test_fifteen_nodes_full(self):
        self.assertEqual(self.solution.countNodes(build_tree(list(range(1, 16)))), 15)

    def test_thirty_one_nodes_full(self):
        self.assertEqual(self.solution.countNodes(build_tree(list(range(1, 32)))), 31)

    def test_thirty_two_nodes(self):
        self.assertEqual(self.solution.countNodes(build_tree(list(range(1, 33)))), 32)

    def test_left_skewed_complete(self):
        self.assertEqual(self.solution.countNodes(build_tree([7, 6, 5, 4, 3])), 5)

    def test_zero_valued_nodes(self):
        self.assertEqual(self.solution.countNodes(build_tree([0, 0, 0, 0])), 4)

    def test_large_last_level_partial(self):
        values = list(range(1, 65))
        self.assertEqual(self.solution.countNodes(build_tree(values)), 64)
        values = list(range(1, 66))
        self.assertEqual(self.solution.countNodes(build_tree(values)), 65)

    def test_against_brute_force_random_complete_trees(self):
        import random

        random.seed(42)
        for _ in range(50):
            n = random.randint(0, 200)
            tree = build_tree(list(range(1, n + 1)))
            expected = _node_count(tree)
            self.assertEqual(self.solution.countNodes(tree), expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Binary Search, Bit Manipulation, Tree, Binary Tree
