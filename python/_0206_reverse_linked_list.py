# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Easy

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        raise Exception("Not solved yet")


def make_list(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_list(self):
        self.assertIsNone(self.sol.reverseList(None))

    def test_single_node(self):
        head = make_list([5])
        self.assertEqual(to_list(self.sol.reverseList(head)), [5])

    def test_two_nodes(self):
        head = make_list([1, 2])
        self.assertEqual(to_list(self.sol.reverseList(head)), [2, 1])

    def test_example_one(self):
        head = make_list([1, 2, 3, 4, 5])
        self.assertEqual(to_list(self.sol.reverseList(head)), [5, 4, 3, 2, 1])

    def test_all_same_values(self):
        head = make_list([7, 7, 7])
        self.assertEqual(to_list(self.sol.reverseList(head)), [7, 7, 7])

    def test_negative_values(self):
        head = make_list([-5000, 0, 5000])
        self.assertEqual(to_list(self.sol.reverseList(head)), [5000, 0, -5000])

    def test_mixed_signs(self):
        head = make_list([1, -1, 2, -2, 3])
        self.assertEqual(to_list(self.sol.reverseList(head)), [3, -2, 2, -1, 1])

    def test_zero_values(self):
        head = make_list([0, 0])
        self.assertEqual(to_list(self.sol.reverseList(head)), [0, 0])

    def test_original_list_disconnected(self):
        head = make_list([1, 2, 3])
        new_head = self.sol.reverseList(head)
        self.assertEqual(head.next, None)
        self.assertEqual(to_list(new_head), [3, 2, 1])

    def test_many_nodes(self):
        values = list(range(1, 5001))
        head = make_list(values)
        self.assertEqual(to_list(self.sol.reverseList(head)), list(reversed(values)))

    def test_many_nodes_negative_range(self):
        values = list(range(-5000, 0))
        head = make_list(values)
        self.assertEqual(to_list(self.sol.reverseList(head)), list(reversed(values)))

    def test_recursive_variant_empty(self):
        self.assertIsNone(Solution()._reverse_recursive(None))

    def test_recursive_variant_single(self):
        head = make_list([9])
        self.assertEqual(to_list(Solution()._reverse_recursive(head)), [9])

    def test_recursive_variant_two(self):
        head = make_list([1, 2])
        self.assertEqual(to_list(Solution()._reverse_recursive(head)), [2, 1])

    def test_recursive_variant_example_one(self):
        head = make_list([1, 2, 3, 4, 5])
        self.assertEqual(to_list(Solution()._reverse_recursive(head)), [5, 4, 3, 2, 1])

    def test_recursive_variant_disconnected(self):
        head = make_list([1, 2, 3])
        new_head = Solution()._reverse_recursive(head)
        self.assertEqual(head.next, None)
        self.assertEqual(to_list(new_head), [3, 2, 1])

    def test_recursive_many_nodes(self):
        values = list(range(100, 0, -1))
        head = make_list(values)
        self.assertEqual(
            to_list(Solution()._reverse_recursive(head)), list(reversed(values))
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Recursion
