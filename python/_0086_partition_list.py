# 86. Partition List
# https://leetcode.com/problems/partition-list/
# Medium

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        raise Exception("Not solved yet")


def to_list(head):
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result


def to_linked_list(values):
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


import unittest


class TestPartitionList(unittest.TestCase):
    def test_example_1(self):
        head = to_linked_list([1, 4, 3, 2, 5, 2])
        result = Solution().partition(head, 3)
        self.assertEqual(to_list(result), [1, 2, 2, 4, 3, 5])

    def test_example_2(self):
        head = to_linked_list([2, 1])
        result = Solution().partition(head, 2)
        self.assertEqual(to_list(result), [1, 2])

    def test_empty_list(self):
        self.assertIsNone(Solution().partition(None, 3))

    def test_single_node_less_than_x(self):
        head = to_linked_list([1])
        result = Solution().partition(head, 3)
        self.assertEqual(to_list(result), [1])

    def test_single_node_equal_x(self):
        head = to_linked_list([3])
        result = Solution().partition(head, 3)
        self.assertEqual(to_list(result), [3])

    def test_single_node_greater_than_x(self):
        head = to_linked_list([5])
        result = Solution().partition(head, 3)
        self.assertEqual(to_list(result), [5])

    def test_all_less_than_x(self):
        head = to_linked_list([1, 2, 3])
        result = Solution().partition(head, 4)
        self.assertEqual(to_list(result), [1, 2, 3])

    def test_all_greater_than_x(self):
        head = to_linked_list([4, 5, 6])
        result = Solution().partition(head, 3)
        self.assertEqual(to_list(result), [4, 5, 6])

    def test_all_equal_to_x(self):
        head = to_linked_list([3, 3, 3])
        result = Solution().partition(head, 3)
        self.assertEqual(to_list(result), [3, 3, 3])

    def test_x_smallest(self):
        head = to_linked_list([1, 2, 3])
        result = Solution().partition(head, 1)
        self.assertEqual(to_list(result), [1, 2, 3])

    def test_x_largest(self):
        head = to_linked_list([1, 2, 3])
        result = Solution().partition(head, 4)
        self.assertEqual(to_list(result), [1, 2, 3])

    def test_negative_values(self):
        head = to_linked_list([-2, 1, -1, 0, 2])
        result = Solution().partition(head, 0)
        self.assertEqual(to_list(result), [-2, -1, 1, 0, 2])

    def test_negative_x(self):
        head = to_linked_list([1, -1, 2, -2, 0])
        result = Solution().partition(head, -1)
        self.assertEqual(to_list(result), [-2, 1, -1, 2, 0])

    def test_duplicates_across_partition(self):
        head = to_linked_list([2, 2, 1, 2, 1])
        result = Solution().partition(head, 2)
        self.assertEqual(to_list(result), [1, 1, 2, 2, 2])

    def test_relative_order_preserved_less(self):
        head = to_linked_list([3, 1, 5, 2, 4])
        result = Solution().partition(head, 3)
        self.assertEqual(to_list(result), [1, 2, 3, 5, 4])

    def test_relative_order_preserved_greater(self):
        head = to_linked_list([5, 3, 4, 2, 6])
        result = Solution().partition(head, 3)
        self.assertEqual(to_list(result), [2, 5, 3, 4, 6])

    def test_values_at_boundaries(self):
        head = to_linked_list([-100, 100, -100, 100])
        result = Solution().partition(head, 0)
        self.assertEqual(to_list(result), [-100, -100, 100, 100])

    def test_two_elements(self):
        head = to_linked_list([1, 2])
        result = Solution().partition(head, 2)
        self.assertEqual(to_list(result), [1, 2])

    def test_two_elements_split(self):
        head = to_linked_list([3, 1])
        result = Solution().partition(head, 2)
        self.assertEqual(to_list(result), [1, 3])


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Two Pointers
