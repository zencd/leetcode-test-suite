# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Easy

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        raise Exception("Not solved yet")


def build_list(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    nodes = [head]
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
        nodes.append(current)
    if pos != -1:
        current.next = nodes[pos]
    return head


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertFalse(self.solution.hasCycle(None))

    def test_single_node_no_cycle(self):
        head = build_list([1], -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_single_node_cycle(self):
        head = build_list([1], 0)
        self.assertTrue(self.solution.hasCycle(head))

    def test_two_nodes_no_cycle(self):
        head = build_list([1, 2], -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_two_nodes_cycle_head(self):
        head = build_list([1, 2], 0)
        self.assertTrue(self.solution.hasCycle(head))

    def test_two_nodes_cycle_tail(self):
        head = build_list([1, 2], 1)
        self.assertTrue(self.solution.hasCycle(head))

    def test_four_nodes_cycle_mid(self):
        head = build_list([3, 2, 0, -4], 1)
        self.assertTrue(self.solution.hasCycle(head))

    def test_four_nodes_no_cycle(self):
        head = build_list([3, 2, 0, -4], -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_cycle_at_tail_node(self):
        head = build_list([1, 2, 3, 4, 5], 4)
        self.assertTrue(self.solution.hasCycle(head))

    def test_cycle_at_head_node(self):
        head = build_list([1, 2, 3, 4, 5], 0)
        self.assertTrue(self.solution.hasCycle(head))

    def test_cycle_at_second_node(self):
        head = build_list([1, 2, 3, 4, 5], 1)
        self.assertTrue(self.solution.hasCycle(head))

    def test_long_list_no_cycle(self):
        head = build_list(list(range(1000)), -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_long_list_cycle(self):
        head = build_list(list(range(1000)), 999)
        self.assertTrue(self.solution.hasCycle(head))

    def test_negative_values_no_cycle(self):
        head = build_list([-10, 0, 10, -100000, 100000], -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_negative_values_cycle(self):
        head = build_list([-10, 0, 10], 1)
        self.assertTrue(self.solution.hasCycle(head))

    def test_duplicate_values_no_cycle(self):
        head = build_list([1, 1, 1, 1], -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_duplicate_values_cycle(self):
        head = build_list([1, 1, 1, 1], 2)
        self.assertTrue(self.solution.hasCycle(head))

    def test_two_equal_nodes_cycle(self):
        head = build_list([5, 5], 0)
        self.assertTrue(self.solution.hasCycle(head))

    def test_three_nodes_cycle_middle(self):
        head = build_list([7, 8, 9], 1)
        self.assertTrue(self.solution.hasCycle(head))

    def test_zero_value_single_node(self):
        head = build_list([0], -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_zero_value_single_node_cycle(self):
        head = build_list([0], 0)
        self.assertTrue(self.solution.hasCycle(head))


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Linked List, Two Pointers, Floyd's Cycle Finding Algorithm
