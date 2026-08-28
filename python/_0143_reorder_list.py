# 143. Reorder List
# https://leetcode.com/problems/reorder-list/
# Medium

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        raise Exception("Not solved yet")


def build_list(values):
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def check(self, values, expected):
        head = build_list(values)
        self.sol.reorderList(head)
        self.assertEqual(to_list(head), expected)

    def test_empty(self):
        self.assertIsNone(build_list([]))
        self.sol.reorderList(None)

    def test_single_node(self):
        self.check([1], [1])

    def test_two_nodes(self):
        self.check([1, 2], [1, 2])

    def test_three_nodes(self):
        self.check([1, 2, 3], [1, 3, 2])

    def test_example1(self):
        self.check([1, 2, 3, 4], [1, 4, 2, 3])

    def test_example2(self):
        self.check([1, 2, 3, 4, 5], [1, 5, 2, 4, 3])

    def test_even_length_six(self):
        self.check([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4])

    def test_odd_length_seven(self):
        self.check([1, 2, 3, 4, 5, 6, 7], [1, 7, 2, 6, 3, 5, 4])

    def test_even_length_eight(self):
        self.check(list(range(1, 9)), [1, 8, 2, 7, 3, 6, 4, 5])

    def test_odd_length_nine(self):
        self.check(list(range(1, 10)), [1, 9, 2, 8, 3, 7, 4, 6, 5])

    def test_values_not_modified(self):
        vals = [10, 20, 30, 40, 50]
        head = build_list(vals)
        self.sol.reorderList(head)
        got = to_list(head)
        self.assertEqual(sorted(got), vals)

    def test_large_list(self):
        vals = list(range(1, 101))
        head = build_list(vals)
        self.sol.reorderList(head)
        got = to_list(head)
        n = len(vals)
        expected = []
        i, j = 0, n - 1
        left = True
        while i <= j:
            if left:
                expected.append(vals[i])
                i += 1
            else:
                expected.append(vals[j])
                j -= 1
            left = not left
        self.assertEqual(got, expected)

    def test_no_cycle_created(self):
        vals = [1, 2, 3, 4, 5, 6, 7]
        head = build_list(vals)
        self.sol.reorderList(head)
        seen = set()
        cur = head
        while cur:
            self.assertNotIn(id(cur), seen)
            seen.add(id(cur))
            cur = cur.next
        self.assertEqual(len(seen), len(vals))

    def test_constraint_values(self):
        head = build_list([1, 1000])
        self.sol.reorderList(head)
        self.assertEqual(to_list(head), [1, 1000])

    def test_duplicate_values(self):
        self.check([5, 5, 5, 5], [5, 5, 5, 5])


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Two Pointers, Stack, Recursion
