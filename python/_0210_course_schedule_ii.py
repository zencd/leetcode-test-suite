# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
# Medium

import unittest
from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        raise Exception("Not solved yet")


def is_valid_order(
    numCourses: int, prerequisites: List[List[int]], order: List[int]
) -> bool:
    if sorted(order) != list(range(numCourses)):
        return False
    pos = {course: i for i, course in enumerate(order)}
    return all(pos[b] < pos[a] for a, b in prerequisites)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.findOrder(2, [[1, 0]]), [0, 1])

    def test_example2(self):
        self.assertTrue(
            is_valid_order(
                4,
                [[1, 0], [2, 0], [3, 1], [3, 2]],
                self.sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
            )
        )

    def test_example3_single_course_no_prereq(self):
        self.assertEqual(self.sol.findOrder(1, []), [0])

    def test_cycle_returns_empty(self):
        self.assertEqual(self.sol.findOrder(2, [[1, 0], [0, 1]]), [])

    def test_self_inclusive_cycle_of_three(self):
        self.assertEqual(self.sol.findOrder(3, [[0, 1], [1, 2], [2, 0]]), [])

    def test_cycle_with_tail(self):
        self.assertEqual(self.sol.findOrder(4, [[1, 0], [2, 1], [1, 2], [3, 0]]), [])

    def test_no_prerequisites(self):
        result = self.sol.findOrder(4, [])
        self.assertTrue(is_valid_order(4, [], result))

    def test_linear_chain(self):
        prereq = [[i + 1, i] for i in range(4)]
        self.assertEqual(self.sol.findOrder(5, prereq), [0, 1, 2, 3, 4])

    def test_reverse_linear_chain(self):
        prereq = [[i - 1, i] for i in range(1, 5)]
        result = self.sol.findOrder(5, prereq)
        self.assertTrue(is_valid_order(5, prereq, result))

    def test_diamond(self):
        prereq = [[1, 0], [2, 0], [3, 1], [3, 2]]
        result = self.sol.findOrder(4, prereq)
        self.assertTrue(is_valid_order(4, prereq, result))

    def test_disconnected_components(self):
        prereq = [[1, 0], [3, 2]]
        result = self.sol.findOrder(4, prereq)
        self.assertTrue(is_valid_order(4, prereq, result))

    def test_single_prerequisite_pair(self):
        self.assertEqual(self.sol.findOrder(2, [[0, 1]]), [1, 0])

    def test_large_fully_ordered_reverse(self):
        n = 100
        prereq = [[i - 1, i] for i in range(1, n)]
        result = self.sol.findOrder(n, prereq)
        self.assertTrue(is_valid_order(n, prereq, result))

    def test_large_cycle_all_in_cycle(self):
        n = 10
        prereq = [[(i + 1) % n, i] for i in range(n)]
        self.assertEqual(self.sol.findOrder(n, prereq), [])

    def test_two_cycles_disjoint(self):
        self.assertEqual(self.sol.findOrder(4, [[1, 0], [0, 1], [3, 2], [2, 3]]), [])

    def test_all_independent_two_pairs_same_source(self):
        prereq = [[1, 0], [2, 0], [3, 0]]
        result = self.sol.findOrder(4, prereq)
        self.assertTrue(is_valid_order(4, prereq, result))
        self.assertEqual(result[0], 0)

    def test_result_contains_all_courses_once(self):
        prereq = [[1, 2], [2, 3], [0, 1]]
        result = self.sol.findOrder(4, prereq)
        self.assertEqual(len(result), 4)
        self.assertEqual(len(set(result)), 4)


if __name__ == "__main__":
    unittest.main()

# Tags: Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort
