# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/
# Easy

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        raise Exception("Not solved yet")


import unittest


def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_node(self):
        head = build_list([1])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_two_nodes_palindrome(self):
        head = build_list([1, 1])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_two_nodes_not_palindrome(self):
        head = build_list([1, 2])
        self.assertFalse(self.solution.isPalindrome(head))

    def test_example_one(self):
        head = build_list([1, 2, 2, 1])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_example_two(self):
        head = build_list([1, 2])
        self.assertFalse(self.solution.isPalindrome(head))

    def test_three_nodes_palindrome(self):
        head = build_list([1, 2, 1])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_three_nodes_not_palindrome(self):
        head = build_list([1, 2, 3])
        self.assertFalse(self.solution.isPalindrome(head))

    def test_five_nodes_palindrome(self):
        head = build_list([1, 2, 3, 2, 1])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_five_nodes_not_palindrome(self):
        head = build_list([1, 2, 3, 4, 5])
        self.assertFalse(self.solution.isPalindrome(head))

    def test_all_same_even(self):
        head = build_list([7, 7, 7, 7])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_all_same_odd(self):
        head = build_list([9, 9, 9])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_zeros(self):
        head = build_list([0, 0, 0])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_zero_mismatch(self):
        head = build_list([0, 1, 0])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_zero_mismatch_false(self):
        head = build_list([0, 1, 2])
        self.assertFalse(self.solution.isPalindrome(head))

    def test_long_palindrome(self):
        values = list(range(1, 101)) + list(range(99, 0, -1))
        head = build_list(values)
        self.assertTrue(self.solution.isPalindrome(head))

    def test_long_not_palindrome(self):
        values = list(range(1, 201))
        head = build_list(values)
        self.assertFalse(self.solution.isPalindrome(head))

    def test_long_mismatch_in_middle(self):
        values = [1, 2, 3, 9, 3, 2, 1]
        head = build_list(values)
        self.assertTrue(self.solution.isPalindrome(head))

    def test_long_mismatch_at_ends(self):
        values = [1, 2, 3, 4, 5]
        head = build_list(values)
        self.assertFalse(self.solution.isPalindrome(head))

    def test_list_restored(self):
        values = [1, 2, 3, 2, 1]
        head = build_list(values)
        self.assertTrue(self.solution.isPalindrome(head))
        self.assertEqual(to_list(head), values)

    def test_list_restored_false(self):
        values = [1, 2, 3, 4]
        head = build_list(values)
        self.assertFalse(self.solution.isPalindrome(head))
        self.assertEqual(to_list(head), values)


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Two Pointers, Stack, Recursion
