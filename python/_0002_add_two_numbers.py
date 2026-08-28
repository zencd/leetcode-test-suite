# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# Medium

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
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
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def add(self, a, b):
        result = self.solution.addTwoNumbers(build_list(a), build_list(b))
        return to_list(result)

    def test_example1(self):
        self.assertEqual(self.add([2, 4, 3], [5, 6, 4]), [7, 0, 8])

    def test_example2_both_zero(self):
        self.assertEqual(self.add([0], [0]), [0])

    def test_example3_long_carry_chain(self):
        self.assertEqual(
            self.add([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]
        )

    def test_simple_no_carry(self):
        self.assertEqual(self.add([1], [2]), [3])

    def test_carry_produces_new_node(self):
        self.assertEqual(self.add([9], [1]), [0, 1])

    def test_different_length_l1_longer(self):
        self.assertEqual(self.add([9, 9, 9], [1]), [0, 0, 0, 1])

    def test_different_length_l2_longer(self):
        self.assertEqual(self.add([1], [9, 9, 9]), [0, 0, 0, 1])

    def test_carry_in_middle(self):
        self.assertEqual(self.add([5, 7], [5, 3]), [0, 1, 1])

    def test_multiple_carry_propagation(self):
        self.assertEqual(self.add([8, 9, 9], [2]), [0, 0, 0, 1])

    def test_no_carry_multi_digit(self):
        self.assertEqual(self.add([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_zero_plus_nonzero(self):
        self.assertEqual(self.add([0], [4, 5, 6]), [4, 5, 6])

    def test_nonzero_plus_zero(self):
        self.assertEqual(self.add([4, 5, 6], [0]), [4, 5, 6])

    def test_nine_plus_nine(self):
        self.assertEqual(self.add([9], [9]), [8, 1])

    def test_all_nines(self):
        self.assertEqual(self.add([9, 9, 9], [9, 9, 9]), [8, 9, 9, 1])

    def test_single_digit_values(self):
        self.assertEqual(self.add([0], [9]), [9])

    def test_very_large_numbers(self):
        a = [9] * 100
        b = [1]
        self.assertEqual(self.add(a, b), [0] * 100 + [1])

    def test_max_node_count_both(self):
        a = [5] * 100
        b = [5] * 100
        expected = [0] + [1] * 100
        self.assertEqual(self.add(a, b), expected)

    def test_carry_starts_from_second_digit(self):
        self.assertEqual(self.add([3, 9], [7]), [0, 0, 1])

    def test_result_not_mutated_inputs(self):
        l1 = build_list([2, 4, 3])
        l2 = build_list([5, 6, 4])
        snapshot1 = to_list(l1)
        snapshot2 = to_list(l2)
        self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(to_list(l1), snapshot1)
        self.assertEqual(to_list(l2), snapshot2)

    def test_result_is_linked_list_nodes(self):
        result = self.solution.addTwoNumbers(build_list([1]), build_list([2]))
        self.assertIsInstance(result, ListNode)
        self.assertEqual(result.val, 3)
        self.assertIsNone(result.next)

    def test_result_length_two_with_carry(self):
        result = self.solution.addTwoNumbers(build_list([5]), build_list([7]))
        self.assertEqual(to_list(result), [2, 1])


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Math, Recursion
