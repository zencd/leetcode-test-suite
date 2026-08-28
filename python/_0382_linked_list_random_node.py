# 382. Linked List Random Node
# https://leetcode.com/problems/linked-list-random-node/
# Medium

import random
import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        raise Exception("Not solved yet")

    def getRandom(self) -> int:
        raise Exception("Not solved yet")


def build_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def list_to_values(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


class TestSolution(unittest.TestCase):
    def test_single_node(self):
        sol = Solution(build_list([42]))
        for _ in range(100):
            self.assertEqual(sol.getRandom(), 42)

    def test_two_nodes_values_in_range(self):
        sol = Solution(build_list([1, 2]))
        for _ in range(200):
            self.assertIn(sol.getRandom(), (1, 2))

    def test_three_nodes_all_values_reachable(self):
        sol = Solution(build_list([1, 2, 3]))
        seen = {sol.getRandom() for _ in range(500)}
        self.assertEqual(seen, {1, 2, 3})

    def test_result_always_from_list(self):
        values = list(range(1, 11)) + list(range(-10, 0))
        sol = Solution(build_list(values))
        for _ in range(500):
            self.assertIn(sol.getRandom(), values)

    def test_negative_values(self):
        sol = Solution(build_list([-5, -100, 0]))
        for _ in range(200):
            self.assertIn(sol.getRandom(), (-5, -100, 0))

    def test_zero_values(self):
        sol = Solution(build_list([0, 0]))
        for _ in range(50):
            self.assertEqual(sol.getRandom(), 0)

    def test_duplicate_values(self):
        sol = Solution(build_list([7, 7, 7]))
        for _ in range(50):
            self.assertEqual(sol.getRandom(), 7)

    def test_extreme_values(self):
        sol = Solution(build_list([-(10**4), 10**4, 0]))
        for _ in range(200):
            self.assertIn(sol.getRandom(), (-(10**4), 0, 10**4))

    def test_long_list(self):
        values = list(range(1, 1001))
        sol = Solution(build_list(values))
        sample = {sol.getRandom() for _ in range(500)}
        self.assertGreater(len(sample), 100)
        self.assertTrue(sample.issubset(values))

    def test_statistical_uniformity(self):
        random.seed(0)
        n = 10
        values = list(range(1, n + 1))
        sol = Solution(build_list(values))
        trials = 100_000
        counts = {v: 0 for v in values}
        for _ in range(trials):
            counts[sol.getRandom()] += 1
        for v in values:
            self.assertAlmostEqual(
                counts[v] / trials,
                1 / n,
                delta=0.02,
                msg=f"value {v} not equally likely: {counts[v] / trials}",
            )

    def test_getrandom_does_not_mutate_list(self):
        head = build_list([1, 2, 3, 4])
        sol = Solution(head)
        for _ in range(100):
            sol.getRandom()
        self.assertEqual(list_to_values(head), [1, 2, 3, 4])

    def test_multiple_instances_independent(self):
        sol_a = Solution(build_list([1, 2]))
        sol_b = Solution(build_list([9]))
        for _ in range(50):
            self.assertIn(sol_a.getRandom(), (1, 2))
            self.assertEqual(sol_b.getRandom(), 9)


if __name__ == "__main__":
    unittest.main()

# Tags: Linked List, Math, Reservoir Sampling, Randomized
