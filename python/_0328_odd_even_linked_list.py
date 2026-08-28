# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/
# Medium

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_list(head):
    values = []
    node = head
    while node is not None:
        values.append(node.val)
        node = node.next
    return values


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_list(self):
        self.assertIsNone(self.sol.oddEvenList(None))

    def test_single_node(self):
        head = build_list([1])
        self.assertEqual(to_list(self.sol.oddEvenList(head)), [1])

    def test_two_nodes(self):
        head = build_list([1, 2])
        self.assertEqual(to_list(self.sol.oddEvenList(head)), [1, 2])

    def test_example_1(self):
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(to_list(self.sol.oddEvenList(head)), [1, 3, 5, 2, 4])

    def test_example_2(self):
        head = build_list([2, 1, 3, 5, 6, 4, 7])
        self.assertEqual(to_list(self.sol.oddEvenList(head)), [2, 3, 6, 7, 1, 5, 4])

    def test_even_length_even_head_unchanged(self):
        head = build_list([1, 2, 3, 4])
        self.assertEqual(to_list(self.sol.oddEvenList(head)), [1, 3, 2, 4])

    def test_even_length_two(self):
        head = build_list([5, 3])
        self.assertEqual(to_list(self.sol.oddEvenList(head)), [5, 3])

    def test_even_length_six(self):
        head = build_list([3, 10, 1, 7, 4, 9])
        self.assertEqual(to_list(self.sol.oddEvenList(head)), [3, 1, 4, 10, 7, 9])

    def test_negative_values(self):
        head = build_list([-1, 2, -3, 4, -5])
        self.assertEqual(to_list(self.sol.oddEvenList(head)), [-1, -3, -5, 2, 4])

    def test_all_equal_values(self):
        head = build_list([7, 7, 7, 7, 7])
        self.assertEqual(to_list(self.sol.oddEvenList(head)), [7, 7, 7, 7, 7])

    def test_zero_values(self):
        head = build_list([0, 0, 0])
        self.assertEqual(to_list(self.sol.oddEvenList(head)), [0, 0, 0])

    def test_extreme_values(self):
        head = build_list([-(10**6), 10**6, -(10**6), 10**6])
        self.assertEqual(
            to_list(self.sol.oddEvenList(head)), [-(10**6), -(10**6), 10**6, 10**6]
        )

    def test_unchanged_when_already_sorted_order(self):
        head = build_list([1, 2, 3])
        self.assertEqual(to_list(self.sol.oddEvenList(head)), [1, 3, 2])

    def test_many_nodes(self):
        values = list(range(1, 21))
        head = build_list(values)
        result = to_list(self.sol.oddEvenList(head))
        expected_odd = values[::2]
        expected_even = values[1::2]
        self.assertEqual(result, expected_odd + expected_even)

    def test_head_pointer_preserved(self):
        head = build_list([1, 2, 3, 4])
        original_head = head
        result = self.sol.oddEvenList(head)
        self.assertIs(result, original_head)

    def test_even_head_preserved_when_empty(self):
        self.assertIsNone(self.sol.oddEvenList(None))

    def test_no_cycle_created(self):
        head = build_list([1, 2, 3, 4, 5])
        result = self.sol.oddEvenList(head)
        self.assertEqual(len(to_list(result)), 5)
        node = result
        seen = set()
        while node is not None:
            self.assertNotIn(id(node), seen)
            seen.add(id(node))
            node = node.next


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List
