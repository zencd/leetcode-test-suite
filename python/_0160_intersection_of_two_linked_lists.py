# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Easy

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        raise Exception("Not solved yet")


def build(values):
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head, tail


def build_intersecting(valuesA, valuesB, tail_values):
    shared_head, _ = build(tail_values) if tail_values else (None, None)
    headA, tailA = build(valuesA)
    headB, tailB = build(valuesB)
    if shared_head is None:
        return headA, headB
    if tailA is None:
        headA = shared_head
    else:
        tailA.next = shared_head
    if tailB is None:
        headB = shared_head
    else:
        tailB.next = shared_head
    return headA, headB


def find_node(head, index):
    cur = head
    for _ in range(index):
        cur = cur.next
    return cur


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def to_list(self, head, limit=1000):
        out = []
        cur = head
        while cur and len(out) < limit:
            out.append(cur.val)
            cur = cur.next
        return out

    def test_returns_none_when_both_lists_disjoint(self):
        a = build([1, 2, 3])[0]
        b = build([4, 5, 6])[0]
        self.assertIsNone(self.sol.getIntersectionNode(a, b))

    def test_examples_from_problem(self):
        headA, headB = build_intersecting([4, 1], [5, 6, 1], [8, 4, 5])
        self.assertEqual(self.sol.getIntersectionNode(headA, headB).val, 8)
        headA, headB = build_intersecting([1, 9, 1], [3], [2, 4])
        self.assertEqual(self.sol.getIntersectionNode(headA, headB).val, 2)

    def test_disjoint_lists_return_none(self):
        headA, headB = build_intersecting([2, 6, 4], [1, 5], [])
        self.assertIsNone(self.sol.getIntersectionNode(headA, headB))

    def test_intersection_at_head_of_both_lists(self):
        a = [10, 11, 12]
        shared_head, _ = build(a)
        self.assertIs(
            self.sol.getIntersectionNode(shared_head, shared_head), shared_head
        )

    def test_intersection_at_tail_of_both_lists(self):
        headA, headB = build_intersecting([1, 2], [3, 4], [9])
        node = self.sol.getIntersectionNode(headA, headB)
        self.assertEqual(node.val, 9)
        self.assertIsNone(node.next)

    def test_single_node_lists_intersecting(self):
        headA, headB = build_intersecting([], [], [7])
        self.assertEqual(self.sol.getIntersectionNode(headA, headB).val, 7)

    def test_single_node_lists_disjoint(self):
        a = build([7])[0]
        b = build([8])[0]
        self.assertIsNone(self.sol.getIntersectionNode(a, b))

    def test_long_lists_intersect_at_end(self):
        vals_a = list(range(1, 30001, 3))
        vals_b = list(range(2, 30002, 3))
        headA, headB = build_intersecting(vals_a, vals_b, [30000])
        node = self.sol.getIntersectionNode(headA, headB)
        self.assertEqual(node.val, 30000)
        self.assertIsNone(node.next)

    def test_one_list_shorter(self):
        headA, headB = build_intersecting([5], [1, 2, 3, 4], [10])
        self.assertEqual(self.sol.getIntersectionNode(headA, headB).val, 10)

    def test_other_list_shorter(self):
        headA, headB = build_intersecting([1, 2, 3, 4], [5], [10])
        self.assertEqual(self.sol.getIntersectionNode(headA, headB).val, 10)

    def test_same_length_lists(self):
        headA, headB = build_intersecting([1, 2, 3], [4, 5, 6], [20, 21])
        self.assertEqual(self.sol.getIntersectionNode(headA, headB).val, 20)

    def test_original_structure_preserved(self):
        headA, headB = build_intersecting([1, 2], [3], [9, 10])
        expected_a = self.to_list(headA)
        expected_b = self.to_list(headB)
        self.sol.getIntersectionNode(headA, headB)
        self.assertEqual(self.to_list(headA), expected_a)
        self.assertEqual(self.to_list(headB), expected_b)

    def test_duplicate_values_no_false_positive(self):
        a = build([1, 2, 3])[0]
        b = build([3, 4, 5])[0]
        self.assertIsNone(self.sol.getIntersectionNode(a, b))

    def test_identical_lists(self):
        headA, headB = build_intersecting([], [], [5, 6, 7, 8])
        first = find_node(headA, 0)
        node = self.sol.getIntersectionNode(headA, headB)
        self.assertIs(node, first)

    def test_tail_reuse_identical_head(self):
        head, tail = build([1, 2, 3])
        self.assertIs(self.sol.getIntersectionNode(head, head), head)

    def test_empty_head_returns_none(self):
        b = build([1, 2])[0]
        self.assertIsNone(self.sol.getIntersectionNode(None, b))
        self.assertIsNone(self.sol.getIntersectionNode(b, None))
        self.assertIsNone(self.sol.getIntersectionNode(None, None))

    def test_large_disjoint_lists(self):
        a_vals = [i % 1000 for i in range(30000)]
        b_vals = [i % 999 + 1 for i in range(30000)]
        a = build(a_vals)[0]
        b = build(b_vals)[0]
        self.assertIsNone(self.sol.getIntersectionNode(a, b))


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Linked List, Two Pointers
