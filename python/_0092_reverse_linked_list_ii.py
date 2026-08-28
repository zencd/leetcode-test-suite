# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/
# Medium

from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
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
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def check(self, values, left, right, expected):
        head = build_list(values)
        result = self.sol.reverseBetween(head, left, right)
        self.assertEqual(to_list(result), expected)

    def test_example1(self):
        self.check([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5])

    def test_example2_single_node(self):
        self.check([5], 1, 1, [5])

    def test_reverse_entire_list(self):
        self.check([1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1])

    def test_reverse_from_head(self):
        self.check([1, 2, 3, 4, 5], 1, 3, [3, 2, 1, 4, 5])

    def test_reverse_at_tail(self):
        self.check([1, 2, 3, 4, 5], 4, 5, [1, 2, 3, 5, 4])

    def test_reverse_last_two(self):
        self.check([1, 2], 1, 2, [2, 1])

    def test_reverse_two_nodes_tail(self):
        self.check([1, 2], 2, 2, [1, 2])

    def test_reverse_single_middle_element(self):
        self.check([1, 2, 3, 4], 2, 2, [1, 2, 3, 4])

    def test_reverse_single_first_element(self):
        self.check([1, 2, 3], 1, 1, [1, 2, 3])

    def test_reverse_single_last_element(self):
        self.check([1, 2, 3], 3, 3, [1, 2, 3])

    def test_negative_values(self):
        self.check([-1, -2, -3, -4], 2, 3, [-1, -3, -2, -4])

    def test_duplicate_values(self):
        self.check([1, 1, 1, 1], 2, 3, [1, 1, 1, 1])

    def test_mixed_values(self):
        self.check([0, -500, 500, 0], 1, 4, [0, 500, -500, 0])

    def test_adjacent_two_nodes(self):
        self.check([1, 3, 5], 2, 3, [1, 5, 3])

    def test_large_list_middle_segment(self):
        values = list(range(1, 21))
        result_vals = values[:4] + values[10:3:-1] + values[11:]
        self.check(values, 5, 11, result_vals)

    def test_head_preserved_when_left_gt_1(self):
        head = build_list([10, 20, 30])
        result = self.sol.reverseBetween(head, 2, 3)
        self.assertEqual(to_list(result), [10, 30, 20])
        self.assertIsNotNone(result)
        self.assertIs(result, head)

    def test_head_is_replaced_when_left_eq_1(self):
        head = build_list([10, 20, 30])
        result = self.sol.reverseBetween(head, 1, 3)
        self.assertEqual(to_list(result), [30, 20, 10])
        self.assertIsNot(result, head)

    def test_no_cycles_created(self):
        head = build_list([1, 2, 3, 4])
        result = self.sol.reverseBetween(head, 2, 4)
        seen = set()
        node = result
        while node:
            self.assertNotIn(id(node), seen)
            seen.add(id(node))
            node = node.next
        self.assertEqual(len(seen), 4)

    def test_returns_correct_node_count(self):
        for n in range(1, 6):
            values = list(range(n))
            head = build_list(values)
            result = self.sol.reverseBetween(head, 1, n)
            self.assertEqual(len(to_list(result)), n)


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List
