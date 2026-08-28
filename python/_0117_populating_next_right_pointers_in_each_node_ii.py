# 117. Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Medium

class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        raise Exception("Not solved yet")


class Solution:
    def connect(self, root: "Node") -> "Node":
        raise Exception("Not solved yet")


def build_tree(values):
    if not values:
        return None
    nodes = []
    for i, v in enumerate(values):
        if v is None:
            nodes.append(None)
        else:
            nodes.append(Node(v))
    for i, node in enumerate(nodes):
        if node is None:
            continue
        li, ri = 2 * i + 1, 2 * i + 2
        if li < len(nodes):
            node.left = nodes[li]
        if ri < len(nodes):
            node.right = nodes[ri]
    return nodes[0]


def to_serialized(root: "Node") -> list:
    result = []
    head = root
    while head:
        curr = head
        next_head = None
        while curr:
            result.append(curr.val)
            if next_head is None and (curr.left or curr.right):
                next_head = curr.left or curr.right
            curr = curr.next
        result.append("#")
        head = next_head
    return result


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_tree(self):
        self.assertIsNone(self.sol.connect(None))
        self.assertEqual(to_serialized(None), [])

    def test_single_node(self):
        root = Node(1)
        self.sol.connect(root)
        self.assertEqual(root.next, None)
        self.assertIs(self.sol.connect(root), root)

    def test_example1(self):
        root = build_tree([1, 2, 3, 4, 5, None, 7])
        self.sol.connect(root)
        self.assertEqual(to_serialized(root), [1, "#", 2, 3, "#", 4, 5, 7, "#"])

    def test_full_binary_tree(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.sol.connect(root)
        self.assertEqual(root.next, None)
        self.assertIs(root.left.next, root.right)
        self.assertIs(root.right.next, None)
        self.assertIs(root.left.left.next, root.left.right)
        self.assertIs(root.left.right.next, root.right.left)
        self.assertIs(root.right.left.next, root.right.right)

    def test_left_spine(self):
        n4 = Node(4)
        n3 = Node(3, left=n4)
        n2 = Node(2, left=n3)
        root = Node(1, left=n2)
        self.sol.connect(root)
        self.assertIs(root.left.next, None)
        self.assertIs(root.left.left.next, None)
        self.assertIs(n4.next, None)
        self.assertEqual(to_serialized(root), [1, "#", 2, "#", 3, "#", 4, "#"])

    def test_right_spine(self):
        n4 = Node(4)
        n3 = Node(3, right=n4)
        n2 = Node(2, right=n3)
        root = Node(1, right=n2)
        self.sol.connect(root)
        self.assertIs(root.right.next, None)
        self.assertIs(root.right.right.next, None)
        self.assertIs(root.right.right.right.next, None)
        self.assertEqual(to_serialized(root), [1, "#", 2, "#", 3, "#", 4, "#"])

    def test_skewed_with_gaps(self):
        n5 = Node(5)
        n4 = Node(4)
        n3 = Node(3, right=n5)
        n2 = Node(2, left=n4)
        root = Node(1, left=n2, right=n3)
        self.sol.connect(root)
        self.assertIs(root.left.next, root.right)
        self.assertIs(root.right.next, None)
        self.assertIs(root.left.left.next, root.right.right)
        self.assertIs(root.right.right.next, None)
        self.assertEqual(to_serialized(root), [1, "#", 2, 3, "#", 4, 5, "#"])

    def test_missing_next_for_orphan_right(self):
        root = build_tree([1, 2, 3, None, None, 4, None])
        self.sol.connect(root)
        self.assertIs(root.right.left.next, None)

    def test_negative_and_boundary_values(self):
        root = build_tree([-100, 100, -100, 0, None, None, 99])
        self.sol.connect(root)
        self.assertIs(root.left.next, root.right)
        self.assertIs(root.right.right.next, None)
        self.assertIs(root.left.left.next, root.right.left) if root.right.left else None

    def test_returns_root(self):
        root = Node(1)
        self.assertIs(self.sol.connect(root), root)

    def test_next_initially_null_not_modified_on_null_input(self):
        self.assertIsNone(self.sol.connect(None))

    def test_wide_tree(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.sol.connect(root)
        level2 = [4, 5, 6, 7]
        head = root.left.left
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        self.assertEqual(vals, level2)
        level3 = [8, 9, 10, 11, 12, 13, 14, 15]
        head = root.left.left.left
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        self.assertEqual(vals, level3)

    def test_degenerate_two_nodes(self):
        root = build_tree([1, None, 2])
        self.sol.connect(root)
        self.assertIs(root.right.next, None)
        root = build_tree([1, 2, None])
        self.sol.connect(root)
        self.assertIs(root.left.next, None)

    def test_deep_chain_random(self):
        import random

        random.seed(42)
        n = 200
        values = [random.randint(-100, 100) for _ in range(n)]
        root = build_tree(values)
        self.sol.connect(root)
        dummy = Node(0)
        tail = dummy
        curr = root
        while curr:
            if curr.left:
                tail.next = curr.left
                tail = curr.left
            if curr.right:
                tail.next = curr.right
                tail = curr.right
            curr = curr.next
        expected = [dummy.next]
        node = dummy.next
        while node:
            expected.append(node.val)
            node = node.next
        actual_head = root
        node = actual_head.left or actual_head.right
        actual = []
        while node:
            actual.append(node.val)
            node = node.next
        tail_node = dummy.next
        got = []
        node = root.left
        collected = []
        c = root
        while c:
            if c.left:
                collected.append(c.left.val)
            if c.right:
                collected.append(c.right.val)
            c = c.next
        self.assertEqual(actual, collected)


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree
