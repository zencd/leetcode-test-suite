# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/
# Medium

from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_no_prerequisites_single_course(self):
        self.assertTrue(self.sol.canFinish(1, []))

    def test_no_prerequisites_multiple_courses(self):
        self.assertTrue(self.sol.canFinish(3, []))

    def test_simple_chain(self):
        self.assertTrue(self.sol.canFinish(2, [[1, 0]]))

    def test_example1(self):
        self.assertTrue(self.sol.canFinish(2, [[1, 0]]))

    def test_example2_cycle(self):
        self.assertFalse(self.sol.canFinish(2, [[1, 0], [0, 1]]))

    def test_self_loop(self):
        self.assertFalse(self.sol.canFinish(1, [[0, 0]]))

    def test_self_loop_among_others(self):
        self.assertFalse(self.sol.canFinish(3, [[0, 0], [1, 0]]))

    def test_three_course_chain(self):
        self.assertTrue(self.sol.canFinish(3, [[1, 0], [2, 1]]))

    def test_fork_diamond(self):
        self.assertTrue(self.sol.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

    def test_three_cycle(self):
        self.assertFalse(self.sol.canFinish(3, [[0, 1], [1, 2], [2, 0]]))

    def test_cycle_subset(self):
        self.assertFalse(self.sol.canFinish(4, [[1, 0], [0, 2], [2, 1]]))

    def test_disconnected_with_cycle(self):
        self.assertFalse(self.sol.canFinish(6, [[1, 0], [2, 3], [3, 4], [4, 2]]))

    def test_disconnected_without_cycle(self):
        self.assertTrue(self.sol.canFinish(6, [[1, 0], [2, 3], [4, 3]]))

    def test_all_courses_dependent(self):
        n = 5
        prereq = [[1, 0], [2, 0], [3, 2], [4, 3]]
        self.assertTrue(self.sol.canFinish(n, prereq))

    def test_cycle_of_two_in_middle(self):
        self.assertFalse(
            self.sol.canFinish(5, [[0, 1], [2, 0], [1, 2], [3, 0], [4, 3]])
        )

    def test_large_chain(self):
        n = 2000
        prereq = [[i, i - 1] for i in range(1, n)]
        self.assertTrue(self.sol.canFinish(n, prereq))

    def test_large_cycle(self):
        n = 2000
        prereq = [[i, (i + 1) % n] for i in range(n)]
        self.assertFalse(self.sol.canFinish(n, prereq))

    def test_single_course_with_invalid_self_dep(self):
        self.assertFalse(self.sol.canFinish(1, [[0, 0]]))

    def test_two_courses_no_dep(self):
        self.assertTrue(self.sol.canFinish(2, []))

    def test_prereq_order_insensitive(self):
        self.assertTrue(self.sol.canFinish(3, [[2, 0], [1, 0], [2, 1]]))


if __name__ == "__main__":
    unittest.main()

# Tags: Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Directed Acyclic Graph
