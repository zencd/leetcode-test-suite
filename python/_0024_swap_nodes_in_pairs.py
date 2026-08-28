# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/
# Medium

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        raise Exception("Not solved yet")


def build_list(values):
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty(self):
        self.assertIsNone(self.solution.swapPairs(None))

    def test_single_node(self):
        head = build_list([1])
        self.assertEqual(to_list(self.solution.swapPairs(head)), [1])

    def test_two_nodes(self):
        head = build_list([1, 2])
        self.assertEqual(to_list(self.solution.swapPairs(head)), [2, 1])

    def test_three_nodes(self):
        head = build_list([1, 2, 3])
        self.assertEqual(to_list(self.solution.swapPairs(head)), [2, 1, 3])

    def test_four_nodes(self):
        head = build_list([1, 2, 3, 4])
        self.assertEqual(to_list(self.solution.swapPairs(head)), [2, 1, 4, 3])

    def test_five_nodes(self):
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(to_list(self.solution.swapPairs(head)), [2, 1, 4, 3, 5])

    def test_six_nodes(self):
        head = build_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(to_list(self.solution.swapPairs(head)), [2, 1, 4, 3, 6, 5])

    def test_even_long(self):
        head = build_list(list(range(10)))
        expected = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]
        self.assertEqual(to_list(self.solution.swapPairs(head)), expected)

    def test_odd_long(self):
        head = build_list(list(range(11)))
        expected = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 10]
        self.assertEqual(to_list(self.solution.swapPairs(head)), expected)

    def test_all_equal_values(self):
        head = build_list([7, 7, 7, 7])
        self.assertEqual(to_list(self.solution.swapPairs(head)), [7, 7, 7, 7])

    def test_zero_values(self):
        head = build_list([0, 0])
        self.assertEqual(to_list(self.solution.swapPairs(head)), [0, 0])

    def test_max_values(self):
        head = build_list([100, 100, 100, 100, 100])
        self.assertEqual(
            to_list(self.solution.swapPairs(head)), [100, 100, 100, 100, 100]
        )

    def test_no_value_modification(self):
        initial = build_list([1, 2, 3, 4])
        node1 = initial
        node2 = node1.next
        node3 = node2.next
        node4 = node3.next
        result = self.solution.swapPairs(initial)
        self.assertEqual(node1.val, 1)
        self.assertEqual(node2.val, 2)
        self.assertEqual(node3.val, 3)
        self.assertEqual(node4.val, 4)
        self.assertIs(result, node2)
        self.assertIs(result.next, node1)
        self.assertIs(result.next.next, node4)
        self.assertIs(result.next.next.next, node3)
        self.assertIsNone(result.next.next.next.next)


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Recursion
