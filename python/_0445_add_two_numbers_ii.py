# 445. Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/
# Medium

from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    pass


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def add(self, l1_values, l2_values):
        l1 = build_list(l1_values)
        l2 = build_list(l2_values)
        return to_list(self.solution.addTwoNumbers(l1, l2))

    def test_example_1(self):
        self.assertEqual(self.add([7, 2, 4, 3], [5, 6, 4]), [7, 8, 0, 7])

    def test_example_2(self):
        self.assertEqual(self.add([2, 4, 3], [5, 6, 4]), [8, 0, 7])

    def test_example_3(self):
        self.assertEqual(self.add([0], [0]), [0])

    def test_equal_lengths_carry_through(self):
        self.assertEqual(self.add([9, 9], [1]), [1, 0, 0])

    def test_carries_all_positions(self):
        self.assertEqual(self.add([9, 9, 9], [1, 1, 1]), [1, 1, 1, 0])

    def test_cascading_carry(self):
        self.assertEqual(self.add([9, 5], [5]), [1, 0, 0])

    def test_single_digit_no_carry(self):
        self.assertEqual(self.add([1], [2]), [3])

    def test_single_digit_with_carry(self):
        self.assertEqual(self.add([9], [9]), [1, 8])

    def test_shorter_plus_longer(self):
        self.assertEqual(self.add([1], [5, 6, 4]), [5, 6, 5])

    def test_longer_plus_shorter(self):
        self.assertEqual(self.add([5, 6, 4], [1]), [5, 6, 5])

    def test_zeros_in_middle(self):
        self.assertEqual(self.add([1, 0, 0, 2], [3, 0, 0, 4]), [4, 0, 0, 6])

    def test_zero_plus_number(self):
        self.assertEqual(self.add([0], [1, 2, 3]), [1, 2, 3])

    def test_number_plus_zero(self):
        self.assertEqual(self.add([1, 2, 3], [0]), [1, 2, 3])

    def test_both_zeros(self):
        self.assertEqual(self.add([0], [0]), [0])

    def test_carry_into_new_most_significant_digit(self):
        self.assertEqual(self.add([5], [5]), [1, 0])

    def test_large_numbers(self):
        self.assertEqual(
            self.add([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [1]),
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        )

    def test_max_length_lists_no_carry(self):
        a = [1] * 100
        b = [2] * 100
        expected = []
        carry = 0
        for x, y in zip(a, b):
            s = x + y + carry
            expected.append(s % 10)
            carry = s // 10
        if carry:
            expected.append(carry)
        expected.reverse()
        self.assertEqual(self.add(a, b), expected)

    def test_result_preserves_list_structure(self):
        l1 = build_list([7, 2, 4, 3])
        l2 = build_list([5, 6, 4])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertIsInstance(result, ListNode)
        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 8)
        self.assertEqual(result.next.next.val, 0)
        self.assertEqual(result.next.next.next.val, 7)
        self.assertIsNone(result.next.next.next.next)

    def test_single_zeros_repeated(self):
        self.assertEqual(self.add([0], [0, 0, 0]), [0, 0, 0])


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Math, Stack
