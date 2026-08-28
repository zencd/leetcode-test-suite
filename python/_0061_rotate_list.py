# 61. Rotate List
# https://leetcode.com/problems/rotate-list/
# Medium

from typing import Optional
import unittest


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
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        raise Exception("Not solved yet")


class TestRotateRight(unittest.TestCase):
    def test_example1(self):
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(to_list(Solution().rotateRight(head, 2)), [4, 5, 1, 2, 3])

    def test_example2(self):
        head = build_list([0, 1, 2])
        self.assertEqual(to_list(Solution().rotateRight(head, 4)), [2, 0, 1])

    def test_empty_list(self):
        self.assertIsNone(Solution().rotateRight(None, 5))

    def test_single_node(self):
        head = build_list([7])
        out = Solution().rotateRight(head, 3)
        self.assertEqual(to_list(out), [7])
        self.assertIs(out, head)

    def test_k_zero(self):
        head = build_list([1, 2, 3])
        out = Solution().rotateRight(head, 0)
        self.assertIs(out, head)

    def test_k_equals_length(self):
        head = build_list([1, 2, 3])
        out = Solution().rotateRight(head, 3)
        self.assertIs(out, head)
        self.assertEqual(to_list(out), [1, 2, 3])

    def test_k_multiple_of_length(self):
        head = build_list([1, 2, 3, 4])
        out = Solution().rotateRight(head, 8)
        self.assertIs(out, head)

    def test_rotate_by_one(self):
        head = build_list([1, 2, 3, 4])
        self.assertEqual(to_list(Solution().rotateRight(head, 1)), [4, 1, 2, 3])

    def test_rotate_full_by_length_minus_one(self):
        head = build_list([1, 2, 3])
        self.assertEqual(to_list(Solution().rotateRight(head, 2)), [2, 3, 1])

    def test_two_nodes(self):
        head = build_list([1, 2])
        self.assertEqual(to_list(Solution().rotateRight(head, 1)), [2, 1])

    def test_two_nodes_even_k(self):
        head = build_list([1, 2])
        out = Solution().rotateRight(head, 4)
        self.assertEqual(to_list(out), [1, 2])

    def test_negative_valued_nodes(self):
        head = build_list([-100, 0, 100])
        self.assertEqual(to_list(Solution().rotateRight(head, 2)), [0, 100, -100])

    def test_large_k(self):
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(
            to_list(Solution().rotateRight(head, 2 * 10**9 % 5 + 2)), [4, 5, 1, 2, 3]
        )

    def test_k_bigger_than_length(self):
        head = build_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(to_list(Solution().rotateRight(head, 7)), [6, 1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Two Pointers
