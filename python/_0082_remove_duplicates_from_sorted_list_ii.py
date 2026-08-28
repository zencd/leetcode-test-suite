# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Medium

import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        raise Exception("Not solved yet")


def build_list(values):
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def to_list(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result


class TestDeleteDuplicates(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def run_case(self, values, expected):
        head = build_list(values)
        result = self.sol.deleteDuplicates(head)
        self.assertEqual(to_list(result), expected)

    def test_empty_list(self):
        self.assertIsNone(self.sol.deleteDuplicates(None))

    def test_single_node(self):
        self.run_case([5], [5])

    def test_two_distinct_nodes(self):
        self.run_case([1, 2], [1, 2])

    def test_two_duplicates(self):
        self.run_case([1, 1], [])

    def test_all_duplicates(self):
        self.run_case([2, 2, 2, 2], [])
        self.run_case([7] * 7, [])

    def test_no_duplicates(self):
        self.run_case([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

    def test_example_1(self):
        self.run_case([1, 2, 3, 3, 4, 4, 5], [1, 2, 5])

    def test_example_2(self):
        self.run_case([1, 1, 1, 2, 3], [2, 3])

    def test_duplicates_at_head(self):
        self.run_case([1, 1, 2, 3, 3], [2])

    def test_duplicates_at_tail(self):
        self.run_case([1, 2, 3, 4, 4], [1, 2, 3])

    def test_duplicates_in_middle(self):
        self.run_case([1, 2, 2, 3], [1, 3])

    def test_everything_duplicated(self):
        self.run_case([1, 1, 2, 2], [])

    def test_three_duplicate_runs(self):
        self.run_case([1, 1, 2, 2, 2, 3, 3, 4], [4])

    def test_negative_values(self):
        self.run_case([-5, -5, -3, -1, -1, 2, 2, 2], [-3])

    def test_zero_values(self):
        self.run_case([0, 0, 0, 1, 2, 2], [1])

    def test_mixed_values(self):
        self.run_case([-100, -100, -1, 0, 1, 1, 1, 100], [-1, 0, 100])

    def test_adjacent_different_duplicates(self):
        self.run_case([1, 1, 2, 2, 3, 3, 4], [4])

    def test_result_link_integrity(self):
        head = build_list([1, 2, 2, 3, 4, 4, 5])
        result = self.sol.deleteDuplicates(head)
        self.assertEqual(to_list(result), [1, 3, 5])
        self.assertIsNone(result.next.next.next)


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Two Pointers
