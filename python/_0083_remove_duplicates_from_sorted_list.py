# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Easy

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
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


import unittest


class TestDeleteDuplicates(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def run_case(self, values):
        return to_list(self.s.deleteDuplicates(build_list(values)))

    def test_example1(self):
        self.assertEqual(self.run_case([1, 1, 2]), [1, 2])

    def test_example2(self):
        self.assertEqual(self.run_case([1, 1, 2, 3, 3]), [1, 2, 3])

    def test_empty_list(self):
        self.assertIsNone(self.s.deleteDuplicates(None))

    def test_single_node(self):
        self.assertEqual(self.run_case([1]), [1])

    def test_two_equal_nodes(self):
        self.assertEqual(self.run_case([2, 2]), [2])

    def test_two_distinct_nodes(self):
        self.assertEqual(self.run_case([1, 2]), [1, 2])

    def test_all_same(self):
        self.assertEqual(self.run_case([7, 7, 7, 7, 7]), [7])

    def test_no_duplicates(self):
        self.assertEqual(self.run_case([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_duplicates_at_end(self):
        self.assertEqual(self.run_case([1, 2, 3, 3, 3]), [1, 2, 3])

    def test_duplicates_at_start(self):
        self.assertEqual(self.run_case([0, 0, 0, 1]), [0, 1])

    def test_negative_values(self):
        self.assertEqual(self.run_case([-100, -5, -5, 0, 0, 100]), [-100, -5, 0, 100])

    def test_all_negative_duplicates(self):
        self.assertEqual(self.run_case([-3, -3, -3]), [-3])

    def test_zero_only_duplicates(self):
        self.assertEqual(self.run_case([0, 0]), [0])

    def test_consecutive_groups(self):
        self.assertEqual(self.run_case([1, 1, 2, 2, 3, 3, 4]), [1, 2, 3, 4])

    def test_interleaved_duplicates(self):
        self.assertEqual(self.run_case([1, 2, 2, 3, 4, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_bound_values(self):
        self.assertEqual(self.run_case([-100, -100, 100, 100]), [-100, 100])

    def test_long_sorted_list(self):
        values = list(range(0, 300, 3))
        duplicated = []
        for v in values:
            duplicated.extend([v, v])
        self.assertEqual(self.run_case(duplicated), values)


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List
