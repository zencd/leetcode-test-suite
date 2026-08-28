# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/
# Medium

import unittest
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        raise Exception("Not solved yet")


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        raise Exception("Not solved yet")


def build_list(spec):
    if not spec:
        return None
    nodes = [Node(v) for v, _ in spec]
    for i, (v, r) in enumerate(spec):
        nodes[i].next = nodes[i + 1] if i + 1 < len(spec) else None
        nodes[i].random = nodes[r] if r is not None else None
    return nodes[0]


def dump_list(head):
    if head is None:
        return None
    nodes = []
    index = {}
    cur = head
    i = 0
    while cur is not None:
        nodes.append(cur)
        index[cur] = i
        i += 1
        cur = cur.next
    return [[n.val, None if n.random is None else index.get(n.random)] for n in nodes]


def assert_same_structure(original, copied):
    orig_dump = dump_list(original)
    copy_dump = dump_list(copied)
    assert orig_dump == copy_dump, f"structure mismatch: {orig_dump} != {copy_dump}"
    orig_nodes = []
    cur = original
    while cur is not None:
        orig_nodes.append(id(cur))
        cur = cur.next
    cur = copied
    while cur is not None:
        assert id(cur) not in orig_nodes, "copy shares a node with original"
        cur = cur.next


class TestSolution(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(Solution().copyRandomList(None))

    def test_single_node_no_random(self):
        spec = [[1, None]]
        head = build_list(spec)
        self.assertEqual(dump_list(head), [[1, None]])
        copied = Solution().copyRandomList(head)
        assert_same_structure(head, copied)

    def test_single_node_self_random(self):
        head = build_list([[1, 0]])
        copied = Solution().copyRandomList(head)
        assert_same_structure(head, copied)

    def test_example1(self):
        spec = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        head = build_list(spec)
        copied = Solution().copyRandomList(head)
        self.assertEqual(dump_list(copied), spec)
        assert_same_structure(head, copied)

    def test_example2(self):
        spec = [[1, 1], [2, 1]]
        head = build_list(spec)
        copied = Solution().copyRandomList(head)
        self.assertEqual(dump_list(copied), spec)
        assert_same_structure(head, copied)

    def test_example3(self):
        spec = [[3, None], [3, 0], [3, None]]
        head = build_list(spec)
        copied = Solution().copyRandomList(head)
        self.assertEqual(dump_list(copied), spec)
        assert_same_structure(head, copied)

    def test_all_random_to_head(self):
        spec = [[1, 0], [2, 0], [3, 0]]
        head = build_list(spec)
        copied = Solution().copyRandomList(head)
        assert_same_structure(head, copied)

    def test_random_pointing_to_last_node(self):
        spec = [[1, 2], [2, 2], [3, 2]]
        head = build_list(spec)
        copied = Solution().copyRandomList(head)
        assert_same_structure(head, copied)

    def test_random_pointing_to_prev_and_next(self):
        spec = [[1, None], [2, 0], [3, 1], [4, 2], [5, 3]]
        head = build_list(spec)
        copied = Solution().copyRandomList(head)
        assert_same_structure(head, copied)

    def test_no_random_at_all(self):
        spec = [[5, None], [4, None], [3, None], [2, None], [1, None]]
        head = build_list(spec)
        copied = Solution().copyRandomList(head)
        assert_same_structure(head, copied)

    def test_negative_and_zero_values(self):
        spec = [[-10000, 1], [0, 0], [10000, None]]
        head = build_list(spec)
        copied = Solution().copyRandomList(head)
        assert_same_structure(head, copied)

    def test_all_self_random(self):
        spec = [[1, 0], [2, 1], [3, 2], [4, 3]]
        head = build_list(spec)
        copied = Solution().copyRandomList(head)
        assert_same_structure(head, copied)

    def test_original_list_unchanged(self):
        spec = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        head = build_list(spec)
        before = dump_list(head)
        Solution().copyRandomList(head)
        self.assertEqual(dump_list(head), before)

    def test_two_copies_both_valid(self):
        spec = [[1, 2], [2, 0], [3, 1]]
        head = build_list(spec)
        copy1 = Solution().copyRandomList(head)
        copy2 = Solution().copyRandomList(head)
        dump1 = dump_list(copy1)
        dump2 = dump_list(copy2)
        self.assertEqual(dump1, spec)
        self.assertEqual(dump2, spec)
        self.assertIsNot(copy1, copy2)

    def test_large_list(self):
        n = 1000
        spec = [[i, (i * 7 + 3) % n] for i in range(n)]
        head = build_list(spec)
        copied = Solution().copyRandomList(head)
        self.assertEqual(dump_list(copied), spec)
        assert_same_structure(head, copied)


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Linked List
