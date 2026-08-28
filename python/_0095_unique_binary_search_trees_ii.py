# 95. Unique Binary Search Trees II
# https://leetcode.com/problems/unique-binary-search-trees-ii/
# Medium

from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        raise Exception("Not solved yet")


def to_list(root):
    result = []
    queue = [root]
    i = 0
    while i < len(queue):
        node = queue[i]
        i += 1
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def normalize(trees):
    return sorted(to_list(t) for t in trees)


def is_valid_bst(root):
    def check(node, lo, hi):
        if node is None:
            return True
        if not (lo < node.val < hi):
            return False
        return check(node.left, lo, node.val) and check(node.right, node.val, hi)

    return check(root, float("-inf"), float("inf"))


def collect_values(root):
    if root is None:
        return []
    return collect_values(root.left) + [root.val] + collect_values(root.right)


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_n_1(self):
        self.assertEqual(normalize(self.s.generateTrees(1)), [[1]])

    def test_n_2(self):
        self.assertEqual(normalize(self.s.generateTrees(2)), [[1, None, 2], [2, 1]])

    def test_n_3(self):
        got = self.s.generateTrees(3)
        expected = [
            [1, None, 2, None, 3],
            [1, None, 3, 2],
            [2, 1, 3],
            [3, 1, None, None, 2],
            [3, 2, None, 1],
        ]
        self.assertEqual(sorted(normalize(got), key=str), sorted(expected, key=str))

    def test_n_4_count(self):
        self.assertEqual(len(self.s.generateTrees(4)), 14)

    def test_n_5_count(self):
        self.assertEqual(len(self.s.generateTrees(5)), 42)

    def test_n_8_count(self):
        self.assertEqual(len(self.s.generateTrees(8)), 1430)

    def test_all_trees_are_valid_bsts(self):
        for n in (1, 2, 3, 4, 5, 6, 7, 8):
            for tree in self.s.generateTrees(n):
                self.assertTrue(is_valid_bst(tree), n)
                self.assertEqual(len(collect_values(tree)), n, n)
                self.assertEqual(sorted(collect_values(tree)), list(range(1, n + 1)), n)

    def test_node_count(self):
        for n in (1, 3, 7):
            for tree in self.s.generateTrees(n):
                self.assertEqual(count_nodes(tree), n, n)

    def test_trees_are_distinct_structures(self):
        n = 4
        shapes = set()
        for tree in self.s.generateTrees(n):
            shapes.add(tuple(to_list(tree)))
        self.assertEqual(len(shapes), len(self.s.generateTrees(n)))

    def test_root_values_for_n_3(self):
        roots = sorted(t.val for t in self.s.generateTrees(3))
        self.assertEqual(roots, [1, 1, 2, 3, 3])

    def test_returns_fresh_trees(self):
        a = self.s.generateTrees(3)
        b = self.s.generateTrees(3)
        self.assertEqual(normalize(a), normalize(b))


if __name__ == "__main__":
    unittest.main()

# Tags: Dynamic Programming, Backtracking, Tree, Binary Search Tree, Binary Tree
