# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/
# Hard

import heapq
import itertools
import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        raise Exception("Not solved yet")


def build_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


class TestMergeKLists(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty_lists(self):
        self.assertIsNone(self.s.mergeKLists([]))

    def test_list_of_one_empty_list(self):
        self.assertIsNone(self.s.mergeKLists([None]))

    def test_single_list(self):
        head = build_list([1, 2, 3])
        self.assertEqual(to_list(self.s.mergeKLists([head])), [1, 2, 3])

    def test_single_node_lists(self):
        heads = [build_list([v]) for v in [3, 1, 2]]
        self.assertEqual(to_list(self.s.mergeKLists(heads)), [1, 2, 3])

    def test_example1(self):
        lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
        self.assertEqual(to_list(self.s.mergeKLists(lists)), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_two_lists(self):
        lists = [build_list([1, 3, 5]), build_list([2, 4, 6])]
        self.assertEqual(to_list(self.s.mergeKLists(lists)), [1, 2, 3, 4, 5, 6])

    def test_duplicates(self):
        lists = [build_list([1, 1, 1]), build_list([1, 1]), build_list([1])]
        self.assertEqual(to_list(self.s.mergeKLists(lists)), [1] * 6)

    def test_negative_values(self):
        lists = [build_list([-5, -1, 3]), build_list([-4, 0, 2])]
        self.assertEqual(to_list(self.s.mergeKLists(lists)), [-5, -4, -1, 0, 2, 3])

    def test_mixed_signs(self):
        lists = [build_list([-2, 0, 2]), build_list([-1, 1])]
        self.assertEqual(to_list(self.s.mergeKLists(lists)), [-2, -1, 0, 1, 2])

    def test_identical_lists(self):
        lists = [build_list([1, 2, 3]) for _ in range(4)]
        self.assertEqual(
            to_list(self.s.mergeKLists(lists)), [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
        )

    def test_many_lists(self):
        lists = [build_list([10 - i]) for i in range(10)]
        expected = list(range(1, 11))
        self.assertEqual(to_list(self.s.mergeKLists(lists)), expected)

    def test_one_list_long(self):
        values = list(range(1, 101))
        head = build_list(values)
        self.assertEqual(to_list(self.s.mergeKLists([head])), list(range(1, 101)))

    def test_unsorted_input_not_merged(self):
        lists = [build_list([1, 2, 3]), build_list([4, 5, 6])]
        self.assertEqual(to_list(self.s.mergeKLists(lists)), [1, 2, 3, 4, 5, 6])

    def test_already_in_order_lists(self):
        lists = [build_list([1, 2]), build_list([3, 4]), build_list([5, 6])]
        self.assertEqual(to_list(self.s.mergeKLists(lists)), [1, 2, 3, 4, 5, 6])

    def test_reverse_order_lists(self):
        lists = [build_list([5, 6]), build_list([3, 4]), build_list([1, 2])]
        self.assertEqual(to_list(self.s.mergeKLists(lists)), [1, 2, 3, 4, 5, 6])

    def test_empty_list_among_others(self):
        lists = [build_list([1, 2]), None, build_list([3, 4])]
        self.assertEqual(to_list(self.s.mergeKLists(lists)), [1, 2, 3, 4])

    def test_all_empty_and_mixed(self):
        lists = [None, None, build_list([7]), None]
        self.assertEqual(to_list(self.s.mergeKLists(lists)), [7])

    def test_large_values(self):
        lists = [build_list([-10000, 10000]), build_list([0])]
        self.assertEqual(to_list(self.s.mergeKLists(lists)), [-10000, 0, 10000])


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort, Tournament Sort
