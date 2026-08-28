# 147. Insertion Sort List
# https://leetcode.com/problems/insertion-sort-list/
# Medium

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        raise Exception("Not solved yet")


def build_list(values):
    dummy = ListNode(0)
    node = dummy
    for val in values:
        node.next = ListNode(val)
        node = node.next
    return dummy.next


def to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_node(self):
        self.assertEqual(to_list(self.sol.insertionSortList(build_list([5]))), [5])

    def test_two_nodes_sorted(self):
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list([1, 2]))), [1, 2]
        )

    def test_two_nodes_unsorted(self):
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list([2, 1]))), [1, 2]
        )

    def test_example1(self):
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list([4, 2, 1, 3]))), [1, 2, 3, 4]
        )

    def test_example2(self):
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list([-1, 5, 3, 4, 0]))),
            [-1, 0, 3, 4, 5],
        )

    def test_already_sorted(self):
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list([1, 2, 3, 4, 5]))),
            [1, 2, 3, 4, 5],
        )

    def test_reverse_sorted(self):
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list([5, 4, 3, 2, 1]))),
            [1, 2, 3, 4, 5],
        )

    def test_all_duplicates(self):
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list([7, 7, 7, 7]))), [7, 7, 7, 7]
        )

    def test_with_duplicates(self):
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list([3, 1, 2, 1, 3, 2]))),
            [1, 1, 2, 2, 3, 3],
        )

    def test_negative_values(self):
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list([-3, -1, -2, -5, 0]))),
            [-5, -3, -2, -1, 0],
        )

    def test_mixed_duplicates(self):
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list([0, 0, -1, 0, -1]))),
            [-1, -1, 0, 0, 0],
        )

    def test_min_max_values(self):
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list([5000, -5000, 0]))),
            [-5000, 0, 5000],
        )

    def test_first_element_smallest(self):
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list([1, 3, 2, 5, 4]))),
            [1, 2, 3, 4, 5],
        )

    def test_first_element_largest(self):
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list([9, 1, 2, 3, 4]))),
            [1, 2, 3, 4, 9],
        )

    def test_last_insertion_at_front(self):
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list([2, 3, 4, 1]))), [1, 2, 3, 4]
        )

    def test_large_random(self):
        import random

        random.seed(42)
        values = [random.randint(-5000, 5000) for _ in range(100)]
        self.assertEqual(
            to_list(self.sol.insertionSortList(build_list(values))), sorted(values)
        )

    def test_stability_preserves_node_order_for_equal_values(self):
        a = ListNode(2, ListNode(2, ListNode(1)))
        head = a
        result = self.sol.insertionSortList(head)
        self.assertEqual(to_list(result), [1, 2, 2])
        self.assertIsNot(result.next, result.next.next)

    def test_returns_new_head_when_first_moved(self):
        head = build_list([3, 1, 2])
        result = self.sol.insertionSortList(head)
        self.assertIsNot(result, head)
        self.assertEqual(to_list(result), [1, 2, 3])

    def test_returns_same_head_when_already_sorted(self):
        head = build_list([1, 2, 3])
        result = self.sol.insertionSortList(head)
        self.assertIs(result, head)


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Sorting
