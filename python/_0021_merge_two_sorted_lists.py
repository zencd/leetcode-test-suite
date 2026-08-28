# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Easy

import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def build(self, values):
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

    def to_list(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_both_empty(self):
        self.assertIsNone(self.solution.mergeTwoLists(None, None))

    def test_first_empty(self):
        result = self.solution.mergeTwoLists(None, self.build([0]))
        self.assertEqual(self.to_list(result), [0])

    def test_second_empty(self):
        result = self.solution.mergeTwoLists(self.build([5, 7]), None)
        self.assertEqual(self.to_list(result), [5, 7])

    def test_example_one(self):
        l1 = self.build([1, 2, 4])
        l2 = self.build([1, 3, 4])
        self.assertEqual(
            self.to_list(self.solution.mergeTwoLists(l1, l2)), [1, 1, 2, 3, 4, 4]
        )

    def test_single_nodes(self):
        result = self.solution.mergeTwoLists(self.build([1]), self.build([2]))
        self.assertEqual(self.to_list(result), [1, 2])

    def test_identical_nodes(self):
        result = self.solution.mergeTwoLists(self.build([3]), self.build([3]))
        self.assertEqual(self.to_list(result), [3, 3])

    def test_all_equal_values(self):
        l1 = self.build([2, 2, 2])
        l2 = self.build([2, 2])
        self.assertEqual(
            self.to_list(self.solution.mergeTwoLists(l1, l2)), [2, 2, 2, 2, 2]
        )

    def test_negative_values(self):
        l1 = self.build([-100, -10, -1])
        l2 = self.build([-50, -5, 0])
        self.assertEqual(
            self.to_list(self.solution.mergeTwoLists(l1, l2)),
            [-100, -50, -10, -5, -1, 0],
        )

    def test_disjoint_ranges(self):
        l1 = self.build([1, 2, 3])
        l2 = self.build([4, 5, 6])
        self.assertEqual(
            self.to_list(self.solution.mergeTwoLists(l1, l2)), [1, 2, 3, 4, 5, 6]
        )

    def test_reversed_disjoint_ranges(self):
        l1 = self.build([4, 5, 6])
        l2 = self.build([1, 2, 3])
        self.assertEqual(
            self.to_list(self.solution.mergeTwoLists(l1, l2)), [1, 2, 3, 4, 5, 6]
        )

    def test_interleaved_values(self):
        l1 = self.build([1, 3, 5])
        l2 = self.build([2, 4, 6])
        self.assertEqual(
            self.to_list(self.solution.mergeTwoLists(l1, l2)), [1, 2, 3, 4, 5, 6]
        )

    def test_one_longer_than_other(self):
        l1 = self.build([1, 3, 5, 7, 9, 11])
        l2 = self.build([2, 4])
        self.assertEqual(
            self.to_list(self.solution.mergeTwoLists(l1, l2)), [1, 2, 3, 4, 5, 7, 9, 11]
        )

    def test_extreme_bounds(self):
        l1 = self.build([-100, -100, 100])
        l2 = self.build([-100, 100, 100])
        self.assertEqual(
            self.to_list(self.solution.mergeTwoLists(l1, l2)),
            [-100, -100, -100, 100, 100, 100],
        )

    def test_nodes_are_spliced_not_copied(self):
        l1 = self.build([1])
        l2 = self.build([2])
        merged = self.solution.mergeTwoLists(l1, l2)
        self.assertIs(merged, l1)
        self.assertIs(merged.next, l2)

    def test_max_size_lists(self):
        l1 = self.build(list(range(-25, 25, 1)))
        l2 = self.build(list(range(-24, 25, 1)))
        expected = sorted(list(range(-25, 25)) + list(range(-24, 25)))
        self.assertEqual(self.to_list(self.solution.mergeTwoLists(l1, l2)), expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Recursion
