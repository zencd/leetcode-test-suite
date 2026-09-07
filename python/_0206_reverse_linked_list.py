# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Easy

from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        raise Exception("Not solved yet")


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
    seen = set()
    while head is not None:
        if id(head) in seen:
            raise AssertionError("cycle detected in linked list")
        seen.add(id(head))
        values.append(head.val)
        head = head.next
    return values


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertIsNone(self.solution.reverseList(None))

    def test_single_node(self):
        head = build_list([42])
        self.assertEqual(to_list(self.solution.reverseList(head)), [42])
        self.assertIsNone(head.next)

    def test_two_nodes(self):
        head = build_list([1, 2])
        result = self.solution.reverseList(head)
        self.assertEqual(to_list(result), [2, 1])
        self.assertIsNone(result.next.next)

    def test_three_nodes(self):
        head = build_list([1, 2, 3])
        self.assertEqual(to_list(self.solution.reverseList(head)), [3, 2, 1])

    def test_example1(self):
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(to_list(self.solution.reverseList(head)), [5, 4, 3, 2, 1])

    def test_reverse_does_not_create_cycle(self):
        head = build_list([1, 2, 3])
        self.solution.reverseList(head)
        to_list(head)

    def test_negative_values(self):
        head = build_list([-5000, 0, 5000])
        self.assertEqual(to_list(self.solution.reverseList(head)), [5000, 0, -5000])

    def test_duplicate_values(self):
        head = build_list([7, 7, 7, 7])
        self.assertEqual(to_list(self.solution.reverseList(head)), [7, 7, 7, 7])

    def test_long_list(self):
        values = list(range(5000))
        head = build_list(values)
        self.assertEqual(to_list(self.solution.reverseList(head)), list(reversed(values)))


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Recursion
