# 25. Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Hard

import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        raise Exception("Not solved yet")


def build_list(values):
    head = None
    tail = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def to_list(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


class TestReverseKGroup(unittest.TestCase):
    def test_single_node(self):
        head = build_list([1])
        result = Solution().reverseKGroup(head, 1)
        self.assertEqual(to_list(result), [1])

    def test_two_nodes_k_1(self):
        head = build_list([1, 2])
        result = Solution().reverseKGroup(head, 1)
        self.assertEqual(to_list(result), [1, 2])

    def test_two_nodes_k_2(self):
        head = build_list([1, 2])
        result = Solution().reverseKGroup(head, 2)
        self.assertEqual(to_list(result), [2, 1])

    def test_five_nodes_k_2(self):
        head = build_list([1, 2, 3, 4, 5])
        result = Solution().reverseKGroup(head, 2)
        self.assertEqual(to_list(result), [2, 1, 4, 3, 5])

    def test_five_nodes_k_3(self):
        head = build_list([1, 2, 3, 4, 5])
        result = Solution().reverseKGroup(head, 3)
        self.assertEqual(to_list(result), [3, 2, 1, 4, 5])

    def test_five_nodes_k_5(self):
        head = build_list([1, 2, 3, 4, 5])
        result = Solution().reverseKGroup(head, 5)
        self.assertEqual(to_list(result), [5, 4, 3, 2, 1])

    def test_equal_values(self):
        head = build_list([3, 3, 3, 3])
        result = Solution().reverseKGroup(head, 2)
        self.assertEqual(to_list(result), [3, 3, 3, 3])

    def test_exact_multiple_k(self):
        head = build_list([1, 2, 3, 4, 5, 6])
        result = Solution().reverseKGroup(head, 3)
        self.assertEqual(to_list(result), [3, 2, 1, 6, 5, 4])

    def test_exact_multiple_k_2(self):
        head = build_list([1, 2, 3, 4, 5, 6, 7, 8])
        result = Solution().reverseKGroup(head, 4)
        self.assertEqual(to_list(result), [4, 3, 2, 1, 8, 7, 6, 5])

    def test_all_nodes_k(self):
        head = build_list([9, 8, 7])
        result = Solution().reverseKGroup(head, 3)
        self.assertEqual(to_list(result), [7, 8, 9])

    def test_longer_list_k_2(self):
        head = build_list([1, 2, 3, 4, 5, 6, 7])
        result = Solution().reverseKGroup(head, 2)
        self.assertEqual(to_list(result), [2, 1, 4, 3, 6, 5, 7])

    def test_zero_values(self):
        head = build_list([0, 0, 0])
        result = Solution().reverseKGroup(head, 2)
        self.assertEqual(to_list(result), [0, 0, 0])

    def test_k_one_no_change(self):
        head = build_list([1, 2, 3, 4])
        result = Solution().reverseKGroup(head, 1)
        self.assertEqual(to_list(result), [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Recursion
