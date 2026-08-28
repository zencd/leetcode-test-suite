# 237. Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/
# Medium

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        raise Exception("Not solved yet")


def build_list(values):
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(node):
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


def find_node(head, val):
    cur = head
    while cur is not None:
        if cur.val == val:
            return cur
        cur = cur.next
    return None


import unittest


class TestSolution(unittest.TestCase):
    def test_delete_middle_node(self):
        head = build_list([4, 5, 1, 9])
        node = find_node(head, 5)
        Solution().deleteNode(node)
        self.assertEqual(to_list(head), [4, 1, 9])

    def test_delete_node_example2(self):
        head = build_list([4, 5, 1, 9])
        node = find_node(head, 1)
        Solution().deleteNode(node)
        self.assertEqual(to_list(head), [4, 5, 9])

    def test_delete_first_node(self):
        head = build_list([1, 2, 3])
        node = find_node(head, 1)
        Solution().deleteNode(node)
        self.assertEqual(to_list(head), [2, 3])

    def test_delete_second_to_last_node(self):
        head = build_list([1, 2, 3])
        node = find_node(head, 2)
        Solution().deleteNode(node)
        self.assertEqual(to_list(head), [1, 3])

    def test_delete_last_non_tail_node(self):
        head = build_list([7, 8, 9, 10])
        node = find_node(head, 9)
        Solution().deleteNode(node)
        self.assertEqual(to_list(head), [7, 8, 10])

    def test_two_node_list(self):
        head = build_list([1, 2])
        node = find_node(head, 1)
        Solution().deleteNode(node)
        self.assertEqual(to_list(head), [2])

    def test_negative_values(self):
        head = build_list([-1000, -500, 1000])
        node = find_node(head, -500)
        Solution().deleteNode(node)
        self.assertEqual(to_list(head), [-1000, 1000])

    def test_delete_node_with_zero_value(self):
        head = build_list([0, 1, 2])
        node = find_node(head, 0)
        Solution().deleteNode(node)
        self.assertEqual(to_list(head), [1, 2])

    def test_long_list(self):
        values = list(range(1000))
        head = build_list(values)
        node = find_node(head, 500)
        Solution().deleteNode(node)
        expected = values[:500] + values[501:]
        self.assertEqual(to_list(head), expected)

    def test_deleted_node_object_is_reused(self):
        head = build_list([1, 2, 3, 4])
        node = find_node(head, 2)
        Solution().deleteNode(node)
        self.assertEqual(node.val, 3)
        self.assertEqual(node.next.val, 4)

    def test_node_count_decreases(self):
        head = build_list([5, 6, 7])
        node = find_node(head, 6)
        Solution().deleteNode(node)
        count = 0
        cur = head
        while cur is not None:
            count += 1
            cur = cur.next
        self.assertEqual(count, 2)

    def test_all_preserved_order(self):
        head = build_list([10, 20, 30, 40, 50])
        node = find_node(head, 30)
        Solution().deleteNode(node)
        self.assertEqual(to_list(head), [10, 20, 40, 50])


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List
