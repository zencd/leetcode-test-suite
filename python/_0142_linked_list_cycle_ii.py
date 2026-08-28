# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/
# Medium

import unittest
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        raise Exception("Not solved yet")


def build_list(values, pos):
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos is not None and pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def get_node(head, index):
    cur = head
    for _ in range(index):
        cur = cur.next
    return cur


def list_values(head, limit=100000):
    values = []
    cur = head
    while cur is not None and len(values) < limit:
        values.append(cur.val)
        cur = cur.next
    return values


class TestSolution(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(Solution().detectCycle(None))

    def test_single_node_no_cycle(self):
        head = build_list([1], -1)
        self.assertIsNone(Solution().detectCycle(head))

    def test_single_node_self_cycle(self):
        head = build_list([1], 0)
        self.assertIs(Solution().detectCycle(head), head)

    def test_cycle_at_head(self):
        head = build_list([1, 2], 0)
        self.assertIs(Solution().detectCycle(head), head)

    def test_cycle_at_middle(self):
        head = build_list([3, 2, 0, -4], 1)
        self.assertIs(Solution().detectCycle(head), get_node(head, 1))

    def test_cycle_at_tail_node(self):
        head = build_list([1, 2, 3, 4], 3)
        self.assertIs(Solution().detectCycle(head), get_node(head, 3))

    def test_no_cycle(self):
        head = build_list([1, 2, 3, 4, 5], -1)
        self.assertIsNone(Solution().detectCycle(head))

    def test_two_nodes_no_cycle(self):
        head = build_list([1, 2], -1)
        self.assertIsNone(Solution().detectCycle(head))

    def test_two_nodes_cycle_at_first(self):
        head = build_list([1, 2], 0)
        self.assertIs(Solution().detectCycle(head), head)

    def test_two_nodes_cycle_at_second(self):
        head = build_list([1, 2], 1)
        self.assertIs(Solution().detectCycle(head), get_node(head, 1))

    def test_negative_values_no_cycle(self):
        head = build_list([-1, -100000, 100000], -1)
        self.assertIsNone(Solution().detectCycle(head))

    def test_large_list_cycle_at_start(self):
        values = list(range(1, 1001))
        head = build_list(values, 0)
        self.assertIs(Solution().detectCycle(head), head)

    def test_large_list_cycle_in_middle(self):
        values = list(range(1, 1001))
        head = build_list(values, 500)
        self.assertIs(Solution().detectCycle(head), get_node(head, 500))

    def test_large_list_no_cycle(self):
        values = list(range(1, 1001))
        head = build_list(values, -1)
        self.assertIsNone(Solution().detectCycle(head))

    def test_list_not_modified(self):
        head = build_list([3, 2, 0, -4], 1)
        target = get_node(head, 1)
        Solution().detectCycle(head)
        self.assertEqual(list_values(head, 10), [3, 2, 0, -4, 2, 0, -4, 2, 0, -4])
        self.assertIs(get_node(head, 1), target)


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Linked List, Two Pointers, Floyd's Cycle Finding Algorithm
