# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Medium

from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        raise Exception("Not solved yet")


def build_list(vals):
    head = None
    tail = None
    for v in vals:
        node = ListNode(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals


class TestRemoveNthFromEnd(unittest.TestCase):
    def test_example_1(self):
        head = build_list([1, 2, 3, 4, 5])
        result = Solution().removeNthFromEnd(head, 2)
        self.assertEqual(to_list(result), [1, 2, 3, 5])

    def test_example_2(self):
        head = build_list([1])
        result = Solution().removeNthFromEnd(head, 1)
        self.assertIsNone(result)

    def test_example_3(self):
        head = build_list([1, 2])
        result = Solution().removeNthFromEnd(head, 1)
        self.assertEqual(to_list(result), [1])

    def test_remove_head(self):
        head = build_list([1, 2, 3])
        result = Solution().removeNthFromEnd(head, 3)
        self.assertEqual(to_list(result), [2, 3])

    def test_remove_tail(self):
        head = build_list([1, 2, 3])
        result = Solution().removeNthFromEnd(head, 1)
        self.assertEqual(to_list(result), [1, 2])

    def test_two_nodes_remove_first(self):
        head = build_list([7, 9])
        result = Solution().removeNthFromEnd(head, 2)
        self.assertEqual(to_list(result), [9])

    def test_two_nodes_remove_second(self):
        head = build_list([7, 9])
        result = Solution().removeNthFromEnd(head, 1)
        self.assertEqual(to_list(result), [7])

    def test_middle_removal(self):
        head = build_list([1, 2, 3, 4])
        result = Solution().removeNthFromEnd(head, 2)
        self.assertEqual(to_list(result), [1, 2, 4])

    def test_middle_removal_4_nodes_n3(self):
        head = build_list([1, 2, 3, 4])
        result = Solution().removeNthFromEnd(head, 3)
        self.assertEqual(to_list(result), [1, 3, 4])

    def test_max_size_list(self):
        vals = list(range(30))
        head = build_list(vals)
        result = Solution().removeNthFromEnd(head, 15)
        self.assertEqual(to_list(result), vals[:15] + vals[16:])

    def test_single_node(self):
        head = build_list([42])
        result = Solution().removeNthFromEnd(head, 1)
        self.assertIsNone(result)

    def test_max_values(self):
        head = build_list([0, 100, 100])
        result = Solution().removeNthFromEnd(head, 3)
        self.assertEqual(to_list(result), [100, 100])

    def test_tail_severed(self):
        head = build_list([1, 2, 3])
        Solution().removeNthFromEnd(head, 1)
        self.assertEqual(to_list(head), [1, 2])
        self.assertIsNone(head.next.next)


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Two Pointers
