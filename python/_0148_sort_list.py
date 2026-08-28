# 148. Sort List
# https://leetcode.com/problems/sort-list/
# Medium

import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        raise Exception("Not solved yet")


def build(vals: List[int]) -> Optional[ListNode]:
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def sort(self, vals: List[int]) -> List[int]:
        return to_list(self.sol.sortList(build(vals)))

    def test_empty_list(self):
        self.assertEqual([], self.sort([]))
        self.assertIsNone(self.sol.sortList(None))

    def test_single_node(self):
        self.assertEqual([1], self.sort([1]))

    def test_two_nodes_ascending(self):
        self.assertEqual([1, 2], self.sort([1, 2]))

    def test_two_nodes_descending(self):
        self.assertEqual([1, 2], self.sort([2, 1]))

    def test_all_equal(self):
        self.assertEqual([5, 5, 5, 5], self.sort([5, 5, 5, 5]))

    def test_already_sorted(self):
        self.assertEqual([1, 2, 3, 4, 5], self.sort([1, 2, 3, 4, 5]))

    def test_reverse_sorted(self):
        self.assertEqual([1, 2, 3, 4, 5], self.sort([5, 4, 3, 2, 1]))

    def test_duplicates(self):
        self.assertEqual([1, 1, 2, 2, 3, 3, 3], self.sort([3, 2, 1, 1, 3, 2, 3]))

    def test_negative_values(self):
        self.assertEqual([-5, -3, -1, 2], self.sort([-3, -5, 2, -1]))

    def test_all_negative(self):
        self.assertEqual([-9, -8, -7], self.sort([-8, -7, -9]))

    def test_mixed_signs(self):
        self.assertEqual([-2, -1, 0, 1, 2], self.sort([0, 2, -1, -2, 1]))

    def test_zeros(self):
        self.assertEqual([0, 0, 0], self.sort([0, 0, 0]))

    def test_example1(self):
        self.assertEqual([1, 2, 3, 4], self.sort([4, 2, 1, 3]))

    def test_example2(self):
        self.assertEqual([-1, 0, 3, 4, 5], self.sort([-1, 5, 3, 4, 0]))

    def test_example3(self):
        self.assertEqual([], self.sort([]))

    def test_extreme_values(self):
        self.assertEqual([-100000, 2, 100000], self.sort([100000, -100000, 2]))

    def test_even_length(self):
        self.assertEqual([1, 2, 3, 4], self.sort([4, 1, 3, 2]))

    def test_odd_length(self):
        self.assertEqual([2, 3, 5], self.sort([5, 2, 3]))

    def test_many_nodes_random(self):
        import random

        random.seed(42)
        vals = [random.randint(-100000, 100000) for _ in range(1000)]
        self.assertEqual(sorted(vals), self.sort(vals))

    def test_alternating_values(self):
        self.assertEqual([-10, -10, 0, 10, 10], self.sort([10, -10, 10, -10, 0]))

    def test_returned_head_is_valid_node(self):
        head = build([3, 1, 2])
        res = self.sol.sortList(head)
        self.assertIsNotNone(res)
        self.assertEqual(res.val, 1)
        self.assertEqual(res.next.val, 2)
        self.assertEqual(res.next.next.val, 3)
        self.assertIsNone(res.next.next.next)

    def test_three_nodes(self):
        self.assertEqual([1, 2, 3], self.sort([2, 3, 1]))
        self.assertEqual([-1, 0, 1], self.sort([0, -1, 1]))

    def test_five_nodes_unsorted(self):
        self.assertEqual([1, 3, 4, 5, 9], self.sort([5, 1, 9, 3, 4]))

    def test_sorted_input_returns_sorted_list(self):
        self.assertEqual([1, 1, 2, 3], self.sort([2, 1, 1, 3]))


if __name__ == "__main__":
    unittest.main(verbosity=2)

# Tags: Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
