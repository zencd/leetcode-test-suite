# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/
# Medium

from typing import Optional
import unittest


class Node:
    def __init__(self, val=0, neighbors=None):
        raise Exception("Not solved yet")


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        raise Exception("Not solved yet")


def build_graph(adj_list):
    if not adj_list:
        return None
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[n - 1] for n in neighbors]
    return nodes[0]


def get_adj(start):
    if start is None:
        return None
    visited = set()
    nodes = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        nodes.append(node)
        stack.extend(node.neighbors)
    nodes.sort(key=lambda n: n.val)
    return [sorted(n.val for n in node.neighbors) for node in nodes]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_none(self):
        self.assertIsNone(self.solution.cloneGraph(None))

    def test_single_node(self):
        original = build_graph([[]])
        cloned = self.solution.cloneGraph(original)
        self.assertEqual(cloned.val, 1)
        self.assertEqual(cloned.neighbors, [])

    def test_two_nodes(self):
        original = build_graph([[2], [1]])
        cloned = self.solution.cloneGraph(original)
        self.assertEqual(get_adj(cloned), [[2], [1]])

    def test_example1(self):
        adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
        original = build_graph(adj)
        cloned = self.solution.cloneGraph(original)
        self.assertEqual(get_adj(cloned), adj)

    def test_line_of_three(self):
        adj = [[2], [1, 3], [2]]
        original = build_graph(adj)
        cloned = self.solution.cloneGraph(original)
        self.assertEqual(get_adj(cloned), adj)

    def test_star_graph(self):
        adj = [[2, 3, 4, 5, 6], [1], [1], [1], [1], [1]]
        original = build_graph(adj)
        cloned = self.solution.cloneGraph(original)
        self.assertEqual(get_adj(cloned), adj)

    def test_cycle(self):
        adj = [[2, 3], [1, 3, 4], [1, 2, 4], [2, 3]]
        original = build_graph(adj)
        cloned = self.solution.cloneGraph(original)
        self.assertEqual(get_adj(cloned), adj)

    def test_larger_graph(self):
        adj = [
            [2, 3],
            [1, 4, 5],
            [1, 6],
            [2, 5],
            [2, 4, 6],
            [3, 5],
        ]
        original = build_graph(adj)
        cloned = self.solution.cloneGraph(original)
        self.assertEqual(get_adj(cloned), adj)

    def test_clone_is_deep(self):
        original = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
        cloned = self.solution.cloneGraph(original)
        self.assertIsNot(cloned, original)
        for clone_neighbor in cloned.neighbors:
            self.assertNotIn(clone_neighbor, original.neighbors)

    def test_clone_mutating_does_not_affect_original(self):
        original = build_graph([[2, 3], [1, 3], [1, 2]])
        cloned = self.solution.cloneGraph(original)
        for node in cloned.neighbors:
            node.neighbors.append(cloned)
            node.val = 999
        self.assertEqual(get_adj(original), [[2, 3], [1, 3], [1, 2]])
        self.assertEqual(original.neighbors[0].val, 2)

    def test_original_mutating_does_not_affect_clone(self):
        original = build_graph([[2, 3], [1, 3], [1, 2]])
        cloned = self.solution.cloneGraph(original)
        original.neighbors[0].val = 999
        self.assertEqual(get_adj(cloned), [[2, 3], [1, 3], [1, 2]])

    def test_two_separate_calls_independent(self):
        original = build_graph([[2, 3], [1, 3], [1, 2]])
        first = self.solution.cloneGraph(original)
        second = self.solution.cloneGraph(original)
        self.assertIsNot(first, second)
        self.assertIsNot(first.neighbors[0], second.neighbors[0])
        self.assertEqual(get_adj(first), get_adj(second))

    def test_many_nodes_line(self):
        n = 100
        adj = [[i + 2] for i in range(n - 1)] + [[n - 1]]
        original = build_graph(adj)
        cloned = self.solution.cloneGraph(original)
        self.assertEqual(get_adj(cloned), adj)

    def test_full_parity_structure(self):
        adj = [[2, 3, 4], [1, 3], [1, 2, 4], [1, 3]]
        original = build_graph(adj)
        cloned = self.solution.cloneGraph(original)
        self.assertEqual(len(get_adj(cloned)), 4)
        self.assertEqual(sorted(x.val for x in cloned.neighbors), [2, 3, 4])


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Depth-First Search, Breadth-First Search, Graph Theory
