# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/
# Easy

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    head = None
    tail = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_removes_values_in_middle_and_tail(self):
        self.assertEqual(
            to_list(Solution().removeElements(build_list([1, 2, 6, 3, 4, 5, 6]), 6)),
            [1, 2, 3, 4, 5],
        )

    def test_empty_list(self):
        self.assertIsNone(Solution().removeElements(build_list([]), 1))

    def test_all_nodes_removed(self):
        self.assertIsNone(Solution().removeElements(build_list([7, 7, 7, 7]), 7))

    def test_single_node_removed(self):
        self.assertIsNone(Solution().removeElements(build_list([5]), 5))

    def test_single_node_kept(self):
        self.assertEqual(
            to_list(Solution().removeElements(build_list([5]), 6)),
            [5],
        )

    def test_head_node_removed(self):
        self.assertEqual(
            to_list(Solution().removeElements(build_list([1, 2, 3]), 1)),
            [2, 3],
        )

    def test_all_leading_nodes_removed(self):
        self.assertEqual(
            to_list(Solution().removeElements(build_list([1, 1, 2, 3]), 1)),
            [2, 3],
        )

    def test_val_not_present(self):
        self.assertEqual(
            to_list(Solution().removeElements(build_list([1, 2, 3]), 4)),
            [1, 2, 3],
        )

    def test_duplicated_values_kept_for_other_values(self):
        self.assertEqual(
            to_list(Solution().removeElements(build_list([2, 1, 2, 1, 2]), 1)),
            [2, 2, 2],
        )

    def test_val_outside_node_range(self):
        self.assertEqual(
            to_list(Solution().removeElements(build_list([0, 50]), 50)),
            [0],
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Recursion
